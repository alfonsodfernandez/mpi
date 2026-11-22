"""Generadores procedurales para Tema 1: Sistemas de Ecuaciones Lineales (Gauss y discusión)."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import (
    aug_to_latex,
    build_unimodular_matrix,
    fmt_num,
    fmt_plain_num,
    make_exercise_payload,
    mat_to_latex,
    mat_to_plain_rows,
    system_to_latex,
)


def gen_sel_gauss_3x3_scd(rng: random.Random) -> dict[str, Any]:
    """Sistema 3x3 compatible determinado con solución entera única y matriz unimodular."""
    A = build_unimodular_matrix(3, rng, steps=4, coeff_choices=[-2, -1, 1, 2])
    sol = [rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]) for _ in range(3)]
    x_vec = sp.Matrix(sol)
    b = A * x_vec
    aug = A.row_join(b)
    rref_m, _ = aug.rref()

    sys_latex = system_to_latex(A, b, ["x", "y", "z"])
    aug_latex = aug_to_latex(A, b)
    rref_latex = aug_to_latex(rref_m[:, :3], rref_m[:, 3])

    statement = (
        "Resuelve el siguiente sistema de ecuaciones lineales mediante el **método de Gauss-Jordan** "
        "(reducción por filas de la matriz ampliada) e introduce la solución única $(x, y, z)$:\n\n"
        f"$$ {sys_latex} $$"
    )

    steps = [
        f"Escribimos la matriz ampliada del sistema: $$ (A\\mid b) = {aug_latex} $$",
        f"Aplicando operaciones elementales por filas hasta la forma escalonada reducida (Gauss-Jordan) se obtiene: $$ {rref_latex} $$",
        f"Al obtener 3 pivotes en las columnas de coeficientes, el sistema es **Compatible Determinado (SCD)** con solución única: "
        f"$x = {sol[0]},\\; y = {sol[1]},\\; z = {sol[2]}$.",
    ]

    return make_exercise_payload(
        generator_id="sel_gauss_3x3_scd",
        topic="sistemas",
        title="Resolución de sistema 3×3 por Gauss-Jordan",
        difficulty="media",
        time_limit_seconds=300,
        statement_md=statement,
        input_spec={
            "kind": "vector",
            "labels": ["x", "y", "z"],
            "placeholder": "Entero o fracción",
        },
        grading_spec={"kind": "vector", "expected": [str(v) for v in sol]},
        correct_display=f"$(x, y, z) = ({sol[0]}, {sol[1]}, {sol[2]})$",
        steps_md=steps,
        theory_ref="Tema 1 · Sistemas Lineales · Eliminación de Gauss y Gauss-Jordan (02_Teoria + 05 Ej. 1)",
        fingerprint_data={"A": mat_to_plain_rows(A), "b": [str(int(v)) for v in b]},
        protected_canvas={
            "kind": "augmented_matrix",
            "label": "Matriz ampliada (A | b)",
            "left": mat_to_plain_rows(A),
            "right": [fmt_plain_num(v) for v in b],
        },
    )


def gen_sel_parametro_k_2x2(rng: random.Random) -> dict[str, Any]:
    """Discusión de sistema 2x2 con parámetro k mediante Gauss (formato CEX 2025/26 P1)."""
    a11 = rng.choice([1, 2])
    a12 = rng.choice([-3, -2, -1, 1, 2, 3])
    b1 = rng.choice([-4, -3, -2, 1, 2, 3, 4])
    k0 = rng.choice([-4, -3, -2, -1, 2, 3, 4])
    # Fila 2: k*x + a22*y = b2 donde a22 = (k0/a11)*a12 (elegimos k0 múltiplo de a11)
    if k0 % a11 != 0:
        k0 *= a11
    ratio = k0 // a11
    a22 = ratio * a12
    is_sci = rng.choice([True, False])
    if is_sci:
        b2 = ratio * b1
        critical_class = "SCI"
        critical_text = "Compatible Indeterminado (infinitas soluciones)"
        row2_rhs_crit = 0
    else:
        offset = rng.choice([-3, -2, -1, 1, 2, 3])
        b2 = ratio * b1 + offset
        critical_class = "SI"
        critical_text = "Incompatible (sin solución)"
        row2_rhs_crit = offset

    k_sym = sp.Symbol("k")
    A_sym = sp.Matrix([[a11, a12], [k_sym, a22]])
    b_sym = sp.Matrix([b1, b2])
    sys_latex = system_to_latex(A_sym, b_sym, ["x", "y"])

    # Escalonada tras F2 <- a11*F2 - k*F1
    piv2 = sp.expand(a11 * a22 - k_sym * a12)
    rhs2 = sp.expand(a11 * b2 - k_sym * b1)

    statement = (
        "Dado el siguiente sistema lineal dependiente del parámetro real $k$:\n\n"
        f"$$ {sys_latex} $$\n\n"
        "Discute el sistema aplicando **exclusivamente el método de Gauss** (sin determinantes ni Rouché-Fröbenius) "
        "e indica el valor crítico $k_0$ y la clasificación en ambos casos."
    )

    steps = [
        f"Escribimos la matriz ampliada: $$ \\left(\\begin{{array}}{{cc|c}} {a11} & {a12} & {b1} \\\\ k & {a22} & {b2} \\end{{array}}\\right) $$",
        f"Aplicamos $F_2 \\leftarrow {a11}F_2 - k F_1$ para hacer cero debajo del primer pivote: "
        f"$$ \\left(\\begin{{array}}{{cc|c}} {a11} & {a12} & {b1} \\\\ 0 & {sp.latex(piv2)} & {sp.latex(rhs2)} \\end{{array}}\\right) $$",
        f"El segundo pivote se anula cuando ${sp.latex(piv2)} = 0 \\iff k = {k0}$.",
        f"Si $k \\neq {k0}$, hay 2 pivotes en la matriz de coeficientes → **Compatible Determinado (SCD)**.",
        f"Si $k = {k0}$, la segunda fila queda $(0\\; 0 \\mid {a11 * row2_rhs_crit})$, por tanto el sistema es **{critical_text} ({critical_class})**.",
    ]

    return make_exercise_payload(
        generator_id="sel_parametro_k_2x2",
        topic="sistemas",
        title="Discusión de sistema 2×2 con parámetro k (Gauss)",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "k_crit", "label": "Valor crítico k₀ donde se anula el 2.º pivote", "type": "number", "placeholder": "Ej: -2"},
                {
                    "id": "class_eq",
                    "label": "Clasificación cuando k = k₀",
                    "type": "choice",
                    "options": [
                        {"value": "SCD", "label": "SCD (solución única)"},
                        {"value": "SCI", "label": "SCI (infinitas soluciones)"},
                        {"value": "SI", "label": "SI (incompatible)"},
                    ],
                },
                {
                    "id": "class_neq",
                    "label": "Clasificación cuando k ≠ k₀",
                    "type": "choice",
                    "options": [
                        {"value": "SCD", "label": "SCD (solución única)"},
                        {"value": "SCI", "label": "SCI (infinitas soluciones)"},
                        {"value": "SI", "label": "SI (incompatible)"},
                    ],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "k_crit", "label": "Valor crítico k₀", "type": "number", "expected": str(k0)},
                {"id": "class_eq", "label": "Caso k = k₀", "type": "choice", "expected": critical_class},
                {"id": "class_neq", "label": "Caso k ≠ k₀", "type": "choice", "expected": "SCD"},
            ],
        },
        correct_display=f"$k_0 = {k0}$; si $k = {k0}$ es **{critical_class}**; si $k \\neq {k0}$ es **SCD**.",
        steps_md=steps,
        theory_ref="Tema 1 · Discusión de SEL con parámetro por Gauss (08 CEX Mod A/B/C P1 · 09 1.10–1.12)",
        fingerprint_data={"a11": a11, "a12": a12, "b1": b1, "k0": k0, "b2": b2},
        protected_canvas={
            "kind": "augmented_matrix",
            "label": "Matriz ampliada con parámetro k",
            "left": [[str(a11), str(a12)], ["k", str(a22)]],
            "right": [str(b1), str(b2)],
        },
    )


def gen_sel_parametro_k_3x3(rng: random.Random) -> dict[str, Any]:
    """Sistema 3x3 con k² (inspirado en 05 Tema 1 Ej. 5): separa exactamente k_sci, k_si y SCD."""
    # Base triangular superior limpia con pivote 3 = k^2 - c^2 y rhs 3 = k - c
    c = rng.choice([2, 3, 4, 5])
    sign_sci = rng.choice([1, -1])
    k_sci = sign_sci * c
    k_si = -k_sci

    a12 = rng.choice([-2, -1, 1, 2])
    a13 = rng.choice([-3, -2, -1, 1, 2, 3])
    b1 = rng.choice([-2, -1, 1, 2, 3])

    u22 = rng.choice([-2, -1, 1, 2])
    u23 = rng.choice([-2, -1, 1, 2])
    b2_u = rng.choice([-3, -1, 1, 2])

    m21 = rng.choice([-2, -1, 1, 2])
    m31 = rng.choice([-2, -1, 1, 2])
    m32 = rng.choice([-1, 1])

    k_sym = sp.Symbol("k")
    # U_aug tiene fila 1: [1, a12, a13 | b1], fila 2: [0, u22, u23 | b2_u], fila 3: [0, 0, k^2 - c^2 | k - k_sci]
    row1 = [sp.Integer(1), sp.Integer(a12), sp.Integer(a13), sp.Integer(b1)]
    row2 = [m21 * row1[j] + ([0, u22, u23, b2_u][j]) for j in range(4)]
    row3_base = [sp.Integer(0), sp.Integer(0), k_sym**2 - c**2, k_sym - k_sci]
    row3 = [sp.expand(row3_base[j] + m31 * row1[j] + m32 * ([0, u22, u23, b2_u][j])) for j in range(4)]

    A_sym = sp.Matrix([row1[:3], row2[:3], row3[:3]])
    b_sym = sp.Matrix([row1[3], row2[3], row3[3]])
    sys_latex = system_to_latex(A_sym, b_sym, ["x", "y", "z"])

    statement = (
        "Estudia por el **método de Gauss** el siguiente sistema de ecuaciones lineales según los valores del parámetro $k \\in \\mathbb{R}$:\n\n"
        f"$$ {sys_latex} $$\n\n"
        "Determina para qué valor de $k$ el sistema es **Compatible Indeterminado (SCI)** y para qué valor es **Incompatible (SI)**."
    )

    steps = [
        f"Construimos la matriz ampliada y eliminamos la primera columna mediante $F_2 \\leftarrow F_2 - ({m21})F_1$ y $F_3 \\leftarrow F_3 - ({m31})F_1$.",
        f"A continuación eliminamos la segunda columna en la tercera fila mediante $F_3 \\leftarrow F_3 - ({m32})F_2$, obteniendo la forma escalonada: "
        f"$$ \\left(\\begin{{array}}{{ccc|c}} 1 & {a12} & {a13} & {b1} \\\\ 0 & {u22} & {u23} & {b2_u} \\\\ 0 & 0 & k^2 - {c**2} & {sp.latex(k_sym - k_sci)} \\end{{array}}\\right) $$",
        f"El tercer pivote se anula cuando $k^2 - {c**2} = (k - {c})(k + {c}) = 0 \\implies k = {c}$ o $k = -{c}$.",
        f"• Si $k = {k_sci}$: la fila 3 es $(0\\; 0\\; 0 \\mid 0)$ → **Compatible Indeterminado (SCI)**.",
        f"• Si $k = {k_si}$: la fila 3 es $(0\\; 0\\; 0 \\mid {k_si - k_sci})$ (contradicción $0 = {k_si - k_sci}$) → **Incompatible (SI)**.",
        f"• Si $k \\notin \\{{-{c}, {c}\\}}$: hay 3 pivotes → **Compatible Determinado (SCD)**.",
    ]

    return make_exercise_payload(
        generator_id="sel_parametro_k_3x3",
        topic="sistemas",
        title="Discusión completa de sistema 3×3 con parámetro k²",
        difficulty="alta",
        time_limit_seconds=360,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "k_sci", "label": "Valor de k para el que el sistema es SCI (infinitas soluciones)", "type": "number", "placeholder": "Entero"},
                {"id": "k_si", "label": "Valor de k para el que el sistema es SI (incompatible)", "type": "number", "placeholder": "Entero"},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "k_sci", "label": "k para SCI", "type": "number", "expected": str(k_sci)},
                {"id": "k_si", "label": "k para SI", "type": "number", "expected": str(k_si)},
            ],
        },
        correct_display=f"SCI para $k = {k_sci}$; SI para $k = {k_si}$; SCD para $k \\neq \\pm {c}$.",
        steps_md=steps,
        theory_ref="Tema 1 · Discusión con parámetro sin Rouché (05 Tema 1 Ej. 5 · 09 1.13–1.15)",
        fingerprint_data={"c": c, "k_sci": k_sci, "a12": a12, "a13": a13, "u22": u22, "m21": m21, "m31": m31},
        protected_canvas={
            "kind": "augmented_matrix",
            "label": "Matriz ampliada (A(k) | b(k))",
            "left": [[str(A_sym[i, j]) for j in range(3)] for i in range(3)],
            "right": [str(b_sym[i, 0]) for i in range(3)],
        },
    )


def gen_sel_lectura_escalonada(rng: random.Random) -> dict[str, Any]:
    """Lectura de una matriz 4x4 como ampliada o de coeficientes (formato exacto CO 2025/26 P2)."""
    scenario = rng.choice(["rref_fail_pivot", "echelon_valid", "echelon_fail_neg1", "consistent_sci"])
    c1 = rng.choice([-2, -1, 0, 1, 2])
    c2 = rng.choice([-3, -2, 1, 2, 3])
    c3 = rng.choice([2, 3, 4])

    if scenario == "rref_fail_pivot":
        M = sp.Matrix([
            [1, 0, 0, c3],
            [0, 1, c1 or 1, c2],
            [0, 0, 0, c3],
            [0, 0, 0, 0],
        ])
        q_a = "Está en forma escalonada reducida por filas."
        ans_a = False
        exp_a = f"Falsa: el coeficiente principal de la fila 3 es {c3} (distinto de 1) y hay entradas no nulas encima de él."
        ans_b = False
        exp_b = f"Falsa: como ampliada de 4 ecuaciones y 3 incógnitas, la fila 3 dice $0 = {c3}$ (incompatible)."
        ans_c = True
        exp_c = f"Verdadera: tiene 4 filas y 3+1 columnas, y la fila 3 expresa la contradicción $0 = {c3}$."
        ans_d = True
        exp_d = "Verdadera: como matriz de coeficientes 4×4 tiene una fila nula; eligiendo $b_4 \\neq 0$ resulta incompatible."
    elif scenario == "echelon_valid":
        M = sp.Matrix([
            [1, 0, c1 or 2, 0],
            [0, 1, c2, c3],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
        ])
        q_a = "Está en forma escalonada por filas (según la convención del curso: pivotes iguales a 1)."
        ans_a = True
        exp_a = "Verdadera: todos los pivotes valen 1, avanzan estrictamente a la derecha y la fila nula está al final."
        ans_b = False
        exp_b = "Falsa: la fila 3 expresa $0 = 1$, por lo que el sistema ampliado es incompatible."
        ans_c = True
        exp_c = "Verdadera: dimensiones 4×(3+1) y contradicción $0 = 1$ en la tercera fila."
        ans_d = True
        exp_d = "Verdadera: tiene fila nula abajo; si el término independiente $b_4 \\neq 0$, el sistema es incompatible."
    elif scenario == "echelon_fail_neg1":
        M = sp.Matrix([
            [1, 0, c1 or 2, 0],
            [0, 0, 1, c2],
            [0, 0, 0, -1],
            [0, 0, 0, 0],
        ])
        q_a = "Está en forma escalonada por filas (según la convención del curso: pivotes iguales a 1)."
        ans_a = False
        exp_a = "Falsa: el primer elemento no nulo de la fila 3 es $-1 \\neq 1$."
        ans_b = False
        exp_b = "Falsa: la fila 3 implica $0 = -1$ (sistema incompatible)."
        ans_c = True
        exp_c = "Verdadera: como matriz ampliada 4×4 (3 incógnitas), la fila 3 contradice la compatibilidad."
        ans_d = True
        exp_d = "Verdadera: como matriz de coeficientes 4×4 tiene última fila nula, pudiendo ser incompatible si $b_4 \\neq 0$."
    else:  # consistent_sci
        M = sp.Matrix([
            [1, 0, c1 or 2, c2],
            [0, 1, -1, c3],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        q_a = "Está en forma escalonada reducida por filas."
        ans_a = True
        exp_a = "Verdadera: los pivotes son 1 en columnas 1 y 2, con ceros encima y debajo, y las filas nulas al final."
        ans_b = True
        exp_b = "Verdadera: sin fila contradictoria y con 2 pivotes para 3 incógnitas, queda 1 variable libre (SCI)."
        ans_c = False
        exp_c = "Falsa: no aparece ninguna fila del tipo $(0\\; 0\\; 0 \\mid c)$ con $c \\neq 0$, luego es compatible."
        ans_d = True
        exp_d = "Verdadera: como matriz de coeficientes 4×4 tiene filas nulas, así que eligiendo $b_3 \\neq 0$ sería incompatible."

    statement = (
        "Analiza la siguiente matriz $M \\in \\mathcal{M}_{4\\times 4}(\\mathbb{R})$ e indica si cada afirmación es **Verdadera (V)** o **Falsa (F)** "
        "siguiendo la definición de forma escalonada del curso (pivotes iguales a 1):\n\n"
        f"$$ M = {mat_to_latex(M)} $$"
    )

    items = [
        {"id": "a", "text": f"a) {q_a}"},
        {"id": "b", "text": "b) Podría ser la matriz ampliada de un sistema de 4 ecuaciones y 3 incógnitas con infinitas soluciones (SCI)."},
        {"id": "c", "text": "c) Podría ser la matriz ampliada de un sistema de 4 ecuaciones y 3 incógnitas incompatible (SI)."},
        {"id": "d", "text": "d) Podría ser la matriz de coeficientes de un sistema de 4 ecuaciones y 4 incógnitas incompatible (SI)."},
    ]

    expected = {"a": ans_a, "b": ans_b, "c": ans_c, "d": ans_d}
    disp = ", ".join(f"{k}) {'V' if v else 'F'}" for k, v in expected.items())

    return make_exercise_payload(
        generator_id="sel_lectura_escalonada",
        topic="sistemas",
        title="Lectura e interpretación de matriz escalonada (V/F)",
        difficulty="media",
        time_limit_seconds=210,
        statement_md=statement,
        input_spec={"kind": "multi_tf", "items": items},
        grading_spec={"kind": "multi_tf", "expected": expected},
        correct_display=disp,
        steps_md=[f"a) {exp_a}", f"b) {exp_b}", f"c) {exp_c}", f"d) {exp_d}"],
        theory_ref="Tema 1 · Forma escalonada y escalonada reducida (07 CO P2 · 09 1.7–1.9)",
        fingerprint_data={"scenario": scenario, "M": mat_to_plain_rows(M)},
        protected_canvas={"kind": "matrix", "label": "Matriz M (4×4)", "rows": mat_to_plain_rows(M)},
    )


def gen_sel_rango_gauss_teorico(rng: random.Random) -> dict[str, Any]:
    """Propiedades de rango, invertibilidad y unicidad a partir de forma escalonada (CO P1 / CEX P2)."""
    n = rng.choice([3, 4, 5, 6])
    zero_rows = rng.choice([0, 1, 2])
    if zero_rows >= n - 1:
        zero_rows = 1
    rank_val = n - zero_rows
    nullity_val = zero_rows
    is_inv = "si" if rank_val == n else "no"
    unique_b = "si" if rank_val == n else "no"

    statement = (
        f"Sea $A$ una matriz cuadrada de orden ${n} \\times {n}$ tal que, al aplicarle el método de Gauss, "
        f"se obtiene una matriz escalonada equivalente $U$ con exactamente **${rank_val}$ filas no nulas** "
        f"(y ${zero_rows}$ fila(s) nula(s)). Responde razonadamente:"
    )

    steps = [
        f"a) Las operaciones elementales por filas preservan el rango. Cada fila no nula de la escalonada $U$ contiene exactamente un pivote, luego $\\operatorname{{rg}}(A) = {rank_val}$.",
        f"b) Por el teorema del rango-nulidad, $\\nu(A) = n - \\operatorname{{rg}}(A) = {n} - {rank_val} = {nullity_val}$.",
        (
            f"c) Como $\\operatorname{{rg}}(A) = {n}$ (rango máximo), $A$ **sí es invertible** ($|A| \\neq 0$)."
            if rank_val == n
            else f"c) Una matriz cuadrada ${n}\\times {n}$ es invertible sii su rango es ${n}$. Como $\\operatorname{{rg}}(A) = {rank_val} < {n}$, $A$ **no es invertible** ($|A| = 0$)."
        ),
        (
            f"d) Al ser $A$ invertible, para cualquier $b \\in \\mathbb{{R}}^{n}$ el sistema $Ax = b$ tiene **solución única** $x = A^{{-1}}b$."
            if rank_val == n
            else "d) Al tener $U$ fila(s) nula(s), $Ax = b$ nunca puede tener $n$ pivotes: solo puede ser incompatible (si queda contradicción en la ampliada) o compatible indeterminado. **No existe** ningún $b$ con solución única."
        ),
    ]

    return make_exercise_payload(
        generator_id="sel_rango_gauss_teorico",
        topic="sistemas",
        title="Rango, nulidad e invertibilidad desde Gauss",
        difficulty="baja",
        time_limit_seconds=180,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "rank", "label": "a) Rango de A, rg(A)", "type": "number", "placeholder": "Entero"},
                {"id": "nullity", "label": "b) Nulidad de A, ν(A) = dim(Ker A)", "type": "number", "placeholder": "Entero"},
                {
                    "id": "invertible",
                    "label": "c) ¿Es A invertible?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, es invertible"}, {"value": "no", "label": "No es invertible"}],
                },
                {
                    "id": "unique_sol",
                    "label": "d) ¿Existe algún vector b para el que Ax = b tenga solución única?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí (de hecho para todo b)"}, {"value": "no", "label": "No existe ningún b"}],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "rank", "label": "rg(A)", "type": "number", "expected": str(rank_val)},
                {"id": "nullity", "label": "ν(A)", "type": "number", "expected": str(nullity_val)},
                {"id": "invertible", "label": "Invertibilidad", "type": "choice", "expected": is_inv},
                {"id": "unique_sol", "label": "Unicidad de Ax=b", "type": "choice", "expected": unique_b},
            ],
        },
        correct_display=f"$\\operatorname{{rg}}(A)={rank_val}$, $\\nu(A)={nullity_val}$, Invertible: {is_inv.upper()}, Solución única para algún $b$: {unique_b.upper()}.",
        steps_md=steps,
        theory_ref="Tema 1–2 · Teorema de equivalencias y forma escalonada (07 CO P1 · 08 CEX P2 · 09 4.7–4.9)",
        fingerprint_data={"n": n, "rank": rank_val, "salt": rng.randint(1, 999999)},
    )
