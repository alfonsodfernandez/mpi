"""Generadores procedurales para Tema 2: Matrices, Inversas, Elementales, LU y Determinantes."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import (
    build_unimodular_matrix,
    fmt_num,
    fmt_plain_num,
    make_exercise_payload,
    mat_to_latex,
    mat_to_plain_rows,
)


def gen_mat_elemental_inversa(rng: random.Random) -> dict[str, Any]:
    """Matriz producto de 2 operaciones elementales y cálculo de su inversa (CO 2025/26 P3)."""
    c1 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    c2 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    variant = rng.choice(["col1_below", "col3_above", "chain_23"])

    if variant == "col1_below":
        # F2 <- F2 + c1 F1 y F3 <- F3 + c2 F1 (conmutan)
        A = sp.Matrix([[1, 0, 0], [c1, 1, 0], [c2, 0, 1]])
        ops_desc = f"$F_2 \\leftarrow F_2 + ({c1})F_1$ y $F_3 \\leftarrow F_3 + ({c2})F_1$"
        inv_desc = f"$F_3 \\leftarrow F_3 + ({-c2})F_1$ y $F_2 \\leftarrow F_2 + ({-c1})F_1$"
    elif variant == "col3_above":
        # F1 <- F1 + c1 F3 y F2 <- F2 + c2 F3
        A = sp.Matrix([[1, 0, c1], [0, 1, c2], [0, 0, 1]])
        ops_desc = f"$F_1 \\leftarrow F_1 + ({c1})F_3$ y $F_2 \\leftarrow F_2 + ({c2})F_3$"
        inv_desc = f"$F_2 \\leftarrow F_2 + ({-c2})F_3$ y $F_1 \\leftarrow F_1 + ({-c1})F_3$"
    else:
        # E2 * E1 donde E1: F2 <- F2 + c1 F1, luego E2: F3 <- F3 + c2 F2
        E1 = sp.Matrix([[1, 0, 0], [c1, 1, 0], [0, 0, 1]])
        E2 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, c2, 1]])
        A = E2 * E1
        ops_desc = f"primero $F_2 \\leftarrow F_2 + ({c1})F_1$ y después $F_3 \\leftarrow F_3 + ({c2})F_2$"
        inv_desc = f"deshacer en orden inverso: primero $F_3 \\leftarrow F_3 + ({-c2})F_2$ y luego $F_2 \\leftarrow F_2 + ({-c1})F_1$"

    A_inv = A.inv()

    statement = (
        "Sea la matriz $A$ obtenida a partir de la identidad $I_3$ mediante transformaciones elementales por filas:\n\n"
        f"$$ A = {mat_to_latex(A)} $$\n\n"
        "Calcula la matriz inversa $A^{-1}$ invirtiendo las operaciones elementales (puedes comprobar $A \\cdot A^{-1} = I_3$)."
    )

    steps = [
        f"Observando cómo se obtiene $A$ desde $I_3$, las operaciones elementales aplicadas son: {ops_desc}.",
        f"La inversa $A^{{-1}}$ deshace esas operaciones en orden inverso: {inv_desc}.",
        f"El resultado exacto es: $$ A^{{-1}} = {mat_to_latex(A_inv)} $$",
        f"Comprobación: $A \\cdot A^{{-1}} = {mat_to_latex(A * A_inv)} = I_3$.",
    ]

    return make_exercise_payload(
        generator_id="mat_elemental_inversa",
        topic="matrices",
        title="Inversa a partir de operaciones elementales (3×3)",
        difficulty="media",
        time_limit_seconds=210,
        statement_md=statement,
        input_spec={"kind": "matrix", "rows": 3, "cols": 3, "label": "Matriz inversa A⁻¹"},
        grading_spec={"kind": "matrix", "expected": mat_to_plain_rows(A_inv)},
        correct_display=f"$$ A^{{-1}} = {mat_to_latex(A_inv)} $$",
        steps_md=steps,
        theory_ref="Tema 2 · Matrices elementales e inversas (02 Pizarra 2/3 · 07 CO P3 · 09 2.1–2.9)",
        fingerprint_data={"variant": variant, "c1": c1, "c2": c2},
        protected_canvas={"kind": "matrix", "label": "Matriz A", "rows": mat_to_plain_rows(A)},
    )


def gen_mat_inversa_gauss_3x3(rng: random.Random) -> dict[str, Any]:
    """Calcula la inversa de una matriz unimodular 3x3 por Gauss-Jordan (inversa entera limpia)."""
    A = build_unimodular_matrix(3, rng, steps=3, coeff_choices=[-2, -1, 1, 2])
    A_inv = A.inv()

    statement = (
        "Calcula la matriz inversa $A^{-1}$ mediante el **método de Gauss-Jordan** sobre $(A \\mid I_3)$:\n\n"
        f"$$ A = {mat_to_latex(A)} $$"
    )

    steps = [
        f"Planteamos la matriz ampliada $(A \\mid I_3)$ y aplicamos operaciones elementales por filas hasta transformar el bloque izquierdo en $I_3$.",
        f"El determinante de $A$ es $|A| = {int(A.det())} \\neq 0$, luego $A$ es invertible (y su inversa tiene entradas enteras).",
        f"El bloque derecho resultante es: $$ A^{{-1}} = {mat_to_latex(A_inv)} $$",
    ]

    return make_exercise_payload(
        generator_id="mat_inversa_gauss_3x3",
        topic="matrices",
        title="Inversa de matriz 3×3 por Gauss-Jordan",
        difficulty="alta",
        time_limit_seconds=330,
        statement_md=statement,
        input_spec={"kind": "matrix", "rows": 3, "cols": 3, "label": "Matriz A⁻¹"},
        grading_spec={"kind": "matrix", "expected": mat_to_plain_rows(A_inv)},
        correct_display=f"$$ A^{{-1}} = {mat_to_latex(A_inv)} $$",
        steps_md=steps,
        theory_ref="Tema 2 · Inversa por Gauss-Jordan (02 Pizarra 1/3 · 05 Tema 2 Ej. 2)",
        fingerprint_data={"A": mat_to_plain_rows(A)},
        protected_canvas={"kind": "matrix", "label": "Matriz A (3×3)", "rows": mat_to_plain_rows(A)},
    )


def gen_mat_conmutar_2x2(rng: random.Random) -> dict[str, Any]:
    """Matrices 2x2 que conmutan con una matriz dada A (formato exacto CO 2025/26 P5)."""
    a = rng.choice([-3, -2, -1, 1, 2, 3, 4])
    b = rng.choice([-3, -2, -1, 1, 2, 3])
    sign = rng.choice([-1, 1])  # c_entry = sign * b
    A = sp.Matrix([[a, b], [sign * b, a]])
    # Si B = [[x, y], [z, w]]:
    # AB = [[ax+bz, ay+bw], [sign*b*x + a*z, sign*b*y + a*w]]
    # BA = [[ax + sign*b*y, bx + ay], [az + sign*b*w, bz + aw]]
    # Igualando: b*z = sign*b*y => z = sign*y;  b*w = b*x => w = x.
    y_val = rng.choice([-3, -2, -1, 1, 2, 3])
    x_val = rng.choice([-4, -2, 1, 3, 5])
    expected_z = sign * y_val
    expected_w = x_val

    statement = (
        "Sea la matriz real:\n\n"
        f"$$ A = {mat_to_latex(A)} $$\n\n"
        "Hallar las condiciones para que una matriz $B = \\begin{pmatrix} x & y \\\\ z & w \\end{pmatrix}$ "
        "conmute con $A$ ($A \\cdot B = B \\cdot A$). "
        f"En particular, si fijamos $x = {x_val}$ e $y = {y_val}$, ¿qué valores deben tomar $z$ y $w$ para que $AB = BA$?"
    )

    rel_z = "z = y" if sign == 1 else "z = -y"
    steps = [
        f"Imponemos $AB = BA$ con $B = \\begin{{pmatrix}} x & y \\\\ z & w \\end{{pmatrix}}$:",
        f"$$ {mat_to_latex(A)} \\begin{{pmatrix}} x & y \\\\ z & w \\end{{pmatrix}} = \\begin{{pmatrix}} x & y \\\\ z & w \\end{{pmatrix}} {mat_to_latex(A)} $$",
        f"Igualando entrada a entrada obtenemos: ${b}z = {sign*b}y \\implies {rel_z}$ y ${b}w = {b}x \\implies w = x$.",
        f"Por tanto, todas las matrices que conmutan con $A$ tienen la forma "
        f"$B = \\begin{{pmatrix}} x & y \\\\ {'' if sign == 1 else '-'}y & x \\end{{pmatrix}}$ con $x, y \\in \\mathbb{{R}}$.",
        f"Para $x = {x_val}$ e $y = {y_val}$, resulta $z = {expected_z}$ y $w = {expected_w}$.",
    ]

    return make_exercise_payload(
        generator_id="mat_conmutar_2x2",
        topic="matrices",
        title="Matrices que conmutan con una matriz dada (AB = BA)",
        difficulty="media",
        time_limit_seconds=240,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "z", "label": "Valor de z", "type": "number", "placeholder": "Entero"},
                {"id": "w", "label": "Valor de w", "type": "number", "placeholder": "Entero"},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "z", "label": "z", "type": "number", "expected": str(expected_z)},
                {"id": "w", "label": "w", "type": "number", "expected": str(expected_w)},
            ],
        },
        correct_display=f"$z = {expected_z},\\; w = {expected_w}$ (en general $w = x$ y ${rel_z}$).",
        steps_md=steps,
        theory_ref="Tema 2 · Producto de matrices y conmutatividad (07 CO P5 · 09 2.10–2.12)",
        fingerprint_data={"a": a, "b": b, "sign": sign, "x": x_val, "y": y_val},
        protected_canvas={"kind": "matrix", "label": "Matriz A (2×2)", "rows": mat_to_plain_rows(A)},
    )


def gen_mat_lu_factorizacion(rng: random.Random) -> dict[str, Any]:
    """Factorización LU normalizada (1's en diagonal de L) y resolución Ax=b vía Ly=b, Ux=y."""
    l21 = rng.choice([-3, -2, -1, 1, 2, 3])
    l31 = rng.choice([-2, -1, 1, 2])
    l32 = rng.choice([-2, -1, 1, 2])
    u11 = rng.choice([-2, -1, 1, 2, 3])
    u22 = rng.choice([-2, -1, 1, 2, 3])
    u33 = rng.choice([-2, -1, 1, 2, 3])
    u12 = rng.choice([-2, -1, 0, 1, 2])
    u13 = rng.choice([-2, -1, 1, 2])
    u23 = rng.choice([-2, -1, 1, 2])

    L = sp.Matrix([[1, 0, 0], [l21, 1, 0], [l31, l32, 1]])
    U = sp.Matrix([[u11, u12, u13], [0, u22, u23], [0, 0, u33]])
    A = L * U
    x_sol = sp.Matrix([rng.choice([-2, -1, 1, 2, 3]) for _ in range(3)])
    y_vec = U * x_sol
    b = L * y_vec

    statement = (
        "Dada la matriz $A$ y el vector de términos independientes $b$:\n\n"
        f"$$ A = {mat_to_latex(A)}, \\qquad b = {mat_to_latex(b)} $$\n\n"
        "Obtén la **factorización $A = LU$ normalizada** (con unos en la diagonal de $L$) y resuelve "
        "$Ax = b$ en dos pasos: primero $Ly = b$ (sustitución hacia delante) y después $Ux = y$ (sustitución hacia atrás)."
    )

    steps = [
        f"Reducimos $A$ a triangular superior $U$ sin intercambiar filas mediante: "
        f"$F_2 \\leftarrow F_2 - ({l21})F_1$, $F_3 \\leftarrow F_3 - ({l31})F_1$, y luego $F_3 \\leftarrow F_3 - ({l32})F_2$.",
        f"Los multiplicadores guardados con su signo en la triangular inferior forman $L$: "
        f"$$ L = {mat_to_latex(L)}, \\qquad U = {mat_to_latex(U)} $$",
        f"Paso 1 ($Ly = b$): resolviendo de arriba abajo obtenemos $y = ({int(y_vec[0])}, {int(y_vec[1])}, {int(y_vec[2])})^T$.",
        f"Paso 2 ($Ux = y$): resolviendo de abajo arriba obtenemos $x = ({int(x_sol[0])}, {int(x_sol[1])}, {int(x_sol[2])})^T$.",
    ]

    return make_exercise_payload(
        generator_id="mat_lu_factorizacion",
        topic="matrices",
        title="Factorización LU normalizada y resolución de Ax = b",
        difficulty="alta",
        time_limit_seconds=360,
        statement_md=statement,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "l32", "label": "Entrada l₃₂ de la matriz L (con 1's en diagonal)", "type": "number", "placeholder": "Entero"},
                {"id": "u33", "label": "Entrada u₃₃ (pivote final de U)", "type": "number", "placeholder": "Entero"},
                {"id": "y", "label": "Vector intermedio y = (y₁, y₂, y₃) de Ly = b", "type": "vector", "labels": ["y₁", "y₂", "y₃"]},
                {"id": "x", "label": "Solución final x = (x₁, x₂, x₃) de Ux = y", "type": "vector", "labels": ["x₁", "x₂", "x₃"]},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "l32", "label": "l₃₂", "type": "number", "expected": str(l32)},
                {"id": "u33", "label": "u₃₃", "type": "number", "expected": str(u33)},
                {"id": "y", "label": "Vector y", "type": "vector", "expected": [str(int(v)) for v in y_vec]},
                {"id": "x", "label": "Solución x", "type": "vector", "expected": [str(int(v)) for v in x_sol]},
            ],
        },
        correct_display=f"$l_{{32}}={l32},\\; u_{{33}}={u33},\\; y=({int(y_vec[0])},{int(y_vec[1])},{int(y_vec[2])}),\\; x=({int(x_sol[0])},{int(x_sol[1])},{int(x_sol[2])})$",
        steps_md=steps,
        theory_ref="Tema 2 · Factorización LU (02 Pizarra 3/3 · 05 Tema 2 Ej. 28 · 09 4.25–4.27)",
        fingerprint_data={"L": mat_to_plain_rows(L), "U": mat_to_plain_rows(U), "x": [int(v) for v in x_sol]},
        protected_canvas={
            "kind": "augmented_matrix",
            "label": "Sistema (A | b) para factorización LU",
            "left": mat_to_plain_rows(A),
            "right": [str(int(v)) for v in b],
        },
    )


def gen_mat_determinante_propiedades(rng: random.Random) -> dict[str, Any]:
    """Cálculo de determinante por cofactores y propiedades (sin regla de Sarrus)."""
    mode = rng.choice(["cofactors_4x4", "properties"])
    if mode == "cofactors_4x4":
        # Matriz 4x4 con 2 o 3 ceros estratégicos en una fila/columna para desarrollo limpio
        a, b, c = [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(3)]
        d, e, f = [rng.choice([-2, -1, 1, 2, 3]) for _ in range(3)]
        g, h = [rng.choice([-2, -1, 1, 2]) for _ in range(2)]
        piv = rng.choice([-3, -2, 2, 3])
        M = sp.Matrix([
            [0, piv, 0, 0],
            [a, d, b, 0],
            [c, e, f, g],
            [0, h, 0, rng.choice([-2, -1, 1, 2])],
        ])
        # Permutamos dos filas aleatoriamente para variedad
        r1, r2 = rng.sample(range(4), 2)
        M.row_swap(r1, r2)
        det_val = int(M.det())

        statement = (
            "Calcula el determinante $|A|$ de la siguiente matriz $4\\times 4$ usando **desarrollo por cofactores** "
            "(elige estratégicamente la fila o columna con más ceros; no uses la regla de Sarrus):\n\n"
            f"$$ A = {mat_to_latex(M)} $$"
        )
        steps = [
            f"Localizamos la fila con un único elemento no nulo ({piv}) y desarrollamos por cofactores aplicando el signo $(-1)^{{i+j}}$.",
            "El menor $3\\times 3$ resultante conserva una fila/columna con ceros, facilitando un segundo desarrollo por adjuntos hasta determinantes $2\\times 2$.",
            f"Operando exactamente se obtiene: $$ |A| = {det_val} $$",
        ]
        return make_exercise_payload(
            generator_id="mat_determinante_propiedades",
            topic="matrices",
            title="Determinante 4×4 por desarrollo de cofactores",
            difficulty="media",
            time_limit_seconds=240,
            statement_md=statement,
            input_spec={"kind": "number", "label": "Determinante |A|", "placeholder": "Entero"},
            grading_spec={"kind": "number", "expected": str(det_val)},
            correct_display=f"$|A| = {det_val}$",
            steps_md=steps,
            theory_ref="Tema 2 · Determinantes por cofactores (02 Pizarra Tema 3 · Checklist 2.7)",
            fingerprint_data={"mode": mode, "M": mat_to_plain_rows(M)},
            protected_canvas={"kind": "matrix", "label": "Matriz A (4×4)", "rows": mat_to_plain_rows(M)},
        )

    # Propiedades: det(k * A^T * B^{-1})
    n = rng.choice([2, 3, 4])
    k = rng.choice([-3, -2, 2, 3])
    det_a = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    det_b = rng.choice([-4, -3, -2, 2, 3, 4])
    # Evitar división fea multiplicando det_a o eligiendo racional limpio
    ans = sp.Rational((k**n) * det_a, det_b)

    statement = (
        f"Sean $A$ y $B$ matrices cuadradas de orden ${n} \\times {n}$ tales que $|A| = {det_a}$ y $|B| = {det_b}$. "
        f"Aplicando las propiedades de los determinantes, calcula el valor exacto de:\n\n"
        f"$$ \\left| ({k}) \\cdot A^T \\cdot B^{{-1}} \\right| $$"
    )
    steps = [
        f"Al multiplicar una matriz ${n}\\times {n}$ por el escalar $k = {k}$, cada una de las ${n}$ filas se multiplica por ${k}$, por lo que $|k M| = k^{n} |M| = ({k})^{n} |M| = {k**n} |M|$.",
        f"Por multiplicatividad y propiedades de transpuesta e inversa: $|A^T B^{{-1}}| = |A^T| \\cdot |B^{{-1}}| = |A| \\cdot \\frac{{1}}{{|B|}}$.",
        f"Sustituyendo los valores dados: $$ ({k})^{n} \\cdot ({det_a}) \\cdot \\frac{{1}}{{{det_b}}} = {fmt_num(ans)} $$",
    ]
    return make_exercise_payload(
        generator_id="mat_determinante_propiedades",
        topic="matrices",
        title="Propiedades de los determinantes (escalar, transpuesta, inversa)",
        difficulty="baja",
        time_limit_seconds=180,
        statement_md=statement,
        input_spec={"kind": "number", "label": "Valor exacto (entero o fracción a/b)", "placeholder": "Ej: -16/3"},
        grading_spec={"kind": "number", "expected": fmt_plain_num(ans)},
        correct_display=f"${fmt_num(ans)}$",
        steps_md=steps,
        theory_ref="Tema 2 · Propiedades de los determinantes (02 Pizarra Tema 3)",
        fingerprint_data={"mode": mode, "n": n, "k": k, "da": det_a, "db": det_b},
    )
