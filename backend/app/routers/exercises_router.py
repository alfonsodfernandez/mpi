"""Router del Motor de Ejercicios Procedurales Infinitos con bloqueo estricto de soluciones."""
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
from ..math_engine.registry import TOPIC_LABELS, generate_unique_exercise, list_catalog
from ..math_engine.utils import grade_answer
from ..models import ExerciseAttempt, utcnow
from ..schemas import (
    ExerciseFeedbackResponse,
    PublicExerciseResponse,
    StartExerciseRequest,
    SubmitExerciseRequest,
)

router = APIRouter(prefix="/api/exercises", tags=["exercises"])


@router.get("/catalog")
def exercises_catalog(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    return {"topics": list_catalog()}


@router.post("/start", response_model=PublicExerciseResponse)
def start_exercise(
    payload: StartExerciseRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    """Genera un ejercicio 100% único y devuelve SOLO el enunciado (JAMÁS la solución)."""
    ex = generate_unique_exercise(
        db=db,
        user_id=ctx.user.id,
        topic=payload.topic,
        generator_id=payload.generator_id,
        difficulty=payload.difficulty,
    )
    now = utcnow()
    expires_at = now + timedelta(seconds=ex["time_limit_seconds"])
    attempt_id = str(uuid.uuid4())

    attempt = ExerciseAttempt(
        id=attempt_id,
        user_id=ctx.user.id,
        session_id=ctx.session_id,
        topic=ex["topic"],
        generator_id=ex["generator_id"],
        title=ex["title"],
        difficulty=ex["difficulty"],
        time_limit_seconds=ex["time_limit_seconds"],
        prompt_json=json.dumps(ex["prompt"], ensure_ascii=False),
        solution_json=json.dumps(ex["solution"], ensure_ascii=False),
        status="active",
        started_at=now,
        expires_at=expires_at,
    )
    db.add(attempt)
    db.commit()

    wm = f"{ctx.user.display_name.upper()} · {now.strftime('%Y-%m-%d %H:%M:%S UTC')} · MPI-I · ID#{attempt_id[:8]}"
    return PublicExerciseResponse(
        attempt_id=attempt_id,
        topic=attempt.topic,
        topic_label=TOPIC_LABELS.get(attempt.topic, attempt.topic),
        generator_id=attempt.generator_id,
        title=attempt.title,
        difficulty=attempt.difficulty,
        time_limit_seconds=attempt.time_limit_seconds,
        started_at=attempt.started_at,
        expires_at=attempt.expires_at,
        prompt=ex["prompt"],
        watermark_text=wm,
    )


@router.post("/{attempt_id}/submit", response_model=ExerciseFeedbackResponse)
def submit_exercise(
    attempt_id: str,
    payload: SubmitExerciseRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    """Evalúa la respuesta en el servidor con SymPy y libera la resolución paso a paso SOLO tras entrega o timeout."""
    attempt = db.get(ExerciseAttempt, attempt_id)
    if attempt is None or attempt.user_id != ctx.user.id:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado.")

    if attempt.status == "invalidated":
        raise HTTPException(
            status_code=409,
            detail="Este ejercicio fue invalidado por una infracción de seguridad. Debes generar uno nuevo.",
        )

    solution = json.loads(attempt.solution_json)

    if attempt.status in {"submitted", "timeout"}:
        # Ya fue entregado: devolvemos su corrección guardada
        return ExerciseFeedbackResponse(
            attempt_id=attempt.id,
            status=attempt.status,
            is_correct=bool(attempt.is_correct),
            score=attempt.score,
            time_spent_seconds=attempt.time_spent_seconds or 0,
            feedback="Ejercicio ya corregido anteriormente.",
            correct_display=solution["correct_display"],
            steps_md=solution["steps_md"],
            theory_ref=solution["theory_ref"],
        )

    now = utcnow()
    started = attempt.started_at
    if started.tzinfo is None:
        started = started.replace(tzinfo=timezone.utc)
    expires = attempt.expires_at
    if expires.tzinfo is None:
        expires = expires.replace(tzinfo=timezone.utc)

    # Verificación estricta de tiempo en el servidor (margen de 6s por latencia de red)
    server_timed_out = payload.timed_out or (now > expires + timedelta(seconds=6))
    time_spent = max(1, min(attempt.time_limit_seconds, int((now - started).total_seconds())))

    is_correct, score, feedback = grade_answer(payload.answer, solution, timed_out=server_timed_out)

    attempt.status = "timeout" if server_timed_out else "submitted"
    attempt.user_answer_json = json.dumps(payload.answer, ensure_ascii=False)
    attempt.is_correct = is_correct
    attempt.score = score
    attempt.submitted_at = now
    attempt.time_spent_seconds = time_spent
    db.commit()

    return ExerciseFeedbackResponse(
        attempt_id=attempt.id,
        status=attempt.status,
        is_correct=is_correct,
        score=score,
        time_spent_seconds=time_spent,
        feedback=feedback,
        correct_display=solution["correct_display"],
        steps_md=solution["steps_md"],
        theory_ref=solution["theory_ref"],
    )


@router.get("/history")
def exercise_history(
    limit: int = 20,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    rows = db.execute(
        select(ExerciseAttempt)
        .where(
            ExerciseAttempt.user_id == ctx.user.id,
            ExerciseAttempt.status.in_(["submitted", "timeout", "invalidated"]),
        )
        .order_by(ExerciseAttempt.started_at.desc())
        .limit(min(limit, 100))
    ).scalars().all()

    return {
        "attempts": [
            {
                "attempt_id": a.id,
                "topic": a.topic,
                "topic_label": TOPIC_LABELS.get(a.topic, a.topic),
                "title": a.title,
                "difficulty": a.difficulty,
                "status": a.status,
                "is_correct": a.is_correct,
                "score": a.score,
                "time_spent_seconds": a.time_spent_seconds,
                "time_limit_seconds": a.time_limit_seconds,
                "started_at": a.started_at.isoformat(),
            }
            for a in rows
        ]
    }
