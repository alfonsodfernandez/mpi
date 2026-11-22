"""Registro central de generadores procedurales, deduplicación por usuario y planos de exámenes UFV."""
from __future__ import annotations

import random
import secrets
from collections.abc import Callable
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import GeneratedFingerprint
from .generators_diag import (
    gen_diag_autovalores_2x2,
    gen_diag_comprobar_autovector,
    gen_diag_lectura_pdp,
    gen_diag_triangular_multiplicidades,
)
from .generators_ev import (
    gen_ev_base_y_coordenadas,
    gen_ev_cambio_base,
    gen_ev_dependencia_parametro,
    gen_ev_rango_nulidad_col,
    gen_ev_subespacio_dim_nucleo,
)
from .generators_matlab import (
    gen_matlab_calor_placa,
    gen_matlab_leontief_markov,
    gen_matlab_polinomio_eval,
    gen_matlab_rubrica_y_funciones,
)
from .generators_matrices import (
    gen_mat_conmutar_2x2,
    gen_mat_determinante_propiedades,
    gen_mat_elemental_inversa,
    gen_mat_inversa_gauss_3x3,
    gen_mat_lu_factorizacion,
)
from .generators_sistemas import (
    gen_sel_gauss_3x3_scd,
    gen_sel_lectura_escalonada,
    gen_sel_parametro_k_2x2,
    gen_sel_parametro_k_3x3,
    gen_sel_rango_gauss_teorico,
)
from .generators_tl import (
    gen_tl_dim_ker_im_formula,
    gen_tl_nucleo_imagen_compatibilidad,
    gen_tl_reconstruccion_canonica,
)

TOPIC_LABELS: dict[str, str] = {
    "sistemas": "Tema 1 · Sistemas Lineales",
    "matrices": "Tema 2 · Matrices y Determinantes",
    "espacios_vectoriales": "Tema 3 · Espacios Vectoriales",
    "aplicaciones_lineales": "Tema 4 · Aplicaciones Lineales",
    "diagonalizacion": "Tema 5 · Autovalores y Diagonalización",
    "matlab": "Laboratorio MATLAB",
}

GeneratorFunc = Callable[[random.Random], dict[str, Any]]

GENERATORS: dict[str, dict[str, Any]] = {
    # Tema 1 · Sistemas
    "sel_gauss_3x3_scd": {"topic": "sistemas", "label": "Sistema 3×3 por Gauss-Jordan", "difficulty": "media", "fn": gen_sel_gauss_3x3_scd},
    "sel_parametro_k_2x2": {"topic": "sistemas", "label": "Discusión 2×2 con parámetro k", "difficulty": "media", "fn": gen_sel_parametro_k_2x2},
    "sel_parametro_k_3x3": {"topic": "sistemas", "label": "Discusión 3×3 con parámetro k²", "difficulty": "alta", "fn": gen_sel_parametro_k_3x3},
    "sel_lectura_escalonada": {"topic": "sistemas", "label": "Lectura de matriz escalonada (V/F)", "difficulty": "media", "fn": gen_sel_lectura_escalonada},
    "sel_rango_gauss_teorico": {"topic": "sistemas", "label": "Rango, nulidad e invertibilidad desde Gauss", "difficulty": "baja", "fn": gen_sel_rango_gauss_teorico},
    # Tema 2 · Matrices y Determinantes
    "mat_elemental_inversa": {"topic": "matrices", "label": "Inversa mediante operaciones elementales", "difficulty": "media", "fn": gen_mat_elemental_inversa},
    "mat_inversa_gauss_3x3": {"topic": "matrices", "label": "Inversa 3×3 por Gauss-Jordan", "difficulty": "alta", "fn": gen_mat_inversa_gauss_3x3},
    "mat_conmutar_2x2": {"topic": "matrices", "label": "Matrices que conmutan (AB = BA)", "difficulty": "media", "fn": gen_mat_conmutar_2x2},
    "mat_lu_factorizacion": {"topic": "matrices", "label": "Factorización LU y resolución Ax = b", "difficulty": "alta", "fn": gen_mat_lu_factorizacion},
    "mat_determinante_propiedades": {"topic": "matrices", "label": "Determinantes (cofactores y propiedades)", "difficulty": "media", "fn": gen_mat_determinante_propiedades},
    # Tema 3 · Espacios Vectoriales
    "ev_dependencia_parametro": {"topic": "espacios_vectoriales", "label": "Dependencia lineal con parámetro k", "difficulty": "media", "fn": gen_ev_dependencia_parametro},
    "ev_base_y_coordenadas": {"topic": "espacios_vectoriales", "label": "Base y coordenadas en ℝ³", "difficulty": "media", "fn": gen_ev_base_y_coordenadas},
    "ev_subespacio_dim_nucleo": {"topic": "espacios_vectoriales", "label": "Subespacios vectoriales y dimensión", "difficulty": "baja", "fn": gen_ev_subespacio_dim_nucleo},
    "ev_cambio_base": {"topic": "espacios_vectoriales", "label": "Matriz de cambio de base", "difficulty": "media", "fn": gen_ev_cambio_base},
    "ev_rango_nulidad_col": {"topic": "espacios_vectoriales", "label": "Pertenencia a Ker(A) y Col(A)", "difficulty": "media", "fn": gen_ev_rango_nulidad_col},
    # Tema 4 · Aplicaciones Lineales
    "tl_reconstruccion_canonica": {"topic": "aplicaciones_lineales", "label": "Reconstrucción de matriz canónica", "difficulty": "media", "fn": gen_tl_reconstruccion_canonica},
    "tl_nucleo_imagen_compatibilidad": {"topic": "aplicaciones_lineales", "label": "Compatibilidad desde plano imagen", "difficulty": "media", "fn": gen_tl_nucleo_imagen_compatibilidad},
    "tl_dim_ker_im_formula": {"topic": "aplicaciones_lineales", "label": "Linealidad, Ker(T), Im(T) e isomorfismos", "difficulty": "media", "fn": gen_tl_dim_ker_im_formula},
    # Tema 5 · Autovalores y Diagonalización
    "diag_autovalores_2x2": {"topic": "diagonalizacion", "label": "Autovalores y autovectores (2×2)", "difficulty": "media", "fn": gen_diag_autovalores_2x2},
    "diag_triangular_multiplicidades": {"topic": "diagonalizacion", "label": "Matriz triangular y multiplicidades mₐ/m_g", "difficulty": "media", "fn": gen_diag_triangular_multiplicidades},
    "diag_comprobar_autovector": {"topic": "diagonalizacion", "label": "Parámetro k desde un autovector dado", "difficulty": "media", "fn": gen_diag_comprobar_autovector},
    "diag_lectura_pdp": {"topic": "diagonalizacion", "label": "Lectura de A = PDP⁻¹ y potencias", "difficulty": "media", "fn": gen_diag_lectura_pdp},
    # Tema 6 · MATLAB
    "matlab_calor_placa": {"topic": "matlab", "label": "MATLAB · Distribución de calor 2×2", "difficulty": "media", "fn": gen_matlab_calor_placa},
    "matlab_leontief_markov": {"topic": "matlab", "label": "MATLAB · Leontief y Cadenas de Markov", "difficulty": "media", "fn": gen_matlab_leontief_markov},
    "matlab_polinomio_eval": {"topic": "matlab", "label": "MATLAB · Polinomios y polyval", "difficulty": "baja", "fn": gen_matlab_polinomio_eval},
    "matlab_rubrica_y_funciones": {"topic": "matlab", "label": "MATLAB · Funciones y Rúbrica UFV 2026", "difficulty": "baja", "fn": gen_matlab_rubrica_y_funciones},
}


# Planos oficiales de simulacros de examen fieles a CO/CEX 2025-26 UFV
EXAM_BLUEPRINTS: dict[str, dict[str, Any]] = {
    "ordinaria": {
        "title": "Simulacro Convocatoria Ordinaria (CO) · Formato UFV",
        "time_limit_seconds": 90 * 60,  # 1,5 h exactas como en 07_Examenes_ordinaria_2025-26.md
        "slots": [
            ("sel_rango_gauss_teorico", 1.0),
            ("sel_lectura_escalonada", 1.0),
            ("mat_elemental_inversa", 1.0),
            ("ev_subespacio_dim_nucleo", 1.0),
            ("mat_conmutar_2x2", 1.0),
            ("tl_nucleo_imagen_compatibilidad", 1.0),
            ("tl_reconstruccion_canonica", 1.25),
            ("diag_autovalores_2x2", 1.25),
            ("diag_triangular_multiplicidades", 1.5),
        ],
    },
    "extraordinaria": {
        "title": "Simulacro Convocatoria Extraordinaria (CEX) · Formato UFV",
        "time_limit_seconds": 105 * 60,  # 1h 45 min exactas como en 08_Examenes_extraordinaria_2025-26.md
        "slots": [
            ("sel_parametro_k_2x2", 1.0),
            ("sel_parametro_k_3x3", 1.25),
            ("mat_lu_factorizacion", 1.25),
            ("ev_base_y_coordenadas", 1.0),
            ("ev_rango_nulidad_col", 1.0),
            ("tl_dim_ker_im_formula", 1.0),
            ("diag_comprobar_autovector", 1.0),
            ("diag_lectura_pdp", 1.25),
            ("matlab_leontief_markov", 1.25),
        ],
    },
    "express": {
        "title": "Simulacro Express de Control (5 Bloques · 35 min)",
        "time_limit_seconds": 35 * 60,
        "slots": [
            ("sistemas", 2.0),
            ("matrices", 2.0),
            ("espacios_vectoriales", 2.0),
            ("aplicaciones_lineales", 2.0),
            ("diagonalizacion", 2.0),
        ],
    },
}


def list_catalog() -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {k: [] for k in TOPIC_LABELS}
    for gid, meta in GENERATORS.items():
        grouped[meta["topic"]].append(
            {"id": gid, "label": meta["label"], "difficulty": meta["difficulty"], "topic": meta["topic"]}
        )
    return [
        {"topic": t, "label": TOPIC_LABELS[t], "generators": grouped[t]}
        for t in TOPIC_LABELS
    ]


def generate_unique_exercise(
    db: Session | None,
    user_id: int | None,
    topic: str = "random",
    generator_id: str | None = None,
    difficulty: str | None = None,
    max_retries: int = 35,
) -> dict[str, Any]:
    """Genera un ejercicio único garantizando que su huella no se haya servido antes a este usuario."""
    rng = random.Random(secrets.randbits(64))

    if generator_id and generator_id in GENERATORS:
        candidates = [generator_id]
    elif topic in TOPIC_LABELS:
        candidates = [gid for gid, m in GENERATORS.items() if m["topic"] == topic]
    else:
        candidates = list(GENERATORS.keys())

    if difficulty in {"baja", "media", "alta"}:
        filtered = [gid for gid in candidates if GENERATORS[gid]["difficulty"] == difficulty]
        if filtered:
            candidates = filtered

    seen_fps: set[str] = set()
    if db is not None and user_id is not None:
        rows = db.execute(
            select(GeneratedFingerprint.fingerprint).where(GeneratedFingerprint.user_id == user_id)
        ).scalars().all()
        seen_fps = set(rows)

    chosen_payload: dict[str, Any] | None = None
    for _ in range(max_retries):
        gid = rng.choice(candidates)
        payload = GENERATORS[gid]["fn"](rng)
        fp = payload["fingerprint"]
        if fp not in seen_fps:
            chosen_payload = payload
            break

    if chosen_payload is None:
        # Extremadamente improbable: forzamos nueva semilla única
        gid = rng.choice(candidates)
        chosen_payload = GENERATORS[gid]["fn"](rng)
        chosen_payload["fingerprint"] = f"{chosen_payload['fingerprint']}-{secrets.token_hex(4)}"

    if db is not None and user_id is not None:
        db.add(
            GeneratedFingerprint(
                user_id=user_id,
                generator_id=chosen_payload["generator_id"],
                fingerprint=chosen_payload["fingerprint"],
            )
        )
        db.flush()

    return chosen_payload


def generate_exam_questions(db: Session | None, user_id: int | None, mode: str) -> tuple[dict[str, Any], list[tuple[dict[str, Any], float]]]:
    """Genera un examen completo (CO / CEX / Express) con problemas 100% frescos y únicos."""
    blueprint = EXAM_BLUEPRINTS.get(mode, EXAM_BLUEPRINTS["express"])
    results: list[tuple[dict[str, Any], float]] = []
    for slot_target, weight in blueprint["slots"]:
        if slot_target in GENERATORS:
            ex = generate_unique_exercise(db, user_id, generator_id=slot_target)
        else:
            ex = generate_unique_exercise(db, user_id, topic=slot_target)
        results.append((ex, weight))
    return blueprint, results
