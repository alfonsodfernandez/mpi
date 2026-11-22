# Exámenes convocatoria ordinaria (CO) 2025/26

Teórico (3 modelos con respuestas) y práctico en MATLAB. Siglas: AR asignación de recursos, DC distribución de calor, FR flujo de redes, IP interpolación polinómica, LEO Leontief, MK Markov, PR PageRank.

**Contenido de este archivo:**
- CO · Teórico · Modelo A (con respuestas)
- CO · Teórico · Modelo B (con respuestas)
- CO · Teórico · Modelo C (con respuestas)
- CO · Práctico · AR01.mlx
- CO · Práctico · AR02.mlx
- CO · Práctico · DC01.mlx
- CO · Práctico · DC02.mlx
- CO · Práctico · FR01.mlx
- CO · Práctico · FR02.mlx
- CO · Práctico · IP01.mlx
- CO · Práctico · IP02.mlx
- CO · Práctico · LEO01.mlx
- CO · Práctico · LEO02.mlx
- CO · Práctico · MK01.mlx
- CO · Práctico · MK02.mlx
- CO · Práctico · PR01.mlx
- CO · Práctico · PR02.mlx


## CO · Teórico · Modelo A (con respuestas)

*Fuente: `EXÁMENES/CO/TEORICO/MPI1_2526_CO_ModA_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Ordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1,5h  Mod A

INSTRUCCIONES

•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en todas ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo contrario la
puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Sea 𝐴 una matriz de orden 4 tal que al aplicar el método de Gauss se obtiene una matriz
escalonada con tres filas no nulas

a) (0,25p) Determina el rango de 𝐴.
b) (0,25p) Decide si 𝐴 es invertible.
c) (0,5p) Razona si existe algún 𝒃 para el que 𝐴𝒙 = 𝒃 tenga solución única.

Respuesta
a) El rango de una matriz se define como el número de filas linealmente independientes, y no cambia al
aplicar transformaciones elementales por filas. Al aplicar el método de Gauss se obtiene una matriz
escalonada con tres filas no nulas y una fila nula. En una matriz escalonada cada fila no nula contiene un
pivote, y cada pivote corresponde a una fila linealmente independiente. Por tanto, rg (𝐴) = 3.

b) Una matriz cuadrada 𝑛 × 𝑛 es invertible si y solo si su rango es máximo, es decir:
rg (𝐴) = 𝑛.
En este caso:
•  𝐴 es 4 × 4,
•  pero su rango es 3 < 4.

Por tanto, 𝐴 no es invertible.

c) Al tener la forma escalonada de A una fila entera de ceros, el sistema 𝐴𝑥 = 𝑏 solo puede ser incompatible
(si la última fila de la forma escalonada de [𝐴 𝑏] tiene un último elemento no nulo) o compatible
indeterminado (si la forma escalonada de [𝐴 𝑏] tiene una última fila entera de ceros). Así, no existe ningún
vector b para el que el sistema 𝐴𝑥 = 𝑏 tenga solución única.
____________________________________________________________________________________________

Pregunta 2. ¿Cuál de las siguientes afirmaciones es cierta sobre la matriz dada? Razona tu respuesta en
cada apartado.
1 0 0 3
40 1 1 28
0 0 0 3
0 0 0 0
a) (0,25p) Está en la forma escalonada reducida por filas.
b) (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, con infinitas
soluciones.
```

#### Página 2

```text
c)  (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, incompatible.
d)  (0,25p) Podría ser la matriz de coeficientes de un sistema de 4 ecuaciones con 4 incógnitas, incompatible.

Respuesta

a) NO es cierto, ya que en la forma escalonada reducida por filas el primer número diferente de cero en
una fila debe ser 1.
b) NO es cierto, ya que la penúltima fila implica que el sistema es incompatible.
c)  Es cierto, ya que las dimensiones cuadran (aunque “sobre” una ecuación), y la penúltima fila indica que
el sistema es incompatible.
d) Es cierto, ya que las dimensiones cuadran, y si el último elemento del vector de términos
independientes es distinto de cero, la matriz ampliada tendría una fila correspondiente a un sistema
incompatible.

____________________________________________________________________________________________

Pregunta 3. Sea
1 0 0
𝐴 = 9−2 1 0;
1 0 1

a)  (0,5p) Describe qué transformaciones elementales representa 𝐴.
b)  (0,5p) Calcula 𝐴!" a partir de las transformaciones del apartado anterior

Respuesta

a) 𝐴 es la matriz correspondiente a la identidad tras aplicarle las siguientes transformaciones elementales:

𝑓# → 𝑓# − 2𝑓"
𝑓$ → 𝑓$ + 𝑓"
b) La inversa de 𝐴 deshace dichas operaciones elementales, es decir, aplica:
𝑓$ → 𝑓$ − 𝑓"
𝑓# → 𝑓# + 2𝑓"
Por tanto:
1 0 0
𝐴!" = 9 2 1 0;
−1 0 1
____________________________________________________________________________________________

Pregunta 4. Sea V = ℝ$ y considérese el subconjunto
W = {(x, y, z) ∈ ℝ$ | x + 2y + z = 0}.

a) (0,5p) Justifica por qué W es un subespacio vectorial de ℝ$ .
b) (0,5p) Determina la dimensión de W.

Respuesta
a) El conjunto W es el conjunto de soluciones de una ecuación lineal homogénea.
Por tanto:
•  contiene al vector nulo,
•  es cerrado para la suma,
•  es cerrado para el producto por escalares.
```

#### Página 3

```text
Luego, W es un subespacio vectorial de ℝ$ .

b) W está definido por una única ecuación lineal independiente en ℝ$ .
Por tanto:
𝑑𝑖𝑚 (𝑊) = 3 − 1 = 2

____________________________________________________________________________________________

2 1
Pregunta 5. (1p) Hallar todas las matrices reales que conmutan con la matriz A = O  P
−1 2

Respuesta
𝑎  𝑏
La matriz buscada es una matriz 𝐵 = O  P tal que 𝐴 · 𝐵 = 𝐵 · 𝐴
𝑐  𝑑
2𝑎 + 𝑐 = 2𝑎 − 𝑏
2 1 𝑎  𝑏  𝑎  𝑏  2 1  2𝑏 + 𝑑 = 𝑎 + 2𝑏  𝑎=𝑑
𝐴𝐵 = 𝐵𝐴 ⟹ O  PO  P=O  PO  P⟹V  ⟹W
−1 2 𝑐  𝑑  𝑐  𝑑 −1 2  −𝑎 + 2𝑐 = 2𝑐 − 𝑑  𝑏 = −𝑐
−𝑏 + 2𝑑 = 𝑐 + 2𝑑

𝑑  −𝑐
Por tanto, existen infinitas matrices que conmutan con la matriz A y vienen dadas por O  P , ∀ 𝑐, 𝑑 ∈ ℝ
𝑐  𝑑

____________________________________________________________________________________________

Pregunta 6. Sea 𝑓(𝑥): ℝ$ → ℝ$ una aplicación lineal con matriz asociada 𝐴 respecto de las bases canónicas,
cuyo subespacio imagen está dado por:
𝐼𝑚(𝑓) = {(𝑥, 𝑦 𝑧) 𝜖 ℝ$ ; 𝑥 + 𝑦 − 𝑧 = 0}
Se pide:

a)  (0.5p) Determinar la dimensión del espacio imagen y el rango de la matriz 𝐴
b) (0,5p) Clasificar razonadamente el sistema lineal 𝐴 ∙ 𝒙 = 9 1 ;, indicando si es compatible determinado,
−1
compatible indeterminado o incompatible, sin calcular la matriz 𝐴 ni determinantes, justificando la respuesta
a partir de la información del subespacio imagen.
Respuesta

a)  El subespacio imagen está definido por la ecuación:

𝑥+𝑦−𝑧 =0
Esto describe un plano en ℝ$ , por tanto 𝑑𝑖𝑚(𝐼𝑚(𝑓)) = 2.
Como el rango de la matriz 𝐴 coincide con la dimensión del espacio imagen: 𝑟(𝐴) = 2.

b)  el sistema lineal 𝐴 ∙ 𝒙 = 9 1 ; será compatible si el vector del término independiente pertenece al
−1
espacio imagen, es decir, si cumple la condición: 𝑥 + 𝑦 − 𝑧 = 0
para 𝒗 = (2, 1, −1)
2 + 1 − (−1) = 4 ≠ 0
Por tanto: v ∉ 𝐼𝑚(𝑓)

El sistema es incompatible (no tiene solución), porque el término independiente no pertenece al subespacio
imagen.
```

#### Página 4

```text
Razonamiento adicional:
𝑟(𝐴) = 2
Número de incógnitas 𝑛 = 3.
Si el vector estuviera en la imagen, el sistema sería compatible indeterminado (infinitas soluciones), porque
𝑟(𝐴) < 𝑛. Como no lo está, es incompatible.
____________________________________________________________________________________________

Pregunta 7. Sea 𝑇: ℝ$ → ℝ$ una transformación lineal, tal que:
𝑇(1,0,0) = (1,0,0)
𝑇(0,1,0) = (1,1,0)
𝑇(1,1,1) = (2,1,1)
a) (1p) Determina la matriz de 𝑇 en la base canónica.
b) (0,25p) Decide si 𝑇 es inyectiva.

Respuesta
1. Sean 𝑒" = (1,0,0), 𝑒# = (0,1,0), 𝑒$ = (0,0,1) los vectores de la base canónica de ℝ$ . Se conocen por el
enunciado 𝑇(𝑒" ) = (1,0,0) y 𝑇(𝑒# ) = (1,1,0).
Sea además el vector 𝑒% = (1,1,1). Se observa que
𝑒% = (1,1,1) = 𝑒" + 𝑒# + 𝑒$
Por lo que, al tratarse de una aplicación lineal, también se tiene:
𝑇(𝑒% ) = 𝑇(𝑒" ) + 𝑇(𝑒# ) + 𝑇(𝑒$ )
Así, se puede despejar 𝑇(𝑒$ ):
𝑇(𝑒$ ) = 𝑇(𝑒% ) − 𝑇(𝑒" ) − 𝑇(𝑒# ) = (2,1,1) − (1,0,0) − (1,1,0) = (0,0,1)
Tenemos, pues, las transformaciones mediante T de todos los vectores de la base canónica, y por lo tanto
tenemos también ya la matriz de la transformación (que tiene por columnas 𝑇(𝑒" ), 𝑇(𝑒# ), 𝑇(𝑒$ )):
1 1 0
𝐴 = 90 1 0;
0 0 1
2. La transformación lineal será inyectiva si la dimensión del núcleo es cero.
El núcleo de la transformación lineal es:
nu(𝑇) = {𝑣 ∈ ℝ$ /𝐴 · 𝑣 = 0}
Para que la dimensión de este subespacio vectorial sea 0, debe haber 0 parámetros libres en su solución, es
decir, el sistema debe ser compatible determinado (al ser homogéneo, entonces admitirá solo la solución
trivial). Para ello, la dimensión de la imagen de T (rango de la matriz A) debe ser 3, lo cual se comprueba
inmediatamente viendo la matriz A, que estando en forma escalonada tiene 3 pivotes. Por lo tanto la
transformación es inyectiva.
NOTA: también es posible recordar que 𝑑𝑖𝑚jnu(𝑇)k = 𝑑𝑖𝑚(ℝ$ ) − 𝑑𝑖𝑚jIm(𝑇)k, pudiendo llegar así a la
misma conclusión (de que el rango de A debe ser 3 para ser inyectiva, como efectivamente ocurre).
______________________________________________________________________________________________

Pregunta 8. Construye una matriz 2x2 no diagonalizable con autovalor único 𝜆 = 4. Justifica la decisión
contestando razonadamente a las siguientes cuestiones:
a) (0,5p) Explica por qué su único autovalor es 4.
b) (0,5p) Obtén una base del subespacio propio de dicho autovalor.
c) (0,25p) ¿Por qué no es diagonalizable?

Respuesta
a) Un ejemplo fácil es:
4 1
𝐴=O  P
0 4
b) Como se trata de una matriz triangular con diagonal 4, su único autovalor es 𝜆 = 4 (tiene multiplicidad
algebraica 2).
```

#### Página 5

```text
(𝐴 − 𝜆 · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 4𝐼) · 𝑣 = 0
0 1  𝑥  0
O  P · O𝑦 P = O P
0 0  0
La solución de este sistema es (𝑥, 𝑦) = (0, 𝛼), con parámetro libre 𝛼 ∈ ℝ.
Así, el espacio propio asociado al autovalor 𝜆 = 4 es 𝐸& = {(𝑥, 𝑦) = (0, 𝛼) ∈ ℝ# , 𝛼 ∈ ℝ}.
Este subespacio vectorial tiene dimensión 1 (𝑚' (𝜆) = 1). Una base de este subespacio es {(0,1)}.

c) Como 𝑚' (𝜆) = 1 ≠ 𝑚( (𝜆) = 2, la matriz no es diagonalizable.

____________________________________________________________________________________________

Pregunta 9. Sea
3 0 0
𝐴 = 91 3 0 ;
0 0 −1

a) (0,5p) Obtén sus autovalores, indicando su multiplicidad algebraica, sin calcular determinantes.
b) (0,5p) Calcula una base del subespacio propio de el/los autovalores con multiplicidad algebraica 1.
c) (0,5p) ¿Es una matriz diagonalizable? Justifica tu respuesta.

Respuesta
a) Al ser una matriz triangular, los autovalores se ven directamente en su diagonal principal. Son 𝜆" = 3
(multiplicidad algebraica 2) y 𝜆# = −1 (multiplicidad algebraica 1).

b) (𝐴 − 𝜆# · 𝐼) · 𝑣 = 0 ⇒ (𝐴 + 𝐼) · 𝑣 = 0
4 0 0  𝑥  0
91 4 0; · r𝑦s = 90; → (𝑥, 𝑦, 𝑧) = (0,0, 𝛼), 𝛼 ∈ ℝ
0 0 0  𝑧  0
Así, el espacio propio del autovalor 𝜆# es 𝐸&! = {(𝑥, 𝑦, 𝑧) = (0,0, 𝛼) ∈ ℝ$ , 𝛼 ∈ ℝ}
Este subespacio vectorial tiene dimensión 1 (𝑚' (𝜆# ) = 1). Una base de este subespacio es {(0,0,1)}.

c)Para saber si es diagonalizable necesitamos conocer la multiplicidad algebraica del espacio propio
asociado al otro autovalor (para ver si coincide con su multiplicidad algebraica, 2).
(𝐴 − 𝜆" · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 3𝐼) · 𝑣 = 0
0 0 0  𝑥  0
𝑦
91 0 0 ; · r s = 90; → (𝑥, 𝑦, 𝑧) = (0, 𝛼, 0), 𝛼 ∈ ℝ
0 0 −4  𝑧  0
Así, el espacio propio del autovalor 𝜆" es 𝐸&" = {(𝑥, 𝑦, 𝑧) = (0, 𝛼, 0) ∈ ℝ$ , 𝛼 ∈ ℝ}
Este subespacio vectorial tiene dimensión 1, es decir, su multiplicidad geométrica es 𝑚' (𝜆" ) = 1 ≠
𝑚( (𝜆" ) = 2. Como la multiplicidad geométrica de este autovalor no coincide con su multiplicidad
algebraica, la matriz no es diagonalizable.
```


## CO · Teórico · Modelo B (con respuestas)

*Fuente: `EXÁMENES/CO/TEORICO/MPI1_2526_CO_ModB_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Ordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1,5h  Mod B

INSTRUCCIONES

•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en todas ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo contrario la
puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Sea 𝐴 una matriz de orden 5 tal que al aplicar el método de Gauss se obtiene una matriz
escalonada con cuatro filas no nulas

a) (0,25p) Determina el rango de 𝐴.
b) (0,25p) Decide si 𝐴 es invertible.
c) (0,5p) Razona si existe algún 𝒃 para el que 𝐴𝒙 = 𝒃 tenga solución única.

Respuesta
a) El rango de una matriz se define como el número de filas linealmente independientes, y no cambia al
aplicar transformaciones elementales por filas. Al aplicar el método de Gauss se obtiene una matriz
escalonada con cuatro filas no nulas y una fila nula. En una matriz escalonada cada fila no nula contiene un
pivote, y cada pivote corresponde a una fila linealmente independiente. Por tanto, rg (𝐴) = 4.

b) Una matriz cuadrada 𝑛 × 𝑛 es invertible si y solo si su rango es máximo, es decir:
rg (𝐴) = 𝑛.
En este caso:
•  𝐴 es 5 × 5,
•  pero su rango es 4 < 5.

Por tanto, 𝐴 no es invertible.

c) Al tener la forma escalonada de A una fila entera de ceros, el sistema 𝐴𝑥 = 𝑏 solo puede ser incompatible
(si la última fila de la forma escalonada de [𝐴 𝑏] tiene un último elemento no nulo) o compatible
indeterminado (si la forma escalonada de [𝐴 𝑏] tiene una última fila entera de ceros). Así, no existe ningún
vector b para el que el sistema 𝐴𝑥 = 𝑏 tenga solución única.
____________________________________________________________________________________________

Pregunta 2. ¿Cuál de las siguientes afirmaciones es cierta sobre la matriz dada? Razona tu respuesta en
cada apartado.
1 0 2 0
40 1 −1 3:
0 0 0 1
0 0 0 0
a) (0,25p) Está en la forma escalonada por filas.
b) (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, con infinitas
soluciones.
```

#### Página 2

```text
c)  (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, incompatible.
d)  (0,25p) Podría ser la matriz de coeficientes de un sistema de 4 ecuaciones con 4 incógnitas, incompatible.

Respuesta

a) SI es cierto al cumplir las tres condiciones para serlo
b) NO es cierto, ya que la penúltima fila implica que el sistema es incompatible.
c)  Es cierto, ya que las dimensiones cuadran (aunque “sobre” una ecuación), y la penúltima fila indica que
el sistema es incompatible.
d) Es cierto, ya que las dimensiones cuadran, y si el último elemento del vector de términos
independientes es distinto de cero, la matriz ampliada tendría una fila correspondiente a un sistema
incompatible.

____________________________________________________________________________________________

Pregunta 3. Sea
1 0 0
𝐴 = ; 3 1 0<
−2 0 1

a)  (0,5p) Describe qué transformaciones elementales representa 𝐴.
b)  (0,5p) Calcula 𝐴!" a partir de las transformaciones del apartado anterior

Respuesta

a) 𝐴 es la matriz correspondiente a la identidad tras aplicarle las siguientes transformaciones elementales:

𝑓# → 𝑓# + 3𝑓"
𝑓$ → 𝑓$ − 2𝑓"
b) La inversa de 𝐴 deshace dichas operaciones elementales, es decir, aplica:
𝑓$ → 𝑓$ + 2𝑓"
𝑓# → 𝑓# − 3𝑓"
Por tanto:
1 0 0
𝐴!" = ;−3 1 0<
2 0 1
____________________________________________________________________________________________

Pregunta 4. Sea V = ℝ$ y considérese el subconjunto
W = {(x, y, z) ∈ ℝ$ | 2x − y + z = 0}.

a) (0,5p) Justifica por qué W es un subespacio vectorial de ℝ$ .
b) (0,5p) Determina la dimensión de W.

Respuesta
a) El conjunto W es el conjunto de soluciones de una ecuación lineal homogénea.
Por tanto:
•  contiene al vector nulo,
•  es cerrado para la suma,
•  es cerrado para el producto por escalares.

Luego, W es un subespacio vectorial de ℝ$ .
```

#### Página 3

```text
b) W está definido por una única ecuación lineal independiente en ℝ$ .
Por tanto:
𝑑𝑖𝑚 (𝑊) = 3 − 1 = 2
____________________________________________________________________________________________

0 −1
Pregunta 5. (1p) Hallar todas las matrices reales que conmutan con la matriz A = P  Q
1 0

Respuesta
𝑎  𝑏
La matriz buscada es una matriz 𝐵 = S  V tal que A·B = B·A
𝑐  𝑑
−𝑐 = 𝑏
0 −1 𝑎  𝑏  𝑎  𝑏 0 −1  −𝑑 = −𝑎  𝑏 = −𝑐
𝐴𝐵 = 𝐵𝐴 ⟹ S  V·S  V=S  V·S  V⟹Y  ⟹Z
1 0  𝑐  𝑑  𝑐  𝑑 1 0  𝑎=𝑑  𝑎=𝑑
𝑏 = −𝑐

𝑎  −𝑐
Por tanto, existen infinitas matrices que conmutan con la matriz A y vienen dadas por P  , ∀ 𝑎, 𝑐 ∈ ℝ
𝑐  𝑎Q

____________________________________________________________________________________________

Pregunta 6. Sea 𝑓(𝑥): ℝ$ → ℝ$ una aplicación lineal con matriz asociada 𝐴 respecto de las bases canónicas,
cuyo subespacio imagen está dado por:
𝐼𝑚(𝑓) = {(𝑥, 𝑦 𝑧) 𝜖 ℝ$ ; 𝑥 − 𝑦 + 𝑧 = 0}
Se pide:

a)  (0.5p) Determinar la dimensión del espacio imagen y el rango de la matriz 𝐴
b) (0,5p) Clasificar razonadamente el sistema lineal 𝐴 ∙ 𝒙 = ;2<, indicando si es compatible determinado,
compatible indeterminado o incompatible, sin calcular la matriz 𝐴 ni determinantes, justificando la respuesta
a partir de la información del subespacio imagen.
Respuesta

a)  El subespacio imagen está definido por la ecuación:

𝑥−𝑦+𝑧 =0
$
Esto describe un plano en ℝ , por tanto dim(𝐼𝑚(𝑓))=2.
Como el rango de la matriz 𝐴 coincide con la dimensión del espacio imagen: 𝑟(𝐴) = 2.

b)  El sistema lineal 𝐴 ∙ 𝒙 = ;2< será compatible si el vector del término independiente pertenece al espacio
imagen, es decir, si cumple la condición: 𝑥 − 𝑦 + 𝑧 = 0
para 𝒗 = (1, 2, 0)
1 − 2 + 0 = −1 ≠ 0
Por tanto: 𝒗 ∉ 𝐼𝑚(𝑓)

El sistema es incompatible (no tiene solución), porque el término independiente no pertenece al subespacio
imagen.
____________________________________________________________________________________________

Pregunta 7. Sea 𝑇: ℝ$ → ℝ$ una transformación lineal, tal que:
𝑇(1,0,0) = (1,1,0)
```

#### Página 4

```text
𝑇(0,1,0) = (0,1,0)
𝑇(1,1,1) = (1,2,1)
a) (1p) Determina la matriz de 𝑇 en la base canónica.
b) (0,25p) Decide si 𝑇 es inyectiva.

Respuesta
1. Sean 𝒆" = (1,0,0), 𝒆# = (0,1,0), 𝒆$ = (0,0,1) los vectores de la base canónica de ℝ$ . Se conocen por el
enunciado 𝑇(𝒆" ) = (1,1,0) y 𝑇(𝒆# ) = (0,1,0).
Sea además el vector 𝒆% = (1, 1, 1). Se observa que
𝒆% = (1, 1, 1) = 𝒆" + 𝒆# + 𝒆$
Por lo que, al tratarse de una aplicación lineal, también se tiene:
𝑇(𝒆% ) = 𝑇(𝒆" ) + 𝑇(𝒆# ) + 𝑇(𝒆$ )
Así, se puede despejar 𝑇(𝒆$ ):
𝑇(𝒆$ ) = 𝑇(𝒆% ) − 𝑇(𝒆" ) − 𝑇(𝒆𝟐 ) = (1, 2, 1) − (1, 1, 0) − (0, 1, 0) = (0, 0, 1)
Tenemos, pues, las transformaciones mediante T de todos los vectores de la base canónica, y por lo tanto
tenemos también ya la matriz de la transformación (que tiene por columnas 𝑇(𝑒" ), 𝑇(𝑒# ), 𝑇(𝑒$ )):
1 0 0
𝐴 = ;1 1 0<
0 0 1
2. La transformación lineal será inyectiva si la dimensión del núcleo es cero.
El núcleo de la transformación lineal es:
nu(𝑇) = {𝑣 ∈ ℝ$ /𝐴 · 𝑣 = 0}
Para que la dimensión de este subespacio vectorial sea 0, debe haber 0 parámetros libres en su solución, es
decir, el sistema debe ser compatible determinado (al ser homogéneo, entonces admitirá solo la solución
trivial). Para ello, la dimensión de la imagen de T (rango de la matriz A) debe ser 3, lo cual se comprueba
inmediatamente viendo la matriz A, que estando en forma escalonada tiene 3 pivotes. Por lo tanto la
transformación es inyectiva.
NOTA: también es posible recordar que 𝑑𝑖𝑚nnu(𝑇)o = 𝑑𝑖𝑚(ℝ$ ) − 𝑑𝑖𝑚nIm(𝑇)o, pudiendo llegar así a la
misma conclusión (de que el rango de A debe ser 3 para ser inyectiva, como efectivamente ocurre).
______________________________________________________________________________________________

Pregunta 8. Construye una matriz 2x2 no diagonalizable con autovalor único 𝜆 = 1. Justifica la decisión
contestando razonadamente a las siguientes cuestiones:
a) (0,5p) Explica por qué su único autovalor es 1.
b) (0,5p) Obtén una base del subespacio propio de dicho autovalor.
c) (0,25p) ¿Por qué no es diagonalizable?

Respuesta
a) Un ejemplo fácil es:
1 1
𝐴=P  Q
0 1
Como se trata de una matriz triangular con diagonal 1, su único autovalor es 𝜆 = 1 (tiene multiplicidad
algebraica 2).
b)
(𝐴 − 𝜆 · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 1 · 𝐼) · 𝑣 = 0
0 1  𝑥  0
P  Q · P𝑦 Q = P Q
0 0  0
La solución de este sistema es (𝑥, 𝑦) = (0, 𝛼), con parámetro libre 𝛼 ∈ ℝ.
Así, el espacio propio asociado al autovalor 𝜆 = 1 es 𝐸' = {(𝑥, 𝑦) = (0, 𝛼) ∈ ℝ# , 𝛼 ∈ ℝ}.
Este subespacio vectorial tiene dimensión 1 (𝑚( (𝜆) = 1). Una base de este subespacio es {(0,1)}.

c) Como 𝑚( (𝜆) = 1 ≠ 𝑚) (𝜆) = 2, la matriz no es diagonalizable.
```

#### Página 5

```text
____________________________________________________________________________________________

Pregunta 9. Sea
2 1 0
𝐴 = ;0 2 0<
0 0 3

a) (0,5p) Obtén sus autovalores, indicando su multiplicidad algebraica, sin calcular determinantes.
b) (0,5p) Calcula una base del subespacio propio de el/los autovalores con multiplicidad algebraica 1.
c) (0,5p) ¿Es una matriz diagonalizable? Justifica tu respuesta.

Respuesta
a) Al ser una matriz triangular, los autovalores se ven directamente en su diagonal principal. Son 𝜆" = 2
(multiplicidad algebraica 2) y 𝜆# = 3 (multiplicidad algebraica 1).

b) (𝐴 − 𝜆# · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 3𝐼) · 𝑣 = 0
−1 1 0  𝑥  0
; 0 −1 0< · v𝑦w = ;0< → (𝑥, 𝑦, 𝑧) = (0,0, 𝛼), 𝛼 ∈ ℝ
0  0 0  𝑧  0
Así, el espacio propio del autovalor 𝜆# es 𝐸'! = {(𝑥, 𝑦, 𝑧) = (0,0, 𝛼) ∈ ℝ$ , 𝛼 ∈ ℝ}
Este subespacio vectorial tiene dimensión 1 (𝑚( (𝜆# ) = 1). Una base de este subespacio es {(0,0,1)}.

c)Para saber si es diagonalizable necesitamos conocer la multiplicidad algebraica del espacio propio
asociado al otro autovalor (para ver si coincide con su multiplicidad algebraica, 2).
(𝐴 − 𝜆" · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 2𝐼) · 𝑣 = 0
0 1 0  𝑥  0
;0 0 0< · v𝑦w = ;0< → (𝑥, 𝑦, 𝑧) = (𝛼, 0, 0), 𝛼 ∈ ℝ
0 0 1  𝑧  0
Así, el espacio propio del autovalor 𝜆" es 𝐸'" = {(𝑥, 𝑦, 𝑧) = (𝛼, 0, 0) ∈ ℝ$ , 𝛼 ∈ ℝ}
Este subespacio vectorial tiene dimensión 1, es decir, su multiplicidad geométrica es 𝑚( (𝜆" ) = 1 ≠
𝑚) (𝜆" ) = 2. Como la multiplicidad geométrica de este autovalor no coincide con su multiplicidad
algebraica, la matriz no es diagonalizable.
```


## CO · Teórico · Modelo C (con respuestas)

*Fuente: `EXÁMENES/CO/TEORICO/MPI1_2526_CO_ModC_resp.pdf`*

#### Página 1

```text
Escuela Politécnica Superior  CALIFICACIÓN:
1er Curso · Grado en Ingeniería Informática
MPI 1· Examen Convocatoria Ordinaria · Curso 2025/26

NOMBRE Y APELLIDOS

CURSO  1º  Grupo  Duración: 1,5h  Mod C

INSTRUCCIONES

•  Entrega esta hoja con tu nombre y todas las que necesites con las respuestas. Escribe tu nombre en todas ellas.
•  Indica las operaciones elementales cuando emplees el Método de Gauss
•  Este es un examen de teoría por lo que debes detallar el razonamiento en cada pregunta, de lo contrario la
puntuación será <50% de los puntos de la pregunta
______________________________________________________________________________________________

Pregunta 1. Sea 𝐴 una matriz de orden 3 tal que al aplicar el método de Gauss se obtiene una matriz
escalonada con dos filas no nulas

a) (0,25p) Determina el rango de 𝐴.
b) (0,25p) Decide si 𝐴 es invertible.
c) (0,5p) Razona si existe algún 𝒃 para el que 𝐴𝒙 = 𝒃 tenga solución única.

Respuesta
a) El rango de una matriz se define como el número de filas linealmente independientes, y no cambia al
aplicar transformaciones elementales por filas. Al aplicar el método de Gauss se obtiene una matriz
escalonada con dos filas no nulas y una fila nula. En una matriz escalonada cada fila no nula contiene un
pivote, y cada pivote corresponde a una fila linealmente independiente. Por tanto, rg (𝐴) = 2.

b) Una matriz cuadrada 𝑛 × 𝑛 es invertible si y solo si su rango es máximo, es decir:
rg (𝐴) = 𝑛.
En este caso:
•  𝐴 es 3 × 3,
•  pero su rango es 2 < 3.

Por tanto, 𝐴 no es invertible.

c) Al tener la forma escalonada de A una fila entera de ceros, el sistema 𝐴𝑥 = 𝑏 solo puede ser incompatible
(si la última fila de la forma escalonada de [𝐴 𝑏] tiene un último elemento no nulo) o compatible
indeterminado (si la forma escalonada de [𝐴 𝑏] tiene una última fila entera de ceros). Así, no existe ningún
vector 𝒃 para el que el sistema 𝐴𝒙 = 𝒃 tenga solución única.
____________________________________________________________________________________________

Pregunta 2. ¿Cuál de las siguientes afirmaciones es cierta sobre la matriz dada? Razona tu respuesta en
cada apartado.
1 0 2 0
40 0 1 3 8
0 0 0 −1
0 0 0 0
a) (0,25p) Está en la forma escalonada por filas.
b) (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, con infinitas
soluciones.
```

#### Página 2

```text
c)  (0,25p) Podría ser la matriz ampliada de un sistema con 4 ecuaciones y 3 incógnitas, incompatible.
d)  (0,25p) Podría ser la matriz de coeficientes de un sistema de 4 ecuaciones con 4 incógnitas, incompatible.

Respuesta

a) NO es cierto el elemento no nulo de la 3ª fila debe ser 1 no −1
b) NO es cierto, ya que la penúltima fila implica que el sistema es incompatible.
c)  Es cierto, ya que las dimensiones cuadran (aunque “sobre” una ecuación), y la penúltima fila indica que
el sistema es incompatible.
d) Es cierto, ya que las dimensiones cuadran, y si el último elemento del vector de términos
independientes es distinto de cero, la matriz ampliada tendría una fila correspondiente a un sistema
incompatible.

____________________________________________________________________________________________

Pregunta 3. Sea
1 −2 0
𝐴 = 90 1 0:
0 3 1

a)  (0,5p) Describe qué transformaciones elementales representa 𝐴.
b)  (0,5p) Calcula 𝐴!" a partir de las transformaciones del apartado anterior

Respuesta

a) 𝐴 es la matriz correspondiente a la identidad tras aplicarle las siguientes transformaciones elementales:

𝑓" → 𝑓" − 2𝑓#
𝑓$ → 𝑓$ + 3𝑓#
b) La inversa de 𝐴 deshace dichas operaciones elementales, es decir, aplica:
𝑓" → 𝑓" + 2𝑓#
𝑓$ → 𝑓$ − 3𝑓#
Por tanto:
1 2 0
𝐴!" = 90 1 0:
0 −3 1
____________________________________________________________________________________________

Pregunta 4. Considérese el subconjunto
W = {(x, y, z) ∈ ℝ$ | x − 2y + 3z = 0 , 2x − y + z = 0}.

a) (0,5p) Justifica por qué W es un subespacio vectorial de ℝ$ .
b) (0,5p) Determina la dimensión de W.

Respuesta
a) El conjunto W es el conjunto de soluciones de un sistema de ecuaciones lineales homogéneo.
Por tanto:
•  contiene al vector nulo,
•  es cerrado para la suma,
•  es cerrado para el producto por escalares.

Luego, W es un subespacio vectorial de ℝ$ .
```

#### Página 3

```text
b) W está definido por:
1 −2 3  1 −2 3  1 −2 3
H  I~H  I~L
2 −1 1  0 3 −5  0 1 −5/3N
Como me queda 1 variable libre 𝑑𝑖𝑚 (𝑊) = 1

____________________________________________________________________________________________

1 −2
Pregunta 5. (1p) Hallar todas las matrices reales que conmutan con la matriz A = T  U
2 1

Respuesta
𝑎  𝑏
La matriz buscada es una matriz 𝐵 = H  I tal que A·B = B·A
𝑐  𝑑
𝑎 − 2𝑐 = 𝑎 + 2𝑏
1 −2 𝑎  𝑏  𝑎  𝑏 1 −2  2𝑎 + 𝑐 = 𝑐 + 2𝑑  𝑏 = −𝑐
𝐴𝐵 = 𝐵𝐴 ⟹ H  I·H  I=H  I·H  I⟹[  ⟹\
2 1  𝑐  𝑑  𝑐  𝑑 2 1  𝑏 − 2𝑑 = −2𝑎 + 𝑏  𝑎=𝑑
2𝑏 + 𝑑 = −2𝑐 + 𝑑

𝑎  −𝑐
Por tanto, existen infinitas matrices que conmutan con la matriz A y vienen dadas por T  , ∀ 𝑎, 𝑐 ∈ ℝ
𝑐  𝑎U

____________________________________________________________________________________________

Pregunta 6. Sea 𝑓(𝑥): ℝ$ → ℝ$ una aplicación lineal con matriz asociada 𝐴 respecto de las bases canónicas,
cuyo subespacio imagen está dado por:
𝐼𝑚(𝑓) = {(𝑥, 𝑦 𝑧) 𝜖 ℝ$ ; 3𝑥 − 2𝑦 − 𝑧 = 0}
Se pide:

a)  (0.5p) Determinar la dimensión del espacio imagen y el rango de la matriz 𝐴
b) (0,5p) Clasificar razonadamente el sistema lineal 𝐴 ∙ 𝒙 = 91:, indicando si es compatible determinado,
compatible indeterminado o incompatible, sin calcular la matriz 𝐴 ni determinantes, justificando la respuesta
a partir de la información del subespacio imagen.
Respuesta

a)  El subespacio imagen está definido por la ecuación:

3𝑥 − 2𝑦 − 𝑧 = 0
$
Esto describe un plano en ℝ , por tanto dim(𝐼𝑚(𝑓))=2.
Como el rango de la matriz 𝐴 coincide con la dimensión del espacio imagen: 𝑟(𝐴) = 2.

b)  El sistema lineal 𝐴 ∙ 𝒙 = 91: será compatible si el vector del término independiente pertenece al espacio
imagen, es decir, si cumple la condición: 3𝑥 − 2𝑦 − 𝑧 = 0
para 𝒗 = (1, 1, 1)
3−2−1=0
Por tanto: 𝒗 ∈ 𝐼𝑚(𝑓)

El sistema es compatible indeterminado porque el término independiente pertenece al subespacio imagen,
pero éste tiene dimensión menor que el espacio de llegada
____________________________________________________________________________________________
```

#### Página 4

```text
Pregunta 7. Sea 𝑇: ℝ$ → ℝ$ una transformación lineal, tal que:
𝑇(1,0,0) = (1,1,1)
𝑇(0,1,0) = (1,1,0)
𝑇(1,1,1) = (0,2,0)
a) (1p) Determina la matriz de 𝑇 en la base canónica.
b) (0,25p) Decide si 𝑇 es inyectiva.

Respuesta
1. Sean 𝒆" = (1,0,0), 𝒆# = (0,1,0), 𝒆$ = (0,0,1) los vectores de la base canónica de ℝ$ . Se conocen por el
enunciado 𝑇(𝒆" ) = (1,1,1) y 𝑇(𝒆# ) = (1,1,0).
Sea además el vector 𝒆% = (1,1,1). Se observa que
𝒆% = (1, 1, 1) = 𝒆" + 𝒆# + 𝒆$
Por lo que, al tratarse de una aplicación lineal, también se tiene:
𝑇(𝒆% ) = 𝑇(𝒆" ) + 𝑇(𝒆# ) + 𝑇(𝒆$ )
Así, se puede despejar 𝑇(𝑒$ ):
𝑇(𝑒$ ) = 𝑇(𝑒% ) − 𝑇(𝑒" ) − 𝑇(𝑒# ) = (0, 2, 0) − (1, 1, 1) − (1, 1 ,0) = (−2, 0, −1)
Tenemos, pues, las transformaciones mediante T de todos los vectores de la base canónica, y por lo tanto
tenemos también ya la matriz de la transformación (que tiene por columnas 𝑇(𝑒" ), 𝑇(𝑒# ), 𝑇(𝑒$ )):
1 1 −2
𝐴 = 91 1 0 :
1 0 −1
2. La transformación lineal será inyectiva si la dimensión del núcleo es cero.
El núcleo de la transformación lineal es:
nu(𝑇) = {𝑣 ∈ ℝ$ /𝐴 · 𝑣 = 0}
Para que la dimensión de este subespacio vectorial sea 0, debe haber 0 parámetros libres en su solución, es
decir, el sistema debe ser compatible determinado (al ser homogéneo, entonces admitirá solo la solución
trivial). Para ello, la dimensión de la imagen de T (rango de la matriz A) debe ser 3,

1 1 −2  1 1 −2  1 1 −2
91 1 0 : ~ 90 0  2 : ~ 90 1 −1:
1 0 −1  0 −1 1  0 0 1
la matriz A, estando en forma escalonada tiene 3 pivotes. Por lo tanto la transformación es inyectiva.
NOTA: también es posible recordar que 𝑑𝑖𝑚mnu(𝑇)n = 𝑑𝑖𝑚(ℝ$ ) − 𝑑𝑖𝑚mIm(𝑇)n, pudiendo llegar así a la
misma conclusión (de que el rango de A debe ser 3 para ser inyectiva, como efectivamente ocurre).
______________________________________________________________________________________________

Pregunta 8. Construye una matriz 2x2 no diagonalizable con autovalor único 𝜆 = 2. Justifica la decisión
contestando razonadamente a las siguientes cuestiones:
a) (0,5p) Explica por qué su único autovalor es 2
b) (0,5p) Obtén una base del subespacio propio de dicho autovalor.
c) (0,25p) ¿Por qué no es diagonalizable?

Respuesta
a) Un ejemplo fácil es:
2 1
𝐴=T  U
0 2
Como se trata de una matriz triangular con diagonal 2, su único autovalor es 𝜆 = 2 (tiene multiplicidad
algebraica 2).
b)
(𝐴 − 𝜆 · 𝐼) · 𝑣 = 0 ⇒ (𝐴 − 2 · 𝐼) · 𝑣 = 0
0 1  𝑥  0
T  U · T𝑦 U = T U
0 0  0
La solución de este sistema es (𝑥, 𝑦) = (0, 𝛼), con parámetro libre 𝛼 ∈ ℝ.
```

#### Página 5

```text
Así, el espacio propio asociado al autovalor 𝜆 = 1 es 𝐸& = {(𝑥, 𝑦) = (0, 𝛼) ∈ ℝ# , 𝛼 ∈ ℝ}.
Este subespacio vectorial tiene dimensión 1 (𝑚' (𝜆) = 1). Una base de este subespacio es {(0,1)}.

c) Como 𝑚' (𝜆) = 1 ≠ 𝑚( (𝜆) = 2, la matriz no es diagonalizable.

____________________________________________________________________________________________

Pregunta 9. Sea
−1 1 0
𝐴 = 9 0 2 0:
0 0 2

a) (0,5p) Obtén sus autovalores, indicando su multiplicidad algebraica, sin calcular determinantes.
b) (0,5p) Calcula una base del subespacio propio de el/los autovalores con multiplicidad algebraica 1.
c) (0,5p) ¿Es una matriz diagonalizable? Justifica tu respuesta.

Respuesta
a) Al ser una matriz triangular, los autovalores se ven directamente en su diagonal principal. Son 𝜆" = 2
(multiplicidad algebraica 2) y 𝜆# = −1 (multiplicidad algebraica 1).

b) Calculamos la base de 𝜆# = −1
(𝐴 − 𝜆# · 𝐼) · 𝑣 = 0 ⇒ (𝐴 + 𝐼) · 𝑣 = 0
0 1 0  𝑥  0
90 3 0: · v𝑦w = 90: → (𝑥, 𝑦, 𝑧) = (𝛼, 0 ,0), 𝛼 ∈ ℝ
0 0 3  𝑧  0
Así, el espacio propio del autovalor 𝜆# es 𝐸&! = {(𝑥, 𝑦, 𝑧) = (𝛼, 0 ,0) ∈ ℝ$ , 𝛼 ∈ ℝ}
Este subespacio vectorial tiene dimensión 1 (𝑚' (𝜆# ) = 1). Una base de este subespacio es {(1, 0, 0)}.

c) Para saber si es diagonalizable necesitamos conocer la multiplicidad algebraica del espacio propio
asociado al otro autovalor 𝜆" = 2 (para ver si coincide con su multiplicidad algebraica, 2).
(𝐴 − 𝜆" · 𝐼) · 𝒗 = 0 ⇒ (𝐴 − 2𝐼) · 𝒗 = 𝟎
−3 1 0  𝑥  0  𝑥 = 𝑠/3
9 0 0 0: · v𝑦w = 90: → y 𝑦 = 𝑠
0 0 0  𝑧  0  𝑧=𝑡
Tenemos dos variables libres 𝑦 = 𝑠, 𝑧 = 𝑡 despejamos la otra: 𝑥 = 𝑠/3 por tanto, las soluciones tienen la
forma:
𝑥  1/3  0
|𝑦} = 𝑠 · ~ 1 • + 𝑡 · ~1•
𝑧  0  0

Así, el espacio propio del autovalor 𝜆" = 2 está generado por los vectores: (1, 3, 0), (0, 1, 0)
Este subespacio vectorial tiene dimensión 2, es decir, su multiplicidad geométrica es 𝑚' (𝜆" ) = 2 =
𝑚( (𝜆" ) = 2. Como la multiplicidad geométrica de este autovalor coincide con su multiplicidad algebraica,
la matriz es diagonalizable.
```


## CO · Práctico · AR01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/AR01.mlx`*

#### AR01. Rack “pop-up” para un evento e-sports

Una asociación juvenil organiza un evento e-sports de fin de semana en el que se celebrarán competiciones online, retransmisiones en directo (streaming), análisis de partidas y generación de contenido para redes sociales. Para ello, se va a instalar un rack temporal de servidores, es decir, un armario técnico que agrupa varios equipos informáticos conectados entre sí y a Internet, y que permite concentrar capacidad de cálculo, almacenamiento y comunicaciones en un mismo punto.

El proveedor ofrece tres tipos de nodos que pueden instalarse en el rack. Cada tipo tiene unas prestaciones fijas en términos de memoria, capacidad gráfica y ancho de banda de red:

Tipo de nodo

RAM (GB)

Unidades GPU

Ancho de banda (Gbps)

Nano

8

4

5

Pro

16

6

8

Ultra

32

10

12

Para que el evento pueda desarrollarse correctamente durante todo el fin de semana, el rack debe proporcionar exactamente:

- 480 GB de RAM

- 190 unidades GPU

- 240 Gbps de ancho de banda

Se pide:

a) (0,6p) Define las variables y escribe, con el editor de ecuaciones el sistema de ecuaciones lineales que modela el problema.

b) (0,4p) Escribe, mediante el editor de ecuaciones, la ecuación matricial correspondiente al sistema

c) (0,7p) Resuelve el sistema con MATLAB utilizando el comando A\b y muestra por pantalla cuántos nodos de cada tipo deben instalarse.

d) (0,4p) Comprueba que la solución obtenida satisface las tres restricciones del problema.

e) (0,4p) Si los precios son: Nano = 900 €, Pro = 1300 €, Ultra = 2200 €, calcula con MATLAB el coste total del rack instalado e imprimelo por consola.

Respuesta


## CO · Práctico · AR02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/AR02.mlx`*

#### AR02. Organización de un retiro universitario

El área de Pastoral Universitaria de la UFV organiza un retiro de fin de semana para alumnos de distintos grados. Durante el evento se llevarán a cabo actividades de acompañamiento personal, dinámicas de grupo y sesiones de reflexión. Para ello, se cuenta con tres tipos de colaboradores voluntarios, cada uno con un perfil y una dedicación diferente:

Tipo de colaborador

Horas de acompañamiento

Dinámicas de grupo

Sesiones de reflexión

Monitor

4

2

1

Coordinador

6

3

2

Formador

10

2

4

Para que el retiro pueda desarrollarse correctamente, se necesita cubrir exactamente:

- 276 horas de acompañamiento personal

- 108 dinámicas de grupo

- 92 sesiones de reflexión

Se pide:

a) (0,6p) Define las variables y escribe, con el editor de ecuaciones el sistema de ecuaciones lineales que modela el problema.

b) (0,4p) Escribe, mediante el editor de ecuaciones, la ecuación matricial correspondiente al sistema

c) (0,7p) Resuelve el sistema con MATLAB utilizando el comando A\b y muestra por pantalla cuántos colaboradores de cada tipo son necesarios.

d) (0,4p) Comprueba que la solución obtenida satisface todas las necesidades del retiro.

e) (0,4p) Si el coste de formación y coordinación por colaborador es: Monitor = 150 €, Coordinador = 250 €, Formador = 400 €, calcula con MATLAB el coste total de la organización

Respuesta


## CO · Práctico · DC01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/DC01.mlx`*

#### DC01. Distribución de calor en la pasta térmica de un portátil

En un portátil, el procesador (CPU) está unido al disipador mediante una capa fina de pasta térmica (gel térmico). Para estudiar si el contacto térmico es uniforme, modelamos la pasta térmica como una placa 2D y aproximamos la temperatura en 4 puntos interiores (una malla 2x2) suponiendo equilibrio estacionario.

La malla interior es:

$$\left\lbrack \begin{array}{cc}
T_1  & T_2 \\
T_3  & T_4
\end{array}\right\rbrack$$

y la condición de equilibrio en cada punto interior es:

$$T_i =\frac{1}{4}\left(\textrm{vecino}\;\textrm{norte}+\textrm{vecino}\;\textrm{sur}+\textrm{vecino}\;\textrm{este}+\textrm{vecino}\;\textrm{oeste}\right)$$

Las temperaturas en los bordes externos (en ºC) son constantes:

- Borde superior (norte): 70ºC

- Borde inferior (sur): 30ºC

- Borde izquierdo (oeste): 60ºC

- Borde derecho (este): 40ºC

Por último, se sabe además que cuando la temperatura media interior de la placa supera los 50ºC, el sistema entra en modo "súper refrigeración", incrementando la velocidad de giro de los ventiladores.

Se pide:

a) (1.0p) Plantea, con el editor de ecuaciones, las ecuaciones de equilibrio para $T_1 ,T_2 ,T_3 ,T_4$ y reescríbelas en forma matricial $\textrm{AT}=b$, indicando $A$, $T$ y $b$.

b) (0.75p) Resuelve el sistema con MATLAB usando A\b y muestra en pantalla $T_1 ,T_2 ,T_3 ,T_4$ con dos decimales.

c) (0.75p) ¿Entrará el sistema en modo "súper refrigeración"? Realiza los cálculos pertinentes con código MATLAB e imprime por pantalla la información que consideres oportuna.

Respuesta


## CO · Práctico · DC02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/DC02.mlx`*

#### DC02. Distribución de calor en el pavimento estructural exterior de la EPS

Durante un día soleado en el campus de la UFV, la estructura metálica blanca y el pavimento exterior adyacente al edificio de la Escuela Politécnica Superior (EPS), junto al Ágora, se calientan de forma no uniforme por el sol, la sombra y el viento. Para estudiar cómo se distribuye el calor en una porción de ese pavimento, se considera una malla interior 2x2 de puntos cuya temperatura $T_i$ se desea conocer.

Denotamos las temperaturas interiores (en ºC) como:

$$\left\lbrack \begin{array}{cc}
T_1  & T_2 \\
T_3  & T_4
\end{array}\right\rbrack$$

Suponemos el modelo clásico de equilibrio:

$$T_i =\frac{1}{4}\left(\textrm{Norte}+\textrm{Sur}+\textrm{Este}+\textrm{Oeste}\right)$$

A una hora concreta del día:

- El lado Este está parcialmente en sombra por la estructura blanca, y por eso está algo más fresco.

- La zona Sur (más cerca del suelo que acumula calor y con menos corriente) está algo más caliente que la Norte (más expuesta al viento y refresca algo más).

Las temperaturas de contorno medidas (en ºC) son:

- Borde superior (norte): 34 ºC

- Borde inferior (sur): 40 ºC

- Borde izquierdo (oeste): 38 ºC

- Borde derecho (este): 32 ºC

Además, gracias a un reciente proyecto de alumnos del Grado en Ingeniería Informática de la UFV, se han instalado sensores térmicos en la estructura, conectados a un procesador de datos, que hace saltar una alarma cuando la temperatura media de la zona estudiada supera los 36º.

Se pide:

a) (1.0p) Plantea, con el editor de ecuaciones, las ecuaciones de equilibrio para $T_1 ,T_2 ,T_3 ,T_4$ y reescríbelas en forma matricial $\textrm{AT}=b$, indicando $A$, $T$ y $b$.

b) (0.75p) Resuelve el sistema con MATLAB usando A\b y muestra en pantalla $T_1 ,T_2 ,T_3 ,T_4$ con dos decimales.

c) (0.75p) ¿Saltará la alarma? Realiza los cálculos pertinentes con código MATLAB, imprimiendo en pantalla lo que consideres oportuno.

Respuesta


## CO · Práctico · FR01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/FR01.mlx`*

#### CO (Flujo de Redes). Distribución de flujos en una red eléctrica

Se condiera una red de flujo de pontencia con cutatro nodos; A, B, C, y D. La conexiones entre nodos están representada por líneas dirigidas, con los siguientes entidos y vaiables de flujo (en kW, potencia activa) .

[Imagen: Red eléctrica: 500 kW entran en A; $q_1$: A→B, $q_6$: A→D, $q_2$: D→B, $q_3$: B→C, $q_4$: C→B, $q_5$: D→C; autoconsumos 50 kW en B, 300 kW en C, 150 kW en D.]

En el nodo A existe una fuente que inyecta 500 kW en la red. Los nodos B, C, y D tiene autconsumos locales (sumideros internos) con el siguiente valor (recuerda tratarlos como flujos salientes):

$$\textrm{autoconsumo}\;\textrm{en}\;\;B=50\;kW$$

$$\textrm{autoconsumo}\;\textrm{en}\;C=300\;kW$$

$$\textrm{autoconsumo}\;\textrm{en}\;D=150\;\textrm{kW}$$

La variables q representan potencias activad (en KW) que fluyen por la líneas de la red en el sentido indicado por las flechas del diagrama.

$$q_1 :\textrm{potencia}\;\textrm{de}\;A\longrightarrow B$$

$$q_2 :\textrm{potencia}\;\textrm{de}\;D\longrightarrow B$$

$$q_3 :\textrm{potencia}\;\;\textrm{de}\;B\longrightarrow C$$

$$q_4 :\textrm{potencia}\;\;\textrm{de}\;C\longrightarrow B$$

$$q_5 :\textrm{potencia}\;\textrm{de}\;D\longrightarrow C$$

$$q_6 :\textrm{potencia}\;\;\textrm{de}\;A\longrightarrow D$$

Se pide:

a) (0,5 p) Plantea el sistema de ecuaciones que describe el flujo en cada nodo (A, B, C, D).

b) (0,5 p) Escribe el sistema en forma matricial.A q = b, A matriz de fjujos asociados, q las potencias y b los kW

c) (0,75 p) Calcula una solución numérica para los flujos suponiendo:

$$\begin{array}{l}
q_2 =100\;\textrm{kW}\\
q_3 =200\;\textrm{kW}\\
q_5 =150\;\textrm{kW}
\end{array}$$

Y comprueba que los balances de potencia en los nodos A, B, C y D son nulos.

d) (0,75 p) Si la línea D→B se desconecta ($q_2$,=0) calcula una solución viable suponiendo:

$$q_3 =200\;\textrm{kW}$$

$$q_5 =150\;\textrm{kW}$$

y comprueba que los balances de potencia en los nodos A, B, C y D son nulos.

Respuesta.

_Imágenes embebidas: 1 (image1.jpeg)_


## CO · Práctico · FR02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/FR02.mlx`*

#### CO (Flujo de Redes). Distribución de flujos en una red eléctrica

Se condiera una red de flujo de pontencia con cutatro nodos; A, B, C, y D. La conexiones entre nodos están reprsentada por líneas dirigidas, con los siguientes entidos y vaiables de flujo (en kW, potencia activa) .

[Imagen: Red eléctrica: 500 kW entran en A; $q_{AB}$, $q_{AC}$, $q_{BC}$, $q_{BD}$, $q_{CD}$, $q_{DB}$; autoconsumos $L_B=150$ kW, $L_C=100$ kW, $L_D=250$ kW.]

En el nodo A existe una fuente que inyecta $A_{\textrm{in}} =500\;\textrm{kW}$ en la red. Los nodos B, C, y D tiene autconsumos locales  con el siguiente valor (recuerda tratarlos como flujos salientes):

$$\textrm{autoconsumo}\;\textrm{en}\;\;L_B =150\;kW$$

$$\textrm{autoconsumo}\;\textrm{en}\;L_C =100\;kW$$

$\textrm{autoconsumo}\;\textrm{en}\;L_D =250\;\textrm{kW}$,

Luego hay un cierre energético $A_{\textrm{in}} =L_B +L_C +L_D$

La variables q representan potencias activad (en KW) que fluyen por la líneas de la red en el sentido indicado por las flechas del diagrama.

$$q_{\textrm{AB}} :\textrm{potencia}\;\textrm{de}\;A\longrightarrow B$$

$$q_{\textrm{AC}} :\textrm{potencia}\;\textrm{de}\;A\longrightarrow C$$

$$q_{\textrm{BC}} :\textrm{potencia}\;\;\textrm{de}\;B\longrightarrow C$$

$$q_{\textrm{BD}} :\textrm{potencia}\;\;\textrm{de}\;B\longrightarrow D$$

$$q_{\textrm{CD}} :\textrm{potencia}\;\textrm{de}\;C\longrightarrow D$$

$$q_{\textrm{DB}} :\textrm{potencia}\;\;\textrm{de}\;D\longrightarrow B$$

Se recomienda utilizar la convención de balance: entradas + inyección = salidas + autoconsumo.

Se pide:

a) (0,5 p) Plantea el sistema de ecuaciones que describe el flujo en cada nodo (A, B, C, D).

b) (0,5 p) Escribe el sistema en forma matricial.A q = b, A matriz de fjujos asociados, q las potencias y b los kW

c) (0,75 p) Calcula una solución numérica para los flujos $q_{\textrm{AB}} ,q_{\textrm{AC}} ,q_{\textrm{CD}}$,  suponiendo:

$$\begin{array}{l}
q_{\textrm{BC}} =80\;\textrm{kW}\\
q_{\textrm{BD}} =120\;\textrm{kW}\\
q_{\textrm{DB}} =70\;\textrm{kW}
\end{array}$$

Y comprueba que los balances de potencia en los nodos A, B, C y D son nulos.

d) (0,75 p) Si la línea D→B se desconecta ($\left.q_{\textrm{DB}} =0\;\textrm{kW}\right)$ calcula los flujos $q_{\textrm{AB}} ,q_{\textrm{AC}} ,q_{\textrm{CD}}$ como solución viable suponiendo:

$$q_{\textrm{DB}} =0\;\textrm{kW}$$

$$q_{\textrm{BC}} =60\;\textrm{kW}$$

$$q_{\textrm{BD}} =140\;\textrm{kW}$$

y comprueba que los balances de potencia en los nodos A, B, C y D son nulos.

Respuesta.

_Imágenes embebidas: 1 (image1.png)_


## CO · Práctico · IP01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/IP01.mlx`*

#### IP01.Precio medio de la electricidad en España (OMIE)

OMIE es el Operador de Mercado Eléctrico designado para la gestión del mercado diario e intradiario de electricidad en la Península Ibérica. Según fuentes de la OMIE el precio medio (€/MWh) en el pico mayo de consumo anual fue el siguiente:

2019 $\to$47.68 €/MWh, (nota de prensa OMIE, 21/01/2020)

2020$\;\to$33.96 €/MWh, (díptico “Main results 2020”)

2021 $\to$111.93 €/MWh, (Informe anual OMIE 2021)

2022 $\to$167.53 €/MWh, (Informe anual OMIE 2022)

a) (0,5 p) ¿Cuál es el grado del polinomio de interpolación?.  Haz un cambio de variable para que el origen se 2019.

b) (0,5 p) Escribe las ecuaciones que determinan los coeficientes del polinomio de interpolación, considerando el cambio de variable de forma que 2019 es 0 en abcisas.

c) (0,5 p) Representación gráfica de datos y del polinomio de interpolación.

d) (0,5 p) Utiliza la interpolación polinómica mediante las funciones polyfit y polyval y calcula el valor estimado del precio medio en el año 2022 (x=3 años respecto a 2019). Compara este valor con el precio oficial para los hogares en España según Eurostat en 2022 (121.9 €/MWh), indicando:

- $$\textrm{Valor}\;\textrm{estimado}\;\textrm{por}\;\textrm{el}\;\textrm{polinomio}$$

- $$\textrm{La}\;\textrm{diferencia}\;\textrm{abosoluta}\;\left(\textrm{en}\;\euro/\textrm{MWh}\right)=\textrm{Valor}\;\textrm{estimado}\;\textrm{por}\;\textrm{el}\;\textrm{polinomio}\;-\textrm{valor}\;\textrm{de}\;\textrm{Eurostat}$$

- $$\textrm{La}\;\textrm{diferencia}\;\textrm{relativa}\;\left(\;\textrm{en}\;%\right)=100\cdot \textrm{Diferencia}\;\textrm{abostula}/\textrm{Valor}\;\textrm{de}\;\textrm{Eurostat}$$

e) (0,5 p) Utilizando el polinomio de interporación envalúa el valor esitmado para 2020 (x=1 año respecto a 2019). Y compara el precio oficial para hograes en España según Eurostat en 2020 (211 €/MWh) indicando

- El valor estimado por el polinomio

- La diferencia abosoluta (en €/MWh)

- La diferencia relativa (en %)

Nota didáctica: el polinomio interpola datos de la OIME (mercado mayorista).; Eurostat publica precios finales domésticos (con peajes, cargas, impuesto, comercialización), con lo que es natural que hay diferencias.

Repuesta.


## CO · Práctico · IP02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/IP02.mlx`*

#### IP02. Demana total del gas natural en España (TWh)

CORES es la Corporación de Reservas Estratégica de Producto Petrolíferos en España, y hemos obtenido el consumo anual en Teravatio-hora (TWh) es la unidad de energía equivalente a un billón de watios-hora $\left.{\left(10\right.}^{12\;} \textrm{Wh}\right)\ldotp$ Esta unidad está realacionada con el consumo de gas natural, ya que un metro cúbico de gas natural equivale a 11.70 kWh aproximadamente.

Considere los siguientes datos:

2019 $\to$398,145 TWh,

2020$\;\to$360,016 TWh

2021 $\to$378 TWh

2022 $\to$364,3 TWh

a) (0,5 p) ¿Cuál es el grado del polinomio de interpolación?.  Haz un cambio de variable para que el origen se 2019.

b) (0,5 p) Escribe las ecuaciones que determinan los coeficientes del polinomio de interpolación, considerando el cambio de variable de forma que 2019 es 0 en abcisas.

c) (0,5 p) Representación gráfica de datos y del polinomio de interpolación.

d) (0,5 p) Utiliza la interpolación polinómica mediante las funciones polyfit y polyval y calcula el valor estimado del precio medio en el año 2022 (x=3 años respecto a 2019). Compara este valor con otro indicado oficial: "Demanda convencional" (hogares+comercio+industria) que en 2022 (226,4 TWh). Calcula:

- $$\textrm{Valor}\;\textrm{estimado}\;\textrm{por}\;\textrm{el}\;\textrm{polinomio}$$

- $$\textrm{La}\;\textrm{diferencia}\;\textrm{abosoluta}\;\left(\textrm{en}\;\textrm{TWh}\right)=\textrm{Valor}\;\textrm{estimado}\;\textrm{por}\;\textrm{el}\;\textrm{polinomio}\;-\textrm{valor}\;\textrm{de}\;\textrm{Eurostat}$$

- $$\textrm{La}\;\textrm{diferencia}\;\textrm{relativa}\;\left(\;\textrm{en}\;%\right)=100\cdot \textrm{Diferencia}\;\textrm{abostula}/\textrm{Valor}\;\textrm{de}\;\textrm{Eurostat}$$

e) (0,5 p) Utilizando el polinomio de interporación envalúa el valor esitmado para 2020 (x=1 año respecto a 2019). Y compara el dato comparado (convencional 2020), que fue 271,838 TWh. Calcula:

- El valor estimado por el polinomio

- La diferencia abosoluta (en TWh)

- La diferencia relativa (en %)

Nota didáctica: el polinomio interpola datos de CORES es un indicador de la reserva, y la demanda convencional indica el consumos de gas natural de los: hogares,comerciose industrias, con lo que es natural que hay diferencias. Este ejercicio permitirá conocer si la reserva superó o no al consumo anual de gas natural.

Repuesta.


## CO · Práctico · LEO01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/LEO01.mlx`*

#### LEO01

Una economía está compuesta por tres sectores:

- Agricultura

- Industria

- Servicios

Las matrices de coeficientes técnicos indican cuántas unidades de producción de un sector se necesitan para producir una unidad de producción en otro sector. La matriz de coeficientes técnicos A es:

[Imagen: Matriz de Leontief $A=\begin{pmatrix}0.2&0.1&0.0\\0.3&0.2&0.1\\0.1&0.2&0.3\end{pmatrix}$.]

La demanda final de la economía es:

[Imagen: Vector de demanda final $d=(50,40,30)^T$.]

Se pide:

a) (1p) Plantear el modelo de Leontief para esta economía.

b) (1p) Calcular la producción total necesaria x para satisfacer la demanda final.

c) (0.5p) Interpretar el resultado económico.

Respuesta

_Imágenes embebidas: 2 (image1.png, image2.png)_


## CO · Práctico · LEO02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/LEO02.mlx`*

#### LEO02

Una economía está formada por tres sectores:

- Agricultura

- Industria

- Energía

La matriz de coeficientes técnicos A viene dada por:

$$A=\left\lbrack \begin{array}{ccc}
0\ldotp 1 & 0\ldotp 2 & 0\ldotp 1\\
0\ldotp 3 & 0\ldotp 1 & 0\ldotp 2\\
0\ldotp 2 & 0\ldotp 1 & 0\ldotp 1
\end{array}\right\rbrack$$

La demanda final es:

$$d=\left\lbrack \begin{array}{c}
40\\
30\\
20
\end{array}\right\rbrack$$

Se pide:

a) (1p) Plantear el modelo de Leontief para esta economía.

b) (1p) Calcular la producción total necesaria x para satisfacer la demanda final.

c) (0.5p) Interpretar brevemente el resultado económico.

Respuesta


## CO · Práctico · MK01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/MK01.mlx`*

#### MK01. Consumo de café en Pontevedra

Consumidores de café en el área de Pontevedra usan tres marcas A, B, C. En marzo de 1995 se hizo una encuesta en la que se entrevistó a las 8450 personas que compran café y los resultados fueron los que se muestran a continuación:

De las 1690 personas que consumieron café de la marca A en marzo, 507 lo siguen consumiendo el mes siguiente, 845 se pasan a la marca B y el resto se pasan a la marca C

De las 3380 personas que consumieron café de la marca B en marzo, 2028 lo siguen consumiendo el mes siguiente, 676 se pasan a la marca A y el resto se pasan a la marca C

De las 3380 personas que consumieron café de la marca C en marzo, 1690 lo siguen consumiendo el mes siguiente, 845 se pasan a la marca A y el resto se pasan a la marca B

Si las probabilidades de cambio se mantienen constantes en el tiempo responde a las siguientes preguntas explicando con detalle el modelo empleado y el por qué de los cálculos

a) (0,75p) Si las compras se hacen mensualmente, ¿cuál será la distribución del mercado de café en Pontevedra en el mes de junio?

b) (1p) A la larga, ¿cómo se distribuirán los clientes de café?

c) (0,75p) En junio, ¿cuál es la proporción de clientes fieles a cada marca (usuarios que permanecen en la misma compañía respecto al mes anterior)?

Da los resultados con fprintf  en % y dos decimales en todos los apartados

Respuesta


## CO · Práctico · MK02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/MK02.mlx`*

#### MK02. Elección de compañía de telefonía móvil en una ciudad

Los usuarios de telefonía móvil de una ciudad utilizan tres compañías: X, Y y Z.

En enero de 2024 se realizó una encuesta a 12000 usuarios, obteniéndose los siguientes resultados sobre los cambios de compañía al mes siguiente.

De los 3600 usuarios que tenían la compañía X en enero:

- 1800 permanecen en X el mes siguiente,

- 1200 se cambian a la compañía Y,

- el resto se cambian a la compañía Z.

De los 4800 usuarios que tenían la compañía Y en enero:

- 2400 permanecen en Y el mes siguiente,

- 1440 se cambian a la compañía X,

- el resto se cambian a la compañía Z.

De los 3600 usuarios que tenían la compañía Z en enero:

- 2160 permanecen en Z el mes siguiente,

- 720 se cambian a la compañía X,

- el resto se cambian a la compañía Y.

Se supone que:

- Las decisiones de cambio se realizan mensualmente.

- Las probabilidades de cambio se mantienen constantes en el tiempo.

Responde a las siguientes preguntas explicando con detalle el modelo empleado y el por qué de los cálculos

a) (0,75p) ¿Cuál será la distribución del mercado entre las compañías X, Y y Z en el mes de abril de 2024?

b) (1p) A largo plazo, ¿cómo se distribuirán los clientes entre las tres compañías?

c) (0,75 p) En el mes de abril, ¿cuál es la proporción de clientes fieles a cada compañía (usuarios que permanecen en la misma compañía respecto al mes anterior)?

Respuesta


## CO · Práctico · PR01.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/PR01.mlx`*

#### PR01. Clasificación de páginas web

Un pequeño motor de búsqueda analiza una red formada por 5 páginas web: $P_1 ,P_2 ,P_3 ,P_4 ,P_5$

Los enlaces entre páginas son los siguientes:

- $P_1$� enlaza a $P_2$ y $P_3$�

- $P_2$� enlaza a $P_3$�

- $P_3$� enlaza a $P_1 ,P_2 ,P_4$�

- $P_4$� enlaza a $P_2$�

- $P_5$ enlaza a $P_3$� y $P_4$�

a) (0,25p) Escribe mediante el editor de ecuaciones la matriz de adyacencia. Después emplea las funciones sparse y full para asígnarle la variable A en Matlab

b) (0,25p) Asigna la variable G al grafo dirigido de la matriz A y representalo gráficamente. Los nombres de las páginas deben aparecer en el grafo

c) (0,25p) Crea la matriz de Markov correspondiente y asignale la variable C. Verifica que se trata de una matriz de Markov

d) (0,5p) Incorpora un factor de atenuación $\delta =85%$ y calcula la nueva matriz estocástica y asígnale la variable M con Matlab. Verifica que M es una matriz estocástica

e) (0,25p) Calcula el vector de estado estacionario de la matriz M mediante autovalores y asígnale la variable q

f) (0,25p) Calcula de nuevo el vector de estado estacionario mediante la función correspondiente de Matlab y el mismo factor de atenuación, asígnale la variable qm

g) (0,25p) Verifica la diferencia entre ambos vectores de estado q calculado con autovalores y qm calculado con Matlab y explica el resultado. Reduce la diferencia entre ambos vectores de estado para que sea menor que ${10}^{-10}$, esxplica cómo lo haces y por qué.

h) (0,5p) Da la clasificación de las páginas a parir de q mediante fprintf e indicando el nombre de cada una de ellas, es decir, debe aparcer el texto: "La 1ª página es...(nombre de la página)"

Respuesta


## CO · Práctico · PR02.mlx

*Fuente: `EXÁMENES/CO/PRACTICO/PR02.mlx`*

#### PR02. Clasificación de páginas web

Un pequeño motor de búsqueda analiza una red formada por 5 páginas web: $P_1 ,P_2 ,P_3 ,P_4 ,P_5$

Los enlaces entre páginas son los siguientes:

- $P_1$ enlaza a $P_2$

- $P_2$ enlaza a $P_3$ y  $P_4$

- $P_3$ enlaza a $P_1$ y $P_5$

- $P_4$ enlaza a $P_2$, $P_3$y $P_5$

- $P_5$ enlaza a $P_1$ y $P_4$

a) (0,25p) Escribe mediante el editor de ecuaciones la matriz de adyacencia. Después emplea las funciones sparse y full para asígnarle la variable A en Matlab

b) (0,25p) Asigna la variable G al grafo dirigido de la matriz A y representalo gráficamente. Los nombres de las páginas deben aparecer en el grafo

c) (0,25p) Crea la matriz de Markov correspondiente y asignale la variable C. Verifica que se trata de una matriz de Markov

d) (0,5p) Incorpora un factor de atenuación $\delta =85%$ y calcula la nueva matriz estocástica y asígnale la variable M con Matlab. Verifica que M es una matriz estocástica

e) (0,25p) Calcula el vector de estado estacionario de la matriz M mediante autovalores y asígnale la variable q

f) (0,25p) Calcula de nuevo el vector de estado estacionario mediante la función correspondiente de Matlab y el mismo factor de atenuación, asígnale la variable qm

g) (0,25p) Verifica la diferencia entre ambos vectores de estado q calculado con autovalores y qm calculado con Matlab y explica el resultado. Reduce la diferencia entre ambos vectores de estado para que sea menor que ${10}^{-10}$, esxplica cómo lo haces y por qué.

h) (0,5p) Da la clasificación de las páginas a parir de q mediante fprintf e indicando el nombre de cada una de ellas, es decir, debe aparcer el texto: "La 1ª página es...(nombre de la página)"

Respuesta
