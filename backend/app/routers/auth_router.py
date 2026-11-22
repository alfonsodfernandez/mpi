"""Router de autenticación dual, seguimiento de sesiones activas (heartbeat) y resumen del alumno."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ..auth import (
    COOKIE_NAME,
    AuthContext,
    check_login_rate_limit,
    create_access_token,
    create_study_session,
    extract_client_ip,
    get_current_auth,
    record_failed_login,
    verify_password,
)
from ..config import settings
from ..content.indexer import get_course_index
from ..database import get_db
from ..math_engine.registry import TOPIC_LABELS
from ..models import ChecklistProgress, ExamSession, ExerciseAttempt, StudySession, User, utcnow
from ..schemas import HeartbeatRequest, LoginRequest, LoginResponse, UserPublic

router = APIRouter(prefix="/api", tags=["auth"])


def _compute_streak(session_dates: list[datetime]) -> tuple[int, int]:
    """Calcula (racha_actual, mejor_racha) en días consecutivos con actividad."""
    if not session_dates:
        return 0, 0
    days = sorted({dt.astimezone(timezone.utc).date() for dt in session_dates})
    best = 1
    run = 1
    for i in range(1, len(days)):
        if (days[i] - days[i - 1]).days == 1:
            run += 1
            best = max(best, run)
        else:
            run = 1
    today = datetime.now(timezone.utc).date()
    if (today - days[-1]).days > 1:
        current = 0
    else:
        current = 1
        for i in range(len(days) - 1, 0, -1):
            if (days[i] - days[i - 1]).days == 1:
                current += 1
            else:
                break
    return current, best


@router.post("/auth/login", response_model=LoginResponse)
def login(payload: LoginRequest, request: Request, response: Response, db: Session = Depends(get_db)):
    ip = extract_client_ip(request)
    check_login_rate_limit(ip)

    user = db.execute(select(User).where(User.username == payload.username.strip())).scalar_one_or_none()
    if user is None or not verify_password(payload.password, user.password_hash):
        record_failed_login(ip)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
        )

    sess = create_study_session(db, user, request)
    token = create_access_token(user.id, user.username, user.role, sess.id)

    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        samesite="lax",
        secure=settings.COOKIE_SECURE,
        max_age=settings.SESSION_EXPIRE_HOURS * 3600,
        path="/",
    )

    return LoginResponse(
        token=token,
        user=UserPublic(
            id=user.id,
            username=user.username,
            display_name=user.display_name,
            role=user.role,
            session_id=sess.id,
        ),
    )


@router.post("/auth/logout")
def logout(response: Response, ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)):
    sess = db.get(StudySession, ctx.session_id)
    if sess is not None and sess.is_active:
        sess.is_active = False
        sess.ended_at = utcnow()
        db.commit()
    response.delete_cookie(COOKIE_NAME, path="/")
    return {"ok": True}


@router.get("/auth/me", response_model=UserPublic)
def me(ctx: AuthContext = Depends(get_current_auth)):
    return UserPublic(
        id=ctx.user.id,
        username=ctx.user.username,
        display_name=ctx.user.display_name,
        role=ctx.user.role,
        session_id=ctx.session_id,
    )


@router.post("/auth/heartbeat")
def heartbeat(payload: HeartbeatRequest, ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)):
    sess = db.get(StudySession, ctx.session_id)
    if sess is None:
        raise HTTPException(status_code=404, detail="Sesión no encontrada.")

    now = utcnow()
    last_seen = sess.last_seen_at
    if last_seen.tzinfo is None:
        last_seen = last_seen.replace(tzinfo=timezone.utc)
    wall_elapsed = max(0, int((now - last_seen).total_seconds()))

    if payload.is_active and payload.delta_seconds > 0:
        # Solo acumulamos tiempo efectivo real acotado por tiempo de reloj transcurrido + margen
        credited = min(payload.delta_seconds, max(wall_elapsed + 2, 0), 45)
        sess.active_seconds += credited

    sess.last_seen_at = now
    sess.current_view = payload.current_view[:64]
    db.commit()
    return {"ok": True, "active_seconds": sess.active_seconds}


@router.get("/student/overview")
def student_overview(ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)) -> dict[str, Any]:
    uid = ctx.user.id
    sessions = db.execute(select(StudySession).where(StudySession.user_id == uid)).scalars().all()
    total_active_seconds = sum(s.active_seconds for s in sessions)
    today = datetime.now(timezone.utc).date()
    today_active_seconds = sum(
        s.active_seconds for s in sessions if s.started_at.astimezone(timezone.utc).date() == today
    )
    streak_current, streak_best = _compute_streak([s.started_at for s in sessions])

    attempts = db.execute(
        select(ExerciseAttempt).where(
            ExerciseAttempt.user_id == uid,
            ExerciseAttempt.status.in_(["submitted", "timeout"]),
        )
    ).scalars().all()

    by_topic: dict[str, dict[str, Any]] = {
        k: {"topic": k, "label": lbl, "total": 0, "correct": 0, "accuracy": 0.0}
        for k, lbl in TOPIC_LABELS.items()
    }
    for a in attempts:
        bucket = by_topic.get(a.topic)
        if bucket:
            bucket["total"] += 1
            if a.is_correct:
                bucket["correct"] += 1
    for b in by_topic.values():
        b["accuracy"] = round((b["correct"] / b["total"] * 100.0), 1) if b["total"] > 0 else 0.0

    total_done = len(attempts)
    total_correct = sum(1 for a in attempts if a.is_correct)
    overall_acc = round((total_correct / total_done * 100.0), 1) if total_done > 0 else 0.0

    exams = db.execute(
        select(ExamSession)
        .where(ExamSession.user_id == uid, ExamSession.status.in_(["completed", "timeout"]))
        .order_by(ExamSession.started_at.desc())
        .limit(5)
    ).scalars().all()

    idx = get_course_index()
    total_checklist = sum(len(g["items"]) for g in idx["checklist"])
    done_checklist = (
        db.execute(
            select(func.count(ChecklistProgress.id)).where(
                ChecklistProgress.user_id == uid, ChecklistProgress.completed.is_(True)
            )
        ).scalar()
        or 0
    )

    return {
        "display_name": ctx.user.display_name,
        "total_active_seconds": total_active_seconds,
        "today_active_seconds": today_active_seconds,
        "total_sessions": len(sessions),
        "streak_current": streak_current,
        "streak_best": streak_best,
        "exercises_completed": total_done,
        "overall_accuracy": overall_acc,
        "checklist_done": int(done_checklist),
        "checklist_total": total_checklist,
        "topic_mastery": list(by_topic.values()),
        "recent_exams": [
            {
                "exam_id": e.id,
                "mode": e.mode,
                "title": e.title,
                "score_10": e.score_10,
                "correct_count": e.correct_count,
                "total_questions": e.total_questions,
                "started_at": e.started_at.isoformat(),
                "status": e.status,
            }
            for e in exams
        ],
    }
