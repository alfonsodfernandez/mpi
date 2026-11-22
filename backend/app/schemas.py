"""Esquemas Pydantic v2. Garantiza separación estricta entre enunciado público y solución secreta."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=64)
    password: str = Field(..., min_length=1, max_length=128)


class UserPublic(BaseModel):
    id: int
    username: str
    display_name: str
    role: str
    session_id: str


class LoginResponse(BaseModel):
    token: str
    user: UserPublic


class HeartbeatRequest(BaseModel):
    delta_seconds: int = Field(default=0, ge=0, le=60)
    is_active: bool = True
    current_view: str = Field(default="home", max_length=64)


class NoteUpdateRequest(BaseModel):
    content: str = Field(default="", max_length=20000)


class ChecklistToggleRequest(BaseModel):
    completed: bool


# --- Ejercicios Procedurales ---

class StartExerciseRequest(BaseModel):
    topic: str = Field(default="random", max_length=48)
    generator_id: str | None = Field(default=None, max_length=64)
    difficulty: str | None = Field(default=None, max_length=24)


class PublicExerciseResponse(BaseModel):
    """Respuesta al iniciar un ejercicio: CERO campos de solución o pasos."""
    attempt_id: str
    topic: str
    topic_label: str
    generator_id: str
    title: str
    difficulty: str
    time_limit_seconds: int
    started_at: datetime
    expires_at: datetime
    prompt: dict[str, Any]  # statement_md, math_blocks, protected_matrix, input_spec, hint_count
    watermark_text: str


class SubmitExerciseRequest(BaseModel):
    answer: Any = None
    timed_out: bool = False


class ExerciseFeedbackResponse(BaseModel):
    """Solo se devuelve DESPUÉS de enviar respuesta o agotar tiempo."""
    attempt_id: str
    status: str
    is_correct: bool
    score: float
    time_spent_seconds: int
    feedback: str
    correct_display: str
    steps_md: list[str]
    theory_ref: str


# --- Simulacro de Exámenes ---

class StartExamRequest(BaseModel):
    mode: str = Field(default="express", pattern="^(ordinaria|extraordinaria|express)$")


class ExamQuestionPublic(BaseModel):
    """Pregunta pública de examen: SIN solución."""
    question_id: str
    question_index: int
    topic: str
    topic_label: str
    title: str
    points_weight: float
    prompt: dict[str, Any]
    answered: bool
    saved_answer: Any = None


class StartExamResponse(BaseModel):
    exam_id: str
    mode: str
    title: str
    total_questions: int
    time_limit_seconds: int
    started_at: datetime
    expires_at: datetime
    watermark_text: str
    questions: list[ExamQuestionPublic]


class SaveExamAnswerRequest(BaseModel):
    answer: Any


class FinalizeExamRequest(BaseModel):
    timed_out: bool = False
    answers: dict[str, Any] | None = None


class ExamQuestionReview(BaseModel):
    question_id: str
    question_index: int
    topic: str
    topic_label: str
    title: str
    points_weight: float
    points_earned: float
    is_correct: bool
    user_answer: Any
    correct_display: str
    feedback: str
    steps_md: list[str]
    theory_ref: str
    prompt: dict[str, Any]


class ExamResultResponse(BaseModel):
    exam_id: str
    mode: str
    title: str
    status: str
    score_10: float
    correct_count: int
    total_questions: int
    time_spent_seconds: int
    questions: list[ExamQuestionReview]


# --- Seguridad / Anti-Trampas ---

class ViolationReportRequest(BaseModel):
    violation_type: str = Field(..., max_length=48)
    severity: str = Field(default="high", pattern="^(high|medium)$")
    context_mode: str = Field(default="practice", max_length=32)
    topic: str = Field(default="general", max_length=64)
    question_ref: str = Field(default="", max_length=160)
    details: str = Field(default="", max_length=1000)
    active_attempt_id: str | None = None
    active_exam_id: str | None = None
    trigger_reset: bool = True


class ViolationReportResponse(BaseModel):
    recorded: bool
    violation_id: int
    reset_enforced: bool
    message: str
