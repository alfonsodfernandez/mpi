"""Generadores procedurales para Tema 6: Laboratorio MATLAB y Aplicaciones (AR, DC, IP, LEO, MK, PR, Rúbrica)."""
from __future__ import annotations

import random
from typing import Any

import sympy as sp

from .utils import fmt_num, fmt_plain_num, make_exercise_payload


def gen_matlab_calor_placa(rng: random.Random) -> dict[str, Any]:
    """Distribución de calor en placa 2x2 (formato exacto CO/CEX DC01-DC02 en MATLAB)."""
    # Malla interior [[T1, T2], [T3, T4]] con bordes constantes N, S, E, O
    # Elegimos bordes pares múltiplos de 4 para que T1..T4 sean limpios (enteros o .5)
    t_n = rng.choice([20, 28, 36, 44, 60, 68, 76, 80])
    t_s = rng.choice([12, 20, 28, 32, 40, 48])
    t_o = rng.choice([24, 32, 40, 48, 56, 64])
    t_e = rng.choice([16, 24, 32, 40, 52])
    umbral = (t_n + t_s + t_o + t_e) // 4 + rng.choice([-4, 4])

    # Ecuaciones:
    # 4 T1 - T2 - T3 = N + O
    # -T1 + 4 T2 - T4 = N + E
    # -T1 + 4 T3 - T4 = S + O
    # -T2 - T3 + 4 T4 = S + E
    A = sp.Matrix([
        [4, -1, -1, 0],
        [-1, 4, 0, -1],
        [-1, 0, 4, -1],
        [0, -1, -1, 4],
    ])
    b = sp.Matrix([t_n + t_o, t_n + t_e, t_s + t_o, t_s + t_e])
    T = A.LUsolve(b)
    t_media = sum(T) / 4
    alerta = "si" if t_media > umbral else "no"

    code = (
        "clc, clear, clf\n"
        "A = [ 4 -1 -1  0;\n"
        "     -1  4  0 -1;\n"
        "     -1  0  4 -1;\n"
        "      0 -1 -1  4];\n"
        f"b = [{t_n + t_o}; {t_n + t_e}; {t_s + t_o}; {t_s + t_e}];\n"
        "T = A \\ b;\n"
        "T_media = mean(T);\n"
        f"fprintf('T1 = %.2f C | Media = %.2f C\\n', T(1), T_media)\n"
    )

    statement = (
        "En una práctica de **Distribución de Calor en MATLAB** se modela una placa con malla interior $2\\times 2$ "
        "($T_1$ arriba-izq, $T_2$ arriba-der, $T_3$ abajo-izq, $T_4$ abajo-der) donde cada punto es la media de sus 4 vecinos:\n\n"
        f"- Borde Norte: **${t_n}\\,^\\circ\\text{{C}}$** · Borde Sur: **${t_s}\\,^\\circ\\text{{C}}$** · "
        f"Borde Oeste: **${t_o}\\,^\\circ\\text{{C}}$** · Borde Este: **${t_e}\\,^\\circ\\text{{C}}$**\n\n"
        f"El sistema activa una alarma térmica si la temperatura media interior supera **${umbral}\\,^\\circ\\text{{C}}$**. "
        "Analiza el script MATLAB y calcula `T(1)`, `T_media` y si salta la alarma."
    )

    steps = [
        f"La temperatura media de los 4 nodos interiores por simetría del laplaciano coincide exactamente con la media de los 4 bordes: "
        f"$T_{{\\text{{media}}}} = \\frac{{{t_n} + {t_s} + {t_o} + {t_e}}}{{4}} = {fmt_num(t_media)}\\,^\\circ\\text{{C}}$.",
        f"Resolviendo $A T = b$ con `T = A \\ b` se obtiene: "
        f"$T_1 = {fmt_num(T[0])},\\; T_2 = {fmt_num(T[1])},\\; T_3 = {fmt_num(T[2])},\\; T_4 = {fmt_num(T[3])}$.",
        f"Comparando $T_{{\\text{{media}}}} = {fmt_num(t_media)}$ con el umbral ${umbral}\\,^\\circ\\text{{C}}$: "
        + ("**SÍ salta la alarma**." if alerta == "si" else "**NO salta la alarma**."),
    ]

    return make_exercise_payload(
        generator_id="matlab_calor_placa",
        topic="matlab",
        title="MATLAB · Distribución de calor (A\\b y equilibrio 2×2)",
        difficulty="media",
        time_limit_seconds=270,
        statement_md=statement,
        code_block=code,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "t1", "label": "Temperatura T(1) (entero o fracción/decimal exacto)", "type": "number", "placeholder": "Ej: 52.5"},
                {"id": "t_media", "label": "Temperatura media T_media", "type": "number", "placeholder": "Ej: 45"},
                {
                    "id": "alerta",
                    "label": f"¿Supera el umbral de {umbral} °C?",
                    "type": "choice",
                    "options": [{"value": "si", "label": "Sí, salta la alarma"}, {"value": "no", "label": "No salta la alarma"}],
                },
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "t1", "label": "T(1)", "type": "number", "expected": fmt_plain_num(T[0])},
                {"id": "t_media", "label": "T_media", "type": "number", "expected": fmt_plain_num(t_media)},
                {"id": "alerta", "label": "Alarma térmica", "type": "choice", "expected": alerta},
            ],
        },
        correct_display=f"$T_1 = {fmt_num(T[0])}\\,^\\circ\\text{{C}},\\; T_{{\\text{{media}}}} = {fmt_num(t_media)}\\,^\\circ\\text{{C}}$, Alarma: {alerta.upper()}.",
        steps_md=steps,
        theory_ref="Laboratorio MATLAB · 02 Distribución de Calor (06_Practicas_MATLAB · 07 CO DC01–DC02)",
        fingerprint_data={"borders": [t_n, t_s, t_o, t_e], "u": umbral},
    )


def gen_matlab_leontief_markov(rng: random.Random) -> dict[str, Any]:
    """Modelo abierto de Leontief (I - C)x = d O Cadena de Markov x1 = P*x0 en MATLAB."""
    mode = rng.choice(["leontief", "markov"])
    if mode == "leontief":
        # Construimos I - C con inversa limpia usando C con entradas racionales simples (décimas/quintos)
        # C = [[0.2, 0.2], [0.4, 0.2]] -> I - C = [[0.8, -0.2], [-0.4, 0.8]]
        configs = [
            (sp.Matrix([[sp.Rational(1, 5), sp.Rational(1, 5)], [sp.Rational(2, 5), sp.Rational(1, 5)]]), ["0.2", "0.2", "0.4", "0.2"]),
            (sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)], [sp.Rational(1, 4), sp.Rational(1, 2)]]), ["0.5", "0.25", "0.25", "0.5"]),
            (sp.Matrix([[sp.Rational(1, 4), sp.Rational(1, 4)], [sp.Rational(1, 2), sp.Rational(1, 4)]]), ["0.25", "0.25", "0.5", "0.25"]),
        ]
        C, strs = rng.choice(configs)
        x_prod = sp.Matrix([rng.choice([40, 80, 120, 160]), rng.choice([40, 80, 120, 160])])
        I_minus_C = sp.eye(2) - C
        d = I_minus_C * x_prod

        code = (
            "clc, clear\n"
            f"C = [{strs[0]} {strs[1]}; {strs[2]} {strs[3]}];\n"
            f"d = [{fmt_plain_num(d[0])}; {fmt_plain_num(d[1])}];\n"
            "x = (eye(2) - C) \\ d;\n"
            "fprintf('Sector 1: %.2f | Sector 2: %.2f\\n', x(1), x(2))\n"
        )
        statement = (
            "Interpreta el siguiente script MATLAB del **modelo abierto de insumos-productos de Leontief** "
            "para una economía de 2 sectores, donde $C$ es la matriz de consumo interno y $d$ es la demanda externa. "
            "Calcula el vector de producción total `x = [x(1); x(2)]` que imprimirá MATLAB."
        )
        steps = [
            "En el modelo abierto de Leontief, la producción total $x$ satisface $x = Cx + d \\iff (I - C)x = d$.",
            f"Calculamos $I - C = \\begin{{pmatrix}} {fmt_num(I_minus_C[0,0])} & {fmt_num(I_minus_C[0,1])} \\\\ {fmt_num(I_minus_C[1,0])} & {fmt_num(I_minus_C[1,1])} \\end{{pmatrix}}$.",
            f"Resolviendo `(eye(2) - C) \\ d` obtenemos $x_1 = {int(x_prod[0])}$ y $x_2 = {int(x_prod[1])}$.",
        ]
        return make_exercise_payload(
            generator_id="matlab_leontief_markov",
            topic="matlab",
            title="MATLAB · Modelo de Leontief (eye(n) - C)\\d",
            difficulty="media",
            time_limit_seconds=240,
            statement_md=statement,
            code_block=code,
            input_spec={"kind": "vector", "labels": ["x(1)", "x(2)"]},
            grading_spec={"kind": "vector", "expected": [str(int(x_prod[0])), str(int(x_prod[1]))]},
            correct_display=f"$x(1) = {int(x_prod[0])},\\; x(2) = {int(x_prod[1])}$",
            steps_md=steps,
            theory_ref="Laboratorio MATLAB · 06 Modelo de Leontief (06_Practicas_MATLAB · 07 CO LEO01–02)",
            fingerprint_data={"mode": mode, "strs": strs, "x": [int(x_prod[0]), int(x_prod[1])]},
        )

    # Markov: matriz estocástica por columnas P (como en 06_Practicas_MATLAB sección 07!)
    p11 = rng.choice([sp.Rational(7, 10), sp.Rational(8, 10), sp.Rational(3, 5), sp.Rational(3, 4)])
    p22 = rng.choice([sp.Rational(6, 10), sp.Rational(7, 10), sp.Rational(4, 5), sp.Rational(1, 2)])
    p21 = 1 - p11
    p12 = 1 - p22
    P = sp.Matrix([[p11, p12], [p21, p22]])
    # Estado estacionario: P*v = v => (1 - p11)*v1 = p12*v2 => v1 / v2 = p12 / p21
    denom = p12 + p21
    v_eq = sp.Matrix([p12 / denom, p21 / denom])
    x0 = sp.Matrix([rng.choice([100, 200, 400]), rng.choice([100, 200, 300])])
    x1 = P * x0

    code = (
        "clc, clear\n"
        f"P = [{float(p11):.2f} {float(p12):.2f}; {float(p21):.2f} {float(p22):.2f}];  % columnas suman 1\n"
        f"x0 = [{int(x0[0])}; {int(x0[1])}];\n"
        "x1 = P * x0;\n"
        "[V, D] = eig(P);\n"
        "fprintf('Tras 1 periodo: %.1f y %.1f\\n', x1(1), x1(2))\n"
    )
    statement = (
        "Analiza este script MATLAB de una **Cadena de Markov** de 2 estados (con columnas de $P$ sumando 1, "
        "convención del Cuaderno de Prácticas UFV). Determina:\n"
        "a) El vector `x1 = P * x0` tras 1 periodo.\n"
        "b) La proporción estacionaria del Estado 1 a largo plazo (autovector normalizado para $\\lambda = 1$)."
    )
    steps = [
        f"a) Multiplicamos $P \\cdot x_0$: "
        f"$x_1(1) = {float(p11):.2f}({int(x0[0])}) + {float(p12):.2f}({int(x0[1])}) = {fmt_num(x1[0])}$; "
        f"$x_1(2) = {float(p21):.2f}({int(x0[0])}) + {float(p22):.2f}({int(x0[1])}) = {fmt_num(x1[1])}$.",
        f"b) En el equilibrio $P \\pi = \\pi$ con $\\pi_1 + \\pi_2 = 1$, se cumple $(1 - p_{{11}})\\pi_1 = p_{{12}}\\pi_2$, es decir "
        f"${fmt_num(p21)}\\pi_1 = {fmt_num(p12)}(1 - \\pi_1) \\implies \\pi_1 = \\frac{{{fmt_num(p12)}}}{{{fmt_num(p12)} + {fmt_num(p21)}}} = {fmt_num(v_eq[0])}$.",
    ]

    return make_exercise_payload(
        generator_id="matlab_leontief_markov",
        topic="matlab",
        title="MATLAB · Cadenas de Markov (P*x0 y vector estacionario)",
        difficulty="media",
        time_limit_seconds=270,
        statement_md=statement,
        code_block=code,
        input_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "x1", "label": "a) Vector x1 = (x1(1), x1(2)) tras 1 periodo", "type": "vector", "labels": ["x1(1)", "x1(2)"]},
                {"id": "pi1", "label": "b) Proporción estacionaria π₁ del Estado 1 (fracción o decimal)", "type": "number", "placeholder": "Ej: 2/5"},
            ],
        },
        grading_spec={
            "kind": "multi_field",
            "fields": [
                {"id": "x1", "label": "Vector x1", "type": "vector", "expected": [fmt_plain_num(x1[0]), fmt_plain_num(x1[1])]},
                {"id": "pi1", "label": "Equilibrio π₁", "type": "number", "expected": fmt_plain_num(v_eq[0])},
            ],
        },
        correct_display=f"$x_1 = ({fmt_num(x1[0])},\\, {fmt_num(x1[1])})^T$, $\\pi_1 = {fmt_num(v_eq[0])}$.",
        steps_md=steps,
        theory_ref="Laboratorio MATLAB · 07 Cadenas de Markov (06_Practicas_MATLAB · Proyecto Red Logística Reto 4)",
        fingerprint_data={"mode": mode, "p11": str(p11), "p22": str(p22), "x0": [int(x0[0]), int(x0[1])]},
    )


def gen_matlab_polinomio_eval(rng: random.Random) -> dict[str, Any]:
    """Interpretación de polyval, orden de coeficientes y rref/norm en MATLAB (Chuleta 06)."""
    a2 = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    a1 = rng.choice([-5, -3, -2, 0, 2, 3, 5])
    a0 = rng.choice([-6, -4, -2, 1, 3, 5, 7])
    x0 = rng.choice([-3, -2, -1, 2, 3])
    val = a2 * (x0**2) + a1 * x0 + a0
    # Trampa clásica: coeficientes ordenados de mayor a menor grado en MATLAB!
    wrong_order_val = a0 * (x0**2) + a1 * x0 + a2

    code = (
        "clc, clear\n"
        f"p = [{a2} {a1} {a0}];\n"
        f"y = polyval(p, {x0});\n"
        "fprintf('Resultado = %d\\n', y)\n"
    )
    statement = (
        "En MATLAB, los polinomios se representan como vectores fila de coeficientes. "
        "¿Qué valor numérico imprimirá el siguiente script al evaluar `polyval`?"
    )
    steps = [
        f"En MATLAB, el vector `p = [{a2} {a1} {a0}]` almacena los coeficientes de **mayor a menor grado**: "
        f"$p(x) = ({a2})x^2 + ({a1})x + ({a0})$.",
        f"Evaluando en $x = {x0}$: $p({x0}) = ({a2})({x0})^2 + ({a1})({x0}) + ({a0}) = {val}$.",
        f"(Error típico a evitar: leer los coeficientes de menor a mayor grado habría dado {wrong_order_val}.)",
    ]

    return make_exercise_payload(
        generator_id="matlab_polinomio_eval",
        topic="matlab",
        title="MATLAB · Interpretación de polyval y representación de polinomios",
        difficulty="baja",
        time_limit_seconds=150,
        statement_md=statement,
        code_block=code,
        input_spec={"kind": "number", "label": "Salida impresa por fprintf", "placeholder": "Entero"},
        grading_spec={"kind": "number", "expected": str(val)},
        correct_display=f"`Resultado = {val}`",
        steps_md=steps,
        theory_ref="Laboratorio MATLAB · Chuleta Sección 3: Polinomios (polyval, roots, polyfit)",
        fingerprint_data={"p": [a2, a1, a0], "x0": x0},
    )


def gen_matlab_rubrica_y_funciones(rng: random.Random) -> dict[str, Any]:
    """Preguntas proceduralizadas sobre funciones clave de MATLAB y la rúbrica oficial UFV 2026."""
    bank = [
        {
            "key": "backslash_sci",
            "title": "MATLAB · Comportamiento de A\\b en sistemas indeterminados",
            "code": "A = [1 1 0 0; 1 0 0 1; 0 0 1 1; 0 1 1 0];\nb = [431; 255; 340; 516];\nx = A \\ b;",
            "q": "El sistema anterior es **compatible indeterminado (SCI)**. Según la chuleta oficial de MPI-I, ¿qué ocurre si usas `A \\ b` en lugar de `rref([A b])`?",
            "opts": [
                ("lsq", "MATLAB devuelve una solución particular (mínimos cuadrados/básica) pero NO muestra la familia paramétrica de infinitas soluciones; debe usarse `rref([A b])`."),
                ("err", "MATLAB lanza un error fatal y detiene la ejecución sin devolver ningún vector."),
                ("all", "MATLAB imprime automáticamente todas las soluciones en función de un parámetro simbólico `t`."),
                ("null", "MATLAB devuelve directamente la base ortonormal del núcleo de `A`."),
            ],
            "ans": "lsq",
            "steps": [
                "En `Funciones_Algebra_Matlab.pdf` (Sección 1.2) se advierte expresamente: si resuelves un sistema indeterminado con `\\`, MATLAB entrega una única solución (mínimos cuadrados/básica).",
                "Para sistemas compatibles indeterminados (como flujo de redes) debe utilizarse `rref([A b])` para obtener la forma escalonada reducida y parametrizar las variables libres.",
            ],
        },
        {
            "key": "rubrica_vars",
            "title": "MATLAB · Rúbrica oficial UFV (Formato_practicas_Matlab_2026)",
            "code": "% Problema 1\nsum = 15\nplot = sum * 2\ndisp(['Total: ', num2str(plot)])",
            "q": "Este fragmento viola **varias reglas** de la rúbrica oficial `Formato_practicas_Matlab_2026.pdf`. ¿Cuál de los siguientes diagnósticos identifica correctamente **todos** los defectos críticos?",
            "opts": [
                ("all_defects", "Sobrescribe nombres de funciones reservadas (`sum`, `plot`), omite `;` mostrando cálculos intermedios, usa `disp` en vez de `fprintf` con formato/unidades y falta `clc, clear, clf`."),
                ("only_semi", "El único error es omitir el punto y coma `;`; el uso de `sum` y `disp` es totalmente recomendable."),
                ("only_comment", "Solo falla por llevar comentarios con `%`; el resto cumple la rúbrica al 100%."),
                ("only_clf", "El único error es no escribir `syms` al inicio del script."),
            ],
            "ans": "all_defects",
            "steps": [
                "Regla 2: Finalizar las líneas intermedias con `;` para no imprimir cálculos intermedios.",
                "Regla 3: Dar resultados con `fprintf()` con formato adecuado (`%n.mf`), unidades y `\\n` (no `disp()`).",
                "Regla 4: Iniciar cada problema con `clc, clear, clf`.",
                "Regla 7: Nunca nombrar variables como funciones de MATLAB (`sum`, `plot`) porque oculta la función original.",
            ],
        },
        {
            "key": "residuo_norm",
            "title": "MATLAB · Verificación de soluciones mediante norma del residuo",
            "code": "x = A \\ b;\nr = A * x - b;\ncheck = norm(r);",
            "q": "Tras ejecutar el bloque anterior en MATLAB, `check` toma el valor `1.4211e-14`. ¿Cómo debe interpretarse este resultado?",
            "opts": [
                ("ok", "La solución `x` es numéricamente correcta: la norma del residuo es prácticamente cero (error de redondeo en doble precisión, muy por debajo de 10⁻¹²)."),
                ("bad", "El sistema es incompatible porque el residuo no es exactamente `0`."),
                ("sci", "El sistema tiene infinitas soluciones porque `norm(r) < 1`."),
                ("det", "Significa que el determinante de `A` vale `1.4211e-14`."),
            ],
            "ans": "ok",
            "steps": [
                "El residuo $r = Ax - b$ mide cuánto se desvía la solución numérica de la ecuación exacta.",
                "En aritmética de coma flotante IEEE 754 (doble precisión), valores del orden de $10^{-14}$ indican convergencia/precisión de máquina (exacta a efectos prácticos; en el Proyecto Red Logística se exige error $< 10^{-12}$).",
            ],
        },
        {
            "key": "pagerank_digraph",
            "title": "MATLAB · Grafos dirigidos y centralidad en Proyecto Red Logística",
            "code": "G = digraph(Origen, Destino, Flujos);\nA = full(adjacency(G, 'weighted'));\npr = centrality(G, 'pagerank', 'Importance', G.Edges.Weight);",
            "q": "¿Qué representa exactamente cada línea de este bloque de código basado en el **Proyecto 01 (Red Logística LOGISPAÑA)**?",
            "opts": [
                ("correct", "Construye un grafo dirigido ponderado con las rutas y toneladas, extrae su matriz de adyacencia densa con los pesos, y calcula la importancia estructural ponderada PageRank de cada centro."),
                ("undir", "Construye un grafo no dirigido ignorando el sentido de las rutas y calcula únicamente el camino más corto entre Madrid y Valencia."),
                ("poly", "Ajusta un polinomio de grado 3 a la demanda histórica de mercancías de 2016 a 2025."),
                ("lu", "Calcula la descomposición LU de la matriz de adyacencia y elimina el nodo de Valencia."),
            ],
            "ans": "correct",
            "steps": [
                "`digraph` modela rutas dirigidas (una conexión A→B distinta de B→A) con pesos de flujo semanal.",
                "`full(adjacency(G, 'weighted'))` convierte la matriz dispersa de adyacencia ponderada a formato matriz completa.",
                "`centrality(G, 'pagerank', 'Importance', G.Edges.Weight)` evalúa la importancia relativa en equilibrio ponderando los flujos (Retos 2, 3, 5 y 6 del Proyecto).",
            ],
        },
        {
            "key": "cayley_polyvalm",
            "title": "MATLAB · Teorema de Cayley-Hamilton con poly y polyvalm",
            "code": "p = poly(A);\nC_H = polyvalm(p, A);\nerr = norm(C_H);",
            "q": "¿Cuál es la diferencia fundamental entre `polyval(p, A)` y `polyvalm(p, A)` en MATLAB?",
            "opts": [
                ("mat_vs_elem", "`polyvalm(p, A)` evalúa el polinomio en sentido matricial ($A^n, A^{n-1}, \\dots, c_0 I$) verificando Cayley-Hamilton ($p(A)=0$), mientras que `polyval(p, A)` evalúa elemento a elemento."),
                ("same", "Son alias idénticos; ambos devuelven exactamente la misma matriz nula."),
                ("roots", "`polyvalm` calcula únicamente las raíces complejas del polinomio característico."),
                ("sparse", "`polyvalm` solo funciona con matrices dispersas (`sparse`)."),
            ],
            "ans": "mat_vs_elem",
            "steps": [
                "Según la Chuleta Oficial (Sección 4), `poly(A)` devuelve los coeficientes del polinomio característico de $A$.",
                "`polyvalm(p, A)` aplica potencias matriciales $A^k$ (y $c_0 I$ para el término independiente), por lo que por el Teorema de Cayley-Hamilton `norm(polyvalm(p, A))` es $\\approx 0$.",
            ],
        },
        {
            "key": "null_function",
            "title": "MATLAB · Interpretación de null(A)",
            "code": "A = [1 2 3; 2 4 6; 3 6 9];\nN = null(A);",
            "q": "Si ejecutamos `N = null(A)` sobre esa matriz $3\\times 3$ de rango 1, ¿qué dimensiones y propiedades tienen las columnas de `N`?",
            "opts": [
                ("two_norm", "`N` es de tamaño $3\\times 2$ y sus 2 columnas forman una base ortonormal (norma 1) del espacio nulo $\\operatorname{Ker}(A)$."),
                ("one_col", "`N` es de tamaño $3\\times 1$ porque el rango de `A` es 1."),
                ("rref", "`N` es la forma escalonada reducida $3\\times 3$ de la matriz `A`."),
                ("empty", "`N` está vacía porque todas las filas son proporcionales."),
            ],
            "ans": "two_norm",
            "steps": [
                "Como $\\operatorname{rg}(A) = 1$ y $n = 3$ columnas, por el teorema del rango $\\nu(A) = \\dim(\\operatorname{Ker} A) = 3 - 1 = 2$.",
                "En MATLAB, `null(A)` devuelve una matriz cuyas columnas son una base ortonormal (norma 1) de $\\operatorname{Ker}(A)$, luego `size(N)` es `3×2`.",
            ],
        },
    ]

    item = rng.choice(bank)
    opts = list(item["opts"])
    rng.shuffle(opts)

    return make_exercise_payload(
        generator_id="matlab_rubrica_y_funciones",
        topic="matlab",
        title=item["title"],
        difficulty="baja",
        time_limit_seconds=150,
        statement_md=item["q"],
        code_block=item["code"],
        input_spec={
            "kind": "choice",
            "options": [{"value": v, "label": lbl} for v, lbl in opts],
        },
        grading_spec={"kind": "choice", "expected": item["ans"]},
        correct_display=next(lbl for v, lbl in item["opts"] if v == item["ans"]),
        steps_md=item["steps"],
        theory_ref="Laboratorio MATLAB · Chuleta de Funciones y Rúbrica 2026 (01 + 06_Practicas_MATLAB)",
        fingerprint_data={"key": item["key"], "salt": rng.randint(1, 999999)},
    )
