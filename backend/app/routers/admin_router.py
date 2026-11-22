"""Router del Panel de Administración y Analítica del Profesor (/api/admin/*)."""
from __future__ import annotations

import csv
import io
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import APIRouter, Depends, Query
from fastapi.responses import Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..auth import AuthContext, require_admin
from ..content.indexer import get_course_index
from ..database import get_db
from ..math_engine.registry import GENERATORS, TOPIC_LABELS
from ..models import (
    ChecklistProgress,
    ExamQuestion,
    ExamSession,
    ExerciseAttempt,
    StudyNote,
    StudySession,
    User,
    ViolationLog,
)
from .auth_router import _compute_streak

router = APIRouter(prefix="/api/admin", tags=["admin"])


def _get_student_user(db: Session) -> User | None:
    return db.execute(select(User).where(User.role == "student")).scalar_one_or_none()


def _collect_admin_report(db: Session) -> dict[str, Any]:
    student = _get_student_user(db)
    if student is None:
        return {"student": None, "kpis": {}, "sessions": [], "violations": [], "topic_analytics": [], "weak_spots": [], "exams": [], "daily_activity": []}

    uid = student.id
    sessions = db.execute(
        select(StudySession).where(StudySession.user_id == uid).order_by(StudySession.started_at.desc())
    ).scalars().all()

    violations = db.execute(
        select(ViolationLog).where(ViolationLog.user_id == uid).order_by(ViolationLog.created_at.desc())
    ).scalars().all()

    attempts = db.execute(
        select(ExerciseAttempt).where(ExerciseAttempt.user_id == uid).order_by(ExerciseAttempt.started_at.desc())
    ).scalars().all()

    exams = db.execute(
        select(ExamSession).where(ExamSession.user_id == uid).order_by(ExamSession.started_at.desc())
    ).scalars().all()

    exam_questions = db.execute(
        select(ExamQuestion)
        .join(ExamSession, ExamQuestion.exam_id == ExamSession.id)
        .where(ExamSession.user_id == uid, ExamSession.status.in_(["completed", "timeout"]))
    ).scalars().all()

    # KPIs de sesiones y tiempo efectivo
    now = datetime.now(timezone.utc)
    total_sessions = len(sessions)
    total_active_seconds = sum(s.active_seconds for s in sessions)

    session_rows = []
    total_wall_seconds = 0
    live_session = None
    for s in sessions:
        st = s.started_at.replace(tzinfo=timezone.utc) if s.started_at.tzinfo is None else s.started_at
        end_ref = s.ended_at or s.last_seen_at
        en = end_ref.replace(tzinfo=timezone.utc) if end_ref.tzinfo is None else end_ref
        wall = max(0, int((en - st).total_seconds()))
        total_wall_seconds += wall
        is_online = bool(s.is_active and (now - en).total_seconds() < 120)
        if is_online and live_session is None:
            live_session = {"session_id": s.id, "current_view": s.current_view, "ip_address": s.ip_address, "last_seen_at": en.isoformat()}
        session_rows.append(
            {
                "id": s.id,
                "started_at": st.isoformat(),
                "last_seen_at": en.isoformat(),
                "ended_at": s.ended_at.isoformat() if s.ended_at else None,
                "ip_address": s.ip_address,
                "device_summary": s.device_summary,
                "user_agent": s.user_agent,
                "wall_seconds": wall,
                "active_seconds": s.active_seconds,
                "current_view": s.current_view,
                "is_active": s.is_active,
                "is_online": is_online,
            }
        )

    streak_current, streak_best = _compute_streak([s.started_at for s in sessions])

    # Analítica por tema (combinando ejercicios sueltos + preguntas de exámenes finalizados)
    topic_stats: dict[str, dict[str, Any]] = {
        t: {
            "topic": t,
            "label": lbl,
            "attempts": 0,
            "correct": 0,
            "failed": 0,
            "timeouts": 0,
            "invalidated": 0,
            "accuracy_pct": 0.0,
            "avg_seconds": 0.0,
            "_time_sum": 0,
            "_time_cnt": 0,
        }
        for t, lbl in TOPIC_LABELS.items()
    }

    gen_stats: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"generator_id": "", "topic": "", "label": "", "attempts": 0, "correct": 0, "timeouts": 0, "time_sum": 0, "time_cnt": 0}
    )

    graded_attempts = [a for a in attempts if a.status in {"submitted", "timeout"}]
    for a in attempts:
        b = topic_stats.get(a.topic)
        if b is None:
            continue
        if a.status == "invalidated":
            b["invalidated"] += 1
            continue
        if a.status not in {"submitted", "timeout"}:
            continue
        b["attempts"] += 1
        if a.is_correct:
            b["correct"] += 1
        else:
            b["failed"] += 1
        if a.status == "timeout":
            b["timeouts"] += 1
        if a.time_spent_seconds:
            b["_time_sum"] += a.time_spent_seconds
            b["_time_cnt"] += 1

        gs = gen_stats[a.generator_id]
        gs["generator_id"] = a.generator_id
        gs["topic"] = a.topic
        gs["label"] = GENERATORS.get(a.generator_id, {}).get("label", a.title)
        gs["attempts"] += 1
        if a.is_correct:
            gs["correct"] += 1
        if a.status == "timeout":
            gs["timeouts"] += 1
        if a.time_spent_seconds:
            gs["time_sum"] += a.time_spent_seconds
            gs["time_cnt"] += 1

    # Añadir preguntas de exámenes completados a las métricas por tema
    for q in exam_questions:
        b = topic_stats.get(q.topic)
        if b is None:
            continue
        b["attempts"] += 1
        if q.is_correct:
            b["correct"] += 1
        else:
            b["failed"] += 1
        gs = gen_stats[q.generator_id]
        gs["generator_id"] = q.generator_id
        gs["topic"] = q.topic
        gs["label"] = GENERATORS.get(q.generator_id, {}).get("label", q.title)
        gs["attempts"] += 1
        if q.is_correct:
            gs["correct"] += 1

    topic_analytics = []
    total_q = 0
    total_ok = 0
    total_time_sum = 0
    total_time_cnt = 0
    for b in topic_stats.values():
        b["accuracy_pct"] = round(b["correct"] / b["attempts"] * 100.0, 1) if b["attempts"] else 0.0
        b["avg_seconds"] = round(b["_time_sum"] / b["_time_cnt"], 1) if b["_time_cnt"] else 0.0
        total_q += b["attempts"]
        total_ok += b["correct"]
        total_time_sum += b["_time_sum"]
        total_time_cnt += b["_time_cnt"]
        topic_analytics.append({k: v for k, v in b.items() if not k.startswith("_")})

    # Detección automática de puntos débiles
    weak_spots = []
    for gs in gen_stats.values():
        if gs["attempts"] == 0:
            continue
        acc = round(gs["correct"] / gs["attempts"] * 100.0, 1)
        avg_s = round(gs["time_sum"] / gs["time_cnt"], 1) if gs["time_cnt"] else 0.0
        if acc < 70.0 or gs["timeouts"] > 0:
            weak_spots.append(
                {
                    "generator_id": gs["generator_id"],
                    "topic": gs["topic"],
                    "topic_label": TOPIC_LABELS.get(gs["topic"], gs["topic"]),
                    "label": gs["label"],
                    "attempts": gs["attempts"],
                    "accuracy_pct": acc,
                    "timeouts": gs["timeouts"],
                    "avg_seconds": avg_s,
                    "recommendation": (
                        "Reforzar velocidad bajo presión de tiempo y repasar procedimiento base."
                        if gs["timeouts"] > 0 and acc >= 50
                        else "Punto crítico prioritario: repasar teoría y realizar 3 ejercicios guiados de este bloque."
                    ),
                }
            )
    weak_spots.sort(key=lambda x: (x["accuracy_pct"], -x["attempts"]))

    # Actividad diaria últimos 14 días
    today = now.date()
    daily_map: dict[str, dict[str, Any]] = {}
    for offset in range(13, -1, -1):
        d = (today - timedelta(days=offset)).isoformat()
        daily_map[d] = {"date": d, "active_minutes": 0.0, "exercises": 0, "correct": 0, "violations": 0}

    for s in sessions:
        d = s.started_at.astimezone(timezone.utc).date().isoformat()
        if d in daily_map:
            daily_map[d]["active_minutes"] = round(daily_map[d]["active_minutes"] + s.active_seconds / 60.0, 1)
    for a in graded_attempts:
        d = a.started_at.astimezone(timezone.utc).date().isoformat()
        if d in daily_map:
            daily_map[d]["exercises"] += 1
            if a.is_correct:
                daily_map[d]["correct"] += 1
    for v in violations:
        d = v.created_at.astimezone(timezone.utc).date().isoformat()
        if d in daily_map:
            daily_map[d]["violations"] += 1

    # Checklist & Notas
    idx = get_course_index()
    total_checklist = sum(len(g["items"]) for g in idx["checklist"])
    done_checklist = len(
        db.execute(
            select(ChecklistProgress).where(
                ChecklistProgress.user_id == uid, ChecklistProgress.completed.is_(True)
            )
        ).scalars().all()
    )
    notes = db.execute(select(StudyNote).where(StudyNote.user_id == uid)).scalars().all()

    return {
        "generated_at": now.isoformat(),
        "student": {
            "username": student.username,
            "display_name": student.display_name,
            "last_login_at": student.last_login_at.isoformat() if student.last_login_at else None,
            "live_session": live_session,
        },
        "kpis": {
            "total_accesses": total_sessions,
            "total_active_seconds": total_active_seconds,
            "total_wall_seconds": total_wall_seconds,
            "streak_current_days": streak_current,
            "streak_best_days": streak_best,
            "total_questions_answered": total_q,
            "overall_accuracy_pct": round(total_ok / total_q * 100.0, 1) if total_q else 0.0,
            "avg_seconds_per_question": round(total_time_sum / total_time_cnt, 1) if total_time_cnt else 0.0,
            "total_violations": len(violations),
            "high_severity_violations": sum(1 for v in violations if v.severity == "high"),
            "exams_completed": sum(1 for e in exams if e.status in {"completed", "timeout"}),
            "exams_invalidated": sum(1 for e in exams if e.status == "invalidated"),
            "avg_exam_score_10": round(
                sum(e.score_10 for e in exams if e.status in {"completed", "timeout"})
                / max(1, sum(1 for e in exams if e.status in {"completed", "timeout"})),
                2,
            )
            if any(e.status in {"completed", "timeout"} for e in exams)
            else 0.0,
            "checklist_done": done_checklist,
            "checklist_total": total_checklist,
        },
        "sessions": session_rows[:100],
        "violations": [
            {
                "id": v.id,
                "created_at": v.created_at.isoformat(),
                "violation_type": v.violation_type,
                "severity": v.severity,
                "context_mode": v.context_mode,
                "topic": v.topic,
                "topic_label": TOPIC_LABELS.get(v.topic, v.topic),
                "question_ref": v.question_ref,
                "details": v.details,
                "triggered_reset": v.triggered_reset,
                "ip_address": v.ip_address,
            }
            for v in violations[:200]
        ],
        "topic_analytics": topic_analytics,
        "weak_spots": weak_spots[:10],
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
                "finished_at": e.finished_at.isoformat() if e.finished_at else None,
            }
            for e in exams[:50]
        ],
        "recent_exercises": [
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
            for a in attempts[:80]
        ],
        "daily_activity": list(daily_map.values()),
        "notes_count": sum(1 for n in notes if n.content.strip()),
    }


@router.get("/dashboard")
def admin_dashboard(_ctx: AuthContext = Depends(require_admin), db: Session = Depends(get_db)) -> dict[str, Any]:
    return _collect_admin_report(db)


@router.get("/export")
def admin_export(
    format: str = Query(default="json", pattern="^(json|csv)$"),
    scope: str = Query(default="all", pattern="^(all|sessions|violations|exercises|exams)$"),
    _ctx: AuthContext = Depends(require_admin),
    db: Session = Depends(get_db),
):
    report = _collect_admin_report(db)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    if format == "json":
        body = json.dumps(report, ensure_ascii=False, indent=2)
        return Response(
            content=body.encode("utf-8"),
            media_type="application/json; charset=utf-8",
            headers={"Content-Disposition": f'attachment; filename="informe_pablo_mpi1_{stamp}.json"'},
        )

    # CSV UTF-8 con BOM para apertura limpia en Excel (es-ES)
    buf = io.StringIO()
    writer = csv.writer(buf)

    if scope in {"all", "sessions"}:
        writer.writerow(["=== SESIONES DE ESTUDIO ==="])
        writer.writerow(["ID", "Inicio UTC", "Fin/Última Actividad UTC", "IP", "Dispositivo", "Duración Total (s)", "Tiempo Activo (s)", "Vista Actual"])
        for s in report["sessions"]:
            writer.writerow([s["id"], s["started_at"], s["ended_at"] or s["last_seen_at"], s["ip_address"], s["device_summary"], s["wall_seconds"], s["active_seconds"], s["current_view"]])
        writer.writerow([])

    if scope in {"all", "violations"}:
        writer.writerow(["=== REGISTRO ANTI-TRAMPAS (INFRACCIONES) ==="])
        writer.writerow(["ID", "Fecha UTC", "Tipo", "Severidad", "Modo", "Tema", "Pregunta", "Reinicio Forzado", "IP", "Detalles"])
        for v in report["violations"]:
            writer.writerow([v["id"], v["created_at"], v["violation_type"], v["severity"], v["context_mode"], v["topic_label"], v["question_ref"], "SI" if v["triggered_reset"] else "NO", v["ip_address"], v["details"]])
        writer.writerow([])

    if scope in {"all", "exercises"}:
        writer.writerow(["=== ANALÍTICA POR TEMA ==="])
        writer.writerow(["Tema", "Intentos", "Aciertos", "Fallos", "Timeouts", "Invalidadas", "% Acierto", "Tiempo Medio (s)"])
        for t in report["topic_analytics"]:
            writer.writerow([t["label"], t["attempts"], t["correct"], t["failed"], t["timeouts"], t["invalidated"], t["accuracy_pct"], t["avg_seconds"]])
        writer.writerow([])
        writer.writerow(["=== HISTORIAL DE EJERCICIOS ==="])
        writer.writerow(["ID", "Fecha UTC", "Tema", "Título", "Dificultad", "Estado", "Correcto", "Puntuación", "Tiempo (s)"])
        for a in report["recent_exercises"]:
            writer.writerow([a["attempt_id"], a["started_at"], a["topic_label"], a["title"], a["difficulty"], a["status"], a["is_correct"], a["score"], a["time_spent_seconds"]])
        writer.writerow([])

    if scope in {"all", "exams"}:
        writer.writerow(["=== SIMULACROS DE EXAMEN ==="])
        writer.writerow(["ID", "Fecha UTC", "Modalidad", "Título", "Estado", "Nota /10", "Aciertos", "Total", "Tiempo (s)", "Motivo Invalidación"])
        for e in report["exams"]:
            writer.writerow([e["exam_id"], e["started_at"], e["mode"], e["title"], e["status"], e["score_10"], e["correct_count"], e["total_questions"], e["time_spent_seconds"], e["invalidation_reason"] or ""])

    csv_bytes = ("\ufeff" + buf.getvalue()).encode("utf-8")
    return Response(
        content=csv_bytes,
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="informe_pablo_mpi1_{scope}_{stamp}.csv"'},
    )
