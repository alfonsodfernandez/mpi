"""Indexador estructurado de los archivos Markdown de _contexto_mpi/ (00 a 10; excluye PII de 11)."""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from ..config import CONTEXT_DIR
from .logistics_analysis import analyze_network


def _read_md(filename: str) -> str:
    path = CONTEXT_DIR / filename
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _extract_h2_sections(md_text: str, max_chars_per_section: int = 12000) -> list[dict[str, Any]]:
    """Extrae bloques '## ...' con su fuente y contenido limpio."""
    parts = re.split(r"(?m)^## ", md_text)
    sections = []
    for raw in parts[1:]:
        lines = raw.splitlines()
        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        source = ""
        m = re.match(r"\*Fuente:\s*`([^`]+)`\*", body)
        if m:
            source = m.group(1)
            body = body[m.end() :].strip()
        if len(body) > max_chars_per_section:
            body = body[:max_chars_per_section].rstrip() + "\n\n*(Extracto completo indexado desde el repositorio del curso.)*"
        sections.append({"title": title, "source": source, "content_md": body})
    return sections


def _parse_checklist_from_01(md01: str) -> list[dict[str, Any]]:
    """Extrae el checklist oficial 'Qué hay que saber de Álgebra' de 01_Asignatura_guia_y_normas.md."""
    topics = [
        {
            "topic_key": "sistemas",
            "title": "Tema 1 · Sistemas Lineales (SL)",
            "items": [
                ("t1_1", "Qué es un SL, matriz de coeficientes y ampliada y su clasificación en función de las soluciones (SCD, SCI, SI)."),
                ("t1_2", "Qué son operaciones elementales por filas y para qué se emplean."),
                ("t1_3", "Qué es una matriz escalonada y escalonada reducida equivalente (mee) y cómo calcularla con Gauss y Gauss-Jordan."),
                ("t1_4", "Discutir un SL con parámetros mediante la matriz escalonada equivalente (sin emplear Rouché ni determinantes)."),
                ("t1_5", "Qué es un SL homogéneo, particularidades de su solución y resolución mediante la mee."),
            ],
        },
        {
            "topic_key": "matrices",
            "title": "Tema 2 · Álgebra de Matrices y Determinantes",
            "items": [
                ("t2_1", "Qué es una matriz y sus operaciones básicas (suma, resta, multiplicación, escalar, potencias y propiedades)."),
                ("t2_2", "Tres formas de interpretar el producto de matrices (clave para espacios vectoriales)."),
                ("t2_3", "Qué es la traspuesta de una matriz y sus propiedades ((AB)ᵀ = BᵀAᵀ, matriz simétrica)."),
                ("t2_4", "Qué es la inversa de una matriz y cómo se calcula mediante el método de Gauss-Jordan."),
                ("t2_5", "Qué es una matriz elemental, cómo se calculan sus inversas y sus propiedades."),
                ("t2_6", "Qué es la factorización LU (y PA = LU), cómo se calcula y cómo se emplea para resolver sistemas."),
                ("t2_7", "Qué es un determinante, cómo calcularlo por cofactores/triangulación (sin Sarrus) y sus propiedades."),
            ],
        },
        {
            "topic_key": "espacios_vectoriales",
            "title": "Tema 3 · Espacios Vectoriales (EV)",
            "items": [
                ("t3_1", "Saber qué es un EV (10 axiomas de definición) y ejemplos (ℝⁿ, Pₙ, Mₘₙ)."),
                ("t3_2", "Saber qué es un subespacio vectorial (2 axiomas de cerradura + 0 ∈ H), ecuaciones, base y dimensión."),
                ("t3_3", "Qué tiene que pasar para que un vector sea combinación lineal de otros vectores."),
                ("t3_4", "Qué es un sistema generador y cómo hallar ecuaciones implícitas, base y dimensión del espacio generado."),
                ("t3_5", "Cómo determinar si un conjunto de vectores es linealmente independiente o dependiente."),
                ("t3_6", "Saber qué es una base de un EV/SEV, calcular coordenadas y matriz de cambio de base."),
                ("t3_7", "Espacio de filas, espacio de columnas, núcleo de una matriz, rango y Teorema del Rango (rg(A) + ν(A) = n)."),
                ("t3_8", "Relacionar matrices y sus filas/columnas con la compatibilidad de sistemas lineales Ax = b."),
            ],
        },
        {
            "topic_key": "aplicaciones_lineales",
            "title": "Tema 4 · Transformaciones Lineales (TL)",
            "items": [
                ("t4_1", "Saber comprobar si una aplicación es lineal (2 axiomas; comprobar primero T(0) = 0)."),
                ("t4_2", "Calcular base, ecuaciones y dimensión del núcleo Ker(T) y la imagen Im(T)."),
                ("t4_3", "Decidir si una TL es inyectiva, sobreyectiva, isomorfismo o ninguna de las dos."),
                ("t4_4", "Hallar la matriz asociada a una TL en bases dadas de V y W."),
                ("t4_5", "Calcular la nueva matriz de una TL al cambiar las bases en V y/o W (A' = Q⁻¹AP)."),
                ("t4_6", "Saber qué son matrices semejantes, equivalentes y congruentes en TL."),
            ],
        },
        {
            "topic_key": "diagonalizacion",
            "title": "Tema 5 · Autovalores y Diagonalización",
            "items": [
                ("t5_1", "Qué es un valor propio (VP), vector propio y su subespacio propio (SEP)."),
                ("t5_2", "Qué es el polinomio característico p_A(λ) = det(A − λI), multiplicidad algebraica y geométrica."),
                ("t5_3", "Qué tienen en común las matrices semejantes (polinomio característico, autovalores, traza, det, rango)."),
                ("t5_4", "Criterio de diagonalización (m_g(λ) = m_a(λ) y raíces reales) y construcción A = PDP⁻¹."),
            ],
        },
    ]
    return [
        {
            "topic_key": t["topic_key"],
            "title": t["title"],
            "items": [{"id": iid, "text": txt} for iid, txt in t["items"]],
        }
        for t in topics
    ]


def _build_theory_modules() -> list[dict[str, Any]]:
    """Construye los 4 bloques de Teoría Interactiva estructurando 00, 01, 02, 03, 04 y 05."""
    md02 = _read_md("02_Teoria_Sistemas_Matrices_Determinantes.md")
    md03 = _read_md("03_Teoria_Espacios_Vectoriales.md")
    md04 = _read_md("04_Teoria_Aplicaciones_Lineales.md")
    md05 = _read_md("05_Ejercicios_de_repaso_resueltos.md")

    sec02 = _extract_h2_sections(md02, max_chars_per_section=9500)
    sec03 = _extract_h2_sections(md03, max_chars_per_section=9500)
    sec04 = _extract_h2_sections(md04, max_chars_per_section=9500)
    sec05 = _extract_h2_sections(md05, max_chars_per_section=9500)

    return [
        {
            "id": "sistemas_matrices",
            "order": 1,
            "topic_filter": "sistemas",
            "secondary_topic": "matrices",
            "title": "Bloque 1 · Sistemas Lineales, Matrices y Determinantes",
            "subtitle": "Gauss, Gauss-Jordan, discusión con parámetros, matrices elementales, inversas, factorización LU y determinantes.",
            "source_files": ["02_Teoria_Sistemas_Matrices_Determinantes.md", "05_Ejercicios_de_repaso_resueltos.md"],
            "definitions": [
                {
                    "term": "Clasificación de un Sistema Lineal (SL)",
                    "body_md": "Dado $A\\mathbf{x} = \\mathbf{b}$ con matriz ampliada $(A\\mid \\mathbf{b})$: es **Compatible Determinado (SCD)** si tiene solución única; **Compatible Indeterminado (SCI)** si tiene infinitas soluciones (aparecen variables libres); e **Incompatible (SI)** si aparece una fila contradictoria $(0\\;\\dots\\;0 \\mid c)$ con $c\\neq 0$.",
                },
                {
                    "term": "Forma Escalonada y Escalonada Reducida (convención UFV)",
                    "body_md": "En la convención de MPI-I: (1) las filas nulas van al final; (2) el primer elemento no nulo de cada fila no nula (pivote) vale **1**; (3) cada pivote está estrictamente a la derecha del pivote superior. Es **escalonada reducida** si además cada pivote es el único elemento no nulo de su columna.",
                },
                {
                    "term": "Matriz Elemental e Inversa",
                    "body_md": "Una matriz $E$ es **elemental** si se obtiene de $I_n$ mediante una única operación elemental por filas. Multiplicar $E\\cdot A$ por la izquierda aplica esa operación a las filas de $A$. Su inversa deshace la operación: $(c F_i)^{-1} = \\frac{1}{c}F_i$, $(F_i + c F_j)^{-1} = F_i - c F_j$, $P_{ij}^{-1} = P_{ij}$.",
                },
                {
                    "term": "Factorización LU Normalizada",
                    "body_md": "$A = L\\cdot U$ donde $L$ es triangular inferior con **1's en la diagonal** (guardando los multiplicadores de Gauss con su signo) y $U$ es triangular superior. Permite resolver $Ax = b$ rápidamente mediante $Ly = b$ (hacia delante) y $Ux = y$ (hacia atrás).",
                },
            ],
            "theorems": [
                {
                    "name": "Teorema de Equivalencias de Matrices Invertibles",
                    "body_md": "Para $A \\in \\mathcal{M}_{n\\times n}(\\mathbb{R})$ son equivalentes: (1) $A$ es invertible; (2) $\\operatorname{rg}(A) = n$; (3) la forma escalonada reducida de $A$ es $I_n$; (4) $Ax = b$ tiene solución única para todo $b$; (5) $Ax = 0$ solo tiene la solución trivial; (6) $|A| \\neq 0$; (7) $A$ es producto de matrices elementales.",
                },
                {
                    "name": "Relación entre Sistemas Homogéneos y No Homogéneos",
                    "body_md": "Un sistema homogéneo $Ax = 0$ siempre es compatible (nunca SI) y si tiene más incógnitas que ecuaciones linealmente independientes es necesariamente SCI. Toda solución de $Ax = b$ se escribe como $\\mathbf{x} = \\mathbf{x}_p + \\mathbf{x}_h$ (una solución particular + la solución general homogénea).",
                },
                {
                    "name": "Propiedades Clave de los Determinantes",
                    "body_md": "$|AB| = |A||B|$; $|A^T| = |A|$; $|kA| = k^n |A|$ (si $A$ es $n\\times n$); $|A^{-1}| = 1/|A|$; si $A=LU$ normalizada entonces $|A|=|U|=\\prod u_{ii}$; sumar a una fila un múltiplo de otra no cambia el determinante; intercambiar dos filas cambia el signo.",
                },
            ],
            "worked_examples": [
                {
                    "title": "Discusión de sistema con parámetro sin Rouché (05 Ej. 5 / 08 CEX P1)",
                    "problem_md": "Discutir $\\begin{cases} x + 2y - 3z = 4 \\\\ 3x - y + 5z = 2 \\\\ 4x + y + (a^2 - 14)z = a + 2 \\end{cases}$ mediante Gauss.",
                    "steps_md": [
                        "Aplicando $F_2 \\leftarrow F_2 - 3F_1$ y $F_3 \\leftarrow F_3 - 4F_1$ llegamos a $\\left(\\begin{smallmatrix}1&2&-3&4\\\\0&-7&14&-10\\\\0&-7&a^2-2&a-14\\end{smallmatrix}\\right)$.",
                        "Haciendo $F_3 \\leftarrow F_3 - F_2$ obtenemos la tercera fila $(0\\; 0\\; a^2 - 16 \\mid a - 4)$.",
                        "Si $a^2 - 16 \\neq 0$ ($a \\neq \\pm 4$): 3 pivotes ⇒ **SCD**.",
                        "Si $a = 4$: fila nula $(0\\; 0\\; 0 \\mid 0)$ ⇒ **SCI** (infinitas soluciones).",
                        "Si $a = -4$: fila $(0\\; 0\\; 0 \\mid -8)$ ⇒ **Incompatible (SI)**.",
                    ],
                },
                {
                    "title": "Inversa por operaciones elementales (07 CO Modelo A P3)",
                    "problem_md": "Dada $A = \\begin{pmatrix}1&0&0\\\\-2&1&0\\\\1&0&1\\end{pmatrix}$, hallar $A^{-1}$ sin Gauss completo.",
                    "steps_md": [
                        "$A$ resulta de aplicar a $I_3$ las operaciones $F_2 \\leftarrow F_2 - 2F_1$ y $F_3 \\leftarrow F_3 + F_1$.",
                        "Como ambas dependen solo de $F_1$, deshacerlas equivale a $F_3 \\leftarrow F_3 - F_1$ y $F_2 \\leftarrow F_2 + 2F_1$.",
                        "Por tanto $A^{-1} = \\begin{pmatrix}1&0&0\\\\2&1&0\\\\-1&0&1\\end{pmatrix}$.",
                    ],
                },
            ],
            "raw_sections": [
                s for s in sec02 if "Pizarra" in s["title"]
            ] + [s for s in sec05 if "Tema 1" in s["title"] or "Tema 2" in s["title"]],
        },
        {
            "id": "espacios_vectoriales",
            "order": 2,
            "topic_filter": "espacios_vectoriales",
            "secondary_topic": None,
            "title": "Bloque 2 · Espacios Vectoriales",
            "subtitle": "Axiomas de EV y SEV, combinación e independencia lineal, bases, dimensión, cambio de base, núcleo y espacios fila/columna.",
            "source_files": ["03_Teoria_Espacios_Vectoriales.md", "05_Ejercicios_de_repaso_resueltos.md"],
            "definitions": [
                {
                    "term": "Subespacio Vectorial (SEV) — Criterio de los 2 Axiomas",
                    "body_md": "Un subconjunto no vacío $H \\subseteq V$ es subespacio vectorial sii: (1) $u, v \\in H \\Rightarrow u + v \\in H$ y (2) $u \\in H, \\alpha \\in \\mathbb{R} \\Rightarrow \\alpha u \\in H$. **Atención:** contener al vector nulo ($0 \\in H$) es condición **necesaria**, pero **no suficiente** (ej. $xy=0$ contiene al $0$ pero no es SEV).",
                },
                {
                    "term": "Independencia Lineal y Base",
                    "body_md": "$\\{v_1, \\dots, v_k\\}$ es **linealmente independiente (LI)** sii $c_1v_1 + \\dots + c_kv_k = 0 \\Rightarrow c_1=\\dots=c_k=0$. Es una **base** de $V$ si es LI y sistema generador. En $\\mathbb{R}^n$, cualquier conjunto de $n$ vectores LI es automáticamente una base.",
                },
                {
                    "term": "Matriz de Cambio de Base",
                    "body_md": "Si $B_1$ y $B_2$ son matrices cuyas columnas son las coordenadas de dos bases en la base canónica, entonces $B_1 (v)_{B_1} = (v)_{B_c} = B_2 (v)_{B_2}$. La matriz que pasa coordenadas de $B_1$ a $B_2$ es $C_{B_1}^{B_2} = B_2^{-1} B_1$.",
                },
                {
                    "term": "Núcleo, Espacio Fila y Espacio Columna",
                    "body_md": "Para $A \\in \\mathcal{M}_{m\\times n}$: $N(A) = \\{x \\in \\mathbb{R}^n : Ax = 0\\}$ (SEV de $\\mathbb{R}^n$); $C(A) = \\operatorname{gen}(\\text{columnas de }A) = \\operatorname{Im}(A)$ (SEV de $\\mathbb{R}^m$); $F(A) = \\operatorname{gen}(\\text{filas de }A)$ (SEV de $\\mathbb{R}^n$).",
                },
            ],
            "theorems": [
                {
                    "name": "Teorema del Rango y la Nulidad",
                    "body_md": "Para toda matriz $A$ de tamaño $m\\times n$: $$\\operatorname{rg}(A) + \\nu(A) = n$$ donde $\\operatorname{rg}(A) = \\dim F(A) = \\dim C(A)$ (número de pivotes) y $\\nu(A) = \\dim N(A)$ (número de variables libres).",
                },
                {
                    "name": "Dimensión de un SEV por Ecuaciones Cartesianas",
                    "body_md": "Si un subespacio $W \\subseteq \\mathbb{R}^n$ viene dado por un sistema lineal homogéneo con $r$ ecuaciones linealmente independientes, entonces $\\dim(W) = n - r$ (coincide con el número de parámetros en sus ecuaciones paramétricas).",
                },
                {
                    "name": "Compatibilidad y Espacio Columna",
                    "body_md": "El sistema lineal $Ax = b$ es compatible **si y solo si** $b \\in C(A)$ (es decir, $b$ es combinación lineal de las columnas de $A$, o equivalentemente $\\operatorname{rg}(A) = \\operatorname{rg}(A\\mid b)$).",
                },
            ],
            "worked_examples": [
                {
                    "title": "Cambio de base y coordenadas en ℝ³ (03 Pizarra Cambio de Base)",
                    "problem_md": "Sean $B_c$ la canónica y $B = \\{(1,1,0),(0,2,1),(1,0,2)\\}$. Calcular $(v)_{B_c}$ si $(v)_B = (3,-1,2)$.",
                    "steps_md": [
                        "Colocamos los vectores de $B$ por columnas: $C_B^{B_c} = B = \\begin{pmatrix}1&0&1\\\\1&2&0\\\\0&1&2\\end{pmatrix}$.",
                        "Multiplicamos $(v)_{B_c} = B\\,(v)_B = 3(1,1,0) - 1(0,2,1) + 2(1,0,2) = (5, 1, 3)$.",
                        "Para el paso inverso de $B_c$ a $B$ usamos $C_{B_c}^B = B^{-1} = \\frac{1}{5}\\begin{pmatrix}4&1&-2\\\\-2&2&1\\\\1&-1&2\\end{pmatrix}$.",
                    ],
                },
                {
                    "title": "Base y dimensión de un espacio nulo (03 Pizarra Rango/Nulidad)",
                    "problem_md": "Hallar $\\nu(A)$ y una base de $N(A)$ para $A = \\begin{pmatrix}1&2&-1\\\\2&-1&3\\end{pmatrix}$.",
                    "steps_md": [
                        "Resolvemos $Ax = 0$: $F_2 \\leftarrow F_2 - 2F_1$ da $-5y + 5z = 0 \\Rightarrow y = z$.",
                        "Sustituyendo en la 1ª ecuación: $x + 2z - z = 0 \\Rightarrow x = -z$.",
                        "Con $z = \\alpha$: $N(A) = \\{(-\\alpha, \\alpha, \\alpha)\\} = \\operatorname{gen}\\{(-1,1,1)\\}$, luego $\\nu(A) = 1$ y $\\operatorname{rg}(A) = 3 - 1 = 2$.",
                    ],
                },
            ],
            "raw_sections": [
                s for s in sec03 if "Pizarra" in s["title"]
            ] + [s for s in sec05 if "Tema 3" in s["title"]],
        },
        {
            "id": "aplicaciones_lineales",
            "order": 3,
            "topic_filter": "aplicaciones_lineales",
            "secondary_topic": None,
            "title": "Bloque 3 · Aplicaciones (Transformaciones) Lineales",
            "subtitle": "Axiomas de linealidad, núcleo e imagen, inyectividad/sobreyectividad/isomorfismos, matriz asociada y cambios de base.",
            "source_files": ["04_Teoria_Aplicaciones_Lineales.md", "05_Ejercicios_de_repaso_resueltos.md"],
            "definitions": [
                {
                    "term": "Transformación Lineal $T: V \\to W$",
                    "body_md": "Cumple los dos axiomas para todo $u, v \\in V$ y $\\alpha \\in \\mathbb{R}$: (1) $T(u+v) = T(u) + T(v)$ y (2) $T(\\alpha v) = \\alpha T(v)$. **Test rápido:** comprueba primero $T(0_V) = 0_W$; si falla, NO es lineal.",
                },
                {
                    "term": "Núcleo $\\operatorname{Ker}(T)$ e Imagen $\\operatorname{Im}(T)$",
                    "body_md": "$\\operatorname{Ker}(T) = \\{v \\in V : T(v) = 0_W\\} \\subseteq V$ y $\\operatorname{Im}(T) = \\{T(v) : v \\in V\\} \\subseteq W$. Si $A$ es la matriz asociada a $T$ en bases fijadas, $\\operatorname{Ker}(T)$ corresponde a $N(A)$ e $\\operatorname{Im}(T)$ a $C(A)$.",
                },
                {
                    "term": "Inyectiva, Sobreyectiva e Isomorfismo",
                    "body_md": "$T$ es **inyectiva** $\\iff \\operatorname{Ker}(T) = \\{0\\} \\iff \\dim\\operatorname{Ker}(T) = 0$ (un pivote por columna). $T$ es **sobreyectiva** $\\iff \\operatorname{Im}(T) = W \\iff \\operatorname{rg}(A) = \\dim W$. Es **isomorfismo** si es inyectiva y sobreyectiva (en $\\mathbb{R}^n \\to \\mathbb{R}^n$, equivale a $A$ invertible).",
                },
                {
                    "term": "Matriz de una TL y Cambio de Base",
                    "body_md": "Las columnas de $M(T, B_V, B_W)$ son las coordenadas en $B_W$ de las imágenes $T(v_1), \\dots, T(v_n)$ de los vectores de $B_V$. Al cambiar a nuevas bases $B'_V, B'_W$ con matrices de paso $P$ y $Q$: $A' = Q^{-1} A P$ (si es endomorfismo $V\\to V$ con misma base, $A' = P^{-1} A P$, matrices **semejantes**).",
                },
            ],
            "theorems": [
                {
                    "name": "Teorema de las Dimensiones",
                    "body_md": "Para toda aplicación lineal $T: V \\to W$ con $\\dim V < \\infty$: $$\\dim V = \\dim(\\operatorname{Ker} T) + \\dim(\\operatorname{Im} T)$$",
                },
                {
                    "name": "Determinación Única sobre una Base",
                    "body_md": "Una aplicación lineal queda unívocamente determinada si se conocen las imágenes $T(v_1), \\dots, T(v_n)$ de los vectores de una base de $V$. Para cualquier $v = \\sum c_i v_i$, $T(v) = \\sum c_i T(v_i)$.",
                },
                {
                    "name": "Restricciones Dimensionales para Inyectividad y Sobreyectividad",
                    "body_md": "Si $T: \\mathbb{R}^n \\to \\mathbb{R}^m$: si $n > m$, $T$ **nunca** puede ser inyectiva ($\\dim \\operatorname{Ker} \\ge n - m > 0$); si $n < m$, $T$ **nunca** puede ser sobreyectiva ($\\dim \\operatorname{Im} \\le n < m$).",
                },
            ],
            "worked_examples": [
                {
                    "title": "Reconstrucción de matriz canónica sin invertir (07 CO Mod A P7)",
                    "problem_md": "Dada $T:\\mathbb{R}^3\\to\\mathbb{R}^3$ con $T(1,0,0)=(1,0,0)$, $T(0,1,0)=(1,1,0)$ y $T(1,1,1)=(2,1,1)$, hallar $A$ y decidir si es inyectiva.",
                    "steps_md": [
                        "Como $(1,1,1) = e_1 + e_2 + e_3$, por linealidad $T(e_3) = T(1,1,1) - T(e_1) - T(e_2) = (2,1,1)-(1,0,0)-(1,1,0) = (0,0,1)$.",
                        "Colocando $T(e_1), T(e_2), T(e_3)$ por columnas: $A = \\begin{pmatrix}1&1&0\\\\0&1&0\\\\0&0&1\\end{pmatrix}$.",
                        "Como $A$ ya está escalonada con 3 pivotes, $\\operatorname{rg}(A)=3 \\Rightarrow \\dim\\operatorname{Ker}(T)=0$ ⇒ $T$ es **inyectiva** (e isomorfismo).",
                    ],
                },
                {
                    "title": "Compatibilidad de Ax = v desde el plano imagen (07 CO Mod A P6)",
                    "problem_md": "Si $\\operatorname{Im}(f) = \\{(x,y,z)\\in\\mathbb{R}^3 : x+y-z=0\\}$, clasificar $Ax = (2, 1, -1)^T$.",
                    "steps_md": [
                        "$\\operatorname{Im}(f)$ es un plano en $\\mathbb{R}^3$, luego $\\dim(\\operatorname{Im} f) = \\operatorname{rg}(A) = 2$ y $\\dim(\\operatorname{Ker} f) = 1$.",
                        "Sustituimos $v=(2,1,-1)$ en la ecuación del plano: $2 + 1 - (-1) = 4 \\neq 0 \\Rightarrow v \\notin \\operatorname{Im}(f)$.",
                        "Por tanto el sistema $Ax = v$ es **Incompatible (SI)**.",
                    ],
                },
            ],
            "raw_sections": sec04 + [s for s in sec05 if "Tema 4" in s["title"]],
        },
        {
            "id": "autovalores_diagonalizacion",
            "order": 4,
            "topic_filter": "diagonalizacion",
            "secondary_topic": None,
            "title": "Bloque 4 · Autovalores, Autovectores y Diagonalización",
            "subtitle": "Polinomio característico, subespacios propios, multiplicidades algebraica y geométrica, criterio de diagonalización y matrices simétricas.",
            "source_files": ["05_Ejercicios_de_repaso_resueltos.md", "07_Examenes_ordinaria_2025-26.md", "09_Banco_de_preguntas_examen.md"],
            "definitions": [
                {
                    "term": "Valor Propio (Autovalor) y Vector Propio (Autovector)",
                    "body_md": "$\\lambda \\in \\mathbb{R}$ es autovalor de $A_{n\\times n}$ si existe $v \\neq 0$ tal que $Av = \\lambda v \\iff (A - \\lambda I)v = 0$. El **subespacio propio** asociado es $E_\\lambda = \\operatorname{Ker}(A - \\lambda I)$.",
                },
                {
                    "term": "Polinomio Característico y Multiplicidades",
                    "body_md": "$p_A(\\lambda) = \\det(A - \\lambda I)$ (convención del banco UFV). La **multiplicidad algebraica** $m_a(\\lambda)$ es el exponente de $(\\lambda - \\lambda_0)$ en $p_A(\\lambda)$. La **multiplicidad geométrica** es $m_g(\\lambda) = \\dim E_\\lambda = n - \\operatorname{rg}(A - \\lambda I)$. Siempre se cumple $1 \\le m_g(\\lambda) \\le m_a(\\lambda)$.",
                },
                {
                    "term": "Diagonalización $A = P D P^{-1}$",
                    "body_md": "$A$ es diagonalizable si existe $P$ invertible (sus columnas son $n$ autovectores LI) y $D$ diagonal (con los autovalores en el mismo orden) tales que $A = P D P^{-1}$. Esto permite calcular potencias al instante: $A^k = P D^k P^{-1}$.",
                },
            ],
            "theorems": [
                {
                    "name": "Criterio Fundamental de Diagonalización en ℝ",
                    "body_md": "$A \\in \\mathcal{M}_{n\\times n}(\\mathbb{R})$ es diagonalizable en $\\mathbb{R}$ **si y solo si**: (1) todas las raíces de $p_A(\\lambda)$ son reales (la suma de sus $m_a$ es $n$), y (2) para todo autovalor $\\lambda$, $m_g(\\lambda) = m_a(\\lambda)$. **Caso particular:** si tiene $n$ autovalores reales distintos, siempre es diagonalizable.",
                },
                {
                    "name": "Atajos Clave para Exámenes",
                    "body_md": "(1) En una matriz **triangular o diagonal**, los autovalores son los elementos de la diagonal principal. (2) $\\operatorname{tr}(A) = \\sum \\lambda_i$ y $|A| = \\prod \\lambda_i$. (3) $0$ es autovalor de $A \\iff A$ es singular ($|A|=0$). (4) Toda matriz **simétrica real** ($A=A^T$) es siempre diagonalizable (incluso ortogonalmente, $A=QDQ^T$).",
                },
                {
                    "name": "Invariantes bajo Semejanza ($B = P^{-1} A P$)",
                    "body_md": "Dos matrices semejantes tienen exactamente el mismo polinomio característico, los mismos autovalores con las mismas multiplicidades $m_a$ y $m_g$, mismo determinante, misma traza y mismo rango.",
                },
            ],
            "worked_examples": [
                {
                    "title": "Construcción de matriz 2×2 no diagonalizable (07 CO Mod A P8)",
                    "problem_md": "Construir una matriz $2\\times 2$ no diagonalizable con único autovalor $\\lambda = 4$.",
                    "steps_md": [
                        "Elegimos el bloque de Jordan triangular $A = \\begin{pmatrix}4 & 1 \\\\ 0 & 4\\end{pmatrix}$.",
                        "Por ser triangular, su único autovalor es $\\lambda = 4$ con $m_a(4) = 2$.",
                        "$A - 4I = \\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}$ tiene rango 1 ⇒ $m_g(4) = 2 - 1 = 1 < 2 = m_a(4)$ (base $E_4 = \\{(1,0)\\}$), luego **no es diagonalizable**.",
                    ],
                },
                {
                    "title": "Estudio de diagonalizabilidad triangular 3×3 (07 CO Mod A P9)",
                    "problem_md": "Estudiar si $A = \\begin{pmatrix}3&0&0\\\\1&3&0\\\\0&0&-1\\end{pmatrix}$ es diagonalizable.",
                    "steps_md": [
                        "Diagonal principal ⇒ $\\lambda_1 = 3$ ($m_a=2$) y $\\lambda_2 = -1$ ($m_a=1$).",
                        "Para $\\lambda_1=3$: $A-3I = \\begin{pmatrix}0&0&0\\\\1&0&0\\\\0&0&-4\\end{pmatrix}$ tiene rango 2 (pivotes en col 1 y col 3).",
                        "$m_g(3) = 3 - 2 = 1 \\neq 2 = m_a(3)$ ⇒ **NO es diagonalizable**.",
                    ],
                },
            ],
            "raw_sections": [s for s in sec05 if "Tema 5" in s["title"]],
        },
    ]


def _build_matlab_lab() -> dict[str, Any]:
    """Estructura el Laboratorio MATLAB a partir de 01 (rúbrica) y 06_Practicas_MATLAB.md."""
    md06 = _read_md("06_Practicas_MATLAB.md")

    rubric_rules = [
        {"num": 1, "title": "Editor de texto y ecuaciones", "desc": "Explica el razonamiento en el editor de texto/ecuaciones del Live Script, evitando comentarios `%` extensos dentro del código."},
        {"num": 2, "title": "Ocultar cálculos intermedios con ;", "desc": "Finaliza TODAS las sentencias intermedias con `;` para que la consola no escupa matrices temporales."},
        {"num": 3, "title": "Resultados formateados con fprintf() y unidades", "desc": "Usa `fprintf('Texto: %6.2f unidades\\n', val)` con salto de línea `\\n` y unidades; NO uses `disp()` para números con decimales."},
        {"num": 4, "title": "Secciones limpias: clc, clear, clf", "desc": "Separa cada problema en una sección del Live Script iniciada siempre con `clc, clear, clf`."},
        {"num": 5, "title": "Nomenclatura estricta de archivos .mlx", "desc": "Empieza por letra, solo letras/números/guiones bajos, SIN tildes, ñ ni espacios (ej. `PR01_Nunez_Garcia_Jose.mlx`)."},
        {"num": 6, "title": "Espaciado en operadores binarios", "desc": "Separa `+`, `-`, `*`, `/`, `=`, `<`, `>` con espacios (`z = (a + b)^3;`); el exponente `^` NO se separa."},
        {"num": 7, "title": "No sobrescribir funciones de MATLAB", "desc": "Jamás uses `sum`, `plot`, `length`, `mean`, `det`, `rank` o `inv` como nombres de variables."},
        {"num": 8, "title": "No repetir asignaciones", "desc": "Define cada parámetro una única vez por problema y reutiliza la variable en los cálculos siguientes."},
    ]

    cheat_sheet = [
        {"fn": "x = A \\ b", "category": "Sistemas", "desc": "Resuelve Ax = b (solución única o mínimos cuadrados si SCI). Comprobar siempre con `norm(A*x - b)`.", "example": "A = [2 2 4; 1 2 0; 1 3 1];\nb = [2300; 800; 1500];\nx = A \\ b;\ncheck = norm(A * x - b);"},
        {"fn": "rref([A b])", "category": "Sistemas", "desc": "Forma escalonada reducida de la matriz ampliada. Obligatoria para sistemas compatibles indeterminados (SCI).", "example": "Ab = [A b];\nsol = rref(Ab);"},
        {"fn": "null(A)", "category": "Espacios Vectoriales", "desc": "Base ortonormal (columnas de norma 1) del espacio nulo Ker(A) = {x : Ax = 0}.", "example": "N = null(A);"},
        {"fn": "fprintf()", "category": "Salida", "desc": "Imprime resultados con control exacto de cifras/decimales (`%6.2f`, `%d`, `%s`, `%e`) y salto `\\n`.", "example": "for i = 1:length(x)\n    fprintf('x(%d) = %6.2f uds\\n', i, x(i))\nend"},
        {"fn": "polyval / polyfit / roots", "category": "Polinomios", "desc": "Polinomios como vector fila de mayor a menor grado (`p = [-5 0 4 0 -1 12]`). Evalúa, ajusta por mínimos cuadrados y halla raíces.", "example": "p = polyfit(t, y, 2);\ny_est = polyval(p, 12);\nraices = roots(p);"},
        {"fn": "[V, D] = eig(A)", "category": "Diagonalización", "desc": "D es diagonal de autovalores; columnas de V son autovectores normalizados (norma 1).", "example": "[V, D] = eig(A);\np = poly(A);\nerr_CH = norm(polyvalm(p, A));"},
        {"fn": "graph / digraph", "category": "Grafos", "desc": "Crea grafos no dirigidos o dirigidos desde listas de aristas `(s, t, pesos)` o matriz de adyacencia.", "example": "G = digraph(s, t, pesos, nodos);\nH = plot(G, 'EdgeLabel', G.Edges.Weight);"},
        {"fn": "shortestpath / highlight", "category": "Grafos", "desc": "Calcula el camino mínimo ponderado entre dos nodos y lo resalta visualmente.", "example": "[camino, coste] = shortestpath(G, 'Madrid', 'Gerona');\nhighlight(H, camino, 'EdgeColor', 'r', 'LineWidth', 2);"},
        {"fn": "sparse / full / adjacency", "category": "Grafos y Redes", "desc": "Almacena matrices dispersas eficientemente y extrae la matriz de adyacencia ponderada de un grafo.", "example": "A_sparse = adjacency(G, 'weighted');\nA = full(A_sparse);"},
        {"fn": "centrality(G, 'pagerank')", "category": "Redes / PageRank", "desc": "Calcula centralidad PageRank o de intermediación (`betweenness`) en redes de gran tamaño.", "example": "pr = centrality(G, 'pagerank', 'Importance', G.Edges.Weight);\nbt = centrality(G, 'betweenness');"},
    ]

    # Extraer los 8 módulos del cuaderno común de prácticas de 06_Practicas_MATLAB.md
    guide_defs = [
        ("01", "01. ASIGNACIÓN DE RECURSOS", "AR", "Modelado de recursos limitados (cultivo de bacterias, dietas, racks de servidores) como sistema lineal Ax = b resuelto con `A \\ b` y verificación de residuo `norm(A*x - b)`."),
        ("02", "02. DISTRIBUCIÓN DE CALOR", "DC", "Equilibrio térmico estacionario en placas 2D: cada nodo interior es el promedio de sus 4 vecinos (N, S, E, O), dando un sistema lineal con diagonal 4."),
        ("03", "03. INTERPOLACIÓN POLINÓMICA", "IP", "Determinación del polinomio de grado n−1 que pasa exactamente por n puntos mediante matriz de Vandermonde y comprobación con `polyfit` / `polyval`."),
        ("04", "04. FLUJO DE REDES", "FR", "Conservación de flujo en nodos (tráfico, agua, redes eléctricas): flujo entrante = flujo saliente. Produce sistemas SCI resueltos con `rref([A b])`."),
        ("05", "05. GRAFOS", "GR", "Matrices de adyacencia, potencias Aᵏ (número de caminos de longitud k), matrices dispersas (`sparse`), `graph`/`digraph` y camino mínimo (`shortestpath`)."),
        ("06", "06. ANÁLISIS DE INSUMOS-PRODUCTOS DE LEONTIEF", "LEO", "Economía cerrada ($Ax = x$, núcleo de $I-A$) y economía abierta ($(I-C)x = d$, producción necesaria para satisfacer la demanda externa $d$)."),
        ("07", "07. CADENAS DE MARKOV", "MK", "Evolución $x_{k+1} = P x_k$ con matriz de transición estocástica y vector estacionario ($P\\pi = \\pi$) calculado por potencias, `eig(P)` y sistema lineal."),
        ("08", "08.  MOTORES DE BÚSQUEDA EN INTERNET. PAGE-RANK", "PR", "Grafo web, matriz de transición con factor de amortiguación (damping $d = 0.85$), tratamiento de nodos colgantes y ranking por autovector dominante."),
    ]

    guides = []
    for idx, (code_num, heading, acronym, summary) in enumerate(guide_defs):
        start = md06.find(f"#### {heading}")
        snippet = ""
        code_examples: list[str] = []
        if start != -1:
            next_start = len(md06)
            if idx + 1 < len(guide_defs):
                nxt = md06.find(f"#### {guide_defs[idx + 1][1]}", start + 10)
                if nxt != -1:
                    next_start = nxt
            else:
                nxt = md06.find("## Práctica 1", start + 10)
                if nxt != -1:
                    next_start = nxt
            chunk = md06[start:next_start]
            snippet = chunk[:5500].strip()
            code_examples = [m.group(1).strip() for m in re.finditer(r"```matlab\n(.*?)```", chunk, re.S)][:4]
        guides.append(
            {
                "id": f"matlab_{code_num}",
                "number": code_num,
                "acronym": acronym,
                "title": heading.replace("  ", " ").strip(),
                "summary": summary,
                "code_examples": code_examples,
                "content_md": snippet,
            }
        )

    # Extraer Prácticas 1, 2 y 3 evaluables del Grupo B
    practicas_eval = []
    for sec in _extract_h2_sections(md06, max_chars_per_section=7000):
        if sec["title"].startswith("Práctica "):
            practicas_eval.append(sec)

    return {
        "rubric_rules": rubric_rules,
        "cheat_sheet": cheat_sheet,
        "guides": guides,
        "evaluated_practices": practicas_eval,
    }


def _build_project_hub() -> dict[str, Any]:
    """Estructura completa del Proyecto 01: Red Logística (10_Proyecto_Red_Logistica.md) + simulación NumPy."""
    retos = [
        {
            "id": "reto_1",
            "number": 1,
            "title": "Reto 1 · Estimación de la demanda logística futura (2028)",
            "weight": "5%",
            "math_core": "Ajuste polinomial por mínimos cuadrados (`polyfit`, `polyval`, `rmse`) con desplazamiento de origen $t = \\text{año} - 2016$.",
            "objectives": [
                "Representar datos históricos 2016–2025 y curvas polinómicas (grados 1, 2, 3) en una sola gráfica hasta 2028.",
                "Comparar modelos mediante RMSE y justificar la elección (equilibrio entre ajuste y sobreajuste al extrapolar a 2028).",
                "Imprimir la ecuación seleccionada con `fprintf` (8 decimales) y tabla con grado, RMSE, predicción 2028 e incremento % vs 2025.",
            ],
            "matlab_functions": ["polyfit", "polyval", "rmse", "plot", "table", "fprintf"],
            "template_hint": "Desplaza el eje X con `t = anios - 2016;` para evitar mal condicionamiento numérico de Vandermonde; el año 2028 corresponde a `t = 12`.",
        },
        {
            "id": "reto_2",
            "number": 2,
            "title": "Reto 2 · Representación matemática de la red logística",
            "weight": "5%",
            "math_core": "Teoría de Grafos: dígrafo ponderado $G = (V, E, w)$ con 12 centros y 22 rutas dirigidas semanales.",
            "objectives": [
                "Importar `P01 Datos.xlsx` directamente con `readtable` (prohibido copiar matrices a mano).",
                "Justificar por qué un grafo dirigido ponderado supera a una tabla simple para escalar a cientos de centros.",
                "Construir y graficar `G = digraph(Origen, Destino, Flujo)` con etiquetas de flujo.",
            ],
            "matlab_functions": ["readtable", "digraph", "plot", "numnodes", "numedges", "fprintf"],
            "template_hint": "Algunas conexiones son unidireccionales (ej. Madrid → Zaragoza) y otras bidireccionales con distinto peso (Madrid ↔ Valencia): por eso se requiere `digraph`, no `graph`.",
        },
        {
            "id": "reto_3",
            "number": 3,
            "title": "Reto 3 · Almacenamiento y representación computacional",
            "weight": "5%",
            "math_core": "Matriz de adyacencia ponderada (dispersa `sparse` para gran escala y densa `full` para verificación) + balance de flujos entrantes/salientes.",
            "objectives": [
                "Construir la matriz de adyacencia ponderada $A$ donde $a_{ij}$ es el flujo semanal del centro $i$ al centro $j$.",
                "Presentar tabla con nombres de filas y columnas (`array2table`) y tabla de flujo entrante (`sum(A, 1)'`) y saliente (`sum(A, 2)`).",
                "Verificar integridad de datos comprobando suma total de flujos y número total de rutas (`nnz(A)` = 22).",
            ],
            "matlab_functions": ["adjacency", "full", "sparse", "array2table", "sum", "table"],
            "template_hint": "En redes con cientos de nodos la matriz tiene mayoría de ceros; `sparse` guarda solo los elementos no nulos y sus índices $(i,j)$, ahorrando memoria y tiempo.",
        },
        {
            "id": "reto_4",
            "number": 4,
            "title": "Reto 4 · Comportamiento dinámico de la red (Cadenas de Markov)",
            "weight": "5%",
            "math_core": "Matriz estocástica de transición $P$ y distribución estacionaria $\\pi$ ($P\\pi = \\pi$) por 3 métodos independientes con error $< 10^{-12}$.",
            "objectives": [
                "Normalizar los flujos salientes de cada centro para construir la matriz de transición estocástica $P$.",
                "Calcular el estado de equilibrio mediante 3 métodos: (1) Iteración de potencias $P^k x_0$, (2) Autovector de $\\lambda = 1$ con `eig`, y (3) Espacio nulo / sistema lineal `null(P - eye(n))`.",
                "Validar la precisión calculando la norma del residuo $\\|P\\pi - \\pi\\|_2 < 10^{-12}$ y presentar ranking en %.",
            ],
            "matlab_functions": ["sum", "eig", "null", "norm", "table", "sort"],
            "template_hint": "Asegúrate de no mezclar la convención fila-estocástica con columna-estocástica: si normalizas por columnas, $\\pi$ satisface $P\\pi = \\pi$ y `sum(pi) == 1`.",
        },
        {
            "id": "reto_5",
            "number": 5,
            "title": "Reto 5 · Importancia estructural de la red (4 criterios y PageRank)",
            "weight": "5%",
            "math_core": "Comparativa multicriterio: (C1) Volumen total, (C2) Grado de conexiones, (C3) Equilibrio Markov/PageRank, (C4) Centralidad de intermediación (`betweenness`).",
            "objectives": [
                "Calcular los 4 criterios de importancia y normalizarlos en tanto por uno (máximo = 1) para una gráfica de barras comparativa.",
                "Contrastar la implementación propia con `centrality(G, 'pagerank', 'Importance', G.Edges.Weight)` y `centrality(G, 'betweenness')`.",
                "Justificar por qué un nodo con menor volumen bruto (ej. Zaragoza como puente norte-este) puede ser más crítico estructuralmente.",
            ],
            "matlab_functions": ["indegree", "outdegree", "centrality", "sort", "bar", "table"],
            "template_hint": "La intermediación (`betweenness`) detecta cuellos de botella en caminos mínimos; PageRank captura si un nodo recibe flujo desde otros hubs importantes.",
        },
        {
            "id": "reto_6",
            "number": 6,
            "title": "Reto 6 · Escenario de emergencia: DANA en Valencia",
            "weight": "5%",
            "math_core": "Análisis de resiliencia de redes: eliminación del nodo Valencia y sus 8 rutas incidentes, recálculo de PageRank con damping $d=0.85$ y plan de choque 72h.",
            "objectives": [
                "Eliminar el centro de Valencia (`rmnode` o filtrado con `setdiff`/`ismember`) e identificar las 8 conexiones perdidas y los nodos aislados (Murcia y Alicante quedan sin rutas operativas!).",
                "Recalcular PageRank con `centrality` y construir la tabla comparativa de posiciones antes vs. después de la DANA.",
                "Seleccionar justificadamente los **2 centros prioritarios** a reforzar con el presupuesto extraordinario en las primeras 72 horas.",
            ],
            "matlab_functions": ["find", "setdiff", "ismember", "rmnode", "digraph", "centrality", "sort"],
            "template_hint": "Al caer Valencia, Murcia y Alicante pierden todas sus conexiones (nodos aislados/colgantes), por lo que el factor de amortiguación de PageRank es imprescindible y el tráfico se desplaza hacia Madrid, Zaragoza y Barcelona.",
        },
    ]

    oral_defense_questions = [
        {
            "q": "¿Por qué no puedes usar un polinomio de grado 9 en el Reto 1 aunque tenga RMSE = 0 sobre los 10 datos históricos?",
            "a": "Porque sufriría sobreajuste extremo (fenómeno de Runge): interpola el ruido puntual (como la caída de 2020) pero oscila violentamente al extrapolar fuera del intervalo hacia 2028, dando predicciones absurdas.",
        },
        {
            "q": "¿Por qué `digraph` es obligatorio en vez de `graph` para modelar LOGISPAÑA?",
            "a": "Porque el flujo logístico tiene sentido y asimetría: por ejemplo Madrid envía 780 t/sem a Valencia pero Valencia envía 350 t/sem a Madrid, y Madrid→Zaragoza no tiene vuelta directa.",
        },
        {
            "q": "¿Qué significa matemáticamente que la norma del residuo `norm(P*pi - pi)` sea del orden de `1e-15`?",
            "a": "Que el vector $\\pi$ satisface la ecuación de equilibrio $P\\pi = \\pi$ (autovector para $\\lambda = 1$) hasta el límite de precisión de máquina IEEE 754 (~$2.2\\times 10^{-16}$), cumpliendo sobradamente la tolerancia $< 10^{-12}$.",
        },
        {
            "q": "¿Qué ocurre con Murcia y Alicante cuando Valencia queda inoperativa por la DANA y por qué falla una cadena de Markov pura sin damping?",
            "a": "Todas las rutas de Murcia y Alicante entran y salen exclusivamente por Valencia; al eliminar Valencia quedan aislados (grado de salida 0 = nodos colgantes), rompiendo la irreducibilidad/estocasticidad de $P$. PageRank lo resuelve con el factor de teletransporte/amortiguación $(1-d)/n$.",
        },
        {
            "q": "¿Por qué no basta mirar el volumen de toneladas (Criterio 1) para elegir dónde invertir?",
            "a": "El volumen bruto es una medida puramente local; ignora la conectividad en cascada. Un hub puente como Zaragoza o Madrid controla rutas críticas entre regiones (alta intermediación y PageRank), por lo que su caída afecta a toda la red.",
        },
    ]

    return {
        "title": "Proyecto 01 · Análisis de una Red Logística (LOGISPAÑA)",
        "rubric_summary": [
            {"item": "Retos 1 a 6 (entregas parciales)", "weight": "30% (5% cada reto)"},
            {"item": "Informe Final ejecutable (Live Script P01_GrupoX.mlx)", "weight": "20%"},
            {"item": "Presentación Grupal (30% del bloque defensa)", "weight": "15%"},
            {"item": "Defensa Oral Individual (70% del bloque defensa)", "weight": "35%"},
        ],
        "retos": retos,
        "oral_defense_questions": oral_defense_questions,
        "baseline_analysis": analyze_network(disabled_center=None),
        "dana_valencia_analysis": analyze_network(disabled_center="Valencia"),
    }


def _parse_question_bank_index() -> dict[str, Any]:
    """Indexa las 122 preguntas del banco (09) y las variantes prácticas de CO/CEX (07, 08) sin filtrar respuestas en modo práctica."""
    md09 = _read_md("09_Banco_de_preguntas_examen.md")
    md07 = _read_md("07_Examenes_ordinaria_2025-26.md")
    md08 = _read_md("08_Examenes_extraordinaria_2025-26.md")

    topic_map = {
        "1": ("sistemas", "Tema 1 · Sistemas de ecuaciones lineales"),
        "2": ("matrices", "Tema 2 · Matrices"),
        "4": ("espacios_vectoriales", "Tema 4 · Espacios vectoriales"),
        "5": ("aplicaciones_lineales", "Tema 5 · Transformaciones lineales"),
        "6": ("diagonalizacion", "Tema 6 · Diagonalización, autovalores y autovectores"),
    }

    # Extraer entradas numeradas '1.1  Título' ... con su convocatoria y pregunta (sin incluir respuesta en listado público!)
    pattern = re.compile(
        r"(?m)^(?P<num>[12456]\.\d+)\s+(?P<title>[^\n]+)\n(?P<meta>202\d/\d{2}\s*·[^\n]+)\n\n(?P<body>.*?)(?=\nRespuesta\n|\n[12456]\.\d+\s+|\Z)",
        re.S,
    )
    entries = []
    for m in pattern.finditer(md09):
        num = m.group("num")
        t_prefix = num.split(".")[0]
        topic_slug, topic_label = topic_map.get(t_prefix, ("general", "General"))
        body_clean = re.sub(r"\n?Ingeniería Informática · UFV\s+\d+\n?", "\n", m.group("body")).strip()
        body_clean = re.sub(r"```\s*#### Página \d+\s*```text\s*", "\n", body_clean).strip()
        entries.append(
            {
                "code": num,
                "topic": topic_slug,
                "topic_label": topic_label,
                "title": m.group("title").strip(),
                "exam_origin": m.group("meta").strip(),
                "statement_preview": body_clean[:600],
            }
        )

    practical_variants = []
    for tag, src in [("CO 2025/26", md07), ("CEX 2025/26", md08)]:
        for sec in _extract_h2_sections(src, max_chars_per_section=2500):
            if "Teórico" not in sec["title"]:
                practical_variants.append(
                    {
                        "convocatoria": tag,
                        "title": sec["title"],
                        "source": sec["source"],
                        "excerpt_md": sec["content_md"][:1400],
                    }
                )

    return {
        "total_bank_questions": len(entries),
        "bank_entries": entries,
        "practical_exams_count": len(practical_variants),
        "practical_variants": practical_variants,
    }


@lru_cache(maxsize=1)
def get_course_index() -> dict[str, Any]:
    md00 = _read_md("00_INDICE.md")
    md01 = _read_md("01_Asignatura_guia_y_normas.md")

    # Extraer secciones Grossman de 01
    grossman_match = re.search(r"## Secciones del libro.*?```text\n(.*?)```", md01, re.S)
    grossman_text = grossman_match.group(1).strip() if grossman_match else ""

    return {
        "course_meta": {
            "name": "Matemáticas para la Ingeniería I (MPI1)",
            "code": "5666",
            "ects": 6,
            "degree": "Grado en Ingeniería Informática · Escuela Politécnica Superior (UFV)",
            "evaluation": [
                {"part": "SE1 · Exámenes teórico-prácticos", "weight": "50%", "min": "Mínimo 5/10"},
                {"part": "SE2.1 · Prácticas individuales MATLAB / Proyecto", "weight": "40%", "min": "Mínimo 5/10"},
                {"part": "SE2.2 · Participación (≥80% asistencia)", "weight": "10%", "min": "No recuperable en CEX"},
            ],
            "bibliography": [
                "Stanley I. Grossman y José Job Flores Godoy, Álgebra lineal, 8.ª ed., McGraw-Hill, 2019 (básica).",
                "David C. Lay, Álgebra lineal y sus aplicaciones, 5.ª ed., Pearson, 2016 (complementaria).",
            ],
            "privacy_notice": "El archivo 11_Administrativo_listados_y_aulas.md contiene datos personales de terceros estudiantes y ha sido excluido deliberadamente de la indexación pública por cumplimiento RGPD.",
            "index_overview_md": md00,
            "grossman_syllabus": grossman_text,
        },
        "checklist": _parse_checklist_from_01(md01),
        "theory_modules": _build_theory_modules(),
        "matlab_lab": _build_matlab_lab(),
        "project_hub": _build_project_hub(),
        "exam_bank": _parse_question_bank_index(),
    }


def search_course_content(query: str) -> list[dict[str, Any]]:
    q = query.strip().lower()
    if len(q) < 2:
        return []
    idx = get_course_index()
    hits: list[dict[str, Any]] = []

    for mod in idx["theory_modules"]:
        for d in mod["definitions"]:
            if q in d["term"].lower() or q in d["body_md"].lower():
                hits.append({"kind": "Definición", "module_id": mod["id"], "title": d["term"], "snippet": d["body_md"][:240], "route": f"/teoria?modulo={mod['id']}"})
        for t in mod["theorems"]:
            if q in t["name"].lower() or q in t["body_md"].lower():
                hits.append({"kind": "Teorema", "module_id": mod["id"], "title": t["name"], "snippet": t["body_md"][:240], "route": f"/teoria?modulo={mod['id']}"})
        for ex in mod["worked_examples"]:
            if q in ex["title"].lower() or q in ex["problem_md"].lower():
                hits.append({"kind": "Ejemplo resuelto", "module_id": mod["id"], "title": ex["title"], "snippet": ex["problem_md"][:240], "route": f"/teoria?modulo={mod['id']}"})

    for fn in idx["matlab_lab"]["cheat_sheet"]:
        if q in fn["fn"].lower() or q in fn["desc"].lower() or q in fn["category"].lower():
            hits.append({"kind": "MATLAB Función", "module_id": "matlab", "title": fn["fn"], "snippet": fn["desc"], "route": "/matlab"})

    for g in idx["matlab_lab"]["guides"]:
        if q in g["title"].lower() or q in g["summary"].lower():
            hits.append({"kind": "Práctica MATLAB", "module_id": g["id"], "title": g["title"], "snippet": g["summary"], "route": "/matlab"})

    for r in idx["project_hub"]["retos"]:
        if q in r["title"].lower() or q in r["math_core"].lower():
            hits.append({"kind": "Proyecto Red Logística", "module_id": r["id"], "title": r["title"], "snippet": r["math_core"], "route": "/proyecto"})

    return hits[:30]
