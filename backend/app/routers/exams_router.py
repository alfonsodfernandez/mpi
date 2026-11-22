"""Router del Simulador de Exámenes UFV (Ordinaria 90m, Extraordinaria 105m, Express 35m) con generación procedural."""
from __future__ import annotations

import json
import uuid
from datetime import timedelta, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..auth import AuthContext, get_current_auth
from ..database import get_db
from ..math_engine.registry import EXAM_BLUEPRINTS, TOPIC_LABELS, generate_exam_questions
from ..math_engine.utils import grade_answer
from ..models import ExamQuestion, ExamSession, utcnow
from ..schemas import (
    ExamQuestionPublic,
    ExamQuestionReview,
    ExamResultResponse,
    FinalizeExamRequest,
    SaveExamAnswerRequest,
    StartExamRequest,
    StartExamResponse,
)

router = APIRouter(prefix="/api/exams", tags=["exams"])


@router.get("/modes")
def exam_modes(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    return {
        "modes": [
            {
                "mode": "express",
                "title": EXAM_BLUEPRINTS["express"]["title"],
                "questions_count": len(EXAM_BLUEPRINTS["express"]["slots"]),
                "duration_minutes": EXAM_BLUEPRINTS["express"]["time_limit_seconds"] // 60,
                "description": "Evaluación rápida de 1 pregunta procedural por cada uno de los 5 bloques del temario (2 ptos/preg).",
            },
            {
                "mode": "ordinaria",
                "title": EXAM_BLUEPRINTS["ordinaria"]["title"],
                "questions_count": len(EXAM_BLUEPRINTS["ordinaria"]["slots"]),
                "duration_minutes": EXAM_BLUEPRINTS["ordinaria"]["time_limit_seconds"] // 60,
                "description": "Estructura idéntica al examen teórico oficial de Convocatoria Ordinaria 2025/26 (9 preguntas sobre 10 puntos, 90 min).",
            },
            {
                "mode": "extraordinaria",
                "title": EXAM_BLUEPRINTS["extraordinaria"]["title"],
                "questions_count": len(EXAM_BLUEPRINTS["extraordinaria"]["slots"]),
                "duration_minutes": EXAM_BLUEPRINTS["extraordinaria"]["time_limit_seconds"] // 60,
                "description": "Estructura oficial de Convocatoria Extraordinaria 2025/26 incluyendo parámetros, LU, cambios de base, autovectores y MATLAB (105 min).",
            },
        ]
    }


@router.post("/start", response_model=StartExamResponse)
def start_exam(
    payload: StartExamRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    """Genera un simulacro completo con problemas únicos; NO incluye soluciones en la respuesta."""
    blueprint, items = generate_exam_questions(db, ctx.user.id, payload.mode)
    now = utcnow()
    exam_id = str(uuid.uuid4())
    time_limit = blueprint["time_limit_seconds"]
    expires_at = now + timedelta(seconds=time_limit)

    exam = ExamSession(
        id=exam_id,
        user_id=ctx.user.id,
        session_id=ctx.session_id,
        mode=payload.mode,
        title=blueprint["title"],
        total_questions=len(items),
        time_limit_seconds=time_limit,
        status="active",
        started_at=now,
        expires_at=expires_at,
    )
    db.add(exam)

    public_questions: list[ExamQuestionPublic] = []
    for idx, (ex, weight) in enumerate(items, start=1):
        qid = str(uuid.uuid4())
        q = ExamQuestion(
            id=qid,
            exam_id=exam_id,
            question_index=idx,
            topic=ex["topic"],
            generator_id=ex["generator_id"],
            title=ex["title"],
            points_weight=weight,
            prompt_json=json.dumps(ex["prompt"], ensure_ascii=False),
            solution_json=json.dumps(ex["solution"], ensure_ascii=False),
        )
        db.add(q)
        public_questions.append(
            ExamQuestionPublic(
                question_id=qid,
                question_index=idx,
                topic=q.topic,
                topic_label=TOPIC_LABELS.get(q.topic, q.topic),
                title=q.title,
                points_weight=weight,
                prompt=ex["prompt"],
                answered=False,
                saved_answer=None,
            )
        )

    db.commit()

    wm = f"{ctx.user.display_name.upper()} · {now.strftime('%Y-%m-%d %H:%M:%S UTC')} · EXAMEN {payload.mode.upper()} · ID#{exam_id[:8]}"
    return StartExamResponse(
        exam_id=exam_id,
        mode=exam.mode,
        title=exam.title,
        total_questions=exam.total_questions,
        time_limit_seconds=exam.time_limit_seconds,
        started_at=exam.started_at,
        expires_at=exam.expires_at,
        watermark_text=wm,
        questions=public_questions,
    )


@router.put("/{exam_id}/questions/{question_id}")
def save_exam_answer(
    exam_id: str,
    question_id: str,
    payload: SaveExamAnswerRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    exam = db.get(ExamSession, exam_id)
    if exam is None or exam.user_id != ctx.user.id:
        raise HTTPException(status_code=404, detail="Examen no encontrado.")
    if exam.status != "active":
        raise HTTPException(status_code=409, detail="Este simulacro ya no está activo.")

    q = db.get(ExamQuestion, question_id)
    if q is None or q.exam_id != exam.id:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada.")

    q.user_answer_json = json.dumps(payload.answer, ensure_ascii=False)
    q.answered_at = utcnow()
    db.commit()
    return {"saved": True, "question_id": question_id}


def _build_exam_result(exam: ExamSession, feedbacks: dict[str, str] | None = None) -> ExamResultResponse:
    reviews: list[ExamQuestionReview] = []
    for q in exam.questions:
        sol = json.loads(q.solution_json)
        prompt = json.loads(q.prompt_json)
        u_ans = json.loads(q.user_answer_json) if q.user_answer_json else None
        fb = (feedbacks or {}).get(q.id)
        if fb is None:
            _, _, fb = grade_answer(u_ans, sol, timed_out=(u_ans is None and exam.status == "timeout"))
        reviews.append(
            ExamQuestionReview(
                question_id=q.id,
                question_index=q.question_index,
                topic=q.topic,
                topic_label=TOPIC_LABELS.get(q.topic, q.topic),
                title=q.title,
                points_weight=q.points_weight,
                points_earned=q.points_earned,
                is_correct=bool(q.is_correct),
                user_answer=u_ans,
                correct_display=sol["correct_display"],
                feedback=fb,
                steps_md=sol["steps_md"],
                theory_ref=sol["theory_ref"],
                prompt=prompt,
            )
        )
    return ExamResultResponse(
        exam_id=exam.id,
        mode=exam.mode,
        title=exam.title,
        status=exam.status,
        score_10=exam.score_10,
        correct_count=exam.correct_count,
        total_questions=exam.total_questions,
        time_spent_seconds=exam.time_spent_seconds or 0,
        questions=reviews,
    )


@router.post("/{exam_id}/finalize", response_model=ExamResultResponse)
def finalize_exam(
    exam_id: str,
    payload: FinalizeExamRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    exam = db.get(ExamSession, exam_id)
    if exam is None or exam.user_id != ctx.user.id:
        raise HTTPException(status_code=404, detail="Examen no encontrado.")
    if exam.status == "invalidated":
        raise HTTPException(status_code=409, detail="Examen invalidado por infracción de seguridad.")
    if exam.status in {"completed", "timeout"}:
        return _build_exam_result(exam)

    now = utcnow()
    started = exam.started_at
    if started.tzinfo is None:
        started = started.replace(tzinfo=timezone.utc)
    expires = exam.expires_at
    if expires.tzinfo is None:
        expires = expires.replace(tzinfo=timezone.utc)

    server_timed_out = payload.timed_out or (now > expires + timedelta(seconds=10))
    time_spent = max(1, min(exam.time_limit_seconds, int((now - started).total_seconds())))

    total_weight = sum(q.points_weight for q in exam.questions) or 1.0
    earned_weight = 0.0
    correct_count = 0
    feedbacks: dict[str, str] = {}

    submitted_map = payload.answers or {}
    for q in exam.questions:
        if q.id in submitted_map:
            q.user_answer_json = json.dumps(submitted_map[q.id], ensure_ascii=False)
            q.answered_at = now
        u_ans = json.loads(q.user_answer_json) if q.user_answer_json else None
        sol = json.loads(q.solution_json)
        is_ok, frac_score, fb = grade_answer(u_ans, sol, timed_out=(u_ans is None and server_timed_out))
        q.is_correct = is_ok
        q.points_earned = round(q.points_weight * frac_score, 3)
        earned_weight += q.points_earned
        if is_ok:
            correct_count += 1
        feedbacks[q.id] = fb

    exam.status = "timeout" if server_timed_out else "completed"
    exam.correct_count = correct_count
    exam.score_10 = round((earned_weight / total_weight) * 10.0, 2)
    exam.finished_at = now
    exam.time_spent_seconds = time_spent
    db.commit()
    db.refresh(exam)

    return _build_exam_result(exam, feedbacks=feedbacks)


@router.get("/history")
def exam_history(ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)):
    rows = db.execute(
        select(ExamSession)
        .where(ExamSession.user_id == ctx.user.id)
        .order_by(ExamSession.started_at.desc())
        .limit(30)
    ).scalars().all()

    return {
        "exams": [
            {
                "exam_id": e.id,
                "mode": e.mode,
                "title": e.title,
                "status": e.status,
                "score_10": e.score_10,
                "correct_count": e.correct_count,
                "total_questions": e.total_questions,
                "time_spent_seconds": e.time_spent_seconds,
                "invalidation_reason": e.invalidation_reason,
                "started_at": e.started_at.isoformat(),
                "can_review": e.status in {"completed", "timeout"},
            }
            for e in rows
        ]
    }


@router.get("/{exam_id}/review", response_model=ExamResultResponse)
def review_exam(exam_id: str, ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)):
    exam = db.get(ExamSession, exam_id)
    if exam is None or (exam.user_id != ctx.user.id and ctx.user.role != "admin"):
        raise HTTPException(status_code=404, detail="Examen no encontrado.")
    if exam.status not in {"completed", "timeout"}:
        raise HTTPException(
            status_code=403,
            detail="La revisión solo está disponible para exámenes entregados o finalizados por tiempo.",
        )
    return _build_exam_result(exam)
