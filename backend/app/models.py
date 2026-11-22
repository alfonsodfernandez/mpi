"""Modelos ORM SQLite para usuarios, sesiones, ejercicios, exámenes, infracciones y notas."""
from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, index=True)  # "student" | "admin"
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    sessions: Mapped[list["StudySession"]] = relationship(back_populates="user")


class StudySession(Base):
    __tablename__ = "study_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, index=True)
    last_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    active_seconds: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(64), default="unknown")
    user_agent: Mapped[str] = mapped_column(String(512), default="")
    device_summary: Mapped[str] = mapped_column(String(160), default="Desconocido")
    current_view: Mapped[str] = mapped_column(String(64), default="home")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    user: Mapped["User"] = relationship(back_populates="sessions")


class GeneratedFingerprint(Base):
    """Registra la huella de cada ejercicio generado para garantizar que Pablo NUNCA repita problema."""
    __tablename__ = "generated_fingerprints"
    __table_args__ = (UniqueConstraint("user_id", "fingerprint", name="uq_user_fingerprint"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    generator_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    fingerprint: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class ExerciseAttempt(Base):
    """Instancia de ejercicio procedural. La solución SOLO vive en backend hasta entrega o timeout."""
    __tablename__ = "exercise_attempts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("study_sessions.id", ondelete="SET NULL"), nullable=True)
    topic: Mapped[str] = mapped_column(String(48), nullable=False, index=True)
    generator_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    difficulty: Mapped[str] = mapped_column(String(24), default="media")
    time_limit_seconds: Mapped[int] = mapped_column(Integer, nullable=False)

    # Datos públicos enviados al frontend
    prompt_json: Mapped[str] = mapped_column(Text, nullable=False)
    # Datos secretos (solución exacta, verificador, pasos en LaTeX) — NUNCA enviados antes de submit/timeout
    solution_json: Mapped[str] = mapped_column(Text, nullable=False)

    # Estado y respuesta del alumno
    status: Mapped[str] = mapped_column(
        String(24), default="active", nullable=False, index=True
    )  # active | submitted | timeout | invalidated
    user_answer_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    time_spent_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)


class ExamSession(Base):
    """Simulacro completo de examen UFV (CO / CEX / Express) generado dinámicamente."""
    __tablename__ = "exam_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("study_sessions.id", ondelete="SET NULL"), nullable=True)
    mode: Mapped[str] = mapped_column(String(32), nullable=False)  # ordinaria | extraordinaria | express
    title: Mapped[str] = mapped_column(String(180), nullable=False)
    total_questions: Mapped[int] = mapped_column(Integer, nullable=False)
    time_limit_seconds: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[str] = mapped_column(
        String(24), default="active", nullable=False, index=True
    )  # active | completed | timeout | invalidated
    score_10: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    correct_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    invalidation_reason: Mapped[str | None] = mapped_column(String(200), nullable=True)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    time_spent_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)

    questions: Mapped[list["ExamQuestion"]] = relationship(
        back_populates="exam", cascade="all, delete-orphan", order_by="ExamQuestion.question_index"
    )


class ExamQuestion(Base):
    """Pregunta individual dentro de un simulacro de examen."""
    __tablename__ = "exam_questions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    exam_id: Mapped[str] = mapped_column(ForeignKey("exam_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    question_index: Mapped[int] = mapped_column(Integer, nullable=False)
    topic: Mapped[str] = mapped_column(String(48), nullable=False, index=True)
    generator_id: Mapped[str] = mapped_column(String(64), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    points_weight: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)

    prompt_json: Mapped[str] = mapped_column(Text, nullable=False)
    solution_json: Mapped[str] = mapped_column(Text, nullable=False)

    user_answer_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    points_earned: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    time_spent_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)

    exam: Mapped["ExamSession"] = relationship(back_populates="questions")


class ViolationLog(Base):
    """Registro detallado de infracciones del sistema Anti-Trampas."""
    __tablename__ = "violation_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("study_sessions.id", ondelete="SET NULL"), nullable=True)
    violation_type: Mapped[str] = mapped_column(String(48), nullable=False, index=True)
    severity: Mapped[str] = mapped_column(String(16), default="high", nullable=False)  # high | medium
    context_mode: Mapped[str] = mapped_column(String(32), default="practice")  # practice | exam | matlab
    topic: Mapped[str] = mapped_column(String(64), default="general")
    question_ref: Mapped[str] = mapped_column(String(160), default="")
    details: Mapped[str] = mapped_column(Text, default="")
    triggered_reset: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(64), default="unknown")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, index=True)


class StudyNote(Base):
    """Bloc de notas rápido integrado por tema para Pablo."""
    __tablename__ = "study_notes"
    __table_args__ = (UniqueConstraint("user_id", "topic_key", name="uq_user_topic_note"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    topic_key: Mapped[str] = mapped_column(String(64), nullable=False)
    content: Mapped[str] = mapped_column(Text, default="", nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)


class ChecklistProgress(Base):
    """Progreso de Pablo en el checklist oficial 'Qué hay que saber de Álgebra'."""
    __tablename__ = "checklist_progress"
    __table_args__ = (UniqueConstraint("user_id", "item_id", name="uq_user_checklist_item"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    item_id: Mapped[str] = mapped_column(String(64), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)
