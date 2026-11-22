"""Router de contenidos indexados de _contexto_mpi/: Teoría, MATLAB, Red Logística, Checklist y Notas."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..auth import AuthContext, get_current_auth
from ..content.indexer import get_course_index, search_course_content
from ..content.logistics_analysis import CENTERS, analyze_network
from ..database import get_db
from ..models import ChecklistProgress, StudyNote, utcnow
from ..schemas import ChecklistToggleRequest, NoteUpdateRequest

router = APIRouter(prefix="/api", tags=["content"])


@router.get("/content/overview")
def content_overview(ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)) -> dict[str, Any]:
    idx = get_course_index()
    rows = db.execute(
        select(ChecklistProgress).where(ChecklistProgress.user_id == ctx.user.id)
    ).scalars().all()
    done_map = {r.item_id: r.completed for r in rows}

    checklist_with_state = []
    for group in idx["checklist"]:
        checklist_with_state.append(
            {
                "topic_key": group["topic_key"],
                "title": group["title"],
                "items": [
                    {"id": it["id"], "text": it["text"], "completed": bool(done_map.get(it["id"], False))}
                    for it in group["items"]
                ],
            }
        )
    return {
        "course_meta": idx["course_meta"],
        "checklist": checklist_with_state,
    }


@router.get("/content/theory")
def content_theory(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    idx = get_course_index()
    return {"modules": idx["theory_modules"]}


@router.get("/content/matlab")
def content_matlab(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    idx = get_course_index()
    return idx["matlab_lab"]


@router.get("/content/project")
def content_project(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    idx = get_course_index()
    return idx["project_hub"]


@router.get("/content/project/simulate")
def simulate_project_network(
    disabled_center: str | None = Query(default=None),
    _ctx: AuthContext = Depends(get_current_auth),
) -> dict[str, Any]:
    valid_names = {c["name"] for c in CENTERS}
    target = disabled_center if disabled_center in valid_names else None
    return analyze_network(disabled_center=target)


@router.get("/content/exam-bank")
def content_exam_bank(_ctx: AuthContext = Depends(get_current_auth)) -> dict[str, Any]:
    """Devuelve índice de preguntas históricas (solo enunciado/metadatos; las soluciones están bloqueadas)."""
    idx = get_course_index()
    return idx["exam_bank"]


@router.get("/content/search")
def content_search(q: str = Query(default="", min_length=0, max_length=120), _ctx: AuthContext = Depends(get_current_auth)):
    return {"query": q, "results": search_course_content(q)}


@router.put("/checklist/{item_id}")
def toggle_checklist(
    item_id: str,
    payload: ChecklistToggleRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    row = db.execute(
        select(ChecklistProgress).where(
            ChecklistProgress.user_id == ctx.user.id,
            ChecklistProgress.item_id == item_id[:64],
        )
    ).scalar_one_or_none()
    if row is None:
        row = ChecklistProgress(user_id=ctx.user.id, item_id=item_id[:64], completed=payload.completed)
        db.add(row)
    else:
        row.completed = payload.completed
        row.updated_at = utcnow()
    db.commit()
    return {"item_id": item_id, "completed": payload.completed}


@router.get("/notes")
def list_notes(ctx: AuthContext = Depends(get_current_auth), db: Session = Depends(get_db)):
    rows = db.execute(select(StudyNote).where(StudyNote.user_id == ctx.user.id)).scalars().all()
    return {
        "notes": {
            r.topic_key: {"content": r.content, "updated_at": r.updated_at.isoformat()}
            for r in rows
        }
    }


@router.put("/notes/{topic_key}")
def upsert_note(
    topic_key: str,
    payload: NoteUpdateRequest,
    ctx: AuthContext = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    safe_key = topic_key[:64]
    row = db.execute(
        select(StudyNote).where(StudyNote.user_id == ctx.user.id, StudyNote.topic_key == safe_key)
    ).scalar_one_or_none()
    if row is None:
        row = StudyNote(user_id=ctx.user.id, topic_key=safe_key, content=payload.content)
        db.add(row)
    else:
        row.content = payload.content
        row.updated_at = utcnow()
    db.commit()
    db.refresh(row)
    return {"topic_key": safe_key, "content": row.content, "updated_at": row.updated_at.isoformat()}
