"""Generadores procedurales para Tema 5: Autovalores, Autovectores y Diagonalización."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import (
    build_unimodular_matrix,
    make_exercise_payload,
    mat_to_latex,
    mat_to_plain_rows,
    vec_to_latex,
)


def gen_diag_autovalores_2x2(rng: random.Random) -> dict[str, Any]:
    """Construye A = P D P⁻¹ 2x2 no trivial con autovalores enteros limpios; pide espectro y autovector."""
    l1, l2 = sorted(rng.sample([-4, -3, -2, -1, 1, 2, 3, 4, 5], 2))
    P = build_unimodular_matrix(2, rng, steps=2, coeff_choices=[-2, -1, 1, 2])
    D = sp.diag(l1, l2)
    A = P * D * P.inv()
    # Evitar que quede diagonal o triangular trivial
    if A[0, 1] == 0 or A[1, 0] == 0:
        P = sp.Matrix([[1, 1], [1, 2]]) if rng.random() < 0.5 else sp.Matrix([[2, 1], [1, 1]])
        A = P * D * P.inv()

    v1 = [int(P[0, 0]), int(P[1, 0])]
    v2 = [int(P[0, 1]), int(P[1, 1])]
    tr = int(A.trace())
    det = int(A.det())
    lam = sp.Symbol("\\lambda")
    poly_expr = sp.expand((A - lam * sp.eye(2)).det())

    statement = (
        "Dada la matriz real $A \\in \\mathcal{M}_{2\\times 2}(\\mathbb{R})$:\n\n"
        f"$$ A = {mat_to_latex(A)} $$\n\n"
        f"Calcula sus **autovalores** $\\lambda_1 < \\lambda_2$ (usando $p_A(\\lambda) = \\det(A - \\lambda I)$) "
        f"y proporciona un **autovector no nulo** asociado al mayor autovalor $\\lambda_2$ "
        "(se aceptará cualquier múltiplo escalar no nulo)."
    )

    steps = [
        f"Calculamos el polinomio característico: $$ p_A(\\lambda) = \\det(A - \\lambda I) = {sp.latex(poly_expr)} = (\\lambda - ({l1}))(\\lambda - ({l2})) $$",
        f"(Comprobación rápida: $\\operatorname{{tr}}(A) = {tr} = {l1} + ({l2})$ y $|A| = {det} = ({l1})\\cdot({l2})$).",
        f"Los autovalores ordenados son $\\lambda_1 = {l1}$ y $\\lambda_2 = {l2}$.",
        f"Para $\\lambda_2 = {l2}$ resolvemos $(A - ({l2})I)v = 0$: "
        f"$$ {mat_to_latex(A - l2 * sp.eye(2))} \\begin{{pmatrix}} x \\\\ y \\end{{pmatrix}} = \\begin{{pmatrix}} 0 \\\\ 0 \\end{{pmatrix}} $$",
        f"Una base de $E_{{{l2}}}$ es $\\left\\{{ {vec_to_latex(v2)} \\right\\}}$ (cualquier múltiplo $t \\cdot {vec_to_latex(v2)}$ con $t \\neq 0$ es válido). "
        f"Para $\\lambda_1 = {l1}$, una base de $E_{{{l1}}}$ es $\\left\\{{ {vec_to_latex(v1)} \\right\\}}$.",
    ]

    return make_exercise_payload(
        generator_id="diag_autovalores_2x2",
        topic="diagonalizacion",
        title="Cálculo de autovalores y autovector asociado (2×2)",
        difficulty="media",
        time_limit_seconds=270,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "l1", "label": "Menor autovalor λ₁", "type": "number", "placeholder": "Entero"},
                {"id": "l2", "label": "Mayor autovalor λ₂", "type": "number", "placeholder": "Entero"},
                {"id": "v2", "label": "Un autovector no nulo v = (x, y) asociado a λ₂", "type": "vector", "labels": ["x", "y"]},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "l1", "label": "λ₁", "type": "number", "expected": str(l1)},
                {"id": "l2", "label": "λ₂", "type": "number", "expected": str(l2)},
                {
                    "id": "v2",
                    "label": "Autovector de λ₂",
                    "type": "eigenvector",
                    "matrix": mat_to_plain_rows(A),
                    "eigenvalue": str(l2),
                },
            ],
        },
        correct_display=f"$\\lambda_1 = {l1},\\; \\lambda_2 = {l2}$; autovector de $\\lambda_2$: cualquier múltiplo no nulo de ${vec_to_latex(v2)}$.",
        steps_md=steps,
        theory_ref="Tema 5 · Polinomio característico y subespacios propios (05 Tema 5 Ej. 1 · 09 6.13–6.15)",
        fingerprint_data={"A": mat_to_plain_rows(A)},
        protected_canvas={"kind": "matrix", "label": "Matriz A (2×2)", "rows": mat_to_plain_rows(A)},
    )


def gen_diag_triangular_multiplicidades(rng: random.Random) -> dict[str, Any]:
    """Matriz triangular 3x3 con autovalor doble: multiplicidad algebraica vs geométrica (07 CO P9)."""
    lam_double, lam_single = rng.sample([-3, -2, -1, 1, 2, 3, 4, 5], 2)
    is_diag = rng.choice([True, False])
    off_entry = 0 if is_diag else rng.choice([-2, -1, 1, 2])
    upper = rng.choice([True, False])

    if upper:
        # Autovalor doble en posiciones (0,0) y (1,1); bloque superior (0,1) controla si es diagonalizable
        # (A - lam_double I) tiene [[0, off_entry, c], [0, 0, d], [0, 0, lam_single - lam_double]]
        c_extra = rng.choice([-2, 0, 2])
        A = sp.Matrix([
            [lam_double, off_entry, c_extra],
            [0, lam_double, 0],
            [0, 0, lam_single],
        ])
    else:
        c_extra = rng.choice([-2, 0, 2])
        A = sp.Matrix([
            [lam_double, 0, 0],
            [off_entry, lam_double, 0],
            [c_extra, 0, lam_single],
        ])

    null_double = (A - lam_double * sp.eye(3)).nullspace()
    mg_double = len(null_double)
    diag_expected = "si" if mg_double == 2 else "no"

    statement = (
        "Considera la siguiente matriz triangular $A \\in \\mathcal{M}_{3\\times 3}(\\mathbb{R})$:\n\n"
        f"$$ A = {mat_to_latex(A)} $$\n\n"
        "Sin desarrollar determinantes largos, halla el autovalor con multiplicidad algebraica 2, "
        "su **multiplicidad geométrica** $m_g = \\dim E_\\lambda$, y decide si $A$ es **diagonalizable** en $\\mathbb{R}$."
    )

    steps = [
        f"Al ser triangular, los autovalores se leen directamente en la diagonal principal: "
        f"$\\lambda_{{doble}} = {lam_double}$ (con $m_a = 2$) y $\\lambda_{{simple}} = {lam_single}$ (con $m_a = 1$, por lo que automáticamente $m_g = 1$).",
        f"Para estudiar si es diagonalizable analizamos el rango de $(A - ({lam_double})I)$: "
        f"$$ A - ({lam_double})I = {mat_to_latex(A - lam_double * sp.eye(3))} $$",
        f"El rango es $\\operatorname{{rg}}(A - ({lam_double})I) = {3 - mg_double}$, luego la multiplicidad geométrica es "
        f"$m_g({lam_double}) = 3 - {3 - mg_double} = {mg_double}$.",
        (
            f"Como $m_g({lam_double}) = 2 = m_a({lam_double})$ y todos los autovalores son reales, **$A$ SÍ es diagonalizable**."
            if mg_double == 2 else
            f"Como $m_g({lam_double}) = 1 < 2 = m_a({lam_double})$, **$A$ NO es diagonalizable**."
        ),
    ]

    return make_exercise_payload(
        generator_id="diag_triangular_multiplicidades",
        topic="diagonalizacion",
        title="Diagonalizabilidad de matriz triangular (mₐ vs m_g)",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "lam_double", "label": "a) Autovalor con multiplicidad algebraica 2", "type": "number", "placeholder": "Entero"},
                {"id": "lam_single", "label": "b) Autovalor con multiplicidad algebraica 1", "type": "number", "placeholder": "Entero"},
                {"id": "mg_double", "label": "c) Multiplicidad geométrica m_g del autovalor doble", "type": "number", "placeholder": "1 o 2"},
                {
                    "id": "is_diag",
                    "label": "d) ¿Es A diagonalizable en ℝ?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, es diagonalizable"}, {"value": "no", "label": "No es diagonalizable"}],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "lam_double", "label": "λ doble", "type": "number", "expected": str(lam_double)},
                {"id": "lam_single", "label": "λ simple", "type": "number", "expected": str(lam_single)},
                {"id": "mg_double", "label": "m_g(λ doble)", "type": "number", "expected": str(mg_double)},
                {"id": "is_diag", "label": "Diagonalizabilidad", "type": "choice", "expected": diag_expected},
            ],
        },
        correct_display=f"$\\lambda_{{doble}}={lam_double}$ ($m_g={mg_double}$), $\\lambda_{{simple}}={lam_single}$; {'Sí' if mg_double == 2 else 'No'} es diagonalizable.",
        steps_md=steps,
        theory_ref="Tema 5 · Criterio de diagonalización y matrices triangulares (07 CO P9 · 09 6.26–6.28)",
        fingerprint_data={"A": mat_to_plain_rows(A)},
        protected_canvas={"kind": "matrix", "label": "Matriz triangular A (3×3)", "rows": mat_to_plain_rows(A)},
    )


def gen_diag_comprobar_autovector(rng: random.Random) -> dict[str, Any]:
    """Parámetro k a partir de un autovector conocido (formato 09 6.8–6.10)."""
    # Construimos A 3x3 con autovector v = (v1, v2, v3) y autovalor lam; reemplazamos a_{1,3} por k
    lam = rng.choice([-3, -2, -1, 2, 3, 4])
    v = sp.Matrix([rng.choice([-2, -1, 1, 2]), rng.choice([-2, -1, 1, 2]), rng.choice([-1, 1])])
    a11 = rng.choice([-2, -1, 1, 2, 3])
    a12 = rng.choice([-2, -1, 1, 2])
    # a11*v1 + a12*v2 + k*v3 = lam*v1 => k = (lam*v1 - a11*v1 - a12*v2) / v3 (entero porque v3 = ±1!)
    k_val = int((lam * v[0] - a11 * v[0] - a12 * v[1]) / v[2])

    a21 = rng.choice([-2, -1, 1, 2])
    a22 = rng.choice([-2, -1, 1, 2, 3])
    a23 = int((lam * v[1] - a21 * v[0] - a22 * v[1]) / v[2])

    a31 = rng.choice([-2, -1, 1, 2])
    a32 = rng.choice([-2, -1, 1, 2])
    a33 = int((lam * v[2] - a31 * v[0] - a32 * v[1]) / v[2])

    k_sym = sp.Symbol("k")
    A_sym = sp.Matrix([[a11, a12, k_sym], [a21, a22, a23], [a31, a32, a33]])
    v_list = [int(v[0]), int(v[1]), int(v[2])]

    statement = (
        f"Se sabe que el vector $v = {vec_to_latex(v_list)}^T$ es un **autovector** de la matriz:\n\n"
        f"$$ A = {mat_to_latex(A_sym)} $$\n\n"
        "Sin calcular el polinomio característico, determina primero el **autovalor $\\lambda$** asociado a $v$ "
        "y después el valor del parámetro **$k$**."
    )

    steps = [
        f"Por definición de autovector debe cumplirse $A \\cdot v = \\lambda \\cdot v$.",
        f"Calculando la segunda (o tercera) componente de $Av$: $({a21})({v_list[0]}) + ({a22})({v_list[1]}) + ({a23})({v_list[2]}) = {lam * v_list[1]} = \\lambda \\cdot ({v_list[1]})$, de donde $\\lambda = {lam}$.",
        f"Imponiendo la igualdad en la primera componente: $({a11})({v_list[0]}) + ({a12})({v_list[1]}) + k({v_list[2]}) = ({lam})({v_list[0]}) = {lam * v_list[0]}$.",
        f"Despejando $k$ obtenemos exactamente $k = {k_val}$.",
    ]

    return make_exercise_payload(
        generator_id="diag_comprobar_autovector",
        topic="diagonalizacion",
        title="Autovalor y parámetro k a partir de un autovector dado",
        difficulty="media",
        time_limit_seconds=210,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "lam", "label": "a) Autovalor λ asociado a v", "type": "number", "placeholder": "Entero"},
                {"id": "k", "label": "b) Valor del parámetro k", "type": "number", "placeholder": "Entero"},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "lam", "label": "Autovalor λ", "type": "number", "expected": str(lam)},
                {"id": "k", "label": "Parámetro k", "type": "number", "expected": str(k_val)},
            ],
        },
        correct_display=f"$\\lambda = {lam},\\; k = {k_val}$.",
        steps_md=steps,
        theory_ref="Tema 5 · Definición de autovector Av = λv (09 6.2 y 6.8–6.10)",
        fingerprint_data={"v": v_list, "lam": lam, "k": k_val, "a11": a11, "a22": a22},
        protected_canvas={
            "kind": "matrix",
            "label": "Matriz A(k)",
            "rows": [[str(a11), str(a12), "k"], [str(a21), str(a22), str(a23)], [str(a31), str(a32), str(a33)]],
        },
    )


def gen_diag_lectura_pdp(rng: random.Random) -> dict[str, Any]:
    """Lectura directa de una diagonalización A = P D P⁻¹ sin multiplicar matrices (09 6.3)."""
    l_double, l_single = rng.sample([-3, -2, -1, 2, 3, 4, 5], 2)
    P = build_unimodular_matrix(3, rng, steps=2, coeff_choices=[-2, -1, 1, 2])
    P_inv = P.inv()
    D = sp.diag(l_double, l_double, l_single)
    power = rng.choice([2, 3])
    v3 = [int(P[i, 2]) for i in range(3)]
    Av_pow = [int((l_single**power) * x) for x in v3]

    statement = (
        "Una matriz $A \\in \\mathcal{M}_{3\\times 3}(\\mathbb{R})$ admite la siguiente factorización $A = P D P^{-1}$:\n\n"
        f"$$ A = {mat_to_latex(P)} {mat_to_latex(D)} {mat_to_latex(P_inv)} $$\n\n"
        "**Sin multiplicar las matrices**, determina:\n"
        "a) El determinante $|A|$ y la traza $\\operatorname{tr}(A)$.\n"
        f"b) El vector resultado de $A^{power} \\cdot v_3$, donde $v_3 = {vec_to_latex(v3)}^T$ es la tercera columna de $P$."
    )

    det_A = (l_double**2) * l_single
    tr_A = 2 * l_double + l_single

    steps = [
        f"Al ser $A$ semejante a $D$, comparten autovalores, traza y determinante: $\\lambda_1 = {l_double}$ ($m_a = m_g = 2$) y $\\lambda_2 = {l_single}$ ($m_a = m_g = 1$).",
        f"$|A| = |D| = ({l_double})^2 \\cdot ({l_single}) = {det_A}$ y $\\operatorname{{tr}}(A) = \\operatorname{{tr}}(D) = {l_double} + {l_double} + ({l_single}) = {tr_A}$.",
        f"Las columnas de $P$ son autovectores correspondientes a la diagonal de $D$; en concreto $v_3 = {vec_to_latex(v3)}^T$ es autovector de $\\lambda_2 = {l_single}$.",
        f"Por tanto $A^{power} v_3 = \\lambda_2^{power} v_3 = ({l_single})^{power} \\cdot {vec_to_latex(v3)}^T = {vec_to_latex(Av_pow)}^T$.",
    ]

    return make_exercise_payload(
        generator_id="diag_lectura_pdp",
        topic="diagonalizacion",
        title="Lectura de diagonalización A = PDP⁻¹ y potencias Aᵏv",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "det", "label": "a.1) Determinante |A|", "type": "number", "placeholder": "Entero"},
                {"id": "tr", "label": "a.2) Traza tr(A)", "type": "number", "placeholder": "Entero"},
                {"id": "av", "label": f"b) Vector A^{power} · v₃", "type": "vector", "labels": ["x", "y", "z"]},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "det", "label": "|A|", "type": "number", "expected": str(det_A)},
                {"id": "tr", "label": "tr(A)", "type": "number", "expected": str(tr_A)},
                {"id": "av", "label": f"A^{power}·v₃", "type": "vector", "expected": [str(x) for x in Av_pow]},
            ],
        },
        correct_display=f"$|A| = {det_A},\\; \\operatorname{{tr}}(A) = {tr_A},\\; A^{power} v_3 = {vec_to_latex(Av_pow)}^T$.",
        steps_md=steps,
        theory_ref="Tema 5 · Semejanza y diagonalización A = PDP⁻¹ (09 6.3 · Checklist 5.3–5.4)",
        fingerprint_data={"ld": l_double, "ls": l_single, "P": mat_to_plain_rows(P), "pow": power},
        protected_canvas={"kind": "matrix", "label": "Matriz de paso P", "rows": mat_to_plain_rows(P)},
    )
