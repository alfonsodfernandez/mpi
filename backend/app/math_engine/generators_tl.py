"""Generadores procedurales para Tema 4: Aplicaciones (Transformaciones) Lineales."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import (
    build_unimodular_matrix,
    format_linear_expr,
    make_exercise_payload,
    mat_to_latex,
    mat_to_plain_rows,
    vec_to_latex,
)


def gen_tl_reconstruccion_canonica(rng: random.Random) -> dict[str, Any]:
    """Reconstruir la matriz canónica de T: R³ -> R³ conociendo T(e1), T(e2) y T(e1+e2+e3) (07 CO P7)."""
    is_inj = rng.choice([True, False])
    if is_inj:
        A = build_unimodular_matrix(3, rng, steps=2, coeff_choices=[-2, -1, 1, 2])
    else:
        c1 = sp.Matrix([rng.choice([1, 2]), rng.choice([-1, 0, 1]), rng.choice([0, 1])])
        c2 = sp.Matrix([rng.choice([-1, 0, 1]), rng.choice([1, 2]), rng.choice([-1, 1])])
        while c1.cross(c2).is_zero_matrix:
            c2[2] += 1
        p, q = rng.choice([-1, 1]), rng.choice([-1, 1])
        A = c1.row_join(c2).row_join(p * c1 + q * c2)

    t_e1 = list(A[:, 0])
    t_e2 = list(A[:, 1])
    # Elegimos v3 = a*e1 + b*e2 + e3 con a,b en {-1, 1}
    a_c = rng.choice([-1, 1])
    b_c = rng.choice([-1, 1])
    v3 = sp.Matrix([a_c, b_c, 1])
    t_v3 = list(A * v3)
    t_e3 = list(A[:, 2])

    statement = (
        "Sea $T : \\mathbb{R}^3 \\to \\mathbb{R}^3$ una transformación lineal tal que:\n\n"
        f"$$ T(1,0,0) = {vec_to_latex(t_e1)}, \\qquad T(0,1,0) = {vec_to_latex(t_e2)}, \\qquad "
        f"T{vec_to_latex(list(v3))} = {vec_to_latex(t_v3)} $$\n\n"
        "Determina la **matriz asociada $A$** de $T$ en la base canónica de $\\mathbb{R}^3$."
    )

    steps = [
        f"Observamos que $v_3 = {vec_to_latex(list(v3))} = ({a_c})e_1 + ({b_c})e_2 + e_3$.",
        f"Por linealidad de $T$: $T(v_3) = ({a_c})T(e_1) + ({b_c})T(e_2) + T(e_3)$, de donde despejamos: "
        f"$$ T(e_3) = T(v_3) - ({a_c})T(e_1) - ({b_c})T(e_2) = {vec_to_latex(t_e3)} $$",
        f"La matriz canónica $A$ tiene por columnas $T(e_1), T(e_2), T(e_3)$: $$ A = {mat_to_latex(A)} $$",
        f"Como $\\operatorname{{rg}}(A) = {A.rank()}$, $T$ {'es inyectiva (e isomorfismo)' if A.rank() == 3 else 'NO es inyectiva ($\\dim \\operatorname{Ker} T = ' + str(3 - A.rank()) + '$)'}.",
    ]

    return make_exercise_payload(
        generator_id="tl_reconstruccion_canonica",
        topic="aplicaciones_lineales",
        title="Reconstrucción de matriz canónica de T: ℝ³ → ℝ³",
        difficulty="media",
        time_limit_seconds=270,
        statement_md=statement,
        input_spec={"kind": "matrix", "rows": 3, "cols": 3, "label": "Matriz canónica A de T"},
        grading_spec={"kind": "matrix", "expected": mat_to_plain_rows(A)},
        correct_display=f"$$ A = {mat_to_latex(A)} $$",
        steps_md=steps,
        theory_ref="Tema 4 · Matriz asociada a una TL (04 Pizarra · 07 CO P7 · 09 5.18–5.20)",
        fingerprint_data={"A": mat_to_plain_rows(A), "a": a_c, "b": b_c},
        protected_canvas={
            "kind": "text_lines",
            "label": "Imágenes conocidas de T",
            "lines": [
                f"T(1, 0, 0) = ({', '.join(str(int(x)) for x in t_e1)})",
                f"T(0, 1, 0) = ({', '.join(str(int(x)) for x in t_e2)})",
                f"T({a_c}, {b_c}, 1) = ({', '.join(str(int(x)) for x in t_v3)})",
            ],
        },
    )


def gen_tl_nucleo_imagen_compatibilidad(rng: random.Random) -> dict[str, Any]:
    """Compatibilidad y rango a partir de un plano imagen (formato exacto 07 CO P6 / 09 5.12–5.14)."""
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    b = rng.choice([-3, -2, -1, 1, 2, 3])
    c = rng.choice([-2, -1, 1, 2])

    in_im = rng.choice([True, False])
    x0 = rng.choice([-3, -2, -1, 1, 2, 3])
    y0 = rng.choice([-3, -2, -1, 1, 2, 3])
    if in_im:
        # Queremos a*x0 + b*y0 + c*z0 = 0 con z0 entero: si c in {-1,1} siempre es entero; si c=±2 ajustamos paridad
        if (a * x0 + b * y0) % c != 0:
            x0 *= abs(c)
        z0 = -(a * x0 + b * y0) // c
        expected_class = "SCI"
    else:
        z0 = rng.choice([-3, -2, -1, 1, 2, 3])
        if a * x0 + b * y0 + c * z0 == 0:
            z0 += 1
        expected_class = "SI"

    eq_plane = format_linear_expr([a, b, c], ["x", "y", "z"])
    eval_val = a * x0 + b * y0 + c * z0

    statement = (
        "Sea $f : \\mathbb{R}^3 \\to \\mathbb{R}^3$ una aplicación lineal con matriz asociada $A$ en las bases canónicas, "
        "cuyo subespacio imagen viene dado por el plano:\n\n"
        f"$$ \\operatorname{{Im}}(f) = \\left\\{{ (x, y, z) \\in \\mathbb{{R}}^3 \\mid {eq_plane} = 0 \\right\\}} $$\n\n"
        f"Sin calcular la matriz $A$, determina $\\dim(\\operatorname{{Im}} f)$, $\\dim(\\operatorname{{Ker}} f)$, "
        f"y clasifica el sistema lineal $A \\cdot \\mathbf{{x}} = {vec_to_latex([x0, y0, z0])}^T$."
    )

    steps = [
        f"a) El plano ${eq_plane} = 0$ en $\\mathbb{{R}}^3$ está definido por 1 ecuación lineal independiente, por lo que $\\dim(\\operatorname{{Im}} f) = \\operatorname{{rg}}(A) = 3 - 1 = 2$.",
        "b) Por el teorema de las dimensiones: $\\dim(\\operatorname{Ker} f) = \\dim(\\mathbb{R}^3) - \\dim(\\operatorname{Im} f) = 3 - 2 = 1$.",
        f"c) El sistema $Ax = v$ es compatible si y solo si $v = ({x0}, {y0}, {z0}) \\in \\operatorname{{Im}}(f)$. Sustituimos en la ecuación del plano: "
        f"$({a})({x0}) + ({b})({y0}) + ({c})({z0}) = {eval_val}$.",
        (
            "Como el resultado es $0$, $v \\in \\operatorname{Im}(f)$ ⇒ el sistema es compatible. Además, como $\\operatorname{rg}(A) = 2 < 3$ ($\\dim \\operatorname{Ker} f = 1$), tiene infinitas soluciones (**SCI**)."
            if in_im else
            f"Como ${eval_val} \\neq 0$, $v \\notin \\operatorname{{Im}}(f)$ ⇒ el sistema no tiene solución (**Incompatible, SI**)."
        ),
    ]

    return make_exercise_payload(
        generator_id="tl_nucleo_imagen_compatibilidad",
        topic="aplicaciones_lineales",
        title="Rango, núcleo y compatibilidad a partir del subespacio imagen",
        difficulty="media",
        time_limit_seconds=210,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "dim_im", "label": "a) dim(Im f) = rg(A)", "type": "number", "placeholder": "Entero"},
                {"id": "dim_ker", "label": "b) dim(Ker f)", "type": "number", "placeholder": "Entero"},
                {
                    "id": "sys_class",
                    "label": f"c) Clasificación del sistema Ax = ({x0}, {y0}, {z0})ᵀ",
                    "type": "choice",
                    "options": [
                        {"value": "SCD", "label": "Compatible Determinado (SCD)"},
                        {"value": "SCI", "label": "Compatible Indeterminado (SCI)"},
                        {"value": "SI", "label": "Incompatible (SI)"},
                    ],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "dim_im", "label": "dim(Im f)", "type": "number", "expected": "2"},
                {"id": "dim_ker", "label": "dim(Ker f)", "type": "number", "expected": "1"},
                {"id": "sys_class", "label": "Clasificación de Ax=v", "type": "choice", "expected": expected_class},
            ],
        },
        correct_display=f"$\\dim(\\operatorname{{Im}} f) = 2,\\; \\dim(\\operatorname{{Ker}} f) = 1$, sistema **{expected_class}**.",
        steps_md=steps,
        theory_ref="Tema 4 · Núcleo, Imagen y Teorema de las Dimensiones (07 CO P6 · 09 5.9–5.14)",
        fingerprint_data={"abc": [a, b, c], "v": [x0, y0, z0]},
    )


def gen_tl_dim_ker_im_formula(rng: random.Random) -> dict[str, Any]:
    """Comprobación de linealidad + dimensiones de Ker e Im + clasificación inyectiva/sobreyectiva/isomorfismo."""
    case = rng.choice(["isomorfismo", "rango2_r3_r3", "sobreyectiva_r3_r2", "no_lineal_const"])
    c1 = rng.choice([-2, -1, 1, 2])
    c2 = rng.choice([-2, -1, 1, 2])
    c3 = rng.choice([-3, -2, 2, 3])

    if case == "isomorfismo":
        A = sp.Matrix([[c1, c2, 0], [0, c3, 1], [0, 0, rng.choice([-2, -1, 1, 2])]])
        e1 = format_linear_expr(list(A[0, :]), ["x", "y", "z"])
        e2 = format_linear_expr(list(A[1, :]), ["x", "y", "z"])
        e3 = format_linear_expr(list(A[2, :]), ["x", "y", "z"])
        formula = f"T : \\mathbb{{R}}^3 \\to \\mathbb{{R}}^3, \\quad T(x, y, z) = ({e1},\\; {e2},\\; {e3})"
        expected_type = "isomorfismo"
        dim_ker, dim_im = "0", "3"
        steps = [
            f"$T$ es lineal ($T(0)=0$ y todas sus componentes son combinaciones lineales homogéneas). Su matriz canónica es triangular superior con diagonal no nula: $$ A = {mat_to_latex(A)} $$",
            "$\\operatorname{rg}(A) = 3 \\implies \\dim(\\operatorname{Im} T) = 3$ y $\\dim(\\operatorname{Ker} T) = 3 - 3 = 0$.",
            "Es inyectiva ($\\dim \\operatorname{Ker} = 0$) y sobreyectiva ($\\dim \\operatorname{Im} = 3 = \\dim \\mathbb{R}^3$) ⇒ es un **isomorfismo**.",
        ]
    elif case == "rango2_r3_r3":
        A = sp.Matrix([[1, c1, 0], [0, 1, c2], [1, c1 + 1, c2]])
        e1 = format_linear_expr(list(A[0, :]), ["x", "y", "z"])
        e2 = format_linear_expr(list(A[1, :]), ["x", "y", "z"])
        e3 = format_linear_expr(list(A[2, :]), ["x", "y", "z"])
        formula = f"T : \\mathbb{{R}}^3 \\to \\mathbb{{R}}^3, \\quad T(x, y, z) = ({e1},\\; {e2},\\; {e3})"
        expected_type = "ninguna"
        dim_ker, dim_im = "1", "2"
        steps = [
            f"$T$ es lineal con matriz canónica $$ A = {mat_to_latex(A)} $$",
            "La fila 3 es suma de las filas 1 y 2 ($F_3 = F_1 + F_2$), mientras $F_1, F_2$ son independientes ⇒ $\\operatorname{rg}(A) = 2$.",
            "Por tanto $\\dim(\\operatorname{Im} T) = 2 < 3$ (no sobreyectiva) y $\\dim(\\operatorname{Ker} T) = 3 - 2 = 1 > 0$ (no inyectiva) ⇒ **ninguna de las dos**.",
        ]
    elif case == "sobreyectiva_r3_r2":
        A = sp.Matrix([[c1, 1, c2], [0, c3, -1]])
        e1 = format_linear_expr(list(A[0, :]), ["x", "y", "z"])
        e2 = format_linear_expr(list(A[1, :]), ["x", "y", "z"])
        formula = f"T : \\mathbb{{R}}^3 \\to \\mathbb{{R}}^2, \\quad T(x, y, z) = ({e1},\\; {e2})"
        expected_type = "sobreyectiva"
        dim_ker, dim_im = "1", "2"
        steps = [
            f"$T$ es lineal con matriz canónica $2\\times 3$: $$ A = {mat_to_latex(A)} $$",
            "Tiene 2 pivotes ⇒ $\\dim(\\operatorname{Im} T) = \\operatorname{rg}(A) = 2 = \\dim(\\mathbb{R}^2)$ (**sobreyectiva**).",
            "$\\dim(\\operatorname{Ker} T) = 3 - 2 = 1 \\neq 0$, por tanto **no es inyectiva** (solo sobreyectiva).",
        ]
    else:  # no_lineal_const
        shift = rng.choice([-3, -2, -1, 1, 2, 3])
        e1 = format_linear_expr([c1, c2], ["x", "y"])
        e2 = format_linear_expr([1, c3], ["x", "z"])
        sign_str = f"+ {shift}" if shift > 0 else f"- {abs(shift)}"
        formula = f"T : \\mathbb{{R}}^3 \\to \\mathbb{{R}}^3, \\quad T(x, y, z) = ({e1},\\; {e2} {sign_str},\\; {c2}z)"
        expected_type = "no_lineal"
        dim_ker, dim_im = "na", "na"
        steps = [
            f"Comprobamos primero la condición necesaria $T(0,0,0) = (0,0,0)$: aquí $T(0,0,0) = (0, {shift}, 0) \\neq (0,0,0)$.",
            "Por tanto, **$T$ NO es una aplicación lineal** (es una aplicación afín).",
        ]

    statement = (
        "Estudia la siguiente aplicación $T$:\n\n"
        f"$$ {formula} $$\n\n"
        "Indica si es lineal y clasifícala (inyectiva, sobreyectiva, isomorfismo, ninguna o no lineal), "
        "indicando las dimensiones de su núcleo e imagen cuando proceda."
    )

    return make_exercise_payload(
        generator_id="tl_dim_ker_im_formula",
        topic="aplicaciones_lineales",
        title="Linealidad, núcleo, imagen y clasificación de T",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {
                    "id": "classification",
                    "label": "a) Clasificación de T",
                    "type": "choice",
                    "options": [
                        {"value": "isomorfismo", "label": "Lineal · Isomorfismo (inyectiva y sobreyectiva)"},
                        {"value": "inyectiva", "label": "Lineal · Solo inyectiva"},
                        {"value": "sobreyectiva", "label": "Lineal · Solo sobreyectiva"},
                        {"value": "ninguna", "label": "Lineal · Ni inyectiva ni sobreyectiva"},
                        {"value": "no_lineal", "label": "NO es una aplicación lineal"},
                    ],
                },
                {
                    "id": "dim_ker",
                    "label": "b) dim(Ker T)",
                    "type": "choice",
                    "options": [
                        {"value": "0", "label": "0"},
                        {"value": "1", "label": "1"},
                        {"value": "2", "label": "2"},
                        {"value": "na", "label": "No aplica (no lineal)"},
                    ],
                },
                {
                    "id": "dim_im",
                    "label": "c) dim(Im T)",
                    "type": "choice",
                    "options": [
                        {"value": "1", "label": "1"},
                        {"value": "2", "label": "2"},
                        {"value": "3", "label": "3"},
                        {"value": "na", "label": "No aplica (no lineal)"},
                    ],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "classification", "label": "Clasificación", "type": "choice", "expected": expected_type},
                {"id": "dim_ker", "label": "dim(Ker T)", "type": "choice", "expected": dim_ker},
                {"id": "dim_im", "label": "dim(Im T)", "type": "choice", "expected": dim_im},
            ],
        },
        correct_display=f"Clasificación: **{expected_type}**; $\\dim(\\operatorname{{Ker}} T) = {dim_ker}$; $\\dim(\\operatorname{{Im}} T) = {dim_im}$.",
        steps_md=steps,
        theory_ref="Tema 4 · Linealidad, Ker(T), Im(T) e Isomorfismos (04 Pizarra · 05 Tema 4 Ej. 2–3)",
        fingerprint_data={"case": case, "c1": c1, "c2": c2, "c3": c3},
    )
