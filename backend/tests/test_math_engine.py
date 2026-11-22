"""Pruebas unitarias exhaustivas del Motor Matemático Procedural (SymPy/NumPy)."""
from __future__ import annotations

import random

import sympy as sp

from backend.app.math_engine.registry import GENERATORS
from backend.app.math_engine.utils import grade_answer, parse_rational


def test_parse_rational_variants():
    assert parse_rational("3") == sp.Rational(3)
    assert parse_rational("-5/2") == sp.Rational(-5, 2)
    assert parse_rational("0.5") == sp.Rational(1, 2)
    assert parse_rational("-0,75") == sp.Rational(-3, 4)
    assert parse_rational("1/0") is None
    assert parse_rational("__import__('os').system('id')") is None
    assert parse_rational("abc") is None


def test_all_26_generators_exact_math_and_uniqueness():
    rng = random.Random(2026)
    assert len(GENERATORS) == 26

    for gid, meta in GENERATORS.items():
        fingerprints = set()
        for _ in range(6):
            ex = meta["fn"](rng)
            assert "prompt" in ex and "solution" in ex
            # Verificar que el prompt público NO contiene datos secretos de solución
            prompt_str = str(ex["prompt"])
            assert "grading_spec" not in prompt_str
            assert "correct_display" not in prompt_str
            assert "steps_md" not in prompt_str

            fingerprints.add(ex["fingerprint"])
            spec = ex["solution"]["grading_spec"]
            kind = spec["kind"]
            if kind in {"number", "vector", "matrix", "choice", "multi_tf"}:
                expected = spec["expected"]
            elif kind == "multi_field":
                expected = {}
                for f in spec["fields"]:
                    if f["type"] == "eigenvector":
                        A = sp.Matrix([[sp.Rational(c) for c in row] for row in f["matrix"]])
                        lam = sp.Rational(f["eigenvalue"])
                        ns = (A - lam * sp.eye(A.rows)).nullspace()
                        assert len(ns) >= 1
                        # Probar con un múltiplo escalar no trivial (-2*v)
                        expected[f["id"]] = [str(-2 * c) for c in ns[0]]
                    else:
                        expected[f["id"]] = f["expected"]
            else:
                raise AssertionError(f"Unsupported grading kind {kind}")

            ok, score, _ = grade_answer(expected, ex["solution"], timed_out=False)
            assert ok is True and score == 1.0, f"Fallo autoevaluación en {gid}"

            # Verificar timeout siempre falla con 0.0
            ok_t, score_t, _ = grade_answer(expected, ex["solution"], timed_out=True)
            assert ok_t is False and score_t == 0.0

        assert len(fingerprints) >= 3, f"Poca variabilidad procedural en {gid}: {len(fingerprints)}/6"


def test_eigenvector_rejects_zero_vector():
    sol = {
        "grading_spec": {
            "kind": "eigenvector",
            "matrix": [["2", "0"], ["0", "3"]],
            "eigenvalue": "3",
        }
    }
    ok_zero, _, _ = grade_answer(["0", "0"], sol)
    assert ok_zero is False
    ok_good, score_good, _ = grade_answer(["0", "5"], sol)
    assert ok_good is True and score_good == 1.0
    ok_bad, _, _ = grade_answer(["1", "1"], sol)
    assert ok_bad is False
