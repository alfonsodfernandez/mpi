"""Pruebas de integración de API, autenticación dual, RBAC (/admin), bloqueo de soluciones y sistema anti-trampas."""
from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from backend.app.config import settings
from backend.app.database import Base, SessionLocal, engine
from backend.app.main import app
from backend.app.models import ExamSession, ExerciseAttempt


@pytest.fixture(scope="module")
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c


def _login(client: TestClient, username: str, password: str) -> dict[str, str]:
    r = client.post("/api/auth/login", json={"username": username, "password": password})
    assert r.status_code == 200, r.text
    token = r.json()["token"]
    return {"Authorization": f"Bearer {token}"}


def test_dual_auth_and_rbac(client: TestClient):
    # Contraseña incorrecta
    bad = client.post("/api/auth/login", json={"username": settings.PABLO_USERNAME, "password": "wrong"})
    assert bad.status_code == 401

    pablo_headers = _login(client, settings.PABLO_USERNAME, settings.PABLO_PASSWORD)
    admin_headers = _login(client, settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD)

    # Pablo NO puede acceder a /api/admin/*
    assert client.get("/api/admin/dashboard", headers=pablo_headers).status_code == 403
    assert client.get("/api/admin/export?format=json", headers=pablo_headers).status_code == 403

    # Profesor SÍ puede acceder
    dash = client.get("/api/admin/dashboard", headers=admin_headers)
    assert dash.status_code == 200
    assert dash.json()["student"]["username"] == settings.PABLO_USERNAME


def test_zero_answer_leakage_and_violation_invalidation(client: TestClient):
    pablo_headers = _login(client, settings.PABLO_USERNAME, settings.PABLO_PASSWORD)
    admin_headers = _login(client, settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD)

    # 1. Iniciar ejercicio procedural
    start = client.post("/api/exercises/start", json={"topic": "sistemas"}, headers=pablo_headers)
    assert start.status_code == 200
    data = start.json()
    raw_dump = json.dumps(data)

    # Regla de oro: CERO fuga de solución antes de enviar
    for forbidden in ["solution", "grading_spec", "correct_display", "steps_md", '"expected"']:
        assert forbidden not in raw_dump, f"Fuga detectada en respuesta pública: {forbidden}"

    attempt_id = data["attempt_id"]

    # 2. Simular fuga de pestaña -> debe invalidar en servidor
    vio = client.post(
        "/api/security/violation",
        json={
            "violation_type": "TAB_SWITCH",
            "context_mode": "practice",
            "topic": data["topic"],
            "question_ref": data["title"],
            "details": "Test cambio de pestaña",
            "active_attempt_id": attempt_id,
            "trigger_reset": True,
        },
        headers=pablo_headers,
    )
    assert vio.status_code == 200
    assert vio.json()["reset_enforced"] is True

    # 3. Intentar enviar el ejercicio invalidado debe dar 409
    sub_blocked = client.post(
        f"/api/exercises/{attempt_id}/submit",
        json={"answer": "1"},
        headers=pablo_headers,
    )
    assert sub_blocked.status_code == 409

    # 4. Nuevo ejercicio -> entregar respuesta correcta comprobada en servidor -> ahora SÍ devuelve pasos
    start2 = client.post("/api/exercises/start", json={"generator_id": "sel_gauss_3x3_scd"}, headers=pablo_headers)
    assert start2.status_code == 200
    att2_id = start2.json()["attempt_id"]
    assert att2_id != attempt_id

    # Leer solución SOLO en test desde DB para simular que Pablo la resolvió bien
    db = SessionLocal()
    try:
        att2 = db.get(ExerciseAttempt, att2_id)
        sol2 = json.loads(att2.solution_json)
        expected_ans = sol2["grading_spec"]["expected"]
    finally:
        db.close()

    res = client.post(
        f"/api/exercises/{att2_id}/submit",
        json={"answer": expected_ans, "timed_out": False},
        headers=pablo_headers,
    )
    assert res.status_code == 200
    fb = res.json()
    assert fb["is_correct"] is True
    assert fb["score"] == 1.0
    assert len(fb["steps_md"]) >= 2

    # 5. Verificar que la infracción y el acierto aparecen en /api/admin/dashboard y en exportaciones
    dash = client.get("/api/admin/dashboard", headers=admin_headers).json()
    assert dash["kpis"]["total_violations"] >= 1
    assert any(v["violation_type"] == "TAB_SWITCH" for v in dash["violations"])
    assert dash["kpis"]["total_questions_answered"] >= 1

    csv_resp = client.get("/api/admin/export?format=csv&scope=all", headers=admin_headers)
    assert csv_resp.status_code == 200
    assert "TAB_SWITCH" in csv_resp.text

    json_resp = client.get("/api/admin/export?format=json", headers=admin_headers)
    assert json_resp.status_code == 200
    assert json_resp.json()["kpis"]["total_violations"] >= 1


def test_exam_simulator_zero_leak_and_grading(client: TestClient):
    pablo_headers = _login(client, settings.PABLO_USERNAME, settings.PABLO_PASSWORD)

    ex = client.post("/api/exams/start", json={"mode": "express"}, headers=pablo_headers)
    assert ex.status_code == 200
    ex_data = ex.json()
    assert ex_data["total_questions"] == 5
    raw_dump = json.dumps(ex_data)
    for forbidden in ["solution", "grading_spec", "correct_display", "steps_md", '"expected"']:
        assert forbidden not in raw_dump

    exam_id = ex_data["exam_id"]
    # No se puede revisar un examen activo
    assert client.get(f"/api/exams/{exam_id}/review", headers=pablo_headers).status_code == 403

    # Finalizar examen
    fin = client.post(f"/api/exams/{exam_id}/finalize", json={"timed_out": False, "answers": {}}, headers=pablo_headers)
    assert fin.status_code == 200
    assert fin.json()["status"] == "completed"
    assert len(fin.json()["questions"]) == 5

    # Ahora SÍ se puede revisar
    rev = client.get(f"/api/exams/{exam_id}/review", headers=pablo_headers)
    assert rev.status_code == 200


def test_content_notes_checklist_and_logistics_dana(client: TestClient):
    pablo_headers = _login(client, settings.PABLO_USERNAME, settings.PABLO_PASSWORD)

    assert client.get("/api/content/overview", headers=pablo_headers).status_code == 200
    assert client.get("/api/content/theory", headers=pablo_headers).status_code == 200
    assert client.get("/api/content/matlab", headers=pablo_headers).status_code == 200
    assert client.get("/api/content/project", headers=pablo_headers).status_code == 200

    sim = client.get("/api/content/project/simulate?disabled_center=Valencia", headers=pablo_headers)
    assert sim.status_code == 200
    assert sim.json()["summary"]["removed_routes_count"] == 8

    # Notas y checklist persistentes
    n = client.put("/api/notes/sistemas_matrices", json={"content": "Recordar: $A=LU$ con 1s en diagonal de L"}, headers=pablo_headers)
    assert n.status_code == 200
    c = client.put("/api/checklist/t1_1", json={"completed": True}, headers=pablo_headers)
    assert c.status_code == 200

    # Heartbeat
    hb = client.post("/api/auth/heartbeat", json={"delta_seconds": 15, "is_active": True, "current_view": "teoria"}, headers=pablo_headers)
    assert hb.status_code == 200
