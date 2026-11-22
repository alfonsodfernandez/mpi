"""Router del Sistema Anti-Trampas: registro de infracciones e invalidación inmediata en servidor."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ..auth import AuthContext, extract_client_ip, get_current_auth
from ..database import get_db
from ..models import ExamSession, ExerciseAttempt, ViolationLog, utcnow
from ..schemas import ViolationReportRequest, ViolationReportResponse

router = APIRouter(prefix="/api/security", tags=["security"])

HIGH_SEVERITY_TYPES = {
    "EXIT_FULLSCREEN",
    "TAB_SWITCH",
    "WINDOW_BLUR",
    "DEVTOOLS_ATTEMPT",
    "SCREENSHOT_ATTEMPT",
}


@router.post("/violation", response_model=ViolationReportResponse)
def report_violation(
    payload: ViolationReportRequest,
    request: Request,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    """Registra la infracción en SQLite y, si procede, invalida al instante el ejercicio o examen en curso."""
    v_type = payload.violation_type.strip().upper()[:48]
    severity = "high" if v_type in HIGH_SEVERITY_TYPES else payload.severity
    enforce_reset = payload.trigger_reset or (v_type in HIGH_SEVERITY_TYPES)

    ip = extract_client_ip(request)
    log = ViolationLog(
        user_id=ctx.user.id,
        session_id=ctx.session_id,
        violation_type=v_type,
        severity=severity,
        context_mode=payload.context_mode[:32],
        topic=payload.topic[:64],
        question_ref=payload.question_ref[:160],
        details=payload.details[:1000],
        triggered_reset=enforce_reset,
        ip_address=ip,
        created_at=utcnow(),
    )
    db.add(log)

    if enforce_reset:
        if payload.active_attempt_id:
            att = db.get(ExerciseAttempt, payload.active_attempt_id)
            if att is not None and att.user_id == ctx.user.id and att.status == "active":
                att.status = "invalidated"
                att.is_correct = False
                att.score = 0.0
                att.submitted_at = utcnow()
        if payload.active_exam_id:
            ex = db.get(ExamSession, payload.active_exam_id)
            if ex is not None and ex.user_id == ctx.user.id and ex.status == "active":
                ex.status = "invalidated"
                ex.invalidation_reason = f"Infracción detectada: {v_type}"
                ex.finished_at = utcnow()

    db.commit()
    db.refresh(log)

    msg = (
        f"Infracción '{v_type}' registrada en auditoría. La sesión de prueba actual ha sido invalidada y se generarán nuevos problemas."
        if enforce_reset
        else f"Acción bloqueada ('{v_type}') y registrada en el historial de auditoría."
    )
    return ViolationReportResponse(
        recorded=True,
        violation_id=log.id,
        reset_enforced=enforce_reset,
        message=msg,
    )
