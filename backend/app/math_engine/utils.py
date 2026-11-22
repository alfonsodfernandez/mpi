"""Utilidades SymPy: matrices unimodulares, formateo LaTeX limpio y evaluador matemático exacto."""
from __future__ import annotations

import hashlib
import json
import random
import re
from fractions import Fraction
from typing import Any

import sympy as sp


def r(val: int | float | str | Fraction | sp.Rational) -> sp.Rational:
    return sp.Rational(val)


def parse_rational(raw: Any) -> sp.Rational | None:
    """Convierte de forma segura una entrada del alumno (entero, fracción 'a/b' o decimal) en sp.Rational."""
    if raw is None:
        return None
    if isinstance(raw, bool):
        return None
    if isinstance(raw, (int, Fraction)):
        return sp.Rational(raw)
    if isinstance(raw, float):
        if raw != raw:  # NaN
            return None
        return sp.Rational(str(round(raw, 8)))
    s = str(raw).strip().replace(",", ".").replace("−", "-").replace(" ", "")
    if not s:
        return None
    # Permitir solo números, signos, barra de fracción y punto decimal
    if not re.fullmatch(r"[+-]?(\d+(\.\d+)?|\.\d+)(/[+-]?\d+(\.\d+)?)?", s):
        return None
    try:
        if "/" in s:
            num_s, den_s = s.split("/", 1)
            den = Fraction(den_s)
            if den == 0:
                return None
            frac = Fraction(num_s) / den
            return sp.Rational(frac.numerator, frac.denominator)
        frac = Fraction(s)
        return sp.Rational(frac.numerator, frac.denominator)
    except Exception:
        return None


def fmt_num(val: Any) -> str:
    """Formatea un entero o racional de SymPy a LaTeX limpio."""
    expr = sp.nsimplify(val)
    if isinstance(expr, sp.Rational) and expr.q != 1:
        if expr.p < 0:
            return f"-\\frac{{{abs(expr.p)}}}{{{expr.q}}}"
        return f"\\frac{{{expr.p}}}{{{expr.q}}}"
    return sp.latex(expr)


def fmt_plain_num(val: Any) -> str:
    """Formatea número en texto plano para canvas anti-OCR o display simple."""
    expr = sp.nsimplify(val)
    if isinstance(expr, sp.Rational) and expr.q != 1:
        return f"{expr.p}/{expr.q}"
    return str(expr)


def mat_to_latex(M: sp.Matrix, env: str = "pmatrix") -> str:
    rows = []
    for i in range(M.rows):
        row_cells = [fmt_num(M[i, j]) for j in range(M.cols)]
        rows.append(" & ".join(row_cells))
    return f"\\begin{{{env}}}" + " \\\\ ".join(rows) + f"\\end{{{env}}}"


def aug_to_latex(A: sp.Matrix, b: sp.Matrix) -> str:
    col_spec = "c" * A.cols + "|c"
    rows = []
    for i in range(A.rows):
        left = " & ".join(fmt_num(A[i, j]) for j in range(A.cols))
        right = fmt_num(b[i, 0])
        rows.append(f"{left} & {right}")
    return f"\\left(\\begin{{array}}{{{col_spec}}}" + " \\\\ ".join(rows) + "\\end{array}\\right)"


def mat_to_plain_rows(M: sp.Matrix) -> list[list[str]]:
    return [[fmt_plain_num(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def vec_to_latex(v: list[Any] | sp.Matrix) -> str:
    elems = list(v) if isinstance(v, sp.Matrix) else v
    return "(" + ",\\, ".join(fmt_num(x) for x in elems) + ")"


def format_linear_expr(coeffs: list[Any], var_names: list[str]) -> str:
    """Construye una expresión lineal en LaTeX como '2x - y + 3z' sin signos redundantes."""
    terms: list[str] = []
    for c, v in zip(coeffs, var_names):
        c_sym = sp.sympify(c)
        if c_sym == 0:
            continue
        is_first = len(terms) == 0
        if c_sym.is_number:
            c_num = sp.nsimplify(c_sym)
            if c_num == 1:
                terms.append(v if is_first else f"+ {v}")
            elif c_num == -1:
                terms.append(f"-{v}" if is_first else f"- {v}")
            elif c_num > 0:
                s = fmt_num(c_num)
                terms.append(f"{s}{v}" if is_first else f"+ {s}{v}")
            else:
                s = fmt_num(-c_num)
                terms.append(f"-{s}{v}" if is_first else f"- {s}{v}")
        else:
            s = sp.latex(c_sym)
            if "+" in s or "-" in s[1:]:
                s = f"({s})"
            terms.append(f"{s}{v}" if is_first else f"+ {s}{v}")
    return " ".join(terms) if terms else "0"


def system_to_latex(A: sp.Matrix, b: sp.Matrix, var_names: list[str] | None = None) -> str:
    if var_names is None:
        var_names = ["x", "y", "z", "w"][: A.cols] if A.cols <= 4 else [f"x_{i+1}" for i in range(A.cols)]
    lines = []
    for i in range(A.rows):
        lhs = format_linear_expr([A[i, j] for j in range(A.cols)], var_names)
        rhs = fmt_num(b[i, 0])
        lines.append(f"{lhs} = {rhs}")
    return "\\begin{cases} " + " \\\\ ".join(lines) + " \\end{cases}"


def build_unimodular_matrix(n: int, rng: random.Random, steps: int = 4, coeff_choices: list[int] | None = None) -> sp.Matrix:
    """Construye una matriz entera n x n con det = ±1 (inversa siempre entera y limpia)."""
    if coeff_choices is None:
        coeff_choices = [-2, -1, 1, 2]
    M = sp.eye(n)
    # Mezclar filas de inicio opcionalmente
    if rng.random() < 0.45 and n >= 2:
        i, j = rng.sample(range(n), 2)
        M.row_swap(i, j)
    for _ in range(steps):
        i, j = rng.sample(range(n), 2)
        k = rng.choice(coeff_choices)
        M.row_op(i, lambda val, col: val + k * M[j, col])
    # Evitar entradas demasiado grandes
    if any(abs(int(M[r_idx, c_idx])) > 7 for r_idx in range(n) for c_idx in range(n)):
        return build_unimodular_matrix(n, rng, steps=max(2, steps - 1), coeff_choices=[-1, 1])
    if M == sp.eye(n):
        M[0, 1] = rng.choice([-2, -1, 1, 2])
    return M


def compute_fingerprint(generator_id: str, seed_payload: Any) -> str:
    raw = json.dumps({"g": generator_id, "p": seed_payload}, sort_keys=True, default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def make_exercise_payload(
    *,
    generator_id: str,
    topic: str,
    title: str,
    difficulty: str,
    time_limit_seconds: int,
    statement_md: str,
    input_spec: dict[str, Any],
    grading_spec: dict[str, Any],
    correct_display: str,
    steps_md: list[str],
    theory_ref: str,
    fingerprint_data: Any,
    protected_canvas: dict[str, Any] | None = None,
    code_block: str | None = None,
) -> dict[str, Any]:
    """Estructura unificada separando estrictamente 'prompt' (público) de 'solution' (secreto)."""
    prompt = {
        "statement_md": statement_md,
        "input_spec": input_spec,
        "protected_canvas": protected_canvas,
        "code_block": code_block,
    }
    solution = {
        "grading_spec": grading_spec,
        "correct_display": correct_display,
        "steps_md": steps_md,
        "theory_ref": theory_ref,
    }
    return {
        "generator_id": generator_id,
        "topic": topic,
        "title": title,
        "difficulty": difficulty,
        "time_limit_seconds": time_limit_seconds,
        "fingerprint": compute_fingerprint(generator_id, fingerprint_data),
        "prompt": prompt,
        "solution": solution,
    }


def grade_answer(user_answer: Any, solution: dict[str, Any], timed_out: bool = False) -> tuple[bool, float, str]:
    """Evalúa matemáticamente con SymPy la respuesta del alumno contra grading_spec."""
    if timed_out:
        return False, 0.0, "Tiempo agotado. El ejercicio se ha registrado automáticamente como incompleto."

    spec = solution["grading_spec"]
    kind = spec["kind"]

    if user_answer is None:
        return False, 0.0, "No se recibió ninguna respuesta."

    if kind == "number":
        parsed = parse_rational(user_answer)
        expected = parse_rational(spec["expected"])
        if parsed is None:
            return False, 0.0, "Formato numérico no válido. Usa enteros o fracciones como -3/4."
        ok = parsed == expected
        return ok, (1.0 if ok else 0.0), (
            "¡Correcto! Valor exacto verificado simbólicamente." if ok
            else f"Incorrecto. Tu valor ({fmt_plain_num(parsed)}) no coincide con el resultado exacto."
        )

    if kind == "vector":
        expected_list = [parse_rational(x) for x in spec["expected"]]
        if not isinstance(user_answer, list) or len(user_answer) != len(expected_list):
            return False, 0.0, f"Debes introducir exactamente {len(expected_list)} componentes."
        parsed_list = [parse_rational(x) for x in user_answer]
        if any(x is None for x in parsed_list):
            return False, 0.0, "Alguna componente del vector está vacía o no es un número/fracción válido."
        matches = [p == e for p, e in zip(parsed_list, expected_list)]
        ok = all(matches)
        score = round(sum(matches) / len(expected_list), 2)
        if ok:
            return True, 1.0, "¡Correcto! Todas las componentes del vector son exactas."
        return False, score, f"Has acertado {sum(matches)} de {len(expected_list)} componentes. Revisa los pasos."

    if kind == "eigenvector":
        # Comprueba A * v == lambda * v y v != 0 (acepta cualquier múltiplo escalar no nulo!)
        A = sp.Matrix([[parse_rational(c) for c in row] for row in spec["matrix"]])
        lam = parse_rational(spec["eigenvalue"])
        n = A.cols
        if not isinstance(user_answer, list) or len(user_answer) != n:
            return False, 0.0, f"Debes introducir un vector no nulo de {n} componentes."
        parsed_list = [parse_rational(x) for x in user_answer]
        if any(x is None for x in parsed_list):
            return False, 0.0, "Alguna componente no es un número/fracción válido."
        v = sp.Matrix(parsed_list)
        if v.is_zero_matrix:
            return False, 0.0, "El vector nulo (0,...,0) nunca puede ser un autovector."
        ok = (A * v == lam * v)
        return ok, (1.0 if ok else 0.0), (
            "¡Correcto! Se verifica exactamente $A v = \\lambda v$ con $v \\neq 0$." if ok
            else "Incorrecto: el vector introducido no satisface $A v = \\lambda v$."
        )

    if kind == "matrix":
        exp_rows = spec["expected"]
        rows_n, cols_n = len(exp_rows), len(exp_rows[0])
        if not isinstance(user_answer, list) or len(user_answer) != rows_n:
            return False, 0.0, f"Se esperaba una matriz de dimensión {rows_n}×{cols_n}."
        total = rows_n * cols_n
        correct_cells = 0
        for i in range(rows_n):
            row = user_answer[i]
            if not isinstance(row, list) or len(row) != cols_n:
                return False, 0.0, f"La fila {i+1} no tiene {cols_n} columnas."
            for j in range(cols_n):
                p = parse_rational(row[j])
                e = parse_rational(exp_rows[i][j])
                if p is not None and p == e:
                    correct_cells += 1
        ok = correct_cells == total
        score = round(correct_cells / total, 2)
        if ok:
            return True, 1.0, "¡Correcto! Todas las entradas de la matriz coinciden exactamente."
        return False, score, f"Has acertado {correct_cells} de {total} entradas de la matriz."

    if kind == "choice":
        ok = str(user_answer).strip() == str(spec["expected"]).strip()
        return ok, (1.0 if ok else 0.0), (
            "¡Correcto! Opción acertada." if ok else "Incorrecto. Revisa el razonamiento detallado."
        )

    if kind == "multi_tf":
        expected_map: dict[str, bool] = spec["expected"]
        if not isinstance(user_answer, dict):
            return False, 0.0, "Debes responder a cada afirmación (Verdadero/Falso)."
        total = len(expected_map)
        hits = 0
        for key, exp_val in expected_map.items():
            raw_v = user_answer.get(key)
            if isinstance(raw_v, str):
                raw_v = raw_v.lower() in {"true", "v", "verdadero", "si", "sí", "1"}
            if isinstance(raw_v, bool) and raw_v == exp_val:
                hits += 1
        ok = hits == total
        score = round(hits / total, 2)
        if ok:
            return True, 1.0, "¡Perfecto! Has evaluado correctamente todas las afirmaciones."
        return False, score, f"Has acertado {hits} de {total} afirmaciones. Revisa cada justificación."

    if kind == "multi_field":
        fields = spec["fields"]
        if not isinstance(user_answer, dict):
            return False, 0.0, "Debes completar todos los apartados del ejercicio."
        total = len(fields)
        hits = 0
        details: list[str] = []
        for f in fields:
            fid = f["id"]
            ftype = f["type"]
            uval = user_answer.get(fid)
            field_ok = False
            if ftype == "number":
                p = parse_rational(uval)
                e = parse_rational(f["expected"])
                field_ok = (p is not None and p == e)
            elif ftype == "number_set":
                # Acepta lista separada por comas de números (sin importar el orden), ej: "-2, 4"
                exp_set = {parse_rational(x) for x in f["expected"]}
                if isinstance(uval, list):
                    raw_items = uval
                else:
                    raw_items = [x.strip() for x in re.split(r"[,;]+", str(uval or "")) if x.strip()]
                parsed_set = {parse_rational(x) for x in raw_items}
                if None not in parsed_set and len(raw_items) == len(exp_set) and parsed_set == exp_set:
                    field_ok = True
            elif ftype == "choice":
                field_ok = str(uval or "").strip() == str(f["expected"]).strip()
            elif ftype == "vector":
                exp_vec = [parse_rational(x) for x in f["expected"]]
                if isinstance(uval, list) and len(uval) == len(exp_vec):
                    p_vec = [parse_rational(x) for x in uval]
                    field_ok = all(p is not None and p == e for p, e in zip(p_vec, exp_vec))
            elif ftype == "eigenvector":
                A = sp.Matrix([[parse_rational(c) for c in row] for row in f["matrix"]])
                lam = parse_rational(f["eigenvalue"])
                if isinstance(uval, list) and len(uval) == A.cols:
                    p_vec = [parse_rational(x) for x in uval]
                    if all(x is not None for x in p_vec):
                        v = sp.Matrix(p_vec)
                        field_ok = (not v.is_zero_matrix) and (A * v == lam * v)
            if field_ok:
                hits += 1
            else:
                details.append(f["label"])
        ok = hits == total
        score = round(hits / total, 2)
        if ok:
            return True, 1.0, "¡Excelente! Todos los apartados son completamente correctos."
        return False, score, f"Has acertado {hits}/{total} apartados. Revisa: {', '.join(details)}."

    return False, 0.0, "Tipo de evaluación no reconocido."
