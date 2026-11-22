# Teoría: sistemas de ecuaciones lineales, matrices y determinantes

Temas 1–3. Primero las diapositivas del Prof. Medina, después las pizarras manuscritas del Grupo A (transcritas) y material de apoyo.

**Contenido de este archivo:**
- Diapositivas: Sistemas de ecuaciones lineales
- Diapositivas: Matrices
- Diapositivas: Determinantes
- Pizarra Grupo A · Tema 1 Sistemas de ecuaciones
- Pizarra Grupo A · Tema 2 Matrices (1/3)
- Pizarra Grupo A · Tema 2 Matrices (2/3)
- Pizarra Grupo A · Tema 2 Matrices (3/3)
- Pizarra Grupo A · Tema 3 Determinantes
- Live Script: problema inicial de matrices y SEL
- Guion: ejercicios de matrices con MATLAB


## Diapositivas: Sistemas de ecuaciones lineales

*Fuente: `02 - Sistemas de ecuaciones lineales_R01.pptm`*

#### Diapositiva 1

- SISTEMAS DE ECUACIONES LINEALES
- MATEMÁTICAS PARA LA INGENIERÍA I
- Prof. Dr. Josemaría Medina Villaverde
- UFV.ES

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 2

- Ecuaciones lineales
- 01
- Teorema de Rouchè-Fröbenius
- 04
- Sistemas de ecuaciones lineales
- 02
- Método de Gauss
- 05
- Resolución de SEL
- 03
- Regla de Cramer
- 06
- ÍNDICE
- Resumen
- 07

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 3

- ECUACIONES LINEALES
- CAPÍTULO 01
- 3
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 4

- Ecuaciones lineales
- 4
- UFV.ES
- Todas las ecuaciones se pueden clasificar como lineales o no lineales.
- Una ecuación lineal tiene solo dos tipos de términos: constantes y variables multiplicadas por constantes.
- Ecuaciones no lineales
Las ecuaciones con cualquier otro tipo de término son ecuaciones no lineales.

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos (imagen): lineal $2x+5-y=0$ (sólo constantes y constante·variable); no lineales $1-z^2=x$ (variable²), $e^x=3$ (función de variable), $y(1-x)=2$ (variable·variable).

#### Diapositiva 5

- Ecuaciones lineales
- 5
- UFV.ES
- Preguntota:
- ¿Cuál de las siguientes ecuaciones no es lineal?
- Otra preguntota:
- (Seleccione todas las que correspondan) ¿Cuáles de las siguientes son ecuaciones lineales para las variables x, y y z?
- Aunque no se dé en esta forma, una ecuación lineal se puede escribir en la forma ax + by + cz = d, para las constantes a, b, c y d (que puede ser cero).

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Preguntota: ¿cuál no es lineal? Opciones $2x+y=0$; $3a^2+5a-1=0$ (señalada con flecha roja: no lineal); $x+y=z-10$; 'todas son lineales'. Otra: ¿cuáles son lineales en x, y, z? $3x-7y=5z+xy+6$ (no); marcadas como lineales: $3x-7y=5z+4(x-y)+6$, $y=z$, $3x-7y+5z=6+4x-y+2z$.

#### Diapositiva 6

- Ecuaciones lineales
- 6
- UFV.ES
- Una ecuación lineal en n variables $𝑥1$, $𝑥2$, $𝑥3$, …, $𝑥𝑛 $tiene la forma:
- $𝑎1𝑥1+𝑎2𝑥2+𝑎3𝑥3+…+ 𝑎𝑛𝑥𝑛=𝑏$
- Los coeficientes $𝑎1$, $𝑎2$, $𝑎3$, …, $𝑎𝑛 $y el término independiente b son números reales.
- Las ecuaciones lineales no contienen productos o raíces de las variables, ni funciones trigonométricas, exponenciales o logarítmicas.
- Las variables aparecen sólo elevadas a la primera potencia.
- Una solución de una ecuación lineal en n variables es una colección de n números reales
- $𝑠1$, $𝑠2$, $𝑠3$, …, $𝑠𝑛 $ tales que la ecuación se satisface cuando se sustituyen en ella los valores:
- $𝑥1 = 𝑠1$,   $𝑥2 = 𝑠2$,    $𝑥3 = 𝑠3$, …….    $𝑥𝑛 = 𝑠𝑛$

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $a_1x_1+a_2x_2+\dots+a_nx_n=b$; solución $x_1=s_1,\dots,x_n=s_n$.

#### Diapositiva 7

- Ecuaciones lineales
- 7
- UFV.ES
- Soluciones para sistemas lineales
- La solución de un sistema de ecuaciones lineales se refiere al par x/y que hace que ambas ecuaciones sean iguales.
- En otras palabras, el par x/y que corresponde a la intersección de dos rectas.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Gráfica: rectas $y_1=-2x+5$ (azul) y $y_2=4x$ (naranja) que se cortan en el punto donde $y_1=y_2$ (x≈0.83, y≈3.33).

#### Diapositiva 8

- 8
- UFV.ES
- Ecuaciones lineales
- Las ecuaciones lineales en x e y no son más que rectas en el plano x-y.
- En esta actividad, trazarás estas dos ecuaciones lineales e interpretará su solución visualmente:
- 2x + 4y = −10
- 6x + 3y = 6
- Veamos soluciones gráficas y simbólicas

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Sistema $2x+4y=-10$, $6x+3y=6$ y foto panorámica del campus UFV ('Veamos soluciones gráficas y simbólicas').

#### Diapositiva 9

- Ecuaciones lineales
- 9
- UFV.ES
- clear; clc;
- x = linspace(0,5,100)
- y1 = -x/2 - 5/2
- plot(x,y1)
- y2 = -2*x + 2
- hold on
- plot(x,y2)
- hold off
- grid on
- xlabel('x')
- ylabel('y')
- title('2x + 4y = -10 / 6x + 3y = 6')
- Solución: (3,-4)

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Código MATLAB: `clear; clc; x = linspace(0,5,100); y1 = -x/2 - 5/2; plot(x,y1); y2 = -2*x + 2; plot(x,y1); hold on; plot(x,y2); hold off; grid on; xlabel('x'); ylabel('y'); title('2x + 4y = -10 / 6x + 3y = 6')`. Gráfica con la solución marcada (3, −4).

#### Diapositiva 10

- Ecuaciones lineales
- 10
- UFV.ES
- clear; clc;
- syms x y
- ec(1) = 2*x + 4*y == -10;
- ec(2) = 6*x + 3*y == 6;
- ec'
- sol = solve(ec,[x,y])
- sol = struct with fields:
- x: 3
- y: -4

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Código MATLAB simbólico: `clear; clc; syms x y; ec(1) = 2*x + 4*y == -10; ec(2) = 6*x + 3*y == 6; ec'; sol = solve(ec,[x,y])` → `sol = struct with fields: x: 3, y: -4`. Misma gráfica.

#### Diapositiva 11

- Ecuaciones lineales
- 11
- UFV.ES
- Escribir un sistema lineal como una ecuación matricial
- Para resolver sistemas de ecuaciones lineales, primero debe reescribirlos en una forma con la que MATLAB pueda trabajar fácilmente.
- Para reescribir un sistema de ecuaciones lineales como una ecuación matricial, organice todos los términos constantes en el lado derecho y las variables desconocidas con sus coeficientes a la izquierda, asegurándose de que las variables aparezcan en el mismo orden en todas las ecuaciones.
- Forme un vector columna a partir de las constantes y una matriz a partir de los coeficientes, incluyendo ceros para las variables faltantes y unos para las variables individuales.
- Denote la matriz de coeficientes como A, el vector constante como b y el vector de variables desconocidas como x, lo que da como resultado una ecuación de matriz () equivalente al sistema original de ecuaciones lineales.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo de ecuación matricial $Ax=b$: $\begin{pmatrix}1.5&1&0\\0&-4&1\\-1&1&-1\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}=\begin{pmatrix}3\\0\\-4\end{pmatrix}$.

#### Diapositiva 12

- Ecuaciones lineales
- 12
- UFV.ES
- clear; clc;
- syms x y
- ec(1) = 2*x + 4*y == -10;
- ec(2) = 6*x + 3*y == 6;
- ec'
- [A b] = equationsToMatrix(ec)
- extA = [A b]
- GJ = rref(extA)

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Código MATLAB: `syms x y; ec(1) = 2*x + 4*y == -10; ec(2) = 6*x + 3*y == 6; [A b] = equationsToMatrix(ec); extA = [A b]; GJ = rref(extA)` → $A=\begin{pmatrix}2&4\\6&3\end{pmatrix}$, $b=(-10,6)^T$, $GJ=\left(\begin{smallmatrix}1&0&|&3\\0&1&|&-4\end{smallmatrix}\right)$ (solución x=3, y=−4 recuadrada).

#### Diapositiva 13

- 13
- UFV.ES
- Ecuaciones lineales
- Resolver la ecuación lineal       $𝑥1+ 2𝑥2=4$

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejercicio: resolver la ecuación lineal $x_1+2x_2=4$ (foto del campus).

#### Diapositiva 14

- Ecuaciones lineales
- 14
- UFV.ES
- $𝑥1=4−2𝑥2$
- $𝑥1=4−2$·$𝜆$, $𝑥2=$ $𝜆$,  $𝜆$ es cualquier número real.
- $𝒙𝟏+ 𝟐𝒙𝟐=𝟒$
- l
- x1
- x2
- 0
- 4
- 1
- 2
- 3
- -2

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $x_1=4-2x_2$; $x_1=4-2\lambda$, $x_2=\lambda$, λ real. Tabla: λ=0 → (4, 0); λ=1 → (2, 1); λ=2 → (0, 2); λ=3 → (−2, 3).

#### Diapositiva 15

- Ecuaciones lineales
- 15
- UFV.ES
- Ecuación lineal de dos incógnitas
- Una ecuación lineal con dos incógnitas es una expresión de la forma ax + by = c, donde x e y son las incógnitas y a, b y c son números reales, de los cuales a a y b se les denomina coeficientes y a c término independiente.
- A todo par de números (x0, y0) que verifique la expresión anterior se le denomina solución de la ecuación.
- La representación gráfica de todas las soluciones de dicha expresión será una recta.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Gráfica de una recta en el plano XY.

#### Diapositiva 16

- SISTEMAS DE ECUACIONES LINEALES
- CAPÍTULO 02
- 16
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 17

- SISTEMAS DE Ecuaciones lineales
- 17
- UFV.ES
- Un sistema de m ecuaciones lineales con n incógnitas $𝒙𝟏$, $𝒙𝟐$,…, $𝒙𝒏$ (al que podemos llamar simplemente sistema lineal), es un conjunto de $𝒎$ ecuaciones lineales, cada una con n incógnitas. Un sistema lineal puede denotarse sin problema mediante:
- $𝑎11𝑥1+𝑎12𝑥2+…+𝑎1𝑛𝑥𝑛=𝑏1𝑎21𝑥1+𝑎22𝑥2+…+𝑎2𝑛𝑥𝑛=𝑏𝑛⋮𝑎𝑚1𝑥1+𝑎𝑚2𝑥2+…+𝑎𝑚𝑛𝑥𝑛=𝑏𝑚$

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\begin{cases}a_{11}x_1+\dots+a_{1n}x_n=b_1\\a_{21}x_1+\dots+a_{2n}x_n=b_2\\\vdots\\a_{m1}x_1+\dots+a_{mn}x_n=b_m\end{cases}$

#### Diapositiva 18

- SISTEMAS DE Ecuaciones lineales
- 18
- UFV.ES
- Sistema de ecuaciones lineales
- Un sistema de dos ecuaciones lineales con dos incógnitas es una expresión del tipo:
- Si representamos la gráfica de cada ecuación, obtendremos dos rectas. El punto de corte de ambas rectas, si existe, será la única solución del sistema.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\begin{cases}ax+by=c\\a'x+b'y=c'\end{cases}$; gráfica de dos rectas que se cortan en un punto.

#### Diapositiva 19

- SISTEMAS DE Ecuaciones lineales
- 19
- UFV.ES
- Un sistema de ecuaciones que tiene una única solución se denomina Compatible Determinado.
- Un sistema de ecuaciones con infinitas soluciones se denomina Compatible Indeterminado.
- Un sistema de ecuaciones que no tiene solución se denomina Incompatible.

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Esquema: Sistemas → Compatible {Determinado (SCD, una solución), Indeterminado (SCI, infinitas)}, Incompatible (SI, sin solución). Tres gráficas: rectas que se cortan (SCD), rectas coincidentes (SCI) y rectas paralelas (SI).

#### Diapositiva 20

- SISTEMAS DE Ecuaciones lineales
- 20
- UFV.ES
- Expresión matricial de un sistema de ecuaciones lineales
- Todo sistema de la forma$ 𝑎1𝑥+𝑏1𝑦=𝑐1𝑎2𝑥+𝑏2𝑦=𝑐2  $se puede expresar mediante el producto de matrices:
- $𝑎1𝑏1𝑎2𝑏2·𝑥𝑦=𝑐1𝑐2$
- la primera formada por los coeficientes y que se denomina matriz asociada del sistema:
- $A=𝑎1𝑏1𝑎2𝑏2$
- y la matriz de los términos independientes:
- $𝐵=𝑐1𝑐2$
- Combinando A y B se obtiene la matriz ampliada:
- $𝐴∗=𝑎1𝑏1𝑎2𝑏2𝑐1𝑐2$

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\begin{cases}a_1x+b_1y=c_1\\a_2x+b_2y=c_2\end{cases}\iff\begin{pmatrix}a_1&b_1\\a_2&b_2\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}c_1\\c_2\end{pmatrix}$; $A=\begin{pmatrix}a_1&b_1\\a_2&b_2\end{pmatrix}$, $B=\begin{pmatrix}c_1\\c_2\end{pmatrix}$, $A^*=\left(\begin{smallmatrix}a_1&b_1&|&c_1\\a_2&b_2&|&c_2\end{smallmatrix}\right)$.

#### Diapositiva 21

- SISTEMAS DE Ecuaciones lineales
- 21
- UFV.ES
- Definición de sistema de ecuaciones lineales
- En general se denomina sistema de m ecuaciones lineales con n incógnitas a un conjunto de relaciones de la forma:
- $𝑎11𝑥1+𝑎12𝑥2+…+𝑎1𝑛𝑥𝑛=𝑏1𝑎21𝑥1+𝑎22𝑥2+…+𝑎2𝑛𝑥𝑛=𝑏2…………………………………………𝑎𝑚1𝑥1+𝑎𝑚2𝑥2+…+𝑎𝑚𝑛𝑥𝑛=𝑏𝑚$
- donde x1, x2, …, xn, son las incógnitas, los números aij son los coeficientes de las incógnitas y los bi son los términos independientes.
- El conjunto de números reales ordenados 1,  2, …,  n será solución del sistema si satisface todas las ecuaciones del mismo.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Diagrama: sistema → compatible (determinado/indeterminado) o incompatible. Interpretación geométrica: (x, y) recta en el plano; (x, y, z) plano en el espacio 3D $ax+by+cz=d$; (x, y, z, …) hiperplano en hiperespacio.

#### Diapositiva 22

- SISTEMAS DE Ecuaciones lineales
- 22
- UFV.ES
- Sistemas homogéneos
- Un sistema de ecuaciones lineales se dice que es HOMOGÉNEO cuando el término independiente de todas las ecuaciones es igual a cero; es decir, bi = 0 ∀i:
- $𝑎11𝑥1+𝑎12𝑥2+…+𝑎1𝑛𝑥𝑛=0𝑎21𝑥1+𝑎22𝑥2+…+𝑎2𝑛𝑥𝑛=0…………………………………………𝑎𝑚1𝑥1+𝑎𝑚2𝑥2+…+𝑎𝑚𝑛𝑥𝑛=0$
- Todo sistema homogéneo es compatible, pues tiene al menos una solución, xi = 0 ∀i
- Se llama solución trivial de un sistema homogéneo a la matriz columna:
- $𝑥1𝑥2⋮𝑥𝑛=00⋮0$
- Si el sistema es compatible indeterminado se suele trabajar para dejar el conjunto de soluciones en forma paramétrica, es decir, haciendo que una (o más) de las incógnitas se comporte como un parámetro libre y expresando las demás en función de ella.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Sistema homogéneo $a_{i1}x_1+\dots+a_{in}x_n=0$; solución trivial $(x_1,\dots,x_n)^T=(0,\dots,0)^T$.

#### Diapositiva 23

- SISTEMAS DE Ecuaciones lineales
- 23
- UFV.ES
- Sistemas homogéneos
- El sistema
- tiene infinitas soluciones; aparte de la trivial: x = y = z = 0, podemos encontrar x = –2, y = –1, z = 3, o x = 2, y = 1, z = –3 y es, como antes, indeterminado.
- Para expresar el conjunto de soluciones en forma paramétrica, elegimos la incógnita que se pueda despejar más fácilmente, en este caso x. Simplemente sumando miembro a miembro las dos primeras ecuaciones:
- $𝐴=1112−111−20$
- $𝐴=0$

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $x+y+z=0,\ 2x-y+z=0,\ x-2y=0$, con $A=\begin{pmatrix}1&1&1\\2&-1&1\\1&-2&0\end{pmatrix}$, $|A|=0$. $F_2\to F_2+F_1$: $3x+2z=0$; soluciones $y=\tfrac12x,\ z=-\tfrac32x$, o bien $x=t,\ y=\tfrac12t,\ z=-\tfrac32t$.

#### Diapositiva 24

- SISTEMAS DE Ecuaciones lineales
- 24
- UFV.ES
- Sistemas equivalentes
- Dos sistemas con el mismo número de incógnitas, aunque no tengan el mismo número de ecuaciones, se dice que son equivalentes si tienen las mismas soluciones, es decir, toda solución del primero es solución del segundo, y viceversa.
- Transformaciones de Gauss

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Flecha decorativa 'Transformaciones de Gauss'.

#### Diapositiva 25

- SISTEMAS DE Ecuaciones lineales
- 25
- UFV.ES
- Sistemas equivalentes
- Para pasar de un sistema a otro equivalente, se pueden usar las siguientes Transformaciones de Gauss:
- Cambiar el orden de las ecuaciones del sistema.
- Multiplicar los dos miembros de una ecuación por un mismo número distinto de cero.
- Suprimir una ecuación del sistema que sea combinación lineal de las demás.
- Sustituir una ecuación por la suma de ella más otra ecuación multiplicada por un número real cualquiera.
- Sustituir una ecuación por una combinación lineal de ella y de las restantes, siempre que el coeficiente de la ecuación sustituida, en la combinación lineal, sea distinto de cero.
- Esta última transformación se conoce como Teorema Fundamental de equivalencia de sistemas.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 26

- RESOLUCIÓN DE SISTEMAS DE ECUACIONES LINEALES
- CAPÍTULO 03
- 26
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 27

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- 27
- UFV.ES
- ¿Se puede hacer esto?
- Método de Gauss o de eliminaciones sucesivas
- Este método consiste en sustituir el sistema dado por otro equivalente, aplicando las transformaciones de Gauss, hasta conseguir un sistema escalonado.
- Sistema escalonado
- es aquél en el que cada ecuación tiene una incógnita menos que la anterior
- ¡Claro! ¡Con las transformaciones de Gauss!

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\begin{cases}a_{11}x_1+a_{12}x_2+a_{13}x_3=b_1\\a_{21}x_1+a_{22}x_2+a_{23}x_3=b_2\\a_{31}x_1+a_{32}x_2+a_{33}x_3=b_3\end{cases}$ → $\begin{cases}a'_{11}x_1+a'_{12}x_2+a'_{13}x_3=b'_1\\a'_{22}x_2+a'_{23}x_3=b'_2\\a'_{33}x_3=b'_3\end{cases}$. Viñeta: '¿Se puede hacer esto?' — '¡Claro! ¡Con las transformaciones de Gauss!'.

#### Diapositiva 28

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- 28
- UFV.ES
- Una matriz está en forma escalonada cuando:
- Las filas nulas, si las hay, ocupan las posiciones más bajas.
- En cada fila no nula, el primer elemento no nulo es 1 (se llama 1 dominante o pivote)
- Dadas dos filas sucesivas (no nulas), el 1 dominante de la fila superior está más a la izquierda que el 1 dominante de la inferior.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo escalonado: $x-2y+3z=9,\ y+3z=5,\ z=2$; matriz $\left(\begin{smallmatrix}1&-2&3&9\\0&1&3&5\\0&0&1&2\end{smallmatrix}\right)$.

#### Diapositiva 29

- 29
- UFV.ES
- Ecuaciones lineales
- Resolver el sistema:

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Resolver: $x-2y+3z=9,\ -x+3y=-4,\ 2x-5y+5z=18$.

#### Diapositiva 30

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- 30
- UFV.ES
- Sumando las ecuaciones 1ª y 2ª obtenemos una nueva 2ª ecuación:
- Sumando $−2$ veces la 1ª a la tercera obtenemos una nueva 3ª ecuación
- Sumando las ecuaciones 2ª y 3ª obtenemos una nueva 3ª ecuación

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Pasos: sumando 1ª y 2ª → $y+3z=5$; sumando −2·1ª a la 3ª → $-y-z=0$; sumando 2ª y 3ª → $2z=5$. Sistema escalonado: $x-2y+3z=9,\ y+3z=5,\ 2z=5$.

#### Diapositiva 31

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- 31
- UFV.ES
- Resolver el sistema:
- A = [1 -2 3;-1 3 0;2 -5 5]
- TI = [9;-4;18]
- $𝐴·𝑋=𝑇𝐼$
- $X= xyz$
- $𝐴=2$
- $𝐀−𝟏·𝐀·𝐗=𝐀−𝟏·𝐓𝐈$
- X = A\TI

_Imágenes/medios en la diapositiva: 10_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** MATLAB: `A = [1 -2 3;-1 3 0;2 -5 5]; TI = [9;-4;18];` $|A|=2$; $A^{-1}AX=A^{-1}TI$; `X = A\TI` → $X=(-3.5,\ -2.5,\ 2.5)^T$.

#### Diapositiva 32

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- clear; clc;
- syms x y z
- ec(1) = x - 2*y + 3*z == 9;
- ec(2) = -x + 3*y == -4;
- ec(3) = 2*x - 5*y + 5*z == 18;
- ec'
- X = [x;y;z]
- Obtenemos las matrices
- [A b] = equationsToMatrix(ec)
- Rehacemos las ecuaciones, para comprobar:
- eq = A*X == b

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** MATLAB simbólico: `syms x y z; ec(1) = x - 2*y + 3*z == 9; ec(2) = -x + 3*y == -4; ec(3) = 2*x - 5*y + 5*z == 18; X = [x;y;z]; [A b] = equationsToMatrix(ec); eq = A*X == b` (para comprobar).

#### Diapositiva 33

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- Solución matricial:
- sol = inv(A)*b
- También
- sol = A\b
- Solución GJ con rref:
- eA = [A b]
- GJ = rref(eA)

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Solución matricial: `sol = inv(A)*b` o `sol = A\b` → (−3.5, −2.5, 2.5). Solución Gauss-Jordan: `eA = [A b]; GJ = rref(eA)` → $\left(\begin{smallmatrix}1&0&0&-3.5\\0&1&0&-2.5\\0&0&1&2.5\end{smallmatrix}\right)$.

#### Diapositiva 34

- 34
- UFV.ES
- Ecuaciones lineales
- Resolver el sistema:

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Resolver: $x_1-3x_2+x_3=1,\ 2x_1-x_2-2x_3=2,\ x_1+2x_2-3x_3=-1$.

#### Diapositiva 35

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- Sumando -2 veces la 1ª ecuación a la segunda
- Sumando -1 veces la 1ª ecuación a la tercera
- Restamos la 2ª ecuación de la tercera
- Y ahora, ¿qué demonios hacemos con esto, que no hay quien lo entienda?

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Pasos: −2·1ª + 2ª → $5x_2-4x_3=0$; −1·1ª + 3ª → $5x_2-4x_3=-2$; restando 2ª de 3ª → $0=-2$ ⇒ incompatible. Viñeta: 'Y ahora, ¿qué demonios hacemos con esto, que no hay quien lo entienda?'.

#### Diapositiva 36

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- solve siempre devuelve 0x1 cuando las ecuaciones no son compatibles
- [A b] = equationsToMatrix(ec)
- eq = A*X == b
- eA = [A b]
- GJ = rref(eA)
- sol = solve(ec)
- Mira que gracioso

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** MATLAB: `[A b] = equationsToMatrix(ec); eq = A*X == b; eA = [A b]; GJ = rref(eA)` → $\left(\begin{smallmatrix}1&0&-1.4&0\\0&1&-0.8&0\\0&0&0&1\end{smallmatrix}\right)$ ('mira qué gracioso'); `sol = solve(ec)` → struct con x1, x2, x3 vacíos [0×1 sym]. Nota: 'solve siempre devuelve 0×1 cuando las ecuaciones no son compatibles'.

#### Diapositiva 37

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- GJ = rref(eA)
- A(:,1)*GJ(1,3) + A(:,2)*GJ(2,3)

_Imágenes/medios en la diapositiva: 8_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Interpretación del rref incompatible: $GJ=\left(\begin{smallmatrix}1&0&-1.4&0\\0&1&-0.8&0\\0&0&0&1\end{smallmatrix}\right)$; la tercera columna de A es combinación lineal de las dos primeras: `A(:,1)*GJ(1,3) + A(:,2)*GJ(2,3)` = (1, −2, −3) = tercera columna.

#### Diapositiva 38

- 38
- UFV.ES
- Ecuaciones lineales
- Resolver el sistema:

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Resolver: $x_2-x_3=0,\ x_1-x_2-3x_3=-1,\ -x_1+3x_2=1$.

#### Diapositiva 39

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- Resolver el sistema:
- Intercambiamos las dos primeras ecuaciones
- Sumando la 1ª ecuación a la 3ª obtenemos una nueva 3ª ecuación
- Sumando -3 veces la segunda ecuación a la 3ª obtenemos una 3ª ecuación trivial
- $𝑥3=𝜆$

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Pasos: intercambiar las dos primeras ecuaciones; sumar 1ª a 3ª → $2x_2-3x_3=0$ *(en la imagen: $+3x_2-3x_3=0$ tras la suma)*; sumar −3·2ª a 3ª → $0=0$ (ecuación trivial) ⇒ SCI con $x_3=\lambda$.

#### Diapositiva 40

- RESOLUCIÓN DE SISTEMAS DE Ecuaciones lineales
- UFV.ES
- Resolución de sistemas mediante la matriz inversa
- La expresión matricial de un sistema de ecuaciones lineales nos ofrece otro mecanismo de resolución del sistema a partir de la matriz inversa de la matriz de los coeficientes.
- Si la matriz A tiene matriz inversa, es decir, si se cumple que:
- m = n: el sistema tiene que tener tantas ecuaciones como incógnitas, es decir, la matriz de los coeficientes debe ser cuadrada.
- |A| ≠ 0: el determinante de la matriz de los coeficientes debe ser distinto de cero, para que la matriz tenga inversa.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $AX=B\Rightarrow A^{-1}AX=A^{-1}B\Rightarrow IX=A^{-1}B\Rightarrow X=A^{-1}B$.

#### Diapositiva 41

- TEOREMA DE ROUCHÈ-FRÖBENIUS
- CAPÍTULO 04
- 41
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 42

- TEOREMA DE ROUCHÈ-FRÖBENIUS
- UFV.ES
- Teorema de Rouchè-Fröbenius
- El teorema de Rouchè-Fröbenius dice:
- "La condición necesaria y suficiente para que un sistema de m ecuaciones y n incógnitas sea compatible (tenga solución) es que el rango de la matriz de los coeficientes sea igual al rango de la matriz ampliada".
- Si estudiamos los rangos de las matrices nos podemos encontrar con las siguientes situaciones:

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\operatorname{rg}(A)=\operatorname{rg}(A^*)$ ⇒ compatible: si $=n$ SCD, si $<n$ SCI; $\operatorname{rg}(A)<\operatorname{rg}(A^*)$ ⇒ incompatible.

#### Diapositiva 43

- TEOREMA DE ROUCHÈ-FRÖBENIUS
- UFV.ES
- Eugène Rouché (18 de agosto de 1832 - 19 de agosto de 1910) fue un matemático francés. Es conocido por ser el autor del Teorema de Rouché sobre análisis complejo y coautor del Teorema de Rouché–Frobenius.
- Rouché nació en 1832 en Sommières, en el sur de Francia. Era hijo de Jean Jacques Rouché, recaudador de impuestos, y de Marie Nicot. Se educó en el Colegio de Santa Bárbara de París (un centro orientado al ingreso de sus alumnos en la Escuela Politécnica), donde coincidió con el célebre ingeniero Gustave Eiffel.
- Tras dos cursos, obtuvo su licenciatura en la École Polytechnique en 1854. Ejerció como docente en Nantes, desde donde se trasladó a París, obteniendo su doctorado en matemáticas en la Escuela de Ciencias en 1858. Entre 1858 y 1877 ejerció como examinador en la Escuela Central de París.
- Fue profesor de matemáticas en el Conservatorio de Artes y Oficios de París y examinador de la Escuela Politécnica.
- Rouché fue miembro de la Sociedad Matemática de Francia, siendo su presidente entre 1883 y 1884. Así mismo, perteneció a la Société Philomatique de Paris y formó parte del Consejo Superior de la Enseñanza Técnica. Resultó elegido miembro de la Academia de Ciencias de Francia en 1896 y de la Academia de Ciencias y de Letras de Montpellier.
- Falleció en 1910 en la ciudad de Lunel, un lugar próximo a su ciudad natal.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Retrato de Eugène Rouché.

#### Diapositiva 44

- TEOREMA DE ROUCHÈ-FRÖBENIUS
- UFV.ES
- Ferdinand Georg Frobenius (Charlottenburg,1​ 26 de octubre de 1849 - Berlín, 3 de agosto 1917) Matemático alemán reconocido por sus aportes a la teoría de las ecuaciones diferenciales y a la teoría de grupos; también por su profundización en el teorema de Cayley-Hamilton y su aporte al teorema planteado por Eugène Rouché llamado entonces teorema de Rouché-Frobenius.
- Nacido en el lujoso suburbio berlinés de Charlottenburg,​ cursó sus estudios superiores en la Universidad Humboldt de Berlín siendo su tesis la solución de las ecuaciones diferenciales bajo la dirección de Karl Weierstrass. Luego de egresar en 1870 se mudó a Zúrich donde sentó cátedra en el Polytechnicum de esa importante ciudad helvética (tal centro de estudios es actualmente llamado ETH Zürich). En 1893 retornó a Berlín donde fue elegido miembro de la Academia de Ciencias Prusiana.
- Su obra ha contribuido a establecer la llamada ley de reciprocidad de Frobenius y los grupos de Frobenius, versando principalmente en la teoría algebraica de los grupos finitos y la sistematización del álgebra mediante procedimientos de lógica matemática y axiomática.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Retrato de Ferdinand Georg Frobenius.

#### Diapositiva 45

- TEOREMA DE ROUCHÈ-FRÖBENIUS
- UFV.ES
- Los buenos matemáticos tienen barba
- ¡FALSO! Este sujeto es Ingeniero

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tres fotos (Rouché ↔ Frobenius ↔ el profesor) con los textos humorísticos 'Los buenos matemáticos tienen barba' y '¡FALSO! Este sujeto es ingeniero'.

#### Diapositiva 46

- MÉTODO DE GAUSS
- CAPÍTULO 05
- 46
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 47

- MÉTODO DE GAUSS
- UFV.ES
- Método de Gauss y expresión matricial
- Utilizando las matrices asociada y ampliada podemos simplificar el método de Gauss visto antes. Bastará con partir de la matriz ampliada e ir escalonándola mediante transformaciones elementales:
- En este sistema la última ecuación, que corresponde a la última fila de la matriz, es
- Por tanto, el sistema tiene solución única:

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $x-2y+z=3,\ -x+y-2z=1,\ 2x-3y+z=2$ → $\left(\begin{smallmatrix}1&-2&1&3\\-1&1&-2&1\\2&-3&1&2\end{smallmatrix}\right)\xrightarrow{F_2+F_1,\ F_3-2F_1}\left(\begin{smallmatrix}1&-2&1&3\\0&-1&-1&4\\0&1&-1&-4\end{smallmatrix}\right)\xrightarrow{F_3+F_2}\left(\begin{smallmatrix}1&-2&1&3\\0&-1&-1&4\\0&0&-2&0\end{smallmatrix}\right)$; $-2z=0\Rightarrow z=0$; solución única $x=-5,\ y=-4,\ z=0$.

#### Diapositiva 48

- MÉTODO DE GAUSS
- UFV.ES
- El método de Gauss también nos permite discutir los sistemas en función de los distintos valores que tome un parámetro determinado ya que, como vimos, es un método para determinar rangos.
- De la última ecuación deducimos los valores del parámetro a que nos pueden hacer que el sistema tenga o no solución, y en el caso de que tenga solución de que sea o no una única solución.
- $2−𝑎−𝑎²𝑧=1−𝑎$
- Tendremos que determinar los valores de a que hacen nulo al último coeficiente y si esos valores coinciden o no con el valor que anula el término independiente.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Discusión con parámetro: $x+y+az=1,\ x+ay+z=1,\ ax+y+z=1$ → $\left(\begin{smallmatrix}1&1&a&1\\1&a&1&1\\a&1&1&1\end{smallmatrix}\right)\xrightarrow{F_2-F_1,\ F_3-aF_1}\left(\begin{smallmatrix}1&1&a&1\\0&a-1&1-a&0\\0&1-a&1-a^2&1-a\end{smallmatrix}\right)\xrightarrow{F_3+F_2}\left(\begin{smallmatrix}1&1&a&1\\0&a-1&1-a&0\\0&0&2-a-a^2&1-a\end{smallmatrix}\right)$; última ecuación $(2-a-a^2)z=1-a$.

#### Diapositiva 49

- MÉTODO DE GAUSS
- UFV.ES
- Si a  1 y a  -2 el sistema es compatible determinado (SCD), ya que el coeficiente de z es distinto de cero, y podemos despejar:
- Si a = 1 , la última ecuación es de la forma 0 = 0 (en este caso también la segunda ecuación) por lo que el sistema tiene infinitas soluciones.
- Si a = -2 , la última ecuación queda 0 = 3, situación que es imposible y el sistema no tiene solución (es un Sistema Incompatible).

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $2-a-a^2=0\Rightarrow a=1$ ó $a=-2$. Si $a\neq1,-2$: SCD, $z=\frac{1-a}{2-a-a^2}=\frac{1-a}{(1-a)(a+2)}=\frac1{a+2}$. Si $a=1$: queda $x+y+z=1$ ⇒ $x=t,\ y=u,\ z=1-t-u$ (SCI, infinitas soluciones). Si $a=-2$: $0=3$ ⇒ SI.

#### Diapositiva 50

- MÉTODO DE GAUSS
- UFV.ES
- Análisis de un sistema por el método de Gauss
- Analicemos de forma genérica un sistema de tres ecuaciones con tres incógnitas en forma matricial.
- Para un sistema genérico en forma matricial, se trata de convertir la matriz ampliada en:
- Para discutir el sistema analizamos la última ecuación. En este caso, analizamos la última fila, y llegamos a dos situaciones diferentes:

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Matrices genéricas: sistema 3×3 y su forma escalonada; $A^*$ general $m\times n$ escalonada con $a'_{ii}$ en la diagonal y $b'_i$.

#### Diapositiva 51

- MÉTODO DE GAUSS
- UFV.ES
- Análisis de un sistema por el método de Gauss
- Para discutir el sistema analizamos la última ecuación. En este caso, analizamos la última fila, y llegamos a dos situaciones diferentes:
- Caso 1:
- Observamos que los rangos de las matrices A y A* son iguales, e iguales al número de ecuaciones y todo dependerá del número de incógnitas.
- Caso 2:
- Observamos que los rangos de las matrices A y A* no coinciden
- COMPATIBLE
- INCOMPATIBLE

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Caso 1: última fila $(0\ 0\ \cdots\ a'_{mn}\,|\,b'_m)$ con $a'_{mn}\neq0$ ⇒ compatible. Caso 2: última fila $(0\ 0\ \cdots\ 0\,|\,b'_m)$ con $b'_m\neq0$ ⇒ incompatible.

#### Diapositiva 52

- MÉTODO DE GAUSS
- UFV.ES
- Análisis de un sistema por el método de Gauss
- Si a  1 y a  -2 el sistema es compatible determinado (SCD), ya que el coeficiente de z es distinto de cero, y podemos despejar:
- Si a = 1 , la última ecuación es de la forma 0 = 0 (en este caso también la segunda ecuación) por lo que el sistema tiene infinitas soluciones.
- Si a = -2 , la última ecuación queda 0 = 3, situación que es imposible y el sistema no tiene solución (es un Sistema Incompatible).

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Repite el ejemplo con parámetro a (ver diapositivas 48–49).

#### Diapositiva 53

- REGLA DE CRAMER
- CAPÍTULO 06
- 53
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 54

- REGLA DE CRAMER
- UFV.ES
- Se dice que un sistema de ecuaciones lineales es un sistema de Cramer si el número de ecuaciones es igual al número de incógnitas y además el determinante formado por los coeficientes de las incógnitas es distinto de cero.
- La Regla de Cramer dice que:
- "un sistema de n ecuaciones con n incógnitas, en el cual el determinante de la matriz de los coeficientes es distinto de cero, admite una solución y sólo una, es decir, es un sistema compatible determinado".

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: $x-y=4,\ -x+y=2$: $\begin{vmatrix}1&-1\\-1&1\end{vmatrix}=1-1=0$ → NO es sistema de Cramer. $x-y=4,\ 2x+y=2$: $\begin{vmatrix}1&-1\\2&1\end{vmatrix}=1+2=3\neq0$ → SÍ es sistema de Cramer.

#### Diapositiva 55

- REGLA DE CRAMER
- UFV.ES

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Sistema n×n en forma matricial; $x_1=\frac{1}{|A|}\begin{vmatrix}b_1&a_{12}&\cdots&a_{1n}\\\vdots&&&\\b_n&a_{n2}&\cdots&a_{nn}\end{vmatrix}$, $x_2$ sustituyendo la 2ª columna por b, …, $x_n$ sustituyendo la última.

#### Diapositiva 56

- REGLA DE CRAMER
- UFV.ES
- ¿De dónde sale todo eso?

_Imágenes/medios en la diapositiva: 9_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Origen de la regla: $AX=B\Rightarrow X=A^{-1}B=\frac1{|A|}\operatorname{adj}(A)^tB$, de donde $x_1=\frac{b_1A_{11}+b_2A_{21}+\dots+b_nA_{n1}}{|A|}$, …, $x_n=\frac{b_1A_{1n}+\dots+b_nA_{nn}}{|A|}$; el numerador es el desarrollo por cofactores del determinante con la columna sustituida.

#### Diapositiva 57

- REGLA DE CRAMER
- UFV.ES
- La solución de un sistema de Cramer puede calcularse como:
- siendo Δi el determinante que resulta de sustituir la columna de la incógnita i–ésima por la matriz de términos independientes:

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $x_i=\frac{\Delta_i}{|A|}$, con $\Delta_i$ = determinante de A con la columna i sustituida por los términos independientes. Para 3×3: $x=\frac{\Delta_x}{|A|},\ y=\frac{\Delta_y}{|A|},\ z=\frac{\Delta_z}{|A|}$ con $\Delta_x=\begin{vmatrix}b_1&a_{12}&a_{13}\\b_2&a_{22}&a_{23}\\b_3&a_{32}&a_{33}\end{vmatrix}$, etc.

#### Diapositiva 58

- RESUMEN
- CAPÍTULO 07
- 58
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 59

- REGLA DE CRAMER
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen (imagen): sistema de ecuaciones lineales (ej. $x+y+z=3,\ 2x-y+z=2,\ x+2y-3z=0$); sistema homogéneo (mismo con términos 0); sistemas equivalentes (ej. $x+y=3,\ 2x-y=0$ y $x+2y=5,\ 2x-2y=-2,\ 3x-y=1$; ambos verifican x=1, y=2).

#### Diapositiva 60

- REGLA DE CRAMER
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen (imagen): expresión matricial ($6x+y=15,\ 3x+2y=8$ → $\begin{pmatrix}6&1\\3&2\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}15\\8\end{pmatrix}$); resolución por inversa $X=A^{-1}B$; teorema de Rouché-Frobenius (rg(A)=rg(A*)=n SCD, <n SCI; rg(A)<rg(A*) SI).

#### Diapositiva 61

- REGLA DE CRAMER
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen (imagen) regla de Cramer: $x_i=\Delta_i/|A|$ si $|A|\neq0$. Ejemplo: $\begin{pmatrix}6&1\\2&2\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}13\\6\end{pmatrix}$, $|A|=10$, $\Delta_x=\begin{vmatrix}13&1\\6&2\end{vmatrix}=20$, $\Delta_y=\begin{vmatrix}6&13\\2&6\end{vmatrix}=10$ ⇒ $x=2,\ y=1$.

#### Diapositiva 62

- Jamás se descubriría nada si nos considerásemos satisfechos con las cosas descubiertas
- Lucius Annaeus Seneca
- Filósofo, político, orador y escritor romano (4ac – Córduba / 12 abril 65 – Roma)
- QUOTE

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Cita sobre fondo azul (Séneca).

#### Diapositiva 63

- SISTEMAS DE ECUACIONES LINEALES
- 91 351 03 03
- INFO@UFV.ESUFV.ES
- CTRA. POZUELO-MAJADAHONDA
- KM 1.800, 28223 POZUELO DE ALARCÓN
- MADRID. ES

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Contraportada UFV 'Sistemas de ecuaciones lineales'.


## Diapositivas: Matrices

*Fuente: `01_1 - Matrices_R00.pptm`*

#### Diapositiva 1

- MATRICES
- MATEMÁTICAS PARA LA INGENIERÍA I
- Prof. Dr. Josemaría Medina Villaverde
- UFV.ES

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 2

- Objetivos
- 01
- ÍNDICE
- Definición
- 02
- Tipos de matrices
- 03
- Operaciones con matrices
- 04
- Rango de una matriz
- 05
- Matrices elementales
- 06
- Matrices equivalentes
- 07
- Factorización LU
- 08
- Condición de una matriz
- 09
- Resumen
- 10

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 3

- OBJETIVOS
- CAPÍTULO 01
- 3
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 4

- OBJETIVOS
- 4
- UFV.ES
- Familiarizarse con el manejo de matrices y determinantes como herramienta básica para poder ordenar datos, resolver sistemas de ecuaciones lineales, …
- Aprender a manejar matrices con MATLAB™

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 5

- DEFINICIÓN
- CAPÍTULO 02
- 5
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 6

- DEFINICIÓN
- 6
- UFV.ES
- Definición
- Se llama matriz de orden m × n a un conjunto de números reales dispuestos en m filas y en n columnas, de la forma:
- Las matrices se representan por letras mayúsculas A, B, C,… Los elementos de la matriz (los números) se representan en general por aij, donde los subíndices (i, j) nos dan la posición que ocupa el término:
- Así, el término a13 es el elemento que está en la primera fila y en la tercera columna.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Fórmula (imagen): $A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}$; $i=1,\dots,m\to$ fila, $j=1,\dots,n\to$ columna.

#### Diapositiva 7

- DEFINICIÓN
- UFV.ES
- Dimensión de una matriz
- El número de filas (m) y el número de columnas (n) nos da la dimensión de la matriz m × n.
- Dos matrices son iguales si tienen la misma dimensión y si los términos que ocupan la misma posición son iguales:
- es una matriz de dimensión
- 2 x 3
- Igualdad de matrices

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $\begin{pmatrix}3&-1&4\\1&5&-9\end{pmatrix}$ es de dimensión 2×3. Igualdad: $A=B\Rightarrow a_{11}=b_{11}, a_{21}=b_{21}, a_{12}=b_{12}, a_{22}=b_{22}, a_{13}=b_{13}, a_{23}=b_{23}\Rightarrow a_{ij}=b_{ij}$.

#### Diapositiva 8

- DEFINICIÓN
- UFV.ES
- Actividades
- Indica la dimensión de las siguientes matrices:
- 2 × 3
- 1 × 4
- 3 × 1
- 3 × 3
- $𝐸=1$
- 1 × 1

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Actividad (dimensiones, con soluciones en recuadros): $A=\begin{pmatrix}5&-1&4\\1&7&-9\end{pmatrix}$ → 2×3; $B=(3\ 2\ -6\ 0)$ → 1×4; $C=(0,1,2)^T$ → 3×1; $D=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$ → 3×3; $E=(1)$ → 1×1.

#### Diapositiva 9

- DEFINICIÓN
- UFV.ES
- Actividades
- Determina los valores de a, b, x, y para que las matrices A y B sean iguales
- $𝐶= 2416           𝐷=𝑥214𝑦3$
- Determina los valores de x, y para que las matrices C y D sean iguales

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Actividades: hallar a, b, x, y para que $A=(3\ a\ -6\ b)$ y $B=(x\ 2\ y\ 0)$ sean iguales; hallar x, y para que $C=\begin{pmatrix}2&4\\1&6\end{pmatrix}$ y $D=\begin{pmatrix}x&2&1\\4&y&3\end{pmatrix}$ sean iguales (no pueden serlo: distinta dimensión).

#### Diapositiva 10

- TIPOS DE MATRICES
- CAPÍTULO 03
- 10
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 11

- TIPOS DE MATRICES
- 11
- UFV.ES
- Si el número de filas es distinto del número de columnas (n ≠ m) la matriz se llama rectangular.
- Dentro de las matrices rectangulares tenemos los siguientes tipos:
- Matriz fila: Es aquella que sólo tiene una fila.
- Matriz columna: Es la que sólo tiene una columna.
- Si el número de filas es igual al número de columnas (m = n) se habla de una matriz cuadrada.
- Dentro de las matrices cuadradas es importante destacar que los elementos aij en que los dos subíndices son iguales forman la diagonal principal, y los elementos en que i+j = n+1 (donde n es el orden de la matriz) forman la diagonal secundaria.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Diagrama de una matriz 3×3 marcando la diagonal principal ($a_{11},a_{22},a_{33}$) y la diagonal secundaria ($a_{13},a_{22},a_{31}$).

#### Diapositiva 12

- TIPOS DE MATRICES
- UFV.ES
- Matriz Triangular:
- Es aquella matriz en la que los elementos situados por encima o por debajo de la diagonal principal son nulos.
- Matriz Diagonal:
- Es aquella matriz en la que los elementos que no están en la diagonal principal son nulos: aij = 0 si i ≠ j
- Matriz Escalar:
- Es aquella matriz diagonal en la que los elementos de la diagonal principal son todos iguales.
- Matriz Unidad (Identidad):
- Es la matriz escalar en la que los elementos no nulos son iguales a 1. Se representa por I.
- Matriz Nula:
- Es aquella en la que todos sus elementos son cero.

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: triangular superior $\begin{pmatrix}1&2&3\\0&4&-1\\0&0&2\end{pmatrix}$, triangular inferior $\begin{pmatrix}1&0&0\\2&-1&0\\3&1&-2\end{pmatrix}$; diagonales $\operatorname{diag}(1,4,2)$ y $\operatorname{diag}(1,0,2)$; escalar $\operatorname{diag}(2,2,2)$; identidad $I_3$; matriz nula de tamaño 3.

#### Diapositiva 13

- OPERACIONES CON MATRICES
- CAPÍTULO 04
- 13
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 14

- OPERACIONES CON MATRICES
- 14
- UFV.ES
- Suma
- Dadas dos matrices A y B de dimensión m × n, se define la suma de matrices (A+B) como aquella matriz cuyos elementos son la suma de los elementos que ocupan la misma posición:
- $𝐶=𝐴+𝐵 → 𝑐𝑖𝑗=𝑎𝑖𝑗+𝑏𝑖𝑗$
- - Propiedad Asociativa      A+(B+C) = (A+B)+C.
- - Elemento neutro (la matriz nula).
- - Elemento opuesto (–A): A + (–A) = 0
- - Propiedad Conmutativa: A + B = B + A

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Suma: $C=A+B$, $c_{ij}=a_{ij}+b_{ij}$. Ejemplo: $A=\begin{pmatrix}1&2&4\\-1&3&2\\0&-2&1\end{pmatrix}$, $B=\begin{pmatrix}2&-1&3\\-2&3&4\\-3&-1&5\end{pmatrix}$, $A+B=\begin{pmatrix}3&1&7\\-3&6&6\\-3&-3&6\end{pmatrix}$.

#### Diapositiva 15

- OPERACIONES CON MATRICES
- 15
- UFV.ES
- $𝐴=1234         𝐵=60       𝐶=𝐴+𝐵= ?$
- Ejercicio: Calcular la suma de matrices A + B:

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejercicio trampa: $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}6\\0\end{pmatrix}$, $C=A+B=?$ (no se puede: distintas dimensiones). Meme 'No me engañas'.

#### Diapositiva 16

- OPERACIONES CON MATRICES
- 16
- UFV.ES
- Producto de un número (escalar) por una matriz
- El producto de un número real k por una matriz A= (aij) es otra matriz de la misma dimensión cuyos elementos son los productos de los elementos de la matriz A por el número k:
- $𝑘𝐴=𝑘𝑎𝑖𝑗=𝑘𝑎𝑖𝑗$
- Propiedad Distributiva respecto de la suma de matrices:
- Propiedad Distributiva respecto de la suma de números:
- Propiedad Asociativa mixta:
- 1·A = A

_Imágenes/medios en la diapositiva: 8_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $kA=k(a_{ij})=(ka_{ij})$. Ejemplo: $A=\begin{pmatrix}1&2&4\\-1&3&2\\0&-2&1\end{pmatrix}$, $5A=\begin{pmatrix}5&10&20\\-5&15&10\\0&-10&5\end{pmatrix}$. Propiedades: $k(A+B)=kA+kB$; $(k+l)A=kA+lA$; $k(lA)=(kl)A$; $1\cdot A=A$.

#### Diapositiva 17

- OPERACIONES CON MATRICES
- 17
- UFV.ES
- Producto de matrices
- Sean las matrices A y B de dimensiones m×n y n×p (es decir, el número de columnas de la matriz A es igual al número de filas de la matriz B).
- Se define el producto A·B, y en ese orden, como una matriz C de dimensiones m×p cuyos elementos son de la forma:
- $𝑐12= 𝑎11∗𝑏12+𝑎12∗𝑏22+𝑎13∗𝑏32+….+𝑎1𝑛∗𝑏𝑛2$
- - Propiedad distributiva respecto de la suma de matrices:

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $C=AB$, $c_{ij}=\sum_{k=1}^n a_{ik}b_{kj}$ (p. ej. $c_{12}=a_{11}b_{12}+a_{12}b_{22}+\dots+a_{1n}b_{n2}$). Propiedades: $A(BC)=(AB)C$; $AI=IA=A$; $A(B+C)=AB+AC$. Ejemplo: $\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\begin{pmatrix}2&1\\3&2\\4&1\end{pmatrix}=\begin{pmatrix}20&8\\47&20\end{pmatrix}$ (2×3 · 3×2 → 2×2).

#### Diapositiva 18

- OPERACIONES CON MATRICES
- 18
- UFV.ES
- $𝐴=123456      𝐵=987          𝐶=𝐴·𝐵=1·9+2·8+3·74·9+5·8+6·7$
- $2𝑥3                         3𝑥1                     2𝑥1$
- $𝐴=123456      𝐵=145654020$
- $2𝑥3                                3𝑥3$
- $𝐶=𝐴·𝐵=1·1+2·6+3·01·4+2·5+3·21·5+2·4+3·04·1+5·6+6·04·4+5·5+6·24·5+5·4+6·0$
- $2𝑥3$
- Producto de matrices

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: $\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\begin{pmatrix}9\\8\\7\end{pmatrix}=\begin{pmatrix}1\cdot9+2\cdot8+3\cdot7\\4\cdot9+5\cdot8+6\cdot7\end{pmatrix}$ (2×1); $\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\begin{pmatrix}1&4&5\\6&5&4\\0&2&0\end{pmatrix}$ = matriz 2×3 con $c_{ij}$ desarrollados (p. ej. $1\cdot1+2\cdot6+3\cdot0$).

#### Diapositiva 19

- OPERACIONES CON MATRICES
- 19
- UFV.ES
- Trasposición
- Dada una matriz A de dimensiones m×n, se llama matriz traspuesta de A y se representa por At, a la matriz que se obtiene al cambiar las filas de A por sus columnas, por lo que la matriz At será de dimensión n×m.
- Una matriz cuadrada se dice que es simétrica cuando coincide con su traspuesta: A=At.
- Para que una matriz sea simétrica, los elementos simétricos respecto de la diagonal principal deben ser iguales.
- Si una matriz cuadrada es igual a la opuesta de su traspuesta, A=−At, se dice que es antisimétrica.
- Para que una matriz sea antisimétrica debe cumplirse que los elementos simétricos respecto de la diagonal principal sean opuestos, y los elementos de la diagonal principal nulos.

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: $A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\to A^t=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$; simétrica $A=\begin{pmatrix}1&1&3\\1&2&4\\3&4&5\end{pmatrix}=A^t$; antisimétrica $A=\begin{pmatrix}0&1&-3\\-1&0&-4\\3&4&0\end{pmatrix}$, $A^t=\begin{pmatrix}0&-1&3\\1&0&4\\-3&-4&0\end{pmatrix}$, $-A^t=A$.

#### Diapositiva 20

- OPERACIONES CON MATRICES
- 20
- UFV.ES
- Trasposición
- Con las matrices traspuestas se cumplen las siguientes propiedades:
- La traspuesta de una suma de matrices es igual a la suma de las matrices traspuestas:
- La traspuesta de un producto de matrices es igual al producto en orden inverso de las matrices traspuestas:
- $𝐴·𝐵𝑡=𝐵𝑡·𝐴𝑡$
- $𝐴+𝐵𝑡=𝐴𝑡+𝐵𝑡$

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $(A+B)^t=A^t+B^t$; $(A\cdot B)^t=B^t\cdot A^t$.

#### Diapositiva 21

- OPERACIONES CON MATRICES
- 21
- UFV.ES
- Matriz inversa
- Si dada una matriz cuadrada A existe otra matriz B, también cuadrada, que multiplicada por la matriz A nos da la matriz unidad, se dice que la matriz A es una matriz regular o inversible y a la matriz B se le llama matriz inversa de A y se representa por A–1:
- $𝐴·𝐴−1=𝐴−1·𝐴=𝐼$
- Si una matriz cuadrada no tiene matriz inversa, se dice que la matriz es singular.
- La matriz inversa verifica las siguientes propiedades:
- La inversa de la matriz inversa es la matriz original.
- La inversa del producto de dos matrices es el producto de las inversas de las matrices cambiando su orden.
- La inversa de la traspuesta de una matriz es igual a la traspuesta de la matriz inversa.
- $𝐴−1−1=𝐴$
- $𝐴·𝐵−1=𝐵−1·𝐴−1$
- $𝐴𝑡−1=𝐴−1𝑡$

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $AA^{-1}=A^{-1}A=I$; $(A^{-1})^{-1}=A$; $(AB)^{-1}=B^{-1}A^{-1}$; $(A^t)^{-1}=(A^{-1})^t$.

#### Diapositiva 22

- OPERACIONES CON MATRICES
- 22
- UFV.ES
- Matriz inversa
- Para hallar una matriz inversa dispondremos de varios métodos distintos. En este tema veremos dos:
- Resolver un sistema de ecuaciones
- El método de Gauss – Jordan
- Sistema de ecuaciones
- Sea la matriz A la indicada. Halla la matriz inversa A–1 mediante un sistema de ecuaciones.

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Inversa de $A=\begin{pmatrix}0&1\\2&0\end{pmatrix}$ por sistema: $A^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $AA^{-1}=\begin{pmatrix}c&d\\2a&2b\end{pmatrix}=I\Rightarrow c=1, d=0, 2a=0, 2b=1\Rightarrow A^{-1}=\begin{pmatrix}0&1/2\\1&0\end{pmatrix}$.

#### Diapositiva 23

- OPERACIONES CON MATRICES
- 23
- UFV.ES
- Método de Gauss – Jordan
- El método de Gauss-Jordan para hallar la matriz inversa consiste en convertir la matriz inicial en la matriz identidad, utilizando transformaciones elementales.
- Llamamos transformaciones elementales por filas a:
- Permutar dos filas i y j. Lo escribimos como Fi↔Fj
- Sustituir la fila i por el resultado de multiplicar o dividir todos sus elementos por un número a ≠ 0. Lo escribimos como Fi =aFi
- Sustituir la fila i por un múltiplo (no nulo) de ella más otra fila j multiplicada por un número b. Lo escribimos como Fi =aFi + bFj, con a ≠ 0 .
- Ampliamos la matriz original, escribiendo junto a ella la matriz identidad, y aplicamos las transformaciones elementales de modo que la matriz inicial se transforme en la matriz identidad.
- Matriz inversa

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 24

- OPERACIONES CON MATRICES
- 24
- UFV.ES
- Matriz inversa
- Método de Gauss – Jordan
- Calcula con el método de Gauss–Jordan la inversa de la matriz

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Gauss-Jordan: $T=\left(\begin{smallmatrix}0&1&|&1&0\\2&0&|&0&1\end{smallmatrix}\right)\xrightarrow{F_1\leftrightarrow F_2}\left(\begin{smallmatrix}2&0&|&0&1\\0&1&|&1&0\end{smallmatrix}\right)\xrightarrow{F_1\to\frac12F_1}\left(\begin{smallmatrix}1&0&|&0&1/2\\0&1&|&1&0\end{smallmatrix}\right)$ ⇒ $A^{-1}=\begin{pmatrix}0&1/2\\1&0\end{pmatrix}$.

#### Diapositiva 25

- RANGO DE UNA MATRIZ
- CAPÍTULO 05
- 25
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 26

- RANGO DE UNA MATRIZ
- 26
- UFV.ES
- Rango
- Se llama rango de una matriz al número de filas o columnas de la matriz que son linealmente independientes, es decir, que no pueden obtenerse a partir de las demás filas o columnas de la misma matriz.
- Ejemplo
- Determina el rango de las matrices A y B siguientes
- La tercera fila de A se obtuvo sumando las dos primeras filas. Estas dos primeras filas son independientes, por lo que el rango de A es 2.
- La tercera fila de B se obtuvo restando la segunda fila al doble de la primera. El rango de B es 2.
- Para hallar el rango de una matriz se pueden usar las transformaciones elementales para intentar hacer el máximo número posible de ceros, intentando triangular la matriz (método de Gauss).
- Puede ser más fácil hallar el rango usando determinantes, como veremos en el capítulo siguiente.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $A=\begin{pmatrix}0&1&-3\\-1&0&-4\\-1&1&-7\end{pmatrix}$, $B=\begin{pmatrix}0&-1&3\\1&0&4\\-1&-2&2\end{pmatrix}$; ambas de rango 2.

#### Diapositiva 27

- RANGO DE UNA MATRIZ
- 27
- UFV.ES
- Rango
- Se llama rango de una matriz al número de filas o columnas de la matriz que son linealmente independientes, es decir, que no pueden obtenerse a partir de las demás filas o columnas de la misma matriz.
- Esta definición está ligada con el concepto de determinantes y con el método de Gauss.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 28

- RANGO DE UNA MATRIZ
- 28
- UFV.ES
- Rango de una matriz
- Se llama rango (o característica) de una matriz (o característica de una matriz) al orden del menor de mayor orden no nulo
- “Si todos los menores de un determinado orden son nulos, también lo son los de órdenes superiores”
- OTRA DEFINICIÓN EQUIVALENTE
- ¿Podría tener rango = 3 esta matriz?

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $A=\begin{pmatrix}1&3\\0&-2\\5&-1\\-2&3\end{pmatrix}$, $\begin{vmatrix}1&3\\0&-2\end{vmatrix}=-2\neq0\Rightarrow\operatorname{rg}(A)=2$. Imagen de un mono pensando: '¿Podría tener rango = 3 esta matriz?' (no: sólo tiene 2 columnas).

#### Diapositiva 29

- RANGO DE UNA MATRIZ
- 29
- UFV.ES
- El rango de una matriz es el número de filas con algún elemento distinto de cero que hay en cualquier forma escalonada por filas.
- Esta definición equivale a decir que el rango de una matriz es el número de filas (o columnas) que son linealmente independientes.
- También se puede ver el rango como el orden de la mayor submatriz cuyo determinante sea distinto de cero.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 30

- MATRICES ELEMENTALES
- CAPÍTULO 06
- 30
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 31

- MATRICES ELEMENTALES
- 31
- UFV.ES
- I3
- Una Matriz Elemental es aquella matriz de orden n que se obtiene aplicando a la matriz identidad In una única operación elemental por filas.
- Operaciones elementales:
- Intercambio de filas
- Producto de una fila por un escalar (número real distinto de 0)
- Combinación de la suma de unas filas con otras
- Permutación

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos de matrices elementales desde $I_3$: $\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$ (intercambio fila 2 con fila 3); $\begin{pmatrix}1&0&0\\0&1&0\\0&0&5\end{pmatrix}$ (multiplicación de la fila 3 por 5); $\begin{pmatrix}1&0&0\\0&1&2\\0&0&1\end{pmatrix}$ (fila 2 = fila 2 + 2·fila 3).

#### Diapositiva 32

- MATRICES ELEMENTALES
- 32
- UFV.ES
- OPERACIONES ELEMENTALES INVERSAS
- Son aquellas que anulan la acción de una operación elemental

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla: operación elemental ↔ inversa: cambiar fila i por j ↔ cambiar j por i; multiplicar una fila por $k\neq0$ ↔ por $1/k$; sumar a la fila i la j multiplicada por k ↔ por −k. Ejemplos: $I\xrightarrow{F_{1,3}}E=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}\xrightarrow{F_{3,1}}I$; $I\xrightarrow{F_2(2)}E=\operatorname{diag}(1,2,1)\xrightarrow{F_2(1/2)}I$.

#### Diapositiva 33

- MATRICES ELEMENTALES
- 33
- UFV.ES
- Matrices y operaciones elementales
- Si la matriz elemental E corresponde a la operación elemental Op entonces:
- Si A → Op → A1, entonces ExA = A1
- El resultado de aplicarle a la matriz A la operación elemental Op equivale a multiplicar la matriz A por la izquierda por la matriz elemental asociada a Op.
- Ejemplo
- Una operación del método de eliminación gaussiana es
- Esta corresponde a

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: en la eliminación, $\left(\begin{smallmatrix}3&6&-9&|&3\\0&0&-2&|&-2\\0&1&-2&|&1\end{smallmatrix}\right)\xrightarrow{R_2\leftrightarrow R_3}\left(\begin{smallmatrix}3&6&-9&|&3\\0&1&-2&|&1\\0&0&-2&|&-2\end{smallmatrix}\right)$, que equivale a multiplicar por la izquierda por $\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$.

#### Diapositiva 34

- MATRICES ELEMENTALES
- 34
- UFV.ES
- Matrices y operaciones elementales
- Utilizando la matriz elemental:
- Aplicar el intercambio de filas R2       R3 a la matriz unidad da como resultado la matriz elemental E
- $100010001→𝑅2↔𝑅3→100001010$

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** La matriz elemental E del intercambio $R_2\leftrightarrow R_3$ es $\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$; aplicada al ejemplo anterior da el mismo resultado.

#### Diapositiva 35

- MATRICES ELEMENTALES
- 35
- UFV.ES
- Matrices y operaciones elementales

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen: Multiplicación — multiplica la fila i de A por $c\neq0$ ($cF_i$); inversa multiplica por $1/c$ ($\frac1cF_i$). Suma — multiplica la fila i por c y la suma a la fila j ($F_j+cF_i$); inversa $F_j-cF_i$. Permutación — permuta filas i y j ($P_{ij}$); inversa $P_{ij}$.

#### Diapositiva 36

- MATRICES ELEMENTALES
- 36
- UFV.ES
- Matrices y operaciones elementales
- Las matrices elementales son invertibles
- TEOREMA
- Cuando aplicamos una operación elemental sobre I, obtenemos una matriz elemental E.
- Cuando aplicamos una operación elemental inversa sobre I, obtenemos la inversa de E, es decir, E−1 .
- Por tanto, toda matriz elemental E tiene inversa, que es también una matriz elemental

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $E_1=\begin{pmatrix}1&-3\\0&1\end{pmatrix}, E_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}, E_3=\begin{pmatrix}1&0\\0&-4\end{pmatrix}$ ⇒ $E_1^{-1}=\begin{pmatrix}1&3\\0&1\end{pmatrix}, E_2^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}, E_3^{-1}=\begin{pmatrix}1&0\\0&-1/4\end{pmatrix}$.

#### Diapositiva 37

- MATRICES ELEMENTALES
- 37
- UFV.ES
- Matrices y operaciones elementales
- Dadas las matrices elementales 3 × 3 que se obtienen de realizar las operaciones elementales F1,3, F2(2) y F2,3(−3), halla sus matrices inversas
- Ejercicios:
- Dada la matriz $𝐴=1−102$:
- halla las matrices elementales tales que E2E1A = I
- halla las matrices elementales inversas de E1 y E2
- escribe A como producto de matrices elementales

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejercicios: dadas las matrices elementales 3×3 de las operaciones $F_{1,3}$, $F_2(2)$ y $F_{2,3}(-3)$, hallar sus inversas. Dada $A=\begin{pmatrix}1&-1\\0&2\end{pmatrix}$: hallar matrices elementales con $E_2E_1A=I$; hallar las inversas de $E_1$ y $E_2$; escribir A como producto de elementales.

#### Diapositiva 38

- MATRICES EQUIVALENTES
- CAPÍTULO 07
- 38
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 39

- MATRICES EQUIVALENTES
- 39
- UFV.ES
- Dos matrices de la misma dimensión, A y B, son equivalentes si existe una matriz elemental (o producto de ellas), E, tal que A=E·B.
- Lo expresamos como A∼B.
- Ejercicio:
- Demuestra que las matrices A y B son equivalentes

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejercicio: demostrar que $A=\begin{pmatrix}2&0&-1\\1&2&3\\5&-2&1\end{pmatrix}$ y $B=\begin{pmatrix}1&2&3\\2&0&-1\\4&-4&-2\end{pmatrix}$ son equivalentes (pista: $F_{1,2}$ y $F_{3,1}(-1)$).

#### Diapositiva 40

- FACTORIZACIÓN LU
- CAPÍTULO 08
- 40
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 41

- FACTORIZACIÓN LU
- 41
- UFV.ES
- TEOREMA
- Dada una matriz invertible A, se puede encontrar mediante eliminación gaussiana, sin intercambio de filas, una factorización de la forma A = LU, siendo:
- L una matriz triangular inferior unitaria (con unos en la diagonal), y
- U una matriz triangular superior, en la que la primera fila coincide con la primera fila de A
- La factorización LU es única. Es útil para el cálculo de determinantes e inversas de matrices grandes, así como para la resolución de sistemas de ecuaciones lineales

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Forma general: $L=\begin{pmatrix}1&0&\cdots&0\\*&1&\cdots&0\\\vdots&&\ddots&\vdots\\*&*&\cdots&1\end{pmatrix}$, $U=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\0&*&\cdots&*\\\vdots&&\ddots&\vdots\\0&0&\cdots&*\end{pmatrix}$.

#### Diapositiva 42

- FACTORIZACIÓN LU
- 42
- UFV.ES
- Sabemos que, a partir de A, se puede llegar a una matriz escalonada U aplicando operaciones elementales, por lo que:
- El problema se reduce, por tanto, al cálculo de una serie de matrices elementales (y sus inversas).

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $E_kE_{k-1}\cdots E_2E_1A=U\Rightarrow A=(E_k\cdots E_1)^{-1}U$, con $L=E_1^{-1}E_2^{-1}\cdots E_{k-1}^{-1}E_k^{-1}$.

#### Diapositiva 43

- FACTORIZACIÓN LU
- 43
- UFV.ES
- Sin embargo, en la práctica no hace falta calcular estas matrices, sino que se emplea el algoritmo de los multiplicadores cambiados de signo, que se ilustra a continuación.
- Ejemplo: Halla la factorización LU de la siguiente matriz
- Finalmente

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $A=\begin{pmatrix}-2&4&-1\\4&-5&4\\-6&-3&-14\end{pmatrix}$. $F_{2,1}(2)$ → $L$ recibe −2 en (2,1); $F_{3,1}(-3)$ → 3 en (3,1); $F_{3,2}(5)$ → −5 en (3,2). Resultado: $A=\begin{pmatrix}1&0&0\\-2&1&0\\3&-5&1\end{pmatrix}\begin{pmatrix}-2&4&-1\\0&3&2\\0&0&-1\end{pmatrix}=LU$.

#### Diapositiva 44

- FACTORIZACIÓN LU
- 44
- UFV.ES
- Veamos el porqué del método de coeficientes para hallar L
- $𝑈= 𝐸3·𝐸2·𝐸1·𝐴$
- $𝑈=𝐸·𝐴$
- $𝐸= 𝐸3·𝐸2·𝐸1$
- E es también una matriz elemental, y “contiene” todas las transformaciones elementales sobre A para obtener U
- Como E es elemental, tiene inversa
- E-1 “contiene” las transformaciones elementales inversas para obtener A a partir de U
- E-1  = L
- Por eso, L contiene los coeficientes de combinación cambiados de signo
- $𝐸−1= 𝐸1−1·𝐸2−1·𝐸3−1$
- $𝐴=𝐸−1𝑈$

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $U=E_3E_2E_1A=EA$ con $E=E_3E_2E_1$; $E^{-1}=E_1^{-1}E_2^{-1}E_3^{-1}$; $A=E^{-1}U$, así que $E^{-1}=L$.

#### Diapositiva 45

- CONDICIÓN DE UNA MATRIZ
- CAPÍTULO 09
- 45
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 46

- CONDICIÓN DE UNA MATRIZ
- 46
- UFV.ES
- En el campo del análisis numérico, el número de condición de una función respecto de su argumento mide cuánto se modifica el valor de salida si se realiza un cambio en el valor de entrada.
- Es decir, cuánto cambia y = f(x) si se modifica x.
- El número de condición se utiliza para medir cuán sensible resulta una función a cambios o errores en el valor de entrada, y cuál será el error en el valor de salida debido a este.
- Se dice que la matriz A de un sistema está bien condicionada si su número de condición está cerca de 1 y que está mal condicionada si es significativamente mayor que 1, lo que indicaría que pequeñas variaciones en los datos pueden producir grandes variaciones en los resultados y por tanto que la solución del sistema es propensa a grandes errores de redondeo.
- Un número de condición para una matriz mide cuán sensible es la respuesta a las perturbaciones en los datos de entrada y a los errores de redondeo cometidos durante el proceso de solución.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 47

- CONDICIÓN DE UNA MATRIZ
- 47
- UFV.ES
- Hay que señalar que hay muchos números de condición diferentes.
- En general, un número de condición se aplica no solo a una matriz en particular, sino también al problema que se está resolviendo. ¿Estamos resolviendo ecuaciones lineales, invirtiendo una matriz, encontrando sus valores propios o calculando el exponencial?
- Una matriz puede estar mal condicionada para la inversión, mientras que el problema de los valores propios está bien condicionado. O al revés.
- Sin embargo, cuando decimos simplemente que una matriz está "mal condicionada", generalmente estamos pensando sólo en la sensibilidad de su inversa, es decir, del número de condición para la inversión, y no en todos los demás números de condición.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 48

- CONDICIÓN DE UNA MATRIZ
- 48
- UFV.ES
- EJEMPLO
- Investiguemos un sistema de ecuaciones lineales que involucra las matrices:
- $𝐴=4.12.89.76.6$
- $𝑏= 4.19.7$
- Se resuelve con MATLAB. A la derecha vemos las dos rectas que componen el sistema de ecuaciones lineales y su solución

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $A=\begin{pmatrix}4.1&2.8\\9.7&6.6\end{pmatrix}$, $b=\begin{pmatrix}4.1\\9.7\end{pmatrix}$. Gráfica MATLAB de las dos rectas (casi coincidentes) y su intersección en (1, 0).

#### Diapositiva 49

- CONDICIÓN DE UNA MATRIZ
- 49
- UFV.ES
- EJEMPLO
- Investiguemos un sistema de ecuaciones lineales que involucra las matrices:
- $𝐴=4.12.89.76.6$
- $𝑏= 4.119.7$

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Mismo A con $b=(4.11, 9.7)^T$: dos gráficas comparadas; con un cambio mínimo en b la intersección se desplaza de (1, 0) a aproximadamente (0.34, 0.97) → matriz mal condicionada.

#### Diapositiva 50

- Resumen
- CAPÍTULO 10
- 50
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 51

- Resumen
- 51
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen (imagen): definición de matriz (tabla de números ordenados, ej. $\begin{pmatrix}5&-2&0\\3&4&-7\end{pmatrix}$); dimensión (m filas × n columnas, aquí 2×3); igualdad ($A=B\Rightarrow a_{ij}=b_{ij}\ \forall i,j$); tipos: fila $(31\ 4\ -5)$, columna $(-5,7)^T$, triangular $\begin{pmatrix}1&-1\\0&3\end{pmatrix}$, diagonal $\operatorname{diag}(2,5)$, escalar $\operatorname{diag}(5,5)$, unidad $I_2$.

#### Diapositiva 52

- Resumen
- 52
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla resumen (imagen): suma ($c_{ij}=a_{ij}+b_{ij}$; $\begin{pmatrix}2&0\\0&5\end{pmatrix}+\begin{pmatrix}4&8\\1&2\end{pmatrix}=\begin{pmatrix}6&8\\1&7\end{pmatrix}$); producto por real ($3\begin{pmatrix}2&1\\4&5\end{pmatrix}=\begin{pmatrix}6&3\\12&15\end{pmatrix}$); producto de matrices ($\begin{pmatrix}1&0\\2&3\end{pmatrix}\begin{pmatrix}2&1\\4&5\end{pmatrix}=\begin{pmatrix}2&1\\16&17\end{pmatrix}$); inversa ($A=\begin{pmatrix}2&3\\5&1\end{pmatrix}\to A^{-1}=\begin{pmatrix}-1/13&3/13\\5/13&-2/13\end{pmatrix}$); traspuesta ($\begin{pmatrix}2&3\\5&1\end{pmatrix}\to\begin{pmatrix}2&5\\3&1\end{pmatrix}$); rango (nº de filas o columnas l.i.; $\begin{pmatrix}6&3\\12&6\end{pmatrix}$ tiene rango 1).

#### Diapositiva 53

- «Ninguna investigación humana puede ser denominada ciencia si no pasa a través de pruebas matemáticas»
- LEONARDO DA VINCI
- pintor, anatomista, arquitecto, paleontólogo, botánico, escritor, escultor, filósofo, ingeniero, inventor, músico, poeta y urbanista italiano (1452 – 1519)
- QUOTE

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Cita sobre fondo azul con retrato de Leonardo da Vinci.

#### Diapositiva 54

- MATRICES
- 91 351 03 03
- INFO@UFV.ESUFV.ES
- CTRA. POZUELO-MAJADAHONDA
- KM 1.800, 28223 POZUELO DE ALARCÓN
- MADRID. ES

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Contraportada UFV 'Matrices' con datos de contacto.


## Diapositivas: Determinantes

*Fuente: `01_2 - Determinantes_R00.pptm`*

#### Diapositiva 1

- DETERMINANTES
- MATEMÁTICAS PARA LA INGENIERÍA I
- Prof. Dr. Josemaría Medina Villaverde
- UFV.ES

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 2

- Definición
- 01
- ÍNDICE
- Menores y cofactores
- 02
- Propiedades de los determinantes
- 03
- Operaciones con matrices
- 04
- Rango de una matriz
- 05
- Resumen
- 10

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 3

- Definición
- CAPÍTULO 01
- 3
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 4

- definición
- 4
- UFV.ES
- Dada una matriz cuadrada de orden n,
- se llama determinante de la matriz A y se representa por |A|
- a un número real que es igual a:
- Es decir, el determinante de una matriz cuadrada es el número real que se obtiene sumando todos los n factorial (n!) productos posibles de n elementos (orden de la matriz) de la matriz, de forma que en cada producto haya un elemento de cada fila y uno de cada columna, precedido cada producto con el signo + ó – según que la permutación de los subíndices que indican la columna tenga un número de inversiones, respecto del orden natural, que sea par o impar.
- Esta definición sólo es práctica para resolver los determinantes de orden 2 y 3. Los determinantes de orden superior se resuelven con otros métodos, ya que aplicando la definición sería muy laborioso.

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Fórmula (imagen): $\det(A)=|A|=\sum_{\sigma\in S_n}(-1)^{i(\sigma)}a_{1\sigma(1)}a_{2\sigma(2)}\cdots a_{n\sigma(n)}$.

#### Diapositiva 5

- definición
- 5
- UFV.ES
- Determinantes de orden dos
- Dada una matriz de orden 2,
- se llama determinante de la matriz A,
- al número:
- Es decir, se multiplican los elementos de la diagonal principal y se le resta el producto de los elementos de la diagonal secundaria.

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $|A|=\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}=a_{11}a_{22}-a_{12}a_{21}$ (diagrama: diagonal principal con +, secundaria con −).

#### Diapositiva 6

- definición
- 6
- UFV.ES
- Determinantes de orden dos

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: $\begin{vmatrix}2&5\\1&4\end{vmatrix}=2\cdot4-5\cdot1=3$; $\begin{vmatrix}-1&-2\\-4&3\end{vmatrix}=-1\cdot3-(-2)(-4)=-3-8=-11$.

#### Diapositiva 7

- definición
- 7
- UFV.ES
- Determinantes de orden tres. Regla de Sarrus
- Dada una matriz de orden 3,
- se llama determinante de la matriz A al número:
- Este desarrollo procedente de la definición de determinante puede recordarse fácilmente con este diagrama, conocido como la regla de Sarrus:

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Sarrus: $|A|=a_{11}a_{22}a_{33}+a_{13}a_{21}a_{32}+a_{12}a_{23}a_{31}-a_{13}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}$, con el diagrama de triángulos (+ y −).

#### Diapositiva 8

- definición
- 8
- UFV.ES
- El determinante es un número real asociado a una matriz cuadrada de números reales
- |A| =
- = a11a22a33 + a21a32a13 + a12a23a31 - a13a22a31 - a32a23a11 - a21a12a33

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Diagrama de Sarrus con colores: $=a_{11}a_{22}a_{33}+a_{21}a_{32}a_{13}+a_{12}a_{23}a_{31}-a_{13}a_{22}a_{31}-a_{32}a_{23}a_{11}-a_{21}a_{12}a_{33}$.

#### Diapositiva 9

- Menores y cofactores
- CAPÍTULO 02
- 9
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 10

- MENORES Y COFACTORES
- 10
- UFV.ES
- Si A es una matriz cuadrada, el menor Mij del elemento aij es el determinante de la matriz obtenida al eliminar en A la fila i y la columna j.
- El cofactor Cij de ese mismo elemento viene dado por:
- Determinante de una matriz de n x n
- COFACTOR = ADJUNTO

_Imágenes/medios en la diapositiva: 9_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $M_{21}=\begin{vmatrix}a_{12}&a_{13}\\a_{32}&a_{33}\end{vmatrix}$, $M_{22}=\begin{vmatrix}a_{11}&a_{13}\\a_{31}&a_{33}\end{vmatrix}$; $C_{ij}=(-1)^{i+j}M_{ij}$; $|A|=\sum_k a_{ik}C_{ik}$ (por la fila i) $=\sum_k a_{kj}C_{kj}$ (por la columna j).

#### Diapositiva 11

- MENORES Y COFACTORES
- 11
- UFV.ES
- Ejemplo
- Calcular:
- $𝐴=3·−11202334−2=3·4+9+0−12+12−0=3·13=39$

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $A=\begin{pmatrix}1&-2&3&0\\-1&1&0&2\\0&2&0&3\\3&4&0&-2\end{pmatrix}$; desarrollando por la 3ª columna: $|A|=3\cdot\begin{vmatrix}-1&1&2\\0&2&3\\3&4&-2\end{vmatrix}=3(4+9+0-12+12-0)=3\cdot13=39$. Captura de MATLAB: `det(A)` = 39.

#### Diapositiva 12

- MENORES Y COFACTORES
- 12
- UFV.ES
- Ejemplo
- A = [1 -2 3 0;-1 1 0 2;0 2 0 3;3 4 0 -2]
- DA = det(A)
- C11 = cofactor(1,1,A)
- C12 = cofactor(1,2,A)
- C13 = cofactor(1,3,A)
- C14 = cofactor(1,4,A)
- DCA = A(1,1)*C11 + A(1,2)*C12+ A(1,3)*C13 + A(1,4)*C14

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Código MATLAB: `A = [1 -2 3 0;-1 1 0 2;0 2 0 3;3 4 0 -2]; DA = det(A); C11 = cofactor(1,1,A); C12 = cofactor(1,2,A); C13 = cofactor(1,3,A); C14 = cofactor(1,4,A); DCA = A(1,1)*C11 + A(1,2)*C12 + A(1,3)*C13 + A(1,4)*C14`. Salida: DA = 39, C11 = 0, C12 = 0, C13 = 13, C14 = 0, DCA = 39.

#### Diapositiva 13

- MENORES Y COFACTORES
- UFV.ES
- Matriz triangular
- El determinante de una matriz triangular es igual al producto de sus componentes en la diagonal.
- $𝐴=𝑖=1𝑛𝑎𝑖𝑖$

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $|A|=\prod_{i=1}^n a_{ii}$; desarrollo por la primera columna de una triangular superior: sólo sobrevive $a_{11}$ por el menor triangular (los demás menores tienen una columna de ceros).

#### Diapositiva 14

- MENORES Y COFACTORES
- UFV.ES
- Matriz triangular
- Cálculo mediante operaciones elementales
- Sean A y B dos matrices cuadradas.
- Si B se obtiene intercambiando dos filas (columnas) de A
- |B| = -|A|
- Si B se obtiene sumando un múltiplo de una fila (columna) de A a otra fila de A,
- |B| = |A|
- Si B se obtiene multiplicando una fila (columna) de A por una constante c ≠ 0,
- |B| = c·|A|
- Estas tres propiedades nos permiten calcular determinantes efectuando operaciones elementales por filas hasta obtener una matriz triangular equivalente

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Fórmulas: intercambio de filas ⇒ $|B|=-|A|$; sumar múltiplo de otra fila ⇒ $|B|=|A|$; multiplicar fila por c ⇒ $|B|=c|A|$.

#### Diapositiva 15

- MENORES Y COFACTORES
- UFV.ES
- Matriz triangular
- Cálculo mediante operaciones elementales
- A = [2 -3 10;1 2 -2;0 1 -3]
- A0 = A;
- % Intercambiar las dos primeras filas
- A([1 2],:) = A([2 1],:);
- A(1,:) = -A(1,:)
- % Sumar 2 veces la primera fila a la segunda
- A(2,:) = A(2,:) + 2*A(1,:)
- % Sumar a la tercera fila la segunda multiplicada por 1/7
- A(3,:) = A(3,:) + (1/7)*A(2,:)
- Como es una matriz diagonal, multiplicamos los elementos de la misma
- dA = prod(diag(A))
- DA = det(A0)

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** MATLAB: `A = [2 -3 10;1 2 -2;0 1 -3]; A0 = A;` intercambiar filas 1 y 2 y cambiar signo (`A([1 2],:) = A([2 1],:); A(1,:) = -A(1,:)`); `A(2,:) = A(2,:) + 2*A(1,:)`; `A(3,:) = A(3,:) + (1/7)*A(2,:)`; resultado triangular $\begin{pmatrix}-1&-2&2\\0&-7&14\\0&0&-1\end{pmatrix}$; `dA = prod(diag(A))` = −7, `DA = det(A0)` = −7.

#### Diapositiva 16

- PROPIEDADES DE LOS DETERMINANTES
- CAPÍTULO 03
- 16
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 17

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- Condiciones que producen determinante cero
- Si A es una matriz cuadrada y cumple cualquiera de las condiciones siguientes, entonces |A|= 0.
- Hay una fila (o columna) completa de ceros
- Dos filas (o columnas) son iguales
- Una fila (o columna) es múltiplo de otra fila (o columna)
- Una fila (o columna) es combinación lineal de otras

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 18

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- El determinante de una matriz A es igual al determinante de su traspuesta
- $𝐴=𝐴𝑡$
- Si los elementos de una fila o de una columna se multiplican todos por un número, el determinante queda multiplicado por dicho número
- Si los elementos de una línea se pueden descomponer en suma de dos o más sumandos, el determinante será igual a la suma de dos determinantes (o más) que tienen todas las restantes líneas iguales y en dicha línea tienen los primeros, segundos, etc. sumandos.
- Si en un determinante los elemento de una línea son nulos, el determinante es nulo
- Si en una matriz se permutan dos filas (o dos columnas), el determinante cambia de signo

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Fórmulas ilustrativas: $|A|=|A^t|$; $\begin{vmatrix}ka_{11}&a_{12}&a_{13}\\ka_{21}&a_{22}&a_{23}\\ka_{31}&a_{32}&a_{33}\end{vmatrix}=k|A|$; descomposición de una columna suma en dos determinantes; fila de ceros ⇒ 0; permutar dos columnas cambia el signo.

#### Diapositiva 19

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- Si un determinante tiene dos líneas paralelas iguales, el determinante es nulo
- Si una matriz cuadrada tiene dos filas o dos columnas proporcionales, su determinante es nulo
- Si los elementos de una línea son combinación lineal de las restantes líneas paralelas, el determinante es nulo
- Si a los elementos de una línea se le suma una combinación lineal de las restantes líneas paralelas, el determinante no varía
- El determinante del producto de dos matrices cuadradas es igual al producto de los determi-nantes de las matrices

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Fórmulas: columnas iguales ⇒ 0; columnas proporcionales ($k\cdot$) ⇒ 0; columna combinación lineal ($r\cdot a_{i1}+s\cdot a_{i2}$) ⇒ 0; sumar a una columna una combinación lineal de otras no cambia el determinante; $|AB|=|A||B|$.

#### Diapositiva 20

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- |A·B| = |A|·|B|
- |A+B| |A|+|B|
- |A|=|L·U|=|L|·|U|=prod[diag(U)]
- |cA|= cn|A|
- A es invertible  |A| 0
- A es invertible  |A-1| = 1/|A|
- |A| = |AT|

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 21

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- Si A es cuadrada n x n estas afirmaciones son equivalentes:
- A es invertible
- Ax = B tiene solución única para toda matriz B de tamaño n x 1
- Ax = 0 tiene solo la solución trivial
- A es equivalente por filas a In
- A se puede escribir como producto de matrices elementales
- |A| ≠ 0
- ¿y si no es cuadrada n x n?

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Bocadillo con un personaje y signo de interrogación: '¿y si no es cuadrada n×n?'. La lista completa: A invertible ⇔ Ax=B tiene solución única ∀B ⇔ Ax=0 sólo trivial ⇔ A equivalente por filas a $I_n$ ⇔ A se puede escribir como producto de matrices elementales ⇔ $|A|\neq0$.

#### Diapositiva 22

- PROPIEDADES DE LOS DETERMINANTES
- UFV.ES
- Si cualquier fila o columna de $𝐴$ es un vector cero, entonces $|A|= 0$.
- Si la fila i o columna $𝑗$ de $𝐴$ se multiplica por un escalar $𝑐$, entonces $|A|$ se multiplica por $𝑐$.
- Si $𝐴, 𝐵$ y $𝐶$ son idénticas excepto por la columna $𝑗$ y que la columna $𝑗$ de $𝐶$ es la suma de las j-ésimas columnas de $𝐴$ y $𝐵$. Entonces, $  |C|=|A|+|B|$. La misma afirmación es cierta para filas.
- El intercambio de cualesquiera dos filas (o columnas) distintos de $𝐴$ tiene el efecto de multiplicar el determinante de $𝐴$ por $−1$.
- Si una matriz cuadrada $𝐴$ tiene dos filas (o columnas) iguales, entonces su determinante es cero.
- Si una fila (columna) de $𝐴$ es un múltiplo escalar de otra fila (columna), entonces $|A|= 0$.
- Si se suma un múltiplo escalar de una fila (columna) de $𝐴$ a otra fila (columna) de $𝐴$, entonces el determinante no cambia.

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 23

- “El gran libro de la naturaleza está escrito en símbolos matemáticos.”
- GALILEO GALILEI
- astrónomo, ingeniero, matemático y físico italiano (1564 – 1642)
- QUOTE

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Cita sobre fondo azul con retrato de Galileo Galilei.

#### Diapositiva 24

- DETERMINANTES
- 91 351 03 03
- INFO@UFV.ESUFV.ES
- CTRA. POZUELO-MAJADAHONDA
- KM 1.800, 28223 POZUELO DE ALARCÓN
- MADRID. ES

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Contraportada UFV 'Determinantes'.


## Pizarra Grupo A · Tema 1 Sistemas de ecuaciones

*Fuente: `GRUPO A/TEMA 1 - Sistemas de Ecuaciones/MPI1 - Tema 1 - Sistemas de ecuaciones - PIZARRA.pdf`*

#### Bloque 1 · Sistemas de m ecuaciones lineales con n incógnitas
(Por simplificar se trabaja con m = 3, n = 3.)

$$\begin{cases}a_{11}x_1+a_{12}x_2+a_{13}x_3=b_1\\a_{21}x_1+a_{22}x_2+a_{23}x_3=b_2\\a_{31}x_1+a_{32}x_2+a_{33}x_3=b_3\end{cases}$$

Clasificación:
- **Compatible** (o consistente): tiene solución.
  - **Determinado**: solución única.
  - **Indeterminado**: infinitas soluciones.
- **Incompatible** (o inconsistente): no tiene solución.

##### Obtención de sistemas equivalentes
Las siguientes **operaciones elementales** se pueden aplicar a un sistema obteniendo un sistema equivalente (el que tiene la misma solución):
- Multiplicar (o dividir) una ecuación por un número real distinto de 0: $e_i=c\cdot e_i,\ c\neq0$.
- Sumar a una ecuación una combinación lineal de otras (o un múltiplo de otra): $e_i=e_i+c\,e_j+d\,e_k+\dots$
- Intercambiar dos ecuaciones.

##### Método de eliminación de Gauss-Jordan (ejemplo)
$$\begin{cases}2x_1+4x_2+6x_3=18\\4x_1+5x_2+6x_3=24\\3x_1+x_2-2x_3=4\end{cases}$$
- $e_1\to e_1/2$: $x_1+2x_2+3x_3=9$ (pivote $x_1$).
- $e_2\to e_2-4e_1$, $e_3\to e_3-3e_1$: $-3x_2-6x_3=-12$, $-5x_2-11x_3=-23$.
- $e_2\to e_2/(-3)$: $x_2+2x_3=4$.
- $e_3\to e_3+5e_2$: $-x_3=-3$; $e_3\to e_3\cdot(-1)$: $x_3=3$.
- *Si aquí paramos y vamos despejando cada $x_i$ y sustituyendo hacia arriba, el método se llama **eliminación gaussiana**. Pero se pueden dar un par de pasos más y dejar el sistema completamente despejado (eso es hacer la **reducción de Gauss-Jordan**).*
- $e_2\to e_2-2e_3$: $x_2=-2$; $e_1\to e_1-2e_2-3e_3$: $x_1=4$.
- Resultado: $x_1=4,\ x_2=-2,\ x_3=3$ → **sistema compatible determinado**.

#### Bloque 2 · Matriz de coeficientes y matriz ampliada
El sistema equivale a $A\cdot X=b$, con $A=(a_{ij})$ la **matriz de coeficientes**, $X=(x_1,x_2,x_3)^T$ y $b=(b_1,b_2,b_3)^T$. La **matriz ampliada** es $A^+=(A\,|\,b)$.

**Reducción por filas** (recuadro): a $A^+$ se le pueden aplicar las mismas operaciones elementales (por filas) que se explicaron para sistemas de ecuaciones: $f_i\to c\,f_i$; $f_i\to f_i+c\,f_j+d\,f_k+\dots$; $f_i\leftrightarrow f_j$. Al aplicar operaciones elementales, las matrices ampliadas que obtenemos son equivalentes, es decir, representan sistemas con la misma solución.

Ejemplos (□ = pivote):
1. $\left(\begin{smallmatrix}2&4&6&|&18\\4&5&6&|&24\\3&1&-2&|&4\end{smallmatrix}\right)\to\dots\to$ **forma escalonada** $\left(\begin{smallmatrix}1&2&3&|&9\\0&1&2&|&4\\0&0&1&|&3\end{smallmatrix}\right)\to\dots\to$ **forma escalonada reducida** $\left(\begin{smallmatrix}1&0&0&|&4\\0&1&0&|&-2\\0&0&1&|&3\end{smallmatrix}\right)$ → sistema compatible determinado, $x_1=4,\ x_2=-2,\ x_3=3$. *Nota: para ser escalonada reducida, los pivotes deben ser el único elemento no nulo de sus respectivas columnas.*
2. $\begin{cases}2x_1+4x_2+6x_3=18\\4x_1+5x_2+6x_3=24\\2x_1+7x_2+12x_3=30\end{cases}\to\dots\to\left(\begin{smallmatrix}1&0&-1&|&1\\0&1&2&|&4\\0&0&0&|&0\end{smallmatrix}\right)$ → **sistema compatible indeterminado**: $x_1=1+x_3$, $x_2=4-2x_3$, $x_3$ parámetro.
3. $\begin{cases}2x_2+3x_3=4\\2x_1-6x_2+7x_3=15\\x_1-2x_2+5x_3=10\end{cases}\to\dots\to\left(\begin{smallmatrix}1&0&8&|&15\\0&1&3/2&|&5/2\\0&0&0&|&-1\end{smallmatrix}\right)$ → **sistema incompatible**.

#### Bloque 3 · Solución matricial y sistemas homogéneos
**Solución matricial:** $A\cdot X=b\ \overset{\text{SCD}}{\Rightarrow}\ X=A^{-1}\cdot b$ (¡matriz inversa! ¡producto de matrices!). *En Matlab: `X = A\b`.*

**Sistemas homogéneos** ($b=0$, $A^+=(A\,|\,0)$):
- Siempre admiten la "solución trivial" $x_1=x_2=x_3=0$.
- No pueden ser incompatibles.
- Sólo pueden ser compatible determinado (con solución trivial) o compatible indeterminado (infinitas soluciones).

Ejemplos:
- $\begin{cases}2x_1+4x_2+6x_3=0\\4x_1+5x_2+6x_3=0\\3x_1+x_2-2x_3=0\end{cases}\to\dots\to I$ → SCD, solución trivial.
- $\begin{cases}x_1+2x_2-x_3=0\\3x_1-3x_2+2x_3=0\\-x_1-11x_2+6x_3=0\end{cases}\to\dots\to\left(\begin{smallmatrix}1&0&-1/9&|&0\\0&1&-5/9&|&0\\0&0&0&|&0\end{smallmatrix}\right)$ → SCI, infinitas soluciones: $x_3=\alpha,\ x_2=\tfrac59\alpha,\ x_1=\tfrac19\alpha$.
- Un sistema homogéneo con más incógnitas que ecuaciones l.i. tiene siempre infinitas soluciones. (Si el sistema es NO homogéneo no tiene por qué ser así: si hay más incógnitas que ecuaciones l.i., el sistema no homogéneo podrá ser o bien incompatible o bien S.C.I. con infinitas soluciones.)

Recuadro "Representación matricial de un sistema homogéneo": $A\cdot X=0$.

#### Bloque 4 · Relación entre sistemas homogéneos y no homogéneos
Sea un sistema no homogéneo $A X=b$ y su sistema homogéneo asociado $AX=0$. **Teorema:** si $X_{p1}$ y $X_{p2}$ son soluciones de $AX=b$, entonces $X_{p1}-X_{p2}$ es solución de $AX=0$.
*Demostración:* $A(X_{p1}-X_{p2})=AX_{p1}-AX_{p2}=b-b=0$.

**Corolario:** si $x$ es solución particular de $AX=b$ e $y$ es otra, existe $h$ solución de $AX=0$ tal que $y=x+h$. Es decir, para encontrar las soluciones de un sistema no homogéneo basta encontrar UNA solución (solución particular, $X_p$) y todas las soluciones del sistema homogéneo asociado (solución homogénea, $X_h$), y sumarlas.

**Ejemplo:** $\begin{cases}x_1+2x_2-x_3=2\\2x_1+3x_2+5x_3=6\\-x_1-3x_2+8x_3=0\end{cases}$ → $\left(\begin{smallmatrix}1&0&13&|&6\\0&-1&7&|&2\\0&0&0&|&0\end{smallmatrix}\right)$, es decir $x_1+13x_3=6$, $-x_2+7x_3=2$ ⇒ $x_3=\alpha$, $x_2=-2+7\alpha$, $x_1=6-13\alpha$:
$$\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}=\underbrace{\begin{pmatrix}6\\-2\\0\end{pmatrix}}_{X_p}+\underbrace{\begin{pmatrix}-13\alpha\\7\alpha\\\alpha\end{pmatrix}}_{X_h}$$
$X_p=(6,-2,0)$ es una solución particular del sistema; $X_h$ resuelve el homogéneo $x_1+13x_3=0,\ -x_2+7x_3=0$.

- Toda solución del sistema $AX=b$ se puede escribir como $X=X_p+X_h$, donde $X_p$ es alguna solución particular y $X_h$ es toda solución homogénea.


## Pizarra Grupo A · Tema 2 Matrices (1/3)

*Fuente: `GRUPO A/TEMA 2 - Matrices/MPI1 - Tema 2 - Matrices - 1de3.pdf`*

#### Matrices

##### Definición de vectores
- Vector fila de n componentes: $v=(x_1,x_2,\dots,x_k,\dots,x_n)$; vector columna de n componentes: $v=(x_1,\dots,x_n)^T$. $x_k$ es la componente k-ésima.
- $\mathbb{R}^n$ es el conjunto de todos los vectores de dimensión n con n componentes reales (p. ej. $\mathbb{R}^2,\mathbb{R}^3$); $\mathbb{C}^n$ igual con componentes complejas.

##### Definición de matrices
$A=(a_{ij})$, matriz $m\times n$ (m filas, n columnas = tamaño o dimensiones). La fila i-ésima y la columna j-ésima son vectores; $a_{ij}$ es el elemento i-j-ésimo. Ejemplo: $A=\begin{pmatrix}3&2&1\\5&7&5\\1&0&0\end{pmatrix}$ (3×3), $a_{23}=5$, $a_{32}=0$.

##### Algunas matrices importantes
- Matriz fila ≡ vector fila ($A_{1\times n}$); matriz columna ≡ vector columna ($A_{n\times1}$).
- Matriz cuadrada: cuando $m=n$ ($A_{n\times n}=A_n$).
- Matriz cero o nula: $a_{ij}=0\ \forall i,j$.
- Triangular superior (ej. $\begin{pmatrix}1&3&7\\0&5&2\\0&0&4\end{pmatrix}$), triangular inferior (ej. $\begin{pmatrix}3&0&0\\4&5&0\\7&8&1\end{pmatrix}$), diagonal (ej. $\operatorname{diag}(1,2,2)$), escalar (ej. $5I$), identidad $I$.

##### Igualdad de matrices
$A=(a_{ij})_{m_1\times n_1}$, $B=(b_{ij})_{m_2\times n_2}$: $A=B\iff m_1=m_2\wedge n_1=n_2\wedge a_{ij}=b_{ij}\ \forall i,j$. "Dos matrices son iguales sii son de las mismas dimensiones y sus elementos i-j-ésimos son iguales."

##### Operaciones básicas con matrices
- **Suma** (¡obligatorio mismas dimensiones!): $A+B=(a_{ij}+b_{ij})$.
- **Multiplicación por escalar**: $\alpha\in\mathbb{R}\Rightarrow\alpha A=(\alpha a_{ij})$.
- **Teoremas y propiedades:** $A+0=A$; $0\cdot A=0$ (0 ∈ ℝ, resultado la matriz 0); $A+B=B+A$ (conmutativa); $(A+B)+C=A+(B+C)$ (asociativa); $\alpha(A+B)=\alpha A+\alpha B$ (distributiva); $1\cdot A=A$; $(\alpha+\beta)A=\alpha A+\beta A$.

##### Producto de vectores y de matrices
- **Producto escalar de vectores** (obligatorio misma dimensión): $a\cdot b=a_1b_1+a_2b_2+\dots+a_nb_n$ — ¡es un número, un "escalar"!
  Propiedades ($a,b,c\in\mathbb{R}^n$, $\alpha\in\mathbb{R}$): $a\cdot0=0$; $a\cdot b=b\cdot a$ (conmutativa); $a\cdot(b+c)=a\cdot b+a\cdot c$ (distributiva); $(\alpha a)\cdot b=\alpha(a\cdot b)$; **no** es asociativa: $(a\cdot b)\cdot c\neq a\cdot(b\cdot c)$.
- **Producto de matrices:** $A_{m\times n}\cdot B_{n\times p}=C_{m\times p}=(c_{ij})$, donde $c_{ij}=(\text{fila } i \text{ de } A)\cdot(\text{columna } j \text{ de } B)=a_{i1}b_{1j}+a_{i2}b_{2j}+\dots+a_{in}b_{nj}=\sum_{k=1}^n a_{ik}b_{kj}$.
  Propiedades: $AB\neq BA$ (no conmutativa); $(AB)C=A(BC)$ (asociativa); $A(B+C)=AB+AC$ y $(A+B)C=AC+BC$ (distributivas).
  Ejemplo: $A=\begin{pmatrix}1&2&3\\1&0&1\end{pmatrix}_{2\times3}$, $B=\begin{pmatrix}0&0&1\\2&4&6\\1&1&0\end{pmatrix}_{3\times3}$ ⇒ $C=AB=\begin{pmatrix}7&11&13\\1&1&1\end{pmatrix}_{2\times3}$ ("hacerlo en Matlab y con la Casio").

##### Inversa de una matriz cuadrada (pág. 99)
Sea $A$ cuadrada $n\times n$. Se denomina matriz inversa de $A$ a la matriz $A^{-1}$ que cumple $AA^{-1}=A^{-1}A=I$ (1ª forma de obtener la inversa: plantear este sistema; ejemplo en p. 102, 2.4.2).
- Si $A$ tiene inversa, se dice que es **invertible**; si es invertible, la inversa es única. ¡Ojo! No todas las matrices cuadradas tienen inversa. Invertible = "no singular"; no invertible = "singular".
- Recuadro matriz identidad: $I_n=(b_{ij})$ con $b_{ij}=1$ si $i=j$, 0 si $i\neq j$; $A I_n=I_nA=A$.
- Ejemplo: $A=\begin{pmatrix}2&-3\\-4&5\end{pmatrix}$, calcular $A^{-1}=\begin{pmatrix}x&y\\z&w\end{pmatrix}$ planteando $AA^{-1}=I$ y resolviendo el sistema.
- **Propiedades:** $(AB)^{-1}=B^{-1}A^{-1}$; $(A^{-1})^{-1}=A$; si $AB=I$ o $BA=I$ ⇒ $A$ invertible y $B=A^{-1}$ (ojo demostraciones en el libro).
- **Solución de sistemas en términos de la inversa:** $Ax=b\Rightarrow x=A^{-1}b$.
- **Procedimiento para encontrar la inversa:** matriz aumentada $(A\,|\,I)$; reducción por filas para poner $A$ en forma escalonada reducida; si se llega a $I$ a la izquierda, $A$ es invertible y $A^{-1}$ ha quedado a la derecha; si se llega a una fila de ceros a la izquierda, $A$ no es invertible ($\nexists A^{-1}$).
  - Ejemplo 2.4.2: $\left(\begin{smallmatrix}2&-3&|&1&0\\-4&5&|&0&1\end{smallmatrix}\right)\to\dots\to\left(\begin{smallmatrix}1&0&|&-5/2&-3/2\\0&1&|&-2&-1\end{smallmatrix}\right)$ ⇒ $A^{-1}=\begin{pmatrix}-5/2&-3/2\\-2&-1\end{pmatrix}$.
  - Ejemplo 2.4.3: $\left(\begin{smallmatrix}1&2&|&1&0\\-2&-4&|&0&1\end{smallmatrix}\right)\to\dots\to\left(\begin{smallmatrix}1&2&|&1&0\\0&0&|&2&1\end{smallmatrix}\right)$ ⇒ $\nexists A^{-1}$.
- **Teorema (equivalencias).** Sea $A$ una matriz $n\times n$:
  - $A$ invertible ⇔ $A$ equivalente por filas a la identidad (dos matrices son "equivalentes por renglones" si una se transforma en la otra mediante operaciones elementales por filas);
  - ⇔ la forma escalonada reducida por filas de $A$ es $I_n$;
  - ⇔ su forma escalonada reducida tiene n pivotes;
  - ⇔ el sistema $Ax=b$ tiene solución única para cada vector b de dimensión n;
  - ⇔ la única solución de $Ax=0$ es la trivial;
  - ⇔ la solución única de $Ax=b$ es $x=A^{-1}b$;
  - ⇔ $|A|\neq0$.
- **Ejemplo:** $2x_1+4x_2+3x_3=6,\ x_2-x_3=-4,\ 3x_1+5x_2+7x_3=7$ ⇒ $Ax=b$ con $A=\begin{pmatrix}2&4&3\\0&1&-1\\3&5&7\end{pmatrix}$, $b=(6,-4,7)^T$; $A^{-1}=\begin{pmatrix}4&-13/3&-7/3\\-1&5/3&2/3\\-1&2/3&2/3\end{pmatrix}$ y $x=A^{-1}b=(25,-8,-4)^T$.

##### Transpuesta de una matriz (pág. 123)
$A=(a_{ij})_{m\times n}\Rightarrow A^T=(a_{ji})_{n\times m}$: se obtiene intercambiando filas por columnas.
**Propiedades** (demostraciones en pág. 124): $(A^T)^T=A$; $(A+B)^T=A^T+B^T$ (si se pueden sumar); $(AB)^T=B^TA^T$; $(A^T)^{-1}=(A^{-1})^T$ (si $A$ es invertible, $A^T$ también).
**Matriz simétrica:** $A$ cuadrada es simétrica ⇔ $A=A^T$ (sus filas son iguales que sus columnas).
**Otra forma de escribir el producto escalar:** con $a,b$ vectores columna, $a\cdot b=a^T b$ (producto escalar = multiplicación de matrices).


## Pizarra Grupo A · Tema 2 Matrices (2/3)

*Fuente: `GRUPO A/TEMA 2 - Matrices/MPI1 - Tema 2 - Matrices - 2de3.pdf`*

#### Matrices elementales y matrices inversas (pág. 130)
*Recordatorio, operaciones elementales por filas:* $f_i\to c\,f_i$; $f_i\leftrightarrow f_j$; $f_i\to f_i+c\,f_j$.

Una matriz cuadrada $E$ de $n\times n$ es **elemental** si se puede obtener a partir de la identidad $I_n$ mediante UNA SOLA operación elemental por filas. Ejemplos (desde $I_3$):
- $f_2\to3f_2$: $\begin{pmatrix}1&0&0\\0&3&0\\0&0&1\end{pmatrix}\equiv 3f_2$
- $f_3\to f_3-2f_1$: $\begin{pmatrix}1&0&0\\0&1&0\\-2&0&1\end{pmatrix}\equiv f_3-2f_1$
- $f_2\leftrightarrow f_3$: $\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}\equiv P_{23}$

##### Operaciones elementales por filas mediante multiplicación por matrices elementales
Para realizar una operación elemental por filas en $A$ se multiplica $A$ **por la izquierda** por la matriz elemental adecuada (ver cuadro resumen en pág. 132). Con $A=\begin{pmatrix}1&1&2&1\\4&2&3&-5\\3&1&-2&4\end{pmatrix}$:
- $f_2\to3f_2$ (matriz elemental multiplicación): $(3f_2)\cdot A=\begin{pmatrix}1&1&2&1\\12&6&9&-15\\3&1&-2&4\end{pmatrix}$
- $f_3\to f_3-2f_1$ (matriz elemental suma): $(f_3-2f_1)\cdot A=\begin{pmatrix}1&1&2&1\\4&2&3&-5\\1&-1&-6&2\end{pmatrix}$
- $f_2\leftrightarrow f_3$ (matriz elemental permutación): $P_{23}\cdot A=\begin{pmatrix}1&1&2&1\\3&1&-2&4\\4&2&3&-5\end{pmatrix}$

##### Matrices elementales y matrices inversas
- $(c\,f_i)^{-1}=\frac1c f_i$; $(f_i+c\,f_j)^{-1}=f_i-c\,f_j$; $(P_{ij})^{-1}=P_{ij}$ (la inversa es la matriz que deshace el cambio).

**Teoremas:**
- Toda matriz elemental es invertible.
- La inversa de una matriz elemental es otra matriz elemental del mismo tipo que representa la operación contraria.
- Una matriz cuadrada es invertible sii es el producto de matrices elementales (esas matrices existen por el teorema anterior): $E_m\cdots E_3E_2E_1A=I\Rightarrow A=E_1^{-1}E_2^{-1}E_3^{-1}\cdots E_m^{-1}$, y $E_m\cdots E_1=A^{-1}$ (las matrices con las transformaciones elementales que convierten $A$ en $I$).

**Teorema de equivalencias** (A de $n\times n$): A invertible ⇔ A equivalente por filas a la identidad ⇔ su forma escalonada reducida es $I_n$ ⇔ tiene n pivotes ⇔ $Ax=b$ tiene solución única para cada b ⇔ la única solución de $Ax=0$ es la trivial ⇔ la solución única de $Ax=b$ es $x=A^{-1}b$ ⇔ $|A|\neq0$. (Dos matrices son "equivalentes por renglones" si una se transforma en la otra mediante operaciones elementales por filas.)

##### Ejemplo: demostrar que $A=\begin{pmatrix}2&4&6\\4&5&6\\3&1&-2\end{pmatrix}$ es invertible y escribirla como producto de matrices elementales
Operaciones: $f_1\to\frac12f_1$; $f_2\to f_2-4f_1$; $f_3\to f_3-3f_1$; $f_2\to-\frac13f_2$; $f_1\to f_1-2f_2$; $f_3\to f_3+5f_2$; $f_3\to-f_3$; $f_1\to f_1+f_3$; $f_2\to f_2-2f_3$, hasta llegar a $I$.
$$\underbrace{\begin{pmatrix}1&0&0\\0&1&-2\\0&0&1\end{pmatrix}\cdots\begin{pmatrix}1&0&0\\-4&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1/2&0&0\\0&1&0\\0&0&1\end{pmatrix}}_{A^{-1}}A=I$$
$$A=\begin{pmatrix}1/2&0&0\\0&1&0\\0&0&1\end{pmatrix}^{-1}\begin{pmatrix}1&0&0\\-4&1&0\\0&0&1\end{pmatrix}^{-1}\cdots\begin{pmatrix}1&0&0\\0&1&-2\\0&0&1\end{pmatrix}^{-1}=\begin{pmatrix}2&0&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\4&1&0\\0&0&1\end{pmatrix}\cdots\begin{pmatrix}1&0&0\\0&1&2\\0&0&1\end{pmatrix}$$

##### Matrices triangulares y factorización en elementales × triangular
- **Matriz triangular superior:** todas las componentes por debajo de la diagonal son 0. **Inferior:** todas las de encima son 0.
- Una matriz cuadrada siempre se puede poner como producto de matrices elementales (a la izquierda) y una matriz triangular superior (a la derecha), incluso no siendo invertible. ¡Claro! La eliminación gaussiana convierte cualquier matriz en triangular superior.

Ejemplo: $A=\begin{pmatrix}3&6&9\\2&5&1\\1&1&8\end{pmatrix}\xrightarrow{f_1\to\frac13f_1}\begin{pmatrix}1&2&3\\2&5&1\\1&1&8\end{pmatrix}\xrightarrow{f_2\to f_2-2f_1,\ f_3\to f_3-f_1}\begin{pmatrix}1&2&3\\0&1&-5\\0&-1&5\end{pmatrix}\xrightarrow{f_3\to f_3+f_2}\begin{pmatrix}1&2&3\\0&1&-5\\0&0&0\end{pmatrix}=U$
$$\begin{pmatrix}1&0&0\\0&1&0\\0&1&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\-1&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\-2&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1/3&0&0\\0&1&0\\0&0&1\end{pmatrix}A=U$$
$$A=\begin{pmatrix}3&0&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\2&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\1&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\0&-1&1\end{pmatrix}\begin{pmatrix}1&2&3\\0&1&-5\\0&0&0\end{pmatrix}$$


## Pizarra Grupo A · Tema 2 Matrices (3/3)

*Fuente: `GRUPO A/TEMA 2 - Matrices/MPI1 - Tema 2 - Matrices - 3de3.pdf`*

#### Forma escalonada por filas
(Matriz triangular superior con 1's y 0's en la diagonal principal.) Ejemplos de patrones 3×3 escalonados: $\begin{pmatrix}1&x&x\\0&1&x\\0&0&1\end{pmatrix}$, $\begin{pmatrix}1&x&x\\0&1&x\\0&0&0\end{pmatrix}$, $\begin{pmatrix}1&x&x\\0&0&1\\0&0&0\end{pmatrix}$, $\begin{pmatrix}1&x&x\\0&0&0\\0&0&0\end{pmatrix}$, $\begin{pmatrix}0&1&x\\0&0&1\\0&0&0\end{pmatrix}$, $\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$, $\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}$.

#### Factorización LU
$A=L\cdot U$, con $L$ triangular inferior (aquí sí buscamos 1's en la diagonal) y $U$ triangular superior (no buscamos 1's en la diagonal principal).

**Ejemplo (2.7.1 del libro):**
$$A=\begin{pmatrix}2&3&2&4\\4&10&-4&0\\-3&-2&-5&-2\\-2&4&4&-7\end{pmatrix}=\begin{pmatrix}1&0&0&0\\2&1&0&0\\-\frac32&\frac58&1&0\\-1&\frac74&\frac{20}3&1\end{pmatrix}\begin{pmatrix}2&3&2&4\\0&4&-8&-8\\0&0&3&9\\0&0&0&-49\end{pmatrix}$$
Pasos: $R_2\to R_2-2R_1$, $R_3\to R_3+\tfrac32R_1$, $R_4\to R_4+R_1$ ⇒ $\begin{pmatrix}2&3&2&4\\0&4&-8&-8\\0&\frac52&-2&4\\0&7&6&-3\end{pmatrix}$; $R_3\to R_3-\tfrac58R_2$, $R_4\to R_4-\tfrac74R_2$ ⇒ $\begin{pmatrix}2&3&2&4\\0&4&-8&-8\\0&0&3&9\\0&0&20&11\end{pmatrix}$; $R_4\to R_4-\tfrac{20}3R_3$ ⇒ $U$.
En forma matricial, el producto de las matrices elementales (de la última a la primera: $R_4-\tfrac{20}3R_3$, $R_4-\tfrac74R_2$, $R_3-\tfrac58R_2$, $R_4+R_1$, $R_3+\tfrac32R_1$, $R_2-2R_1$) por $A$ da $U$. Despejando, $A$ es el producto de sus inversas (elementales con los multiplicadores cambiados de signo) por $U$; ese producto de inversas es $L$, cuyos elementos bajo la diagonal son precisamente los multiplicadores: $L=\begin{pmatrix}1&0&0&0\\2&1&0&0\\-\frac32&\frac58&1&0\\-1&\frac74&\frac{20}3&1\end{pmatrix}$.

**Teorema 2.7.2 (factorización LU)** (recorte del libro, parafraseado): si una matriz cuadrada $A$ se puede reducir por renglones a una triangular $U$ sin permutar renglones, existe una triangular inferior $L$ invertible con unos en la diagonal tal que $A=LU$; si además $U$ tiene n pivotes ($A$ invertible), la factorización es única.

#### Uso de la factorización LU para resolver sistemas de ecuaciones
$Ax=b\Rightarrow LUx=b\Rightarrow L(Ux)=b$. Llamando $y=Ux$:
1. Resuelvo el sistema $Ly=b$ — ¡es inmediato! (sustitución hacia delante).
2. Resuelvo el sistema $Ux=y$ — ¡también es inmediato! (sustitución hacia atrás).

**Ejemplo 2.7.2:** resolver $Ax=b$ con la $A$ anterior y $b=(4,-8,-4,-1)^T$.
1. $Ly=b$: $y_1=4$; $2y_1+y_2=-8\Rightarrow y_2=-16$; $-\tfrac32y_1+\tfrac58y_2+y_3=-4\Rightarrow y_3=12$; $-y_1+\tfrac74y_2+\tfrac{20}3y_3+y_4=-1\Rightarrow y_4=-49$.
2. $Ux=y$: $2x_1+3x_2+2x_3+4x_4=4$; $4x_2-8x_3-8x_4=-16$; $3x_3+9x_4=12$; $-49x_4=-49$ ⇒ $x_4=1$, $x_3=1$, $x_2=0$, $x_1=-1$.

Solución: $x=(-1,0,1,1)^T$.


## Pizarra Grupo A · Tema 3 Determinantes

*Fuente: `GRUPO A/TEMA 3 - Determinantes/MPI1 - Tema 3 - Determinantes - PIZARRA.pdf`*

#### Determinantes

##### Regla de Sarrus
- 2×2: $|A|=a_{11}a_{22}-a_{21}a_{12}$.
- 3×3: $|A|=a_{11}a_{22}a_{33}+a_{23}a_{12}a_{31}+a_{21}a_{32}a_{13}-(a_{13}a_{22}a_{31}+a_{21}a_{12}a_{33}+a_{23}a_{32}a_{11})$.

##### Desarrollo de un determinante por cofactores (o adjuntos)
- **Menor:** $A_{n\times n}\Rightarrow M_{ij}$ = matriz resultante de eliminar la fila i y la columna j.
- **Cofactor** (o adjunto): $A_{ij}=(-1)^{i+j}|M_{ij}|$, con $(-1)^{i+j}=1$ si $i+j$ par, $-1$ si impar (patrón de signos $\begin{smallmatrix}+&-&+\\-&+&-\\+&-&+\end{smallmatrix}$).
- **Expansión por cofactores** ("desarrollo de un determinante por adjuntos"): fijada cualquier fila i-ésima, $|A|=\sum_{k=1}^n a_{ik}A_{ik}$; fijada cualquier columna j-ésima, $|A|=\sum_{k=1}^n a_{kj}A_{kj}$.
- Ejemplo (nube): con $A=\begin{pmatrix}1&0&2\\3&5&7\\1&1&1\end{pmatrix}$ se puede desarrollar por la fila 1 o por la columna 2 (donde hay un 0); p. ej. $M_{22}=\begin{pmatrix}1&2\\1&1\end{pmatrix}$, $A_{22}=(-1)^{2+2}|M_{22}|=-1$.
- **Determinante de matrices triangulares (sup. o inf.) y diagonales:** $|A|=\prod_{k=1}^n a_{kk}=a_{11}a_{22}\cdots a_{nn}$ (producto de los números de la diagonal principal).

##### Propiedades de los determinantes
- $|AB|=|A|\,|B|$; en general $|A+B|\neq|A|+|B|$.
- Si $A=LU$ (factorización LU, $L$ con 1's en la diagonal ⇒ $|L|=1$) ⇒ $|A|=|U|$ = producto de los elementos de la diagonal de $U$.
- $|A|=|A^T|$.
- Si hay alguna fila o columna de ceros ⇒ $|A|=0$.
- Si una fila o columna se multiplica por $c$ ⇒ $|A|$ se multiplica por $c$.
- Si $A$ y $B$ sólo difieren en la columna j, y $C$ tiene como columna j la suma de ambas ($a_{ij}+b_{ij}$), entonces $|C|=|A|+|B|$.
- Si intercambiamos dos filas o columnas ⇒ $|A|$ se multiplica por $-1$.
- Si $A$ tiene dos filas o columnas iguales ⇒ $|A|=0$.
- Si una fila o columna es múltiplo de otra ⇒ $|A|=0$.
- Si sumamos a una fila o columna un múltiplo de otra ⇒ $|A|$ no cambia.
- Ejercicio de cálculo de determinante triangularizando una matriz: Ejemplo 3.2.14 (pág. 195); también el ejemplo de la página siguiente.

##### Determinantes e inversas
- $A$ invertible ⇔ $|A|\neq0$.
- $|A^{-1}|=\dfrac1{|A|}$.
- **Matriz adjunta:** $\operatorname{adj}A=(A_{ij})$, matriz formada por todos los adjuntos de $A$ (¡ojo, el libro la define diferente!).
- $A\cdot(\operatorname{adj}A)=|A|\cdot I$ (multiplicar una matriz por su adjunta da la matriz diagonal con $|A|$ en la diagonal). *(Con la definición de la pizarra, esto vale para la adjunta traspuesta.)*
- $A^{-1}=\dfrac1{|A|}\operatorname{adj}(A^T)$.

##### Determinantes y matrices elementales
- $E=P_{ij}\Rightarrow|E|=-1$.
- $E=(f_i+c\,f_j)\Rightarrow|E|=1$.
- $E=(c\,f_i)\Rightarrow|E|=c$.
Todas se entienden sabiendo que $|I|=1$ y cómo afectan al determinante las transformaciones elementales.


## Live Script: problema inicial de matrices y SEL

*Fuente: `unfiled/MATRICES_Y_SLE_ProblemaInicial_R00.mlx`*

###  [Imagen: Logotipo UFV Madrid.]

Prof J.M. Medina

### MATRICES Y SISTEMAS DE ECUACIONES LINEALES

- Contenido

- PROBLEMA 1  ·     Solución

#### PROBLEMA 1

Una empresa fabrica tres productos: A, B y C. Para producirlos, utiliza tres tipos de recursos: mano de obra, maquinaria y materiales. Cada producto requiere una cantidad específica de cada recurso, y la empresa tiene una disponibilidad limitada de estos.

[Imagen: Tabla de recursos: Mano de obra — Producto A 2 h, B 3 h, C 2 h, disponibilidad 240 h; Maquinaria — 1 h, 2 h, 1 h, 150 h; Materiales — 3 kg, 2 kg, 4 kg, 300 kg.]

La empresa quiere saber cuántas unidades de cada producto puede fabricar sin exceder los recursos disponibles. Discutir los resultados.

Solución

```matlab

```

**Salida:**
```text
R =
2  3  2
1  2  1
3  2  4
Q = ([A; B; C])
RD =
SEL = ([2⁢A+3⁢B+2⁢C=240; A+2⁢B+C=150; 3⁢A+2⁢B+4⁢C=300])
X =
-60.0000
60.0000
90.0000
res = ([A=-60; B=60; C=90])
SEL = ([2⁢A+3⁢B+2⁢C≤240; A+2⁢B+C≤150; 3⁢A+2⁢B+4⁢C≤300])
ans = struct with fields:
A: x - 2*u - v
B: u
C: v
parameters: [u  v  x]
conditions: (3*B)/2 + C < x - B/2 & x - B/2 <= (5*B)/6 - C/3 + 100 & 0 < u & 0 < v & x <= 150 & x - B/2 <= 120
f =
-1  -1  -1
cond =
0  0  0
Optimal solution found.
X =
fval =
-108
exitflag =
```

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Guion: ejercicios de matrices con MATLAB

*Fuente: `Ejercicios de Matrices.pdf`*

#### Página 1

```text
EJERCICIOS DE MATRICES CON MATLAB.
MANIPULACIÓN DE MATRICES EN MATLAB. Realice en Matlab los siguientes ejemplos.

Contenido

Introducción
Entrada de matrices
Manipular elementos
Operaciones con matrices
Suma
Resta
Multiplicación
División
Operador "."
Operaciones elementales de filas

Introducción

En el presente documento vamos a ver las principales formas de manejar matrices en MATLAB.

Entrada de matrices

Podemos crear matrices especiales o introducir una matriz concreta. Para esto último se utilizan los corchetes: "[ ]", las
comas "," para separar los elementos (también se pueden separar con un espacio) y el punto y como ";" para separar filas.

A = [1 2 3;4 5 6]

B = [1,2,3;4,5,6]

Matrices especiales:

C = ones(3)

D = ones(3,2)

E = ones(2,3)

F = zeros(3)

G = zeros(3,4)

Un caso especial es la matriz unidad:

H = eye(3)

Podemos necesitar una matriz rectangular con unos en la "diagonal":

I = eye(4,7)

Manipular elementos

Generamos una matriz aleatoria y extraemos elementos o submatrices:

J = rand(5,7)

J1 = J(3,7)

Obsérvese que en este caso hemos utilizado paréntesis.

J2 = J(1:2,6:7)

J21 = [J(1,1), J(2,3); J(5,1), J(5,7)]

Hemos empleado el operador ":", que sirve para introducir vectores, entre otras cosas:

V1 = [1:7]

V2 = [1:2:7]

Vamos a ver dos formas de obtener las tres primeras columnas de J:

J3 = J(:,1:3)

```

#### Página 2

```text
J4 = J;

J4(:,4:end) = []

Eliminamos la fila 3:

J5 = J;

J5(3,:) = []

Eliminamos la columna 5:

J6 = J;

J6(:,5) = []

Añadimos una columna al final

J7 = J6;

J7(:,end+1) = [1;2;3;4;5]

¿Y si la hubiéramos querido añadir en la columna 4?

J8 = J6;

J8(:,5:end+1) = J8(:,4:end)

J8(:,4) = [1;2;3;4;5]

Operaciones con matrices

Suma

A = [1,2,3,4;5,6,7,8]

B = [1 3 5 7;2 4 6 8]

C=A+B

Resta

D=A-C

Multiplicación

Recordemos que no todas las matrices se pueden multiplicar

try

E = A*B

catch ME

disp('A y B no se pueden multiplicar')

end

try

E = A*B'

catch ME

disp('A y B no se pueden multiplicar')

end

División

¿Cómo podemos dividir A por B?

NO EXISTE DIVISIÓN DE MATRICES. Lo más parecido que podemos hacer es multiplicar por la inverse, si existe.

A = magic(3)

```

#### Página 3

```text
B = rand(3)

A*inv(B)

A/B

A\B

inv(A)*B

Operador "."

Multiplicando elemento por elemento.

A = [1,2,3,4;5,6,7,8]

B = [1 3 5 7;2 4 6 8]

A.*B

Operaciones elementales de filas

Son fundamentales para emplear métodos como el de Gauss:

Usamos la matriz J.

Hacemos un "1" en J(1,1):

JG1 = J;

JG1(1,:) = JG1(1,:)/JG1(1,1)

JG1(2,:) = JG1(2,:) - JG1(1,:)*JG1(2,1)

JG1(3,:) = JG1(3,:) - JG1(1,:)*JG1(3,1)

JG1(4,:) = JG1(4,:) - JG1(1,:)*JG1(4,1)

JG1(5,:) = JG1(5,:) - JG1(1,:)*JG1(5,1)

JG1(2,:) = JG1(2,:)/JG1(2,2)

JG1(3,:) = JG1(3,:) - JG1(2,:)*JG1(3,2)

JG1(4,:) = JG1(4,:) - JG1(2,:)*JG1(4,2)

```
