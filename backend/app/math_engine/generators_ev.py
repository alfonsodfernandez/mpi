"""Generadores procedurales para Tema 3: Espacios Vectoriales, Bases, Cambio de Base y Rango/Nulidad."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import (
    build_unimodular_matrix,
    fmt_num,
    fmt_plain_num,
    format_linear_expr,
    make_exercise_payload,
    mat_to_latex,
    mat_to_plain_rows,
    vec_to_latex,
)


def gen_ev_dependencia_parametro(rng: random.Random) -> dict[str, Any]:
    """Valor de k para que un conjunto de 3 vectores en R³ sea linealmente dependiente (05 Tema 3 Ej. 1)."""
    # Construimos v1, v2 LI y v3 = alpha*v1 + beta*v2 excepto una componente que reemplazamos por k
    v1 = [rng.choice([-2, -1, 1, 2, 3]), rng.choice([-2, -1, 1, 2]), rng.choice([-2, -1, 1, 2])]
    v2 = [rng.choice([-2, -1, 1, 2]), rng.choice([-3, -2, -1, 1, 2, 3]), rng.choice([-2, -1, 1, 2])]
    # Asegurar que v1, v2 no son proporcionales y que el menor 2x2 superior es no nulo
    while v1[0] * v2[1] - v1[1] * v2[0] == 0:
        v2[1] += 1
    alpha = rng.choice([-2, -1, 1, 2])
    beta = rng.choice([-2, -1, 1, 2])
    v3_dep = [alpha * v1[i] + beta * v2[i] for i in range(3)]
    k_val = v3_dep[2]

    M_sym = sp.Matrix([
        [v1[0], v2[0], v3_dep[0]],
        [v1[1], v2[1], v3_dep[1]],
        [v1[2], v2[2], sp.Symbol("k")],
    ])
    det_expr = sp.expand(M_sym.det())

    statement = (
        "Determina el valor del parámetro real $k$ para que el siguiente conjunto de vectores de $\\mathbb{R}^3$ "
        "sea **linealmente dependiente**:\n\n"
        f"$$ S = \\left\\{{ v_1 = {vec_to_latex(v1)},\\; v_2 = {vec_to_latex(v2)},\\; v_3 = ({v3_dep[0]},\\, {v3_dep[1]},\\, k) \\right\\}} $$"
    )

    steps = [
        "Tres vectores en $\\mathbb{R}^3$ son linealmente dependientes si y solo si el rango de la matriz formada por sus columnas es menor que 3 (equivalentemente, su determinante es cero o aparece una fila nula en Gauss).",
        f"Planteamos la matriz con los vectores por columnas: $$ M = {mat_to_latex(M_sym)} $$",
        f"Calculando el determinante (o escalonando por Gauss): $\\det(M) = {sp.latex(det_expr)} = 0$.",
        f"Despejando $k$ obtenemos $k = {k_val}$. De hecho, para $k = {k_val}$ se cumple $v_3 = ({alpha})v_1 + ({beta})v_2$.",
    ]

    return make_exercise_payload(
        generator_id="ev_dependencia_parametro",
        topic="espacios_vectoriales",
        title="Dependencia lineal de vectores con parámetro k",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={"kind": "number", "label": "Valor de k para dependencia lineal", "placeholder": "Entero o fracción"},
        grading_spec={"kind": "number", "expected": str(k_val)},
        correct_display=f"$k = {k_val}$ (entonces $v_3 = ({alpha})v_1 + ({beta})v_2$).",
        steps_md=steps,
        theory_ref="Tema 3 · Independencia lineal (03 Pizarra · 05 Tema 3 Ej. 1)",
        fingerprint_data={"v1": v1, "v2": v2, "a": alpha, "b": beta},
        protected_canvas={
            "kind": "matrix",
            "label": "Vectores por columnas",
            "rows": [[str(v1[0]), str(v2[0]), str(v3_dep[0])], [str(v1[1]), str(v2[1]), str(v3_dep[1])], [str(v1[2]), str(v2[2]), "k"]],
        },
    )


def gen_ev_base_y_coordenadas(rng: random.Random) -> dict[str, Any]:
    """Comprobar base en R³ y calcular coordenadas de u respecto de B (08 CEX P4 / 05 Tema 3 Ej. 7)."""
    B = build_unimodular_matrix(3, rng, steps=3, coeff_choices=[-2, -1, 1, 2])
    coords = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(3)]
    u = B * sp.Matrix(coords)

    v1 = [int(B[i, 0]) for i in range(3)]
    v2 = [int(B[i, 1]) for i in range(3)]
    v3 = [int(B[i, 2]) for i in range(3)]
    u_list = [int(u[i, 0]) for i in range(3)]

    statement = (
        "Considera el conjunto de vectores $B = \\{v_1, v_2, v_3\\}$ de $\\mathbb{R}^3$:\n\n"
        f"$$ v_1 = {vec_to_latex(v1)},\\qquad v_2 = {vec_to_latex(v2)},\\qquad v_3 = {vec_to_latex(v3)} $$\n\n"
        f"Se sabe que $B$ es una base de $\\mathbb{{R}}^3$. Calcula las **coordenadas** $(c_1, c_2, c_3)$ del vector "
        f"$u = {vec_to_latex(u_list)}$ respecto de la base $B$ (es decir, $u = c_1 v_1 + c_2 v_2 + c_3 v_3$)."
    )

    steps = [
        f"Colocando los vectores de $B$ como columnas obtenemos la matriz $P_B = {mat_to_latex(B)}$. Su determinante es $|P_B| = {int(B.det())} \\neq 0$ (3 pivotes por Gauss), confirmando que es base de $\\mathbb{{R}}^3$.",
        f"Las coordenadas $(c_1, c_2, c_3)$ satisfacen el sistema $P_B \\cdot c = u$: $$ {mat_to_latex(B)} \\begin{{pmatrix}} c_1 \\\\ c_2 \\\\ c_3 \\end{{pmatrix}} = {mat_to_latex(u)} $$",
        f"Resolviendo por Gauss-Jordan (o multiplicando por $P_B^{{-1}}$) resulta: $c_1 = {coords[0]},\\; c_2 = {coords[1]},\\; c_3 = {coords[2]}$.",
        f"Comprobación: $({coords[0]}){vec_to_latex(v1)} + ({coords[1]}){vec_to_latex(v2)} + ({coords[2]}){vec_to_latex(v3)} = {vec_to_latex(u_list)}$.",
    ]

    return make_exercise_payload(
        generator_id="ev_base_y_coordenadas",
        topic="espacios_vectoriales",
        title="Coordenadas de un vector respecto de una base de ℝ³",
        difficulty="media",
        time_limit_seconds=300,
        statement_md=statement,
        input_spec={"kind": "vector", "labels": ["c₁", "c₂", "c₃"]},
        grading_spec={"kind": "vector", "expected": [str(c) for c in coords]},
        correct_display=f"$(u)_B = ({coords[0]},\\, {coords[1]},\\, {coords[2]})$",
        steps_md=steps,
        theory_ref="Tema 3 · Bases y coordenadas (03 Pizarra · 08 CEX P4 · 09 4.28–4.30)",
        fingerprint_data={"B": mat_to_plain_rows(B), "c": coords},
        protected_canvas={
            "kind": "augmented_matrix",
            "label": "Sistema (B | u)",
            "left": mat_to_plain_rows(B),
            "right": [str(x) for x in u_list],
        },
    )


def gen_ev_subespacio_dim_nucleo(rng: random.Random) -> dict[str, Any]:
    """Decidir si W es subespacio vectorial y hallar su dimensión (07 CO P4 / 09 4.4–4.15)."""
    variant = rng.choice(["homog_1eq_R3", "homog_2eq_indep_R4", "homog_2eq_dep_R4", "non_homog_trap", "nonlinear_trap"])
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    b = rng.choice([-3, -2, -1, 1, 2, 3])
    c = rng.choice([-3, -2, -1, 1, 2, 3])
    d = rng.choice([-3, -2, 1, 2, 3])

    if variant == "homog_1eq_R3":
        eq = format_linear_expr([a, b, c], ["x", "y", "z"])
        desc = f"W = \\{{ (x, y, z) \\in \\mathbb{{R}}^3 \\mid {eq} = 0 \\}}"
        is_sev = "si"
        dim_ans = 2
        steps = [
            f"$W$ es el conjunto de soluciones de una ecuación lineal homogénea: contiene a $(0,0,0)$ y es cerrado para la suma y el producto por escalares. Por tanto **sí es un subespacio vectorial** de $\\mathbb{{R}}^3$.",
            f"Al estar definido en $\\mathbb{{R}}^3$ por $1$ ecuación lineal independiente, $\\dim(W) = 3 - 1 = 2$ (un plano que pasa por el origen).",
        ]
    elif variant == "homog_2eq_indep_R4":
        eq1 = format_linear_expr([1, a, 0, b], ["x", "y", "z", "t"])
        eq2 = format_linear_expr([0, 1, c, d], ["x", "y", "z", "t"])
        desc = f"W = \\{{ (x, y, z, t) \\in \\mathbb{{R}}^4 \\mid {eq1} = 0,\\; {eq2} = 0 \\}}"
        is_sev = "si"
        dim_ans = 2
        steps = [
            "$W$ es el espacio nulo (núcleo) de un sistema lineal homogéneo de 2 ecuaciones en $\\mathbb{R}^4$ ⇒ **sí es subespacio vectorial**.",
            "La matriz de coeficientes tiene pivotes en las columnas 1 y 2 (2 ecuaciones linealmente independientes), luego $\\dim(W) = 4 - 2 = 2$.",
        ]
    elif variant == "homog_2eq_dep_R4":
        mult = rng.choice([-3, -2, 2, 3])
        eq1 = format_linear_expr([a, b, c, d], ["x", "y", "z", "t"])
        eq2 = format_linear_expr([mult * a, mult * b, mult * c, mult * d], ["x", "y", "z", "t"])
        desc = f"W = \\{{ (x, y, z, t) \\in \\mathbb{{R}}^4 \\mid {eq1} = 0,\\; {eq2} = 0 \\}}"
        is_sev = "si"
        dim_ans = 3
        steps = [
            "$W$ es solución de un sistema lineal homogéneo ⇒ **sí es subespacio vectorial** de $\\mathbb{R}^4$.",
            f"¡Cuidado! La segunda ecuación es exactamente ${mult}$ veces la primera (ecuación redundante). Solo hay **1 ecuación linealmente independiente**, luego $\\dim(W) = 4 - 1 = 3$.",
        ]
    elif variant == "non_homog_trap":
        rhs = rng.choice([-5, -3, -2, 1, 2, 4, 5])
        eq = format_linear_expr([a, b, c], ["x", "y", "z"])
        desc = f"W = \\{{ (x, y, z) \\in \\mathbb{{R}}^3 \\mid {eq} = {rhs} \\}}"
        is_sev = "no"
        dim_ans = -1  # sentinel N/A
        steps = [
            f"Comprobamos si el vector nulo pertenece a $W$: al sustituir $(0,0,0)$ obtenemos $0 = {rhs}$, lo cual es falso.",
            "Todo subespacio vectorial debe contener al vector nulo. Por tanto, **$W$ NO es un subespacio vectorial** (es un plano afín desplazado).",
        ]
    else:  # nonlinear_trap: xy = 0 or x^2 - y^2 = 0
        desc = "W = \\{ (x, y, z) \\in \\mathbb{R}^3 \\mid x \\cdot y = 0 \\}"
        is_sev = "no"
        dim_ans = -1
        steps = [
            "Aunque $(0,0,0) \\in W$ (condición necesaria, pero NO suficiente), $W$ no es cerrado bajo la suma.",
            "Contraejemplo: $u = (1,0,0) \\in W$ y $v = (0,1,0) \\in W$, pero $u + v = (1,1,0)$ cumple $1 \\cdot 1 = 1 \\neq 0$, luego $u + v \\notin W$. **$W$ NO es subespacio vectorial**.",
        ]

    statement = (
        "Considera el subconjunto $W$ definido por:\n\n"
        f"$$ {desc} $$\n\n"
        "Determina si $W$ es un **subespacio vectorial** y, en caso afirmativo, indica su **dimensión** "
        "(si no es subespacio, selecciona *No aplica*)."
    )

    dim_choice = "na" if is_sev == "no" else str(dim_ans)

    return make_exercise_payload(
        generator_id="ev_subespacio_dim_nucleo",
        topic="espacios_vectoriales",
        title="Identificación de subespacios vectoriales y su dimensión",
        difficulty="baja",
        time_limit_seconds=180,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {
                    "id": "is_sev",
                    "label": "a) ¿Es W un subespacio vectorial?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, es subespacio vectorial"}, {"value": "no", "label": "No es subespacio vectorial"}],
                },
                {
                    "id": "dim",
                    "label": "b) Dimensión de W",
                    "type": "choice",
                    "options": [
                        {"value": "0", "label": "dim(W) = 0"},
                        {"value": "1", "label": "dim(W) = 1"},
                        {"value": "2", "label": "dim(W) = 2"},
                        {"value": "3", "label": "dim(W) = 3"},
                        {"value": "na", "label": "No aplica (no es subespacio)"},
                    ],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "is_sev", "label": "¿Es subespacio?", "type": "choice", "expected": is_sev},
                {"id": "dim", "label": "Dimensión", "type": "choice", "expected": dim_choice},
            ],
        },
        correct_display=("Sí es subespacio, $\\dim(W) = " + str(dim_ans) + "$." if is_sev == "si" else "No es subespacio vectorial (No aplica dimensión)."),
        steps_md=steps,
        theory_ref="Tema 3 · Subespacios vectoriales y ecuaciones cartesianas (03 Pizarra · 07 CO P4 · 09 4.4–4.15)",
        fingerprint_data={"variant": variant, "a": a, "b": b, "c": c, "d": d},
    )


def gen_ev_cambio_base(rng: random.Random) -> dict[str, Any]:
    """Matriz de cambio de base C_{B1}^{B2} = B2^{-1} B1 en R² (03 Pizarra Cambio de Base / 05 Ej. 10)."""
    B1 = build_unimodular_matrix(2, rng, steps=3, coeff_choices=[-2, -1, 1, 2])
    B2 = build_unimodular_matrix(2, rng, steps=3, coeff_choices=[-2, -1, 1, 2])
    while B1 == B2:
        B2 = build_unimodular_matrix(2, rng, steps=3, coeff_choices=[-2, -1, 1, 2])

    P = B2.inv() * B1  # transforma coordenadas de B1 a B2: (v)_{B2} = P (v)_{B1}

    u1, u2 = [int(B1[0, 0]), int(B1[1, 0])], [int(B1[0, 1]), int(B1[1, 1])]
    w1, w2 = [int(B2[0, 0]), int(B2[1, 0])], [int(B2[0, 1]), int(B2[1, 1])]

    statement = (
        "En $\\mathbb{R}^2$ se consideran dos bases:\n\n"
        f"$$ B_1 = \\left\\{{ {vec_to_latex(u1)},\\; {vec_to_latex(u2)} \\right\\}}, \\qquad "
        f"B_2 = \\left\\{{ {vec_to_latex(w1)},\\; {vec_to_latex(w2)} \\right\\}} $$\n\n"
        "Calcula la **matriz de cambio de base $C_{B_1}^{B_2}$** que transforma las coordenadas de un vector "
        "desde la base $B_1$ a la base $B_2$, es decir, $(v)_{B_2} = C_{B_1}^{B_2} \\cdot (v)_{B_1}$."
    )

    steps = [
        f"Formamos las matrices cuyas columnas son los vectores de cada base en la canónica: "
        f"$$ B_1 = {mat_to_latex(B1)}, \\qquad B_2 = {mat_to_latex(B2)} $$",
        f"Como $B_1 (v)_{{B_1}} = (v)_{{B_c}} = B_2 (v)_{{B_2}}$, despejando se tiene $C_{{B_1}}^{{B_2}} = B_2^{{-1}} B_1$.",
        f"Calculamos $B_2^{{-1}} = {mat_to_latex(B2.inv())}$ (determinante $|B_2| = {int(B2.det())}$).",
        f"Multiplicando: $$ C_{{B_1}}^{{B_2}} = B_2^{{-1}} B_1 = {mat_to_latex(B2.inv())} {mat_to_latex(B1)} = {mat_to_latex(P)} $$",
    ]

    return make_exercise_payload(
        generator_id="ev_cambio_base",
        topic="espacios_vectoriales",
        title="Matriz de cambio de base entre dos bases de ℝ²",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={"kind": "matrix", "rows": 2, "cols": 2, "label": "Matriz C(B₁ → B₂)"},
        grading_spec={"kind": "matrix", "expected": mat_to_plain_rows(P)},
        correct_display=f"$$ C_{{B_1}}^{{B_2}} = {mat_to_latex(P)} $$",
        steps_md=steps,
        theory_ref="Tema 3 · Cambio de base (03 Pizarra Cambio de Base · 05 Tema 3 Ej. 10)",
        fingerprint_data={"B1": mat_to_plain_rows(B1), "B2": mat_to_plain_rows(B2)},
        protected_canvas={"kind": "matrix", "label": "Base B₁ | Base B₂", "rows": mat_to_plain_rows(B1.row_join(B2))},
    )


def gen_ev_rango_nulidad_col(rng: random.Random) -> dict[str, Any]:
    """Pertenencia al núcleo y al espacio columna + Teorema del rango (09 4.19–4.24)."""
    # Construimos A (3x3) de rango 2 con columnas c1, c2 LI y c3 = p*c1 + q*c2
    c1 = sp.Matrix([rng.choice([1, 2]), rng.choice([-2, -1, 1, 2]), rng.choice([-2, -1, 1, 2])])
    c2 = sp.Matrix([rng.choice([-1, 0, 1]), rng.choice([1, 2]), rng.choice([-2, -1, 1, 2])])
    while c1.cross(c2).is_zero_matrix:
        c2[2] += 1
    p = rng.choice([-2, -1, 1, 2])
    q = rng.choice([-2, -1, 1, 2])
    c3 = p * c1 + q * c2
    A = c1.row_join(c2).row_join(c3)

    # Vector candidato para Ker(A): [p, q, -1] está en Ker(A)
    in_ker = rng.choice([True, False])
    v_ker = sp.Matrix([p, q, -1]) if in_ker else sp.Matrix([p, q, 1])
    if not in_ker and (A * v_ker).is_zero_matrix:
        v_ker = sp.Matrix([p + 1, q, -1])

    # Vector candidato para Col(A)
    in_col = rng.choice([True, False])
    a_c, b_c = rng.choice([-2, -1, 1, 2]), rng.choice([-1, 1, 2])
    if in_col:
        v_col = a_c * c1 + b_c * c2
    else:
        normal = c1.cross(c2)
        v_col = a_c * c1 + b_c * c2 + sp.Matrix([1 if normal[0] != 0 else 0, 1 if normal[0] == 0 and normal[1] != 0 else 0, 1 if normal[0] == 0 and normal[1] == 0 else 0])

    Ax_ker = A * v_ker
    aug_col = A.row_join(v_col)
    rref_col, pivots_col = aug_col.rref()

    statement = (
        "Sea la matriz $A \\in \\mathcal{M}_{3\\times 3}(\\mathbb{R})$:\n\n"
        f"$$ A = {mat_to_latex(A)} $$\n\n"
        f"y los vectores $u = {vec_to_latex(v_ker)}$ y $w = {vec_to_latex(v_col)}$. Determina:"
    )

    steps = [
        f"a) Calculamos $A \\cdot u = {mat_to_latex(Ax_ker)}$. " + (
            "Como $Au = 0$, el vector **$u$ sí pertenece al núcleo** $N(A)$."
            if in_ker else "Como $Au \\neq 0$, el vector **$u$ NO pertenece al núcleo** $N(A)$."
        ),
        f"b) Para saber si $w \\in C(A)$ comprobamos si el sistema $Ax = w$ es compatible. Escalonando $(A \\mid w)$ resulta: "
        f"$$ {mat_to_latex(rref_col)} $$ " + (
            f"El sistema es compatible (no hay pivote en la última columna), luego **$w$ sí pertenece a $C(A)$** (en concreto $w = ({a_c})c_1 + ({b_c})c_2$)."
            if in_col else "Aparece un pivote en la última columna (ecuación $0=1$), sistema incompatible ⇒ **$w$ NO pertenece a $C(A)$**."
        ),
        f"c) Como $c_3 = ({p})c_1 + ({q})c_2$ y $c_1, c_2$ son linealmente independientes, $\\operatorname{{rg}}(A) = 2$ y por el teorema del rango $\\nu(A) = 3 - 2 = 1$.",
    ]

    return make_exercise_payload(
        generator_id="ev_rango_nulidad_col",
        topic="espacios_vectoriales",
        title="Pertenencia a Ker(A) y Col(A), rango y nulidad",
        difficulty="media",
        time_limit_seconds=270,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {
                    "id": "in_ker",
                    "label": "a) ¿Pertenece u al núcleo N(A)?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, u ∈ N(A)"}, {"value": "no", "label": "No, u ∉ N(A)"}],
                },
                {
                    "id": "in_col",
                    "label": "b) ¿Pertenece w al espacio columna C(A)?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, w ∈ C(A)"}, {"value": "no", "label": "No, w ∉ C(A)"}],
                },
                {"id": "rank", "label": "c) Rango de A, rg(A)", "type": "number", "placeholder": "Entero"},
                {"id": "nullity", "label": "d) Nulidad de A, ν(A)", "type": "number", "placeholder": "Entero"},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "in_ker", "label": "u ∈ N(A)", "type": "choice", "expected": "si" if in_ker else "no"},
                {"id": "in_col", "label": "w ∈ C(A)", "type": "choice", "expected": "si" if in_col else "no"},
                {"id": "rank", "label": "rg(A)", "type": "number", "expected": "2"},
                {"id": "nullity", "label": "ν(A)", "type": "number", "expected": "1"},
            ],
        },
        correct_display=f"$u \\in N(A)$: {'Sí' if in_ker else 'No'}; $w \\in C(A)$: {'Sí' if in_col else 'No'}; $\\operatorname{{rg}}(A)=2$; $\\nu(A)=1$.",
        steps_md=steps,
        theory_ref="Tema 3 · Núcleo, espacio columna y Teorema del Rango (03 Pizarra · 09 4.19–4.24)",
        fingerprint_data={"A": mat_to_plain_rows(A), "u": [int(x) for x in v_ker], "w": [int(x) for x in v_col]},
        protected_canvas={"kind": "matrix", "label": "Matriz A (3×3)", "rows": mat_to_plain_rows(A)},
    )
