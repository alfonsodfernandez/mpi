# Banco de preguntas de álgebra (122 preguntas de exámenes 2022/23–2025/26)

Versión completa con enunciados y respuestas. Las otras dos versiones del banco (`Banco_preguntas_algebra_UFV_Enunciados.pdf`, sólo enunciados, y `Banco_preguntas_algebra_UFV_Presentacion.pdf`, las mismas preguntas y soluciones en formato diapositivas) tienen el mismo contenido y no se repiten aquí.

**Contenido de este archivo:**
- Banco de preguntas: enunciados y respuestas


## Banco de preguntas: enunciados y respuestas

*Fuente: `Banco_preguntas_algebra_UFV.pdf`*

#### Página 1

```text
GRADO EN INGENIERÍA INFORMÁTICA

Banco de preguntas
de álgebra

Matemáticas para
la Ingeniería I

Enunciados y respuestas
Clasificación por temas y dificultad

122 preguntas · 15 exámenes

Cursos 2022/23 a 2025/26
Convocatorias ordinarias y extraordinaria

Octubre de 2026
```

#### Página 2

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

Contenido y criterios
Tema  Preguntas  Página
1. Sistemas de ecuaciones lineales  16  3
2. Matrices  13  17
3. Determinantes  0  24
4. Espacios vectoriales  40  25
5. Transformaciones lineales  24  41
6. Diagonalización, autovalores y autovectores  29  51

Criterio de clasificación. Cada pregunta se asigna al último tema necesario para resolverla. Se
incluyen los datos de contexto necesarios para que las preguntas encadenadas puedan leerse por
separado. Las 30 afirmaciones de verdadero/falso se clasifican individualmente y se reúnen en un
bloque final en cada tema correspondiente. Hay 117 preguntas y 5 bloques de verdadero/falso: 122
entradas numeradas en total. Cada afirmación conserva su modelo y apartado original.
Orden de trabajo. Dentro de cada tema se avanza desde la identificación directa y los ejemplos
elementales hacia los cálculos, las construcciones y las discusiones con parámetros. Las variantes
de dificultad equivalente se mantienen próximas. La numeración es tema.pregunta; cada cabecera
conserva curso, convocatoria, modelo y número original.
Convenciones. Se trabaja sobre ℝ. SCD, SCI y SI significan, respectivamente, compatible determina-
do, compatible indeterminado e incompatible. Se sigue la definición de forma escalonada utilizada
en los materiales del curso, con primer coeficiente no nulo igual a 1 en cada fila no nula. En una
factorización 𝐿𝑈 normalizada, la diagonal de 𝐿 está formada por unos. Se usa 𝑝𝐴 (𝜆) = det(𝐴 − 𝜆𝐼).

Ingeniería Informática · UFV  2
```

#### Página 3

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 1

Sistemas de ecuaciones lineales
Formas escalonadas, interpretación de soluciones y discusión mediante Gauss.

1.1  Construcción de una matriz ampliada escalonada
2024/25 · Ordinaria · Modelo A · Pregunta original 1

Escribe una forma escalonada de la matriz ampliada de un sistema lineal de 5 ecuaciones con 4
variables que sea compatible indeterminado.
Respuesta
Un ejemplo es
1  2  3  4  5
⎡  ⎤
⎢ 0  1  2  3  4 ⎥
⎢  ⎥
⎢ 0  0  1  2  3 ⎥.
⎢ 0  0  0  0  0 ⎥
⎢  ⎥
⎣ 0  0  0  0  0 ⎦
No hay ecuación contradictoria y queda una variable libre. Tres pivotes son una posibilidad, no una
necesidad: cualquier ejemplo compatible con menos de cuatro pivotes sirve.

1.2  Construcción de una matriz ampliada escalonada
2024/25 · Ordinaria · Modelo B · Pregunta original 1

Escribe una forma escalonada de la matriz ampliada de un sistema lineal de 4 ecuaciones con 5
variables que sea incompatible.
Respuesta
Un ejemplo es
1  2  3  4  5  6
⎡  ⎤
⎢ 0  1  2  3  4  5 ⎥
⎢  ⎥.
⎢ 0  0  1  2  3  4 ⎥
⎢  ⎥
⎣ 0  0  0  0  0  1 ⎦
La última fila expresa 0 = 1, por lo que el sistema es incompatible.

Ingeniería Informática · UFV  3
```

#### Página 4

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.3  Construcción de una matriz ampliada escalonada
2024/25 · Ordinaria · Modelo C · Pregunta original 1

Escribe una forma escalonada de la matriz ampliada de un sistema lineal de 6 ecuaciones con 4
variables que sea compatible determinado.
Respuesta
Un ejemplo es
1  2  3  4  5
⎡  ⎤
⎢ 0  1  2  3  4 ⎥
⎢  ⎥
⎢ 0  0  1  2  3 ⎥
⎢  ⎥.
⎢ 0  0  0  1  2 ⎥
⎢ 0  0  0  0  0 ⎥
⎢  ⎥
⎣ 0  0  0  0  0 ⎦
Es compatible y las cuatro variables tienen pivote: la solución es única. Las dos últimas ecuaciones
son redundantes.

1.4  Construcción de los tres tipos de sistema
2023/24 · Ordinaria · Modelo A · Pregunta original 2

Escribe una matriz ampliada en forma escalonada de un sistema lineal con 4 variables que sea: a)
compatible determinado; b) compatible indeterminado; c) incompatible. Explica por qué cada ejem-
plo cumple lo pedido.
Respuesta

a)
1  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  3 ⎥
⎢  ⎥
⎣ 0  0  0  1  4 ⎦
Es compatible y tiene 4 pivotes en los coeficientes: no hay variables libres. No es necesario que
haya exactamente 4 ecuaciones; podrían añadirse ecuaciones redundantes.
b)
1  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  3 ⎥
⎢  ⎥
⎣ 0  0  0  0  0 ⎦
Es compatible y tiene 3 pivotes para 4 variables: queda una variable libre.
c)
1  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  3 ⎥
⎢  ⎥
⎣ 0  0  0  0  1 ⎦
La última fila expresa 0 = 1, por lo que no tiene solución.

Ingeniería Informática · UFV  4
```

#### Página 5

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.5  Construcción de los tres tipos de sistema
2023/24 · Ordinaria · Modelo B · Pregunta original 2

Escribe una matriz ampliada en forma escalonada de un sistema lineal con 3 variables que sea: a)
compatible determinado; b) compatible indeterminado; c) incompatible. Explica por qué cada ejem-
plo cumple lo pedido.
Respuesta

a)
⎡ 1 0 0 1 ⎤
⎢ 0 1 0 2 ⎥
⎢  ⎥
⎣ 0 0 1 3 ⎦
Es compatible y tiene 3 pivotes en los coeficientes: no hay variables libres. No es necesario que
haya exactamente 3 ecuaciones; podrían añadirse ecuaciones redundantes.
b)
⎡ 1 0 0 1 ⎤
⎢ 0 1 0 2 ⎥
⎢  ⎥
⎣ 0 0 0 0 ⎦
Es compatible y tiene 2 pivotes para 3 variables: queda una variable libre.
c)
⎡ 1 0 0 1 ⎤
⎢ 0 1 0 2 ⎥
⎢  ⎥
⎣ 0 0 0 1 ⎦
La última fila expresa 0 = 1, por lo que no tiene solución.

Ingeniería Informática · UFV  5
```

#### Página 6

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.6  Construcción de los tres tipos de sistema
2023/24 · Ordinaria · Modelo C · Pregunta original 2

Escribe una matriz ampliada en forma escalonada de un sistema lineal con 5 variables que sea: a)
compatible determinado; b) compatible indeterminado; c) incompatible. Explica por qué cada ejem-
plo cumple lo pedido.
Respuesta

a)
1  0  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  0  3 ⎥
⎢ 0  0  0  1  0  4 ⎥
⎢  ⎥
⎣ 0  0  0  0  1  5 ⎦
Es compatible y tiene 5 pivotes en los coeficientes: no hay variables libres. No es necesario que
haya exactamente 5 ecuaciones; podrían añadirse ecuaciones redundantes.
b)
1  0  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  0  3 ⎥
⎢ 0  0  0  1  0  4 ⎥
⎢  ⎥
⎣ 0  0  0  0  0  0 ⎦
Es compatible y tiene 4 pivotes para 5 variables: queda una variable libre.
c)
1  0  0  0  0  1
⎡  ⎤
⎢ 0  1  0  0  0  2 ⎥
⎢  ⎥
⎢ 0  0  1  0  0  3 ⎥
⎢ 0  0  0  1  0  4 ⎥
⎢  ⎥
⎣ 0  0  0  0  0  1 ⎦
La última fila expresa 0 = 1, por lo que no tiene solución.

Ingeniería Informática · UFV  6
```

#### Página 7

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.7  Lectura de una matriz como ampliada o como coeficientes
2025/26 · Ordinaria · Modelo A · Pregunta original 2

Indica qué afirmaciones son ciertas y razona cada respuesta para la matriz

⎛ 1  0  0  3⎞
⎜
⎜ 0  1  1  2⎟
⎟
⎜
⎜  ⎟
⎟.
⎜
⎜  3⎟
⎟
⎜0  0  0  ⎟
⎝0  0  0  0⎠

a) Está en forma escalonada reducida por filas.
b) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas con infinitas
soluciones.
c) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas incompatible.
d) Podría ser la matriz de coeficientes de un sistema de cuatro ecuaciones y cuatro incógnitas in-
compatible.

Respuesta

a) Falsa. El último coeficiente principal es 3, no 1, y además hay entradas no nulas encima de él.
b) Falsa. Interpretada como ampliada, su tercera fila expresa 0 = 𝑐 con 𝑐 ≠ 0.
c) Verdadera, por la misma contradicción de la tercera fila.
d) Verdadera. Si es la matriz de coeficientes, basta elegir un término independiente 𝑏4 ≠ 0; su última
ecuación sería 0 = 𝑏4 .

Ingeniería Informática · UFV  7
```

#### Página 8

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.8  Lectura de una matriz como ampliada o como coeficientes
2025/26 · Ordinaria · Modelo B · Pregunta original 2

Indica qué afirmaciones son ciertas y razona cada respuesta para la matriz

⎛ 1  0 2 0⎞
⎜
⎜ 0  1 −1 3⎟
⎟
⎜
⎜  ⎟
⎟.
⎜
⎜  0 0 1⎟⎟
⎜0  ⎟
⎝0  0 0 0⎠

a) Está en forma escalonada por filas.
b) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas con infinitas
soluciones.
c) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas incompatible.
d) Podría ser la matriz de coeficientes de un sistema de cuatro ecuaciones y cuatro incógnitas in-
compatible.

Respuesta

a) Verdadera. Sus coeficientes principales son 1, avanzan hacia la derecha y la fila nula queda al
final.
b) Falsa. Interpretada como ampliada, su tercera fila expresa 0 = 𝑐 con 𝑐 ≠ 0.
c) Verdadera, por la misma contradicción de la tercera fila.
d) Verdadera. Si es la matriz de coeficientes, basta elegir un término independiente 𝑏4 ≠ 0; su última
ecuación sería 0 = 𝑏4 .

Ingeniería Informática · UFV  8
```

#### Página 9

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.9  Lectura de una matriz como ampliada o como coeficientes
2025/26 · Ordinaria · Modelo C · Pregunta original 2

Indica qué afirmaciones son ciertas y razona cada respuesta para la matriz

⎛ 1  0  2 0⎞
⎜
⎜ 0  0  1 3⎟⎟
⎜
⎜  ⎟
⎟.
⎜
⎜  0 −1⎟
⎟
⎜0  0  ⎟
⎝0  0  0 0⎠

a) Está en forma escalonada por filas.
b) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas con infinitas
soluciones.
c) Podría ser la matriz ampliada de un sistema de cuatro ecuaciones y tres incógnitas incompatible.
d) Podría ser la matriz de coeficientes de un sistema de cuatro ecuaciones y cuatro incógnitas in-
compatible.

Respuesta

a) Falsa con la definición del curso, que exige coeficientes principales iguales a 1: el de la tercera fila
es −1. Al multiplicar esa fila por −1 se obtiene la forma escalonada.
b) Falsa. Interpretada como ampliada, su tercera fila expresa 0 = 𝑐 con 𝑐 ≠ 0.
c) Verdadera, por la misma contradicción de la tercera fila.
d) Verdadera. Si es la matriz de coeficientes, basta elegir un término independiente 𝑏4 ≠ 0; su última
ecuación sería 0 = 𝑏4 .

Ingeniería Informática · UFV  9
```

#### Página 10

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.10  Discusión de un sistema de dos ecuaciones
2025/26 · Extraordinaria · Modelo A · Pregunta original 1

Dado el sistema, con 𝑘 ∈ ℝ,
⎧
{𝑥 + 𝑦 = 2,
⎨
{
⎩𝑘𝑥 − 𝑦 = 1,
a) Escribe la matriz ampliada y aplica Gauss, indicando operaciones y restricciones sobre 𝑘.
b) Sin determinantes ni Rouché–Frobenius, determina cuándo hay una solución, infinitas soluciones
o ninguna.

Respuesta
La matriz ampliada es
1  1 2
[  ].
𝑘 −1 1
Aplicando 𝐹2 ← 𝐹2 − 𝑘𝐹1 se obtiene

1  1  2
[  ].
0 −1 − 𝑘 1 − 2𝑘

Para 𝑘 ≠ −1, se divide la segunda fila por su coeficiente principal y resulta

⎡ 1 1  2 ⎤
⎢  2𝑘−1 ⎥.
⎣ 0 1  𝑘+1  ⎦
Hay una única solución en esos casos. Para 𝑘 = −1, la segunda fila expresa 0 = 3; al normalizarla
queda [0 0 ∣ 1]. Es incompatible. Nunca hay infinitas soluciones.

Ingeniería Informática · UFV  10
```

#### Página 11

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.11  Discusión de un sistema de dos ecuaciones
2025/26 · Extraordinaria · Modelo B · Pregunta original 1

Dado el sistema, con 𝑘 ∈ ℝ,
⎧
{𝑥 + 𝑦 = 2,
⎨
{
⎩𝑥 + 𝑘𝑦 = 1,
a) Escribe la matriz ampliada y aplica Gauss, indicando operaciones y restricciones sobre 𝑘.
b) Sin determinantes ni Rouché–Frobenius, determina cuándo hay una solución, infinitas soluciones
o ninguna.

Respuesta
La matriz ampliada es
1 1 2
[  ].
1 𝑘 1
Aplicando 𝐹2 ← 𝐹2 − 𝐹1 se obtiene
1  1  2
[  ].
0 𝑘 − 1 −1
Para 𝑘 ≠ 1, se divide la segunda fila por su coeficiente principal y resulta

⎡ 1 1  2 ⎤
⎢  1 ⎥.
⎣ 0 1 − 𝑘−1 ⎦

Hay una única solución en esos casos. Para 𝑘 = 1, la segunda fila expresa 0 = −1; al normalizarla
queda [0 0 ∣ 1]. Es incompatible. Nunca hay infinitas soluciones.

Ingeniería Informática · UFV  11
```

#### Página 12

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.12  Discusión de un sistema de dos ecuaciones
2025/26 · Extraordinaria · Modelo C · Pregunta original 1

Dado el sistema, con 𝑘 ∈ ℝ,
⎧
{−𝑘𝑥 + 𝑦 = 2,
⎨
{
⎩𝑥 + 𝑘𝑦 = 1.
a) Escribe la matriz ampliada y aplica Gauss, indicando operaciones y restricciones sobre 𝑘.
b) Sin determinantes ni Rouché–Frobenius, determina cuándo hay una solución, infinitas soluciones
o ninguna.

Respuesta
La matriz ampliada es
−𝑘 1 2
[  ].
1 𝑘 1
Aplicando 𝐹1 ↔ 𝐹2 y 𝐹2 ← 𝐹2 + 𝑘𝐹1 se obtiene

1  𝑘  1
[  2  ].
0 1+𝑘 2+𝑘

Para todo 𝑘 ∈ ℝ, ya que 1 + 𝑘 2 > 0, se divide la segunda fila por su coeficiente principal y resulta

⎡ 1 𝑘  1 ⎤
⎢  𝑘+2  ⎥.
⎣ 0 1  1+𝑘2 ⎦
Hay una única solución en esos casos. No hay restricciones reales: siempre existe una única solución.
Nunca hay infinitas soluciones ni incompatibilidad.

Ingeniería Informática · UFV  12
```

#### Página 13

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.13  Discusión de un sistema con parámetro
2022/23 · Ordinaria · Modelo B · Pregunta original 1

Considera el sistema 𝐶(𝑎)𝑥 = 𝑏(𝑎), con 𝑎 ∈ ℝ:

⎛ 1 1 𝑎⎞  ⎛ 1
⎜  ⎟  ⎜ ⎞ ⎟
𝐶(𝑎) = ⎜
⎜  ⎟,
⎜1 𝑎 1 ⎟
⎟  𝑏(𝑎) = ⎜
⎜ 1⎟
⎜  ⎟.
⎟
⎝ 𝑎 1 1⎠  ⎝ 1⎠

a) Escribe la matriz ampliada y aplica Gauss, indicando las operaciones y las restricciones sobre 𝑎.
b) Determina cuándo tiene una solución, infinitas soluciones o ninguna solución. No utilices deter-
minantes ni el teorema de Rouché–Frobenius.

Respuesta
La matriz ampliada es [𝐶(𝑎) ∣ 𝑏(𝑎)]. 𝐹2 ← 𝐹2 − 𝐹1 , 𝐹3 ← 𝐹3 − 𝑎𝐹1 y después 𝐹3 ← 𝐹3 + 𝐹2 dan

⎡ 1  1  𝑎  1 ⎤
⎢ 0 𝑎−1  1 − 𝑎  0 ⎥
⎢  ⎥
⎣ 0  0 −(𝑎 + 2)(𝑎 − 1) 1 − 𝑎 ⎦

Para 𝑎 ≠ 1, −2, normalizamos cada fila no nula dividiéndola por su coeficiente principal y obtenemos
la forma escalonada
⎡ 1 1  𝑎  1 ⎤
⎢ 0 1 −1  0 ⎥
⎢  1
⎥.
⎣ 0 0  1 𝑎+2 ⎦
Si 𝑎 ≠ 1, −2, los tres coeficientes principales son no nulos: hay una única solución. Si 𝑎 = 1, el sistema
se reduce a 𝑥 + 𝑦 + 𝑧 = 1: hay infinitas soluciones. Si 𝑎 = −2, la última ecuación es 0 = 3: no hay
solución. En los casos excepcionales se reordenan y normalizan las filas no nulas, sin dividir por los
factores que se anulan.

Ingeniería Informática · UFV  13
```

#### Página 14

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.14  Discusión de un sistema con parámetro
2022/23 · Ordinaria · Modelo C · Pregunta original 1

Considera el sistema 𝐶(𝑎)𝑥 = 𝑏(𝑎), con 𝑎 ∈ ℝ:

⎛ 1 2 4⎞  ⎛ 3
⎜  ⎟  ⎜ ⎞ ⎟
𝐶(𝑎) = ⎜
⎜
⎜ 2 −𝑎 2⎟
⎟,
⎟  𝑏(𝑎) = ⎜ −2
⎜ ⎟
⎜  ⎟.
⎟
⎝−1 −2 𝑎⎠  ⎝ 𝑎 ⎠

a) Escribe la matriz ampliada y aplica Gauss, indicando las operaciones y las restricciones sobre 𝑎.
b) Determina cuándo tiene una solución, infinitas soluciones o ninguna solución. No utilices deter-
minantes ni el teorema de Rouché–Frobenius.

Respuesta
La matriz ampliada es [𝐶(𝑎) ∣ 𝑏(𝑎)]. 𝐹2 ← 𝐹2 − 2𝐹1 y 𝐹3 ← 𝐹3 + 𝐹1 dan

⎡ 1  2  4  3 ⎤
⎢ 0 −𝑎 − 4  −6  −8 ⎥
⎢  ⎥
⎣ 0  0 𝑎+4 𝑎+3 ⎦

Para 𝑎 ≠ −4, normalizamos cada fila no nula dividiéndola por su coeficiente principal y obtenemos
la forma escalonada
⎡ 1 2 64  8
3 ⎤
⎢ 0 1  ⎥.
⎢  𝑎+4  𝑎+4 ⎥
𝑎+3
⎣ 0 0  1 𝑎+4 ⎦
Si 𝑎 ≠ −4, hay tres pivotes en los coeficientes y una única solución. Si 𝑎 = −4, la última ecuación es
0 = −1: no hay solución. Nunca hay infinitas soluciones. En los casos excepcionales se reordenan y
normalizan las filas no nulas, sin dividir por los factores que se anulan.

Ingeniería Informática · UFV  14
```

#### Página 15

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.15  Discusión de un sistema con parámetro
2022/23 · Ordinaria · Modelo D · Pregunta original 1

Considera el sistema 𝐶(𝑎)𝑥 = 𝑏(𝑎), con 𝑎 ∈ ℝ:

⎛ 1 1 −1⎞  ⎛ 1
⎜  ⎟  ⎜ ⎞ ⎟
𝐶(𝑎) = ⎜
⎜2 3 𝑎 ⎟
⎜  ⎟,
⎟  𝑏(𝑎) = ⎜
⎜ 3⎟
⎜  ⎟.
⎟
⎝1 𝑎 3 ⎠  ⎝ 2⎠

a) Escribe la matriz ampliada y aplica Gauss, indicando las operaciones y las restricciones sobre 𝑎.
b) Determina cuándo tiene una solución, infinitas soluciones o ninguna solución. No utilices deter-
minantes ni el teorema de Rouché–Frobenius.

Respuesta
La matriz ampliada es [𝐶(𝑎) ∣ 𝑏(𝑎)]. 𝐹2 ← 𝐹2 − 2𝐹1 , 𝐹3 ← 𝐹3 − 𝐹1 y 𝐹3 ← 𝐹3 − (𝑎 − 1)𝐹2 dan

⎡ 1 1  −1  1 ⎤
⎢ 0 1  𝑎 + 2  1 ⎥
⎢  ⎥
⎣ 0 0 −(𝑎 + 3)(𝑎 − 2) 2 − 𝑎 ⎦

Para 𝑎 ≠ −3, 2, normalizamos cada fila no nula dividiéndola por su coeficiente principal y obtenemos
la forma escalonada
⎡ 1 1  −1  1 ⎤
⎢ 0 1 𝑎+2  1 ⎥
⎢  1
⎥.
⎣ 0 0  1 𝑎+3 ⎦
Si 𝑎 ≠ −3, 2, hay una única solución. Si 𝑎 = 2, quedan dos ecuaciones con pivote y una fila nula: hay
infinitas soluciones. Si 𝑎 = −3, la última ecuación es 0 = 5: no hay solución. En los casos excepcionales
se reordenan y normalizan las filas no nulas, sin dividir por los factores que se anulan.

Ingeniería Informática · UFV  15
```

#### Página 16

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

1.16  Verdadero o falso: repaso del tema
2024/25 · Ordinaria · Pregunta original 10 · Modelos A, B y C

Indica si cada afirmación es verdadera (V) o falsa (F). Las etiquetas A.n, B.n y C.n indican el modelo
y el apartado original.

A.1 Un sistema de ecuaciones lineales puede tener exactamente dos soluciones.
A.2 Toda matriz es equivalente por filas a una matriz escalonada.
B.1 Todo sistema de una ecuación lineal 𝑎𝑥 + 𝑏𝑦 = 𝑐 con al menos uno de los coeficientes 𝑎, 𝑏
distinto de cero es compatible.
B.2 Todo sistema homogéneo de ecuaciones lineales es compatible.
C.1 Si una fila en una forma escalonada de una matriz ampliada es [0 0 0 5 0], el sistema asociado
es incompatible.
C.2 Si la matriz de coeficientes de un sistema de tres ecuaciones con tres incógnitas tiene un pivote
en cada columna, el sistema tiene una solución única.

Respuesta

A.1 F. Un sistema compatible sin variables libres tiene una única solución; si tiene alguna variable
libre, tiene infinitas. Por tanto, no puede tener exactamente dos.
A.2 V. El método de Gauss produce una matriz escalonada equivalente.
B.1 V. Si 𝑎 ≠ 0, se puede despejar 𝑥 en función de 𝑦. Si 𝑎 = 0, entonces 𝑏 ≠ 0 y se puede despejar
𝑦. En ambos casos existen soluciones.
B.2 V. El vector nulo siempre es solución.
C.1 F. La fila expresa 5𝑥4 = 0, una ecuación compatible; no expresa 0 = 𝑐 ≠ 0.
C.2 V. Hay tres pivotes en los coeficientes y ninguna fila contradictoria.

Ingeniería Informática · UFV  16
```

#### Página 17

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 2

Matrices
Operaciones elementales, inversión y productos de matrices.

2.1  Inversa de una matriz elemental
2024/25 · Ordinaria · Modelo A · Pregunta original 3

Obtén la inversa sin realizar cálculos, razonando el resultado:

⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 0 ⎟
⎟
⎝0 0 4 ⎠

Respuesta
La operación 𝐹3 ← 4𝐹3 se deshace con 𝐹3 ← 41 𝐹3 .

⎜⎛1 0 0 ⎞
⎟
𝐴−1 = ⎜0  ⎟.
⎜ 1 01 ⎟
⎜  ⎟
⎝0 0 4 ⎠

2.2  Inversa de una matriz elemental
2024/25 · Ordinaria · Modelo B · Pregunta original 4

Obtén la inversa sin realizar cálculos, razonando el resultado:

⎛ 1 0 0⎞
⎜  ⎟
𝐵=⎜  ⎟
⎟.
⎜0 1 0 ⎟
⎜
⎝0 3 1 ⎠

Respuesta
La operación 𝐹3 ← 𝐹3 + 3𝐹2 se deshace con 𝐹3 ← 𝐹3 − 3𝐹2 .

⎜⎛1 0 0 ⎞
⎟
𝐵−1 = ⎜  ⎟.
⎜0 1 0 ⎟
⎜  ⎟
⎝0 −3 1⎠

Ingeniería Informática · UFV  17
```

#### Página 18

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.3  Inversa de una matriz elemental
2024/25 · Ordinaria · Modelo C · Pregunta original 4

Obtén la inversa sin realizar cálculos, razonando el resultado:

⎛ 0 1 0⎞
⎜  ⎟
𝐶=⎜  ⎟.
⎜1 0 0 ⎟
⎜  ⎟
⎝0 0 1 ⎠

Respuesta
Intercambiar las dos primeras filas dos veces devuelve la matriz inicial. La operación es su propia
inversa.
⎛ 0 1 0⎞
⎜  ⎟
𝐶−1 = ⎜⎜1 0 0 ⎟
⎜  ⎟.
⎟
⎝0 0 1 ⎠

2.4  Inversión de operaciones elementales
2025/26 · Ordinaria · Modelo A · Pregunta original 3

Sea
⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜−2 1 0⎟
⎟
⎝ 1 0 1⎠
a) Describe las transformaciones elementales que representa 𝐴. b) Calcula 𝐴−1 a partir de esas trans-
formaciones.
Respuesta
Se obtiene 𝐴 aplicando a 𝐼 las operaciones 𝐹2 ← 𝐹2 − 2𝐹1 y 𝐹3 ← 𝐹3 + 𝐹1 . Su inversa deshace estas
operaciones en orden inverso: 𝐹3 ← 𝐹3 − 𝐹1 y 𝐹2 ← 𝐹2 + 2𝐹1 . Por tanto,

⎜⎛ 1 0 0⎞
⎟
𝐴−1 = ⎜  ⎟.
⎜ 2 1 0⎟
⎜  ⎟
⎝−1 0 1⎠

Ingeniería Informática · UFV  18
```

#### Página 19

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.5  Inversión de operaciones elementales
2025/26 · Ordinaria · Modelo B · Pregunta original 3

Sea
⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜ 3 1 0⎟
⎟
⎝−2 0 1⎠
a) Describe las transformaciones elementales que representa 𝐴. b) Calcula 𝐴−1 a partir de esas trans-
formaciones.
Respuesta
Se obtiene 𝐴 aplicando a 𝐼 las operaciones 𝐹2 ← 𝐹2 + 3𝐹1 y 𝐹3 ← 𝐹3 − 2𝐹1 . Su inversa deshace estas
operaciones en orden inverso: 𝐹3 ← 𝐹3 + 2𝐹1 y 𝐹2 ← 𝐹2 − 3𝐹1 . Por tanto,

⎜⎛ 1 0 0⎞
⎟
𝐴−1 = ⎜  ⎟.
⎜−3 1 0⎟
⎜  ⎟
⎝ 2 0 1⎠

2.6  Inversión de operaciones elementales
2025/26 · Ordinaria · Modelo C · Pregunta original 3

Sea
⎛ 1 −2 0⎞
⎜  ⎟
𝐴=⎜
⎜0 1 0 ⎟
⎜  ⎟
⎟.
⎝0 3 1 ⎠
a) Describe las transformaciones elementales que representa 𝐴. b) Calcula 𝐴−1 a partir de esas trans-
formaciones.
Respuesta
Se obtiene 𝐴 aplicando a 𝐼 las operaciones 𝐹1 ← 𝐹1 − 2𝐹2 y 𝐹3 ← 𝐹3 + 3𝐹2 . Su inversa deshace estas
operaciones en orden inverso: 𝐹3 ← 𝐹3 − 3𝐹2 y 𝐹1 ← 𝐹1 + 2𝐹2 . Por tanto,

⎜⎛1 2 0 ⎞
⎟
𝐴−1 = ⎜  ⎟.
⎜0 1 0 ⎟
⎜  ⎟
⎝0 −3 1⎠

Ingeniería Informática · UFV  19
```

#### Página 20

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.7  Producto de matrices elementales
2024/25 · Ordinaria · Modelo A · Pregunta original 4

Dadas
⎛ 1 2  3⎞  ⎛ 1 3  3⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟,
𝐴=⎜
⎜−1 −4 −1⎟
⎟  𝐵=⎜
⎜−1 −4 −1⎟
⎟
⎝0  1  0⎠  ⎝1  2  3⎠
encuentra dos matrices elementales 𝐸0 , 𝐸1 tales que 𝐸0 𝐸1 𝐵 = 𝐴.
Respuesta
Se pasa de 𝐵 a 𝐴 mediante 𝐹1 ↔ 𝐹3 y después 𝐹3 ← 𝐹3 − 𝐹1 . Las matrices correspondientes son

⎛ 0 0 1⎞  ⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟.
𝐸1 = ⎜
⎜0 1 0 ⎟
⎟  𝐸0 = ⎜
⎜ 0 1 0⎟
⎟
⎝1 0 0 ⎠  ⎝−1 0 1⎠

La primera operación actúa mediante el factor situado más a la derecha: 𝐸0 (𝐸1 𝐵) = 𝐴.

2.8  Producto de matrices elementales
2024/25 · Ordinaria · Modelo B · Pregunta original 3

Dadas
⎛ 1 2  3⎞  ⎛ 0 1 1⎞
⎜  ⎟  ⎜  ⎟
𝐴=⎜
⎜
⎜ 1 −1 −1 ⎟
⎟,
⎟  𝐵=⎜  ⎟,
⎜2 1 2 ⎟
⎜  ⎟
⎝0 1  1⎠  ⎝1 2 3 ⎠
encuentra dos matrices elementales 𝐸0 , 𝐸1 tales que 𝐸0 𝐸1 𝐵 = 𝐴.
Respuesta
Se pasa de 𝐵 a 𝐴 mediante 𝐹1 ↔ 𝐹3 y después 𝐹2 ← 𝐹2 − 𝐹1 . Las matrices correspondientes son

⎛ 0 0 1⎞  ⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟.
𝐸1 = ⎜
⎜0 1 0 ⎟
⎟  𝐸0 = ⎜
⎜−1 1 0⎟
⎟
⎝1 0 0 ⎠  ⎝ 0 0 1⎠

La primera operación actúa mediante el factor situado más a la derecha: 𝐸0 (𝐸1 𝐵) = 𝐴.

Ingeniería Informática · UFV  20
```

#### Página 21

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.9  Producto de matrices elementales
2024/25 · Ordinaria · Modelo C · Pregunta original 3

Dadas
⎛ 1 2 −1⎞  ⎛ 1 2 −1⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟,
𝐴=⎜
⎜0 1 2⎟ ⎟  𝐵=⎜
⎜1 5 −1⎟⎟
⎝−1 1 1 ⎠  ⎝0 1 2 ⎠
encuentra dos matrices elementales 𝐸0 , 𝐸1 tales que 𝐸0 𝐸1 𝐵 = 𝐴.
Respuesta
Se pasa de 𝐵 a 𝐴 mediante 𝐹2 ↔ 𝐹3 y después 𝐹3 ← 𝐹3 − 2𝐹1 . Las matrices correspondientes son

⎛ 1 0 0⎞  ⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟.
𝐸1 = ⎜
⎜0 0 1 ⎟
⎟  𝐸0 = ⎜
⎜ 0 1 0⎟
⎟
⎝0 1 0 ⎠  ⎝−2 0 1⎠

La primera operación actúa mediante el factor situado más a la derecha: 𝐸0 (𝐸1 𝐵) = 𝐴.

2.10  Matrices que conmutan con una matriz dada
2025/26 · Ordinaria · Modelo A · Pregunta original 5

Halla todas las matrices reales que conmutan con

2 1
𝐴=(  ).
−1 2

Respuesta
𝑎 𝑏
Escribimos 𝐵 = (  ) e igualamos las entradas de 𝐴𝐵 y 𝐵𝐴. Las condiciones resultantes son 𝑑 = 𝑎
𝑐 𝑑
y 𝑏 = −𝑐. Por tanto, todas las soluciones son

𝑎 −𝑐
𝐵=(  ),  𝑎, 𝑐 ∈ ℝ.
𝑐 𝑎

Estas condiciones también son suficientes al sustituirlas en ambos productos.

Ingeniería Informática · UFV  21
```

#### Página 22

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.11  Matrices que conmutan con una matriz dada
2025/26 · Ordinaria · Modelo B · Pregunta original 5

Halla todas las matrices reales que conmutan con

0 −1
𝐴=(  ).
1 0

Respuesta
𝑎 𝑏
Escribimos 𝐵 = (  ) e igualamos las entradas de 𝐴𝐵 y 𝐵𝐴. Las condiciones resultantes son 𝑑 = 𝑎
𝑐 𝑑
y 𝑏 = −𝑐. Por tanto, todas las soluciones son

𝑎 −𝑐
𝐵=(  ),  𝑎, 𝑐 ∈ ℝ.
𝑐 𝑎

Estas condiciones también son suficientes al sustituirlas en ambos productos.

2.12  Matrices que conmutan con una matriz dada
2025/26 · Ordinaria · Modelo C · Pregunta original 5

Halla todas las matrices reales que conmutan con

1 −2
𝐴=(  ).
2 1

Respuesta
𝑎 𝑏
Escribimos 𝐵 = (  ) e igualamos las entradas de 𝐴𝐵 y 𝐵𝐴. Las condiciones resultantes son 𝑑 = 𝑎
𝑐 𝑑
y 𝑏 = −𝑐. Por tanto, todas las soluciones son

𝑎 −𝑐
𝐵=(  ),  𝑎, 𝑐 ∈ ℝ.
𝑐 𝑎

Estas condiciones también son suficientes al sustituirlas en ambos productos.

Ingeniería Informática · UFV  22
```

#### Página 23

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

2.13  Verdadero o falso: repaso del tema
2024/25 · Ordinaria · Pregunta original 10 · Modelos A, B y C

Indica si cada afirmación es verdadera (V) o falsa (F). Las etiquetas A.n, B.n y C.n indican el modelo
y el apartado original.

A.3 Sean 𝐴, 𝐵 dos matrices. La igualdad 𝐴𝐵 = 0 implica 𝐴 = 0 o 𝐵 = 0.
A.4 Todas las matrices elementales son invertibles y su inversa es otra matriz elemental.
B.3 Una matriz cuadrada 𝐴 es no singular si y solo si se puede escribir como producto de matrices
elementales.
B.4 Si 𝐴 es no singular y tiene factorización 𝐿𝑈, entonces 𝐿 y 𝑈 son únicas.
C.3 El producto de matrices es conmutativo.
C.4 La suma de matrices es conmutativa.

Respuesta

A.3 F. Por ejemplo, 𝐴 = diag(1, 0) y 𝐵 = diag(0, 1) son no nulas y 𝐴𝐵 = 0.
A.4 V. Cada operación elemental se deshace mediante otra operación elemental.
B.3 V. Gauss–Jordan reduce una matriz invertible a 𝐼, y cada operación se representa por una
matriz elemental invertible.
B.4 V con la convención del curso: 𝐿 triangular inferior con diagonal unitaria y 𝑈 triangular
superior. Sin normalizar la diagonal de 𝐿, la afirmación no sería cierta.
C.3 F. En general, 𝐴𝐵 ≠ 𝐵𝐴.
C.4 V. Para matrices del mismo tamaño, la suma se realiza entrada a entrada.

Ingeniería Informática · UFV  23
```

#### Página 24

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 3

Determinantes
Localización de las cuestiones de determinantes dentro de preguntas mixtas.

En el conjunto de exámenes analizados no hay ninguna pregunta completa dedicada exclusivamente
a determinantes que pueda situarse aquí sin introducir contenidos de temas posteriores.
Ninguna de las 30 afirmaciones de verdadero/falso corresponde exclusivamente a este tema. Los
determinantes aparecen en preguntas que también requieren espacios vectoriales, transformaciones
o autovalores. Para respetar el orden de los temas y conservar unidos los apartados, esas preguntas
se incluyen más adelante.

Dónde encontrar estas cuestiones

Determinante a partir de una factorización LU; modelo A de 2024/25: pregunta 4.31, página 35.

Determinante a partir de una factorización LU; modelo B de 2024/25: pregunta 4.32, página 36.

Determinante a partir de una factorización LU; modelo C de 2024/25: pregunta 4.33, página 36.

Determinante y filas nulas; extraordinaria A de 2025/26: pregunta 4.16, página 29.

Determinante y pivotes; extraordinaria B de 2025/26: pregunta 4.17, página 29.

Determinante y filas nulas; extraordinaria C de 2025/26: pregunta 4.18, página 29.

El polinomio característico y las relaciones entre determinante y autovalores se trabajan en el tema
6.

Ingeniería Informática · UFV  24
```

#### Página 25

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 4

Espacios vectoriales
Subespacios, bases, dimensión, rango, núcleo y espacios asociados a matrices.

4.1  Una recta como subespacio generado
2024/25 · Ordinaria · Modelo A · Pregunta original 6

Sea 𝐻 = {𝑡(1, 3, 2) ∶ 𝑡 ∈ ℝ}. a) Encuentra un vector 𝑣 ∈ ℝ3 tal que 𝐻 = Gen{𝑣}. b) ¿La existencia de
ese vector demuestra que 𝐻 es un subespacio de ℝ3 ?
Respuesta
Sirve 𝑣 = (1, 3, 2). Por definición, 𝐻 = Gen{𝑣}, y todo conjunto generado es un subespacio. En efecto,
contiene 0 y, si 𝑠𝑣, 𝑡𝑣 ∈ 𝐻, entonces 𝑠𝑣 + 𝑡𝑣 = (𝑠 + 𝑡)𝑣 ∈ 𝐻 y 𝛼(𝑠𝑣) = (𝛼𝑠)𝑣 ∈ 𝐻.

4.2  Una recta como subespacio generado
2024/25 · Ordinaria · Modelo B · Pregunta original 6

Sea 𝐻 = {𝑡(−1, 2, −3) ∶ 𝑡 ∈ ℝ}. a) Encuentra un vector 𝑣 ∈ ℝ3 tal que 𝐻 = Gen{𝑣}. b) ¿La existencia
de ese vector demuestra que 𝐻 es un subespacio de ℝ3 ?
Respuesta
Sirve 𝑣 = (−1, 2, −3). Por definición, 𝐻 = Gen{𝑣}, y todo conjunto generado es un subespacio. En
efecto, contiene 0 y, si 𝑠𝑣, 𝑡𝑣 ∈ 𝐻, entonces 𝑠𝑣 + 𝑡𝑣 = (𝑠 + 𝑡)𝑣 ∈ 𝐻 y 𝛼(𝑠𝑣) = (𝛼𝑠)𝑣 ∈ 𝐻.

4.3  Una recta como subespacio generado
2024/25 · Ordinaria · Modelo C · Pregunta original 6

Sea 𝐻 = {𝑡(2, −1, 1) ∶ 𝑡 ∈ ℝ}. a) Encuentra un vector 𝑣 ∈ ℝ3 tal que 𝐻 = Gen{𝑣}. b) ¿La existencia
de ese vector demuestra que 𝐻 es un subespacio de ℝ3 ?
Respuesta
Sirve 𝑣 = (2, −1, 1). Por definición, 𝐻 = Gen{𝑣}, y todo conjunto generado es un subespacio. En
efecto, contiene 0 y, si 𝑠𝑣, 𝑡𝑣 ∈ 𝐻, entonces 𝑠𝑣 + 𝑡𝑣 = (𝑠 + 𝑡)𝑣 ∈ 𝐻 y 𝛼(𝑠𝑣) = (𝛼𝑠)𝑣 ∈ 𝐻.

4.4  Contener al cero no basta para ser subespacio
2025/26 · Extraordinaria · Modelo A · Pregunta original 7

Sea
𝐻 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥𝑦 = 0}.
a) Justifica si (0, 0, 0) pertenece a 𝐻. b) ¿Es un subespacio? Da un contraejemplo y explica si es com-
patible con tu respuesta anterior.
Respuesta
El vector nulo pertenece a 𝐻, porque satisface su condición. Sin embargo, 𝑢 = (1, 0, 0) y 𝑣 = (0, 1, 0)
pertenecen a 𝐻, mientras que 𝑢 + 𝑣 = (1, 1, 0) no: 𝑥𝑦 = 1 ≠ 0. No es cerrado para la suma y no es un
subespacio. No hay contradicción: contener al cero es una condición necesaria, pero no suficiente.

Ingeniería Informática · UFV  25
```

#### Página 26

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.5  Contener al cero no basta para ser subespacio
2025/26 · Extraordinaria · Modelo B · Pregunta original 7

Sea
𝐻 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 2𝑥𝑦 = 0}.
a) Justifica si (0, 0, 0) pertenece a 𝐻. b) ¿Es un subespacio? Da un contraejemplo y explica si es com-
patible con tu respuesta anterior.
Respuesta
El vector nulo pertenece a 𝐻, porque satisface su condición. Sin embargo, 𝑢 = (1, 0, 0) y 𝑣 = (0, 1, 0)
pertenecen a 𝐻, mientras que 𝑢 + 𝑣 = (1, 1, 0) no: 2𝑥𝑦 = 2 ≠ 0. No es cerrado para la suma y no es un
subespacio. No hay contradicción: contener al cero es una condición necesaria, pero no suficiente.

4.6  Contener al cero no basta para ser subespacio
2025/26 · Extraordinaria · Modelo C · Pregunta original 7

Sea
𝐻 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥2 + 𝑦2 ≤ 1}.
a) Justifica si (0, 0, 0) pertenece a 𝐻. b) ¿Es un subespacio? Da un contraejemplo y explica si es com-
patible con tu respuesta anterior.
Respuesta
El vector nulo pertenece a 𝐻, porque satisface su condición. Sin embargo, 𝑢 = (1, 0, 0) y 𝑣 = (0, 1, 0)
pertenecen a 𝐻, mientras que 𝑢 + 𝑣 = (1, 1, 0) no: 𝑥2 + 𝑦2 = 2 > 1. No es cerrado para la suma y no es
un subespacio. No hay contradicción: contener al cero es una condición necesaria, pero no suficiente.

4.7  Rango, inversa y unicidad de solución
2025/26 · Ordinaria · Modelo A · Pregunta original 1

Sea 𝐴 una matriz de orden 4 que, al aplicar Gauss, da una matriz escalonada con 3 filas no nulas. a)
Determina su rango. b) Decide si es invertible. c) Razona si existe algún 𝑏 para el que 𝐴𝑥 = 𝑏 tenga
solución única.
Respuesta
Hay 3 pivotes, de modo que rg 𝐴 = 3 < 4 y 𝐴 no es invertible. Ningún 𝑏 produce una solución única:
si el sistema es compatible, queda una variable libre y hay infinitas soluciones; en caso contrario, no
hay ninguna.

4.8  Rango, inversa y unicidad de solución
2025/26 · Ordinaria · Modelo B · Pregunta original 1

Sea 𝐴 una matriz de orden 5 que, al aplicar Gauss, da una matriz escalonada con 4 filas no nulas. a)
Determina su rango. b) Decide si es invertible. c) Razona si existe algún 𝑏 para el que 𝐴𝑥 = 𝑏 tenga
solución única.
Respuesta
Hay 4 pivotes, de modo que rg 𝐴 = 4 < 5 y 𝐴 no es invertible. Ningún 𝑏 produce una solución única:
si el sistema es compatible, queda una variable libre y hay infinitas soluciones; en caso contrario, no
hay ninguna.

Ingeniería Informática · UFV  26
```

#### Página 27

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.9  Rango, inversa y unicidad de solución
2025/26 · Ordinaria · Modelo C · Pregunta original 1

Sea 𝐴 una matriz de orden 3 que, al aplicar Gauss, da una matriz escalonada con 2 filas no nulas. a)
Determina su rango. b) Decide si es invertible. c) Razona si existe algún 𝑏 para el que 𝐴𝑥 = 𝑏 tenga
solución única.
Respuesta
Hay 2 pivotes, de modo que rg 𝐴 = 2 < 3 y 𝐴 no es invertible. Ningún 𝑏 produce una solución única:
si el sistema es compatible, queda una variable libre y hay infinitas soluciones; en caso contrario, no
hay ninguna.

4.10  Subespacio definido por ecuaciones homogéneas
2025/26 · Ordinaria · Modelo A · Pregunta original 4

Sea
𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 + 2𝑦 + 𝑧 = 0}.
a) Justifica que 𝑊 es un subespacio de ℝ3 . b) Determina su dimensión.
Respuesta
Contiene al vector nulo, y la suma y el producto por escalares conservan las ecuaciones homogéneas.
Por ello, es un subespacio. Al resolver las ecuaciones se obtiene una base {(−2, 1, 0), (−1, 0, 1)}; por
tanto, dim 𝑊 = 2.

4.11  Subespacio definido por ecuaciones homogéneas
2025/26 · Ordinaria · Modelo B · Pregunta original 4

Sea
𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 2𝑥 − 𝑦 + 𝑧 = 0}.
a) Justifica que 𝑊 es un subespacio de ℝ3 . b) Determina su dimensión.
Respuesta
Contiene al vector nulo, y la suma y el producto por escalares conservan las ecuaciones homogéneas.
Por ello, es un subespacio. Al resolver las ecuaciones se obtiene una base {(1, 2, 0), (0, 1, 1)}; por tanto,
dim 𝑊 = 2.

4.12  Subespacio definido por ecuaciones homogéneas
2025/26 · Ordinaria · Modelo C · Pregunta original 4

Sea
𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 − 2𝑦 + 3𝑧 = 0,  2𝑥 − 𝑦 + 𝑧 = 0}.
a) Justifica que 𝑊 es un subespacio de ℝ3 . b) Determina su dimensión.
Respuesta
Contiene al vector nulo, y la suma y el producto por escalares conservan las ecuaciones homogé-
neas. Por ello, es un subespacio. Al resolver las ecuaciones se obtiene una base {(1, 5, 3)}; por tanto,
dim 𝑊 = 1.

Ingeniería Informática · UFV  27
```

#### Página 28

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.13  Dimensión y parámetros en un subespacio
2023/24 · Ordinaria · Modelo A · Pregunta original 1

Sea 𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑎𝑥 + 𝑏𝑦 + 𝑧 = 0, 𝑥 + 𝑦 + 𝑧 = 0}. Determina razonadamente para qué valores
de 𝑎, 𝑏 la dimensión de 𝑊 es 2.
Respuesta
Las ecuaciones son proporcionales únicamente cuando 𝑎 = 𝑏 = 1, porque ambas tienen coeficiente
1 en 𝑧. Así,
⎧
{2, (𝑎, 𝑏) = (1, 1),
dim 𝑊 = ⎨
{
⎩1, (𝑎, 𝑏) ≠ (1, 1).
La respuesta es 𝑎 = 𝑏 = 1.

4.14  Dimensión y parámetros en un subespacio
2023/24 · Ordinaria · Modelo B · Pregunta original 1

Sea 𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑎𝑥 + 𝑏𝑦 + 𝑧 = 0, 𝑥 + 𝑦 + 𝑧 = 0}. Determina razonadamente para qué valores
de 𝑎, 𝑏 la dimensión de 𝑊 no es 2.
Respuesta
Las ecuaciones son proporcionales únicamente cuando 𝑎 = 𝑏 = 1, porque ambas tienen coeficiente
1 en 𝑧. Así,
⎧
{2, (𝑎, 𝑏) = (1, 1),
dim 𝑊 = ⎨
{
⎩1, (𝑎, 𝑏) ≠ (1, 1).
La respuesta es (𝑎, 𝑏) ≠ (1, 1).

4.15  Dimensión y parámetros en un subespacio
2023/24 · Ordinaria · Modelo C · Pregunta original 1

Sea 𝑊 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 2𝑥 −𝑦 = 𝑎, 𝑥 +𝑦 −𝑧 = 0}. Determina para qué valores de 𝑎 es un subespacio
vectorial y calcula su dimensión en esos casos.
Respuesta
Para contener al vector nulo debe ser 𝑎 = 0. Con ese valor las ecuaciones son homogéneas, por lo que
sí definen un subespacio. Se obtiene 𝑦 = 2𝑥, 𝑧 = 3𝑥, de modo que 𝑊 = Gen{(1, 2, 3)} y dim 𝑊 = 1.

Ingeniería Informática · UFV  28
```

#### Página 29

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.16  Consecuencias de la forma escalonada
2025/26 · Extraordinaria · Modelo A · Pregunta original 2

Sea 𝐴 cuadrada de orden 𝑛. Al reducirla por Gauss se obtiene una forma escalonada 𝑈 con exacta-
mente una fila nula.
a) ¿Qué puedes concluir sobre det 𝐴?
b) ¿Es 𝐴 invertible? ¿Por qué?
c) Indica el número de pivotes, el rango y la dependencia de filas y columnas. Explica las conse-
cuencias para la compatibilidad y el número de soluciones de 𝐴𝑥 = 𝑏 sin calcular determinantes.

Respuesta
Hay 𝑛 − 1 pivotes, de modo que rg 𝐴 = rg 𝑈 = 𝑛 − 1 < 𝑛. Las familias de todas las filas y de todas
las columnas son dependientes, y el máximo número de vectores independientes en cada una es
𝑛 − 1. La matriz es singular: det 𝐴 = 0 y no tiene inversa. El sistema nunca tiene solución única: es
incompatible si 𝑏 ∉ Col(𝐴) y compatible indeterminado si 𝑏 ∈ Col(𝐴); en este último caso hay 1
variables libres.

4.17  Consecuencias de la forma escalonada
2025/26 · Extraordinaria · Modelo B · Pregunta original 2

Sea 𝐴 cuadrada de orden 𝑛. Al reducirla por Gauss se obtiene una forma escalonada 𝑈 cuya última
fila no es nula.
a) ¿Qué puedes concluir sobre det 𝐴?
b) ¿Es 𝐴 invertible? ¿Por qué?
c) Indica el número de pivotes, el rango y la dependencia de filas y columnas. Explica las conse-
cuencias para la compatibilidad y el número de soluciones de 𝐴𝑥 = 𝑏 sin calcular determinantes.

Respuesta
Al no ser nula la última fila de una matriz escalonada, ninguna fila es nula. Hay 𝑛 pivotes, rg 𝐴 =
rg 𝑈 = 𝑛, y las filas y las columnas son linealmente independientes. Por tanto, det 𝐴 ≠ 0 y 𝐴 es
invertible. Para todo 𝑏 ∈ ℝ𝑛 , 𝐴𝑥 = 𝑏 es compatible determinado. La existencia de un pivote en cada
fila y columna permite esta última conclusión sin calcular determinantes.

4.18  Consecuencias de la forma escalonada
2025/26 · Extraordinaria · Modelo C · Pregunta original 2

Sea 𝐴 cuadrada de orden 𝑛 > 2. Al reducirla por Gauss se obtiene una forma escalonada 𝑈 con las
dos últimas filas nulas y las demás no nulas.
a) ¿Qué puedes concluir sobre det 𝐴?
b) ¿Es 𝐴 invertible? ¿Por qué?
c) Indica el número de pivotes, el rango y la dependencia de filas y columnas. Explica las conse-
cuencias para la compatibilidad y el número de soluciones de 𝐴𝑥 = 𝑏 sin calcular determinantes.

Respuesta
Hay 𝑛 − 2 pivotes, de modo que rg 𝐴 = rg 𝑈 = 𝑛 − 2 < 𝑛. Las familias de todas las filas y de todas
las columnas son dependientes, y el máximo número de vectores independientes en cada una es
𝑛 − 2. La matriz es singular: det 𝐴 = 0 y no tiene inversa. El sistema nunca tiene solución única: es
incompatible si 𝑏 ∉ Col(𝐴) y compatible indeterminado si 𝑏 ∈ Col(𝐴); en este último caso hay 2
variables libres.

Ingeniería Informática · UFV  29
```

#### Página 30

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.19  Pertenencia al núcleo y al espacio columna
2024/25 · Ordinaria · Modelo A · Pregunta original 5

Determina razonadamente si 𝑢 pertenece al núcleo de 𝐴, al espacio columna, a ambos o a ninguno:

⎛ 1 −1 5 ⎞  ⎛ −7
⎜  ⎟  ⎜ ⎞  ⎟
𝐴=⎜
⎜2
⎜  0 7⎟⎟,
⎟  𝑢=⎜
⎜3⎟
⎜  ⎟.
⎟
⎝−3 −5 −3⎠  ⎝2⎠

Respuesta
El producto directo da 𝐴𝑢 = 0, por lo que 𝑢 ∈ ker 𝐴. Para estudiar 𝐴𝑥 = 𝑢, se aplican 𝐹2 ← 𝐹2 − 2𝐹1 ,
𝐹3 ← 𝐹3 + 3𝐹1 y 𝐹3 ← 𝐹3 + 4𝐹2 . Aparece [0 0 0 ∣ 49]: 𝑢 ∉ Col(𝐴). Pertenece únicamente al núcleo.

4.20  Pertenencia al núcleo y al espacio columna
2024/25 · Ordinaria · Modelo B · Pregunta original 5

Determina razonadamente si 𝑢 pertenece al núcleo de 𝐴, al espacio columna, a ambos o a ninguno:

⎛ 1 2 3⎞  ⎛ −1⎞
⎜
⎜  ⎟
⎟,  ⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜2 4 6 ⎟
⎟  𝑢=⎜
⎜−1⎟⎟
⎝1 1 2 ⎠  ⎝1⎠

Respuesta
El producto directo da 𝐴𝑢 = 0, por lo que 𝑢 ∈ ker 𝐴. En [𝐴 ∣ 𝑢], la operación 𝐹2 ← 𝐹2 − 2𝐹1 produce
[0 0 0 ∣ 1]. Por tanto, 𝑢 ∉ Col(𝐴). Pertenece únicamente al núcleo.

4.21  Pertenencia al núcleo y al espacio columna
2024/25 · Ordinaria · Modelo C · Pregunta original 5

Determina razonadamente si 𝑢 pertenece al núcleo de 𝐴, al espacio columna, a ambos o a ninguno:

⎛ 1 −2 1⎞  ⎛ 1
⎜  ⎟  ⎜ ⎞ ⎟
𝐴=⎜
⎜2 −4 2⎟
⎜  ⎟
⎟,  𝑢=⎜
⎜ 2⎟
⎜  ⎟.
⎟
⎝3 −6 3⎠  3
⎝ ⎠

Respuesta
El producto directo da 𝐴𝑢 = 0, por lo que 𝑢 ∈ ker 𝐴. El vector 𝑢 es la primera columna de 𝐴, de
modo que 𝐴𝑒1 = 𝑢 y 𝑢 ∈ Col(𝐴). Pertenece a ambos espacios.

Ingeniería Informática · UFV  30
```

#### Página 31

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.22  Pertenencia al espacio columna y coordenadas
2022/23 · Ordinaria · Modelo B · Pregunta original 3

Considera la matriz de coeficientes
⎛ 1 1 2⎞
⎜
⎜  ⎟
⎟.
𝐶=⎜
⎜1 2 1 ⎟
⎟
⎝2 1 1 ⎠
Determina si 𝑢 = (1, 1, 1) pertenece al espacio columna de 𝐶. Si pertenece, calcula sus coordenadas
en una base de dicho espacio.
Respuesta
Las tres columnas forman una base 𝐵 de ℝ3 . Como su suma es (4, 4, 4), se tiene 𝑢 = 41 𝑐1 + 14 𝑐2 + 14 𝑐3 .
Por tanto, 𝑢 ∈ Col(𝐶) y [𝑢]𝐵 = ( 41 , 14 , 14 ).

4.23  Pertenencia al espacio columna y coordenadas
2022/23 · Ordinaria · Modelo C · Pregunta original 3

Considera la matriz de coeficientes

⎛ 1 2  4⎞
⎜
⎜  ⎟
𝐶=⎜
⎜2  4  2⎟⎟.
⎟
⎝−1 −2 −4⎠

Determina si 𝑢 = (1, 1, 1) pertenece al espacio columna de 𝐶. Si pertenece, calcula sus coordenadas
en una base de dicho espacio.
Respuesta
Al resolver 𝐶𝑥 = 𝑢, la operación 𝐹3 ← 𝐹3 + 𝐹1 sobre la ampliada produce [0 0 0 ∣ 2]. El sistema es
incompatible: 𝑢 ∉ Col(𝐶) y no tiene coordenadas en una base de ese espacio.

4.24  Pertenencia al espacio columna y coordenadas
2022/23 · Ordinaria · Modelo D · Pregunta original 3

Considera la matriz de coeficientes
⎛ 1 1 −1⎞
⎜  ⎟
𝐶=⎜
⎜2 3 2 ⎟
⎜  ⎟.
⎟
⎝1 2 3 ⎠
Determina si 𝑢 = (1, 1, 1) pertenece al espacio columna de 𝐶. Si pertenece, calcula sus coordenadas
en una base de dicho espacio.
Respuesta
Para resolver 𝐶𝑥 = 𝑢, se aplican 𝐹2 ← 𝐹2 − 2𝐹1 , 𝐹3 ← 𝐹3 − 𝐹1 y 𝐹3 ← 𝐹3 − 𝐹2 . La última fila es
[0 0 0 ∣ 1]. Por tanto, 𝑢 ∉ Col(𝐶) y no tiene coordenadas en una base de ese espacio.

Ingeniería Informática · UFV  31
```

#### Página 32

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.25  Rango y núcleo a partir de una factorización LU
2023/24 · Ordinaria · Modelo A · Pregunta original 4

Una matriz 𝐴 admite la factorización

⎛ 1  0  0  0 ⎞ ⎛2 1 3 ⎞
⎜
⎜ 2  1  0  0⎟⎟ ⎜
⎜ 0 −2 3⎟⎟
𝐴=⎜
⎜
⎜
⎟
⎟
⎟
⎜
⎜
⎜
⎟
⎟
⎟ .
⎜
⎜ −3  2  1  0⎟⎟⎜⎜ 0  0 4 ⎟
⎟
⎝1  2  3  1 ⎠ ⎝0 0 0 ⎠

Determina razonadamente: a) su tamaño y rango; b) una base y la dimensión de su núcleo.
Respuesta
La matriz 𝐿 es invertible; por ello, 𝐴 y 𝑈 son equivalentes por filas y ker 𝐴 = ker 𝑈. El tamaño es 4 × 3
y el rango es 3, por los 3 pivotes de 𝑈. ker 𝐴 = {0}: su base es el conjunto vacío ∅ y su dimensión es
0.

4.26  Rango y núcleo a partir de una factorización LU
2023/24 · Ordinaria · Modelo B · Pregunta original 4

Una matriz 𝐴 admite la factorización

⎛ 1 0 0 ⎞ ⎛1 1 3 ⎞
⎜
⎜  ⎟
⎟⎜⎜0 −2 4⎟
⎟
𝐴=⎜
⎜ 2 1 0⎟⎟⎜⎜  ⎟.
⎟
⎝−3 2 1⎠ ⎝0 0 0⎠

Determina razonadamente: a) su tamaño y rango; b) una base y la dimensión de su núcleo.
Respuesta
La matriz 𝐿 es invertible; por ello, 𝐴 y 𝑈 son equivalentes por filas y ker 𝐴 = ker 𝑈. El tamaño es
3 × 3 y el rango es 2, por los 2 pivotes de 𝑈. 𝑈𝑥 = 0 equivale a 𝑥2 = 2𝑥3 , 𝑥1 = −5𝑥3 . Así, ker 𝐴 =
Gen{(−5, 2, 1)}, de dimensión 1.

4.27  Rango y núcleo a partir de una factorización LU
2023/24 · Ordinaria · Modelo C · Pregunta original 4

Una matriz 𝐴 admite la factorización

⎛ 1 0 0 ⎞ ⎛1 1 3 3 ⎞
⎜
⎜  ⎟
⎟⎜⎜0 −2 4 2⎟⎟
𝐴=⎜
⎜ 2 1 0⎟ ⎟⎜⎜  ⎟.
⎟
⎝ −3 2 1 ⎠⎝  0 0 0 1 ⎠

Determina razonadamente: a) su tamaño y rango; b) una base y la dimensión de su núcleo.
Respuesta
La matriz 𝐿 es invertible; por ello, 𝐴 y 𝑈 son equivalentes por filas y ker 𝐴 = ker 𝑈. El tamaño
es 3 × 4 y el rango es 3, por los 3 pivotes de 𝑈. 𝑈𝑥 = 0 da 𝑥4 = 0, 𝑥2 = 2𝑥3 , 𝑥1 = −5𝑥3 . Así,
ker 𝐴 = Gen{(−5, 2, 1, 0)}, de dimensión 1.

Ingeniería Informática · UFV  32
```

#### Página 33

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.28  Base, coordenadas y dependencia sin determinantes
2025/26 · Extraordinaria · Modelo A · Pregunta original 4

Sea el conjunto ordenado 𝐵 = {𝑣1 , 𝑣2 , 𝑣3 }, donde

𝑣1 = (1, 1, 0),  𝑣2 = (1, 1, 2),  𝑣3 = (1, 2, 3).

a) Determina si es una base de ℝ3 , justificando las operaciones y sin determinantes. b) En caso
afirmativo, calcula las coordenadas de 𝑢 = (0, 1, 7); en caso contrario, encuentra una relación de
dependencia entre los vectores.
Respuesta
Colocamos los vectores como columnas:

⎛ 1 1 1⎞
⎜
⎜  ⎟
⎟.
𝐶=⎜
⎜1 1 2 ⎟
⎟
⎝0 2 3 ⎠

Las operaciones 𝐹2 ← 𝐹2 − 𝐹1 , 𝐹2 ↔ 𝐹3 y 𝐹2 ← 𝐹2 /2 dan

⎛ 1 1 1⎞
⎜
⎜  3⎟
⎟.
⎜0 1 2 ⎟
⎜  ⎟
⎝0 0 1 ⎠

Hay tres pivotes: los vectores son independientes y forman una base de ℝ3 . Para 𝐶(𝛼, 𝛽, 𝛾)T = 𝑢, las
mismas operaciones dan, antes de normalizar,

𝛾 = 1,  2𝛽 + 3𝛾 = 7,  𝛼 + 𝛽 + 𝛾 = 0.

[𝑢]𝐵 = (−3, 2, 1).

Ingeniería Informática · UFV  33
```

#### Página 34

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.29  Base, coordenadas y dependencia sin determinantes
2025/26 · Extraordinaria · Modelo B · Pregunta original 4

Sea el conjunto ordenado 𝐵 = {𝑣1 , 𝑣2 , 𝑣3 }, donde

𝑣1 = (−1, 2, 1),  𝑣2 = (0, 1, −3),  𝑣3 = (1, 2, 3).

a) Determina si es una base de ℝ3 , justificando las operaciones y sin determinantes. b) En caso
afirmativo, calcula las coordenadas de 𝑢 = (2, 10, 4); en caso contrario, encuentra una relación de
dependencia entre los vectores.
Respuesta
Colocamos los vectores como columnas:

⎛ −1 0 1⎞
⎜
⎜  ⎟
𝐶=⎜
⎜2  1 2⎟⎟.
⎟
⎝ 1  −3 3 ⎠

Las operaciones 𝐹2 ← 𝐹2 + 2𝐹1 , 𝐹3 ← 𝐹3 + 𝐹1 , 𝐹3 ← 𝐹3 + 3𝐹2 , 𝐹1 ← −𝐹1 y 𝐹3 ← 𝐹3 /16 dan

⎛ 1 0 −1⎞
⎜
⎜  ⎟
⎟.
⎜0 1 4 ⎟
⎜  ⎟
⎝0 0 1 ⎠

Hay tres pivotes: los vectores son independientes y forman una base de ℝ3 . Para 𝐶(𝛼, 𝛽, 𝛾)T = 𝑢, las
mismas operaciones dan, antes de normalizar,

16𝛾 = 48,  𝛽 + 4𝛾 = 14,  −𝛼 + 𝛾 = 2.

[𝑢]𝐵 = (1, 2, 3).

Ingeniería Informática · UFV  34
```

#### Página 35

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.30  Base, coordenadas y dependencia sin determinantes
2025/26 · Extraordinaria · Modelo C · Pregunta original 4

Sea el conjunto ordenado 𝐵 = {𝑣1 , 𝑣2 , 𝑣3 }, donde

𝑣1 = (3, 2, 1),  𝑣2 = (0, 1, −1),  𝑣3 = (1, −2, 3).

a) Determina si es una base de ℝ3 , justificando las operaciones y sin determinantes. b) En caso
afirmativo, calcula las coordenadas de 𝑢 = (2, 10, 4); en caso contrario, encuentra una relación de
dependencia entre los vectores.
Respuesta
Colocamos los vectores como columnas:

⎛ 3 0 1⎞
⎜
⎜  ⎟
⎟.
𝐶=⎜
⎜2 1 −2⎟⎟
⎝1 −1 3 ⎠

Las operaciones 𝐹1 ↔ 𝐹3 , 𝐹2 ← 𝐹2 − 2𝐹1 , 𝐹3 ← 𝐹3 − 3𝐹1 , 𝐹3 ← 𝐹3 − 𝐹2 y 𝐹2 ← 𝐹2 /3 dan

⎛ 1 −1 3 ⎞
⎜
⎜  8⎟
⎟.
⎜0 1 − 3 ⎟
⎜  ⎟
⎝0 0  0 ⎠

Hay dos pivotes, por lo que no forman una base. Una relación de dependencia es

1  8
𝑣1 − 8𝑣2 − 3𝑣3 = 0,  𝑣 3 = 𝑣1 − 𝑣2 .
3  3
Al no ser una base, no procede dar coordenadas de 𝑢 en 𝐵 como coordenadas respecto de una base.

4.31  Espacio fila, determinante y clasificación del sistema
2024/25 · Ordinaria · Modelo A · Pregunta original 2

La matriz de coeficientes 𝐴 de un sistema lineal admite la factorización

⎛ 1  0  0  0⎞ ⎛−1 2 3 4⎞
⎜
⎜ 2  1  0  0⎟
⎟ ⎜
⎜ 0 −2 2 3⎟⎟
𝐴=⎜
⎜
⎜
⎟
⎟
⎟
⎜
⎜
⎜
⎟
⎟
⎟ .
⎜
⎜3  4  1  0⎟
⎟⎜⎜ 0  0 1 2 ⎟
⎟
⎝1  2  3  1⎠ ⎝ 0  0 0 3⎠

a) Determina una base y la dimensión del espacio de filas de 𝐴.
b) Determina el rango de 𝐴.
c) Calcula el determinante de 𝐴.
d) Clasifica el sistema 𝐴𝑥 = 𝑏, con 𝑏 ∈ ℝ4 .
No multipliques las matrices.
Respuesta
Como 𝐿 es invertible, Fila(𝐴) = Fila(𝑈). Una base es {(−1, 2, 3, 4), (0, −2, 2, 3), (0, 0, 1, 2), (0, 0, 0, 3)},
de dimensión 4; por tanto, rg 𝐴 = 4. Además, det 𝐿 = 1 y det 𝐴 = det 𝑈 = 6.
Como 𝐴 es invertible, el sistema 𝐴𝑥 = 𝑏 es compatible determinado para todo 𝑏 ∈ ℝ4 .

Ingeniería Informática · UFV  35
```

#### Página 36

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.32  Espacio fila, determinante y clasificación del sistema
2024/25 · Ordinaria · Modelo B · Pregunta original 2

La matriz de coeficientes 𝐴 de un sistema lineal admite la factorización

⎛ 1  0  0  0 ⎞ ⎛1  2  3  4⎞
⎜
⎜ 2  1  0  0⎟⎟ ⎜
⎜ 0  0  1  2⎟
⎟
𝐴=⎜
⎜
⎜
⎟
⎟
⎟
⎜
⎜
⎜
⎟
⎟.
⎜
⎜3  1  1  0⎟  ⎜
⎟ ⎜0  0  0  0⎟
⎟
⎟
⎝3  1  0  1 ⎠ ⎝0  0  0  0⎠

a) Determina una base y la dimensión del espacio de filas de 𝐴.
b) Determina el rango de 𝐴.
c) Calcula el determinante de 𝐴.
d) Clasifica el sistema 𝐴𝑥 = 𝑏, con 𝑏 ∈ ℝ4 .
No multipliques las matrices.
Respuesta
Como 𝐿 es invertible, Fila(𝐴) = Fila(𝑈). Una base es {(1, 2, 3, 4), (0, 0, 1, 2)}, de dimensión 2; por
tanto, rg 𝐴 = 2. Además, det 𝐿 = 1 y det 𝐴 = det 𝑈 = 0.
El rango de 𝐴 es menor que el número de incógnitas, por lo que 𝐴𝑥 = 𝑏 no puede tener solución
única. Es compatible indeterminado si 𝑏 ∈ Col(𝐴) e incompatible si 𝑏 ∉ Col(𝐴).

4.33  Espacio fila, determinante y clasificación del sistema
2024/25 · Ordinaria · Modelo C · Pregunta original 2

La matriz de coeficientes 𝐴 de un sistema lineal admite la factorización

⎛ 1  0  0  0 ⎞ ⎛1  2  3  4⎞
⎜
⎜ 2  1  0  0⎟⎟ ⎜
⎜ 0  1  1  3⎟
⎟
𝐴=⎜
⎜
⎜
⎟
⎟
⎟
⎜
⎜
⎜
⎟
⎟.
⎜
⎜3  1  1  0⎟⎟⎜⎜0  0  1  0⎟
⎟
⎟
⎝3  1  0  1 ⎠ ⎝0  0  0  0⎠

a) Determina una base y la dimensión del espacio de filas de 𝐴.
b) Determina el rango de 𝐴.
c) Calcula el determinante de 𝐴.
d) Clasifica el sistema 𝐴𝑥 = 𝑏, con 𝑏 ∈ ℝ4 .
No multipliques las matrices.
Respuesta
Como 𝐿 es invertible, Fila(𝐴) = Fila(𝑈). Una base es {(1, 2, 3, 4), (0, 1, 1, 3), (0, 0, 1, 0)}, de dimensión
3; por tanto, rg 𝐴 = 3. Además, det 𝐿 = 1 y det 𝐴 = det 𝑈 = 0.
El rango de 𝐴 es menor que el número de incógnitas, por lo que 𝐴𝑥 = 𝑏 no puede tener solución
única. Es compatible indeterminado si 𝑏 ∈ Col(𝐴) e incompatible si 𝑏 ∉ Col(𝐴).

Ingeniería Informática · UFV  36
```

#### Página 37

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.34  Construcción de un sistema con nulidad fijada
2025/26 · Extraordinaria · Modelo A · Pregunta original 6

Sea 𝐴𝑥 = 0, con 𝐴 ∈ ℝ4×6 y rg 𝐴 = 3.
a) Indica el número de ecuaciones e incógnitas.
b) Describe algebraicamente el conjunto solución y determina su dimensión.
c) Construye una matriz con esas características que admita una solución no nula con exactamente
tres componentes nulas. Resuelve el sistema para demostrarlo.

Respuesta
Hay 4 ecuaciones y 6 incógnitas. El conjunto solución es ker 𝐴, un subespacio de ℝ6 de dimensión
6 − 3 = 3. Un ejemplo es
⎛ 1 0 0 0 0 0⎞
⎜
⎜ 0 1 0 0 0 0⎟  ⎟
𝐴=⎜ ⎜
⎜  ⎟
⎟ .
⎜ 0  0  1  0  0  0 ⎟
⎟
⎜  ⎟
⎝1 1 1 0 0 0 ⎠
Tiene rango 3. Sus soluciones son 𝑥 = (0, 0, 0, 𝛼, 𝛽, 𝛾), con los parámetros libres reales. Al elegirlos
iguales a 1 se obtiene 𝑥 = (0, 0, 0, 1, 1, 1), una solución no nula con exactamente tres componentes
nulas.

4.35  Construcción de un sistema con nulidad fijada
2025/26 · Extraordinaria · Modelo B · Pregunta original 6

Sea 𝐴𝑥 = 0, con 𝐴 ∈ ℝ5×7 y rg 𝐴 = 4.
a) Indica el número de ecuaciones e incógnitas.
b) Describe algebraicamente el conjunto solución y determina su dimensión.
c) Construye una matriz con esas características que admita una solución no nula con exactamente
tres componentes nulas. Resuelve el sistema para demostrarlo.

Respuesta
Hay 5 ecuaciones y 7 incógnitas. El conjunto solución es ker 𝐴, un subespacio de ℝ7 de dimensión
7 − 4 = 3. Un ejemplo es
⎛ 1 0 0 0 0 0 0⎞
⎜
⎜ 0 1 0 0 0 0 0⎟  ⎟
⎜
⎜  ⎟
⎟
𝐴=⎜ ⎜ 0  0  1  0  0  0  0 ⎟
⎟ .
⎜
⎜  ⎟
⎟
⎜
⎜  ⎟
⎜0 0 0 1 −1 0 0⎟  ⎟
⎝0 0 0 0 0 0 0 ⎠
Tiene rango 4. Sus soluciones son 𝑥 = (0, 0, 0, 𝛼, 𝛼, 𝛽, 𝛾), con los parámetros libres reales. Al elegirlos
iguales a 1 se obtiene 𝑥 = (0, 0, 0, 1, 1, 1, 1), una solución no nula con exactamente tres componentes
nulas.

Ingeniería Informática · UFV  37
```

#### Página 38

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.36  Construcción de un sistema con nulidad fijada
2025/26 · Extraordinaria · Modelo C · Pregunta original 6

Sea 𝐴𝑥 = 0, con 𝐴 ∈ ℝ6×5 y rg 𝐴 = 4.
a) Indica el número de ecuaciones e incógnitas.
b) Describe algebraicamente el conjunto solución y determina su dimensión.
c) Construye una matriz con esas características que admita una solución no nula con exactamente
tres componentes nulas. Resuelve el sistema para demostrarlo.

Respuesta
Hay 6 ecuaciones y 5 incógnitas. El conjunto solución es ker 𝐴, un subespacio de ℝ5 de dimensión
5 − 4 = 1. Un ejemplo es
⎛ 1 0 0 0 0⎞
⎜
⎜ 0 1 0 0 0⎟  ⎟
⎜
⎜  ⎟
⎟
⎜
⎜ 0  0  1  0  0 ⎟
⎟
𝐴=⎜ ⎜  ⎟
⎟ .
⎜
⎜ 0  0  0  1  −1 ⎟
⎟
⎜
⎜  ⎟
⎟
⎜
⎜  ⎟
⎜0 0 0 0 0 ⎟  ⎟
⎝0 0 0 0 0 ⎠
Tiene rango 4. Sus soluciones son 𝑥 = (0, 0, 0, 𝛼, 𝛼), con los parámetros libres reales. Al elegirlos
iguales a 1 se obtiene 𝑥 = (0, 0, 0, 1, 1), una solución no nula con exactamente tres componentes
nulas.

4.37  Espacio columna de una matriz con parámetro
2022/23 · Ordinaria · Modelo B · Pregunta original 2

Sea la matriz ampliada
⎛ 1 1 𝑎 1⎞
⎜
⎜  ⎟
⎟.
𝐴(𝑎) = ⎜
⎜1 𝑎 1 1 ⎟
⎟
⎝ 𝑎 1 1 1⎠
Determina para qué valores de 𝑎 el espacio columna de 𝐴(𝑎) tiene dimensión 1, 2, 3 o 4. En cada caso
posible, calcula una base.
Respuesta
La dimensión coincide con el número de columnas pivote. Se seleccionan las columnas corres-
pondientes de la matriz original, no de la matriz escalonada. Si 𝑎 = 1, la dimensión es 1 y una
base es {(1, 1, 1)}. Si 𝑎 ≠ 1, −2, la dimensión es 3 y sirven las tres primeras columnas. Si 𝑎 =
−2, la dimensión sigue siendo 3, pero hay que tomar las columnas primera, segunda y cuarta:
{(1, 1, −2), (1, −2, 1), (1, 1, 1)}. No hay valores que den dimensión 2 o 4.

Ingeniería Informática · UFV  38
```

#### Página 39

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.38  Espacio columna de una matriz con parámetro
2022/23 · Ordinaria · Modelo C · Pregunta original 2

Sea la matriz ampliada
⎛ 1 2 4 3⎞
⎜
⎜  ⎟
⎟.
𝐴(𝑎) = ⎜
⎜ 2 −𝑎 2 −2⎟
⎟
⎝−1 −2 𝑎 𝑎 ⎠
Determina para qué valores de 𝑎 el espacio columna de 𝐴(𝑎) tiene dimensión 1, 2, 3 o 4. En cada caso
posible, calcula una base.
Respuesta
La dimensión coincide con el número de columnas pivote. Se seleccionan las columnas corres-
pondientes de la matriz original, no de la matriz escalonada. La dimensión es siempre 3; no pue-
de ser 1, 2 ni 4. Para 𝑎 ≠ −4 sirven las tres primeras columnas. Para 𝑎 = −4, una base es
{(1, 2, −1), (4, 2, −4), (3, −2, −4)}, es decir, las columnas primera, tercera y cuarta.

4.39  Espacio columna de una matriz con parámetro
2022/23 · Ordinaria · Modelo D · Pregunta original 2

Sea la matriz ampliada
⎛ 1 1 −1 1⎞
⎜  ⎟
𝐴(𝑎) = ⎜
⎜2 3 𝑎 3 ⎟
⎜  ⎟.
⎟
⎝1 𝑎 3 2 ⎠
Determina para qué valores de 𝑎 el espacio columna de 𝐴(𝑎) tiene dimensión 1, 2, 3 o 4. En cada caso
posible, calcula una base.
Respuesta
La dimensión coincide con el número de columnas pivote. Se seleccionan las columnas correspon-
dientes de la matriz original, no de la matriz escalonada. Si 𝑎 = 2, la dimensión es 2 y una base es
{(1, 2, 1), (1, 3, 2)}. Si 𝑎 ≠ 2, −3, la dimensión es 3 y sirven las tres primeras columnas. Si 𝑎 = −3, la
dimensión es 3 y una base es {(1, 2, 1), (1, 3, −3), (1, 3, 2)}, las columnas primera, segunda y cuarta.
No hay valores que den dimensión 1 ni 4.

Ingeniería Informática · UFV  39
```

#### Página 40

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

4.40  Verdadero o falso: repaso del tema
2024/25 · Ordinaria · Pregunta original 10 · Modelos A, B y C

Indica si cada afirmación es verdadera (V) o falsa (F). Las etiquetas A.n, B.n y C.n indican el modelo
y el apartado original.

A.5 Una base de un espacio vectorial es única.
A.6 El núcleo de una matriz 𝑚 × 𝑛 es un subespacio de ℝ𝑚 .
B.5 Cualesquiera tres vectores de ℝ3 linealmente independientes forman una base de ℝ3 .
B.6 El espacio columna de 𝐴 es el conjunto de todas las soluciones del sistema 𝐴𝑥 = 𝑏.
B.7 Si 𝐵 es una forma escalonada de 𝐴, las columnas pivote de 𝐵 forman una base de Col(𝐴).
C.5 Todo conjunto de cinco vectores linealmente independientes en ℝ5 es una base de ℝ5 .
C.6 Una matriz de cambio de base siempre es invertible.

Respuesta

A.5 F. En ℝ, tanto {1} como {2} son bases.
A.6 F. El núcleo es un subespacio de ℝ𝑛 , el espacio de las incógnitas.
B.5 V. Un conjunto libre con tantos vectores como la dimensión es una base.
B.6 F. Col(𝐴) contiene los términos independientes 𝑏 para los que el sistema es compatible, no
sus soluciones 𝑥.
B.7 F. Deben elegirse las columnas correspondientes de 𝐴, pues las operaciones por filas pueden
cambiar el espacio columna.
C.5 V. Son cinco vectores libres en un espacio de dimensión cinco.
C.6 V. El cambio inverso corresponde a la matriz inversa.

Ingeniería Informática · UFV  40
```

#### Página 41

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 5

Transformaciones lineales
Matriz canónica, núcleo, imagen, inyectividad y sobreyectividad.

5.1  Construcción de una aplicación lineal
2023/24 · Ordinaria · Modelo A · Pregunta original 5

Escribe la matriz de una transformación lineal 𝑇 ∶ ℝ4 → ℝ3 que sea sobreyectiva y justifica la
respuesta. Si no fuera posible, explica por qué.
Respuesta
Un ejemplo en las bases canónicas es

⎛ 1 0 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 0 0 ⎟
⎟
⎝0 0 1 0 ⎠

Sus columnas generan ℝ3 , por lo que Im 𝑇 = ℝ3 y 𝑇 es sobreyectiva.

5.2  Construcción de una aplicación lineal
2023/24 · Ordinaria · Modelo B · Pregunta original 5

Escribe la matriz de una transformación lineal 𝑇 ∶ ℝ4 → ℝ5 que sea inyectiva y justifica la respuesta.
Si no fuera posible, explica por qué.
Respuesta
Un ejemplo en las bases canónicas es

⎛ 1  0  0  0⎞
⎜
⎜ 0  1  0  0⎟
⎟
⎜
⎜  ⎟
⎟
⎜
𝐴=⎜ 0  0  1  0⎟
⎟ .
⎜
⎜  ⎟
⎟
⎜
⎜  ⎟
1⎟
⎜0  0  0  ⎟
⎝0  0  0  0⎠

Hay un pivote en cada una de las 4 columnas: 𝐴𝑥 = 0 solo tiene la solución nula. Por tanto, 𝑇 es
inyectiva.

Ingeniería Informática · UFV  41
```

#### Página 42

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.3  Construcción de una aplicación lineal
2023/24 · Ordinaria · Modelo C · Pregunta original 5

Escribe la matriz de una transformación lineal 𝑇 ∶ ℝ3 → ℝ4 que sea inyectiva y justifica la respuesta.
Si no fuera posible, explica por qué.
Respuesta
Un ejemplo en las bases canónicas es
⎛ 1  0  0⎞
⎜
⎜ 0  1  0⎟
⎟
𝐴=⎜
⎜
⎜
⎟
⎟.
⎜
⎜0  0  1⎟
⎟
⎟
⎝0  0  0⎠
Hay un pivote en cada una de las 3 columnas: 𝐴𝑥 = 0 solo tiene la solución nula. Por tanto, 𝑇 es
inyectiva.

5.4  Construcción con una propiedad de la aplicación
2025/26 · Extraordinaria · Modelo A · Pregunta original 5

Escribe una matriz que represente una transformación lineal 𝑇 ∶ ℝ3 → ℝ4 inyectiva. Justifica la
propiedad sin calcular determinantes.
Respuesta
Un ejemplo es
⎛ 1  0  0⎞
⎜
⎜ 0  1  0⎟
⎟
𝐴=⎜
⎜
⎜
⎟
⎟.
⎜
⎜0  0  1⎟
⎟
⎟
⎝0  0  0⎠
Hay un pivote en cada columna, así que 𝐴𝑥 = 0 solo admite la solución nula. Su núcleo es trivial y
es inyectiva.

5.5  Construcción con una propiedad de la aplicación
2025/26 · Extraordinaria · Modelo B · Pregunta original 5

Escribe una matriz que represente una transformación lineal 𝑇 ∶ ℝ4 → ℝ3 sobreyectiva. Justifica la
propiedad sin calcular determinantes.
Respuesta
Un ejemplo es
⎛ 1 0 0 0⎞
⎜  ⎟
𝐴=⎜
⎜0 1 0 0 ⎟
⎜  ⎟.
⎟
⎝ 0 0 1 0 ⎠
Hay un pivote en cada fila, de modo que las columnas generan ℝ3 . La imagen coincide con el espacio
de llegada y es sobreyectiva.

Ingeniería Informática · UFV  42
```

#### Página 43

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.6  Construcción con una propiedad de la aplicación
2025/26 · Extraordinaria · Modelo C · Pregunta original 5

Escribe una matriz distinta de la identidad que represente una transformación lineal 𝑇 ∶ ℝ4 → ℝ4
biyectiva. Justifica la propiedad sin calcular determinantes.
Respuesta
Un ejemplo es
⎛ 1  1  0  0⎞
⎜
⎜ 0  1  0  0⎟
⎟
𝐴=⎜
⎜
⎜
⎟
⎟.
⎜
⎜0  0  1  0⎟
⎟
⎟
⎝0  0  0  1⎠
Hay un pivote en cada fila y en cada columna. El núcleo es trivial y la imagen es ℝ4 ; por tanto, es
inyectiva y sobreyectiva, es decir, biyectiva. La matriz no es 𝐼.

5.7  Sobreyectividad sin inyectividad
2024/25 · Ordinaria · Modelo B · Pregunta original 7

Escribe la matriz de una transformación lineal 𝑇 ∶ ℝ4 → ℝ3 que sea sobreyectiva y no inyectiva.
Respuesta
Un ejemplo es
⎛ 1 0 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 0 0 ⎟
⎟
⎝0 0 1 0 ⎠
Sus tres primeras columnas generan ℝ3 , por lo que es sobreyectiva. Su núcleo tiene dimensión 4−3 =
1 > 0, así que no es inyectiva.

5.8  Sobreyectividad sin inyectividad
2024/25 · Ordinaria · Modelo C · Pregunta original 7

Escribe la matriz de una transformación lineal 𝑇 ∶ ℝ5 → ℝ3 que sea sobreyectiva y no inyectiva.
Respuesta
Un ejemplo es
⎛ 1 0 0 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 0 0 0 ⎟
⎟
⎝0 0 1 0 0 ⎠
Sus tres primeras columnas generan ℝ3 , por lo que es sobreyectiva. Su núcleo tiene dimensión 5−3 =
2 > 0, así que no es inyectiva.

Ingeniería Informática · UFV  43
```

#### Página 44

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.9  Compatibilidad a partir del subespacio imagen
2023/24 · Ordinaria · Modelo A · Pregunta original 3

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, e imagen

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 + 𝑦 + 𝑧 = 0, 𝑧 = 0}.

Clasifica razonadamente el sistema
⎛ 1
⎜ ⎞ ⎟
𝐴𝑥 = ⎜
⎜ −1
⎜ ⎟
⎟.
⎟
⎝ ⎠

Respuesta
El vector 𝑏 = (1, −1, 0) satisface las ecuaciones de la imagen; por tanto, el sistema es compatible. Una
base de la imagen es {(1, −1, 0)} y su dimensión es 1. Por rango–nulidad, dim ker 𝑓 = 3 − 1 = 2 > 0.
El sistema es compatible indeterminado.

5.10  Compatibilidad a partir del subespacio imagen
2023/24 · Ordinaria · Modelo B · Pregunta original 3

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, e imagen

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 − 𝑦 − 𝑧 = 0}.

Clasifica razonadamente el sistema
⎛ 0
⎜ ⎞ ⎟
𝐴𝑥 = ⎜
⎜1⎟
⎜  ⎟.
⎟
−1
⎝ ⎠

Respuesta
El vector 𝑏 = (0, 1, −1) satisface las ecuaciones de la imagen; por tanto, el sistema es compatible. Una
base de la imagen es {(1, 1, 0), (1, 0, 1)} y su dimensión es 2. Por rango–nulidad, dim ker 𝑓 = 3 − 2 =
1 > 0. El sistema es compatible indeterminado.

5.11  Compatibilidad a partir del subespacio imagen
2023/24 · Ordinaria · Modelo C · Pregunta original 3

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, e imagen

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 + 2𝑦 − 𝑧 = 0, 𝑥 − 3𝑧 = 0}.

Clasifica razonadamente el sistema
⎛ 3
⎜ ⎞ ⎟
𝐴𝑥 = ⎜
⎜ −1
⎜ ⎟
⎟.
⎟
⎝1⎠

Respuesta
El vector 𝑏 = (3, −1, 1) satisface las ecuaciones de la imagen; por tanto, el sistema es compatible. Una
base de la imagen es {(3, −1, 1)} y su dimensión es 1. Por rango–nulidad, dim ker 𝑓 = 3 − 1 = 2 > 0.
El sistema es compatible indeterminado.

Ingeniería Informática · UFV  44
```

#### Página 45

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.12  Rango y compatibilidad a partir de un plano imagen
2025/26 · Ordinaria · Modelo A · Pregunta original 6

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, y

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 + 𝑦 − 𝑧 = 0}.

a) Determina la dimensión de la imagen y el rango de 𝐴. b) Clasifica 𝐴𝑥 = 𝑏, con 𝑏 = (2, 1, −1), sin
calcular 𝐴 ni determinantes.
Respuesta
La imagen es un plano definido por una ecuación homogénea no trivial: dim Im 𝑓 = rg 𝐴 = 2. Al
sustituir 𝑏 se obtiene 2 + 1 − (−1) = 4 ≠ 0. No pertenece a la imagen, por lo que el sistema es
incompatible.

5.13  Rango y compatibilidad a partir de un plano imagen
2025/26 · Ordinaria · Modelo B · Pregunta original 6

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, y

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 𝑥 − 𝑦 + 𝑧 = 0}.

a) Determina la dimensión de la imagen y el rango de 𝐴. b) Clasifica 𝐴𝑥 = 𝑏, con 𝑏 = (1, 2, 0), sin
calcular 𝐴 ni determinantes.
Respuesta
La imagen es un plano definido por una ecuación homogénea no trivial: dim Im 𝑓 = rg 𝐴 = 2. Al
sustituir 𝑏 se obtiene 1 − 2 + 0 = −1 ≠ 0. No pertenece a la imagen, por lo que el sistema es incom-
patible.

5.14  Rango y compatibilidad a partir de un plano imagen
2025/26 · Ordinaria · Modelo C · Pregunta original 6

Sea 𝑓 ∶ ℝ3 → ℝ3 lineal, con matriz canónica 𝐴, y

Im 𝑓 = {(𝑥, 𝑦, 𝑧) ∈ ℝ3 ∶ 3𝑥 − 2𝑦 − 𝑧 = 0}.

a) Determina la dimensión de la imagen y el rango de 𝐴. b) Clasifica 𝐴𝑥 = 𝑏, con 𝑏 = (1, 1, 1), sin
calcular 𝐴 ni determinantes.
Respuesta
La imagen es un plano definido por una ecuación homogénea no trivial: dim Im 𝑓 = rg 𝐴 = 2. Al
sustituir 𝑏 se obtiene 3 − 2 − 1 = 0. Pertenece a la imagen, así que el sistema es compatible. Además,
dim ker 𝑓 = 3 − 2 = 1: hay infinitas soluciones y es compatible indeterminado.

Ingeniería Informática · UFV  45
```

#### Página 46

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.15  Bases y dimensiones del núcleo y la imagen
2025/26 · Extraordinaria · Modelo A · Pregunta original 8

Sea 𝑇 ∶ ℝ3 → ℝ2 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (𝑥 + 𝑧, 𝑥 + 𝑦). a) Halla una base del núcleo y su dimensión.
b) Halla una base de la imagen y su dimensión. c) ¿Es sobreyectiva? Razona la respuesta.
Respuesta
Resolver 𝑇(𝑥, 𝑦, 𝑧) = 0 da 𝑧 = −𝑥 e 𝑦 = −𝑥. Por tanto,

ker 𝑇 = Gen{(1, −1, −1)},  dim ker 𝑇 = 1.

La matriz canónica es
1 0 1
𝐴=(  ).
1 1 0
Tiene dos columnas independientes, de modo que rg 𝐴 = 2 y Im 𝑇 = ℝ2 . Una base de la imagen es
{(1, 0), (0, 1)}, de dimensión 2. Como la imagen coincide con el espacio de llegada, 𝑇 es sobreyectiva.

5.16  Bases y dimensiones del núcleo y la imagen
2025/26 · Extraordinaria · Modelo B · Pregunta original 8

Sea 𝑇 ∶ ℝ3 → ℝ2 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (2𝑥 + 𝑦, 𝑥 − 2𝑧). a) Halla una base del núcleo y su dimensión.
b) Halla una base de la imagen y su dimensión. c) ¿Es sobreyectiva? Razona la respuesta.
Respuesta
Resolver 𝑇(𝑥, 𝑦, 𝑧) = 0 da 𝑥 = 2𝑧 e 𝑦 = −4𝑧. Por tanto,

ker 𝑇 = Gen{(2, −4, 1)},  dim ker 𝑇 = 1.

La matriz canónica es
2 1 0
𝐴=(  ).
1 0 −2
Tiene dos columnas independientes, de modo que rg 𝐴 = 2 y Im 𝑇 = ℝ2 . Una base de la imagen es
{(1, 0), (0, 1)}, de dimensión 2. Como la imagen coincide con el espacio de llegada, 𝑇 es sobreyectiva.

5.17  Bases y dimensiones del núcleo y la imagen
2025/26 · Extraordinaria · Modelo C · Pregunta original 8

Sea 𝑇 ∶ ℝ3 → ℝ2 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (𝑥 + 2𝑦, 2𝑥 − 𝑧). a) Halla una base del núcleo y su dimensión.
b) Halla una base de la imagen y su dimensión. c) ¿Es sobreyectiva? Razona la respuesta.
Respuesta
Resolver 𝑇(𝑥, 𝑦, 𝑧) = 0 da 𝑥 = −2𝑦 y 𝑧 = −4𝑦. Por tanto,

ker 𝑇 = Gen{(2, −1, 4)},  dim ker 𝑇 = 1.

La matriz canónica es
1 2 0
𝐴=(  ).
2 0 −1
Tiene dos columnas independientes, de modo que rg 𝐴 = 2 y Im 𝑇 = ℝ2 . Una base de la imagen es
{(1, 0), (0, 1)}, de dimensión 2. Como la imagen coincide con el espacio de llegada, 𝑇 es sobreyectiva.

Ingeniería Informática · UFV  46
```

#### Página 47

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.18  Reconstrucción de la matriz canónica
2025/26 · Ordinaria · Modelo A · Pregunta original 7

Sea 𝑇 ∶ ℝ3 → ℝ3 lineal y supongamos que

𝑇(1, 0, 0) = (1, 0, 0),  𝑇(0, 1, 0) = (1, 1, 0),

𝑇(1, 1, 1) = (2, 1, 1).
a) Determina la matriz de 𝑇 en la base canónica. b) Decide si 𝑇 es inyectiva.
Respuesta
Por linealidad, 𝑇(𝑒3 ) = 𝑇(1, 1, 1) − 𝑇(𝑒1 ) − 𝑇(𝑒2 ) = (0, 0, 1). Así,

⎛ 1 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 0 ⎟
⎟
⎝0 0 1 ⎠

𝐴 ya tiene tres pivotes. En consecuencia, ker 𝑇 = {0} y 𝑇 es inyectiva.

5.19  Reconstrucción de la matriz canónica
2025/26 · Ordinaria · Modelo B · Pregunta original 7

Sea 𝑇 ∶ ℝ3 → ℝ3 lineal y supongamos que

𝑇(1, 0, 0) = (1, 1, 0),  𝑇(0, 1, 0) = (0, 1, 0),

𝑇(1, 1, 1) = (1, 2, 1).
a) Determina la matriz de 𝑇 en la base canónica. b) Decide si 𝑇 es inyectiva.
Respuesta
Por linealidad, 𝑇(𝑒3 ) = 𝑇(1, 1, 1) − 𝑇(𝑒1 ) − 𝑇(𝑒2 ) = (0, 0, 1). Así,

⎛ 1 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜1 1 0 ⎟
⎟
⎝0 0 1 ⎠

La operación 𝐹2 ← 𝐹2 − 𝐹1 transforma 𝐴 en 𝐼 y muestra los tres pivotes. En consecuencia, ker 𝑇 = {0}
y 𝑇 es inyectiva.

Ingeniería Informática · UFV  47
```

#### Página 48

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.20  Reconstrucción de la matriz canónica
2025/26 · Ordinaria · Modelo C · Pregunta original 7

Sea 𝑇 ∶ ℝ3 → ℝ3 lineal y supongamos que

𝑇(1, 0, 0) = (1, 1, 1),  𝑇(0, 1, 0) = (1, 1, 0),

𝑇(1, 1, 1) = (0, 2, 0).
a) Determina la matriz de 𝑇 en la base canónica. b) Decide si 𝑇 es inyectiva.
Respuesta
Por linealidad, 𝑇(𝑒3 ) = 𝑇(1, 1, 1) − 𝑇(𝑒1 ) − 𝑇(𝑒2 ) = (−2, 0, −1). Así,

⎛ 1 1 −2⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜1 1 0 ⎟⎟
⎝1 0 −1⎠

En 𝐴𝑥 = 0, la segunda ecuación da 𝑥2 = −𝑥1 ; la primera fuerza 𝑥3 = 0 y la tercera da 𝑥1 = 0. Así,
también 𝑥2 = 0. En consecuencia, ker 𝑇 = {0} y 𝑇 es inyectiva.

5.21  Aplicación lineal definida por una matriz ampliada
2022/23 · Ordinaria · Modelo B · Pregunta original 4

La siguiente matriz define una aplicación lineal 𝑓 en bases canónicas:

⎛ 1 1 𝑎 1⎞
⎜  ⎟
𝐴(𝑎) = ⎜  ⎟.
⎜1 𝑎 1 1 ⎟
⎜  ⎟
⎝ 𝑎 1 1 1⎠

a) Indica las dimensiones de los espacios de partida y llegada.
b) Determina para qué valores de 𝑎 es inyectiva y para cuáles es sobreyectiva.
c) Calcula una base y la dimensión del núcleo para 𝑎 = 1.
d) Calcula una base y la dimensión de la imagen para 𝑎 = 0.

Respuesta

a) 𝑓 ∶ ℝ4 → ℝ3 : las dimensiones son 4 y 3.
b) Nunca es inyectiva, pues dim ker 𝑓 = 4 − rg 𝐴 ≥ 1. Es sobreyectiva para 𝑎 ≠ 1, incluido 𝑎 = −2,
cuando rg 𝐴 = 3.
c) Al resolver 𝐴(1)𝑥 = 0 se obtiene la base {(−1, 1, 0, 0), (−1, 0, 1, 0), (−1, 0, 0, 1)}. La dimensión del
núcleo es 3.
d) Para 𝑎 = 0, el rango es 3; por tanto, Im 𝑓 = ℝ3 y una base es {(1, 0, 0), (0, 1, 0), (0, 0, 1)}.

Ingeniería Informática · UFV  48
```

#### Página 49

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.22  Aplicación lineal definida por una matriz ampliada
2022/23 · Ordinaria · Modelo C · Pregunta original 4

La siguiente matriz define una aplicación lineal 𝑓 en bases canónicas:

⎛ 1 2 4 3⎞
⎜  ⎟
𝐴(𝑎) = ⎜  ⎟.
⎜ 2 −𝑎 2 −2⎟
⎜  ⎟
⎝−1 −2 𝑎 𝑎 ⎠

a) Indica las dimensiones de los espacios de partida y llegada.
b) Determina para qué valores de 𝑎 es inyectiva y para cuáles es sobreyectiva.
c) Calcula una base y la dimensión del núcleo para 𝑎 = 2.
d) Calcula una base y la dimensión de la imagen para 𝑎 = 0.

Respuesta

a) 𝑓 ∶ ℝ4 → ℝ3 : las dimensiones son 4 y 3.
b) Nunca es inyectiva, pues dim ker 𝑓 = 4 − rg 𝐴 ≥ 1. Es sobreyectiva para todo 𝑎 ∈ ℝ, cuando
rg 𝐴 = 3.
c) Al resolver 𝐴(2)𝑥 = 0 se obtiene la base {(8, −3, −5, 6)}. La dimensión del núcleo es 1.
d) Para 𝑎 = 0, el rango es 3; por tanto, Im 𝑓 = ℝ3 y una base es {(1, 0, 0), (0, 1, 0), (0, 0, 1)}.

5.23  Aplicación lineal definida por una matriz ampliada
2022/23 · Ordinaria · Modelo D · Pregunta original 4

La siguiente matriz define una aplicación lineal 𝑓 en bases canónicas:

⎛ 1 1 −1 1⎞
⎜  ⎟
𝐴(𝑎) = ⎜
⎜2 3 𝑎 3 ⎟
⎜  ⎟.
⎟
⎝1 𝑎 3 2 ⎠

a) Indica las dimensiones de los espacios de partida y llegada.
b) Determina para qué valores de 𝑎 es inyectiva y para cuáles es sobreyectiva.
c) Calcula una base y la dimensión del núcleo para 𝑎 = 1.
d) Calcula una base y la dimensión de la imagen para 𝑎 = 0.

Respuesta

a) 𝑓 ∶ ℝ4 → ℝ3 : las dimensiones son 4 y 3.
b) Nunca es inyectiva, pues dim ker 𝑓 = 4 − rg 𝐴 ≥ 1. Es sobreyectiva para 𝑎 ≠ 2, incluido 𝑎 = −3,
cuando rg 𝐴 = 3.
c) Al resolver 𝐴(1)𝑥 = 0 se obtiene la base {(4, 1, 1, −4)}. La dimensión del núcleo es 1.
d) Para 𝑎 = 0, el rango es 3; por tanto, Im 𝑓 = ℝ3 y una base es {(1, 0, 0), (0, 1, 0), (0, 0, 1)}.

Ingeniería Informática · UFV  49
```

#### Página 50

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

5.24  Verdadero o falso: repaso del tema
2024/25 · Ordinaria · Pregunta original 10 · Modelos A, B y C

Indica si cada afirmación es verdadera (V) o falsa (F). Las etiquetas A.n, B.n y C.n indican el modelo
y el apartado original.

A.7 Las bases de dos espacios vectoriales isomorfos de dimensión finita tienen el mismo número
de vectores.
A.8 Si 𝑓 ∶ ℝ4 → ℝ3 es lineal, es posible que dim ker 𝑓 = 1 y rg 𝑓 = 2.
B.8 Si 𝑓 ∶ 𝑉 → 𝑊 es lineal y 𝑥 ∈ ker 𝑓 , entonces 𝑓 (𝑥 + 𝑣) = 𝑣 para todo 𝑣 ∈ 𝑉.
C.7 Toda función de la forma 𝑓 (𝑥) = 𝑎𝑥 + 𝑏 es una aplicación lineal de ℝ en ℝ.

Respuesta

A.7 V. Los isomorfismos conservan la dimensión.
A.8 F. Rango–nulidad exige dim ker 𝑓 + rg 𝑓 = 4, pero 1 + 2 = 3.
B.8 F. La linealidad da 𝑓 (𝑥 + 𝑣) = 𝑓 (𝑥) + 𝑓 (𝑣) = 𝑓 (𝑣), que no tiene por qué ser 𝑣.
C.7 F. Debe cumplirse 𝑓 (0) = 0, lo que exige 𝑏 = 0.

Ingeniería Informática · UFV  50
```

#### Página 51

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

TEMA 6

Diagonalización, autovalores y
autovectores
Autovalores, espacios propios, polinomio característico y diagonalización.

6.1  Un autovalor sin cálculos
2024/25 · Ordinaria · Modelo B · Pregunta original 8

Encuentra un autovalor de la siguiente matriz sin realizar cálculos. Razona la respuesta.

⎛ 1 2 3⎞
⎜  ⎟
𝐴=⎜  ⎟.
⎜1 2 3 ⎟
⎜  ⎟
⎝1 2 3 ⎠

Respuesta
Las filas repetidas hacen que 𝐴 sea singular; por tanto, existe 𝑣 ≠ 0 con 𝐴𝑣 = 0. Así, 0 es un autovalor.
Este argumento no presupone que la matriz sea diagonalizable.

6.2  Comprobación de posibles autovectores
2024/25 · Ordinaria · Modelo C · Pregunta original 8

¿Cuáles de los siguientes vectores son autovectores de 𝐴?

⎛ 1 3 6⎞
⎜
⎜  ⎟
⎟,
𝐴=⎜
⎜2 1 4 ⎟
⎟
⎝1 0 3 ⎠

𝑣1 = (1, 3, 2),  𝑣2 = (−2, −2, 1),  𝑣3 = (0, 1, −5).

Respuesta

𝐴𝑣1 = (22, 13, 7),  𝐴𝑣2 = (−2, −2, 1),  𝐴𝑣3 = (−27, −19, −15).
Solo 𝐴𝑣2 = 𝑣2 es proporcional al vector de partida. Por tanto, únicamente 𝑣2 es autovector, asociado
al autovalor 1.

Ingeniería Informática · UFV  51
```

#### Página 52

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.3  Lectura de una diagonalización
2024/25 · Ordinaria · Modelo C · Pregunta original 9

Una matriz admite la factorización

⎛ −2 0 −1⎞ ⎛5 0 0⎞ ⎛ 0 0 1 ⎞
⎜
⎜  ⎟
⎟⎜⎜0 5 0 ⎟⎟ ⎜
⎜2 1 4⎟  ⎟
𝐴=⎜
⎜0 1 2⎟  ⎟⎜⎜  ⎟
⎟⎜⎜  ⎟.
⎟
⎝ 1  0 0 ⎠⎝  0 0 4 ⎠⎝  −1 0 −2 ⎠

Sin multiplicar las matrices, determina los autovalores y una base de cada espacio propio.
Respuesta
La factorización es 𝐴 = 𝑃𝐷𝑃−1 . Los autovalores son 5, con multiplicidad algebraica 2, y 4, con mul-
tiplicidad algebraica 1. Las columnas correspondientes de 𝑃 dan

𝐵𝐸5 = {(−2, 0, 1), (0, 1, 0)},  𝐵𝐸4 = {(−1, 2, 0)}.

6.4  Vectores que conservan su dirección
2025/26 · Extraordinaria · Modelo A · Pregunta original 9

Sea 𝑇 ∶ ℝ2 → ℝ2 , dada por 𝑇(𝑥, 𝑦) = (2𝑥+𝑦, 2𝑦). a) Obtén el conjunto de vectores que se transforman
en una versión escalada de sí mismos. b) ¿Cuál es el factor de escala? ¿Qué estructura algebraica tiene
el conjunto?
Respuesta
La matriz canónica es
2 1
𝐴=(  ).
0 2
Es triangular y su único autovalor es 2. Resolver (𝐴 − (2)𝐼)𝑣 = 0 da

𝐸2 = {(𝑡, 0) ∶ 𝑡 ∈ ℝ}.

Es una recta vectorial, un subespacio de dimensión 1. Para cada vector no nulo de ella, el factor de
escala es 2. El cero también pertenece al conjunto, aunque no es autovector y satisface 𝑇(0) = 𝑐 0
para cualquier escalar 𝑐.

Ingeniería Informática · UFV  52
```

#### Página 53

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.5  Vectores que conservan su dirección
2025/26 · Extraordinaria · Modelo B · Pregunta original 9

Sea 𝑇 ∶ ℝ2 → ℝ2 , dada por 𝑇(𝑥, 𝑦) = (−𝑥, 2𝑥 − 𝑦). a) Obtén el conjunto de vectores que se transfor-
man en una versión escalada de sí mismos. b) ¿Cuál es el factor de escala? ¿Qué estructura algebraica
tiene el conjunto?
Respuesta
La matriz canónica es
−1 0
𝐴=(  ).
2 −1
Es triangular y su único autovalor es −1. Resolver (𝐴 − (−1)𝐼)𝑣 = 0 da

𝐸−1 = {(0, 𝑡) ∶ 𝑡 ∈ ℝ}.

Es una recta vectorial, un subespacio de dimensión 1. Para cada vector no nulo de ella, el factor de
escala es −1. El cero también pertenece al conjunto, aunque no es autovector y satisface 𝑇(0) = 𝑐 0
para cualquier escalar 𝑐.

6.6  Vectores que conservan su dirección
2025/26 · Extraordinaria · Modelo C · Pregunta original 9

Sea 𝑇 ∶ ℝ2 → ℝ2 , dada por 𝑇(𝑥, 𝑦) = (𝑥, 𝑥 + 𝑦). a) Obtén el conjunto de vectores que se transforman
en una versión escalada de sí mismos. b) ¿Cuál es el factor de escala? ¿Qué estructura algebraica
tiene el conjunto?
Respuesta
La matriz canónica es
1 0
𝐴=(  ).
1 1
Es triangular y su único autovalor es 1. Resolver (𝐴 − (1)𝐼)𝑣 = 0 da

𝐸1 = {(0, 𝑡) ∶ 𝑡 ∈ ℝ}.

Es una recta vectorial, un subespacio de dimensión 1. Para cada vector no nulo de ella, el factor de
escala es 1. El cero también pertenece al conjunto, aunque no es autovector y satisface 𝑇(0) = 𝑐 0
para cualquier escalar 𝑐.

Ingeniería Informática · UFV  53
```

#### Página 54

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.7  La diagonalización no es única
2024/25 · Ordinaria · Modelo A · Pregunta original 8

¿La diagonalización de una matriz es única? Explícalo con el ejemplo

−2 12  3 4  2 0  −1 4
(  )=(  )(  )(  ).
−1 5  1 1  0 1  1 −3

Respuesta
No. Pueden permutarse las columnas de 𝑃 si se permutan de la misma forma los autovalores de 𝐷.
En este caso, otra diagonalización es

−2 12  4 3  1 0  1 −3
(  )=(  )(  )(  ).
−1 5  1 1  0 2  −1 4

También pueden multiplicarse los autovectores de 𝑃 por escalares no nulos.

6.8  Parámetros a partir de un autovector
2023/24 · Ordinaria · Modelo A · Pregunta original 6

Dada la matriz
1 𝑎
𝐴=(  ),
2 𝑏
a) calcula 𝑎, 𝑏 para que (−2, 1) sea un autovector asociado a 𝜆1 = 5; b) calcula el otro autovalor.
Respuesta
La igualdad 𝐴𝑣 = 𝜆1 𝑣 exige
−2 + 𝑎 = −10,  −4 + 𝑏 = 5.
Por tanto, 𝑎 = −8 y 𝑏 = 9. La suma de los autovalores es la traza 10, de modo que el otro autovalor
es 5.

6.9  Parámetros a partir de un autovector
2023/24 · Ordinaria · Modelo B · Pregunta original 6

Dada la matriz
𝑎 −2
𝐴=(  ),
−5 𝑏
a) calcula 𝑎, 𝑏 para que (1, 1) sea un autovector asociado a 𝜆1 = −4; b) calcula el otro autovalor.
Respuesta
La igualdad 𝐴𝑣 = 𝜆1 𝑣 exige
𝑎 − 2 = −4,  −5 + 𝑏 = −4.
Por tanto, 𝑎 = −2 y 𝑏 = 1. La suma de los autovalores es la traza −1, de modo que el otro autovalor
es 3.

Ingeniería Informática · UFV  54
```

#### Página 55

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.10  Parámetros a partir de un autovector
2023/24 · Ordinaria · Modelo C · Pregunta original 6

Dada la matriz
𝑎 1
𝐴=(  ),
5 𝑏
a) calcula 𝑎, 𝑏 para que (1, 1) sea un autovector asociado a 𝜆1 = 3; b) calcula el otro autovalor.
Respuesta
La igualdad 𝐴𝑣 = 𝜆1 𝑣 exige
𝑎 + 1 = 3,  5 + 𝑏 = 3.
Por tanto, 𝑎 = 2 y 𝑏 = −2. La suma de los autovalores es la traza 0, de modo que el otro autovalor es
−3.

6.11  Condición para que los autovalores sean reales
2024/25 · Ordinaria · Modelo A · Pregunta original 7

Halla los valores de 𝑎 para los que los autovalores de 𝐴 son reales. Expresa la respuesta como una
desigualdad.
2 𝑎
𝐴=(  ).
−1 1

Respuesta

𝑝𝐴 (𝜆) = det(𝐴 − 𝜆𝐼) = 𝜆2 − 3𝜆 + 2 + 𝑎.
Las raíces son reales si y solo si el discriminante es no negativo:

9 − 4(2 + 𝑎) = 1 − 4𝑎 ≥ 0  ⟺  𝑎≤ .

6.12  Espacio nulo asociado y autovalores restantes
2024/25 · Ordinaria · Modelo B · Pregunta original 9

Sea
⎛ 1 0  1⎞
⎜  ⎟
𝐴=⎜
⎜
⎜ 0 1 −1 ⎟
⎟.
⎟
⎝1 −1 0 ⎠
Un autovalor es 1 y una base de su espacio propio es {(1, 1, 0)}. a) ¿De qué matriz construida a partir
de 𝐴 es este vector una base del espacio nulo? b) Obtén los otros dos autovalores.
Respuesta
Es una base de ker(𝐴 − 𝐼) y también de ker(𝐼 − 𝐴). Como tr 𝐴 = 2 y det 𝐴 = −2, los otros autovalores
cumplen 𝜆2 + 𝜆3 = 1 y 𝜆2 𝜆3 = −2. Son las raíces de 𝑡2 − 𝑡 − 2 = (𝑡 − 2)(𝑡 + 1): 2 y −1.

Ingeniería Informática · UFV  55
```

#### Página 56

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.13  Polinomio característico y multiplicidades
2022/23 · Ordinaria · Modelo B · Pregunta original 5

Sea el endomorfismo de ℝ3 cuya matriz en la base canónica es

⎛ 1 1 0⎞
⎜  ⎟
𝐶=⎜  ⎟.
⎜1 0 1 ⎟
⎜  ⎟
⎝0 1 1 ⎠

Calcula su polinomio característico, sus autovalores y sus multiplicidades.
Respuesta
Con la convención 𝑝𝐶 (𝜆) = det(𝐶 − 𝜆𝐼), se obtiene

𝑝𝐶 (𝜆) = −(𝜆 − 1)(𝜆 + 1)(𝜆 − 2) = −𝜆3 + 2𝜆2 + 𝜆 − 2.

Los autovalores son 1, −1, 2, todos de multiplicidad algebraica 1 (y geométrica 1).

6.14  Polinomio característico y multiplicidades
2022/23 · Ordinaria · Modelo C · Pregunta original 5

Sea el endomorfismo de ℝ3 cuya matriz en la base canónica es

⎛ 1  2  4⎞
⎜
⎜  ⎟
𝐶=⎜
⎜2  4  2⎟ ⎟.
⎟
⎝ −1 −2 −4 ⎠

Calcula su polinomio característico, sus autovalores y sus multiplicidades.
Respuesta
Con la convención 𝑝𝐶 (𝜆) = det(𝐶 − 𝜆𝐼), se obtiene

𝑝𝐶 (𝜆) = −𝜆(𝜆 − 4)(𝜆 + 3) = −𝜆3 + 𝜆2 + 12𝜆.

Los autovalores son 0, 4, −3, todos de multiplicidad algebraica 1 (y geométrica 1).

6.15  Polinomio característico y multiplicidades
2022/23 · Ordinaria · Modelo D · Pregunta original 5

Sea el endomorfismo de ℝ3 cuya matriz en la base canónica es

⎛ 1 1 −1⎞
⎜
⎜  ⎟
⎟.
𝐶=⎜
⎜2 3 2 ⎟⎟
⎝1 2 3 ⎠

Calcula su polinomio característico, sus autovalores y sus multiplicidades.
Respuesta
Con la convención 𝑝𝐶 (𝜆) = det(𝐶 − 𝜆𝐼), se obtiene

𝑝𝐶 (𝜆) = −𝜆(𝜆 − 2)(𝜆 − 5) = −𝜆3 + 7𝜆2 − 10𝜆.

Los autovalores son 0, 2, 5, todos de multiplicidad algebraica 1 (y geométrica 1).

Ingeniería Informática · UFV  56
```

#### Página 57

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.16  Matriz canónica y espectro de una aplicación
2023/24 · Ordinaria · Modelo A · Pregunta original 7

Sea 𝑓 ∶ ℝ3 → ℝ3 , dada por 𝑓 (𝑥, 𝑦, 𝑧) = (𝑥 + 2𝑦, −𝑦, 𝑥 + 𝑦 − 2𝑧). Calcula: a) su matriz en la base
canónica; b) sus autovalores y su multiplicidad.
Respuesta
Las columnas son 𝑓 (𝑒1 ), 𝑓 (𝑒2 ), 𝑓 (𝑒3 ), por lo que

⎛ 1 2 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 −1 0 ⎟
⎟
⎝1 1 −2⎠

El polinomio característico es

det(𝐴 − 𝜆𝐼) = (1 − 𝜆)(−1 − 𝜆)(−2 − 𝜆).

Los autovalores son 1, −1, −2, todos con multiplicidad algebraica 1.

6.17  Matriz canónica y espectro de una aplicación
2023/24 · Ordinaria · Modelo B · Pregunta original 7

Sea 𝑓 ∶ ℝ3 → ℝ3 , dada por 𝑓 (𝑥, 𝑦, 𝑧) = (𝑥 + 4𝑧, 2𝑥 − 𝑦 − 4𝑧, 3𝑧). Calcula: a) su matriz en la base
canónica; b) sus autovalores y su multiplicidad.
Respuesta
Las columnas son 𝑓 (𝑒1 ), 𝑓 (𝑒2 ), 𝑓 (𝑒3 ), por lo que

⎛ 1 0  4⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜2 −1 −4⎟
⎟
⎝0 0  3⎠

El polinomio característico es

det(𝐴 − 𝜆𝐼) = (1 − 𝜆)(−1 − 𝜆)(3 − 𝜆).

Los autovalores son 1, −1, 3, todos con multiplicidad algebraica 1.

Ingeniería Informática · UFV  57
```

#### Página 58

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.18  Matriz canónica y espectro de una aplicación
2023/24 · Ordinaria · Modelo C · Pregunta original 7

Sea 𝑓 ∶ ℝ3 → ℝ3 , dada por 𝑓 (𝑥, 𝑦, 𝑧) = (3𝑥 + 𝑦, −2𝑦, 2𝑥 + 𝑦 − 𝑧). Calcula: a) su matriz en la base
canónica; b) sus autovalores y su multiplicidad.
Respuesta
Las columnas son 𝑓 (𝑒1 ), 𝑓 (𝑒2 ), 𝑓 (𝑒3 ), por lo que

⎛ 3 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 −2 0 ⎟
⎟
⎝2 1 −1⎠

El polinomio característico es

det(𝐴 − 𝜆𝐼) = (3 − 𝜆)(−2 − 𝜆)(−1 − 𝜆).

Los autovalores son 3, −2, −1, todos con multiplicidad algebraica 1.

6.19  Espacios propios de una transformación lineal
2025/26 · Extraordinaria · Modelo A · Pregunta original 3

Sea 𝑇 ∶ ℝ3 → ℝ3 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (𝑥 + 𝑦, 2𝑦, 3𝑧).
a) Calcula su matriz en la base canónica.
b) Determina los autovalores y sus multiplicidades algebraicas.
c) Calcula los autovectores asociados a cada autovalor.
Utiliza las operaciones más sencillas posibles.
Respuesta
Las imágenes de la base canónica son las columnas de

⎛ 1 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 2 0 ⎟
⎟
⎝0 0 3 ⎠

Por ser triangular, los autovalores se leen en la diagonal. Los autovalores son 1, 2, 3, todos simples.
Al resolver (𝐴 − 𝜆𝐼)𝑣 = 0 se obtiene

𝐸1 = Gen{(1, 0, 0)},  𝐸2 = Gen{(1, 1, 0)},  𝐸3 = Gen{(0, 0, 1)}.

Los autovectores son los múltiplos no nulos del generador de cada espacio propio.

Ingeniería Informática · UFV  58
```

#### Página 59

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.20  Espacios propios de una transformación lineal
2025/26 · Extraordinaria · Modelo B · Pregunta original 3

Sea 𝑇 ∶ ℝ3 → ℝ3 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (𝑥 − 𝑦, 𝑦 + 𝑧, −𝑧).
a) Calcula su matriz en la base canónica.
b) Determina los autovalores y sus multiplicidades algebraicas.
c) Calcula una base de cada espacio propio.
d) Determina razonadamente si 𝐴 es diagonalizable.
Utiliza las operaciones más sencillas posibles.
Respuesta
Las imágenes de la base canónica son las columnas de

⎛ 1 −1 0 ⎞
⎜  ⎟
𝐴=⎜
⎜0 1
⎜  1⎟⎟.
⎟
⎝0 0 −1⎠

Por ser triangular, los autovalores se leen en la diagonal. Los autovalores son 1, de multiplicidad
algebraica 2, y −1, de multiplicidad 1. Los sistemas (𝐴 − 𝜆𝐼)𝑣 = 0 dan

𝐸1 = Gen{(1, 0, 0)},  𝐸−1 = Gen{(−1, −2, 4)}.

Como dim 𝐸1 = 1 < 2, 𝐴 no es diagonalizable.

6.21  Espacios propios de una transformación lineal
2025/26 · Extraordinaria · Modelo C · Pregunta original 3

Sea 𝑇 ∶ ℝ3 → ℝ3 , dada por 𝑇(𝑥, 𝑦, 𝑧) = (2𝑥 + 𝑦, 𝑦 − 2𝑧, 3𝑧).
a) Calcula su matriz en la base canónica.
b) Determina los autovalores y sus multiplicidades algebraicas.
c) Calcula una base de cada espacio propio.
d) Determina razonadamente si 𝐴 es diagonalizable.
Utiliza las operaciones más sencillas posibles.
Respuesta
Las imágenes de la base canónica son las columnas de

⎛ 2 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 1 −2⎟
⎟
⎝0 0 3 ⎠

Por ser triangular, los autovalores se leen en la diagonal. Los autovalores son 1, 2, 3, todos de multi-
plicidad algebraica 1. Los sistemas (𝐴 − 𝜆𝐼)𝑣 = 0 dan

𝐸1 = Gen{(−1, 1, 0)},  𝐸2 = Gen{(1, 0, 0)},  𝐸3 = Gen{(−1, −1, 1)}.

Hay tres autovectores linealmente independientes, por lo que 𝐴 es diagonalizable.

Ingeniería Informática · UFV  59
```

#### Página 60

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.22  Espacio propio y criterio de diagonalización
2024/25 · Ordinaria · Modelo A · Pregunta original 9

Sea
⎛ 0 −12 3 ⎞
⎜
⎜  ⎟
𝐴=⎜
⎜0  1  −1⎟
⎟.
⎟
⎝0  1  3⎠
a) Calcula una base del espacio propio del autovalor 𝜆 = 2.
b) Sabiendo que los autovalores son 0, 2, 2, decide razonadamente si 𝐴 es diagonalizable.

Respuesta
El sistema (𝐴 − 2𝐼)𝑥 = 0 da 𝑦 = −𝑧 y 𝑥 = 15𝑧/2. Por tanto,

𝐸2 = Gen{(15, −2, 2)},  dim 𝐸2 = 1.

La multiplicidad geométrica de 2 es 1, mientras que su multiplicidad algebraica es 2. La matriz no
es diagonalizable.

6.23  Construcción de una matriz no diagonalizable
2025/26 · Ordinaria · Modelo A · Pregunta original 8

Construye una matriz 2 × 2 no diagonalizable con autovalor único 𝜆 = 4. Justifica: a) por qué es su
único autovalor; b) una base del espacio propio; c) por qué no es diagonalizable.
Respuesta
Sirve
4 1
𝐴=(  ).
0 4
Por ser triangular, su único autovalor es 4, de multiplicidad algebraica 2. El sistema (𝐴 − 4𝐼)𝑣 = 0
exige 𝑦 = 0 y deja 𝑥 libre. Por tanto,

𝐸4 = Gen{(1, 0)},  𝑚𝑔 (4) = 1 < 2 = 𝑚𝑎 (4).

La matriz no es diagonalizable.

6.24  Construcción de una matriz no diagonalizable
2025/26 · Ordinaria · Modelo B · Pregunta original 8

Construye una matriz 2 × 2 no diagonalizable con autovalor único 𝜆 = 1. Justifica: a) por qué es su
único autovalor; b) una base del espacio propio; c) por qué no es diagonalizable.
Respuesta
Sirve
1 1
𝐴=(  ).
0 1
Por ser triangular, su único autovalor es 1, de multiplicidad algebraica 2. El sistema (𝐴 − 1𝐼)𝑣 = 0
exige 𝑦 = 0 y deja 𝑥 libre. Por tanto,

𝐸1 = Gen{(1, 0)},  𝑚𝑔 (1) = 1 < 2 = 𝑚𝑎 (1).

La matriz no es diagonalizable.

Ingeniería Informática · UFV  60
```

#### Página 61

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.25  Construcción de una matriz no diagonalizable
2025/26 · Ordinaria · Modelo C · Pregunta original 8

Construye una matriz 2 × 2 no diagonalizable con autovalor único 𝜆 = 2. Justifica: a) por qué es su
único autovalor; b) una base del espacio propio; c) por qué no es diagonalizable.
Respuesta
Sirve
2 1
𝐴=(  ).
0 2
Por ser triangular, su único autovalor es 2, de multiplicidad algebraica 2. El sistema (𝐴 − 2𝐼)𝑣 = 0
exige 𝑦 = 0 y deja 𝑥 libre. Por tanto,

𝐸2 = Gen{(1, 0)},  𝑚𝑔 (2) = 1 < 2 = 𝑚𝑎 (2).

La matriz no es diagonalizable.

6.26  Diagonalización de una matriz triangular
2025/26 · Ordinaria · Modelo A · Pregunta original 9

Sea
⎛ 3 0 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜1 3 0 ⎟
⎟
⎝0 0 −1⎠
a) Obtén sus autovalores y sus multiplicidades algebraicas sin calcular determinantes.
b) Calcula una base del espacio propio del autovalor de multiplicidad algebraica 1.
c) ¿Es diagonalizable? Justifica la respuesta.

Respuesta
Los autovalores son las entradas de la diagonal: −1 tiene multiplicidad algebraica 1 y 3, multiplicidad
2. Resolviendo los correspondientes sistemas homogéneos se obtienen

𝐵𝐸−1 = {(0, 0, 1)},  𝐵𝐸3 = {(0, 1, 0)}.

La dimensión de 𝐸3 es 1 < 2: no es diagonalizable.

Ingeniería Informática · UFV  61
```

#### Página 62

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.27  Diagonalización de una matriz triangular
2025/26 · Ordinaria · Modelo B · Pregunta original 9

Sea
⎛ 2 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜0 2 0 ⎟
⎟
⎝0 0 3 ⎠
a) Obtén sus autovalores y sus multiplicidades algebraicas sin calcular determinantes.
b) Calcula una base del espacio propio del autovalor de multiplicidad algebraica 1.
c) ¿Es diagonalizable? Justifica la respuesta.

Respuesta
Los autovalores son las entradas de la diagonal: 3 tiene multiplicidad algebraica 1 y 2, multiplicidad
2. Resolviendo los correspondientes sistemas homogéneos se obtienen

𝐵𝐸3 = {(0, 0, 1)},  𝐵𝐸2 = {(1, 0, 0)}.

La dimensión de 𝐸2 es 1 < 2: no es diagonalizable.

6.28  Diagonalización de una matriz triangular
2025/26 · Ordinaria · Modelo C · Pregunta original 9

Sea
⎛ −1 1 0⎞
⎜
⎜  ⎟
⎟.
𝐴=⎜
⎜ 0 2 0⎟⎟
⎝ 0 0 2⎠
a) Obtén sus autovalores y sus multiplicidades algebraicas sin calcular determinantes.
b) Calcula una base del espacio propio del autovalor de multiplicidad algebraica 1.
c) ¿Es diagonalizable? Justifica la respuesta.

Respuesta
Los autovalores son las entradas de la diagonal: −1 tiene multiplicidad algebraica 1 y 2, multiplicidad
2. Resolviendo los correspondientes sistemas homogéneos se obtienen

𝐵𝐸−1 = {(1, 0, 0)},  𝐵𝐸2 = {(1, 3, 0), (0, 0, 1)}.

Las dimensiones de los espacios propios suman 1 + 2 = 3 y coinciden con las multiplicidades alge-
braicas: sí es diagonalizable.

Ingeniería Informática · UFV  62
```

#### Página 63

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

6.29  Verdadero o falso: repaso del tema
2024/25 · Ordinaria · Pregunta original 10 · Modelos A, B y C

Indica si cada afirmación es verdadera (V) o falsa (F). Las etiquetas A.n, B.n y C.n indican el modelo
y el apartado original.

A.9 La matriz 𝑃 que diagonaliza una matriz dada, 𝐷 = 𝑃−1 𝐴𝑃, es única.
A.10 Si una matriz es diagonalizable, entonces es regular.
B.9 Si 𝐴 es una matriz 𝑛 × 𝑛 con autovalor 𝜆 y autovector asociado 𝑥, todo múltiplo escalar de 𝑥
es también autovector de 𝐴.
B.10 Si 𝐴 es semejante a una matriz diagonalizable, entonces 𝐴 también es diagonalizable.
C.8 Si 𝐴 y 𝐵 son semejantes y 𝐵 es singular, 𝐴 también es singular.
C.9 Si 𝐴 y 𝐵 son matrices 𝑛 × 𝑛 semejantes, tienen los mismos autovectores.
C.10 Si 𝐴 es diagonalizable, sus columnas son linealmente independientes.

Respuesta

A.9 F. Pueden reordenarse o escalarse los autovectores, ajustando 𝐷 cuando corresponda.
A.10 F. La matriz nula es diagonal y singular.
B.9 F. El múltiplo 0𝑥 = 0 no es autovector. La afirmación sí vale para múltiplos por escalares no
nulos.
B.10 V. Si 𝐴 = 𝑆𝐵𝑆−1 y 𝐵 = 𝑃𝐷𝑃−1 , entonces 𝐴 = (𝑆𝑃)𝐷(𝑆𝑃)−1 .
C.8 V. La semejanza conserva el determinante.
C.9 F. Los autovectores se transforman mediante la matriz de semejanza; no tienen por qué coin-
cidir como vectores.
C.10 F. Una matriz diagonal con algún cero en la diagonal es diagonalizable y tiene columnas
dependientes.

Ingeniería Informática · UFV  63
```

#### Página 64

```text
Matemáticas para la Ingeniería I
Banco de preguntas de álgebra

Índice de procedencia
Correspondencia entre las preguntas originales y la numeración de este documento. Cada referencia
enlaza con su enunciado y respuesta.

2022/23 · Ordinaria · Modelo B
P1: 1.13 P2: 4.37  P3: 4.22 P4: 5.21  P5: 6.13

2022/23 · Ordinaria · Modelo C
P1: 1.14 P2: 4.38  P3: 4.23 P4: 5.22  P5: 6.14

2022/23 · Ordinaria · Modelo D
P1: 1.15 P2: 4.39  P3: 4.24 P4: 5.23  P5: 6.15

2023/24 · Ordinaria · Modelo A
P1: 4.13 P2: 1.4  P3: 5.9  P4: 4.25  P5: 5.1 P6: 6.8  P7: 6.16

2023/24 · Ordinaria · Modelo B
P1: 4.14 P2: 1.5  P3: 5.10  P4: 4.26 P5: 5.2 P6: 6.9  P7: 6.17

2023/24 · Ordinaria · Modelo C
P1: 4.15 P2: 1.6  P3: 5.11  P4: 4.27 P5: 5.3 P6: 6.10 P7: 6.18

2024/25 · Ordinaria · Modelo A
P1: 1.1 P2: 4.31 P3: 2.1 P4: 2.7 P5: 4.19 P6: 4.1 P7: 6.11 P8: 6.7  P9: 6.22  P10 [1, 2]: 1.16  P10 [3,
4]: 2.13 P10 [5, 6]: 4.40 P10 [7, 8]: 5.24 P10 [9, 10]: 6.29

2024/25 · Ordinaria · Modelo B
P1: 1.2 P2: 4.32 P3: 2.8 P4: 2.2 P5: 4.20 P6: 4.2 P7: 5.7  P8: 6.1  P9: 6.12  P10 [1, 2]: 1.16  P10 [3, 4]:
2.13 P10 [5, 6, 7]: 4.40 P10 [8]: 5.24 P10 [9, 10]: 6.29

2024/25 · Ordinaria · Modelo C
P1: 1.3 P2: 4.33 P3: 2.9 P4: 2.3 P5: 4.21 P6: 4.3 P7: 5.8  P8: 6.2  P9: 6.3  P10 [1, 2]: 1.16  P10 [3, 4]:
2.13 P10 [5, 6]: 4.40 P10 [7]: 5.24 P10 [8, 9, 10]: 6.29

2025/26 · Ordinaria · Modelo A
P1: 4.7 P2: 1.7  P3: 2.4  P4: 4.10  P5: 2.10 P6: 5.12 P7: 5.18 P8: 6.23  P9: 6.26

2025/26 · Ordinaria · Modelo B
P1: 4.8 P2: 1.8  P3: 2.5  P4: 4.11  P5: 2.11 P6: 5.13 P7: 5.19 P8: 6.24  P9: 6.27

2025/26 · Ordinaria · Modelo C
P1: 4.9 P2: 1.9  P3: 2.6  P4: 4.12  P5: 2.12 P6: 5.14 P7: 5.20 P8: 6.25  P9: 6.28

2025/26 · Extraordinaria · Modelo A
P1: 1.10 P2: 4.16  P3: 6.19 P4: 4.28  P5: 5.4  P6: 4.34 P7: 4.4  P8: 5.15  P9: 6.4

2025/26 · Extraordinaria · Modelo B
P1: 1.11 P2: 4.17  P3: 6.20 P4: 4.29  P5: 5.5  P6: 4.35 P7: 4.5  P8: 5.16  P9: 6.5

2025/26 · Extraordinaria · Modelo C
P1: 1.12 P2: 4.18  P3: 6.21 P4: 4.30  P5: 5.6  P6: 4.36 P7: 4.6  P8: 5.17  P9: 6.6

Ingeniería Informática · UFV  64
```
