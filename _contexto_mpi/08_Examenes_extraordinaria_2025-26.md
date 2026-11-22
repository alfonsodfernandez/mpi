# Exámenes convocatoria extraordinaria (CEX) 2025/26

Teórico (3 modelos con respuestas) y variantes de problemas prácticos MATLAB (GR = grafos; resto de siglas como en la ordinaria).

**Contenido de este archivo:**
- CEX · Teórico · Modelo A (con respuestas)
- CEX · Teórico · Modelo B (con respuestas)
- CEX · Teórico · Modelo C (con respuestas)
- CEX · DC01
- CEX · DC02.mlx
- CEX · DC03.mlx
- CEX · FR01.mlx
- CEX · FR02.mlx
- CEX · FR03.mlx
- CEX · GR01.mlx
- CEX · GR02.mlx
- CEX · GR03.mlx
- CEX · IP01.mlx
- CEX · IP02.mlx
- CEX · IP03.mlx
- CEX · LEO01.mlx
- CEX · LEO02.mlx
- CEX · LEO03.mlx
- CEX · MK01.mlx
- CEX · MK02.mlx
- CEX · MK03.mlx
- CEX · PR01.mlx
- CEX · PR02.mlx
- CEX · PR03.mlx
- CEX · Práctico · AR01
- CEX · Práctico · AR02
- CEX · Práctico · AR03


## CEX · Teórico · Modelo A (con respuestas)

*Fuente: `EXÁMENES/CEX/TEORICO/MPI1_2526_CEX_ModA_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Extraordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1h 45 min  Mod A

INSTRUCCIONES
•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en todas
ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo contrario la
puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Dado el sistema lineal
𝑥+𝑦 =2
F
𝑘𝑥 − 𝑦 = 1

a) (0,5 p) Escribe la matriz ampliada y aplica el método de Gauss para obtener la matriz escalonada, indicando
las operaciones y restricciones sobre 𝑘.
b) (0,5 p) Sin calcular determinantes ni usar el Teorema de Rouché-Fröbenius, determina razonadamente para
qué valores de 𝑘 el sistema tiene:
b.1) Una solución
b.2) Infinitas soluciones
b.3) No tiene solución

Respuesta

a)
1 1 2  1  1  2
O  P ~ 𝐹! − 𝑘𝐹" → 𝐹! ~ O  P
𝑘 −1 1  0 −1 − 𝑘 1 − 2𝑘
Si −1 − 𝑘 ≠ 0, el sistema tiene una solución única.
Si −1 − 𝑘 = 0, entonces 𝑘 = −1, sustituimos en la fila 2
1 1 2
O  P → sistema incompatible
0 0 3
b)
b.1) Si 𝑘 ≠ −1, el sistema tiene solución única.
b.2) Nunca hay infinitas soluciones (no hay fila nula completa).
b.3) Si 𝑘 = −1 , el sistema no tiene solución.
____________________________________________________________________________________________

Pregunta 2. Sea A una matriz cuadrada de orden 𝑛. Si al reducirla por Gauss obtenemos una forma
escalonada U con exactamente una fila nula:
a) (0,25p) ¿Qué puedes concluir sobre el valor de ∣A∣ (el determinante de A)?
b) (0,25p) ¿Es A invertible? ¿Por qué?
c) (0,5p) ¿Qué puedes afirmar sobre la naturaleza de la forma escalonada U (número de pivotes, rango,
dependencia lineal de columnas/filas) y sobre las implicaciones para el sistema lineal 𝐴𝒙 = 𝒃
(compatibilidad y número de soluciones) sin necesidad de calcular determinantes?
Respuesta
a) Si U tiene una fila nula, entonces al menos un elemento de la diagonal principal es cero.
Como |U| = u"" ∙ u!! … . u## , el producto será cero. Por tanto:
|U| = 0 ⟹ |A| = 0
b) Si ∣A∣=0, la matriz A no es invertible.
```

#### Página 2

```text
c)  Al tener la matriz escalonada equivalente (U) una fila nula, tendrá 𝑛 − 1 pivotes, lo mismo que su
rango, tendrá 𝑛 − 1 filas/columnas linealmente independientes y el sistema 𝐴𝒙 = 𝒃 no podrá ser
compatible determinado, podrá ser compatible indeterminado o incompatible dependiendo de 𝒃
____________________________________________________________________________________________

Pregunta 3. Sea una transformación lineal 𝑇: ℝ$ → ℝ$ , definida por:
𝑇(𝑥, 𝑦 , 𝑧) = (𝑥 + 𝑦, 2𝑦, 3𝑧)
a) (0,25p) Calcula la matriz A de la transformación de la base canónica.
b) (0,5p) Determina los autovalores y sus multiplicidades aritméticas
c) (0,75p) Calcula los autovectores asociados a cada autovalor.
Se tendrá en cuenta la simplicidad de operaciones para obtener la máxima puntuación

Respuesta.
a) La matriz A asociada a la base canónica se calcula mediante las imágenes por T de la base canónica de
ℝ$ ,es decir:

𝑇(1, 0, 0) = (1, 0, 0)
𝑇(0, 1, 0) = (1, 2, 0)
𝑇(0, 0, 1) = (0, 0, 3)
1 1 0
A = j0 2 0k
0 0 3
b) Los autovalores se obtienen de la diagonal principal al tratarse de una matriz triangular superior
1−λ  1  0
det(A − λI) = j 0  2−λ  0 k = (1 − λ)(2 − λ)(3 − λ)
0  0  3−λ
λ" = 1  𝑚% = 1
λ! = 2  𝑚% = 1
λ$ = 3  𝑚% = 1
c)
𝜆" = 1
0 1 0  0 1 0
𝐴 − 𝐼 = j0 1 0k ~ j0 0 0k
0 0 2  0 0 1

Tomamos como variable libre 𝑥 = 𝑡 y despejamos las otras:
𝑥=𝑡
𝑦=0
𝑧=0
Una base del subespacio propio está formada por 𝑣" = (1,0,0)

𝜆! = 2
−1 1 0  1 −1 0
𝐴 − 2𝐼 = j 0 0 0k ~ j0 0 0k
0 0 1  0 0 1
Tomamos como variable libre 𝑦 = 𝑡 y despejamos las otras:
𝑥=𝑡
𝑦=𝑡
𝑧=0
Una base del subespacio propio está formada por 𝑣! = (1,1,0)

λ$ = 3
−2 1 0  1 −1/2 0  1 0 0
𝐴 − 3𝐼 = j 0 −1 0k ~ j0  1  0k ~ j0 1 0k
0  0 0  0  0  0  0 0 0
```

#### Página 3

```text
Tomamos como variable libre 𝑧 = 𝑡 y despejamos las otras:
𝑥=0
𝑦=0
𝑧=𝑡
Una base del subespacio propio está formada por 𝑣$ = (0,0,1)
En resumen:
𝜆" = 1  𝑣" = (1,0,0)
𝜆! = 2  𝑣! = (1,1,0)
𝜆$ = 3  𝑣$ = (0,0,1)

____________________________________________________________________________________________

Pregunta 4. Dado 𝐵 = {𝒗" = (1,1,0), 𝒗! = (1,1,2), 𝒗$ = (1,2,3)}.
a) (0,5p) Determina si 𝐵 es una base de ℝ$ justificando las operaciones y sin calcular determinantes
b) (0,5p) En caso afirmativo, calcula las coordenadas del vector 𝒖 = (0, 1, 7) en dicha base, de lo contrario,
determina una combinación lineal entre ellos

Respuesta.

a) Un conjunto de vectores es una base si son un sistema generador de vectores linealmente independientes.
Como 𝐵 la forman 3 vectores de ℝ$ , basta comprobar que son linealmente independientes. Para ello, una
combinación lineal de ellos igualada al vector nulo debe tener como única solución la trivial:
1 1 1  𝜆"  0
𝜆" 𝒗" + 𝜆! 𝒗! + 𝜆$ 𝒗$ = 𝟎 ⟹ j1 1 2k · j𝜆! k = j0k
0 2 3  𝜆$  0

Para que tenga como única solución la trivial la matriz de coeficientes debe tener tres pivotes.
1 1 1  1 1 1  1 1 1
j1 1 2k ~ j0 0 1k ~ j0 2 3k
0 2 3  0 2 3  0 0 1
Por lo tanto, los vectores 𝒗" , 𝒗! y 𝒗$ son linealmente independientes y forman una base de ℝ$

b) Calculamos las coordenadas del vector 𝒖 = (0, 1, 7)

1 1 1  𝜆  0
(0, 1, 7) = 𝜆(1,1,0) + 𝜇(1,1,2) + 𝛾(1,2,3) ⟹ j1 1 2k · j𝜇k = j1k
0 2 3  𝛾  7

Resolviendo el sistema de ecuaciones:
1 1 1 0  1 1 1 0 1 1 1 0  1 1 1 0  1 1 1 0  1 0 1 −2  1 0 0 −3
j1 1 2 1k ~ j0 0 1 1k j0 2 3 7k ~ j0 2 0 4k ~ j0 1 0 2k ~ j0 1 0 2 k ~ j0 1 0 2 k
0 2 3 7  0 2 3 7 0 0 1 1  0 0 1 1  0 0 1 1  0 0 1 1  0 0 1 1

Las soluciones son; 𝜆 = −3, 𝜇 = 2 , 𝛾 = 1, luego las coordenadas del vector 𝒖 = (0, 1, 7) en base B son (−3, 2, 1)
____________________________________________________________________________________________

Pregunta 5. (1p) Escribe una matriz que represente una transformación lineal 𝑇: ℝ$ → ℝ& , que sea inyectiva y
explica por qué la transformación es inyectiva sin calcular determinantes.

Respuesta.

Como el espacio de partida es ℝ$ y el de llegada es ℝ& la matriz es de 4x3 de modo que al multiplicar
(transformar un vector de ℝ$ ) por una matriz de 3x1 se obtenga una matriz columna de 4x1 (vector de ℝ& )

Proponemos la matriz,
1  2  3
0  1  2
𝐴=~  •
0  0  1
0  0  0
```

#### Página 4

```text
Como el espacio de partida es ℝ$ , el rango máximo posible es 3. Por tanto, basta con que la matriz 𝐴 asociada
tenga 3 pivotes.
Para que 𝑇: ℝ$ → ℝ& sea inyectiva, debe cumplirse: 𝜈 = dim(𝐾𝑒𝑟 𝑇) = 0 y 𝜌 = dim(𝐼𝑚 𝑇) = 3
Por el teorema del rango: 𝜈 + 𝜌 = 3, es decir 𝜈 + 3 = 3 ⟹ 𝜈 = 0
La transformación es inyectiva porque su núcleo tiene dimensión cero, es decir, 𝐾𝑒𝑟 𝑇 = {0}.
____________________________________________________________________________________________

Pregunta 6. Sea el sistema homogéneo 𝐴𝒙 = 𝟎 con 𝐴 ∈ ℝ&×( y rg (𝐴) = 3.

a) (0,25p) Indica el número de ecuaciones y de incógnitas que tiene el sistema propuesto
b) (0,5p) Describe el conjunto solución desde el punto de vista algebraico, y determina la dimensión de dicho
conjunto solución.
c) (0,75p) Pon un ejemplo de matriz de coeficientes de un sistema de ecuaciones con esas características que
tenga al menos una solución no nula con exactamente tres componentes iguales a cero. Para demostrarlo
debes resolverlo y mostrar las respuestas

Respuesta

a) Dado que la matriz de coeficientes es de dimensiones 4x6, se trata de un sistema de 4 ecuaciones con 6
incógnitas.
b) El sistema es homogéneo, luego su conjunto solución es el núcleo de la matriz 𝐴:
nu 𝐴 = {𝑥 ∈ ℝ( : 𝐴𝒙 = 𝟎}
Es decir, el conjunto solución es un subespacio vectorial de ℝ( (que coincide con el espacio nulo de A)

Para hallar su dimensión, aplicamos el teorema rango–nulidad:

dim (nu 𝐴) + rg (𝐴) = 𝑛
donde 𝑛 es el número de incógnitas (columnas de 𝐴).

En este caso: 𝑛 = 6 y rg (𝐴) = 3. Por tanto:

dim (nu 𝐴) = 6 − 3 = 3
El conjunto solución tiene dimensión 3.
c) Un ejemplo de sistema de estas características vendrá dado por:
1 0 0 0 0 0
0 1 0 0 0 0
𝐴=‡  ˆ
0 0 1 0 0 0
1 1 1 0 0 0
Esta matriz de coeficientes se corresponde con el sistema homogéneo:
𝑥" = 0
𝑥! = 0
‰
𝑥$ = 0
𝑥" + 𝑥! + 𝑥$ = 0
Cuya solución es (𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥) , 𝑥( ) = (0,0,0, 𝛼, 𝛽, 𝛾), con 𝛼, 𝛽, 𝛾 ∈ ℝ, parámetros libres reales. Efectivamente,
un ejemplo de solución de este sistema con exactamente tres variables iguales a cero sería:
(𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥) , 𝑥( ) = (0,0,0,1,1,1).
Otro ejemplo, menos evidente, de sistema de estas características vendrá dado por:
1  0  0  1 1 1
0  1  0  2 −1 0
𝐴=‡  ˆ
0  0  1  3 0 1
1  1  0  3 0 1
Esta matriz de coeficientes se corresponde con el sistema homogéneo:
```

#### Página 5

```text
𝑥" + 𝑥& + 𝑥) + 𝑥( = 0
𝑥! + 2𝑥& − 𝑥) = 0
‰
𝑥$ + 3𝑥& + 𝑥( = 0
𝑥" + 𝑥! + 3𝑥& + 𝑥( = 0
Cuya solución es (𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥) , 𝑥( ) = (−𝛼 − 𝛽 − 𝛾, −2𝛼 + 𝛽, −3𝛼 − 𝛾, 𝛼, 𝛽, 𝛾), con 𝛼, 𝛽, 𝛾 ∈ ℝ, parámetros
libres reales. Un ejemplo de solución de este sistema con exactamente tres variables iguales a cero sería:
(𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥) , 𝑥( ) = (0,0,0,1,2, −3).
____________________________________________________________________________________________

Pregunta 7. Sea

H = {(x, y, z) ∈ ℝ$ : xy = 0}

1.  (0,25p) Justificar si el vector (𝑥, 𝑦, 𝑧) = (0, 0, 0) pertenece al conjunto.
2.  (0,5p) ¿Es 𝐻 un subespacio? Justifica tu respuesta con un contraejemplo y explica si es compatible este
resultado con lo que hayas afirmado en el apartado 1.

Respuesta

1.  El vector (𝑥, 𝑦, 𝑧) = (0,0,0) pertenece al conjunto, ya que ese vector tiene 𝑥 = 0 e 𝑦 = 0, que cumplen la
ecuación que define al conjunto: 𝑥𝑦 = 0.
2.  El conjunto no es un subespacio vectorial ya que, por ejemplo, no cumple la propiedad de cerradura de la
suma:
Sean 𝐮 = (1,0,0) ∈ H y 𝐯 = (0,1,0) ∈ H. Resulta que 𝐮 + 𝐯 = (1,1,0) cumple 𝐱 · 𝐲 = 1 ≠ 0, luego 𝐮 + 𝐯 ∉ H.

____________________________________________________________________________________________

Pregunta 8. Sea 𝑇: ℝ$ → ℝ! dada por:
𝑇(𝑥, 𝑦, 𝑧) = (𝑥 + 𝑧, 𝑥 + 𝑦)
a) (0,5p) Halla una base de nu(𝑇) y su dimensión.
b) (0,5p) Halla una base de Im(𝑇) y su dimensión.
c) (0,25p) ¿Es 𝑇 sobreyectiva? Razona tu respuesta.

𝑛𝑢(𝑇) = espacio nulo de T

Respuesta

a) nu(𝑇) = {𝑣 ∈ ℝ$ / 𝑇(𝑣) = 0} = {𝑣 ∈ ℝ$ / 𝑥 + 𝑧 = 0, 𝑥 + 𝑦 = 0} = {(𝛼, −𝛼, −𝛼) ∈ ℝ$ , 𝛼 ∈ ℝ}
La dimensión de este subespacio es 1 (su forma paramétrica tiene un solo parámetro), y las bases estarán
formadas por un único vector, por ejemplo {(1, −1, −1)}.
b) La matriz asociada de la Transformación Lineal se puede obtener fácilmente calculando las imágenes de los
vectores de la base canónica de ℝ$ :
𝑇(1, 0, 0) = (1, 1)
𝑇(0, 1, 0) = (0, 1)
𝑇(0, 0,1) = (1, 0)

1 0 1
𝐴=”  •
1 1 0
El subespacio imagen de la transformación es el espacio generado por las columnas de A. Una base de dicho
subespacio será cualquier conjunto libre contenido en ese conjunto generador, por ejemplo {(1,0), (0,1)}.
c) El espacio generado por la base descrita en el punto anterior es, precisamente, ℝ! (el espacio de llegada de
la transformación lineal), por lo que la transformación es sobreyectiva.
____________________________________________________________________________________________
```

#### Página 6

```text
Pregunta 9. Sea la transformación lineal 𝑇: ℝ! → ℝ! dada por:
𝑇(𝑥, 𝑦) = (2𝑥 + 𝑦, 2𝑦)
a) (0,5p) Obtener el conjunto de vectores que se transforman en una versión escalada de sí mismos.
b) (0,5p) ¿Cuál es ese factor de escala? ¿Qué estructura algebraica es dicho conjunto?

Respuesta

Lo que se está pidiendo en este ejercicio son los autovectores, y correspondientes autovalores, de la matriz de la
transformación. Dicha matriz en la base canónica de ℝ! es:
2 1
𝐴=”  •
0 2
Como se trata de una matriz triangular con diagonal 2, su único autovalor es 𝜆 = 2 (tiene multiplicidad
algebraica 2).
Este autovalor 𝜆 = 2 es el factor de escala pedido en el enunciado.
(𝐴 − 𝜆 · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 2𝐼) · 𝑣 = 0
0 1  𝑥  0
”  • · ”𝑦 • = ” •
0 0  0
La solución de este sistema es (𝑥, 𝑦) = (𝛼, 0), con parámetro libre 𝛼 ∈ ℝ.
Así, el espacio propio asociado al autovalor 𝜆 = 2 es 𝐸* = {(𝑥, 𝑦) = (𝛼, 0) ∈ ℝ! , 𝛼 ∈ ℝ}. Este es el conjunto
pedido en el enunciado, de los vectores que se transforman en una versión escalada de sí mismos. Este
conjunto es un subespacio vectorial de ℝ! .
Efectivamente, para cualquier vector 𝑣 ∈ 𝐸* , se cumplirá que: 𝑇(𝑣) = 𝜆 · 𝑣.
____________________________________________________________________________________________
```


## CEX · Teórico · Modelo B (con respuestas)

*Fuente: `EXÁMENES/CEX/TEORICO/MPI1_2526_CEX_ModB_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Extraordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1h 45min  Mod B

INSTRUCCIONES
•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en
todas ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo
contrario la puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Dado el sistema lineal
𝑥+𝑦 =2
!𝑥 + 𝑘𝑦 = 1

a) (0,5 p) Escribe la matriz ampliada y aplica el método de Gauss para obtener la matriz escalonada, indicando
las operaciones y restricciones sobre 𝑘.
b) (0,5 p) Sin calcular determinantes ni usar el Teorema de Rouché-Fröbenius, determina razonadamente para
qué valores de 𝑘 el sistema tiene:
b.1) Una solución
b.2) Infinitas soluciones
b.3) No tiene solución

Respuesta

a)
1 1  2  1  1  2
)1 𝑘  ~ 𝐹! − 𝐹" → 𝐹! ~ )
1*  0 𝑘 − 1 −1*
.

b)
b.1) Si 𝑘 − 1 ≠ 0 → 𝑘 ≠ 1, el sistema tiene una solución única.
b.2) Nunca hay infinitas soluciones (no hay fila nula completa).
b.3) Si 𝑘 − 1 = 0 → 𝑘 = 1, el sistema es incompatible y no tiene solución
.
____________________________________________________________________________________________

Pregunta 2. Sea A una matriz cuadrada de orden 𝑛. Si al reducirla por Gauss obtenemos una forma
escalonada U en la que la última fila no es nula:
a) (0,25p) ¿Qué puedes concluir sobre el valor de ∣A∣ (el determinante de A)?
b) (0,25p) ¿Es A invertible? ¿Por qué?
c) (0,5p) ¿Qué puedes afirmar sobre la naturaleza de la forma escalonada U (número de pivotes, rango,
dependencia lineal de columnas/filas) y sobre las implicaciones para el sistema lineal 𝐴𝒙 = 𝒃
(compatibilidad y número de soluciones) sin necesidad de calcular determinantes?
Respuesta
a) Si la última fila de U no es nula, entonces U tiene n pivotes
b) Como |U| = u"" ∙ u!! … . u## , el producto no será cero. Por tanto: |U| ≠ 0 ⟹ |A| ≠ 0
Si ∣ 𝐴 ∣≠ 0, la matriz A es invertible.
c) Al tener la matriz escalonada equivalente (U) la última fila no nula, tendrá 𝑛 pivotes, lo mismo que su
rango, tendrá 𝑛 filas/columnas linealmente independientes y el sistema 𝐴𝒙 = 𝒃 será compatible
determinado.
```

#### Página 2

```text
____________________________________________________________________________________________

Pregunta 3. Sea una transformación lineal 𝑇: ℝ$ → ℝ$ , definida por:
𝑇(𝑥, 𝑦 , 𝑧) = (𝑥 − 𝑦, 𝑦 + 𝑧, −𝑧)
a)  (0,25p) Calcula la matriz A de la transformación de la base canónica.
b)  (0,5p) Determina los autovalores y sus multiplicidades aritméticas
c)  (0,5p) Calcula una base del subespacio propio de cada autovalor
d)  (0,25p) Determina razonadamente si la matriz A es diagonalizable
Se tendrá en cuenta la simplicidad de operaciones para obtener la máxima puntuación

Respuesta.
a) La matriz A asociada a la base canónica se calcula mediante las imágenes por T de la base canónica de
ℝ$ ,es decir:

𝑇(1, 0, 0) = (1, 0, 0)
𝑇(0, 1, 0) = (−1, 1, 0)
𝑇(0, 0, 1) = (0, 1, −1)
1 −1 0
A= 0 1  1
V0 0 −1W

b) Los autovalores se obtienen de la diagonal principal al tratarse de una matriz triangular superior
1 − λ −1  0
det(A − λI) = 0  1−λ  1  = (−1 − λ)(1 − λ)!
V 0  0 −1 − λW
λ" = 1  𝑚% = 2
λ! = −1  𝑚% = 1
c)
𝜆" = 1
0 −1 0  0 1 0
𝐴−𝐼 = 0 0  1 ~ 0 0 1
V0 0 −2W V0 0 0W

Tomamos como variable libre 𝑥 = 𝑡 y despejamos las otras:
𝑥=𝑡
𝑦=0
𝑧=0
Una base del subespacio propio está formada por 𝑣" = (1,0,0)

𝜆! = −1
2 −1 0  1 −1/2  0
𝐴+𝐼 = 0 2 1 ~ 0  1  1/2
V0 0 0W V  W
0  0  0
Tomamos como variable libre 𝑧 = 𝑡 y despejamos las otras:
𝑥 = −𝑡/4
𝑦 = −𝑡/2
𝑧=𝑡
Una base del subespacio propio está formada por 𝑣! = (−1, −2,4)

En resumen:  Comentado [RVB1]:
𝜆" = 1  𝑚% = 2  𝑣" = (1,0,0)
𝜆! = −1  𝑚% = 1  𝑣! = (−1, −2, 4)

d) A no es diagonalizable ya que la dimensión del subespacio propio del autovalor 𝜆" = 1 es 1 mientras
que su multiplicidad aritmética es 2
```

#### Página 3

```text
____________________________________________________________________________________________

Pregunta 4. Dado 𝐵 = {𝒗" = (−1, 2, 1), 𝒗! = (0, 1, −3), 𝒗$ = (1, 2, 3)}.

a) (0,5p) Determina si 𝐵 es una base de ℝ$ justificando las operaciones y sin calcular determinantes
b) (0,5p) En caso afirmativo, calcula las coordenadas del vector 𝒖 = (2, 10, 4) en dicha base, de lo contrario,
determina una combinación lineal entre ellos

Respuesta.

a) Un conjunto de vectores es una base si son un sistema generador de vectores linealmente independientes.
Como 𝐵 la forman 3 vectores de ℝ$ , basta comprobar que son linealmente independientes. Para ello, una
combinación lineal de ellos igualada al vector nulo debe tener como única solución la trivial:
−1 0 1  𝜆"  0
𝜆" 𝒗" + 𝜆! 𝒗! + 𝜆$ 𝒗$ = 𝟎 ⟹ 2  1 2 · 𝜆! = 0
V 1 −3 3W V𝜆 W V0W
$

Para que tenga como única solución la trivial la matriz de coeficientes debe tener tres pivotes.
−1 0 1  −1 0 1  1 1 1
2  1 2 ~ 0  1 4 ~ 0 1 4
V 1 −3 3W V 0 −3 4W V0 0 16W

El sistema es compatible determinado por lo que únicamente tiene por solución la trivial y los vectores 𝒗" , 𝒗!
y 𝒗$ son linealmente independientes y forman una base de ℝ$

b) Calculamos las coordenadas del vector 𝒖 = (2, 10, 4)

−1 0 1  𝜆  2
(2, 10, 4) = 𝜆(−1, 2, 1) + 𝜇(0, 1, −3) + 𝛾 (1,2,3) ⟹ V 2  1 2 · 𝜇 = 10
W V𝛾 W V W
1 −3 3  4

Resolviendo el sistema de ecuaciones:
−1 0 1 2  −1 0 1 1  1 0 −1 −1  1 0 −1 −1
2  1 2 10 ~ 0  1 4 14 ~ 0 1 4 12 ~ 0 1 4 12
V 1 −3 3 4 W V 0 −3 4 6 W V0 0 16 48 W V0 0 1  3W

Las soluciones son; 𝜆 = 1, 𝜇 = 2 , 𝛾 = 3, luego las coordenadas del vector 𝒖 = (2, 10, 4) en base B son (1, 2, 3)
____________________________________________________________________________________________

Pregunta 5. (1p) Escribe una matriz que represente una transformación lineal 𝑇: ℝ& → ℝ$ , que sea sobreyectiva
y explica por qué la transformación es sobreyectiva sin calcular determinantes.

Respuesta.

Como el espacio de partida es ℝ& y el de llegada es ℝ$ la matriz es de 3x4 de modo que al multiplicar
(transformar un vector de ℝ& ) por una matriz de 4x1 se obtenga una matriz columna de 3x1 (vector de ℝ$ )

Proponemos la matriz,
1 2 3 4
𝐴= 0 1 2 3
V  W
0 0 1 2

Como el espacio de llegada es ℝ$ , el rango máximo posible es 3 cuando la matriz 𝐴 asociada tenga 3 pivotes,
como la que se propone.
Para que 𝑇: ℝ& → ℝ$ sea sobreyectiva, debe cumplirse: dim(𝐼𝑚 𝑇) = 3 = 𝑟𝑎𝑛𝑔𝑜(𝐴) = dim (ℝ$ )
La transformación es sobreyectiva porque dim(𝐼𝑚 𝑇) = dim (ℝ$ )
____________________________________________________________________________________________
```

#### Página 4

```text
Pregunta 6. Sea el sistema homogéneo 𝐴𝒙 = 𝟎 con 𝐴 ∈ ℝ'×) y rg (𝐴) = 4.

a) (0,25p) Indica el número de ecuaciones y de variables que tiene el sistema propuesto
b) (0,5p) Describe el conjunto solución desde el punto de vista algebraico, y determina la dimensión de dicho
conjunto solución.
c) (0,75p) Pon un ejemplo de matriz de coeficientes de un sistema de ecuaciones con esas características que
tenga al menos una solución no nula con exactamente tres componentes iguales a cero. Para demostrarlo
debes resolverlo y mostrar las respuestas

Respuesta

a) Dado que la matriz de coeficientes es de dimensiones 5x7, se trata de un sistema de 5 ecuaciones con 7
variables.
b) El sistema es homogéneo, luego su conjunto solución es el núcleo de la matriz 𝐴:
nu 𝐴 = {𝑥 ∈ ℝ) : 𝐴𝒙 = 𝟎}
Es decir, el conjunto solución es un subespacio vectorial de ℝ) .

Para hallar su dimensión, aplicamos el teorema rango–nulidad:

dim (nu 𝐴) + rg (𝐴) = 𝑛
donde 𝑛 es el número de incógnitas (columnas de 𝐴).
En este caso: 𝑛 = 7 y rg (𝐴) = 4. Por tanto:

dim (nu 𝐴) = 7 − 4 = 3
El conjunto solución tiene dimensión 3.
c) Un ejemplo de sistema de estas características vendrá dado por:
1 0 0 0 0 0 0
0 1 0 0 0 0 0
𝐴 = ⎛ 0 0 1 0 0 0 0⎞
⎜0 0 0 1 −1 0 0⎟
0 0 0 0 0 0 0
⎝  ⎠
Esta matriz de coeficientes se corresponde con el sistema homogéneo:
𝑥" = 0
𝑥! = 0
|𝑥$ = 0
𝑥& − 𝑥' = 0
Cuya solución es (𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥' , 𝑥* , 𝑥) ) = (0,0,0, 𝛼, 𝛼, 𝛽, 𝛾), con 𝛼, 𝛽, 𝛾 ∈ ℝ, parámetros libres reales.
Efectivamente, un ejemplo de solución de este sistema con exactamente tres variables iguales a cero sería:
(𝑥" , 𝑥! , 𝑥$ , 𝑥& , 𝑥' , 𝑥* , 𝑥) ) = (0,0,0,1,1,1,1).
____________________________________________________________________________________________

Pregunta 7. Sea

H = {(x, y, z) ∈ ℝ$ : 2xy = 0}

1.  (0,25p) Justificar si el vector (𝑥, 𝑦, 𝑧) = (0, 0, 0) pertenece al conjunto.
2.  (0,5p) ¿Es 𝐻 un subespacio? Justifica tu respuesta con un contraejemplo y explica si es compatible este
resultado con lo que hayas afirmado en el apartado 1.

Respuesta
```

#### Página 5

```text
1.  El vector (𝑥, 𝑦, 𝑧) = (0,0,0) pertenece al conjunto, ya que ese vector tiene 𝑥 = 0 e 𝑦 = 0, que cumplen la
ecuación que define al conjunto: 2𝑥𝑦 = 0.
2.  El conjunto no es un subespacio vectorial ya que, por ejemplo, no cumple la propiedad de cerradura de la
suma:

Sean 𝐮 = (1,0,0) ∈ H y 𝐯 = (0,1,0) ∈ H. Resulta que 𝐮 + 𝐯 = (1,1,0) que resulta que cumple que:

2xy = 2 ≠ 0, luego 𝐮 + 𝐯 ∉ H.

____________________________________________________________________________________________

Pregunta 8. Sea 𝑇: ℝ$ → ℝ! dada por:
𝑇(𝑥, 𝑦, 𝑧) = (2𝑥 + 𝑦, 𝑥 − 2𝑧)
a) (0,5p) Halla una base de nu(𝑇) y su dimensión.
b) (0,5p) Halla una base de Im(𝑇) y su dimensión.
c) (0,25p) ¿Es 𝑇 sobreyectiva? Razona tu respuesta.

𝑛𝑢(𝑇) = espacio nulo de T

Respuesta

a) nu(𝑇) = {𝑣 ∈ ℝ$ / 𝑇(𝑣) = 0} = {𝑣 ∈ ℝ$ , 2𝑥 + 𝑦 = 0, 𝑥 − 2𝑧 = 0}
Resolvemos el sistema lineal homogéneo:
2𝑥 + 𝑦 = 0  2 1 0  1 0 −2  1 0 −2
‡ 𝑥 − 2𝑧 = 0 ⟹ )1 0 −2* ~ )2 1 0 * ~ )0 1 4 *
Tomamos como variable libre 𝑧 = 𝑡 y despejando las otras dos:
𝑥 = 2𝑡  𝑥  2
𝑦 = −4𝑡 ⟹ 𝑦 = 𝑡 · −4
ˆ 𝑧=𝑡  ‰𝑧 Š  V1W
La dimensión de este subespacio es 1 (su forma paramétrica tiene un solo parámetro), y las bases estarán
formadas por un único vector, por ejemplo {(2, −4,1)}.
b) La matriz asociada de la Transformación Lineal se puede obtener fácilmente calculando las imágenes de los
vectores de la base canónica de ℝ$ :
𝑇(1, 0, 0) = (2, 1)
𝑇(0, 1, 0) = (1, 0)
𝑇(0, 0,1) = (0, −2)

2 1 0
𝐴=‹
1 0 −2Œ
El subespacio imagen de la transformación es el espacio generado por las columnas de A.
2 1 0  1 0 −2  1 0 −2
‹1 0 −2Œ ~ ‹2 1 0 Œ ~ ‹0 1 4 Œ
Una base de dicho subespacio será cualquier conjunto libre contenido en ese conjunto generador, por ejemplo
{(1,0), (0,1)}.
c) El espacio generado por la base descrita en el punto anterior es, precisamente, ℝ! (el espacio de llegada de
la transformación lineal), por lo que la transformación es sobreyectiva.
____________________________________________________________________________________________

Pregunta 9. Sea la transformación lineal 𝑇: ℝ! → ℝ! dada por:
𝑇(𝑥, 𝑦) = (−𝑥, 2𝑥 − 𝑦)
a) (0,5p) Obtener el conjunto de vectores que se transforman en una versión escalada de sí mismos.
b) (0,5p) ¿Cuál es ese factor de escala? ¿Qué estructura algebraica es dicho conjunto?

Respuesta
```

#### Página 6

```text
Lo que se está pidiendo en este ejercicio son los autovectores, y correspondientes autovalores, de la matriz de la
transformación. Dicha matriz en la base canónica de ℝ! es:
𝑇(1, 0) = (−1, 2)
𝑇(0, 1) = (0, −1)
−1 0
𝐴=‹
2 −1Œ
Como se trata de una matriz triangular con diagonal −1, su único autovalor es 𝜆 = −1 (tiene multiplicidad
algebraica 2).
Este autovalor 𝜆 = −1 es el factor de escala pedido en el enunciado.
(𝐴 − 𝜆 · 𝐼 ) · 𝑣 = 0 ⇒ (𝐴 + 𝐼 ) · 𝑣 = 0
0 0  𝑥  0
‹2 0Œ · ‹𝑦Œ = ‹0Œ
La solución de este sistema es (𝑥, 𝑦) = (0, 𝛼 ), con parámetro libre 𝛼 ∈ ℝ.
Así, el espacio propio asociado al autovalor 𝜆 = −1 es 𝐸+ = {(𝑥, 𝑦) = (0, 𝛼) ∈ ℝ! , 𝛼 ∈ ℝ}. Este es el conjunto
pedido en el enunciado, de los vectores que se transforman en una versión escalada de sí mismos. Este
conjunto es un subespacio vectorial de ℝ! .
Efectivamente, para cualquier vector 𝑣 ∈ 𝐸+ , se cumplirá que: 𝑇(𝑣 ) = 𝜆 · 𝑣.
____________________________________________________________________________________________
```


## CEX · Teórico · Modelo C (con respuestas)

*Fuente: `EXÁMENES/CEX/TEORICO/MPI1_2526_CEX_ModC_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Extraordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1 h 45 min  Mod C

INSTRUCCIONES
•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en
todas ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo
contrario la puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Dado el sistema lineal
−𝑘𝑥 + 𝑦 = 2
!
𝑥 + 𝑘𝑦 = 1

a) (0,5 p) Escribe la matriz ampliada y aplica el método de Gauss para obtener la matriz escalonada, indicando
las operaciones y restricciones sobre 𝑘.
b) (0,5 p) Sin calcular determinantes ni usar el Teorema de Rouché-Fröbenius, determina razonadamente para
qué valores de 𝑘 el sistema tiene:
b.1) Una solución
b.2) Infinitas soluciones
b.3) No tiene solución

Respuesta

a)
1  1 𝑘  1
−𝑘  1  2  1  𝑘  1  1  𝑘  1  2+𝑘5
*  + 𝐹 ↔ 𝐹" ~ *  + 𝐹 + 𝑘𝐹! → 𝐹" ~ *  + ~𝐹" → 2  3 𝐹 ~ 4
1  𝑘  1 !  −𝑘  1  2 "  0 1 + 𝑘"  2+𝑘  1 + 𝑘" " 0 1
1 + 𝑘"
.

b) Como 1 + 𝑘 " no puede anularse
b.1) El sistema tiene una solución única para cualquier valor de 𝑘.
b.2) Nunca hay infinitas soluciones (no hay fila nula completa).
b.3) No puede ser incompatible tampoco
.
____________________________________________________________________________________________

Pregunta 2. Sea A una matriz cuadrada de orden 𝑛 > 2. Si al reducirla por Gauss obtenemos una forma
escalonada U en la que las dos últimas filas son nulas (las demás no):
a) (0,25p) ¿Qué puedes concluir sobre el valor de ∣A∣ (el determinante de A)?
b) (0,25p) ¿Es A invertible? ¿Por qué?
c) (0,5p) ¿Qué puedes afirmar sobre la naturaleza de la forma escalonada U (número de pivotes, rango,
dependencia lineal de columnas/filas) y sobre las implicaciones para el sistema lineal 𝐴𝒙 = 𝒃
(compatibilidad y número de soluciones) sin necesidad de calcular determinantes?
Respuesta
a) Si las dos últimas filas de U son nulas, entonces U tiene 𝑛 − 2 pivotes
Como |U| = u!! ∙ u"" … . u## , el producto será cero. Por tanto: |U| = 0 ⟹ |A| = 0

b) Si ∣ 𝐴 ∣= 0, la matriz A no es invertible.
```

#### Página 2

```text
b) Al tener la matriz escalonada equivalente (U) las dos últimas filas nulas, tendrá 𝑛 − 2 pivotes, lo
mismo que su rango, tendrá 𝑛 − 2 filas/columnas linealmente independientes y el sistema 𝐴𝒙 = 𝒃 será
compatible indeterminado o incompatible dependiendo del vector 𝒃
____________________________________________________________________________________________

Pregunta 3. Sea una transformación lineal 𝑇: ℝ$ → ℝ$ , definida por:
𝑇(𝑥, 𝑦 , 𝑧) = (2𝑥 + 𝑦, 𝑦 − 2𝑧, 3𝑧)
a)  (0,25p) Calcula la matriz A de la transformación de la base canónica.
b)  (0,5p) Determina los autovalores y sus multiplicidades aritméticas
c)  (0,5p) Calcula una base del subespacio propio de cada autovalor
d)  (0,25p) Determina razonadamente si la matriz A es diagonalizable
Se tendrá en cuenta la simplicidad de operaciones para obtener la máxima puntuación

Respuesta.
a) La matriz A asociada a la base canónica se calcula mediante las imágenes por T de la base canónica de
ℝ$ ,es decir:

𝑇(1, 0, 0) = (2, 0, 0)
𝑇(0, 1, 0) = (1, 1, 0)
𝑇(0, 0, 1) = (0, −2, 3)
2 1 0
A = 40 1 −25
0 0 3

b) Los autovalores se obtienen de la diagonal principal al tratarse de una matriz triangular superior

λ! = 3  𝑚% = 1
λ" = 2  𝑚% = 1
λ$ = 1  𝑚% = 1
c)
𝜆! = 3
−1 1  0  1 −1 0
𝐴 − 3𝐼 = 4 0 −2 −25 ~ 40 1 15
0 0  0  0 0 0

Tomamos como variable libre 𝑧 = 𝑡 y despejamos las otras:
𝑥 = −𝑡
𝑦 = −𝑡
𝑧=𝑡
Una base del subespacio propio está formada por 𝑣! = (−1, −1, 1)

𝜆" = 2
0 1  0  0 1 0
𝐴 − 2𝐼 = 40 −1 −25 ~ 40 0 15
0 0  1  0 0 0
Tomamos como variable libre 𝑥 = 𝑡 y despejamos las otras:
𝑥=𝑡
𝑦=0
𝑧=0
Una base del subespacio propio está formada por 𝑣" = (1, 0, 0)

𝜆$ = 1
1 1 0  1 1 0
𝐴 − 𝐼 = 40 0 −25 ~ 40 0 15
0 0 2  0 0 0
Tomamos como variable libre 𝑦 = 𝑡 y despejamos las otras:
```

#### Página 3

```text
𝑥 = −𝑡
𝑦=𝑡
𝑧=0
Una base del subespacio propio está formada por 𝑣$ = (−1, 1, 0)

En resumen:
𝜆! = 3  𝑚% = 1  𝑣! = (−1, −1, 1)
𝜆" = 2  𝑚% = 1  𝑣" = (1, 0, 0)
𝜆$ = 1  𝑚% = 1  𝑣$ = (−1, 1, 0)

d) A es diagonalizable ya que las dimensiones de los subespacios propios coinciden con
las multiplicidades aritméticas de los autovalores correspondientes
____________________________________________________________________________________________

Pregunta 4. Dado 𝐵 = {𝒗! = (3, 2, 1), 𝒗" = (0, 1, −1), 𝒗$ = (1, −2, 3)}.

a) (0,5p) Determina si 𝐵 es una base de ℝ$ justificando las operaciones y sin calcular determinantes
b) (0,5p) En caso afirmativo, calcula las coordenadas del vector 𝒖 = (2, 10, 4) en dicha base, de lo contrario,
determina una combinación lineal entre ellos

Respuesta.

a) Un conjunto de vectores es una base si son un sistema generador de vectores linealmente independientes.
Como 𝐵 la forman 3 vectores de ℝ$ , basta comprobar que son linealmente independientes. Para ello, una
combinación lineal de ellos igualada al vector nulo debe tener como única solución la trivial:
3 0  1  𝜆!  0
𝜆! 𝒗! + 𝜆" 𝒗" + 𝜆$ 𝒗$ = 𝟎 ⟹ 42 1 −25 · 4𝜆" 5 = 405
1 −1 3  𝜆$  0

Para que tenga como única solución la trivial la matriz de coeficientes debe tener tres pivotes.
3 0  1  1 −1 3  1 −1 3  1 −1 3
42 1 −25 ~ 42 1 −25 ~ 40 3 −85 ~ 40 3 −85
1 −1 3  3 0  1  0 3 −8  0 0  0

Por lo tanto, los vectores 𝒗! , 𝒗" y 𝒗$ no son linealmente independientes y no forman una base de ℝ$

b) A la vista de la matriz escalonada obtenida podemos decir que existe una combinación entre ellos:
1 −1 3  ⎡1 0  ⎤
1 −1 3  8 ⎢  3 ⎥
40 3 −85 ~ [0 1 − \ ~ ⎢  8
0 0  0  3
⎢0 1 − ⎥⎥
0 0  0  3
⎣0 0 0 ⎦
Se observa que:
1  8
𝑣$ = 𝑣! − 𝑣"
3  3
1  8
(1, −2, 3) = (3, 2, 1) − (0, 1, −1)
3  3
____________________________________________________________________________________________

Pregunta 5. (1p) Escribe una matriz (no identidad) que represente una transformación lineal 𝑇: ℝ& → ℝ& , que
sea biyectiva y explica por qué la transformación es biyectiva sin calcular determinantes.

Respuesta.

Como el espacio de partida es ℝ& y el de llegada es ℝ& la matriz es de 4x4 de modo que al multiplicar
(transformar un vector de ℝ& ) por una matriz de 4x1 se obtenga una matriz columna de 4x1 (vector de ℝ& )

Proponemos la matriz,
```

#### Página 4

```text
1  2  3  4
0  1  2  3
𝐴=[  \
0  0  1  2
0  0  0  1

Como el espacio de legada es ℝ& , el rango máximo posible es 4 cuando la matriz 𝐴 asociada tenga 4 pivotes,
como la que se propone.
Para que 𝑇: ℝ& → ℝ& sea biyectiva basta que sea inyectiva. En el ejemplo aportado, por el teorema del rango:
dim (𝐼𝑚(𝑇)) + dim (𝐾𝑒𝑟(𝑇)) = dim (ℝ& ) Dado que 𝑟𝑔(𝐴) = dimj𝐼𝑚(𝑇)k = 4 = dim (ℝ& ) se deduce que
dim (𝐾𝑒𝑟(𝑇)) = 0, por tanto, T es inyectiva
Dado que se trata de que T es un endomorfismo, al ser inyectivo, es sobreyectivo y, por tanto, biyectivo
____________________________________________________________________________________________

Pregunta 6. Sea el sistema homogéneo 𝐴𝒙 = 𝟎 con 𝐴 ∈ ℝ'×) y rg (𝐴) = 4.

a) (0,25p) Indica el número de ecuaciones y de variables que tiene el sistema propuesto
b) (0,5p) Describe el conjunto solución desde el punto de vista algebraico, y determina la dimensión de dicho
conjunto solución.
c) (0,75p) Pon un ejemplo de matriz de coeficientes de un sistema de ecuaciones con esas características que
tenga al menos una solución no nula con exactamente tres componentes iguales a cero. Para demostrarlo
debes resolverlo y mostrar las respuestas

Respuesta

a) Dado que la matriz de coeficientes es de dimensiones 6x5, se trata de un sistema de 6 ecuaciones con 5
variables.
b) El sistema es homogéneo, luego su conjunto solución es el núcleo de la matriz 𝐴:
nu 𝐴 = {𝑥 ∈ ℝ) : 𝐴𝒙 = 𝟎}
Es decir, el conjunto solución es un subespacio vectorial de ℝ) .
Para hallar su dimensión, aplicamos el teorema rango–nulidad:

dim (nu 𝐴) + rg (𝐴) = 𝑛
donde 𝑛 es el número de incógnitas (columnas de 𝐴).

En este caso: 𝑛 = 5 y rg (𝐴) = 4. Por tanto:

dim (nu 𝐴) = 5 − 4 = 1
El conjunto solución tiene dimensión 1.
c) Un ejemplo de sistema de estas características vendrá dado por:
1 0 0 0 0
0 1 0 0 0
⎛  ⎞
0 0 1 0 0
𝐴=⎜
⎜0 0 0 1 −1⎟  ⎟
0 0 0 0 0
⎝0 0 0 0 0 ⎠
Esta matriz de coeficientes se corresponde con el sistema homogéneo:
𝑥! = 0
𝑥" = 0
w
𝑥$ = 0
𝑥& − 𝑥) = 0
Cuya solución es (𝑥! , 𝑥" , 𝑥$ , 𝑥& , 𝑥) ) = (0,0,0, 𝛼, 𝛼), con 𝛼 ∈ ℝ, parámetros libres reales. Efectivamente, un
ejemplo de solución de este sistema con exactamente tres variables iguales a cero sería: (𝑥! , 𝑥" , 𝑥$ , 𝑥& , 𝑥) ) =
(0,0,0,1,1).
____________________________________________________________________________________________
```

#### Página 5

```text
Pregunta 7. Sea

H = {(x, y, z) ∈ ℝ$ : 𝑥 " + 𝑦 " ≤ 1}

1.  (0,25p) Justificar si el vector (𝑥, 𝑦, 𝑧) = (0, 0, 0) pertenece al conjunto.
2.  (0,5p) ¿Es 𝐻 un subespacio? Justifica tu respuesta con un contraejemplo y explica si es compatible este
resultado con lo que hayas afirmado en el apartado 1.

Respuesta

1.  El vector (𝑥, 𝑦, 𝑧) = (0,0,0) pertenece al conjunto, ya que ese vector tiene 𝑥 = 0 e 𝑦 = 0, que cumplen la
ecuación que define al conjunto: 𝑥 " + 𝑦 " = 0 ≤ 1.
2.  El conjunto no es un subespacio vectorial ya que, por ejemplo, no cumple la propiedad de cerradura de la
suma:
Sean 𝐮 = (1,0,0) ∈ H y 𝐯 = (0,1,0) ∈ H. Resulta que 𝐮 + 𝐯 = (1,1,0) que no cumple 𝑥 " + 𝑦 " = 2 ≰ 1

____________________________________________________________________________________________

Pregunta 8. Sea 𝑇: ℝ$ → ℝ" dada por:
𝑇(𝑥, 𝑦, 𝑧) = (𝑥 + 2𝑦, 2𝑥 − 𝑧)
a) (0,5p) Halla una base de nu(𝑇) y su dimensión.
b) (0,5p) Halla una base de Im(𝑇) y su dimensión.
c) (0,25p) ¿Es 𝑇 sobreyectiva? Razona tu respuesta.

𝑛𝑢(𝑇) = espacio nulo de T

Respuesta

a) nu(𝑇) = {𝑣 ∈ ℝ$ / 𝑇(𝑣) = 0} = {𝑣 ∈ ℝ$ , 𝑥 + 2𝑦 = 0, 2𝑥 − 𝑧 = 0}
Resolvemos el sistema lineal homogéneo:
𝑥 + 2𝑦 = 0  1 2 0  1 2  0  1 2  0
…  ⟹*  +~*  +~†
2𝑥 − 𝑧 = 0  2 0 −1  0 −4 −1  0 1 1/4‡
Tomamos como variable libre 𝑧 = 𝑡 y despejando las otras dos:
𝑥 = 𝑡/2  𝑥  ⎡ ⎤  2
⎢ 2 ⎥
ˆ𝑦 = −𝑡/4 ⟹ ‰𝑦Š = 𝑡 · ⎢ 1⎥ = 𝑡 · 4−15
𝑧=𝑡  𝑧  ⎢− 4⎥  4
⎣ 1 ⎦
La dimensión de este subespacio es 1 (su forma paramétrica tiene un solo parámetro), y las bases estarán
formadas por un único vector, por ejemplo {(2, −1, 4)}.
b) La matriz asociada de la Transformación Lineal se puede obtener fácilmente calculando las imágenes de los
vectores de la base canónica de ℝ$ :
𝑇(1, 0, 0) = (1, 2)
𝑇(0, 1, 0) = (2, 0)
𝑇(0, 0,1) = (0, −1)

1 2 0
𝐴=‹  Œ
2 0 −1
El subespacio imagen de la transformación es el espacio generado por las columnas de A.
1 2 0  1 2  0  1 2  0
‹  Œ~‹  Œ ~ 20 1 1/43
2 0 −1  0 −4 −1
Una base de dicho subespacio será cualquier conjunto libre contenido en ese conjunto generador, por ejemplo
{(1,0), (0,1)}.
```

#### Página 6

```text
c) El espacio generado por la base descrita en el punto anterior es, precisamente, ℝ" (el espacio de llegada de
la transformación lineal), por lo que la transformación es sobreyectiva.
____________________________________________________________________________________________

Pregunta 9. Sea la transformación lineal 𝑇: ℝ" → ℝ" dada por:
𝑇(𝑥, 𝑦) = (𝑥, 𝑥 + 𝑦)
a) (0,5p) Obtener el conjunto de vectores que se transforman en una versión escalada de sí mismos.
b) (0,5p) ¿Cuál es ese factor de escala? ¿Qué estructura algebraica es dicho conjunto?

Respuesta

Lo que se está pidiendo en este ejercicio son los autovectores, y correspondientes autovalores, de la matriz de la
transformación. Dicha matriz en la base canónica de ℝ" es:
𝑇(1, 0) = (1, 1)
𝑇(0, 1) = (0, 1)
1 0
𝐴=‹  Œ
1 1
Como se trata de una matriz triangular con diagonal 1, su único autovalor es 𝜆 = 1 (tiene multiplicidad
algebraica 2).
Este autovalor 𝜆 = 1 es el factor de escala pedido en el enunciado.
(𝐴 − 𝜆 · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 𝐼) · 𝑣 = 0
0 0  𝑥  0
‹  Œ · ‹𝑦 Œ = ‹ Œ
1 0  0
La solución de este sistema es (𝑥, 𝑦) = (0, 𝛼), con parámetro libre 𝛼 ∈ ℝ.
Así, el espacio propio asociado al autovalor 𝜆 = 1 es 𝐸* = {(𝑥, 𝑦) = (0, 𝛼) ∈ ℝ" , 𝛼 ∈ ℝ}. Este es el conjunto
pedido en el enunciado, de los vectores que se transforman en una versión escalada de sí mismos. Este
conjunto es un subespacio vectorial de ℝ" .
Efectivamente, para cualquier vector 𝑣 ∈ 𝐸* , se cumplirá que: 𝑇(𝑣) = 𝜆 · 𝑣.
____________________________________________________________________________________________
```


## CEX · DC01

*Fuente: `EXÁMENES/CEX/TEORICO/DC01.mlx`*

#### DC01. Distribución de temperaturas en una placa metálica

Con el fin de conocer la temperatura en el interior de una placa metálica circular se modela una rejilla como la de la figura en la que se muestran las temperaturas (en ºC) en los puntos frontera y se denominan como $t_1 ,t_2 ,t_3$ y $t_4$ las temperaturas en los puntos interiores que se desean calcular (no cambies los nombres de las variables)e ....

a) (0,5p) Escribe las ecuaciones de equilibrio indicando en cada una de ellas a qué nodo pertenece. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

b) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

c) (1p) Calcula mediante Matlab (script) las temperaturas en los nodos interiores. Da el resultado con fprintf con dos decimales identificando el nodo, es decir: "La temperatura en el nodo .... es de ...."

d) (0,5p) ¿Cuál sería la temperatura en el centro del disco? Da el resultado con fprintf con dos decimales

[Imagen: Placa circular con 4 nodos $t_1$–$t_4$; contorno: arriba 10°, 10°; izquierda 10°, 10°; derecha 5°, 5°; abajo 5°, 5°.]

Respuesta:

_Imágenes embebidas: 1 (image1.png)_


## CEX · DC02.mlx

*Fuente: `EXÁMENES/CEX/DC02.mlx`*

#### DC02. Distribución de temperaturas en una placa metálica

Con el fin de conocer la temperatura en el interior de una placa metálica circular se modela una rejilla como la de la figura en la que se muestran las temperaturas (en ºC) en los puntos frontera y se denominan como $t_1 ,t_2 ,t_3$ y $t_4$ las temperaturas en los puntos interiores que se desean calcular (no cambies los nombres de las variables)e ....

a) (0,5p) Escribe las ecuaciones de equilibrio indicando en cada una de ellas a qué nodo pertenece. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

b) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

c) (1p) Calcula mediante Matlab (script) las temperaturas en los nodos interiores. Da el resultado con fprintf con dos decimales identificando el nodo, es decir: "La temperatura en el nodo .... es de ...."

d) (0,5p) ¿Cuál sería la temperatura en el centro del disco? Da el resultado con fprintf con dos decimales

[Imagen: Placa circular con 4 nodos interiores $t_1$–$t_4$; temperaturas de contorno: arriba 5°, 5°; izquierda 5°, 5°; derecha 9°, 9°; abajo 15°, 15°.]

Respuesta:

_Imágenes embebidas: 1 (image1.png)_


## CEX · DC03.mlx

*Fuente: `EXÁMENES/CEX/DC03.mlx`*

#### DC03. Distribución de temperaturas en una placa metálica

Con el fin de conocer la temperatura en el interior de una placa metálica circular se modela una rejilla como la de la figura en la que se muestran las temperaturas (en ºC) en los puntos frontera y se denominan como $t_1 ,t_2 ,t_3$ y $t_4$ las temperaturas en los puntos interiores que se desean calcular (no cambies los nombres de las variables)e ....

a) (0,5p) Escribe las ecuaciones de equilibrio indicando en cada una de ellas a qué nodo pertenece. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

b) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones sin cambiar los nombres del enunciado

c) (1p) Calcula mediante Matlab (script) las temperaturas en los nodos interiores. Da el resultado con fprintf con dos decimales identificando el nodo, es decir: "La temperatura en el nodo .... es de ...."

d) (0,5p) ¿Cuál sería la temperatura en el centro del disco? Da el resultado con fprintf con dos decimales

[Imagen: Placa circular con 4 nodos interiores $t_1$–$t_4$; contorno: arriba 0°, 5°; izquierda 0°, 0°; derecha 5°, 5°; abajo 1°, 1°.]

Respuesta:

_Imágenes embebidas: 1 (image1.png)_


## CEX · FR01.mlx

*Fuente: `EXÁMENES/CEX/FR01.mlx`*

#### FR01. Red de distribución de repuestos aeronáuticos.

Un centro logístico de repuestos abastece dos almacenes intermedios y, desde ellos, un taller principal y una zona final de expedición.

Nodos

- $N_1$: Centro logístico central

- $N_2$: Almacén Este

- $N_3$: Almacén Oeste

- $N_4$: Taller de integración

- $N_5$: Zona de consolidación

- $N_6$: Expedición final

[Imagen: Red logística de pallets: entrada 120 pallets/h en $N_1$; $x_1$: $N_1\to N_2$, $x_2$: $N_1\to N_3$, $x_3$: $N_2\to N_4$, $x_4$: $N_3\to N_4$, $x_5$: $N_4\to N_5$, $x_6$: $N_5\to N_6$; salidas: 25 pallets/h en $N_3$, 20 en $N_2$, 15 en $N_4$, 60 en $N_6$.]

Datos

- El centro logístico $N_1$ expide 120 pallets/h (pallets/hora).

- En $N_2$ se consumen localmente 20 pallets/h.

- En $N_3$ se consumen localmente 25 pallets/h.

- En $N_4$ se consumen 15 pallets/h.

- En $N_6$ salen del sistema 60 pallets/h.

- Restricción operativa: por planificación interna, el flujo desde el almacén Este hacia el taller debe superar en 5 pallets/h al del almacén Oeste: $x_3 -x_4 =5$

Capacidades máximas

- $$x_1 \le 80$$

- $$x_2 \le 70$$

- $$x_3 \le 50$$

- $$x_4 \le 45$$

- $$x_5 \le 65$$

- $$x_6 \le 65$$

Toma el balance por nodos siguiendo el criterio: entrada − salida = demanda neta

Se pide:

a) (0,25 p). Escribe en el editor de ecuaciones las ecuaciones de balance de los seis nodos identificando a qué nodo pertenece cada una

b) (0,25p) Reescribe las ecuaciones en forma matricial. Para evitar dependencia lineal, toma 5 balances independientes y la restricción operativa, lo puedes realizar reemplazando la condición del nodo $N_4$ por la restricción operativa.

c) (1p) Resuelve el sistema con Matlab y calcula los seis flujos. Da el resultado con fprintf y dos decimales identificando el flujo a que pertenece

d) (0,5p) Comprueba si la solución respeta las capacidades máximas y calcula el porcentaje de ocupación de cada arco. (Utiliza dos decimales)

e) (0,5 p) Verifica con Matlab que también se cumple la ecuación del nodo$\;N_4$, que no se ha usado para resolver los otros

Respuesta:

_Imágenes embebidas: 1 (image1.jpeg)_


## CEX · FR02.mlx

*Fuente: `EXÁMENES/CEX/FR02.mlx`*

#### FR02. Red de agua regenerada para riego urbano e industrial.

Una red de agua regenerada alimenta dos distritos y un parque industrial antes de llegar a un depósito de regulación final.

Nodos

- $N_1$: Estación depuradora

- $N_2$: Distrito Norte

- $N_3$: Distrito Sur

- $N_4$: Parque industrial

- $N_5$: Balsa intermedia

- $N_6$: Depósito regulardor final

[Imagen: Misma topología con caudales de fluido: entrada 140 m³/h en $N_1$; salidas 20 m³/h en $N_3$, 30 en $N_2$, 10 en $N_4$, 80 en $N_6$.]

Datos

- En $N_1 \;$la depuradora entrega 140 m³/h. (Metros cúbicos/hora)

- En $N_2$ se derivan 30 m³/h para riego de zonas verdes.

- En $N_3$ se derivan 20 m³/h.

- En $N_4$ el parque industrial consume 10 m³/h.

- En $N_6$ deben llegar 80 m³/h.

- Restricción operativa: el caudal enviado al Distrito Norte debe superar en 20 m³/h al enviado al Distrito Sur:  $x_1 -x_2 =20$

Capacidades máximas

- $$x_1 \le 90$$

- $$x_2 \le 80$$

- $$x_3 \le 65$$

- $$x_4 \le 60$$

- $$x_5 \le 95$$

- $$x_6 \le 90$$

Toma el balance por nodos siguiendo el criterio: entrada − salida = demanda neta

Se pide:

a) (0,25 p). Escribe en el editor de ecuaciones las ecuaciones de balance de los seis nodos identificando cada uno de ellos

b) (0, 25p) Reescribe la ecuación anterior en forma matricial. Para evitar dependencia lineal, toma 5 balances independientes y la restricción operativa, lo puedes realizar reemplazando la condición del nodo $N_4$ por la restricción operativa.

c) (1 p) Resuelve el sistema con Matlab y calcula los seis caudales. Da el resultado con fprintf y dos decimales identificando el caudal a que pertenece

d) (0,5 p) Comprueba qué caudales cumplen o no las capacidades máximas y calcula el margen restante en cada uno.

e) (0,5 p) Si la demanda final en $N_6$ aumenta a 85 m³/h,  recalcula la solución y comenta si la red sigue siendo viable.

Respuesta:

_Imágenes embebidas: 1 (image1.jpeg)_


## CEX · FR03.mlx

*Fuente: `EXÁMENES/CEX/FR03.mlx`*

#### FR03. Red de transporte interno de equipajes en una terminal aeroportuaria..

Una terminal aérea conduce equipajes desde el clasificador central hacia dos líneas, que confluyen en inspección y continúan hasta carga final.

Nodos

- $N_1$: Clasificador central

- $N_2$: Línea A

- $N_3$: Línea B

- $N_4$: Área de inspección

- $N_5$: Muelle de consolidación

- $N_6$: Carga final

[Imagen: Misma topología con maletas: entrada 130 maletas/min en $N_1$; salidas 25 en $N_3$, 15 en $N_2$, 20 en $N_4$, 70 en $N_6$.]

Datos

- En $N_1 \;$el clasificador central procesa 130 maletas/min.

- En $N_2$ se retiran 15 maletas/min por incidencias locales..

- En $N_3$ se retiran 25 malestas/min.

- En $N_4$ la inspección aparta 20 malestas/min.

- En $N_6$ salen 70 maletas/min hacia carga

- Restricción operativa: por diseño de la terminal, la línea B debe enviar 10 maletas/min más a inspección que la línea A:  $x_4 -x_3 =10$

Capacidades máximas

- $$x_1 \le 60$$

- $$x_2 \le 80$$

- $$x_3 \le 45$$

- $$x_4 \le 60$$

- $$x_5 \le 75$$

- $$x_6 \le 75$$

Toma el balance por nodos siguiendo el criterio: entrada − salida = demanda neta

Se pide:

a) (0,25 p). Escribe en el editor de ecuaciones las ecuaciones de balance de los seis nodos identificando cada uno de ellos

b) (0, 25p) Reescribe la ecuación anterior en forma matricial. Para evitar dependencia lineal, toma 5 balances independientes y la restricción operativa, lo puedes realizar reemplazando la condición del nodo $N_4$ por la restricción operativa.

c) (1 p) Resuelve el sistema con Matlab y calcula los seis flujos de maletas. Da el resultado con fprintf y dos decimales identificando el flujo a que pertenece

d) (0,5 p) Verifica qué enlaces están por encima del 90% de ocupación de su capacidad máxima y si la solución obtenida es factible

e) (0,5 p) Comprueba si, al reducir la capacidad del flujjo $x_6$ a 68 maletas/min, la solución sigue siendo factible. Justifica la respuesta utilizando Matlab.

Respuesta:

_Imágenes embebidas: 1 (image1.jpeg)_


## CEX · GR01.mlx

*Fuente: `EXÁMENES/CEX/GR01.mlx`*

#### GR01. Grafos

Sea el siguiente grafo de resultados de una competición, en el que X→Y representa una victoria directa de X sobre Y :

[Imagen: Grafo dirigido de 5 vértices A–E (variante 1 de las flechas) para el problema de grafos del examen.]

a) (1.0p) Escribe, mediante el editor de textos, una tabla que represente las victorias y derrotas de cada jugador en el torneo. En dicha tabla los jugadores deben aparecer en orden alfabético. Crea también la matriz de adyacencia en MATLAB, asignándole la variable A.

b) (0,5p) Representa el grafo dirigido de la competición (es decir, se pide que obtengas tú el grafo que te damos en el enunciado).

c) (1.0p) ¿Queda clara la clasificación del torneo atendiendo a victorias directas e indirectas? Da el resultado mediante fprintf en orden de 1º a último.

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · GR02.mlx

*Fuente: `EXÁMENES/CEX/GR02.mlx`*

#### GR01. Grafos

Sea el siguiente grafo de resultados de una competición, en el que X→Y representa una victoria directa de X sobre Y :

[Imagen: Grafo dirigido de 5 vértices A–E (variante 2: algunas flechas invertidas respecto a la variante 1).]

a) (1.0p) Escribe, mediante el editor de textos, una tabla que represente las victorias y derrotas de cada jugador en el torneo. En dicha tabla los jugadores deben aparecer en orden alfabético. Crea también la matriz de adyacencia en MATLAB, asignándole la variable A.

b) (0,5p) Representa el grafo dirigido de la competición (es decir, se pide que obtengas tú el grafo que te damos en el enunciado).

c) (1.0p) ¿Queda clara la clasificación del torneo atendiendo a victorias directas e indirectas? Da el resultado mediante fprintf en orden de 1º a último.

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · GR03.mlx

*Fuente: `EXÁMENES/CEX/GR03.mlx`*

#### GR01. Grafos

Sea el siguiente grafo de resultados de una competición, en el que X→Y representa una victoria directa de X sobre Y :

[Imagen: Grafo dirigido de 5 vértices A–E (variante 3 de las flechas).]

a) (1.0p) Escribe, mediante el editor de textos, una tabla que represente las victorias y derrotas de cada jugador en el torneo. En dicha tabla los jugadores deben aparecer en orden alfabético. Crea también la matriz de adyacencia en MATLAB, asignándole la variable A.

b) (0,5p) Representa el grafo dirigido de la competición (es decir, se pide que obtengas tú el grafo que te damos en el enunciado).

c) (1.0p) ¿Queda clara la clasificación del torneo atendiendo a victorias directas e indirectas? Da el resultado mediante fprintf en orden de 1º a último.

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · IP01.mlx

*Fuente: `EXÁMENES/CEX/IP01.mlx`*

#### IP01. Consumo eléctrico de una nave industrial.

En una nave industrial se registra la potencia eléctrica demandada durante un turno de trabajo. Se dispone de las siguientes mediciones:

Hora t (h)

8:00

10:00

12:00

14:00

16:00

18:00

Potencia P (kW)

420

465

510

560

590

610

Se pide:

a) (0,25 puntos). Escribe con el editor de ecuaciones la expresión general del polinomio interpolador.

b) (0,25 puntos). Escribe con el editor de ecuaciones las ecuaciones necesarias para obtener el polinomio

c) (0,25 puntos). Reescribe con el editor de ecuaciones el sistema anterior en forma matricial

d) (0,75 puntos) Resuelve con Matlab el sistema y obten los coeficiones del polinomio interpolador. Da el resultado con fprintf y  2 decimales identificando claramente a qué coeficiente corresponde cada término

e) (0,5 puntos) Con Matlab calcula la potencia estimada a las 9:00 h, 13:00 h y a las 17:00 h. Da el resultado con fprintf y dos decimales

f) (0,5 puntos) Representa en una misma gráfica:

- Los 6 puntos dados.

- Los 3 puntos calculados.

- El polinomio de interpolación.

Nota:

- Para simplificar el cálculo y evitar problemas numéricos,es recomendable realizar un cambio de variable que centre los datos en el origen, por ejemplo $z=t-8$. No obstante, el problema puede resolverse correctamente sin realizar dicho cambio.

- En los apartados b y c, no es neceario desarrollar las potencias.

Respuesta.


## CEX · IP02.mlx

*Fuente: `EXÁMENES/CEX/IP02.mlx`*

#### IP02. Temperatura del aceite en un banco de ensayos.

En un banco de ensayos se mide la temperatura del aceite de un sistema mecánico durante el calentamiento incical. Los datos registrados son:

Tiempo (minutos)

0

5

10

15

20

25

Temperatura T (ºC)

22,0

36,5

52,8

67,1

74,0

78,2

Se pide:

a) (0,25 puntos). Escribe con el editor de ecuaciones la expresión general del polinomio interpolador.

b) (0,25 puntos). Escribe con el editor de ecuaciones las ecuaciones necesarias para obtener el polinomio

c) (0,25 puntos). Reescribe con el editor de ecuaciones el sistema anterior en forma matricial

d) (0,75 puntos) Resuelve con Matlab el sistema y obten los coeficiones del polinomio interpolador. Da el resultado con fprintf y  2 decimales identificando claramente a qué coeficiente corresponde cada término

e) (0,5 punto) Con Matlab calcule la potencia estimada a los 3 min, 12 min, 22 min. Da el resultado con fprintf y dos decimales

f) (0,5 puntos) Represente en una misma gráfica:

- Los 6 puntos experimentales dados.

- Los 3 puntos calculados.

- El polinomio de interpolación.

Nota:

- En los apartados b y c, no es neceario desarrollar las potencias.

Respuesta.


## CEX · IP03.mlx

*Fuente: `EXÁMENES/CEX/IP03.mlx`*

#### IP03. Producción acumulada de una planta fotovoltaica.

Durante una jornada despejada se ha registrado la energía acumulada producida por una instalación fotovoltaica en distintos instantes del día:

Hora

9:00

10:00

11:00

12:00

13:00

14:00

Energía acumulada E (kWh)

35

82

140

205

268

320

Se pide:

a) (0,25 puntos). Escribe con el editior de ecuaciones la expresión general del polinomio interpolador:

b) (0,25 puntos). Escribe con el editor de ecuaciones las ecuaciones necesarias para obtener el polinomio

c) (0,25 puntos). Reescribe con el editor de ecuaciones el sistema anterior en forma matricial

d) (0,75 puntos) Resuelve con Matlab el sistema y obten los coeficiones del polinomio interpolador. Da el resultado con fprintf y  2 decimales identificando claramente a qué coeficiente corresponde cada término

e) (0,5 puntos) Con Matlab calcule la potencia estimada a las 9:30 h, 11:30 h y 13:30 h.

f) (0,5 puntos) Represente en una misma gráfica:

- Los 6 puntos experimentales dados.

- Los 3 puntos calculados.

- El polinomio de interpolación.

Nota:

- Para simplificar el cálculo y evitar problemas numéricos,es recomendable realizar un cambio de variable que centre los datos en el origen, por ejemplo $z=t-9$. No obstante, el problema puede resolverse correctamente sin realizar dicho cambio.

- En los apartados b y c, no es neceario desarrollar las potencias.

- En el apartado e, recuerda que MATLAB no entiende horas y minutos, entiende números reales. Por eso tenemos que transformar los minutos en parte de una hora.

- Calcular los coeficientes del polinomio de interpolación con dos dígitos.

Respuesta.


## CEX · LEO01.mlx

*Fuente: `EXÁMENES/CEX/LEO01.mlx`*

#### LEO01. Economía con cuatro sectores

Una economía está formada por 4 sectores productivos:

- Agricultura

- Industria

- Energía

- Servicios

La matriz de coeficientes técnicos A viene dada por:

$$A=\left\lbrack \begin{array}{cccc}
0\ldotp 15 & 0\ldotp 10 & 0\ldotp 05 & 0\ldotp 20\\
0\ldotp 20 & 0\ldotp 25 & 0\ldotp 10 & 0\ldotp 15\\
0\ldotp 10 & 0\ldotp 20 & 0\ldotp 30 & 0\ldotp 10\\
0\ldotp 05 & 0\ldotp 15 & 0\ldotp 10 & 0\ldotp 20
\end{array}\right\rbrack$$

y la demanda final inicial es:

$$d=\left\lbrack \begin{array}{c}
120\\
200\\
150\\
180
\end{array}\right\rbrack$$

Todas las magnitudes están medidas en millones de euros.

a) (0.25p) Determina razonadamente si se trata de una economía productiva

b) (0,5p) Calcula el vector de producción total x. Da el resultado con fprintf con 2 decimales identificando cada sector

c) (0,75p) Debido a una crisis energética, la demanda final del sector Energía aumenta un 30 %, mientras que la del sector Industria disminuye un 10 %. Define el nuevo vector de demanda dshock y calcula la nueva producción de equilibrio. Da el resultado con fprintf con 2 decimales identificando cada sector

d) (1.0p) Supón ahora que el coeficiente técnico a(3,3) (consumo interno del sector Energía) aumenta de 0.30 a 0.38. Analiza cómo cambia la producción total agregada respecto de la del apartado a) y  explica el resultado desde el punto de vista económico

Debes dar: la producción total inicial, la nueva y el incrmento absoluto y porcentual todas ellas con fprintf y 2 decimales

Respuesta


## CEX · LEO02.mlx

*Fuente: `EXÁMENES/CEX/LEO02.mlx`*

#### LEO02. Economía regional con cuatro sectores

Una economía regional está formada por los sectores:

- Construcción

- Transporte

- Energía

- Servicios

La matriz de coeficientes técnicos es:

$$A=\left\lbrack \begin{array}{cccc}
0\ldotp 12 & 0\ldotp 08 & 0\ldotp 05 & 0\ldotp 10\\
0\ldotp 10 & 0\ldotp 20 & 0\ldotp 08 & 0\ldotp 12\\
0\ldotp 06 & 0\ldotp 12 & 0\ldotp 25 & 0\ldotp 08\\
0\ldotp 04 & 0\ldotp 10 & 0\ldotp 06 & 0\ldotp 18
\end{array}\right\rbrack$$

y la demanda final inicial es:

$$d=\left\lbrack \begin{array}{c}
180\\
140\\
120\\
200
\end{array}\right\rbrack$$

Todas las magnitudes están medidas en millones de euros.

a) (0.25p) Determina razonadamente si se trata de una economía productiva

b) (0,5p) Calcula el vector de producción total x. Da el resultado con fprintf con 2 decimales identificando cada sector

c) (0,75p) Debido a una crisis energética, la demanda final del sector Construcción aumenta un 20 %, mientras que la del sector Transporte disminuye un 15 %. Define el nuevo vector de demanda dshock y calcula la nueva producción de equilibrio. Da el resultado con fprintf con 2 decimales identificando cada sector

d) (1.0p) Supón ahora que el coeficiente técnico $a_{33}$ (consumo interno del sector Energía) aumenta de 0.25 a 0.35. Analiza cómo cambia la producción total agregada respecto de la del apartado a) y  explica el resultado desde el punto de vista económico

Debes dar: la producción total inicial, la nueva y el incrmento absoluto y porcentual todas ellas con fprintf y 2 decimales

Respuesta


## CEX · LEO03.mlx

*Fuente: `EXÁMENES/CEX/LEO03.mlx`*

#### LEO03. Sistema energético nacional

Una economía regional está formada por los sectores:

- Agricultura

- Industria alimentaria

- Energía

- Distribución

La matriz de coeficientes técnicos es:

$$A=\left\lbrack \begin{array}{cccc}
0\ldotp 10 & 0\ldotp 05 & 0\ldotp 04 & 0\ldotp 06\\
0\ldotp 15 & 0\ldotp 18 & 0\ldotp 10 & 0\ldotp 08\\
0\ldotp 08 & 0\ldotp 12 & 0\ldotp 28 & 0\ldotp 10\\
0\ldotp 05 & 0\ldotp 08 & 0\ldotp 06 & 0\ldotp 16
\end{array}\right\rbrack$$

y la demanda final inicial es:

$$d=\left\lbrack \begin{array}{c}
250\\
180\\
160\\
220
\end{array}\right\rbrack$$

Todas las magnitudes están medidas en millones de euros.

a) (0.25p) Determina razonadamente si se trata de una economía productiva

b) (0,5p) Calcula el vector de producción total x. Da el resultado con fprintf con 2 decimales identificando cada sector

c) (0,75p) Debido a una sequía, la demanda final del sector Energía aumenta un 12%, mientras que la del sector Agricltura disminuye un 12 %. Define el nuevo vector de demanda dshock y calcula la nueva producción de equilibrio. Da el resultado con fprintf con 2 decimales identificando cada sector

d) (1.0p) Supón ahora que el coeficiente técnico $a_{22}$ (consumo interno del sector Industria alimentaria) aumenta de 0.18 a 0.30. Analiza cómo cambia la producción total agregada respecto de la del apartado a) y  explica el resultado desde el punto de vista económico

Debes dar: la producción total inicial, la nueva y el incrmento absoluto y porcentual todas ellas con fprintf y 2 decimales

Respuesta


## CEX · MK01.mlx

*Fuente: `EXÁMENES/CEX/MK01.mlx`*

MK01. Flujo de emigración a ciudades periféricas de Madrid

Se calcula que cada año el 15% de la población de Madrid se traslada a Guadalajara y el 12% a Segovia. El 5% de la población de Segovia se traslada a Guadalajara y el 17% a Madrid. El 13% de la población de Guadalajara se traslada a Madrid y el 3% a Segovia. Actualmente, las poblaciones totales son de 3,5 millones en Madrid, 150.000 en Segovia y 100.000 en Guadalajara

a) (0,25p) Escribe con el editor de ecuaciones una tabla que represente la matriz de transición para la cadena de Markov que describe el patrón de migración. Asígnale en Matlab la variable M y verifica que se trata de una matriz de transición. El orden de las columnas debe ser: Guadalajara, Madrid, y Segovia

b) (0,25p) Escribe con el editor de ecuaciones el vector de estado inicial y asígnale con Matlab la variable x0. Debe ser un vector columna

c) (1p) Calcula la distribución de población esperada después de 10 años en cada ciudad mediante una sola operación. Da el resultado con fprintf redondeado al entero más próximo identificando cada ciudad

d) (1p) Con el tiempo y suponiendo que el patrón de migráción se mantiene constante, determina la población en cada ciudad a largo plazo, para ello emplea el método de autovalores y autovectores. Da el resultado con fprintf redondeado al entero más próximo e identificando cada ciudad

Respuesta


## CEX · MK02.mlx

*Fuente: `EXÁMENES/CEX/MK02.mlx`*

MK02. Flujo de emigración a ciudades periféricas de Barcelona

Se calcula que cada año el 11% de la población de Barcelona se traslada a Tarrasa y el 8% a Mataró. El 6% de la población de Tarrasa se traslada a Mataró y el 13% a Barcelona. El 9% de la población de Mataró se traslada a Barcelona y el 7% a Tarrasa. Actualmente, las poblaciones totales son de 1,7 millones en Barcelona, 230.000 en Tarrasa y 130.000 en Mataró

a) (0,25p) Escribe con el editor de ecuaciones una tabla que represente la matriz de transición para la cadena de Markov que describe el patrón de migración. Asígnale en Matlab la variable M y verifica que se trata de una matriz de transición. El orden de las columnas debe ser: Barcelona, Mataró y Tarrasa

b) (0,25p) Escribe con el editor de ecuaciones el vector de estado inicial y asígnale con Matlab la variable x0. Debe ser un vector columna

c) (1p) Calcula la distribución de población esperada después de 7 años en cada ciudad mediante una sola operación. Da el resultado con fprintf redondeado al entero más próximo identificando cada ciudad

d) (1p) Con el tiempo y suponiendo que el patrón de migráción se mantiene constante, determina la población en cada ciudad a largo plazo, para ello emplea el método de resolución de un sistema lineal homogéneo. Da el resultado con fprintf redondeado al entero más próximo e identificando cada ciudad

Respuesta


## CEX · MK03.mlx

*Fuente: `EXÁMENES/CEX/MK03.mlx`*

MK03. Flujo de emigración a ciudades periféricas de Valencia

Se calcula que cada año el 10% de la población de Valencia se traslada a Torrent y el 6% a Gandía. El 5% de la población de Torrent se traslada a Gandía y el 16% a Valencia. El 11% de la población de Gandía se traslada a Valencia y el 3% a Torrent. Actualmente, las poblaciones totales son de 840.000 en Valencia, 90.000 en Torrent y 75.000 en Gandía

a) (0,25p) Escribe con el editor de ecuaciones una tabla que represente la matriz de transición para la cadena de Markov que describe el patrón de migración. Asígnale en Matlab la variable M y verifica que se trata de una matriz de transición. El orden de las columnas debe ser: Gandía, Torrent, Valencia

b) (0,25p) Escribe con el editor de ecuaciones el vector de estado inicial y asígnale con Matlab la variable x0. Debe ser un vector columna

c) (1p) Calcula la distribución de población esperada después de 5 años en cada ciudad mediante una sola operación. Da el resultado con fprintf redondeado al entero más próximo identificando cada ciudad

d) (1p) Con el tiempo y suponiendo que el patrón de migráción se mantiene constante, determina la distribución de población a largo plazo. Para ello emplea un método iterativo con un error menor que ${10}^{-6}$.Da el resultado con fprintf redondeado el resultado al entero más próximo e identificando cada ciudad

Nota: Para resolver el último apartado debes ir calculando vectores de estado sucesivos hasta que la norma de la diferencia entre dos consecutivos sea menor que${10}^{-6}$. Para ello te sugerimos que emplees un bucle while y la función norm

Respuesta


## CEX · PR01.mlx

*Fuente: `EXÁMENES/CEX/PR01.mlx`*

#### PR02. Clasificación de páginas web

En una miniweb existen 6 páginas enlazadas como se muestra en la figura:

[Imagen: Grafo dirigido de 6 nodos (A–F): E↔C, C↔D, A→C, A→B, D→B, D↔F, B↔F.]

En todas las respuestas se suponen las páginas en orden alfabético

a) (0,5p) Calcula la matriz de adyacencia. Escríbela con el editor de ecuaciones y luego asígnale la variable A en MATLAB.

b) (0,5p) Dibuja el grafo dirigido correspondiente.

c) (0,5p) Calcula la matriz de Markov correspondiente (sin atenuación). Explica el proceso.  Asígnale la variable B en MATLAB;

d) (1p) Calcula la clasificación de páginas a partir de la matriz B sin aplicar factor de atenuación. Da el resultado mediante fprintf ordenando las páginas, es decir, debes dar "la 1ª página es....", etc ¿En qué problema incurre el algoritmo sin aplicar factor de atenuación?

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · PR02.mlx

*Fuente: `EXÁMENES/CEX/PR02.mlx`*

#### PR02. Clasificación de páginas web

En una miniweb existen 6 páginas enlazadas como se muestra en la figura:

[Imagen: Mismo grafo con etiquetas permutadas: D↔F, F↔A, C→F, C→E, A→E, A↔B, E↔B.]

En todas las respuestas se suponen las páginas en orden alfabético

a) (0,5p) Calcula la matriz de adyacencia. Escríbela con el editor de ecuaciones y luego asígnale la variable A en MATLAB.

b) (0,5p) Dibuja el grafo dirigido correspondiente.

c) (0,5p) Calcula la matriz de Markov correspondiente (sin atenuación). Explica el proceso.  Asígnale la variable B en MATLAB;

d) (1p) Calcula la clasificación de páginas a partir de la matriz B sin aplicar factor de atenuación. Da el resultado mediante fprintf ordenando las páginas, es decir, debes dar "la 1ª página es....", etc ¿En qué problema incurre el algoritmo sin aplicar factor de atenuación?

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · PR03.mlx

*Fuente: `EXÁMENES/CEX/PR03.mlx`*

#### PR02. Clasificación de páginas web

En una miniweb existen 6 páginas enlazadas como se muestra en la figura:

[Imagen: Mismo grafo con etiquetas permutadas: B↔A, A↔F, D→A, D→C, F→C, F↔E, C↔E.]

En todas las respuestas se suponen las páginas en orden alfabético

a) (0,5p) Calcula la matriz de adyacencia. Escríbela con el editor de ecuaciones y luego asígnale la variable A en MATLAB.

b) (0,5p) Dibuja el grafo dirigido correspondiente.

c) (0,5p) Calcula la matriz de Markov correspondiente (sin atenuación). Explica el proceso.  Asígnale la variable B en MATLAB;

d) (1p) Calcula la clasificación de páginas a partir de la matriz B sin aplicar factor de atenuación. Da el resultado mediante fprintf ordenando las páginas, es decir, debes dar "la 1ª página es....", etc ¿En qué problema incurre el algoritmo sin aplicar factor de atenuación?

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## CEX · Práctico · AR01

*Fuente: `EXÁMENES/CEX/PRÁCTICO/AR01.mlx`*

#### AR01. Recursos de una piscifactoría

La Dirección General de Recursos Marinos proporciona cuatro tipos de alimento a una reserva que alberga cuatro especies de peces.

Cada pez de la especie 1 consume semanalmente un promedio de 1,8 unidades de alimento A, 0,9 unidades de alimento B, 2,4 unidades de alimento C y 1,3 unidades de alimento D.

Cada pez de la especie 2 consume semanalmente un promedio de 2,6 unidades de A, 1,7 unidades de B, 1,5 unidades de C y 2,1 unidades de D.

Cada pez de la especie 3 consume semanalmente un promedio de 1,2 unidades de A, 2,8 unidades de B, 2,2 unidades de C y 1,6 unidades de D.

Cada pez de la especie 4 consume semanalmente un promedio de 3,1 unidades de A, 1,4 unidades de B, 1,8 unidades de C y 2,7 unidades de D.

Cada semana se suministran a la reserva:

- 23.400 unidades de alimento A,

- 17.200 unidades de alimento B,

- 20.800 unidades de alimento C,

- 19.500 unidades de alimento D.

Suponiendo que todo el alimento es consumido y que la población de cada especie permanece constante, se desea determinar cuántos peces de cada especie pueden coexistir en la reserva.

a) (0,5p) Determina inequívocamente las variables y sus unidades. Emplea el editor de texto y ecuaciones no el script

b) (0,75p) Escribe las ecuaciones que permiten resolver el problema idenetificando a qué corresponde cada una de ellas. Emplea el editor de texto y ecuaciones no el script

c) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones no el script

d) (0,75p) Resuélvelo con Matlab dando el resultado con fprintf identificando claramente cada una de las respuestas, es decir, debes dar "se necesitan .... peces del tipo ..." . Da el resultado redondeado al entero inferior mediante la función floor

Respuesta


## CEX · Práctico · AR02

*Fuente: `EXÁMENES/CEX/PRÁCTICO/AR02.mlx`*

#### AR02.Asignación de recursos en un hospital

Un hospital debe distribuir semanalmente cuatro tipos de recursos sanitarios entre cuatro tipos de pacientes: pacientes de medicina interna, traumatología, cirugía y cuidados paliativos.

Cada paciente de medicina interna requiere semanalmente, en promedio, 1,6 horas de enfermería, 0,8 dosis de medicación A, 2,3 pruebas diagnósticas y 1,2 unidades de material sanitario.

Cada paciente de traumatología requiere 2,4 horas de enfermería, 1,5 dosis de medicación A, 1,1 pruebas diagnósticasy 1,8 unidades de material sanitario.

Cada paciente de cirugía requiere 1,3 horas de enfermería, 2,2 dosis de medicación A, 2,6 pruebas diagnósticas y 1,4 unidades de material sanitario.

Cada paciente de cuidados intermedios requiere 2,1 horas de enfermería, 1,1 dosis de medicación A, 1,7 pruebas diagnósticas y 2,5 unidades de material sanitario.

El hospital dispone semanalmente de:

21400 horas de enfermería,

17100 dosis de medicación A

24600 pruebas diagnósticas,

20100 unidades de material sanitario.

Suponiendo que todos los recursos se emplean exactamente, se desea determinar cuántos pacientes de cada tipo puede atender el hospital

a) (0,5p) Determina inequívocamente las variables y sus unidades. Emplea el editor de texto y ecuaciones no el script

b) (0,75p) Escribe las ecuaciones que permiten resolver el problema idenetificando a qué corresponde cada una de ellas. Emplea el editor de texto y ecuaciones no el script

c) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones no el script

d) (0,75p) Resuélvelo con Matlab dando el resultado con fprintf identificando claramente cada una de las respuestas, es decir, debes dar "el hospital puede atender a .... pacientes de  ..." . Da el resultado redondeado al entero inferior mediante la función floor

Respuesta


## CEX · Práctico · AR03

*Fuente: `EXÁMENES/CEX/PRÁCTICO/AR03.mlx`*

#### AR03. Planificación de producción en una fábrica de baterías

Una fábrica produce cuatro modelos de baterías para vehículos eléctricos y sistemas de almacenamiento energético:

- UrbanCell: batería compacta para vehículos urbanos.

- EcoDrive: batería de autonomía media para turismos.

- PowerMax: batería de alta capacidad para vehículos industriales ligeros.

- GridStore: batería estacionaria para almacenamiento de energía renovable.

Cada batería UrbanCell requiere, en promedio, 1,4 kg de litio, 0,9 kg de níquel, 2,1 horas de ensamblaje y 1,2 unidadesde control de calidad.

Cada batería EcoDrive requiere 2,3 kg de litio, 1,6 kg de níquel, 1,2 horas de ensamblaje y 1,7 unidades de control de calidad.

Cada batería PowerMax requiere 1,1 kg de litio, 2,4 kg de níquel, 2,6 horas de ensamblaje y 1,5 unidades de control de calidad.

Cada batería GridStore requiere 1,8 kg de litio, 1,3 kg de níquel, 1,7 horas de ensamblaje y 2,2 unidades de control de calidad.

La fábrica dispone semanalmente de:

- 17400 kg de litio.

- 16400 kg de níquel.

- 23600 horas de montaje.

- 19500 unidades de control de calidad.

Suponiendo que todos los recursos se consumen exactamente, se desea calcular cuántas baterías de cada modelo deben fabricarse.

a) (0,5p) Determina inequívocamente las variables y sus unidades. Emplea el editor de texto y ecuaciones no el script

b) (0,75p) Escribe las ecuaciones que permiten resolver el problema idenetificando a qué corresponde cada una de ellas. Emplea el editor de texto y ecuaciones no el script

c) (0,5p) Reescribe las ecuaciones en forma matricial. Emplea el editor de texto y ecuaciones no el script

d) (0,75p) Resuélvelo con Matlab dando el resultado con fprintf identificando claramente cada una de las respuestas, es decir, debes dar "se podrán fabricar   ... baterías ...." . Da el resultado redondeado al entero inferior mediante la función floor

Respuesta
