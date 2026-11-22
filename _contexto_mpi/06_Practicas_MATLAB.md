# Prácticas de MATLAB

Cuaderno común de prácticas (aplicaciones del álgebra), chuleta de funciones, prácticas evaluables del Grupo B (modelos A/B y soluciones) y el capítulo de Markov del libro.

**Contenido de este archivo:**
- Chuleta: funciones de álgebra en MATLAB (idéntica a la copia de GRUPO B/PRACTICAS)
- Cuaderno de prácticas común (recursos, calor, interpolación, redes, grafos, Leontief, Markov, PageRank)
- Práctica 1 · Modelo A (enunciado)
- Práctica 1 · Modelo A (resuelta)
- Práctica 1 · Modelo B (enunciado)
- Práctica 1 · Modelo B (resuelta)
- Práctica 2 · Modelo A
- Práctica 2 · Modelo B
- Práctica 3 · Modelo A
- Práctica 3 · Modelo B
- Libro Grossman · Capítulo 9: Cadenas de Markov y teoría de juegos


## Chuleta: funciones de álgebra en MATLAB (idéntica a la copia de GRUPO B/PRACTICAS)

*Fuente: `COMUN A TODOS LOS GRUPOS/Funciones_Algebra_Matlab.pdf`*

#### Página 1

```text
PRÁCTICAS ÁLGEBRA

Table of Contents
INTRODUCCIÓN................................................................................................................................................ 1
1 SISTEMAS LINEALES.....................................................................................................................................1
1.1 Sistemas con solución única (comando \ )................................................................................................1
Cómo dar los resultados con fprintf.............................................................................................................1
Cómo comprobar que el resultado es correcto (norm)................................................................................2
1.2 Sistemas lineales con infinitas soluciones (rref)....................................................................................... 2
La función null............................................................................................................................................. 3
2 Representación gráfica de funciones anónimas vectorizadas (y=@(x)) con plot............................................ 3
3 Polinomios (polyval, roots, polyfit)....................................................................................................................4
4 Autovalores y autovectores (eig, poly, polyvalm).............................................................................................5
5 Grafos (graph, digraph, sparse, full, shortestpath, highlight)........................................................................... 7
5.1 Dibujar un grafo a partir de la matriz de adyacencia.................................................................................7
5.2 Dibujar un grafo dirigido o dígrafo a partir de la matriz de adyacencia.....................................................7
5. 3 Camino más corto, grafos ponderados y matriz de adyacencia.............................................................. 8
RESUMEN DE FUNCIONES............................................................................................................................ 11

INTRODUCCIÓN
El presente documento describe las funciones de Matlab que deben emplearse para la resolución de
problemas de Álgebra Lineal

1 SISTEMAS LINEALES
1.1 Sistemas con solución única (comando \ )
Dado un sistema de ecuaciones lineales:

si tiene solución unica se resuelve con la barra de dividir invertida:

clc, clear
A = [2 2 4;1 2 0;1 3 1];
b = [2300;800;1500];
x = A\b

x = 3×1

Cómo dar los resultados con fprintf
Dado que los resultados se guardan en una matriz columna (vector),para mostrarlos adecuadamente
debemos emplear la función fpritnf dentro de un bucle for. En el caso anterior sería:

```

#### Página 2

```text
for i = 1:3
fprintf('x(%i) =  %i\n',i, x(i))
end

x(1) =  100
x(2) =  350
x(3) =  350

En caso de que queramos mostrar rótulos específicos debemos crear una variable de tipo string:

rotulo = ["titulo1" "titulo2" "titulo3"]

rotulo = 1×3 string
"titulo1"  "titulo2"  "titulo3"

que nos permite incluir los rótulos dentro del mismo bucle del fprintf mediante %s:

for i = 1:3
fprintf('%s =  %i\n',rotulo(i), x(i))
end

titulo1 =  100
titulo2 =  350
titulo3 =  350

No debemos olvidar añadir las unidades en las respuestas cuando sea necesario (metros, cm, euros, etc)

El comando fprintf permite formatear las salidas numéricas (número de decimales) mediante %a.bf
donde a son las cifras y b los decimales:

fprintf('%6.4f',x(1))

100.0000

la letra f indica que se trata de un número en coma flotante

Cómo comprobar que el resultado es correcto (norm)
Para comprobar que el resultado del sistema lineal  es correcto, calcularemos el residuo que es el
vector  y después calcularemos su "longitud" o norma (o módulo) con la función norm.

Veamos cómo lo haríamos en el ejemplo anterior:

r = A*x - b % residuo

r = 3×1

check = norm(r)

check =

No siempre resultará cero pero sí un número muy próximo a cero del orden de  por ejemplo

1.2 Sistemas lineales con infinitas soluciones (rref)

```

#### Página 3

```text
En el caso de que el sistema sea compatible indeterminado deberemos expresar las infinitas soluciones en
función de un parámetro para resolverlos deispondemos de dos funciones en Matlab:

La función rref (reduced row echelon form) nos proporciona la forma escalonada reducida de una matriz
(que debe ser la ampliada del sistema lineal

A = [1 1 0 0;1 0 0 1;0 0 1 1;0 1 1 0]; % Matriz de coeficientes
b = [431;255;340;516]; % Matriz de términos independientes
Ab = [A b]; % Matriz ampliada
sol = rref(Ab) % matriz en forma escalonada reducida

sol = 4×5
1  0  0  1  255
0  1  0  -1  176
0  0  1  1  340
0  0  0  0  0

Observando la matriz escalonada equivalente vemos que se trata de un sistema compatible indeterminado
(infinitas soluciones).

Tomando  como variable libre  podemos expresar las otras en la forma:

Recuerda que si resuelves un sistema indeterminado con la barra de dividir invertida (\) Matlab te dará la
solución de mínimos cuadrados

La función null
La función null calcula una base del espacio nulo de la matriz, es decir, encuentra todos los vectores
x tales que  devolviendo los vectores en las columnas de una matriz. Dichos vectores están
normalizados (norma o módulo 1)

A = [1 2 3;
2 4 6;
3 6 9];
null(A)

ans = 3×2
0.9555  0.1251
-0.0390  -0.8443
-0.2925  0.5211

2 Representación gráfica de funciones anónimas vectorizadas (y=@(x))
con plot

```

#### Página 4

```text
Como todavía no conocemos el cálculo simbólico de Matlab que veremos en el segundo cuatrimestte, para
representar gráficamente una función deberemos crearla como anónima vectorizada (y=@(x)) de tal forma
que sus argumentos de entrada y salida sean vectores, por ejemplo:

f = @(x) sin(x)

f = function_handle with value:
@(x)sin(x)

De tal modo que si queremos dibuja;rla en el intervalo  procederemos de la siguiente forma:

xp = linspace(-pi,pi,100); % generamos un vector de 100 componentes entre
-pi y pi
yp = f(xp);
plot(xp, yp,'LineWidth',2)
xlabel('x'); % etiquetas OX
ylabel('f(x)'); % etiueta OY
xline(0) % eje OY
yline(0) % eje OX
title('y = sen(x))') % título

En resumen, toda gráfica debe tener:

• Ejes
• Rótulos de ejes (con unidades si corresponde)
• Título
• Grosor de linea de 2

3 Polinomios (polyval, roots, polyfit)
Matlab trabaja con polinomios mediante vectores de forma que un polinomio se asimila a un vector fila
donde sus componentes son los coeficientes del polinomio en orden de mayor a menor grado. Cuando el

```

#### Página 5

```text
polinomio no tenga términos de un grado determinado se introduuce cero, por ejemplo, si queremos asignar
la variable p al polinomio  lo haremos así:

p = [-5 0 4 0 -1 12]

p = 1×6
-5  0  4  0  -1  12

Matlab dispone de varias funciones que trabajan directamente con polinomios, veamos las que nos
interesan

La función polyval da el valor de un polinomio en un punto, así si queremos saber el valor del poliomio
anterior para  escribiremos:

polyval(p,-3)

ans =
1122

Esta función la emplearemos para repressentar gráficamente el polinomio ya que admite vectores como
argumentos

xp = linspace(-1,1,100);
yp = polyval(p,xp);
plot(xp, yp,'LineWidth',2)
xline(0)

Existe la función polyfit que calcula el polinomio de ajuste dados unos puntos y que sólo emplearemos
para comprobar el resultado del polinomio calculado mediante sistemas lineales (ver la práctica
corrrespondiente)

También existe la función roots que calcula las raíces de un polinomio

4 Autovalores y autovectores (eig, poly, polyvalm)

```

#### Página 6

```text
Dada una matriz cuadrada, A, Matlab calcula fácilmente sus autovalores y autovectores y los da en sendas
matrices D y V mediante la función eig (que proviene de "eigenvalue")

La función es [V, D] = eig(A) donde D es la matriz diagonal de autovalores y V la matriz cuyas
columnas son los auotvectores normalizados (norma 1)

A = [3 1 1 1;1 3 -1 1;1 -1 3 1;1 1 1 2]

A = 4×4
3  1  1  1
1  3  -1  1
1  -1  3  1
1  1  1  2

[V, D] = eig(A)

V = 4×4
-0.1949  -0.7213  0.0000  0.6646
0.5446  0.2170  -0.7071  0.3953
0.5446  0.2170  0.7071  0.3953
-0.6072  0.6209  0.0000  0.4957
D = 4×4
0.5272  0  0  0
0  1.5374  0  0
0  0  4.0000  0
0  0  0  4.9354

Se puede emplear la función poly para calcular los coeficentes del polinomio característico de la matriz A

p = poly(A)

p = 1×5
1.0000  -11.0000  39.0000  -48.0000  16.0000

Lógicamente las raíces del polinomio característico coinciden con los autovalores:

roots (p)

ans = 4×1
4.9354
4.0000
1.5374
0.5272

La función polyvalm calcula el valor de un polinomio para una matriz. Esto nos permite verificar el teorema
de Cayley-Hamilton: todoa matriz cuadrada es raíz de su polonimo característico:

C_H = polyvalm(p,A)

C_H = 4×4
10-13 ×
-0.6395  -0.3197  -0.1776  -0.3553
-0.3197  -0.7816  0.1066  -0.1421
-0.3197  0.2487  -0.3553  -0.1421
-0.4263  -0.2132  -0.0711  -0.2842

norm(C_H)

ans =
1.2180e-13

```

#### Página 7

```text
5 Grafos (graph, digraph, sparse, full, shortestpath,
highlight)
5.1 Dibujar un grafo a partir de la matriz de adyacencia
clc, clear,clf
A = [0 1 1 1;1 1 1 0;1 1 0 0 ;1 0 0 0] % Matriz de adyacencia del grafo

A = 4×4
0  1  1  1
1  1  1  0
1  1  0  0
1  0  0  0

% Dibujamos el grafo
n = {'v1','v2', 'v3','v4'} % Nombramos los nodos

n = 1×4 cell
'v1'  'v2'  'v3'  'v4'

gr = graph(A,n);
plot(gr)

5.2 Dibujar un grafo dirigido o dígrafo a partir de la matriz de adyacencia

Dada la matriz de adyacencia  dibujar el grafo dirigido correspondiente:

Podemos introducir la matriz mediante la función sparse, o directamente

i = [1 1 2 3 4 4];

```

#### Página 8

```text
j = [2 4 4 1 1 3];
n = 4;
A = sparse(i,j,1,n,n);
full(A)

ans = 4×4
0  1  0  1
0  0  0  1
1  0  0  0
1  0  1  0

De esta forma se almacena una matriz dispersa (sparse) en una estructura de datos que sólo requiere
memoria para los elementos no nulos y sus índices. Esto apenas es necesario para una matriz de 4x4 con
sólo 10 entradas nulas, pero adquiere una importancia crucial para problemas más grandes.

Veamos cómo Matlab genera automáticamente el grafo. Previamente nombraremos los nodos con sus
denominaciones (en este caso números):

nodos = {'1', '2', '3','4'};
G = digraph(A,nodos);
plot(G)

5. 3 Camino más corto, grafos ponderados y matriz de adyacencia
Un grafo ponderado es aquél en que a cada una de sus aristas se le ha asignado un "peso" que
corresponde a coste, distancia, etc.

Matlab dispone de la función shortestpath que calcula el camino más corto entre dos nodos. Si se ha
asignado un peso a cada arista, la función shortestpath permite calcular el peso total del camino más
corto. Veámoslo con un ejemplo:

Supongamos el siguiente grafo:

clc, clear, clf
s = [1 1 1 2 2 6 6 7 7 3 3 9 9 4 4 11 11 8];
t = [2 3 4 5 6 7 8 5 8 9 10 5 10 11 12 10 12 12];

```

#### Página 9

```text
A sus aristas les asignamos los siguientes pesos:

pesos = [10 10 10 10 10 1 1 1 1 1 1 1 1 1 1 1 1 1];
nodos = {'1','2','3','4','5','6','7','8','9','10','11','12'}

nodos = 1×12 cell
'1'  '2'  '3'  '4'  '5'  '6'  '7'

G = graph(s,t,pesos,nodos);
H = plot(G,EdgeLabel=pesos)

H =
GraphPlot with properties:

NodeColor: [0.0660 0.4430 0.7450]
MarkerSize: 4
Marker: 'o'
EdgeColor: [0.0660 0.4430 0.7450]
LineWidth: 0.5000
LineStyle: '-'
NodeLabel: {'1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12'}
EdgeLabel: {'10' '10' '10' '10' '10' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '
XData: [-0.3385 1.0937 -0.4605 -1.6217 1.7518 1.5742 1.9192 0.4330 0.4884 -1.3026 -2.1816 -1.3
YData: [-0.5448 0.3637 -2.1786 0.3898 -0.5722 1.9227 1.1394 2.0214 -1.9189 -1.7733 -0.2326 1.3
ZData: [0 0 0 0 0 0 0 0 0 0 0 0]

Show all properties

Calculamos el camino más corto entre los vértices 3 y 8 así como el "coste" (suma de pesos de las aristas
del camino más corto) mediante la funcion shortestpath:

[Camino,Coste] = shortestpath(G,3,8)

Camino = 1×5
3  9  5  7  8
Coste =

Marcamos en rojo el camino obtenido:

highlight(H,Camino,'EdgeColor','r')

```

#### Página 10

```text
Finalmente podemos calcular la matriz de adyacencia del digrafo con las funciones adjacency y full:

A = sparse(s,t,pesos)

A = 11×12 sparse double matrix (18 nonzeros)
(1,2)  10
(1,3)  10
(1,4)  10
(2,5)  10
(7,5)  1
(9,5)  1
(2,6)  10
(6,7)  1
(6,8)  1
(7,8)  1
(3,9)  1
(3,10)  1
(9,10)  1
(11,10)  1
(4,11)  1
(4,12)  1
(8,12)  1
(11,12)  1

full(A)

ans = 11×12
0  10  10  10  0  0  0  0  0  0  0  0
0  0  0  0  10  10  0  0  0  0  0  0
0  0  0  0  0  0  0  0  1  1  0  0
0  0  0  0  0  0  0  0  0  0  1  1
0  0  0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  1  1  0  0  0  0
0  0  0  0  1  0  0  1  0  0  0  0
0  0  0  0  0  0  0  0  0  0  0  1
0  0  0  0  1  0  0  0  0  1  0  0
0  0  0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  1  0  1

```

#### Página 11

```text
RESUMEN DE FUNCIONES
Función  Descripción
\  Resuelve sistemas de ecuaciones lineales (solución única o de mínimos cuadrados).
fprintf  Muestra resultados en pantalla con formato personalizado.
norm  Calcula la norma (longitud) de un vector o la magnitud de una matriz.
rref  Obtiene la forma escalonada reducida de una matriz.
null  Calcula una base del espacio nulo de una matriz.
@(x)  Define funciones anónimas vectorizadas.
plot  Representa gráficamente datos o funciones.
polyval  Evalúa un polinomio en puntos dados.
roots  Calcula las raíces de un polinomio.
polyfit  Ajusta un polinomio a un conjunto de puntos.
eig  Calcula autovalores y autovectores de una matriz cuadrada.
poly  Obtiene los coeficientes del polinomio característico de una matriz.
polyvalm  Evalúa un polinomio en una matriz.
graph  Crea un grafo no dirigido a partir de una matriz de adyacencia.
digraph  Crea un grafo dirigido (dígrafo) a partir de una matriz de adyacencia.
sparse  Crea una matriz dispersa almacenando solo sus elementos no nulos.
full  Convierte una matriz dispersa en una matriz completa.
shortestpath  Calcula el camino más corto entre dos nodos de un grafo.
highlight  Resalta nodos o aristas en la representación gráfica de un grafo.

```


## Cuaderno de prácticas común (recursos, calor, interpolación, redes, grafos, Leontief, Markov, PageRank)

*Fuente: `COMUN A TODOS LOS GRUPOS/MPI1_PracticasR1.mlx`*

### ÁLGEBRA LINEAL · PRÁCTICAS

- Table of Contents

- 01. ASIGNACIÓN DE RECURSOS ·     P01.01 Cultivo de bacterias ·     P01.02 Elaboración de una dieta · 02. DISTRIBUCIÓN DE CALOR ·     P02.01 Ejercicio 8 página 33 del libro ·     P02.02. Distribución de calor en una placa (2) · 03. INTERPOLACIÓN POLINÓMICA ·     P03.01 Ejemplo 1.3.3 del libro (pág 34 - 35) ·     P03.2. Rendimiento de un proceso productivo en función de la temperatura · 04. FLUJO DE REDES ·     P04.01 Ejemplo del libro pag 43 ·     Problema 04.02. Análisis de redes · 05. GRAFOS ·     P05.01 Ejemplo 1 ·     P05.02 Ejemplo 2.8.1 (pag. 159) ·     P05.03 Ejemplo 2 ·     P05.04. Camino más corto, grafos ponderados y matriz de adyacencia ·     P05.05. Problema para practicar · 06. ANÁLISIS DE INSUMOS-PRODUCTOS DE LEONTIEF ·     Fundamento teórico ·         Ejemplo 1. Economía cerrada ·         Ejemplo 2. Economía abierta ·     P06.01 Ejemplo 2.4.9 del libro pags 109 - 111 ·     P06.02 Economía de Israel · 07. CADENAS DE MARKOV ·     P07.01 Ejemplo 2 revisado ·     P07.02. Ejemplo 1 revisado ·     P07.01 Ejemplo 9.3.3 del tema 9 del libro (web) pag 27 ·     P07.02. Alquiler de venículos · 08.  MOTORES DE BÚSQUEDA EN INTERNET. PAGE-RANK

#### 01. ASIGNACIÓN DE RECURSOS

Una gran cantidad de aplicaciones de los sistemas de ecuaciones lineales involucran asignar recursos limitados sujetos a un conjunto de restricciones.

P01.01 Cultivo de bacterias

Una bióloga colocó tres cepas de bacterias (denominadas I, II y III) en un tubo de ensayo, donde se alimentarán de tres diferentes fuentes alimenticias (A, B y C). Cada día, 2300 unidades de A, 800 unidades de B y 1500 unidades de C se colocan en el tubo de ensayo y cada bacteria consume cierto número de unidades de cada alimento por día, como se muestra en la tabla ¿Cuántas bacterias de cada cepa pueden coexistir en el tubo de ensayo y consumir todo el alimento?

[Imagen: Tabla bacterias/alimentos — Alimento A: cepa I 2, cepa II 2, cepa III 4; Alimento B: 1, 2, 0; Alimento C: 1, 3, 1.]

Sean $x_1 ,x_2$ y $x_3$ los números de bacterias de las cepas I, II y III, respectivamente. Dado que cada una de las bacterias $x_1$ de la cepa I consumen 2 unidades de A por día, la cepa I consume un total de $2x_1$ unidades por día. De igual modo, las cepas II y III consumen un total de $2x_2$ y $4x_3$ unidades de alimento A diariamente. Puesto que se quiere consumir las 2300 unidades de A, se tiene la ecuación

$$2x_1 +2x_2 +4x_3 =2300$$

Del mismo modo, se obtienen ecuaciones correspondientes para el consumo de B y C:

$$\begin{array}{l}
x_1 +2x_2 \;\;\;\;\;\;\;\;\;\;=800\\
x_1 +3x_2 +x_3 =1500
\end{array}$$

Por tanto, se tiene un sistema de tres ecuaciones lineales con tres variables que podemos resolver con Matlab:

```matlab
clc, clear
A1 = [2 2 4;1 2 0;1 3 1];
b = [2300;800;1500];
x = A1\b;
disp('La bióloga debe colocar:')
for i = 1:3
    fprintf('%i bacterias en la cepa %i\n',x(i),i)
end
```

**Salida:**
```text
La bióloga debe colocar:
100 bacterias en la cepa 1
350 bacterias en la cepa 2
350 bacterias en la cepa 3
```

P01.02 Elaboración de una dieta

Generalmente, un paquete de cereales indica el número de calorías y las cantidades de proteínas, carbohidratos y grasa contenidos en una unidad de producto. Se acompañan las cantidades para dos cereales comunes. Suponga que se preparará una mezcla de esos cereales, de manera que contenga exactamente 295 calorías, 9 gramos de proteínas, 48 gramos de carbohidratos y 8 gramos de grasa.

a) Escribe las ecuaciones que resuelven el problema indicando claramente a qué corresponden las variables

b) Escribe la ecuación matricial correspondiente

c) Determina si es posible preparar la mezcla pedida con los dos cereales.

[Imagen: Tabla 'Información nutricional por cada porción' — Krispis de Shit / Frostis de Crap: Calorías 110 / 130; Proteínas (g) 4 / 3; Carbohidratos (g) 20 / 18; Grasa (g) 2 / 5.]

#### 02. DISTRIBUCIÓN DE CALOR

El fundamento teórico está explicado en el problema 8 de la página 33 del libro

P02.01 Ejercicio 8 página 33 del libro

Debemos aproximar las temperaturas en los 9 puntos interiores de la placa

[Imagen: Placa con 9 puntos interiores $T_1$–$T_9$ (cuadrícula 3×3); bordes: superior 100°, laterales 50°, inferior 0° (problema de distribución de temperatura en equilibrio).]

Escribimos las ecuaciones de equilibrio en cada punto interior:

$$\begin{array}{l}
T_1 =\frac{1}{4}\left(T_2 +T_4 +100+50\right)\\
T_2 =\frac{1}{4}\left(T_1 +T_3 +T_5 +100\right)\\
T_3 =\frac{1}{4}\left(T_2 +T_6 +100+50\right)\\
T_4 =\frac{1}{4}\left(T_1 +T_5 +T_7 +50\right)\\
T_5 =\frac{1}{4}\left(T_2 +T_4 +T_6 +T_8 \right)\\
T_6 =\frac{1}{4}\left(T_3 +T_5 +T_9 +50\right)\\
T_7 =\frac{1}{4}\left(T_4 +T_8 +50+0\right)\\
T_8 =\frac{1}{4}\left(T_5 +T_7 +T_9 +0\right)\\
T_9 =\frac{1}{4}\left(T_6 +T_8 +50+0\right)
\end{array}$$

Reescribimos estas ecuaciones en forma matricial:

$$\left\lbrack \begin{array}{ccccccccc}
1 & -\frac{1}{4} & 0 & -\frac{1}{4} & 0 & 0 & 0 & 0 & 0\\
-\frac{1}{4} & 1 & -\frac{1}{4} & 0 & -\frac{1}{4} & 0 & 0 & 0 & 0\\
0 & -\frac{1}{4} & 1 & 0 & 0 & -\frac{1}{4} & 0 & 0 & 0\\
-\frac{1}{4} & 0 & 0 & 1 & -\frac{1}{4} & 0 & -\frac{1}{4} & 0 & 0\\
0 & -\frac{1}{4} & 0 & -\frac{1}{4} & 1 & -\frac{1}{4} & 0 & -\frac{1}{4} & 0\\
0 & 0 & -\frac{1}{4} & 0 & -\frac{1}{4} & 1 & 0 & 0 & -\frac{1}{4}\\
0 & 0 & 0 & -\frac{1}{4} & 0 & 0 & 1 & -\frac{1}{4} & 0\\
0 & 0 & 0 & 0 & -\frac{1}{4} & 0 & -\frac{1}{4} & 1 & -\frac{1}{4}\\
0 & 0 & 0 & 0 & 0 & -\frac{1}{4} & 0 & -\frac{1}{4} & 1
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
T_1 \\
T_2 \\
T_3 \\
T_4 \\
T_5 \\
T_6 \\
T_7 \\
T_8 \\
T_9
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
\frac{150}{4}\\
25\\
\frac{150}{4}\\
\frac{50}{4}\\
0\\
\frac{50}{4}\\
\frac{50}{4}\\
0\\
\frac{50}{4}
\end{array}\right\rbrack$$

Ahora podemos resolver el sistema lineal:

```matlab
T = [1 -0.25 0 -0.25 0 0 0 0 0;
    -0.25 1 -0.25 0 -0.25 0 0 0 0;
    0 -0.25 1 0 0 -0.25 0 0 0;
    -0.25 0 0 1 -0.25 0 -0.25 0 0;
    0 -0.25 0 -0.25 1 -0.25 0 -0.25 0;
    0 0 -0.25 0 -0.25 1 0 0 -0.25
    0 0 0 -0.25 0 0 1 -0.25 0;
    0 0 0 0 -0.25 0 -0.25 1 -0.25;
    0 0 0 0 0 -0.25 0 -0.25 1]
b = [150/4;25;150/4;50/4;0;50/4;50/4;0;50/4]
s = T\b;
```

**Salida:**
```text
T =
1.0000  -0.2500  0  -0.2500  0  0  0  0  0
-0.2500  1.0000  -0.2500  0  -0.2500  0  0  0  0
0  -0.2500  1.0000  0  0  -0.2500  0  0  0
-0.2500  0  0  1.0000  -0.2500  0  -0.2500  0  0
0  -0.2500  0  -0.2500  1.0000  -0.2500  0  -0.2500  0
0  0  -0.2500  0  -0.2500  1.0000  0  0  -0.2500
0  0  0  -0.2500  0  0  1.0000  -0.2500  0
0  0  0  0  -0.2500  0  -0.2500  1.0000  -0.2500
0  0  0  0  0  -0.2500  0  -0.2500  1.0000
b =
37.5000
25.0000
37.5000
12.5000
12.5000
12.5000
12.5000
```

Damos los resultados con fprintf:

```matlab
for i = 1:length(b)
    fprintf('La temperatura en el punto T(%i) es de %6.2f ºC\n',i,s(i))
end
```

**Salida:**
```text
La temperatura en el punto T(1) es de  67.86 ºC
La temperatura en el punto T(2) es de  71.43 ºC
La temperatura en el punto T(3) es de  67.86 ºC
La temperatura en el punto T(4) es de  50.00 ºC
La temperatura en el punto T(5) es de  50.00 ºC
La temperatura en el punto T(6) es de  50.00 ºC
La temperatura en el punto T(7) es de  32.14 ºC
La temperatura en el punto T(8) es de  28.57 ºC
La temperatura en el punto T(9) es de  32.14 ºC
```

P02.02. Distribución de calor en una placa (2)

Una placa metálica  se encuentra situada de forma que las temperaturas en sus bordes se muestran en la figura.

Se desea calcular las temperaturas interiores de la placa en los puntos indicados.

a) Escribe el sistema de ecauciones de equilibrio de temperaturas

b) Escriba el sistema mediante una ecuación matricial

c)  Resuelve el sistema. Emplea el mismo orden de los nodos para dar el resultado. Muestra los resultados con dos decimales.

[Imagen: Placa triangular con puntos interiores $t_1$–$t_6$; borde izquierdo 0°, hipotenusa 40°, borde inferior 5° (equilibrio térmico).]

#### 03. INTERPOLACIÓN POLINÓMICA

Fundamento teórico: libro pgas 34 - 35

P03.01 Ejemplo 1.3.3 del libro (pág 34 - 35)

Calcula la ecuación de un polinomio de menor grado que pase por los puntos $P_1 =\left(2,5\right),P_2 =\left(3,10\right),P_3 =\left(4,-3\right)$

Como son 3 puntos el polinomio será de segundo grado (parábola) en la forma: $p\left(x\right)=a_0 +a_1 x+a_2 x^2$

Escribimos las ecuaciones resultantes de imponer la condición de que pase por los puntos: $p\left(x_i \right)=y_i$:

Pasa por $P_1$: $p\left(2\right)=a_0 +a_1 \cdot 2+a_{2\cdot } {\cdot \;2}^2 =5$

Pasa por $P_2$: $p\left(3\right)=a_0 +a_1 \cdot 3+a_{2\cdot } \cdot 3^2 =10$

Pasa por $P_3$: $p\left(4\right)=a_0 +a_1 \cdot 4+a_{2\cdot } 4^2 =-3$

Escribimos las ecuaciones en forma matricial: $\left\lbrack \begin{array}{ccc}
4 & 2 & 1\\
9 & 3 & 1\\
16 & 4 & 1
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
a_2 \\
a_1 \\
a_0
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
5\\
10\\
-3
\end{array}\right\rbrack$

Resolvemos:

```matlab
clc, clear,clf
A = [4 2 1;9 3 1;16 4 1];
b = [5;10;-3];
P = A\b
```

**Salida:**
```text
P =
-9
-59
```

Damos la respuesta con fprintf:

```matlab
fprintf('El polinomio es: p(x) = %i·x^2 + %i·x + %i',P(1),P(2),P(3))
```

**Salida:**
```text
El polinomio es: p(x) = -9·x^2 + 50·x + -59
```

Representamos gráficamente los puntos y el polinomio en la misma gráfica

```matlab
x = [2 3 4]; y = [5 10 -3]; % coordenadas de los puntos
plot(x,y,'or','LineWidth',1.5)
hold on
xp = linspace(2,4,100); % creamos un vector de 100 componentes entre 2 y 4
yp = polyval(P,xp);
plot(xp,yp,'-k','LineWidth',2)
legend('puntos','parábola')
xlabel('x');ylabel('y')
hold off
```

**Salida:**
```text
[figura]
```

P03.2. Rendimiento de un proceso productivo en función de la temperatura

En una planta química se sintetiza un producto que es utilizado posteriormente como conservante de productos enlatados. El rendimiento del proceso depende de la temperatura.

Se dispone de los siguientes datos:

[Imagen: Tabla temperatura–rendimiento: T (°C) 150, 160, 170, 180, 190, 200, 210; R (%) 35.5, 37.8, 43.6, 45.7, 47.3, 50.1, 51.2 (ajuste por mínimos cuadrados/interpolación).]

a) Escribe las ecuaciones que determinan el polinomio que interpola los datos

b) Determina los coeficientes del polinomio resolviendo las ecuaciones

c) Representa gráficamente los puntos y el polinomio obtenido $R=f\left(T\right)$

d) Se considera un rendimiento óptimo el que va de 38.5 a 45, por lo que la planta trabaja a 175ºC. Si la temperatura de trabajo cae a 162 ºC por una avería, ¿será el proceso satisfactorio hasta que sea reparada?

#### 04. FLUJO DE REDES

Fundamento teórico: libro pags 42 - 46

P04.01 Ejemplo del libro pag 43

[Imagen: Red de tráfico de 4 intersecciones A, B, C, D (calles Atonsu-Prempeh, Roman Hill, Mercado Asafo-Kaietia, Intercambiador Labour-Asafo) con flujos internos x, y, z, w y externos: 190 vph sale en A, 241 vph sale por Roman Hill, 150 vph entra en B, 105 vph entra por Labour-Asafo, 280 vph entra en D, 236 vph entra por el sur en D, 230 vph sale en C, 110 vph sale por el sur en C.]

a) Escribimos las ecuaciones de cada nodo (tráfico entrante = tráfico saliente):

Nodo A: $x+y=241+290$

Nodo B: $150+105=x+w$

Nodo C: $z+w=230+110$

Nodo D: $280+236=y+z$

b) Reescribimos las ecuaciones en forma matricial:

$$\begin{array}{l}
x+y=431\\
x+w=255\\
z+w=340\\
y+z=516
\end{array}$$$$\Longrightarrow \left\lbrack \begin{array}{cccc}
1 & 1 & 0 & 0\\
1 & 0 & 0 & 1\\
0 & 0 & 1 & 1\\
0 & 1 & 1 & 0
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
x\\
y\\
z\\
w
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
431\\
255\\
340\\
516
\end{array}\right\rbrack$$

c) Calculamos la forma escalonada reducida de la matriz ampliada del sistema mediante rref:

```matlab
clc, clear
A = [1 1 0 0;1 0 0 1;0 0 1 1;0 1 1 0]; % matriz de coeficientes
b = [431;255;340;516]; % vector de términos independientes
Ab = [A b] % matriz ampliada
P = rref(Ab)
```

**Salida:**
```text
WARNING: Warning: Graphics timeout occurred. To share details of this issue with MathWorks technical support, please include that this is an unresponsive graphics client with your service request.
Ab =
1  1  0  0  431
1  0  0  1  255
0  0  1  1  340
0  1  1  0  516
P =
1  0  0  1  255
0  1  0  -1  176
0  0  1  1  340
0  0  0  0  0
```

Analizamos el resultado y lo escribimos en forma de ecuaciones:

$\begin{array}{l}
x+w=255\\
y-w=176\\
z+w=340
\end{array}$ tomamos como variable libre la que corresponde a la columna sin pivote: $w=t$ y sustituimos: $\begin{array}{l}
x=255-t\\
y=176+t\\
z=340-t\\
w=t
\end{array}$ esta es la solución general del sistema que podemos escribir matricialmente como: $\left\lbrack \begin{array}{c}
x\\
y\\
z\\
w
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
255\\
176\\
340\\
0
\end{array}\right\rbrack +t\cdot \left\lbrack \begin{array}{c}
-1\\
1\\
-1\\
1
\end{array}\right\rbrack$

Observando las ecuaciones podemos concluir que $t=w\le 255$ de modo que se conservan las direcciones en las calles, en el caso límite de que $w=t=255$ tendremos: $\begin{array}{l}
x=255-255=0\\
y=176+255=431\\
z=340-255=85
\end{array}$    Si tomamos (como en el libro) un tráfico límite de $w=t=100$ obtendremos:$\begin{array}{l}
x=255-100=155\;\textrm{vph}\\
y=176+100=276\;\textrm{vph}\\
z=340-100=240\;\textrm{vph}
\end{array}$

Problema 04.02. Análisis de redes

Dado el esquema de flujo en la red:

[Imagen: Red de flujo con 5 nodos: 2→1 con 20, 1→4 con $x_1$, 1→3 con $x_2$, 2→3 con $x_3$, 5→2 con $x_4$, 4→5 con $x_5$, 3→4 con 10, 3→5 con 10.]

a) Escribe un sistema de ecuaciones lineales que representen la red

b) Resuelve el sistema lineal con el comando rref

c) Analiza el resultado ¿qué condiciones pueden establecerse?

#### 05. GRAFOS

Fundamento teórico: Libro tema 2.8 pags 159 - 165

No obstante incluimos a continuación una breve explicación de grafos y dígrafos

1. Grafos

Existen muchas situaciones en las que es importante poder modelar las interrelaciones entre un conjunto finito de objetos. Por ejemplo, al describir varios tipos de redes (carreteras que conectan ciudades, rutas de aerolíneas que conectan ciudades, redes de comunicación que conectan satélites, etc.) o relaciones entre grupos o individuos (relaciones de amistad en una sociedad, relaciones depredador-presa en un ecosistema, relaciones de dominio en un deporte, etc.). Los grafos son adecuados para modelar tales redes y relaciones, y es evidente que las matrices son una herramienta útil en su estudio.

Un grafo consiste de un conjunto finito de puntos (llamados vértices) y un conjunto finito de aristas, cada una de las cuales conecta dos vértices (no necesariamente distintos). Se dice que dos vértices son adyacentes si son los puntos finales de una arista. La figura muestra un ejemplo del mismo grafo dibujado en dos formas diferentes. Los grafos son “iguales” en el sentido de que todo por lo que debe preocuparse es por las relaciones de adyacencia que identifican las aristas.

[Imagen: Grafo no dirigido A, B, C, D (todas las aristas excepto C–D) dibujado de dos maneras (isomorfas).]

Es posible registrar la información esencial acerca de un grafo en una matriz y usar álgebra matricial para ayudar a responder ciertas preguntas acerca del grafo. Esto es particularmente útil si los grafos son grandes, pues las computadoras pueden manejar los cálculos muy rápidamente.

Si G es un grafo con n vértices, entonces su matriz de adyacencia es la matriz $A$ [o $A\left(G\right)$] de n x n definida por:

$$a_{\textrm{ij}} =\left\lbrace \begin{array}{ll}
1 & \textrm{si}\;\textrm{existe}\;\textrm{una}\;\textrm{arista}\;\textrm{entre}\;\textrm{los}\;\textrm{vertices}\;i\;y\;j\\
0 & \textrm{en}\;\textrm{caso}\;\textrm{contrario}
\end{array}\right.$$

A continuación se muestra un grafo y su matriz de adyacencia

[Imagen: Grafo con 4 vértices y un lazo en $v_2$, y su matriz de adyacencia $A=\begin{pmatrix}0&1&1&1\\1&1&1&0\\1&1&0&0\\1&0&0&0\end{pmatrix}$.]

Observa que la matriz de adyacencia de un grafo necesariamente es una matriz simétrica.(¿Porqué?)Nota también que una entrada diagonal $a_{\textrm{ii}}$ de A es cero a menos que haya un bucle en el vértice i.

En algunas situaciones un grafo puede tener más de una arista entre un par de vértices. En tales casos, puede tener sentido modificar la definición de la matriz de adyacencia de modo que $a_{\textrm{ij}}$ sea igual al número de aristas entre los vértices $i$ y $j$.

Trayectoria

Una trayectoria en un grafo es una secuencia de aristas que permiten viajar de un vértice a otro de manera continua. La longitud de una trayectoria es el número de aristas que contiene, y a una trayectoria con  $k\;$aristas se le denominará k-trayectoria. Por ejemplo, en el grafo de la figura, $v_1 ,v_3 ,v_2 ,{\;v_1 }$ es una 3-trayectoria, y $v_4 ,v_1 ,v_2 ,v_2 ,v_1 ,v_3$ es una 5-trayectoria. Nótese que la primera de éstas es cerrada (comienza y termina en el mismo vértice); a tal trayectoria se le llama circuito. La segunda usa las aristas entre $v_1$ y $v_2$ dos veces; una trayectoria que no incluye la misma arista más de una vez se llama trayectoria simple.

Es posible usar las potencias de la matriz de adyacencia de un grafo para obtener información acerca de las trayectorias de varias longitudes en el grafo. Considere el cuadrado de la matriz de adyacencia de la figura anterior:

$$A^2 =\left\lbrack \begin{array}{cccc}
3 & 2 & 1 & 0\\
2 & 3 & 2 & 1\\
1 & 2 & 2 & 1\\
0 & 1 & 1 & 1
\end{array}\right\rbrack$$

¿Qué representan las entradas de $A^2$? Observa la entrada (2, 3). A partir de la definición de multiplicación matricial, se sabe que:

$${\left(A^2 \right)}_{23} =a_{21} \cdot a_{13} +a_{22} \cdot a_{23} +a_{23} \cdot a_{33} +a_{24} \cdot a_{43}$$

La única manera en que esta expresión puede resultar en un número distinto de cero es si al menos uno de los productos $a_{2k} \cdot a_{\textrm{k3}}$ que constituyen la suma es distinto de cero. Pero $a_{2k} \cdot a_{\textrm{k3}}$ es distinto de cero si y sólo si tanto $a_{2k}$ como $a_{\textrm{k3}}$ son distintos de cero, lo que significa que hay una arista entre $v_2$ y $v_k$ , así como una arista entre $v_k$ y $v_3$. Por tanto, habrá una 2-trayectoria entre los vértices 2 y 3 (vía el vértice k). En el ejemplo, esto ocurre para $k=1$ y para $k=2$,de modo que:

$${\left(A^2 \right)}_{23} =a_{21} \cdot a_{13} +a_{22} \cdot a_{23} +a_{23} \cdot a_{33} +a_{24} \cdot a_{43} =1\cdot 1+1\cdot 1+1\cdot 0+0\cdot 0=2$$

la cual dice que hay dos 2-trayectorias entre los vértices 2 y 3. (Comprueba para ver que las entradas restantes de $A^2$ correctamente dan 2-trayectorias en el grafo.) El argumento que acaba de darse puede generalizarse para producir el siguiente resultado:

Si A es la matriz de adyacencia de un grafo G, entonces la entrada $\left(i,j\right)$ de $A^k$ es igual al número de k-trayectorias entre los vértices $i$ y $j$.

P05.01 Ejemplo 1

Para saber cuántas 3-trayectorias hay entre $v_1$ y $v_2$ en el grafo del ejemplo anterior, debemos conocer el elemento $\left(1,2\right)$ de la matriz $A^3$. Podemos hacerlo con Matlab y dibujarlo con el comando graph:

```matlab
clc, clear,clf
A = [0 1 1 1;1 1 1 0;1 1 0 0 ;1 0 0 0] % Matriz de adyacencia del grafo
% Dibujamos el grafo
n = {'v1','v2', 'v3','v4'} % Nombramos los nodos
gr = graph(A,n);
plot(gr)
A3 = A^3; % Calculamos A^3
s = A3(1,2); % Extraemos el elemento (1,2) de la matriz A^3
fprintf('Entre v1 y v2 hay %i 3-trayectorias\n',s)
```

**Salida:**
```text
A =
0  1  1  1
1  1  1  0
1  1  0  0
1  0  0  0
n = 1×4 cell array
{'v1'}  {'v2'}  {'v3'}  {'v4'}
[figura]
Entre v1 y v2 hay 6 3-trayectorias
```

Dígrafos (o grafos dirigidos)

En muchas aplicaciones que pueden modelarse mediante un grafo, los vértices se ordenan mediante algún tipo de relación que impone una dirección a las aristas. Por ejemplo, las aristas dirigidas pueden usarse para representar rutas de una vía en un grafo que modela una red de transporte o relaciones depredador-presa en un grafo que modela un ecosistema. Un grafo con aristas dirigidas se llama digrafo. La siguiente figura muestra un ejemplo.

[Imagen: Dígrafo de 4 vértices: $v_1\to v_2$, $v_1\to v_4$, $v_4\to v_1$, $v_2\to v_4$, $v_4\to v_3$, $v_3\to v_1$.]

Una sencilla modificación de la definición de las matrices de adyacencia permite usarlas con digrafos.

Si G es un dígrafo con n vértices, entonces su matriz de adyacencia es la matriz $A$ [o $A\left(G\right)$] de n x n definida por:

$$a_{\textrm{ij}} =\left\lbrace \begin{array}{ll}
1 & \textrm{si}\;\textrm{existe}\;\textrm{una}\;\textrm{arista}\;\textrm{del}\;\textrm{vertice}\;i\;\textrm{al}\;\textrm{vertice}\;j\\
0 & \textrm{en}\;\textrm{caso}\;\textrm{contrario}
\end{array}\right.$$

Por tanto, la matriz de adyacencia del dígrafo anterior es:

$$A=\left\lbrack \begin{array}{cccc}
0 & 1 & 0 & 1\\
0 & 0 & 0 & 1\\
1 & 0 & 0 & 0\\
1 & 0 & 1 & 0
\end{array}\right\rbrack$$

Cómo opera Matlab

Para definir la matriz de adyacencia se generan únicamente aquellos elementos que no son nulos mediante sendos vectores que indican la fila/columna donde se encuentran

```matlab
  i = [1 1 2 3 4 4];
  j = [2 4 4 1 1 3];
  n = 4;
  A1 = sparse(i,j,1,n,n);
  full(A1)
```

**Salida:**
```text
ans =
0  1  0  1
0  0  0  1
1  0  0  0
1  0  1  0
```

De esta forma se almacena una matriz dispersa (sparse) en una estructura de datos que sólo requiere memoria para los elementos no nulos y sus índices. Esto apenas es necesario para una matriz de 4x4 con sólo 10 entradas nulas, pero adquiere una importancia crucial para problemas más grandes.

Veamos cómo Matlab genera automáticamente el grafo. Previamente nombraremos los nodos con sus denominaciones (en este caso números):

```matlab
nodos = {'1', '2', '3','4'};
G = digraph(A1,nodos);
plot(G)
```

**Salida:**
```text
[figura]
```

Es aconsejable leer bien el menú de ayuda de matlab del comando digraph. En él encontraréis todas las posibilidades del comando como asignar pesos a los nodos, omitir auto enlaces, ect.

P05.02 Ejemplo 2.8.1 (pag. 159)

Vamos a emplear el ejemplo del libro para aprender cómo opera Matlab con grafos dirigidos (o dígrafos).

a) Como representar el grafo a partir de la matriz de incidencia (o adyacencia):

Para definir la matriz de adyacencia se generan únicamente aquellos elementos que no son nulos mediante sendos vectores que indican la fila/columna donde se encuentran

```matlab
clc, clear, clf
i = [ 1 2 2 3 4 4 5 5];
j = [ 2 1 5 4 2 3 1 4];
n = 5;
A1 = sparse(i,j,1,n,n);
full(A1)
```

**Salida:**
```text
ans =
0  1  0  0  0
1  0  0  0  1
0  0  0  1  0
0  1  1  0  0
1  0  0  1  0
```

De esta forma se almacena una matriz dispersa (sparse) en una estructura de datos que sólo requiere memoria para los elementos no nulos y sus índices. Esto apenas es necesario para una matriz de 4x4 con sólo 10 entradas nulas, pero adquiere una importancia crucial para problemas más grandes.

b) Veamos cómo Matlab genera automáticamente el digrafo. Previamente nombraremos los nodos con sus denominaciones (en este caso números):

```matlab
nodos = {'1', '2', '3','4' '5'};
G = digraph(A1,nodos);
plot(G)
```

**Salida:**
```text
[figura]
```

Es aconsejable leer bien el menú de ayuda de matlab del comando digraph. En él encontraréis todas las posibilidades del comando como asignar pesos a los nodos, omitir auto enlaces, ect.

P05.03 Ejemplo 2

Cinco tenistas (Djokovic, Federer, Nadal, Roddick y Safin) compiten en un torneo con el sistema round-robin en el que cada jugador compite con todos los demás una vez. El digrafo en la figura resume los resultados. Una arista dirigida del vértice $i$ al vértice $j$ significa que el jugador $i$ venció al jugador $j$. (Un digrafo en el que existe exactamente una arista dirigida entre cada par de vértices se llama torneo.)

[Imagen: Grafo dirigido de 5 vértices (D, F, N, R, S) en forma de pentágono con estrella (relaciones de dominancia/torneo).]

La matriz de adyacencia de este digrafo es:

$$A=\left\lbrack \begin{array}{ccccc}
0 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & 1 & 1\\
1 & 0 & 0 & 1 & 0\\
0 & 0 & 0 & 0 & 1\\
0 & 0 & 1 & 0 & 0
\end{array}\right\rbrack$$

donde el orden de los vértices (y por tanto, las filas y columnas de A), (es decir, D, F, N, R, S) se determina alfabéticamente. Por tanto, Federer corresponde a la fila 2 y columna 2, por ejemplo. Supongamos que se quiere clasificar a los cinco jugadores con base en los resultados de sus partidos. Una forma de hacer esto puede ser contar el número de triunfos de cada jugador. Observa que el número de triunfos de cada jugador es justo la suma de las entradas en la fila correspondiente; de manera equivalente, el vector que contiene todas las sumas de filas está dado por el producto $A\cdot \mathit{\mathbf{j}}$ donde

$\mathit{\mathbf{j}}=\left\lbrack \begin{array}{c}
1\\
1\\
1\\
1\\
1
\end{array}\right\rbrack$de modo que: $A\cdot \mathit{\mathbf{j}}=\left\lbrack \begin{array}{ccccc}
0 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & 1 & 1\\
1 & 0 & 0 & 1 & 0\\
0 & 0 & 0 & 0 & 1\\
0 & 0 & 1 & 0 & 0
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
1\\
1\\
1\\
1\\
1
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
3\\
3\\
2\\
1\\
1
\end{array}\right\rbrack$

que produce la siguiente clasificación:

Primero: Djokovic, Federer (empatados)

Segundo: Nadal

Tercero: Roddick, Safin (empatados)

¿Los jugadores empatados en esta clasificación son igualmente fuertes? Djokovic puede argumentar que, puesto que venció a Federer, él merece el primer lugar. Roddick usaría el mismo tipo de argumento para romper el empate con Safin. Sin embargo, Safin podría argumentar que él tiene dos victorias “indirectas” porque venció a Nadal, quien venció a otros dos; es más, puede puntualizar que Roddick sólo tiene una victoria indirecta (sobre Safin, quien venció a Nadal).

Dado que en un grupo de empates puede no haber un jugador que venciera a todos los demás en el grupo, la notación de victorias indirectas parece más útil. Una victoria indirecta corresponde a una 2-trayectoria en el digrafo, de modo que puede usar el cuadrado de la matriz de adyacencia. Para calcular tanto los triunfos como las victorias indirectas para cada jugador, se necesitan las sumas de fila de la matriz $A+A^2$, que están dadas por:

[Imagen: Cálculo: $(A+A^2)\mathbf j=\left(\begin{smallmatrix}0&1&0&1&1\\0&0&1&1&1\\1&0&0&1&0\\0&0&0&0&1\\0&0&1&0&0\end{smallmatrix}+\begin{smallmatrix}0&0&2&1&2\\1&0&1&1&1\\0&1&0&1&2\\0&0&1&0&0\\1&0&0&1&0\end{smallmatrix}\right)\mathbf 1=\left(\begin{smallmatrix}0&1&2&2&3\\1&0&2&2&2\\1&1&0&2&2\\0&0&1&0&1\\1&0&1&1&0\end{smallmatrix}\right)\mathbf 1=(8,7,6,2,3)^T$ (poder de cada vértice en el grafo de dominancia).]

En consecuencia, los jugadores se clasificarían en el siguiente orden: Djokovic, Federer, Nadal, Safin, Roddick. Por desgracia, este planteamiento no garantiza romper todos los empates.

Veamos cómo hacerlo con Matlab.

```matlab
A2 = [0 1 0 1 1;0 0 1 1 1;1 0 0 1 0;0 0 0 0 1;0 0 1 0 0] % Matriz de adyacencia
% Dibujamos el dígrafo para comprobación
nodos = {'Djokovic', 'Federer', 'Nadal','Roddick','Safin'};
G = digraph(A2,nodos);
plot(G)
B = A2 + A2^2; % Caclulamos A+A^2
cl = sum(B,2) % Creamos el vector cl con la suma de las filas de B
```

**Salida:**
```text
A2 =
0  1  0  1  1
0  0  1  1  1
1  0  0  1  0
0  0  0  0  1
0  0  1  0  0
[figura]
cl =
```

Vamos a dar los resultados:

```matlab
% Ordenamos los elementos del vector cl de mayor a menor conservando su
% indice para los nombres de los nodos
idx = 1:5;
for k = 1:4
    indm = k;
    for j = k+1:5
    if cl(idx(j))>cl(idx(indm))
        indm = j;
    end
    end
temp = idx(k);
idx(k) = idx(indm);
idx(indm) = temp;
end
% Damos los resultados
for i = 1:5
   text = [num2str(i), 'º es: ', nodos{idx(i)}, '.'];
   disp(text)
end
```

**Salida:**
```text
1º es: Djokovic.
2º es: Federer.
3º es: Nadal.
4º es: Safin.
5º es: Roddick.
```

Esto último puede parecer algo artificioso. Podemos hacerlo empleando la función sort de Matlab de la siguiente forma:

```matlab
[C,I] = sort(cl,'descend') % en C los puntos de mayor a menor en I los índices del vector cl que se corresponden con el orden de C
nodosord = nodos(I); % ordenamos los nodos de igual forma que la clasificación
N = convertCharsToStrings(nodosord); % convertimos los nodos de formato cell a char para el fprintf
for i = 1: length(cl)
    fprintf('%.0fº es %s\n',i,N(i))
end
```

**Salida:**
```text
C =
I =
1º es Djokovic
2º es Federer
3º es Nadal
4º es Safin
5º es Roddick
```

Se puede generalizar lo visto anteriormente en el siguiente:

Teorema: Si A es la matriz de adyacencia de un dígrafo y $a_{\textrm{ij}}^r$el elemento $\left(i,j\right)$ de la matriz $A^r$, entonces $a_{\textrm{ij}}^r$ es igual al número de r-trayectorias entre el nodo $i$ y el nodo $j$. O dicho de otro modo: el nodo $i$ está conectado con el nodo $j$ mediante una r-trayectoria si y sólo si $a_{\textrm{ij}}^r \not= 0$.

Veamos la aplicación práctica de este teorema en un ejemplo.

Ejemplo. La figura representa el mapa de rutas de una pequeña compañía aérea que presta servicio a las cuatro ciudades $P_1 ,\;P_2 \;,P_3 ,P_4$.

[Imagen: Grafo dirigido de 4 vértices $P_1$–$P_4$ con aristas en ambos sentidos entre algunos pares.]

Considerada como grafo dirigido, su matriz de adyacencia es: $M=\left\lbrack \begin{array}{cccc}
0 & 1 & 1 & 0\\
1 & 0 & 1 & 0\\
1 & 0 & 0 & 1\\
0 & 1 & 1 & 0
\end{array}\right\rbrack$

Si calculamos las potencias de M:

$$M^2 =\left\lbrack \begin{array}{cccc}
2 & 0 & 1 & 1\\
1 & 1 & 1 & 1\\
0 & 2 & 2 & 0\\
2 & 0 & 1 & 1
\end{array}\right\rbrack ,\;\;\;\;\;M^3 =\left\lbrack \begin{array}{cccc}
1 & 3 & 3 & 1\\
2 & 2 & 3 & 1\\
4 & 0 & 2 & 2\\
1 & 3 & 3 & 1
\end{array}\right\rbrack$$

Si queremos saber el número de conexiones desde la ciudad $P_4$ a la ciudad $P_3$ podemos emplear el teorema anterior. Como $m_{43} =1$, hay una 1-trayectoria entre $P_4$ y $P_3$, como $m_{43}^2 =1$ hay una 2-trayectoria entre $P_4$ y $P_3$ y como $m_{43}^3 =3$ hay tres 3-trayectorias entre $P_4$ y $P_3$.

En efecto, lo podemos verificar mediante el dígrafo:

Conexiones 1-trayectoria entre $P_4$ y $P_3$:  $P_4 \to$$P_3$

Conexiones 2-trayectoria entre $P_4$ y $P_3$:  $P_4 \to P_2 \to$$P_3$

Conexiones 3-trayectoria entre $P_4$ y $P_3$:  $P_4 \to$$P_3 \to P_4 \to P_3$

$$P_4 \to$$$$P_2 \to P_1 \to P_3$$

$$P_4 \to$$$$P_3 \to P_1 \to P_3$$

P05.04. Camino más corto, grafos ponderados y matriz de adyacencia

Un grafo ponderado es aquél en que a cada una de sus aristas se le ha asignado un "peso" que corresponde a coste, distancia, etc.

Matlab dispone de la función shortestpath que calcula el camino más corto entre dos nodos. Si se ha asignado un peso a cada arista, la función shortestpath permite calcular el peso total del camino más corto. Veámoslo con un ejemplo:

Supongamos el siguiente grafo:

```matlab
clc, clear, clf
s = [1 1 1 2 2 6 6 7 7 3 3 9 9 4 4 11 11 8];
t = [2 3 4 5 6 7 8 5 8 9 10 5 10 11 12 10 12 12];
```

A sus aristas les asignamos los siguientes pesos:

```matlab
pesos = [10 10 10 10 10 1 1 1 1 1 1 1 1 1 1 1 1 1];
nodos = {'1','2','3','4','5','6','7','8','9','10','11','12'}
G = graph(s,t,pesos,nodos);
H = plot(G,EdgeLabel=pesos)
```

**Salida:**
```text
nodos = 1×12 cell array
{'1'}  {'2'}  {'3'}  {'4'}  {'5'}  {'6'}  {'7'}  {'8'}  {'9'}  {'10'}  {'11'}  {'12'}
H =
<a href="matlab:helpPopup('matlab.graphics.chart.primitive.GraphPlot')" style="font-weight:bold">GraphPlot</a> with properties:

NodeColor: [0 0.4470 0.7410]
MarkerSize: 4
Marker: 'o'
EdgeColor: [0 0.4470 0.7410]
LineWidth: 0.5000
LineStyle: '-'
NodeLabel: {'1'  '2'  '3'  '4'  '5'  '6'  '7'  '8'  '9'  '10'  '11'  '12'}
EdgeLabel: {'10'  '10'  '10'  '10'  '10'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'  '1'}
XData: [-0.3385 1.0937 -0.4605 -1.6217 1.7518 1.5742 1.9192 0.4330 0.4884 -1.3026 -2.1816 -1.3554]
YData: [-0.5448 0.3637 -2.1786 0.3898 -0.5722 1.9227 1.1394 2.0214 -1.9189 -1.7733 -0.2326 1.3833]
ZData: [0 0 0 0 0 0 0 0 0 0 0 0]

Show <a href="matlab:if exist('H', 'var'), matlab.graphics.internal.getForDisplay('H', H, 'matlab.graphics.chart.primitive.GraphPlot'), else, matlab.graphics.internal.getForDisplay('H'), end">all properties</a>
```

Calculamos el camino más corto entre los vértices 3 y 8 así como el "coste" (suma de pesos de las aristas del camino más corto) mediante la funcion shortestpath:

```matlab
[Camino,Coste] = shortestpath(G,3,8)
```

**Salida:**
```text
Camino =
3  9  5  7  8
Coste =
```

Marcamos en rojo el camino obtenido:

```matlab
 highlight(H,Camino,'EdgeColor','r')
```

**Salida:**
```text
[figura]
```

Finalmente podemos calcular la matriz de adyacencia del digrafo con las funciones adjacency y full:

```matlab
A = sparse(s,t,pesos)
full(A)
```

**Salida:**
```text
A = 11×12 sparse double matrix (18 nonzeros)
(1,2)  10
(1,3)  10
(1,4)  10
(2,5)  10
(7,5)  1
(9,5)  1
(2,6)  10
(6,7)  1
(6,8)  1
(7,8)  1
(3,9)  1
(3,10)  1
(9,10)  1
(11,10)  1
(4,11)  1
(4,12)  1
(8,12)  1
(11,12)  1
ans =
0  10  10  10  0  0  0  0  0  0  0  0
0  0  0  0  10  10  0  0  0  0  0  0
0  0  0  0  0  0  0  0  1  1  0  0
0  0  0  0  0  0  0  0  0  0  1  1
0  0  0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  1  1  0  0  0  0
0  0  0  0  1  0  0  1  0  0  0  0
0  0  0  0  0  0  0  0  0  0  0  1
0  0  0  0  1  0  0  0  0  1  0  0
0  0  0  0  0  0  0  0  0  0  0  0
```

P05.05. Problema para practicar

Son conocidas las distancias entre las cinco ciudades siguientes: Málaga, Madrid, Barcelona, Valencia y Sevilla, que se muestran en la tabla siguiente.

Málaga

Madrid

Barcelona

Valencia

Sevilla

1 Málaga

0

529

996

618

206

2 Madrid

529

0

626

360

530

3 Barcelona

996

626

0

349

994

4 Valencia

618

360

349

0

656

5 Sevilla

206

530

994

656

0

- Construir el grafo dirigido, incluyendo las distancias entre ciudades y los nombres de éstas. Añadir una rama entre Sevilla y Oviedo, que se encuentra a 779 kms. La ruta debe ser de ida y vuelta.

- Distancia mínima entre Oviedo y Madrid

- Matriz de adyacencia completa

#### 06. ANÁLISIS DE INSUMOS-PRODUCTOS DE LEONTIEF

Fundamento teórico: Libro pags 18 - 19, 109 - 111

Fundamento teórico

Una economía es un sistema muy complejo con muchas interrelaciones entre sus diversos sectores y los bienes y servicios que se producen y consumen. Determinar los precios óptimos y los niveles de producción sujetos a las metas económicas deseadas requiere sofisticados modelos matemáticos. El álgebra lineal resulta ser una poderosa herramienta en el desarrollo y análisis de tales modelos económicos.

En esta sección se introducen dos modelos basados en el trabajo del economista de Harvard, Wassily Leontief, en la década de 1930 por lo que recibió el Premio Nobel de Economía en 1973. Sus métodos, a los que con frecuencia se les refiere como análisis input-output, ahora son herramientas estándar en la economía matemática y los usan ciudades, corporaciones y países completos para planificación y pronósticos económicos.

[Imagen: Fotografía de Wassily Leontief (economista, modelo input-output).]

Ejemplo 1. Economía cerrada

La economía de una región consiste de tres industrias o sectores: servicios, electricidad y producción de petróleo. Por simplicidad, se supone que cada industria produce un solo artículo (bienes o servicios) en un año dado y que el ingreso (output) se genera a partir de la venta de este artículo. Cada industria compra artículos de las otras industrias, incluida ella misma, para generar su output. Ningún artículo se compra fuera de la región y ninguna salida (output) se vende fuera de la región. Para cada industria se supone que la producción iguala exactamente al consumo (output igual a input, ingreso igual a gasto). En este sentido, esta es una economía cerrada que está en equilibrio. La tabla resume cuánta output de cada industria consume cada industria.

[Imagen: Tabla de Leontief (economía cerrada): consumido por (filas) / producido por (columnas) Servicios, Electricidad, Petróleo: Servicios 1/4, 1/3, 1/2; Electricidad 1/4, 1/3, 1/4; Petróleo 1/2, 1/3, 1/4.]

De la primera columna de la tabla se ve que la industria de servicios consume 1/4 de su propio output, la electricidad consume otro 1/4 y la industria petrolera usa 1/2 del output de la industria de servicios. Las otras dos columnas tienen interpretaciones similares. Note que la suma de cada columna es 1, lo que indica que se consumen todos los output de cada industria.

Sean $x_1 ,x_2$ y $x_3$ que denotan el output (ingreso) anual de las industrias de servicios, electricidad y petróleo, respectivamente, en millones de dólares. Dado que el consumo corresponde al gasto, la industria de servicios gasta $\frac{1}{4}x_1$en su propio artículo, $\frac{1}{3}x_2$ en electricidad y $\frac{1}{2}x_3$ en petróleo. Esto significa que el gasto total anual de la industria de servicios es $\frac{1}{4}x_1 +\frac{1}{3}x_2 +\frac{1}{2}x_3$. Dado que la economía está en equilibrio, el gasto de la industria de servicios debe ser igual a su ingreso anual $x_1$. Esto genera la primera de las siguientes ecuaciones; las otras dos ecuaciones se obtienen al analizar los gastos de las industrias de electricidad y petróleo.

[Imagen: Ecuaciones: Servicios $\tfrac14x_1+\tfrac13x_2+\tfrac12x_3=x_1$; Electricidad $\tfrac14x_1+\tfrac13x_2+\tfrac14x_3=x_2$; Petróleo $\tfrac12x_1+\tfrac13x_2+\tfrac14x_3=x_3$.]

Al ordenar cada ecuación, se obtiene un sistema homgéneo de ecuaciones lineales, que se resuelven:

[Imagen: Sistema homogéneo $-\tfrac34x_1+\tfrac13x_2+\tfrac12x_3=0$, $\tfrac14x_1-\tfrac23x_2+\tfrac14x_3=0$, $\tfrac12x_1+\tfrac13x_2-\tfrac34x_3=0$ → rref $\left(\begin{smallmatrix}1&0&-1&|&0\\0&1&-3/4&|&0\\0&0&0&|&0\end{smallmatrix}\right)$.]

Al hacer $x_3 =t$ se obtiene que $x_1 =t$ y $x_2 =\frac{3}{4}t$. Por tanto, los outputs relativos de las industrias de servicios, electricidad y petróleo deben estar en las proporciones $x_1 :x_2 :x_3 =4:3:4$ para que la economía esté en equilibrio. Este ejemplo ilustra lo que comúnmente se conoce como modelo cerrado de Leontief.

Veamos cómo abordar esto con Matlab. Las ecuaciones del sistema lineal homogéneo anterior pueden escribirse en la forma: $\left(I-C\right)\mathit{\mathbf{x}}=0$ donde $C$ es la matriz:

$C=\left\lbrack \begin{array}{ccc}
\frac{1}{4} & \frac{1}{3} & \frac{1}{2}\\
\frac{1}{4} & \frac{1}{3} & \frac{1}{4}\\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4}
\end{array}\right\rbrack$ y la matriz $\left(I-C\right)\;$es la matriz de coeficientes del sistema homogéneo correspondiente. Lo resolvemos en Matlab:

```matlab
C = [1/4 1/3 1/2;1/4 1/3 1/4;1/2 1/3 1/4];
[n,~] = size(C); % Asignamos a la variable n la dimension de la matriz C (cuadrada)
I = eye(n); % Creamos la matriz identidad de orden n
IC = I - C;
```

Verificamos que se trata de una economía cerrada sumando sus columnas y comprobando que todas ellas suman 1:

```matlab
Col = sum(C); % El comando sum por defecto genera un vector fila con la suma de las columnas de la matriz
[n,~] = size(C); % Para hacerlo más genérico
if sum(Col) == n % Se cumple cuando cada suma de columnas es 1
    fprintf('Se trata de una economía cerrada')
else
    frpintf('Es una economía abierta')
end
```

**Salida:**
```text
Se trata de una economía cerrada
```

Ahora vamos a resolver el sistema homogéneo que será compatible indeterminado por lo que deberemos asignar un valor a la variable libre que se corresponderá con la columna que no tenga pivote (la/s última/s)

```matlab
S = rref(IC)
```

**Salida:**
```text
S =
1.0000  0  -1.0000
0  1.0000  -0.7500
0  0  0
```

Asignamos el valor $-1$ al elemento $\left(3,3\right)$ de S, extraemos la ultima columna de S en la variable s (vector columna) y dividimos sus elementos por el menor de ellos.

```matlab
S(3,3) = -1;
s = S(:,3);
s = s/min(s)
```

**Salida:**
```text
s =
1.0000
0.7500
1.0000
```

Como se observa, las componentes del vector columna s obtenido guardan la misma proporción calculada anteriormente.

Dado que los outputs corresponden a ingresos, también se puede considerar a $x_1 ,x_2$ y $x_3$ como precios de los tres artículos.

Ahora se modifica el modelo del ejemplo anterior para estudiar una economía abierta, una en la que haya tanto demanda externa como interna por los artículos que se producen. No es de sorprender que esta versión se conozca como modelo abierto de Leontief.

Ejemplo 2. Economía abierta

Consideremos las tres industrias del ejemplo 1, pero con consumo dado por la tabla siguiente. Se ve que, de los artículos producidos por la industria de servicios, 20% los consume la industria de servicios, 40% la industria eléctrica y 10% la industria petrolera. Por tanto, sólo 70% del output de la industria de servicios lo consume esta economía. La implicación de este cálculo es que hay un exceso de output (ingreso) sobre el input (gasto) para la industria de servicios. Se dice que la industria de servicios es productiva. Del mismo modo, la industria petrolera es productiva, pero la industria eléctrica es no productiva. (Esto se refleja en el hecho de que las sumas de la primera y tercera columnas son menos que 1, pero la suma de la segunda columna es igual a 1.) El exceso de output puede aplicarse para satisfacer una demanda externa.

[Imagen: Tabla de Leontief (economía abierta): consumido por / producido por Servicios, Electricidad, Petróleo: Servicios 0.20, 0.50, 0.10; Electricidad 0.40, 0.20, 0.20; Petróleo 0.10, 0.30, 0.30.]

Supongamos que hay una demanda externa anual (en millones de dólares) de 10, 10 y 30 de las industrias de servicios, eléctrica y petrolera, respectivamente. Entonces, al igualar los gastos (demanda interna y demanda externa) con el ingreso (output), se obtienen las siguientes ecuaciones:

[Imagen: Ecuaciones output = demanda interna + demanda externa: $x_1=0.2x_1+0.5x_2+0.1x_3+10$; $x_2=0.4x_1+0.2x_2+0.2x_3+10$; $x_3=0.1x_1+0.3x_2+0.3x_3+30$.]

Escritas en forma matricial se tiene:

$$\mathit{\mathbf{x}}=\mathit{\mathbf{C}}\cdot \mathit{\mathbf{x}}+\mathit{\mathbf{d}}\Longrightarrow \left(I-C\right)\mathit{\mathbf{x}}=\mathit{\mathbf{d}}\Longrightarrow \mathit{\mathbf{x}}={\left(I-C\right)}^{-1} \mathit{\mathbf{d}}$$

A la ecuación $\mathit{\mathbf{x}}=\mathit{\mathbf{C}}\cdot \mathit{\mathbf{x}}+\mathit{\mathbf{d}}$ se le denomina ecuación de Leontief y a la matriz $I-C$ matriz de Leontief

donde:

[Imagen: $C=\begin{pmatrix}0.2&0.5&0.1\\0.4&0.2&0.2\\0.1&0.3&0.3\end{pmatrix}$, $\mathbf x=(x_1,x_2,x_3)^T$, $\mathbf d=(10,10,30)^T$.]

La matriz $C$ se llama matriz de consumo o matriz de tecnología, $\mathit{\mathbf{x}}$ es el vector de producción, y $\mathit{\mathbf{d}}$ es el vector de demanda. En general, si $C=\left\lbrack c_{\textrm{ij}} \right\rbrack ,\mathit{\mathbf{x}}=\left\lbrack x_i \right\rbrack$ y $d=\left\lbrack d_i \right\rbrack$entonces $c_{\textrm{ij}}$representa el valor en dólares del output de la industria $i$ que se necesita para producir un dólar de output de la industria $j$, $x_i$ es el valor monetario (precio) del output de la industria $i$, y $d_i$es el valor monetario de la demanda externa para el output de la industria $i$. Una vez más, se está interesado en encontrar un vector de producción $\mathit{\mathbf{x}}$ con componentes no negativas. Por tanto, el problema importante a resolver en economía es el de determinar las condiciones bajo las cuales la ecuación de Leontief posee soluciones no negativas. A tal vector $\mathit{\mathbf{x}}$ se le llama solución factible. Es evidente que dicho vector existirá siempre que el sistema $\mathit{\mathbf{x}}=C\cdot \mathit{\mathbf{x}}-\mathit{\mathbf{d}}$ tenga solución, o lo que es lo mismo, siempre que la matriz $\left(I-C\right)$ tenga inversa aunque esta condición no es suficiente para garantizar que el vector $\mathit{\mathbf{x}}$ sea positivo.

Resolviendo el ejemplo mediante Matlab:

```matlab
C = [0.2 0.5 0.1;0.4 0.2 0.2;0.1 0.3 0.3];
d = [10;10;30];
[n,~] = size(C);
I = eye(n);
IC = I - C;
x = (I-C) \ d;
fprintf('El precio del sector Servicios es de %4.2f millones de $\n',x(1))
fprintf('El precio del sector Eléctrico es de %4.2f millones de $\n',x(2))
fprintf('El precio del sector Petrolero es de %4.2f millones de $\n',x(3))
```

**Salida:**
```text
El precio del sector Servicios es de 61.74 millones de $
El precio del sector Eléctrico es de 63.04 millones de $
El precio del sector Petrolero es de 78.70 millones de $
```

Es evidente observando la ecuación $\mathit{\mathbf{x}}={\left(I-C\right)}^{-1} \mathit{\mathbf{d}}$ que si la matriz $I-C$ es invertible y si ${\left(I-C\right)}^{-1}$ tiene todos sus elementos no negativos, entonces para cada vector demanda  el vector producción  correspondiente también tendrá todos sus elementos no negativos y por tanto, será un vector de producción válido para la economía. Eso es debido a que el vector demanda $\mathit{\mathbf{d}}$ siempre es positivo.Economías para las que la matriz ${\left(I-C\right)}^{-1}$ tiene todos sus elementos no negativos se llaman economías productivas. Dichas economías son deseables ya que la demanda siempre puede satisfacerse mediante ciertos niveles de producción. El siguiente teorema, cuya deducción puede encontrarse en cualquier libro de economía, establece las condiciones bajo las cuales una economía abierta es productiva:

Teorema: Si $C$ es la matriz de consumo de una economía abierta y si la suma de los elementos de todas sus columnas o de todas sus filas es menor que 1, entonces la matriz $I-C$ es invertible, los elementos de   ${\left(I-C\right)}^{-1}$ son todos positivos y la economía es productiva.

En el ejemplo anterior, veamos cuál es la suma de las columnas de $C$ para saber si se trata de una economía  productiva:

```matlab
% Calculamos el vector suma de las columnas de C
SC = sum(C)
% Vemos la matriz (I-C)^-1
inv(IC)
```

**Salida:**
```text
SC =
0.7000  1.0000  0.6000
ans =
2.1739  1.6522  0.7826
1.3043  2.3913  0.8696
0.8696  1.2609  1.9130
```

Se observa que la suma de los elementos de la 2ª columna de C es 1, sin embargo el vector suma de las filas de $C$ tiene todos sus elementos menores que 1, por lo tanto se trata de una matriz productiva.

Si nos encontráramos con una matriz $C$ con muchos elementos podríamos emplear Matlab para saber si la matriz es productiva, lo vemos con el ejemplo anterior:

```matlab
[n,~] = size(C);
Sumfila = sum(C, 2);   % suma de cada fila
SumCol = sum(C, 1);   % suma de cada columna

% Verificar condición: todas las filas < 1  O  todas las columnas < 1
if all(Sumfila < 1) || all(SumCol < 1)
    fprintf('La economía es productiva\n');
else
    fprintf('La economía no es productiva\n');
end
```

**Salida:**
```text
La economía es productiva
```

Tambien podemos comprobar que todos los elementos de ${\left(I-C\right)}^{-1}$ son positivos:

```matlab
if all(C(:) > 0)
    % todos los elementos son > 0
    disp('La economía es productiva');
else
    disp('La economía puede no ser productiva');
end
```

**Salida:**
```text
La economía es productiva
```

P06.01 Ejemplo 2.4.9 del libro pags 109 - 111

Realizamos los cálculos en millones tal como lo da el enunciado

Creamos la matriz $C$ de demanda interna

```matlab
clc, clear
C1 = [0.17 0.004 0 0.029 0 0.008];
C2 = [0.003 0.295 0.018 0.002 0.004 0.016];
C3 = [0.025 0.173 0.46 0.007 0.011 0.007];
C4 = [0.348 0.037 0.021 0.403 0.011 0.048];
C5 = [0.007 0.001 0.029 0.025 0.358 0.025];
C6 = [0.12 0.074 0.104 0.123 0.173 0.234];
C = [C1;C2;C3;C4;C5;C6];
C
```

**Salida:**
```text
C =
0.1700  0.0040  0  0.0290  0  0.0080
0.0030  0.2950  0.0180  0.0020  0.0040  0.0160
0.0250  0.1730  0.4600  0.0070  0.0110  0.0070
0.3480  0.0370  0.0210  0.4030  0.0110  0.0480
0.0070  0.0010  0.0290  0.0250  0.3580  0.0250
0.1200  0.0740  0.1040  0.1230  0.1730  0.2340
```

Creamos el vector columna de demanda externa

```matlab
d = [99.64;75.548;14.444;33.501;23.527;263.985];
```

Resolvemos la ecuación $\left(I-C\right)\cdot \mathit{\mathbf{x}}=\mathit{\mathbf{d}}$

```matlab
I = eye(6);
IC = I - C;
x = (I - C)\d;
```

Damos los resultados

```matlab
e = ["NMT" "  M" " MB" "NMB" "  E" "  S"];
for i = 1:6
    fprintf('La producción del sector %s es de %-.6f miles de millones de $\n',e(i),x(i))
end
```

**Salida:**
```text
La producción del sector NMT es de 131.028369 miles de millones de $
La producción del sector  M es de 120.443727 miles de millones de $
La producción del sector  MB es de 80.644944 miles de millones de $
La producción del sector NMB es de 178.679232 miles de millones de $
La producción del sector  E es de 65.657018 miles de millones de $
La producción del sector  S es de 431.259170 miles de millones de $
```

P06.02 Economía de Israel

Una versión muy simplificada de una tabla de insumo-producto para la economía de Israel en 1958 divide dicha economía en tres sectores —agricultura, manufactura y energía— con los siguientes resultados:

[Imagen: Tabla de coeficientes (Agricultura, Manufactura, Energía): Agricultura 0.293, 0, 0; Manufactura 0.014, 0.207, 0.017; Energía 0.044, 0.010, 0.216.]

a) ¿Cuántas unidades de producción agrícola se requieren para obtener una unidad de producto agrícola? (texto)

b) ¿Cuántas unidades de producción agrícola se requieren para obtener 200000 unidades de productos de esta naturaleza?

c) ¿Cuántas unidades de producción agrícola se requieren para obtener 50000 unidades de energía?

d) ¿Cuántas unidades de energía se requieren para obtener 50000 unidades de productos agrícolas?

e) Si las exportaciones (en miles de € ) en 1958 fueron las siguientes:

[Imagen: Tabla de producción resultante: Agricultura 13 213; Manufactura 17 597; Energía 1 786.]

Determina el valor en €  de los productos agrícolas, la energía y los artículos manufacturados necesarios para hacer funcionar este modelo y exportar el valor establecido de cada producto (redondea el resultado al entero más próximo con el comando fix)

#### 07. CADENAS DE MARKOV

Fundamento teórico del Libro: Tema 9 (web) capítulo 9.3  pags 24 - 43

NOTA IMPORTANTE: En el libro las matrices de probabilidad (P) son tales que sus filas suman 1 de modo que los vectores de estado son vectores fila que se multiplican por la izquierda por P. Sin embargo en la siguiente explicación son las columnas de P las que suman 1 y los vectores de estado son vectores columna que se multiplican por la derecha de P. El resultado es el mismo: ${\left(P\cdot \mathit{\mathbf{x}}\right)}^T ={\mathit{\mathbf{x}}}^T \cdot P^T$. Eres libre de emplear cualquiera de los dos, pero ten cuidado de no mezclarlos

Fundamento teórico:

Proceso de Markov

Supongamos un sistema físico o matemático sometido a un proceso de cambio de tal forma que en un momento dado puede ocupar un número finito de estados. Por ejemplo, el tiempo en una ciudad podría considerarse en uno de los tres posibles estados: soleado, cubierto o lluvioso. O bien un individuo puede encontrarse en cuatro posibles estados emocionales: feliz, triste, enfadado o nervioso. Supongamos que dicho sistema cambia con el tiempo de un estado a otro y que en determinados períodos de tiempo se observa el estado en que se encuentra. Si el estado del sistema en una observación no se puede predecir con certeza, pero puede predecirse la probabilidad de que se encuentre en un estado determinado sabiendo en qué estado se encontraba en la observación anterior, entonces el proceso de cambio se denomina cadena de Markov o proceso de Markov.

Definición 1. Si una cadena de Markov posee $k$ posibles estados (numerados como $1,2,\ldotp \ldotp \ldotp ,k$ ) la probabilidad de que el sistema esté en el estado $i$ en cualquier observación después de que estuviera en el estado $j\;$en la observación precedente se denota por $p_{\textrm{ij}}$ y se denomina probabilidad de transición del estado $j$ al estado $i$. La matriz $P=\left\lbrack p_{\textrm{ij}} \right\rbrack$ se denomina matriz de transición de la cadena de Markov.

Por ejemplo, en una cadena de Markov de tres estados, la matriz de transición tiene la forma:

[Imagen: Matriz de transición genérica $P=(p_{ij})$ 3×3: columnas = estado precedente (1, 2, 3), filas = nuevo estado.]

En la que $p_{32}$ es la probabilidad de que el sistema cambie del estado 3 al 2 y $p_{11}$ es la probabilidad de que el sistema permanezca en el estado 1 después de estar en ese mismo estado.

Ejemplo 1. Matriz de transición de una cadena de Markov

Una agencia de alquiler de vehículos dispone de tres centros designados por 1, 2 y 3. Un cliente puede alquilar un coche en cualquiera de los tres centros y devolverlo en cualquiera de ellos. El gerente determinó que los clientes devolvían los coches en los distintos locales de acuerdo con las siguientes probabilidades:

[Imagen: Matriz de transición alquiler (columnas: centro de recogida 1–3; filas: centro de devolución): $\begin{pmatrix}.8&.3&.2\\.1&.2&.6\\.1&.5&.2\end{pmatrix}$.]

Esta es la matriz de transición del sistema considerado como una cadena de Markov. En ella se observa, por ejemplo, que la probabilidad de recoger el vehículo en el centro 3 y devolverlo en el 2 es de 0.6.

Ejemplo 2. Matriz de transición de una cadena de Markov

Revisando los libros de donaciones de la Asociación de antiguos alumnos de un instituto se observa que el 80% de los miembros que contribuyeron un año lo hicieron también el siguiente y el 30% de los que no contribuyeron sí lo hicieron el año siguiente. Esta situación puede representarse mediante una cadena de Markov con dos estados:

a) El estado 1 corresponde a los alumnos que pagan un año

b) El estado 2 corresponden a los alumnos que no pagan ese año.

La matriz de transición es: $P=\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack$

En los ejemplos anteriores las matrices de transición poseen la propiedad de que los elementos de sus columnas suman 1. Esto no es un hecho accidental. Si $P=\left\lbrack p_{\textrm{ij}} \right\rbrack$ es la matriz de transición de una cadena de Markov con $k$ estados, entonces para cada $j$ (columna) debemos tener:

$p_{1j} +p_{2j} +\ldotp \ldotp \ldotp +p_{\textrm{kj}} =1$             (1)

ya que si el sistema está en el estado $j$ en cualquier observación es seguro que estará en cualquiera de los $k$ estados posibles en la siguiente.

Una matriz con la propiedad (1) se denomina matriz estocástica, matriz de probabilidad o matriz de Markov. De lo visto hasta ahora se deduce que una matriz de transición de una cadena de Markov debe ser una matriz estocástica.

En una cadena de Markov el estado del sistema en cualquier momento en que se observe no puede determinarse con certeza. Lo mejor que se puede hacer es determinar las probabilidades para cada uno de los estados posibles. Por ejemplo, en una cadena de Markov con tres estados describiremos el posible estado del sistema en una observación mediante el vector columna: $\mathit{\mathbf{x}}=\left\lbrack \begin{array}{c}
x_1 \\
x_2 \\
x_3
\end{array}\right\rbrack$. En el que $x_i$ representa la probabilidad de que el sistema se encuentre en el estado $i$. En general podemos establecer la siguiente definición.

Definición 2. El vector de estado para una observación de una cadena de Markov con $k$ estados es un vector columna cuyo elemento $i-\textrm{esimo}$ representa la probabilidad de que el sistema se encuentre en el estado $i$ en ese momento.

Obsérvese que los elementos de cualquier vector de estado son no negativos y suman 1. Un vector columna con dichas propiedades se denomina vector de probabilidad.

Supongamos ahora que conocemos el vector de estado ${\mathit{\mathbf{x}}}^{\left(0\right)}$ de una cadena de Markov en la observación inicial. El siguiente teorema nos permitirá determinar los vectores de estado en observaciones subsiguientes (${\mathit{\mathbf{x}}}^{\left(1\right)}$, ${\mathit{\mathbf{x}}}^{\left(2\right)}$, ..., $\left.{\mathit{\mathbf{x}}}^{\left(n\right)} ,\ldotp \ldotp \ldotp \right)$

Teorema 1. Si $P$ es una matriz de transición en una cadena de Markov y  ${\mathit{\mathbf{x}}}^{\left(n\right)}$ es el vector de estado en la enésima observación, entonces ${\mathit{\mathbf{x}}}^{\left(n+1\right)} =P{\mathit{\mathbf{x}}}^{\left(n\right)}$.

De este teorema se sigue que:

$${\mathit{\mathbf{x}}}^{\left(1\right)} =P{\mathit{\mathbf{x}}}^{\left(0\right)}$$

$${\mathit{\mathbf{x}}}^{\left(2\right)} =P{\mathit{\mathbf{x}}}^{\left(1\right)} =P^2 {\mathit{\mathbf{x}}}^{\left(0\right)}$$

$${\mathit{\mathbf{x}}}^{\left(3\right)} =P{\mathit{\mathbf{x}}}^{\left(2\right)} =P^3 {\mathit{\mathbf{x}}}^{\left(0\right)}$$

.....

$${\mathit{\mathbf{x}}}^{\left(n\right)} =P{\mathit{\mathbf{x}}}^{\left(n-1\right)} =P^n {\mathit{\mathbf{x}}}^{\left(0\right)}$$

De esta forma el vector de estado inicial ${\mathit{\mathbf{x}}}^{\left(0\right)}$ y la matriz de transición $P$ determinan el vector de estado ${\mathit{\mathbf{x}}}^{\left(n\right)}$ para $n=1,2,\ldotp \ldotp \ldotp$

Ejemplo 3. Ejemplo 2 revisado.

La matriz de transición del ejemplo 2 era: $P=\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack$

Creamos ahora el registro de donaciones de un nuevo graduado que no ha pagado el primer año después de su graduación. Para dicho graduado, el sistema se encuentra inicialmente en el estado 2 con seguridad por lo que el vector de estado inicial es: ${\mathit{\mathbf{x}}}^{\left(0\right)} =\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack$. Del teorema anterior tenemos que:

$${\mathit{\mathbf{x}}}^{\left(1\right)} =P{\mathit{\mathbf{x}}}^{\left(0\right)} =\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\ldotp 30\\
0\ldotp 70
\end{array}\right\rbrack$$

$${\mathit{\mathbf{x}}}^{\left(2\right)} =P{\mathit{\mathbf{x}}}^{\left(1\right)} =\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
0\ldotp 30\\
0\ldotp 70
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\ldotp 45\\
0\ldotp 55
\end{array}\right\rbrack$$

$${\mathit{\mathbf{x}}}^{\left(3\right)} =P{\mathit{\mathbf{x}}}^{\left(2\right)} =\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
0\ldotp 45\\
0\ldotp 55
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\ldotp 525\\
0\ldotp 475
\end{array}\right\rbrack$$

Así, después de tres años la probabilidad de que el alumno pague es de 0.525 (52,5%). Si continuamos más allá de los tres años obtenemos los siguientes vectores de estado (con tres cifras decimales):

[Imagen: Iteraciones de Markov: $x^{(4)}=(.563,.438)$, $x^{(5)}=(.581,.419)$, $x^{(6)}=(.591,.409)$, $x^{(7)}=(.595,.405)$, $x^{(8)}=(.598,.402)$, $x^{(9)}=(.599,.401)$, $x^{(10)}=(.599,.401)$, $x^{(11)}=(.600,.400)$.]

Para todo $n>11$ obtenemos el mismo vector de estado ${\mathit{\mathbf{x}}}^{\left(n\right)} =\left\lbrack \begin{array}{c}
0\ldotp 6\\
0\ldotp 4
\end{array}\right\rbrack$

Nota: esto no es ectrictamente cierto, basta hacer los cálculos con Matlab para ver que, por ejemplo, entre el vector de estado 11 y 12 hay una diferencia del orden de ${10}^{-4}$ como se ve a continuación:

```matlab
clc, clear
P = [0.8 0.3;0.2 0.7]
x0 = [0;1]
P14 = P^14*x0
P15 = P^15*x0
dif = P15 - P14
norm(dif)
```

**Salida:**
```text
P =
0.8000  0.3000
0.2000  0.7000
x0 =
P14 =
0.6000
0.4000
P15 =
0.6000
0.4000
dif =
1.0e-04 *

0.1831
-0.1831
ans =
2.5895e-05
```

En otras palabras, los vectores estado convergen a un vector fijo a medida que las observaciones aumentan.

Ejemplo 4. Ejemplo 1 revisado

La matriz de transición del ejemplo 1 era: $\left\lbrack \begin{array}{ccc}
0\ldotp 8 & 0\ldotp 3 & 0\ldotp 2\\
0\ldotp 1 & 0\ldotp 2 & 0\ldotp 6\\
0\ldotp 1 & 0\ldotp 5 & 0\ldotp 2
\end{array}\right\rbrack$

Si se recoge el coche en el local 2, el vector de estado inicial es: ${\mathit{\mathbf{x}}}^{\left(0\right)} =\left\lbrack \begin{array}{c}
0\\
1\\
0
\end{array}\right\rbrack$. A partir de este vector aplicamos el teorema anterior repetidamente y obtenemos los vectores de estados representados en la siguiente tabla:

[Imagen: Tabla de evolución $x^{(n)}$ para n = 0…11: $x_1$: 0, .300, .400, .477, .511, .533, .544, .550, .553, .555, .556, .557; $x_2$: 1, .200, .370, .252, .261, .240, .238, .233, .232, .231, .230, .230; $x_3$: 0, .500, .230, .271, .228, .227, .219, .217, .215, .214, .214, .213.]

Para valores de $n$ mayores que 11 todos los vectores estado son iguales al vector ${\mathit{\mathbf{x}}}^{\left(11\right)}$ hasta la tercera cifra decimal. (Pasa exactamente lo mismo que antes)

En este ejemplo observamos dos cosas:

- Que no ha sido necesario saber durante cuánto tiempo el cliente alquiló el coche, es decir, en un proceso de Markov el tiempo que pasa entre observaciones no es necesario que siempre sea el mismo.

- Que los vectores de estado tienden hacia uno fijo a medida que aumenta el número de observaciones, al igual que en el ejemplo 1.

Comportamiento límite de los vectores de estado

En los ejemplos anteriores hemos visto que los vectores de estado se aproximan a un vector fijo a medida que el número de observaciones aumenta. Nos preguntamos ahora si este comportamiento se producirá siempre. Un ejemplo sencillo nos mostrará que no es así.

Ejemplo 5. Un sistema que oscila entre dos vectores de estado

Sean: $P=\left\lbrack \begin{array}{cc}
0 & 1\\
1 & 0
\end{array}\right\rbrack$y ${\mathit{\mathbf{x}}}^{\left(0\right)} =\left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack$.

En este caso, como $P^2 =I$ y $P^3 =P$, tenemos que: ${\mathit{\mathbf{x}}}^{\left(0\right)} ={\mathit{\mathbf{x}}}^{\left(2\right)} ={\mathit{\mathbf{x}}}^{\left(4\right)} =\left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack$y, por otro lado: ${\mathit{\mathbf{x}}}^{\left(1\right)} ={\mathit{\mathbf{x}}}^{\left(3\right)} ={\mathit{\mathbf{x}}}^{\left(5\right)} =\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack$

Es decir, este sistema oscila indefinidamente entre dos vectores de estado no aproximándose a ningún vector de estado fijo.

Sin embargo, si imponemos una leve condición a la matriz de transición vemos que el sistema tiende a un vector de estado fijo:

Definición 3. Una matriz de transición es regular si alguna de sus potencias enteras positivas posee todos sus elementos positivos.

Así, para una matriz de transición regular $P$ existe algún entero positivo $m$ de manera que todos los elementos de $P^m$ son positivos. Es el caso de las matrices de transición de los ejemplos 1 y 2 para $m=1$.

Una cadena de Markov gobernada por una matriz de transición regular se denomina cadena de Markov regular. Veremos que toda cadena de Markov regular posee un vector de estado fijo $\mathit{\mathbf{q}}$ tal que $P^n {\mathit{\mathbf{x}}}^{\left(0\right)}$ se aproxima a $\mathit{\mathbf{q}}$ a medida que $n$ aumenta para cualquier vector de estado inicial ${\mathit{\mathbf{x}}}^{\left(0\right)}$.

Teorema 2. Comportamiento de $P^n$ cuando $n\to \infty$

Si $P$ es una matriz de transición regular, entonces cuando $n\to \infty$:

$P^n \to \left\lbrack \begin{array}{cccc}
q_1  & q_1  & \cdots  & q_1 \\
q_2  & q_2  & \cdots  & q_2 \\
\vdots  & \vdots  & \vdots  & \vdots \\
q_k  & q_k  & \cdots  & q_k
\end{array}\right\rbrack$donde $q_i$ son todos positivos y cumplen que: $q_1 +q_2 +\ldotp \ldotp \ldotp +q_k =1$

Definamos: $Q=\left\lbrack \begin{array}{cccc}
q_1  & q_1  & \cdots  & q_1 \\
q_2  & q_2  & \cdots  & q_2 \\
\vdots  & \vdots  & \vdots  & \vdots \\
q_k  & q_k  & \cdots  & q_k
\end{array}\right\rbrack$ y $\mathit{\mathbf{q}}=\left\lbrack \begin{array}{c}
q_1 \\
q_2 \\
\vdots \\
q_k
\end{array}\right\rbrack$

$Q\;$es una matriz de transición cuyas columnas son iguales al vector de probabilidad $\mathit{\mathbf{q}}$. $Q$ posee la propiedad de que si $\mathit{\mathbf{x}}$ es cualquier vector de probabilidad entonces:

[Imagen: Demostración: si todas las columnas de Q son iguales a $\mathbf q$ y $x_1+\dots+x_k=1$, entonces $Q\mathbf x=(x_1+\dots+x_k)\mathbf q=\mathbf q$.]

Es decir, $Q$ transforma cualquier vector de probabilidad $\mathit{\mathbf{x}}$ en el vector fijo de probabilidad $\mathit{\mathbf{q}}$, lo que nos lleva al siguiente teorema:

Teorema 2. Comportamiento de $P^n \mathit{\mathbf{x}}$ cuando $n\to \infty$

Si $P$ es una matriz de transición regular y $\mathit{\mathbf{x}}$ cualquier vector de probabilidad, cuando $n\to \infty$ se tiene que: $P^n \cdot \mathit{\mathbf{x}}\to \left\lbrack \begin{array}{c}
q_1 \\
q_2 \\
\vdots \\
q_k
\end{array}\right\rbrack =\mathit{\mathbf{q}}$

donde $\mathit{\mathbf{q}}$ es un vector de probabilidad fijo, independiente de $n$, cuyos elementos son positivos.

Combinándolo con el teorema 2 obtenemos que $P^n \cdot \mathit{\mathbf{x}}\to \mathit{\mathbf{Q}}\cdot \mathit{\mathbf{x}}\;$ cuando $n\to \infty$. El vector $\mathit{\mathbf{q}}$ se denomina vector de estado estacionario o vector de equilibrio de una cadena de Markov regular.

Para sistemas con varios estados la forma más efectiva de calcular el vector de estado estacionario consiste en calcular $P^n \cdot \mathit{\mathbf{x}}$ para valores de $n$ grandes. El siguiente teorema nos proporciona otra forma de calcularlo.

Teorema 4. Vector de estado estacionario.

El vector de estado estacionario $\mathit{\mathbf{q}}$ de una matriz de transición regular $P$ es el único vector de probabilidad que satisface la ecuación $P$$\cdot \;\mathit{\mathbf{q}}\;=\mathit{\mathbf{q}}$

Para verlo consideremos la igualdad matricial $P{\cdot P}^n =P^{n+1}$. Por el teorema 2, tanto $P^n$ como $P^{n+1}$ se aproximan a $Q$ cuando $n\to \infty$. Sustituyendo en la igualdad anterior obtenemos $P\cdot Q=Q$. Cualquiera de las columnas de esta ecuación matricial da $P\;\cdot \mathit{\mathbf{q}}=\mathit{\mathbf{q}}$. Para ver que $\mathit{\mathbf{q}}$ es el único vector de probabilidad que satisface esta ecuación, supongamos que $\mathit{\mathbf{r}}$ es otro vector de probabilidad que cumple que $P\cdot \;\mathit{\mathbf{r}}=\mathit{\mathbf{r}}$. Entonces también se cumplirá que $P^n \cdot \mathit{\mathbf{r}}=\mathit{\mathbf{r}}$ para $n=1,2,\ldotp \ldotp \ldotp$. Si hacemos que $n\to \infty$ , por el teorema 3 obtenemos que $\mathit{\mathbf{q}}=\mathit{\mathbf{r}}$.

El teorema 4 puede expresarse también diciendo que el sistema lineal homogéneo $\left(I-P\right)\;\mathit{\mathbf{q}}=0$ tiene como solución única el vector $\mathit{\mathbf{q}}$ cuyos elementos son todos no negativos y cumplen $q_1 +q_2 +\ldotp \ldotp \ldotp +q_k =1$.  Se observa que el vector $\mathit{\mathbf{q}}$ es un autovector de la matriz  $P$ asociado al autovalor $\lambda =1$.

Podemos aplicar esta técnica para calcular los vectores de estado estacionario de algunos ejemplos anteriores.

P07.01 Ejemplo 2 revisado

En el ejemplo 2 la matriz de transición era: $P=\left\lbrack \begin{array}{cc}
0\ldotp 8 & 0\ldotp 3\\
0\ldotp 2 & 0\ldotp 7
\end{array}\right\rbrack$

Por lo que el sistema homogéneo $\left(I-P\right)\;\mathit{\mathbf{q}}=0$ es: $\left\lbrack \begin{array}{cc}
0\ldotp 2 & -0\ldotp 3\\
-0\ldotp 2 & 0\ldotp 3
\end{array}\right\rbrack \cdot \left\lbrack \begin{array}{c}
q_1 \\
q_2
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\\
0
\end{array}\right\rbrack$

que se reduce a la única ecuación: $0\ldotp 2\;q_1 -0\ldotp 3q_2 =0\Longrightarrow q_1 =1\ldotp 5\;q_2$

Tomando $q_2 =s$ como variable libre, las soluciones se pueden expresar como: $\mathit{\mathbf{q}}=s\left\lbrack \begin{array}{c}
1\ldotp 5\\
1
\end{array}\right\rbrack$

Para hacer que $\mathit{\mathbf{q}}$ sea un vector de probabilidad tomamos $s=\frac{1}{1\ldotp 5+1}=0\ldotp 4$, por tanto el vector de estado estacionario buscado es: $\mathit{\mathbf{q}}=\left\lbrack \begin{array}{c}
0\ldotp 6\\
0\ldotp 4
\end{array}\right\rbrack$. Es decir, a largo plazo, el 60% de los alumnos pagarán y el 40% no.

Veamos cómo podemos aplicar la teoría de autovalores para resolver el ejemplo con Matlab (se recomienda leer el menu de ayuda de Matlab del comando eig)

```matlab
P = [0.8 0.3;0.2 0.7];
[V,D] = eig(P)
```

**Salida:**
```text
V =
0.8321  -0.7071
0.5547  0.7071
D =
1.0000  0
0  0.5000
```

En general, Matlab no situa el autovalor 1 en una posición concreta, por lo que debemos buscarlo en la matriz D

```matlab
% Buscamos la columna de D donde se encuentra el autovalor 1
for i = 1:2
  if  D(i,i) == 1 % esto es muy peligroso porque puede no ser cero, mejor (D(i,i) - 1)<error,
      % donde error es una medida del error que establecemos (por ejemplo 10^-10)
      k = i;
  end
end
% Extraemos la columna de V que se corresponde con la posición obtenida
% anteriormente y normalizamos (dividimos por la suma de sus componentes)
% para obtener el vector de estado estacionario q
q = V(:,k);
q = q/sum(q)
```

**Salida:**
```text
q =
0.6000
0.4000
```

P07.02. Ejemplo 1 revisado

En el ejemplo 1 la matriz de transición era: $P=\left\lbrack \begin{array}{ccc}
0\ldotp 8 & 0\ldotp 3 & 0\ldotp 2\\
0\ldotp 1 & 0\ldotp 2 & 0\ldotp 6\\
0\ldotp 1 & 0\ldotp 5 & 0\ldotp 2
\end{array}\right\rbrack$, por lo que el sistema lineal homogéneo $\left(I-P\right)\;\mathit{\mathbf{q}}=0$ es:

$\left\lbrack \begin{array}{ccc}
0\ldotp 2 & -0\ldotp 3 & -0\ldotp 2\\
-0\ldotp 1 & 0\ldotp 8 & -0\ldotp 6\\
-0\ldotp 1 & -0\ldotp 5 & 0\ldotp 8
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
q_1 \\
q_2 \\
q_3
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\\
0\\
0
\end{array}\right\rbrack$. Resolvemos el sistema por el método de Gauss-Jordan la matriz escalonada reducida equivalente a la matriz de coeficientes es:

$\left\lbrack \begin{array}{ccc}
1 & 0 & -\frac{34}{13}\\
0 & 1 & -\frac{14}{13}\\
0 & 0 & 0
\end{array}\right\rbrack$. Tomando $q_3 =s\;$como variable libre, el conjunto solución se expresa como: $\mathit{\mathbf{q}}=s\cdot \left\lbrack \begin{array}{c}
\frac{34}{13}\\
\frac{14}{13}\\
1
\end{array}\right\rbrack$. Para que $\mathit{\mathbf{q}}$ sea un vector de probabilidad, debemos tomar $s=\frac{1}{\frac{34}{13}+\frac{14}{13}+1}=\frac{13}{61}$. Por lo que el vector de estado estacionario del sistema es:

$$\mathit{\mathbf{q}}=\left\lbrack \begin{array}{c}
\frac{34}{61}\\
\frac{14}{61}\\
\frac{13}{61}
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
0\ldotp 5573\ldotp \ldotp \ldotp \\
0\ldotp 2295\ldotp \ldotp \ldotp \\
0\ldotp 2131\ldotp \ldotp \ldotp
\end{array}\right\rbrack$$

El script de Matlab para el cálculo del vector estacionario $\mathit{\mathbf{q}}$ es:

```matlab
clc, clear
P = [0.8 0.3 0.2;0.1 0.2 0.6;0.1 0.5 0.2];
q1 = null(eye(3)-P); % el comando null calcula el núcleo de la matriz
q = q1 / sum(q1)
```

**Salida:**
```text
q =
0.5574
0.2295
0.2131
```

Podemos comprobar que se cumple: $P\cdot \mathit{\mathbf{q}}=\mathit{\mathbf{q}}$:

```matlab
P * q - q
```

**Salida:**
```text
ans =
1.0e-16 *

-0.2776
0.5551
```

Obsérvese que $\left(P\cdot \mathit{\mathbf{q}}-\mathit{\mathbf{q}}\right)$ no es exactamente cero por errores de redondeo en el cálculo

También podemos calcularlo mediante autovalores:

```matlab
[V,D] = eig(P)
for i = 1:3
  if  (D(i,i) - 1) < 1e-10 % error 10^-10
      k = i;
  end
end
q1 = V(:,k);
q1 = q1/sum(q1)
```

**Salida:**
```text
V =
0.8718  0.8161  0.0784
0.3590  -0.4308  -0.7431
0.3333  -0.3853  0.6646
D =
1.0000  0  0
0  0.5472  0
0  0  -0.3472
q1 =
1.0e+15 *

0.7066
-6.6929
5.9863
```

Los vectores de estado estacionario son casi iguales:

```matlab
q - q1
```

**Salida:**
```text
ans =
1.0e+15 *

-0.7066
6.6929
-5.9863
```

P07.01 Ejemplo 9.3.3 del tema 9 del libro (web) pag 27

La empresa de banquetes Gourmet tiene 40% del negocio de banquetes en una cierta ciudad mediana. Su única competencia, Delicious Foods Services (DFS) tiene el otro 60%. Para ser más competitiva, Gourmet contrata a una agencia de publicidad para impulsar su imagen. Durante una amplia campaña publicitaria se recopilaron las cifras de ventas mensuales. Se encontró que 90% de los clientes de Gourmet regresan a Gourmet al siguiente mes, mientras que el 20% de los clientes de DFS se cambian a Gourmet.

a) ¿Qué porcentaje de clientes usa cada servicio después de 1 mes?

b) ¿Qué porcentaje usa cada servicio cada 2 meses?

d) ¿Cuál es la cuota de mercado de largo plazo para cada servicio?

Escribimos la matriz de transición

```matlab
clc, clear
T = [0.9 0.1;0.2 0.8]
```

**Salida:**
```text
T =
0.9000  0.1000
0.2000  0.8000
```

Como la empresa Gourmet tiene un 40% del mercado y Delicious Foods Services tiene el 60%, el vector de estado inicial es $p_0 =\left\lbrack 0\ldotp 4\;\;\;0\ldotp 6\right\rbrack$

```matlab
p0 = [0.4 0.6];
```

Nótese que en el libro multiplica el vector de estado (fila) por la izquierda por la matriz de transición: $\mathit{\mathbf{p}}\cdot T$, se obtiene el mismo resultado trasponiendo ambos $T^T \cdot {\mathit{\mathbf{p}}}^T$, notación que veréis en muchos libros.

Calculamos el estado al cabo de un mes:

```matlab
p1 = p0 * T
```

**Salida:**
```text
p1 =
0.4800  0.5200
```

Calculamos el vector de estado al cabo de dos meses, es decir: ${\mathit{\mathbf{p}}}_2 ={\mathit{\mathbf{p}}}_1 \cdot T={\mathit{\mathbf{p}}}_0 \cdot T^2$

```matlab
p2 = p1 * T
```

**Salida:**
```text
p2 =
0.5360  0.4640
```

De igual forma:

```matlab
pp2 = p0 * T^2
```

**Salida:**
```text
pp2 =
0.5360  0.4640
```

Para calcular el vector de estado estacionario creamos un blucle while que se detiene cuando la norma de la diferencia entre dos vectores de estado consecutivos es menor que un error dado, en nuestro caso tomamos ${10}^{-6}$

```matlab
er = 1;
p = p0;
i = 0;
while er > 1e-6
    p = p * T;
    er = norm(p - p0);
    p0 = p;
    i = i + 1;
end
disp(p)
```

**Salida:**
```text
0.6667  0.3333
```

Obtenemos el vector de estado estacionario $\left\lbrack 0\ldotp 6667\;\;\;\;0\ldotp 3333\right\rbrack$ con un error de ${10}^{-6}$ al cabo de 34 meses, es decir, a largo plazo, la marca Gourmet tendrá $\frac{2}{3}\approx 0\ldotp 6667$ del mercado y la marca Delicious Foods Services $\frac{1}{3}\approx 0\ldotp 3333$ del mercado

Podemos comprobar que se trata del vector de estado estacionario calculando el módulo del vector: $\mathit{\mathbf{p}}-\mathit{\mathbf{p}}\cdot T$

```matlab
d = p - p*T;
norm(d)
```

**Salida:**
```text
ans =
6.1226e-07
```

Observamos que la norma del vector es menor que ${10}^{-6}$ como queríamos

También podría calcularse el vector de estado estacionario calculando el autovector que corresponde al autovalor 1 de la matriz de probabilidad transpuesta:

```matlab
[V,D] = eig(T')
```

**Salida:**
```text
V =
0.8944  -0.7071
0.4472  0.7071
D =
1.0000  0
0  0.7000
```

En general, Matlab no situa el autovalor 1 en una posición concreta, por lo que debemos buscarlo en la matriz D

```matlab
% Buscamos la columna de D donde se encuentra el autovalor 1
for i = 1:2
  if  D(i,i) == 1
      k = i;
  end
end
% Extraemos la columna de V que se corresponde con la posición obtenida
% anteriormente y normalizamos (dividimos por la suma de sus componentes)
% para obtener el vector de estado estacionario q
q = V(:,k);
q = q/sum(q)
```

**Salida:**
```text
q =
0.6667
0.3333
```

P07.02. Alquiler de venículos

En Barcelona, una compañía de alquiler de automóviles cuenta con una flota de 2000 coches. El patrón de los lugares de alquiler y devolución se describe en la siguiente tabla. En un día típico ¿cuántos coches estarán alquilados o listos para alquilarse en la oficina situada en el centro de la ciudad? Da el resultado al entero más próximo.

[Imagen: Tabla de transición alquiler de coches (columnas: lugar de alquiler Estación de tren, Centro ciudad, Aeropuerto; filas: lugar de devolución): Estación 0.90, 0.01, 0.09; Centro 0.01, 0.90, 0.01; Aeropuerto 0.09, 0.09, 0.90.]

#### 08.  MOTORES DE BÚSQUEDA EN INTERNET. PAGE-RANK

FUNDAMENTO TEÓRICO

Supongamos que a Alice y a Bob les dan seis páginas de internet que contienen palabras clave de un tema que les interesa a ambos. Cada uno tiene su propia estrategia a la hora de establecer el orden de importancia de las páginas.

Estrategia de Alice

Alice decide que la red de enlaces (referencias) entre las páginas puede ser un medio de medir su importancia relativa, de modo que dibuja un diagrama llamado grafo de web  (webgraph) en el que se muestran los enlaces entre las seis páginas. Un enlace directo de la página  a la página  significa que la  página posee un enlace de salida $i$ hacia la $j$, es decir, referencia esa página.

Alice procede de la siguiente forma:

- Ignora enlaces desde o hacia páginas que no sean las seis consideradas.

- Ignora enlaces de una página a sí misma.

- Ignora enlaces duplicados

- Asume que no existen páginas colgadas, es decir, páginas sin enlaces de salida.

[Imagen: Grafo dirigido de 6 páginas web (1–6) con enlaces entre ellas (modelo PageRank).]

Alice diseña una estrategia de navegación en la web según la cual toma una de las páginas (por ejemplo, la 2) clica en uno de sus enlaces y conecta con otra página. Repite el proceso desde la nueva página navegando de una página a otra. Registra cuántas veces visita cada página después de 10, 100, 1.000, 10.000 y 20.000 clics y lo refleja en una Tabla (Nótese que el número de páginas visitadas es uno más que el número de “clicks”).

[Imagen: Tabla 'Número total de clicks' por página tras 0, 10, 100, 1000, 10000, 20000 clicks: Pág. 1: 0, 3, 21, 165, 1504, 3012; Pág. 2: 1, 2, 16, 148, 1391, 2790; Pág. 3: 0, 3, 27, 271, 2706, 5424; Pág. 4: 0, 0, 4, 100, 1096, 2206; Pág. 5: 0, 2, 22, 155, 1415, 2745; Pág. 6: 0, 1, 11, 162, 1889, 3824.]

También crea otra tabla calculando la fracción de visitas (tanto por 1) a cada página con 4 cifras decimales:

[Imagen: Misma tabla en proporciones: Pág. 1: 0, .2727, .2079, .1648, .1504, .1506; Pág. 2: 1, .1818, .1584, .1479, .1391, .1395; Pág. 3: 0, .2727, .2673, .2707, .2706, .2712; Pág. 4: 0, 0, .0396, .0999, .1096, .1103; Pág. 5: 0, .1818, .2178, .1548, .1415, .1372; Pág. 6: 0, .0909, .1089, .1618, .1889, .1912.]

Basándose en 20.000 repeticiones identifica a la página 3 como la más importante ya que es la más visitada y establece un orden de importancia de las páginas: 3, 6, 1, 2, 5, 4

Intrepretación mediante matrices de Markov

Observamos que para cada página de la  Tabla 2 las cifras tienden a estabilizarse. Esto no es un fenómeno accidental; veremos que en este ejemplo, independientemente de la página que se elija al principio y los enlaces seleccionados posteriormente el %  de visitas a cada página convergerá a un valor límite que depende únicamente de al estructura del grafo de web. Los valores limite de esas fracciones, llamados page ranks pueden emplearse para medir la importancia relativa de las páginas.

Aunque el procedimiento que emplea Alice es apropiado para una red pequeña como la suya, no es factible en grandes grafos de web como internet (www). Para éstos podemos obtener una clasificación como la de Alice empleando cadenas de Markov. Como primer paso para explicar el método se define la matriz de adyacencia de un grafo de web con $n$ páginas como una matriz nxn cuyo elemento $a_{\textrm{ij}}$ es un 1 si la página $j$ posee un enlace hacia la página $i$ y un 0 en caso contrario[1]. Por ejemplo, la matriz de adyacencia del grafo de web de la Figura 1 es:

[Imagen: Matriz de adyacencia de la red de 6 páginas (columnas = salidas, filas = entradas): $A=\begin{pmatrix}0&1&0&0&1&1\\0&0&1&0&1&0\\1&0&0&1&0&1\\0&1&0&0&0&1\\0&1&1&0&0&0\\0&0&1&1&1&0\end{pmatrix}$.]

[1] IMPORTANTE: date cuenta que la matriz de adyacencia de un grafo web es la traspuesta de la matriz de adyacencia que hemos visto al estudiar dígrafos. Sin embargo al calcular el orden de las páginas con la función centrality de Matlab se introduce el digrafo como hemos visto en la sección anterior ya que el algoritmo de Matlab traspone la matriz.

Todo la teoría siguiente puede explicarse de igual forma tomando la matriz de adyacencia del díagrafo, $\left(A^T \right)$ la diferencia es que, para calcular los vectores de estado sucesivos en lugar de multiplicar ${A\cdot \mathit{\mathbf{x}}}^{\left(0\right)}$ multiplkcaríamos ${\mathit{\mathbf{x}}}^{\left(0\right)} \cdot A^T$ siendo${\mathit{\mathbf{x}}}^{\left(0\right)}$ un vector fila

Obsérvese que:

- La suma de los elementos de la fila $i$ representa el numero de enlaces entrantes a la página $i$ procedentes de otras páginas

- La suma de los elementos de la columna $j$ representa el número de enlaces salientes de la página $j$ hacia otras páginas.

Definición 1. Si navegamos a través de un grafo de web con  $n$ páginas, el vector de estado $x^{\left(k\right)}$ es un vector columna de nx1 cuyo elemento $i$ es la probabilidad de que estemos en la página $i$ después de $k$ “clicks”.

Para ilustrar esta idea supongamos que conocemos con certeza que quien navega por la web se encuentra en la página $j$ después de $k$ “clicks”, en cuyo caso el elemento $j$ del vector $x^{\left(k\right)}$  es 1 y todos sus otros elementos son 0. De ello se deduce que el producto  ${\textrm{Ax}}^{\left(k\right)}$ es el vector columna $j$ de la matriz $A$ . Por ejemplo, si sabemos que Alice comienza en la página 2, su vector de estado inicial $x^{\left(0\right)}$  y el producto ${A\cdot \mathit{\mathbf{x}}}^{\left(0\right)}$ sería:

[Imagen: $x^{(0)}=(0,1,0,0,0,0)^T$, $Ax^{(0)}=(1,0,0,1,1,0)^T$.](1)

Los elementos de ${A\cdot x}^{\left(0\right)}$ indican que desde la página 2 puede ir a cualquiera de las páginas 1, 4 ó 5 ya que son las únicas a las que se enlaza la página 2. Suponiendo que Alice elige aleatoriamente cualquiera de los tres enlaces, cada uno de ellos tendrá una probabilidad de $\frac{1}{3}$ de ser elegido.

La siguiente definición formaliza la idea de que Alice elija aleatoriamente un enlace de salida.

Definición 2. La matriz de probabilidad de transición $B=\left\lbrack b_{\textrm{ij}} \right\rbrack$ asociada a una matriz de adyacencia $A=\left\lbrack a_{\textrm{ij}} \right\rbrack$ es la matriz obtenida dividiendo cada elemento de $A$ por la suma de los elementos de la misma columna, es decir:

$$b_{\textrm{ij}} =\frac{a_{\textrm{ij}} }{\sum_{k=1}^n a_{\textrm{kj}} }$$

Es evidente que $0\le b_{\textrm{ij}} \le 1$ y que los elementos de las columnas de $B$ suman 1, como sucede en las matrices de Markov. Como ejemplo la matriz de probabilidad de transición asociada a (1) anterior es:

[Imagen: Matriz de transición normalizada por columnas $B=\begin{pmatrix}0&1/3&0&0&1/3&1/3\\0&0&1/3&0&1/3&0\\1&0&0&1/2&0&1/3\\0&1/3&0&0&0&1/3\\0&1/3&1/3&0&0&0\\0&0&1/3&1/2&1/3&0\end{pmatrix}$.](2)

Esta matriz proporciona la probabilidad al ir navegando de una página a otra. Por ejemplo, si sabemos que Alice está inicialmente en la página 2, su vector de estado con 4 cifras decimales después de un “click” será:

[Imagen: $x^{(1)}=Bx^{(0)}=(1/3,0,0,1/3,1/3,0)^T\approx(0.3333,0,0,0.3333,0.3333,0)^T$.]

Y sus vectores de estado tras sucesivos “clicks” formarán la secuencia:

$x^{\left(k\right)} =Bx^{\left(k-1\right)} ,\;\;\;\;\;k=1,2,3,\ldotp \ldotp \ldotp$   (3)

Se sigue que los sucesivos vectores de estado con 4 cifras decimales serán:

[Imagen: Iteraciones: $x^{(2)}=(.1111,.1111,.5,0,0,.2778)$; $x^{(3)}=(.1296,.1667,.2037,.1296,.2037,.1667)$; $x^{(5)}=(.1533,.1245,.3014,.1121,.1286,.18)$; $x^{(10)}=(.1562,.1366,.27,.1101,.1366,.1905)$; $x^{(15)}=(.1544,.1365,.2727,.109,.1365,.191)$.]

Autovalores de la matriz de transición

Si suponemos que el vector de estado $x^{\left(k\right)}$ tiende hacia un límite $\mathit{\mathbf{x}}$ cuando $k$ (número de “clicks”) aumenta indefinidamente, de (3) se deduce que: $\mathit{\mathbf{x}}=B\;\mathit{\mathbf{x}}$

Es decir, $\mathit{\mathbf{x}}$ es un autovector de $B$ correspondiente al autovalor 1. Recordemos que una matriz estocástica (o de Markov) posee siempre el autovalor $\lambda =1$como dominante, es decir, se cumple que, para todos los demás autovalores de la matriz $\left|\lambda_i \right|<\lambda$

Si normalizamos el vector $\mathit{\mathbf{x}}$ de forma que sus elementos sumen 1, sus elementos se pueden interpretar como la fracción de veces que se espera que cada página sea visitada después de infinitos “clicks”. Por ejemplo, con ayuda de un CAS[1] se obtiene que para la matriz $B$ de (2) ese autovector es:

[Imagen: Vector estacionario $x=\frac1{110}(17,15,30,12,15,21)^T\approx(0.1545,0.1364,0.2727,0.1091,0.1364,0.1909)^T$ (PageRank: la página 3 es la más relevante).]

Compara este resultado con el de la Tabla 2.

[1] CAS = Computer Algebra System (como Matlab)

Cómo trabajar con Matlab

Para empezar, debemos introducir la matriz de adyacencia del grafo correspondiente, teniendo en cuenta el orden alfabético (u otro similar) de las páginas así como la disposición de entradas-salidas.

La matriz de adyacencia del ejemplo de la figura 2 (b) es:

$$A=\left\lbrack \begin{array}{cccccc}
0 & 0 & 1 & 0 & 0 & 0\\
1 & 0 & 0 & 1 & 1 & 0\\
0 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 1 & 0 & 0 & 1\\
1 & 1 & 0 & 0 & 0 & 1\\
1 & 0 & 1 & 1 & 0 & 0
\end{array}\right\rbrack$$

```matlab
clc, clear, clf
A = [0 0 1 0 0 0;1 0 0 1 1 0;0 1 0 0 1 1;0 0 1 0 0 1;1 1 0 0 0 1;1 0 1 1 0 0]
```

**Salida:**
```text
A =
0  0  1  0  0  0
1  0  0  1  1  0
0  1  0  0  1  1
0  0  1  0  0  1
1  1  0  0  0  1
1  0  1  1  0  0
```

Otra forma de definir la matriz de adyacencia con Matlab es generar únicamente aquellos elementos que no son nulos mediante sendos vectores que indican la fila/columna donde se encuentran

```matlab
% Otra forma de hacerlo
i = [1 2 2 2 3 3 3 4 4 5 5 5 6 6 6];
j = [3 1 4 5 2 5 6 3 6 2 6 1 1 3 4];
n = 6;
A1 = sparse(i,j,1,n,n); % Creamos una matriz dispersa A1 en la que unicamente son no nulos (1) los elementos de posicion dada por los vectores i y j
B1 = full(A1) % completamos la matriz dispersa con ceros
```

**Salida:**
```text
B1 =
0  0  1  0  0  0
1  0  0  1  1  0
0  1  0  0  1  1
0  0  1  0  0  1
1  1  0  0  0  1
1  0  1  1  0  0
```

De esta forma se almacena una matriz dispersa (sparse) en una estructura de datos que sólo requiere memoria para los elementos no nulos y sus índices. Esto apenas es necesario para una matriz de 6 por 6 con sólo 13 entradas nulas, pero adquiere una importancia crucial para problemas más grandes.

A continuación generamos el grafo. Previamente nombraremos los nodos (en este caso números):

```matlab
nodos = {'1', '2', '3','4', '5', '6'};
G = digraph(A,nodos); % También podríamos hacerlo con la matriz B
plot(G)
```

**Salida:**
```text
[figura]
```

Es aconsejable leer bien el menú de ayuda de matlab del comando digraph. En él encontraréis todas las posibilidades del comando como asignar pesos a los nodos, omitir auto enlaces, ect.

Ahora debemos trasponer la matriz de adyacencia y dividir cada columna por el número de unos que contenga:

```matlab
B2 = B1'; % Trasponemos la matriz de adyacencia
B = B2./sum(B2) % Dividimos cada columna de B
```

**Salida:**
```text
B =
0  0.3333  0  0  0.3333  0.3333
0  0  0.3333  0  0.3333  0
1.0000  0  0  0.5000  0  0.3333
0  0.3333  0  0  0  0.3333
0  0.3333  0.3333  0  0  0
0  0  0.3333  0.5000  0.3333  0
```

Calculamos ahora los autovalores (D) autovectores (V) de la matriz B con el comando eig de Matlab , extraemos de la matriz de autovectores el que corresponde al autovalor 1 y lo normalizamos. Ten en cuenta que Matlab no da los autovalores ordenados.

```matlab
[V,D] = eig(B) % Calculamos autovalores (D) y autovectores (V) de B
[d,ind] = sort(abs((diag(D))),'descend') % Ordenamos los autovalores en d. ind nos da los indices de las posiciones originales (columna)
```

**Salida:**
```text
V =
-0.3605 + 0.0000i  -0.1544 + 0.3706i  -0.1544 - 0.3706i  -0.3573 + 0.0000i  -0.1025 + 0.0000i  0.1213 + 0.0000i
-0.3181 + 0.0000i  -0.2242 - 0.1962i  -0.2242 + 0.1962i  -0.4042 + 0.0000i  -0.2741 + 0.0000i  0.1213 + 0.0000i
-0.6361 + 0.0000i  0.7495 + 0.0000i  0.7495 + 0.0000i  0.1808 + 0.0000i  0.4842 + 0.0000i  -0.4851 + 0.0000i
-0.2545 + 0.0000i  -0.1192 + 0.2162i  -0.1192 - 0.2162i  0.3740 + 0.0000i  -0.4603 + 0.0000i  0.4851 + 0.0000i
-0.3181 + 0.0000i  -0.2242 - 0.1962i  -0.2242 + 0.1962i  -0.4042 + 0.0000i  -0.2741 + 0.0000i  0.3638 + 0.0000i
-0.4453 + 0.0000i  -0.0275 - 0.1944i  -0.0275 + 0.1944i  0.6108 + 0.0000i  0.6268 + 0.0000i  -0.6063 + 0.0000i
D =
1.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  -0.2977 + 0.5522i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  -0.2977 - 0.5522i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.1842 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  -0.2554 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  -0.3333 + 0.0000i
d =
1.0000
0.6273
0.6273
0.3333
0.2554
0.1842
ind =
```

Como sabemos que el mayor autovalor es $\lambda =1$, sabemos que éste estará en la primera posición, una vez ordenados, por tanto, el autovector correspondiente corresponderá a esa misma posición en la matriz V:

```matlab
v = abs(V(:,ind(1))); % el autovector es v
v = v/sum(v) % normalizamos el autovector de modo que sus elementos sumen 1, asimilándolos a probabilidades
```

**Salida:**
```text
v = 6×1
0.1545
0.1364
0.2727
0.1091
0.1364
0.1909
```

Se verifica el resultado con el obtenido anteriormente

Estrategia de Bob

Aunque Bob coincide con Alice en la definición de clasificación de páginas, se da cuenta de que puede resultar engañosa para algunos grafos web. Por ejemplo, en la Figura 2(a) el grafo web consiste en dos grupos de páginas no enlazados.

[Imagen: Dos redes de 6 páginas: (a) red desconectada en dos grupos {1,2,3} y {4,5,6}; (b) red conectada con enlaces cruzados.]

En este caso si un vector de estado inicial tiene probabilidad cero de enlazar a todas las páginas de uno de los grupos, lo mismo pasará en los siguientes vectores de estado, de modo que nunca se accederá a ninguna de las páginas de ese grupo. La Figura 2 (b) representa un ejemplo más sutil. En este caso el grupo de páginas 1, 2 y 3 no tiene enlaces hacia el grupo de las páginas 4, 5, 6 de modo que cuando se abandona el grupo 4, 5, 6 se queda “atrapado” en el grupo 1, 2, 3 de modo que el conteo de acceso a las páginas 4, 5 y 6 tenderá a cero por lo que la clasificación de páginas en ese grupo será cero.

La solución de Bob a este problema es asumir que no esta obligado a seguir los enlaces que aparecen en la página en que se encuentra, pudiendo elegir, con una probabilidad determinada, cualquier página de la red. Concretamente, Bob supone que existe una probabilidad $\delta$, denominada factor de atenuación, de que salte a una página referenciada en la que se encuentra y una probabilidad de $1-\delta$ de elegir la siguiente página aleatoriamente.  Si hay $n$ páginas en la red, en el último caso, la probabilidad de elegir una página aleatoriamente es $\frac{1-\delta }{n}$

Para poner en práctica su estrategia, Bob crea una nueva matriz de probabilidad de transición $M=\left\lbrack m_{\textrm{ij}} \right\rbrack$ en la que:

$m_{\textrm{ij}} =\delta b_{\textrm{ij}} +\frac{1-\delta }{n}$      (4)

con $b_{\textrm{ij}}$ según la definición 2. Entonces reemplaza (3) con el esquema iterativo:

$${\mathit{\mathbf{x}}}^{\left(k\right)} =M{\mathit{\mathbf{x}}}^{\left(k-1\right)} ,\;\;k=1,2,3,\ldotp \ldotp \ldotp \ldotp$$

Por tanto, la matriz $M$ tiene la forma:

$M=\delta B+\frac{1-\delta }{n}\left\lbrack \begin{array}{cccc}
1 & 1 & \cdots  & 1\\
1 & 1 & \cdots  & 1\\
\vdots  & \vdots  & \ddots  & \vdots \\
1 & 1 & \cdots  & 1
\end{array}\right\rbrack$  (6)

De lo que se sigue que el esquema iterativo de (5) se puede escribir de la forma:

${\mathit{\mathbf{x}}}^{\left(k\right)} ={\delta B\cdot x}^{\left(k-1\right)} +\frac{1-\delta }{n}\left\lbrack \begin{array}{c}
1\\
1\\
\vdots \\
1
\end{array}\right\rbrack$   (7)

Como ejemplo, consideremos el grafo de web de la Figura 2(b), en este caso su matriz de adyacencia (traspuesta) y su matriz de transición son:

[Imagen: Red sin enlaces de salida en algunas páginas: $A=\begin{pmatrix}0&1&0&0&1&1\\0&0&1&0&1&1\\1&1&0&1&0&1\\0&0&0&0&0&1\\0&0&0&0&0&0\\0&0&0&1&1&0\end{pmatrix}$, $B=\begin{pmatrix}0&1/2&0&0&1/3&1/4\\0&0&1&0&1/3&1/4\\1&1/2&0&1/2&0&1/4\\0&0&0&0&0&1/4\\0&0&0&0&0&0\\0&0&0&1/2&1/3&0\end{pmatrix}$.]

Por lo general elegiremos un vector de estado inicial en el que todos sus elementos sean iguales (misma probabilidad de todas las páginas):

$${\mathit{\mathbf{x}}}^{\left(0\right)} =\left\lbrack \begin{array}{c}
\frac{1}{6}\\
\frac{1}{6}\\
\frac{1}{6}\\
\frac{1}{6}\\
\frac{1}{6}\\
\frac{1}{6}
\end{array}\right\rbrack$$

La estrategia iterativa de Alice ${\mathit{\mathbf{x}}}^{\left(k+1\right)} =B{\mathit{\mathbf{x}}}^{\left(k\right)}$ resulta:

[Imagen: Iteraciones desde $x^{(0)}=(1/6,\dots,1/6)$: $x^{(5)}=(.1999,.4043,.393,.0007,0,.0022)$, $x^{(10)}=(.1992,.4015,.3992,0,0,0)$, $x^{(15)}=(.1998,.4002,.4,0,0,0)$ (la probabilidad se concentra en las páginas 1–3).]

En comparación, cuando Bob implemente su esquema iterativo modificado empezando con el mismo vector de estado inicial, pero con $\delta =0\ldotp 85$ obtendrá:

[Imagen: Iteraciones con factor de amortiguación: $x^{(5)}=(.1891,.348,.355,.0352,.025,.0477)$, $x^{(10)}=(.189,.3464,.3576,.035,.025,.0469)$, $x^{(15)}=(.1892,.3462,.3578,.035,.025,.0469)$.]

A partir de estos resultados observamos que mientras que en la estrategia de Alice las páginas 4, 5 y 6 obtienen cero, en la de Bob se obtienen resultados no nulos más razonables.

Matemáticamente, incluir un factor de atenuación de $\delta$ $\left(0\le \delta \le 1\right)$ asegura que la matriz $M$ sea regular y que para cualquier vector de estado inicial normalizado las iteraciones ${\;\mathit{\mathbf{x}}}^{\left(k\right)}$ convergen a un autovector de componentes positivas que corresponde al autovalor 1.

Aunque la teoría de las cadenas de Markov se venía utilizando desde hace tiempo para clasificar los nodos de las redes, la introducción de un factor de amortiguación fue la principal innovación del algoritmo PageRank utilizado por el motor de búsqueda de Google. Este algoritmo lleva el nombre de Larry Page, quien, junto con Sergey Brin, fundó la empresa Google a finales de los años 90.

Cómo hacerlo con Matlab

A continuación rehacemos los cálculos de la "Estrategia de Bob" con Matlab. Primero vamos a "reproducir" los pasos dados,para ello debemos crear la matriz M con el factor de atenuación correspondiente.

Creamos la matriz del dígrafo:

```matlab
A1 = [0 0 1 0 0 0;1 0 1 0 0 0;0 1 0 0 0 0;0 0 1 0 0 1;1 1 0 0 0 1;1 1 1 1 1 0];
```

Dibujamos el grafo

```matlab
nodos = {'1', '2', '3','4', '5', '6'};
G1 = digraph(A1,nodos); % También podríamos hacerlo con la matriz B
plot(G1)
C2 = A1'; % Trasponemos la matriz de adyacencia
C = C2./sum(C2) % Dividimos cada columna de B
```

**Salida:**
```text
[figura]
C = 6×6
0  0.5000  0  0  0.3333  0.2000
0  0  1.0000  0  0.3333  0.2000
1.0000  0.5000  0  0.5000  0  0.2000
0  0  0  0  0  0.2000
0  0  0  0  0  0.2000
0  0  0  0.5000  0.3333  0
```

Generamos la matriz M con la ecuación (6):

```matlab
[n,~] = size(C); % la variable n toma el valor de las filas/columnmas de B
delta = 0.85; % Factor de atenuación
M = delta * C +(((1-delta)/n) * ones(n)) % ones(n) crea unna matriz cuadrada de orden n con unos
```

**Salida:**
```text
M = 6×6
0.0250  0.4500  0.0250  0.0250  0.3083  0.1950
0.0250  0.0250  0.8750  0.0250  0.3083  0.1950
0.8750  0.4500  0.0250  0.4500  0.0250  0.1950
0.0250  0.0250  0.0250  0.0250  0.0250  0.1950
0.0250  0.0250  0.0250  0.0250  0.0250  0.1950
0.0250  0.0250  0.0250  0.4500  0.3083  0.0250
```

Ahora procedemos de la misma forma que con Alice:

```matlab
[V1,D1] = eig(M) % Calculamos autovalores (D) y autovectores (V) de B
[d1,ind1] = sort(abs((diag(D1))),'descend'); % Ordenamos los autovalores en d. ind nos da los indices de las posiciones originales (columna)
```

**Salida:**
```text
V1 = 6×6
-0.3545 + 0.0000i  0.3536 + 0.3536i  0.3536 - 0.3536i  -0.1586 + 0.0000i  -0.0940 + 0.0000i  0.4264 + 0.0000i
-0.6453 + 0.0000i  -0.7071 + 0.0000i  -0.7071 + 0.0000i  -0.5471 + 0.0000i  0.1362 + 0.0000i  -0.4264 + 0.0000i
-0.6647 + 0.0000i  0.3536 - 0.3536i  0.3536 + 0.3536i  -0.4321 + 0.0000i  -0.0259 + 0.0000i  -0.2132 + 0.0000i
-0.0625 + 0.0000i  -0.0000 - 0.0000i  -0.0000 + 0.0000i  0.2815 + 0.0000i  0.3970 + 0.0000i  -0.4264 + 0.0000i
-0.0625 + 0.0000i  -0.0000 - 0.0000i  -0.0000 + 0.0000i  0.2815 + 0.0000i  0.3970 + 0.0000i  0.6396 + 0.0000i
-0.0913 + 0.0000i  0.0000 + 0.0000i  0.0000 - 0.0000i  0.5747 + 0.0000i  -0.8104 + 0.0000i  0.0000 + 0.0000i
D1 = 6×6
1.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  -0.4250 + 0.4250i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  -0.4250 - 0.4250i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.3470 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  -0.3470 + 0.0000i  0.0000 + 0.0000i
0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  0.0000 + 0.0000i  -0.0000 + 0.0000i
```

Como sabemos que el mayor autovalor es $\lambda =1$, sabemos que éste estará en la primera posición, una vez ordenados, por tanto, el autovector correspondiente corresponderá a esa misma posición en la matriz V:

```matlab
v1 = abs(V1(:,ind(1))); % el autovector es v
v1 = v1/sum(v1) % normalizamos el autovector de modo que sus elementos sumen 1, asimilándolos a probabilidades
```

**Salida:**
```text
v1 = 6×1
0.1885
0.3431
0.3534
0.0333
0.0333
0.0486
```

Se verifica el resultado con el obtenido anteriormente

Finalmente, Matlab nos permite en un solo comando, ordenar las páginas incluyendo un factor de atenuación $\delta$, de la siguiente forma:

```matlab
pr = centrality(G1,'pagerank','FollowProbability',0.85)
```

**Salida:**
```text
pr = 6×1
0.1885
0.3431
0.3534
0.0333
0.0333
0.0486
```

Finalmente damos el resultado con fprintf

```matlab
[C,I] = sort(pr,'descend') % en C los puntos de mayor a menor en I los índices del vector cl que se corresponden con el orden de C
nodosord = nodos(I); % ordenamos los nodos de igual forma que la clasificación
N = convertCharsToStrings(nodosord); % convertimos los nodos de formato cell a char para el fprintf
for i = 1: length(C)
    fprintf('%.0fº es la web %s\n',i,N(i))
end
```

**Salida:**
```text
C = 6×1
0.3534
0.3431
0.1885
0.0486
0.0333
0.0333
I = 6×1
1º es la web 3
2º es la web 2
3º es la web 1
4º es la web 6
5º es la web 4
6º es la web 5
```

Compara el resultado obtenido con el del ejemplo estudiado anteriormente,  ten en cuenta que en el  ejemplo se han redondeado las cifras a 4 decimales mientras que Matlab opera con doble precisión (19 decimales)

El algoritmo “Page Rank” de Google

Hemos calculado el pageRank al estilo de Google para nuestro internet. Google es una máquina que hace justamente eso, visitan páginas y estudian la conectividad de unas con otras y le asignan pesos de importancia en la red, el denominado pageRank.

Aunque la teoría de cadenas de Markov había sido empleada anteriormente para clasificar nodos de redes, la introducción del factor de atenuación representó la mayor innovación del algoritmo PageRank empleado por el motor de búsqueda de Google. Este algoritmo toma su nombre de Larry Page quien, junto con Sergey Brin, fundó la compañía Google a finales de los 90.

Además, Google tiene herramientas secretas. No se conoce como asigna las probabilidades de visita asociadas a cada navegante que nosotros hemos supuesto que eran (1/número de páginas) para tener en cuenta cuando un navegante no sigue los enlaces de la página que está visitando.

Por supuesto, en Google pueden tocar los números asociados con el pageRank, por ejemplo, si pagas, para posicionarte mejor en las búsquedas.

Engañar a Google cada vez es más difícil, no es buena idea poner muchos enlaces a la misma página desde la tuya porque entonces nos penalizan. Así acaban con el linkspam. Ahora tienen en cuenta tus búsquedas anteriores y tus visitas para darte un resultado de búsqueda personalizado de modo que si dos personas hacen la misma búsqueda conectados a sus cuentas de Google obtienen diferentes resultados.

Lecturas adicionales de ayuda

La web de MatWorks dedica un apartado a el algoritmo PageRank, puedes consultarlo aquí: https://es.mathworks.com/help/matlab/math/use-page-rank-algorithm-to-rank-websites.html

_Imágenes embebidas: 41 (image1.jpeg, image1.png, image10.png, image11.png, image12.png, image13.png, image14.png, image15.png, image16.png, image17.png, image18.png, image19.png, image2.jpeg, image2.png, image20.png, image21.png, image22.png, image23.png, image24.png, image25.png, image26.png, image27.png, image28.png, image29.png, image3.png, image30.png, image31.png, image32.png, image33.png, image34.png, image35.png, image36.png, image37.png, image38.png, image39.png, image4.png, image5.png, image6.png, image7.png, image8.png, image9.png)_


## Práctica 1 · Modelo A (enunciado)

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 1/PR01_ModA.mlx`*

### PRÁCTICAS DE ÁLGEBRA

### PRÁCTICA 1

### MODELO A

ALUMNO:

INSTRUCCIONES

- Renombra el archivo como Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad

- Indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

- Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo hagas con fprintf

- Table of Contents

- PRÁCTICAS DE ÁLGEBRA · PRÁCTICA 1 · MODELO A ·     P01. Optimización de la Producción de Cerámica Especializada ·     P02. Edad media de la población española ·     P03. Red de distribución de agua

#### P01. Optimización de la Producción de Cerámica Especializada

Una empresa especializada en la fabricación de cerámica técnica necesita producir una mezcla de 100 kg de un compuesto cerámico avanzado $\left(P\right)$. Para lograr las propiedades deseadas (resistencia térmica, dureza, porosidad y ligereza), el compuesto debe contener cantidades exactas de cuatro óxidos metálicos clave: Alumina, Zirconio, Silicato de Calcio y Oxido de Magnesio.

La contribución, en porcentaje de peso por kilogramo, de estos óxidos a las cuatro propiedades requeridas se muestra en la siguiente tabla (las unidades de las propiedades están normalizadas):

Alúmina

Zirconio

Silicato de Calcio

Óxido de Magnesio

Requisito Total

Resistencia Térmica

0.3

0.1

0.2

0.4

18 kg-unidad

Dureza

0.4

0.2

0.1

0.1

15 kg-unidad

Porosidad

0.1

0.5

0.1

0.2

20 kg-unidad

Ligereza

0.2

0.2

0.6

0.3

22 kg-unidad

Se desea saber si existe una única combinación de los cuatro óxidos que cumpla exactamente con los requisitos totales de las cuatro propiedades y de la mezcla

a) (0,5p) Nombra e identifica las variables

b) (1p) Escribe las ecuaciones con el editor de ecuaciones que permiten resolver nuestra duda indicando a que corresponde cada una. Reescríbelas en forma matricial con el editor de ecuaciones

c) (1p) Determina si existe dicha combinación (no lo resuelvas). Justifica tu respuesta

d) (0,5p) En caso afirmativo, ¿cuántos kilogramos de cada óxido deben mezclarse para obtener el compuesto cerámico  con las propiedades especificadas? Da la respuesta con dos decimales e indicando a qué pertenece cada una

Respuesta

#### P02. Edad media de la población española

Dada la siguuiente gráfica

[Imagen: Gráfico de barras 'Edad media de la población española entre 1950 y 2050*' (Statista 2024, fuente United Nations): 1950 27,5; 1955 28,6; 1960 29,2; 1965 30; 1970 29,8; 1975 29,9; 1980 30,4; 1985 31,6; 1990 33,4; 1995 35,5; 2000 37,6; 2005 39,1; 2010 40; 2015 42,5; 2020* 44,9; 2025* 47,3; 2030* 49,6; 2035* 51,4; 2040* 52,6; 2045* 53,2; 2050* 53,2.]

La gráfica está realizada en el año 2019 por lo que los años marcados con * son estimaciones

a) (0,5p) Si tomamos los datos de los años 2000 a 2015 (ambos incluídos) ¿cuál es el grado del polinomio de interpolación?. Justifica tu respuesta

b) (1p) Escribe las ecuaciones que determinan los coeficientes del polinomio de interpolación. Para evitar problemas, realiza previamente un cambio de variable de modo que el año 2000 corresponda al origen de abscisas $z=2000-x$

c) (0,5p) Calcula los coeficientes del polinomio de interpolación resolviendo el sistema de ecuaciones lineales.. Da el resultado en porden de mayor a menor exponente del término. No se permite emplear la función polyfit

d) (1p) Representa gráficamente los puntos de datos y el polinomio en la misma gráfica. Emplea las funciones xticks y xticklabels para que aparezcan los años en el eje de abscisas (es decir, en lugar de 0, 5, 10, 15 deben mostrarse los años)

e) (0,5p)Calcula el valor de la edad media para 2020 y compáralo con el que da la gráfica. Da el resultado con dos decimales.Explica la diferencia

f) (0,5p) Calcula la edad media en 2012.  Da el resultado con dos decimales.

Respuesta

#### P03. Red de distribución de agua

Una red de tuberías distribuye agua en una pequeña urbanización. Los flujos están medidos en litros por segundo (litros/s).

Diagrama de la red:

- Una tubería principal entra en el nodo A con un flujo de 100 litros/s.

- De A, el agua fluye hacia B (flujo $x_1$) y hacia D (flujo $x_4$).

- De B, el agua fluye hacia C (flujo $x_2$). Además, del nodo B salen 20 litros/s del sistema.

- De D, el agua fluye hacia B (flujo $x_3$) y hacia C (flujo $x_5$).

- Del nodo C, salen 80 litros/s del sistema.

Se pide:

a) (0,5p) Escribe mediante el editor de ecuaciones, el sistema de ecuaciones que describe el flujo de agua en cada nodo (A, B, C, D). identifica cada nodo en cada ecuación.

b) (0,5p) Escribe el sistema del apartado anterior en forma matricial mediante el editor de ecuaciones

c) (0,75p) Encuentra la solución general del sistema para determinar los flujos $x_1 ,x_2 ,x_3 ,x_4 ,x_5$

d) (1,25p) Debido a trabajos de mantenimiento, la tubería que va de D a B debe cerrarse. ¿Cuál es el rango de valores posibles para el flujo $x_1$ si se sabe que todas las tuberías deben tener un flujo no negativo?

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## Práctica 1 · Modelo A (resuelta)

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 1/PR01_ModA_resp.pdf`*

#### Página 1

```text
PRÁCTICAS DE ÁLGEBRA
PRÁCTICA 1
MODELO A

ALUMNO:

INSTRUCCIONES

• Renombra el archivo como Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea
habilitada para ello en Canvas
• Responde debajo de donde se indica
• Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase
• El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos
de aplicación de la normativa de la universidad
• Indica cada uno de los apartados en la respuesta
• No elimines las secciones
• Comienza siempre el script de cada problama con clc, clear, clf
• Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado
• El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos
ebn la calificación final de la práctica
• Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo
hagas con

Table of Contents
PRÁCTICAS DE ÁLGEBRA................................................................................................................................1
PRÁCTICA 1....................................................................................................................................................... 1
MODELO A......................................................................................................................................................... 1
P01. Optimización de la Producción de Cerámica Especializada...................................................................1
P02. Edad media de la población española....................................................................................................3
P03. Red de distribución de agua................................................................................................................... 7

P01. Optimización de la Producción de Cerámica Especializada
Una empresa especializada en la fabricación de cerámica técnica necesita producir una mezcla de 100
kg de un compuesto cerámico avanzado  . Para lograr las propiedades deseadas (resistencia térmica,
dureza, porosidad y ligereza), el compuesto debe contener cantidades exactas de cuatro óxidos metálicos
clave: Alumina, Zirconio, Silicato de Calcio y Oxido de Magnesio.

La contribución, en porcentaje de peso por kilogramo, de estos óxidos a las cuatro propiedades requeridas
se muestra en la siguiente tabla (las unidades de las propiedades están normalizadas):

```

#### Página 2

```text
Alúmina  Zirconio  Silicato de  Óxido de  Requisito Total
Calcio  Magnesio
Resistencia  0.3  0.1  0.2  0.4  27 kg-unidad
Térmica
Dureza  0.4  0.2  0.1  0.1  15 kg-unidad
Porosidad  0.1  0.5  0.1  0.2  22 kg-unidad
Ligereza  0.2  0.2  0.6  0.3  36 kg-unidad
Se desea saber si existe una única combinación de los cuatro óxidos que cumpla exactamente con los
requisitos totales de las cuatro propiedades y de la mezcla

a) (0,5p) Nombra e identifica las variables

b) (1p) Escribe las ecuaciones que permiten resolver nuestra duda indicando a que corresponde cada una.
Reescríbelas en forma matricial

c) (1p) Determina si existe dicha combinación. Justifica tu respuesta

d) (0,5p) En caso afirmativo, ¿cuántos kilogramos de cada óxido deben mezclarse para obtener el
compuesto cerámico con las propiedades especificadas?

Respuesta

a) Las variables son:

b) Las ecuaciones son:

c) Será posible si el sistema es compatible determinado:

clc, clear
A = [0.3 0.1 0.2 0.4;
0.4 0.2 0.1 0.1;
0.1 0.5 0.1 0.2;
0.2 0.2 0.6 0.3;
1 1 1 1]

A = 5×4
0.3000  0.1000  0.2000  0.4000
0.4000  0.2000  0.1000  0.1000
0.1000  0.5000  0.1000  0.2000

```

#### Página 3

```text
0.2000  0.2000  0.6000  0.3000
1.0000  1.0000  1.0000  1.0000

b = [27;15;22;36;100]

b = 5×1

Ab = [A b]

Ab = 5×5
0.3000  0.1000  0.2000  0.4000  27.0000
0.4000  0.2000  0.1000  0.1000  15.0000
0.1000  0.5000  0.1000  0.2000  22.0000
0.2000  0.2000  0.6000  0.3000  36.0000
1.0000  1.0000  1.0000  1.0000  100.0000

sol = rref(Ab)

sol = 5×5
1  0  0  0  10
0  1  0  0  20
0  0  1  0  30
0  0  0  1  40
0  0  0  0  0

Como la matriz escalonada equivalente a la matriz ampliada tiene 4 pivotes en la parte de coeficientes, el
sistema es compatible determinado y tiene una única solución.

d)

x = A\b;
oxi = ["Alúmina" "Zirconio" "Silicato de Calcio" "Óxido de magnesio"];
disp('Serán necesarios:')

Serán necesarios:

for i = 1:4
fprintf('%.2f kg de %s\n',x(i),oxi(i))
end

10.00 kg de Alúmina
20.00 kg de Zirconio
30.00 kg de Silicato de Calcio
40.00 kg de Óxido de magnesio

P02. Edad media de la población española
Dada la siguuiente gráfica

```

#### Página 4

```text
La gráfica está realizada en el año 2019 por lo que los años marcados con * son estimaciones

a) (0,5p) Si tomamos los datos de los años 2000 a 2015 (ambos incluídos) ¿cuál es el grado del polinomio
de interpolación?. Justifica tu respuesta

b) (1p) Escribe las ecuaciones que determinan los coeficientes del polinomio de interpolación. Para evitar
problemas, realiza previamente un cambio de variable de modo que el año 2000 corresponda al origen de
abscisas

c) (0,5p) Calcula los coeficientes del polinomio de interpolación resolviendo el sistema de ecuaciones
lineales

d) (1p) Representa gráficamente los puntos de datos y el polinomio en la misma gráfica. Emplea las
funciones xticks y xticklabels para que aparezcan los años en el eje de abscisas

e) (0,5p)Calcula el valor de la edad media para 2020 y compáralo con el que da la gráfica. Da el resultado
con dos decimales.Explica la diferencia

f) (0,5p) Calcula la edad media en 2012. Da el resultado con dos decimales.

Respuesta

a) Al ser 4 puntos el polinomio es de tercer grado ya que  es la ecuacion general
que supone 4 variables que calculo con las 4 ecuaciones con los 4 puntos

b) El polinomio es:

```

#### Página 5

```text
Los datos son:

2000  2005  2010  2015
37.6  39.1  40  42.5
Las ecuaciones después del cambio de variable son:

c) Calculamos los coeficientes de mayor a menor grado

clc, clear, clf
anio = 2000:5:2015; anio = anio';z=anio-2000;
edad = [37.6 39.1 40 42.5]';
A = [z.^3 z.^2 z ones(4,1)];
p = A\edad

p = 4×1
0.0029
-0.0560
0.5067
37.6000

d) Representación gráfica:

plot(z, edad,'or','LineWidth',2)
xticks(z);
xticklabels({'2000', '2005', '2010', '2015'});
hold on
xp = linspace(0,15,100);
yp = polyval(p,xp);
plot(xp, yp, '-k','LineWidth',2)
xlabel('Año')
ylabel('Edad media (años)')
legend('datos','polinomio interpolacion','Location','best')
hold off

```

#### Página 6

```text
e) Edad media en 2020 estimada:

edad2020 = polyval(p, 20);
fprintf('La edad media en 2020 estimada es de %.2f años\n',edad2020)

La edad media en 2020 estimada es de 48.80 años

Hay una diferencia de

La diferencia es debida a la tendencia del polinomio tal como se observa en la siguiente gráfica:

plot(z, edad,'or','LineWidth',2)
xticks(z);
xticklabels({'2000', '2005', '2010', '2015'});
hold on
xp = linspace(0,20,100);
yp = polyval(p,xp);
plot(xp, yp, '-k','LineWidth',2)
plot(20,44.9,'*k','LineWidth',2)
xlabel('Año')
ylabel('Edad media (años)')
legend('datos','polinomio interpolacion','Valor de
tabla','Location','best')
hold off

```

#### Página 7

```text
f)

Edad media en 2012 interpolada:

edad2012 = polyval(p, 12);
fprintf('La edad media en 2012 interpolada es de %.2f años\n',edad2012)

La edad media en 2012 interpolada es de 40.68 años

P03. Red de distribución de agua
Una red de tuberías distribuye agua en una pequeña urbanización. Los flujos están medidos en litros por
segundo (litros/s).

Diagrama de la red:

• Una tubería principal entra en el nodo A con un flujo de 100 litros/s.
• De A, el agua fluye hacia B (flujo ) y hacia D (flujo ).
• De B, el agua fluye hacia C (flujo  ). Además, del nodo B salen 20 litros/s del sistema.
• De D, el agua fluye hacia B (flujo  ) y hacia C (flujo  ).
• Del nodo C, salen 80 litros/s del sistema.

Se pide:

a) (0,5p) Escribe el sistema de ecuaciones que describe el flujo de agua en cada nodo (A, B, C, D).
identifica cada nodo

b) (0,5p) Escribe el sistema del apartado anterior en forma matricial

c) (0,75p) Encuentra la solución general del sistema para determinar los flujos

d) (1,25p) Debido a trabajos de mantenimiento, la tubería que va de D a B debe cerrarse. ¿Cuál es el rango
de valores posibles para el flujo  si se sabe que todas las tuberías deben tener un flujo no negativo?

```

#### Página 8

```text
Respuesta

a)

Nodo A:

Nodo B:

Nodo C:

Nodo D:

b)

c)

clc, clear
A = [1 0 0 1 0;
1 -1 1 0 0;
0 1 0 0 1;
0 0 -1 1 -1]

A = 4×5
1  0  0  1  0
1  -1  1  0  0
0  1  0  0  1
0  0  -1  1  -1

b = [100;20;80;0]

```

#### Página 9

```text
b = 4×1

Ab = [A b]

Ab = 4×6
1  0  0  1  0  100
1  -1  1  0  0  20
0  1  0  0  1  80
0  0  -1  1  -1  0

x = rref(Ab)

x = 4×6
1  0  0  1  0  100
0  1  0  0  1  80
0  0  1  -1  1  0
0  0  0  0  0  0

La solución general es, tomando como variables libres  y  y despejando las demás:

d) Si la tubería que va de D a B debe cerrarse, es decir,  y nos queda:

Si se sabe que todas las tuberías deben tener un flujo no negativo, entonces  , por tanto

```


## Práctica 1 · Modelo B (enunciado)

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 1/PR01_ModB.mlx`*

### PRÁCTICAS DE ÁLGEBRA

### PRÁCTICA 1

### MODELO B

ALUMNO:

INSTRUCCIONES:

- Renombra el archivo como Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad

- Indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

- Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo hagas con fprintf

- Table of Contents

- PRÁCTICAS DE ÁLGEBRA · PRÁCTICA 1 · MODELO B ·     P01. Apartamentos ·     P02. Población en España ·     P03.Flujo de datos en una red informática

#### P01. Apartamentos

Se va a construir un gran edificio de apartamentos utilizando técnicas de construcción modular. La distribución de los apartamentos en cada planta se elegirá entre uno de los tres planes básicos. El plan A tiene 18 apartamentos en una planta, incluyendo 3 unidades de tres dormitorios, 7 unidades de dos dormitorios y 8 unidades de un dormitorio. Cada planta del plan B incluye 4 unidades de tres dormitorios, 4 unidades de dos dormitorios y 8 unidades de un dormitorio. Cada piso del plan C incluye 5 unidades de tres dormitorios, 3 unidades de dos dormitorios y 9 unidades de un dormitorio.

Se desa saber si es posible diseñar el edificio con exactamente 66 unidades de tres dormitorios, 74 unidades de dos dormitorios y 136 unidades de un dormitorio en un total de 16 pisos

a) (0,5p) Nombra e identifica las variables

b) (1p) Escribe con el editor de ecuaciones las ecuaciones que permiten resolver nuestra duda. Reescríbelas con el editor de ecuaciones en su forma matricial

c) (1p) Determina si es posible diseñar el edificio tal y como deseamos (no lo resuelvas). Justifica tu respuesta

d) (0,5p) Si es así, ¿hay más de una forma de hacerlo? Si solo hay una, da la respuesta indicando la cantidad de cada plan necesaria. Se valorará que des la respuesta mediante fprintf

Respuesta

#### P02. Población en España

La gráfica representa la població española entre 2001 y 2014

[Imagen: Gráfico 'Evolución de la población de España (2001-2014)': 2001 40.476.723; 2002 41.035.271; 2003 41.827.836; 2004 42.547.454; 2005 43.296.335; 2006 44.009.969; 2007 44.784.659; 2008 45.668.938; 2009 46.239.271; 2010 46.486.621; 2011 46.667.175; 2012 46.818.216; 2013 46.727.890; 2014 46.507.760.]

a) (0,5p) Si tomamos los datos de los años 2010 a 2014 (ambos incluidos) ¿cuál es el grado del polinomio de interpolación? Justifica la respuesta

b) (1p) Escribe mediante el editor de ecuaciones las ecuaciones que determinan los coeficientes del polinomio de interpolación. Para evitar problemas, realiza previamente un cambio de variable de modo que el año 2010 corresponda al origen de abscisas $z=2010-x$

c) (1p) Calcula los coeficientes del polinomio de interpolación resolviendo el sistema de ecuaciones lineales. Da el resultado de mayor a menor grado del término. No se permite emplear la función polyfit

d) (1p) Representa gráficamente los puntos de datos y el polinomio en la misma gráfica. Emplea las funciones xticks y xticklabels para que aparezcan los años en el eje de abscisas

e) (0,5p) Calcula la población en 2015 y compáralo con el dato real de 46.440.099. Da el resultado con fprintf redondeada al entero más próximo Explica la diferencia representando gráficamente el polinomio hasta 2015

Respuesta

#### P03. Flujo de datos en una red informática

El flujo de paquetes de datos (en megabits por segundo, Mbps) entre varios servidores de una red se describe de la siguiente forma

Diagrama de la red:

- Al servidor A llegan 50 Mbps y al servidor B llegan 30 Mbps desde el exterior.

- Desde A, los datos se envían a C (flujo $\left.x_1 \right)$ y a D (flujo $x_2$).

- Desde B, los datos se envían a C (flujo $x_3$).

- Desde C, los datos se envían a E (flujo $x_4$).

- Desde D, los datos se envían a C (flujo $x_5$) y a E (flujo $x_6$).

- Todo el tráfico de la red sale a través del servidor E.

a) (0,5p) Escribe  mediante el editor de ecuaciones el sistema de ecuaciones que describe el flujo de datos en cada nodo (A, B, C, D,E). identifica cada nodo

b) (0,5p) Escribe con el editor de ecuaciones (no con Matlab) el sistema del apartado anterior en forma matricial

c) (0,75p) Encuentra la solución general del sistema para determinar los flujos $x_1 ,x_2 ,x_3 ,x_4 ,x_5 ,x_6$

d)(1,25p) Si el enlace de D a C se satura y no puede transmitir más de 5 Mbps, ¿cuál es el flujo máximo que puede pasar por el enlace de C a E?

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## Práctica 1 · Modelo B (resuelta)

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 1/PR01_ModB_resp.pdf`*

#### Página 1

```text
PRÁCTICAS DE ÁLGEBRA
PRÁCTICA 1
MODELO B

ALUMNO:

INSTRUCCIONES:

• Renombra el archivo como Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea
habilitada para ello en Canvas
• Responde debajo de donde se indica
• Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase
• El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos
de aplicación de la normativa de la universidad
• Indica cada uno de los apartados en la respuesta
• No elimines las secciones
• Comienza siempre el script de cada problama con clc, clear, clf
• Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado
• El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos
ebn la calificación final de la práctica
• Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo
hagas con fprintf

P01. Apartamentos
Se va a construir un gran edificio de apartamentos utilizando técnicas de construcción modular. La
distribución de los apartamentos en cada planta se elegirá entre uno de los tres planes básicos. El plan
A tiene 18 apartamentos en una planta, incluyendo 3 unidades de tres dormitorios, 7 unidades de dos
dormitorios y 8 unidades de un dormitorio. Cada planta del plan B incluye 4 unidades de tres dormitorios, 4
unidades de dos dormitorios y 8 unidades de un dormitorio. Cada piso del plan C incluye 5 unidades de tres
dormitorios, 3 unidades de dos dormitorios y 9 unidades de un dormitorio.

Se desa saber si es posible diseñar el edificio con exactamente 66 unidades de tres dormitorios, 74
unidades de dos dormitorios y 136 unidades de un dormitorio en un total de 16 pisos

a) (0,5p) Nombra e identifica las variables

b) (1p) Escribe las ecuaciones que permiten resolver nuestra duda y después en su forma matricial

c) (1p) Determina si es posible diseñar el edificio tal y como deseamos. Justifica tu respuesta

d) (0,5p) Si es así, ¿hay más de una forma de hacerlo? Si solo hay una, da la respuesta indicando la
cantidad de cada plan necesaria. Se valorará que des la respuesta mediante fprintf

Respuesta

```

#### Página 2

```text
a) Sean:

número de pisos del plan A

número de pisos del plan B

número de pisos del plan C

b) Las condiciones del problema se convierten en las siguientes ecuaciones:

Unidades de 3 dormitorios:

Unidades de 2 dormitorios:

Unidades de 1 dormitorio:

Total de pisos;

c) Calculamos la forma escalonada reducida de la matriz ampliada del sistema:

clc, clear
A = [3 4 5;7 4 3;8 8 9;1 1 1]

A = 4×3
3  4  5
7  4  3
8  8  9
1  1  1

b = [66;74;136;16];
Ab = [A b];
sol = rref(Ab)

sol = 4×4
1  0  0  6
0  1  0  2
0  0  1  8
0  0  0  0

A la vista de los resultados el sistema es compatible determinado, una única solución

d) Damos la solución:

plan = ["A" "B" "C"]

plan = 1×3 string
"A"  "B"  "C"

disp('Se  requieren:')

Se  requieren:

for i=1:3
fprintf('%i pisos del plan %s\n',sol(i,end),plan(i))
end

```

#### Página 3

```text
6 pisos del plan A
2 pisos del plan B
8 pisos del plan C

P02. Población en España
La gráfica representa la població española entre 2001 y 2014

a) (0,5p) Si tomamos los datos de los años 2010 a 2014 (ambos incluidos) ¿cuál es el grado del polinomio
de interpolación?

b) (1p) Escribe las ecuaciones que determinan los coeficientes del polinomio de interpolación. Para evitar
problemas, realiza previamente un cambio de variable de modo que el año 2010 corresponda al origen de
abscisas

c) (1p) Calcula los coeficientes del polinomio de interpolación resolviendo el sistema de ecuaciones lineales

d) (1p) Representa gráficamente los puntos de datos y el polinomio en la misma gráfica. Emplea las
funciones xticks y xticklabels para que aparezcan los años en el eje de abscisas

e) (0,5p) Calcula la población en 2015 y compáralo con el dato real de 46.440.099. Da el resultado
con fprintf redondeada al entero más próximo Explica la diferencia representando gráficamente el
polinomio hasta 2015

Respuesta

a) Tomamos los datos de 2010 a 2014:

Año  2010  2011  2012  2013  2014

```

#### Página 4

```text
Población  46.486.621  46.667.175  46.818.216  46.727.890  46.507.760

Al tener 5 puntos el polinomio es de 4º grado:

b) Con el cambio de variable las ecuaciones son:

c)

clc, clear, clf
anio = 2010:1:2014

anio = 1×5
2010  2011  2012  2013  2014

z = anio' - 2010

z = 5×1

poblacion = [46486621;46667175;46818216;46727890;46507760]

poblacion = 5×1
46486621
46667175
46818216
46727890
46507760

A = [z.^4 z.^3 z.^2 z ones(5,1)]

A = 5×5
0  0  0  0  1
1  1  1  1  1
16  8  4  2  1
81  27  9  3  1
256  64  16  4  1

p = A\poblacion

p = 5×1
107 ×
0.0013
-0.0116
0.0239
0.0044
4.6487

d)

```

#### Página 5

```text
plot(z,poblacion,'or','LineWidth',2)
xticks(z);
xticklabels({'2010', '2011', '2012', '2013', '2014'});
hold on
xlabel('Año')
xp = linspace(0,4,100);
yp = polyval(p,xp);
xlabel('Año')
ylabel('Población')
plot(xp,yp,'-k','LineWidth',2)
legend('datos','polinomio interpol.','Location','best')
title('Población en España 2010-2014')
hold off

e)

p2015 = polyval(p,5);
fprintf('la poblacion estimada en 2015 es de %.0f habitantes\n',p2015)

la poblacion estimada en 2015 es de 46592806 habitantes

La población real es de 46.440.099. Por la forma del polinomio da una estimación mayor en 2014 cuando
la población está en descenso

Lo vemos si representamos los puntos del polinomio de 4º grado hasta 2015

plot(z,poblacion,'or','LineWidth',2)
xticks(z);
xticklabels({'2010', '2011', '2012', '2013', '2014'});
hold on
xlabel('Año')
xp = linspace(0,5,100);
yp = polyval(p,xp);
xlabel('Año')
ylabel('Población')

```

#### Página 6

```text
plot(xp,yp,'-k','LineWidth',2)
legend('datos','polinomio interpol.','Location','best')
title('Población en España 2010-2014')
hold off

.Se observa como el polinomio sube después de 2014, por eso la previsiónpara 2015 es falsa

P03.Flujo de datos en una red informática
El flujo de paquetes de datos (en megabits por segundo, Mbps) entre varios servidores de una red se
describe de la siguiente forma

Diagrama de la red:

• Al servidor A llegan 50 Mbps y al servidor B llegan 30 Mbps desde el exterior.
• Desde A, los datos se envían a C (flujo  y a D (flujo ).
• Desde B, los datos se envían a C (flujo  ).
• Desde C, los datos se envían a E (flujo  ).
• Desde D, los datos se envían a C (flujo  ) y a E (flujo  ).
• Todo el tráfico de la red sale a través del servidor E.

a) (0,5p) Escribe el sistema de ecuaciones que describe el flujo de datos en cada nodo (A, B, C, D,E).
identifica cada nodo

b) (0,5p) Escribe el sistema del apartado anterior en forma matricial

c) (0,75p) Encuentra la solución general del sistema para determinar los flujos

d)(1,25p) Si el enlace de D a C se satura y no puede transmitir más de 5 Mbps, ¿cuál es el flujo máximo
que puede pasar por el enlace de C a E?

Respuesta

```

#### Página 7

```text
Esquema de red:

a)

b)

c)

clc, clear
A = [1 1 0 0 0 0;
0 0 1 0 0 0;
1 0 1 -1 1 0;
0 1 0 0 -1 -1;
0 0 0 1 0 1]

A = 5×6
1  1  0  0  0  0
0  0  1  0  0  0
1  0  1  -1  1  0
0  1  0  0  -1  -1
0  0  0  1  0  1

b = [50;30;0;0;80]

b = 5×1

```

#### Página 8

```text

Ab = [A b]

Ab = 5×7
1  1  0  0  0  0  50
0  0  1  0  0  0  30
1  0  1  -1  1  0  0
0  1  0  0  -1  -1  0
0  0  0  1  0  1  80

x = rref(Ab)

x = 5×7
1  0  0  0  1  1  50
0  1  0  0  -1  -1  0
0  0  1  0  0  0  30
0  0  0  1  0  1  80
0  0  0  0  0  0  0

Tomando como variable libre  y  y despejando las demás:

d) Si el enlace de D a C se satura y no puede transmitir más de 5 Mbps, entonces  ¿cuál es el flujo
máximo que puede pasar por el enlace de C a E?

Si  entonces ¿cuál es el valor máximo de  ?

Como  y  tomando el valor máximo  nos queda:  , es decirt
dado que  tenemos que

Por otra parte  , es decir las condiciones son:

el valor minimo de  es cero, por tanto, el valor máximo de  es 80 Mbps

```


## Práctica 2 · Modelo A

*Fuente: `GRUPO B/PRACTICAS/PRACTICA 2/PR02_ModA.mlx`*

### PRÁCTICAS DE ÁLGEBRA

### PRÁCTICA 2

### MODELO A

ALUMNO:

INSTRUCCIONES

- Renombra el archivo como Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad

- Indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

- Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo hagas con

- Table of Contents

- PRÁCTICAS DE ÁLGEBRA · PRÁCTICA 2 · MODELO A ·     Problema 01. El torneo soñado de Ajedrez, de Anna Cramling. ·     Problema 02. Huertos de 4 vecinos ·     Problema 03. Red de carreteras

#### Problema 01. El torneo soñado de Ajedrez, de Anna Cramling.

Aunque es difícil elegir, según el consenso general, los 5 mejores jugadores de ajedrez de la historia, por su impacto en el juego, sus logros y sus habilidades personales, han sido:

- Magnus Carlsen (CAR): Campeón Mundial desde 2013 hasta la fecha (2025) y récord de mayor puntuación Elo en la historia (2882 en 2014).

- Garry Kasparov (KAS): Campeón Mundial desde 1985 hasta 2000, y mayor puntuación Elo de su época (2851 en 1999).

- Bobby Fischer (FIS): Campeón Mundial en 1972, derrotando a Boris Spassky en el famoso "Match del Siglo".

- José Raúl Capablanca (CAP): Campeón Mundial desde 1921 hasta 1927, uno de los grandes maestros del ajedrez clásico.

- Anatoly Karpov (KAR): Campeón Mundial desde 1975 hasta 1985, rival de Kasparov en una de las rivalidades más famosas de la historia del ajedrez.

La conocida youtuber y jugadora de ajedrez hispano-sueca Anna Cramling ha organizado el que espera ser el mayor evento del año en el mundo del ajedrez, lo que catapultará definitivamente su canal. Se trata de un torneo ficticio de ajedrez en el metaverso, en el que participan los avatares de los 5 jugadores descritos anteriormente, los 5 mejores de la historia.

El torneo es en formato "todos contra todos", de manera que los 5 jugadores se enfrentarán entre ellos en partidas individuales, decidiéndose la clasificación del torneo en función de las victorias directas e indirectas.

El desarrollo del torneo da los siguientes resultados:

- Fisher pierde contra Kasparov y contra Carlsen.

- Kasparov pierde contra Carlsen.

- Capablanca pierde todas sus partidas.

- Carlsen solo pierde contra Karpov.

- Karpov pierde contra Fisher y Kasparov.

NOTA: en el listado anterior, se entiende que si un jugador no ha perdido, entonces ha ganado. Es decir, no hay "tablas" (empates).

a) (0.75p) Escribe, mediante el editor de textos, una tabla que represente las victorias y derrotas de cada jugador en el torneo. En dicha tabla los jugadores deben aparecer en el orden: FIS, KAS, CAP, CAR y KAR. Crea también la matriz de adyacencia en MATLAB, asignándole la variable A.

b) (0.75p) Representa el grafo dirigido de la competición.

c) (1,5p) Establece la calsificación final. Detalla los pasos y los resultados que vayas obteniendo hasta conseguir la clasificación final

Respuesta

#### Problema 02. Huertos de 4 vecinos

Cuatro vecinos, cada uno con un jardín de vegetales, está de acuerdo en compartir sus productos. Uno cosechará frijoles (B), otro lechuga (L), otro tomates (T) y otro calabazas (Z). La tabla muestra qué fracción de cada cultivo recibirá cada vecino.

[Imagen: Tabla consumidor/productor (B, L, T, Z): B: 0, 1/4, 1/8, 1/6; L: 1/2, 1/4, 1/4, 1/6; T: 1/4, 1/4, 1/2, 1/3; Z: 1/4, 1/4, 1/8, 1/3.]

a) (1p) ¿Se trata de una economía abierta o cerrada? Justifica tu respuesta

b) (2,5p) ¿Qué precios deben cobrar los vecinos por sus cultivos, si cada persona debe quedar a la par y el cultivo de menor precio tiene un valor de $50? Explica detalladamente cada paso

Respuesta

#### Problema 03. Red de carreteras

Dispones de la red de carreteras entre seis pueblos. La matriz de distancias (en km) es:

[Imagen: Tabla de distancias entre A–F: A: 0, 120, 200, 300, 240, 400; B: 120, 0, 80, 220, 190, 360; C: 200, 80, 0, 140, 330, 260; D: 300, 220, 140, 0, 100, 180; E: 240, 190, 330, 100, 0, 150; F: 400, 360, 260, 180, 150, 0.]

a) (0,5p) Representa el grafo ponderado

b) (1,5p) Encuentra la ruta más corta desde A hasta F y su distancia total

c) (1,5p) Si la carretera entre E y F queda cortada (ese arco desaparece), ¿cuál es ahora la ruta más corta A→F y su distancia? Emplea la funcion rmedge para eliminar los nodos correspondientes en el grafo . Representa el grafo de nuevo

Respuesta

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Práctica 2 · Modelo B

*Fuente: `GRUPO B/PRACTICAS/PRACTICA 2/PR02_ModB.mlx`*

### PRÁCTICAS DE ÁLGEBRA

### PRÁCTICA 2

### MODELO B

ALUMNO:

INSTRUCCIONES

- Renombra el archivo como Apellido1_Apellido2_Nombre_ModB.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad

- Indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

- Debes dar correctamente los resultados numéricos en el formato que se pide. Se valorará que lo hagas con

- Table of Contents

- PRÁCTICAS DE ÁLGEBRA · PRÁCTICA 2 · MODELO B ·     Problema 01. Torneo 5 contra 5 en la Kings League. ·     Problema 02. Huertos de 5 vecinos ·     Problema 3. Red ferroviaria

#### Problema 01. Torneo 5 contra 5 en la Kings League.

La Kings League (cuyo nombre comercial es Kings League Infojobs por motivos de patrocinio), es una liga de fútbol 7 con sede principal en Barcelona, España, creada por el exfutbolista Gerard Piqué en 2022 en asociación con otras personalidades de internet y streamers, como el conocidísimo Ibai Llanos.

Esta revolucionaria Kings League sigue su camino, y acaba de celebrar a finales de 2024 su final four. Sin embargo, y a pesar de haber terminado la temporada, aprovechando el tirón que la competición está teniendo entre millones de seguidores, Ibai Llanos acaba de anunciar un nuevo formato corto, donde se enfrentarán los 5 equipos más queridos por el público:

- Porcinos FC (POR), capitaneados por el polifacético Ibai Llanos.

- 1K (1K), cuyo capitán es el exjugador del Real Madrid y de la Selección Española, Iker Casillas.

- Saiyans FC (SAI), capitaneados por el conocido creador de contenido, TheGrefg

- Jijantes FC (JIJ), capitaneados por el premiado periodista Gerard Romero.

- Los Troncos FC (TRO), cuyo capitán es el youtuber Perxitaa.

El desarrollo del torneo da los siguientes resultados:

- Los Saiyans FC pierden contra 1K y Jijantes FC.

- Los 1K de Casillas pierden contra los Jijantes FC de Romero.

- Ibai no tiene su día, y sus Porcinos pierden todos sus partidos.

- Jijantes FC solo pierden contra los Troncos de Perxitaa.

- Perxitaa consigue que sus Troncos solo pierdan contra Saiyans de TheGrefg y los 1K de Casillas.

NOTA: en el listado anterior, se entiende que si un equipo no ha perdido, entonces ha ganado. Es decir, no hay empates.

a) (0.75p) Escribe, mediante el editor de textos, una tabla que represente las victorias y derrotas de cada equipo en el torneo. En dicha tabla los equipos deben aparecer en el orden: SAI, 1K, POR, JIJ y TRO. Crea también la matriz de adyacencia en MATLAB, asignándole la variable A.

b) (0.75p) Representa el grafo dirigido de la competición.

c) (1,5p) Establece la calsificación final. Detalla los pasos y los resultados que vayas obteniendo hasta conseguir la clasificación final

Respuesta

#### Problema 02. Huertos de 5 vecinos

Cinco vecinos, cada uno con un jardín de vegetales, está de acuerdo en compartir sus productos. Uno cosechará manzanas (A), peras (P), uvas (U), melocotones (M) y ciruelas (C).. La tabla muestra qué fracción de cada cultivo recibirá cada vecino.

[Imagen: Tabla consumidor/productor (A, P, U, M, C): A: 1/2, 1/8, 1/5, 1/5, 1/6; P: 1/4, 1/8, 1/5, 1/5, 1/6; U: 1/8, 1/4, 1/5, 1/5, 1/6; M: 1/8, 1/4, 1/5, 1/5, 1/6; C: 0, 1/4, 1/5, 1/5, 1/3.]

a) (1p) ¿Se trata de una economía abierta o cerrada? Justifica tu respuesta

b) (2,5p) ¿Qué precios deben cobrar los vecinos por sus cultivos, si cada persona debe quedar a la par y el cultivo de menor precio tiene un valor de $100? Explica detalladamente cada paso. Redondea los resultados al entero más próximo

Respuesta

#### Problema 3. Red ferroviaria

Una empresa ferroviaria opera una red de trenes entre seis ciudades del norte de España: Burgos (A), León (B), Oviedo (C), Santander (D), Vitoria (E) y Logroño (F).

La siguiente tabla muestra las distancias directas (en km) entre ciudades conectadas. El valor 0 indica que no hay conexión directa.

[Imagen: Tabla de distancias por carretera (0 = sin conexión directa) entre A (Burgos), B (León), C (Oviedo), D (Santander), E (Vitoria), F (Logroño): A–B 125, A–D 115, A–E 95; B–C 120, B–F 250; C–D 160, C–F 200; D–E 130; E–F 150.]

a) (0,5p) Representa el grafo ponderado corrrespondiente indicando las distancias entre las ciudades

b) (1,5p) Encuentra la ruta más corta desde León hasta Santander y su distancia total.

c) (1,5p) Si la línea Vitoria–Santander queda temporalmente fuera de servicio, Emplea la funcion rmedge para eliminar los nodos correspondientes en el grafo y represéntalo. ¿cuál es ahora la ruta más corta de León a Santander y su distancia? Explica el resultado

Respuesta

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Práctica 3 · Modelo A

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 3/PR03_ModA.mlx`*

### PRÁCTICA 3

### Modelo A

INSTRUCCIONES:

- Renombra el archivo como PR03_Apellido1_Apellido2_Nombre_ModA.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Explica qué haces en cada paso de la resolución

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad. No copies/pegues lo que te indique Copilot sin saber lo que haces

- Separa e indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- Realiza todos los cálculos (aunque se puedan realizar directamente como búsqueda en una matriz) mediante script de Matlab y da los resultados con fprintf en el formato que se demanda en cada caso y con el texto necesario para responder a la pregunta

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

NOMBRE Y APELLIDOS:

#### Problema 1. Ascensor

En un edificio con bajo y cuatro pisos (1.º, 2.º, 3.º, 4.º) el ascensor siempre se mueve en cada periodo (no permanece en la misma planta).

[Imagen: Ilustración de un edificio de viviendas de 5 plantas.]

Se sabe que:

- Desde el bajo: el 25% de los viajes van al 1.º, el 25% al 2.º, el 30% al 3.º y el 20% al 4.º.

- Desde el 1.º: el 82% de los viajes bajan al bajo, el 8% suben al 2.º, el 5% suben al 3.º y el 5% suben al 4.º.

- Desde el 2.º: el 80% de los viajes bajan bajo, el 5% bajan al 1.º  el 7% suben al 3.º y el 8% sube al 4º

- Desde el 3.º: el 78% de los viajes bajan al bajo.º, el 12% bajan al 1º, el 5% bajan al 2º  y el 5% suben al 4.º.

- Desde el 4.º: siempre baja al bajo

Se pregunta:

a) (0,5p) Escribe la matriz de transición P que describe la situación descrita anteriormente mediante el editor de ecuaciones  y luego asÍgnale en Matlab la variable P. Ordena las filas/columnas segun el siguiente orden: bajo-1º-2º-3º-4º

b) (0,5p) Verifica que se trata de una matriz de transición y que es regular (debes comprobar dos cosas con Matlab)

c) (1p) ¿Cuál es la probabilidad de que, a largo plazo, el ascensor se encuentre en cada uno de los cuatro pisos y el bajo? Resuélvelo mediante autovalores. Da el resultado con fprintf en % redondeado al entero más  próximo

d) (1p) ¿Cuál es la probabilidad de que un residente se encuentre el ascensor en la planta baja al llegar el edificio? No utilices  los cálculos del apartado anterior y resuélvelo mediante un sistema lineal homogéneo. Da el resultado con fprintf en % y dos decimales

e) (0,5p) Antonio vive en el tercer piso, ¿cuál es la probabilidad de que cuando salga de casa por la mañana se encuentre el ascensor en su piso?

f) (0,5p) ¿A qué piso de los cuatro debe mudarse Antonio para que sea más probable que el ascensor se encuentre en su piso por la mañana?

Respuesta

#### Problema 2. Webs de divulgación cultural

Se consideran las siguientes seis páginas web pertenecientes a un ecosistema digital de divulgación cultural:

- ArteVivo

- CienciaAbierta

- CineForo

- EcoPlaneta

- HistoriaDigital

- LibroMundo

Cada página contiene enlaces a otras dentro de la misma red. Los enlaces se representan mediante flechas del tipo

Página A → Página B si A incluye un enlace que dirige a B.

La estructura de enlaces entre las seis páginas es la siguiente:

- ArteVivo → HistoriaDigital, LibroMundo

- CienciaAbierta → HistoriaDigital, EcoPlaneta

- CineForo → LibroMundo

- EcoPlaneta → CienciaAbierta

- HistoriaDigital → CienciaAbierta, CineForo

- LibroMundo → ArteVivo, EcoPlaneta

Se pide:

a) (0,5p) Escribe mediante el editor de ecuaciones la matriz de adyacencia. El orden de filas/columnas debe ser el mismo que en el enunciado (alfabético) Después emplea las funciones sparse y full para asígnarle la variable A en Matlab

b) (0,5p) Asigna la variable G al grafo dirigido de la matriz A y representalo gráficamente. Los nombres de las páginas deben aparecer en el grafo

c) (0,5p) Crea la matriz de Markov correspondiente y asignale la variable C. Verifica que se trata de una matriz de Markov

d) (0,75p) Incorpora un factor de atenuación $\delta =85%$ y calcula la nueva matriz estocástica y asígnale la variable M con Matlab. Verifica que M es una matriz estocástica

e) (0,75p) Calcula el vector de estado estacionario mediante autovalores y asígnale la variable q

f) (0,5p) Calcula de nuevo el vector de estado estacionario mediante la función correspondiente de Matlab y el mismo factor de atenuación, asígnale la variable qm

g) (0,75p) Verifica la diferencia entre ambos vectores de estado q calculado con autovalores y qm calculado con Matlab y explica el resultado. Reduce la diferencia entre ambos vectores de estado para que sea menor que ${10}^{-10}$, esxplica cómo lo haces y por qué.

h) (0,75p) Da la clasificación de las páginas a parir de q mediante fprintf e indicando el nombre de cada una de ellas, es decir, debe aparcer el texto: "La 1ª página es...(nombre de la página)"

i) (1p) Clasifica de nuevo las páginas, esta vez sin factor de atenuación (debes dar el resultado igual que en el apartado anterior y mostrando el vector de estado estacionario) y explica el resultado comparándolo con el obtenido anteriormente. Explica detalladamente qué haces y por qué.

Respuesta

_Imágenes embebidas: 1 (image1.png)_


## Práctica 3 · Modelo B

*Fuente: `GRUPO B/PRACTICAS/PRÁCTICA 3/PR03_ModB.mlx`*

### PRÁCTICA 3

### Modelo B

INSTRUCCIONES:

- Renombra el archivo como PR03_Apellido1_Apellido2_Nombre_ModB.mlx y súbelo a la tarea habilitada para ello en Canvas

- Responde debajo de donde se indica

- Explica qué haces en cada paso de la resolución

- Los cálculos con Matlab deberán emplear exclusivamente las funciones vistas en clase

- El empleo de cualquier otra IA que no sea Copilot de Matlab será considerado como plagio a efectos de aplicación de la normativa de la universidad. No copies/pegues lo que te indique Copilot sin saber lo que haces

- Separa e indica cada uno de los apartados en la respuesta

- No elimines las secciones

- Comienza siempre el script de cada problama con clc, clear, clf

- Escribe tu nombre y apellidos al comienzo del archivo en el lugar indicado

- Realiza todos los cálculos (aunque se puedan realizar directamente como búsqueda en una matriz) mediante script de Matlab y da los resultados con fprintf en el formato que se demanda en cada caso y con el texto necesario para responder a la pregunta

- El incumplimiento de cualquiera de las presentes instrucciones conllevará una disminución de puntos ebn la calificación final de la práctica

NOMBRE Y APELLIDOS:

#### Problema 1. Centro de atención telefónica

En una ciudad se celebran elecciones entre cinco partidos:

- Avance Popular

- Futuro Justo

- Horizonte Ciudadano

- Renovación Democrática

- Unión Verde Global

Se sabe que los votantes tienden a cambiar su preferencia de un partido a otro en cada elección, según las siguientes probabilidades observadas en encuestas:

- Desde Avance Popular: 35% permanece en Avance Popular, 25% cambia a Horizonte Ciudadano, 20% a Unión Verde Global, 10% a Futuro Justo, 10% a Renovación Democrática.

- Desde Futuro Justo: 45% permanece en Futuro Justo, 20% cambia a Horizonte Ciudadano, 15% a Unión Verde Global, 10% a Avance Popular, 10% a Renovación Democrática.

- Desde Horizonte Ciudadano: 50% permanece en Horizonte Ciudadano, 20% cambia a Unión Verde Global, 10% a Avance Popular, 10% a Futuro Justo, 10% a Renovación Democrática.

- Desde Renovación Democrática: 60% permanece en Renovación Democrática, 15% cambia a Horizonte Ciudadano, 10% a Unión Verde Global, 10% a Avance Popular, 5% a Futuro Justo.

- Desde Unión Verde Global: 40% permanece en Unión Verde Global, 30% cambia a Horizonte Ciudadano, 10% a Avance Popular, 10% a Futuro Justo, 10% a Renovación Democrática.

Se pregunta:

a) (0,5p) Escribe la matriz de transición P que describe la situación anterior mediante el editor de ecuaciones y luego asÍgnale en Matlab la variable P. Ordena las filas/columnas según orden alfabético de los partidos (como se dan en el enunciado)

b) (0,5p) Verifica que se trata de una matriz de transición y que es regular (debes comprobar dos cosas con Matlab)

c) (0,75p) Si el resultado en las elecciones de 2025 fue:

- Avance Popular: 18.3%

- Futuro Justo: 27,8%

- Horizonte Ciudadano; 31,4%

- Renovación Democrática:15,5%

- Unión Verde Global: 7%

¿Qué resultado se espera en las elecciones de 2030?. Da el resultado con fprintf indicando el % de votos de cada partido con dos decimales

d) (0,75p) ¿Quién ganará las elecciones en el largo plazo y con qué porcentaje de votos?  Resuélvelo mediante autovalores. Da el resultado con fprintf en % con dos decimales

e) (0,5p) Si Juan es simpatizante de Futuro Justo, ¿cuál es la probabilidad de que siga apoyando a ese partido en el largo plazo? No utilices  los cálculos del apartado anterior y resuélvelo mediante un sistema lineal homogéneo. Da el resultado con fprintf en % y dos decimales

f) (0,5p) ¿Qué partido debería elegir un votante para maximizar la probabilidad de que su preferencia se mantenga estable en el tiempo?

g) (0,5p) Da los resultados de las elecciones a largo plazo ordenando los partidos de mayor a menor porcentaje de votos

Respuesta

#### Problema 2. Red de blogs de viajes

Se consideran seis blogs de viajes que forman parte de una red colaborativa. Cada blog incluye enlaces a otros dentro del mismo ecosistema. Los enlaces se representan como:

Blog A → Blog B si A incluye un enlace que dirige a B.

Los blogs son:

- DiarioNomada

- EcoTurismo

- HistoriaViajera

- MochilaMundo

- RutasSecretas

- ViajeGourmet

La estructura de enlaces es la siguiente:

- DiarioNomada → MochilaMundo, EcoTurismo

- EcoTurismo → RutasSecretas

- HistoriaViajera → RutasSecretas, ViajeGourmet

- MochilaMundo → HistoriaViajera, DiarioNomada

- RutasSecretas → EcoTurismo, MochilaMundo

- ViajeGourmet → DiarioNomada

Se pide:

a) (0,5p) Escribe mediante el editor de ecuaciones la matriz de adyacencia. El orden de filas/columnas debe ser el mismo que en el enunciado (alfabético) Después emplea las funciones sparse y full para asígnarle la variable A en Matlab

b) (0,5p) Asigna la variable G al grafo dirigido de la matriz A y representalo gráficamente. Los nombres de las páginas deben aparecer en el grafo

c) (0,5p) Crea la matriz de Markov correspondiente y asignale la variable C. Verifica que se trata de una matriz de Markov

d) (0,75p) Incorpora un factor de atenuación $\delta =85%$ y calcula la nueva matriz estocástica y asígnale la variable M con Matlab. Verifica que M es una matriz estocástica

e) (0,75p) Calcula el vector de estado estacionario mediante autovalores y asígnale la variable q

f) (0,5p) Calcula de nuevo el vector de estado estacionario mediante la funcion correspondiente de Matlab y el mismo factor de atenuación, asígnale la variable qm

g) (0,75p) Verifica la diferencia entre ambos vectores de estado q calculado con autovalores y qm calculado con Matlab y explica el resultado. Reduce la diferencia entre ambos vectores de estado para que sea menor que ${10}^{-10}$, esxplica cómo lo haces y por qué.

h) (0,75p) Da la clasificación de las páginas a parir de q mediante fprintf e indicando el nombre de cada una de ellas, es decir, debe aparcer el texto: "La 1ª página es...(nombre de la página)"

i) (1p) Clasifica de nuevo las páginas, esta vez sin factor de atenuación (debes dar el resultado igual que en el apartado anterior y mostrando el vector de estado estacionario) y explica el resultado comparándolo con el obtenido anteriormente. Explica detalladamente qué haces y por qué.

Respuesta


## Libro Grossman · Capítulo 9: Cadenas de Markov y teoría de juegos

*Fuente: `Capitulo_09 Libro.pdf`*

#### Página 1

```text
CAPÍTULO

Shutterstock/Franck Boston

La teoría de juegos puede aplicarse al análisis de cualquier comportamiento competitivo, incluyendo juegos comunes.

Cadenas de Markov
y teoría de juegos
```

#### Página 2

```text
2  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

9.1 Juegos de dos personas: estrategias puras
La moderna teoría de juegos se desarrolló en los años de 1940 por John von Neumann y Oskar Mor-
gensten1 para proporcionar un marco matemático general para la economía. Las ideas principales de
esta teoría se extrajeron de juegos comunes como ajedrez, bridge, solitario, dominó y damas. La
teoría general se desarrolló sin ninguna referencia directa a un juego en particular. La teoría de juegos
puede aplicarse al análisis de cualquier comportamiento competitivo, incluyendo juegos comunes, la
economía, la guerra y la competencia biológica. En el estudio de la competencia biológica la teoría de
juegos ofrece un útil marco conceptual para entender el comportamiento.2
Muchos juegos conocidos tienen oponentes o competidores que realizan una secuencia de movi-
mientos de acuerdo con las reglas del juego. En algunos juegos, los movimientos consecutivos se
realizan con la información completa sobre las oportunidades del oponente (ajedrez). En otros jue-
gos, los movimientos se realizan simplemente por el azar (por ejemplo, lanzando una moneda) o el
jugador puede elegir sus movimientos deliberadamente de entre todos los movimientos posibles. El
juego puede terminar después de un número finito de movimientos con un ganador y un perdedor.
Generalmente hay un rendimiento para el ganador del juego, que puede ser un pago en efectivo o
simplemente la satisfacción del triunfo. (El rendimiento para las especies que juegan el juego de la
ecología es que se les permite seguir jugando).
Un juego está caracterizado por sus reglas. En algunos casos el juego puede ser tan complicado
que descubrir sus reglas puede ser un logro considerable. Considérese el problema de determinar las
reglas del ajedrez viendo cómo se juega. Después de cuatro o cinco juegos, las reglas principales se-
rían evidentes, pero sería necesario observar muchos más juegos para determinar todas las reglas.
Similarmente, las complejas interacciones de un sistema social humano o de un ecosistema pueden
pensarse como el desenvolvimiento de un juego con un número muy grande de jugadores: sus reglas
no se comprenden completamente.
Una vez que se conocen las reglas de un juego, el problema es determinar cómo deberían elegir
sus movimientos los jugadores y qué consecuencias existen para estos movimientos. En otras pala-
bras, los jugadores deben determinar sus estrategias mediante el análisis de las reglas del juego. El
resultado final de un juego generalmente dependerá de manera crítica de la elección de movimientos
de todos los jugadores. Para juegos complejos, puede resultar imposible analizar todas las posibilida-
des y, en este caso, los jugadores deben basarse en la experiencia, la intuición o el simple ensayo y
error para determinar sus movimientos.
En esta sección y en la siguiente se estudiará un juego sencillo entre dos personas con gran deta-
lle. Los conceptos presentados y los resultados obtenidos para este juego forman un modelo para el
análisis de juegos más generales. Se empezará con tres ejemplos de juegos de dos personas.

E JE M P LO 9.1.1  Monedas coincidentes

Dos jugadores, R y C, (denotados “renglón” y “columna”, respectivamente) cada uno coloca una
moneda frente a sí y al hacerlo determinan si una Cara o una Cruz está hacia arriba. Ninguno de los
jugadores sabe, inicialmente, si el otro jugador ha seleccionado una cara o una cruz. Entonces se
muestran las monedas. Si las monedas coinciden (esto es, ambas son caras o ambas son cruces), en-
tonces el jugador R le paga al jugador C 1 dólar. Si las monedas no coinciden, entonces el jugador C
le paga al jugador R 1 dólar.

John von Neumann y Oskar Morgensten, The Theory of Games and Economic Behavior, (Princeton, N.J.: Princeton University Press,
1944).
R.C. Lowontin, “Evolution and the Theory of Games”, Journal of Theoretical Biology, 1(1961):382-403.
L.B. Slobodkin, “The Strategy of Evolution”, American Scientist, 52(1964):342-357
```

#### Página 3

```text
9.1  Juegos de dos personas: estrategias puras  3

Podemos describir este juego en términos de una matriz de pagos (anotada desde el punto de
vista de R):

Jugador C
Cara Cruz
Cara –1  1
Jugador R
Cruz ( 1  –1)

Por lo tanto, por ejemplo, si el jugador R elige Cara y el jugador C elige Cruz, entonces el jugador R
gana 1 unidad (en este caso $1). Si tanto el jugador R como el jugador C seleccionan Cara, entonces
el jugador R pierde 1 unidad.

EJ EMPLO 9.1.2  Un juego de negocios

Big Save y Giant Foods son los únicos supermercados en Central City. El mercado minorista de ali-
mentos está compartido a partes iguales por estas dos empresas. Debido a un aumento en los costos,
Big Save desea aumentar sus precios. Sin embargo, si lo hace, teme perder parte del negocio en favor
de Giant Foods. Por otro lado, si baja sus precios y Giant Foods sube sus precios, la ganancia resul-
tante de clientes compensará por mucho la reducción de ganancia por unidad. Ambas empresas tie-
nen tres opciones: aumentar los precios, no hacer cambios, y bajar los precios.
Big Save puede controlar sus precios, pero no tiene control sobre lo que hace Giant Foods. Para
ayudarle a decidir qué hacer, contrata a un analista independiente en investigación de mercados,
quien obtiene la información en la tabla 9.1. Los números en la tabla representan porcentajes de au-
mentos o decrementos. Por ejemplo, si Big Save mantiene sus precios iguales y Giant Foods baja sus
precios, entonces Big Save perderá 3% del número total de clientes en favor de Giant Foods. Si Big
Save baja sus precios y Giant Foods sube sus precios, entonces Big Save ganará 10% de mercado.

Tabla 9.1 Elecciones de mercado para supermercados competidores
Elecciones
de Giant Food  Manter precios
Aumentar precios (I)  Bajar precios (D)
Elecciones  iguales (S)
de Big Save
Aumentar precios (I)  2  –2  –7

Manter precios iguales (S)  6  0  –3

Bajar precios (D)  10  5  3

Estos datos pueden representarse en la siguiente matriz de pagos:

Giant Foods
I S D
I  2 –2 –7
Big Save  S  6 0 –3
D ( 10 5 3)

¿Qué debe hacer cada supermercado? Se contestará esta pregunta más adelante en esta sección.
```

#### Página 4

```text
4  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

E JE M P LO 9.1.3  Un juego de guerra3

Durante la Segunda Guerra Mundial, una batalla crucial, llamada la Batalla del Mar de Bismark, se
peleó por el control de Nueva Guinea. El líder aliado, General Kenney, tenía reportes de inteligencia
que indicaban que los japoneses movilizarían un convoy de tropas y suministros del puerto de Rabaul,
en el extremo este de la isla de Nueva Bretaña, hacia Lae, justo al oeste de Nueva Bretaña en Nueva
Guinea. El líder japonés tenía dos opciones: tomar una ruta que pasaba por el norte de Nueva Breta-
ña o una que pasara por el sur. En la ruta del norte, la poca visibilidad era casi una certeza, mientras
que en la ruta del sur era casi seguro que el clima estaría despejado. En cualquier elección el viaje
duraría 3 días.
El General Kenney tenía la elección de concentrar el grueso de sus aviones de reconocimiento
en una u otra ruta. Una vez avistado, el convoy sería bombardeado hasta su llegada a Lae. En días de
tiempo de bombardeo, el equipo de Kenney estimó los resultados de varias opciones dadas en la tabla
9.2.

Tabla 9.2 Elecciones para japoneses y aliados (número de días de bombardeo)
Elecciones
de japoneses
Ruta del norte  Ruta del sur
Elecciones
de los aliados
Ruta del norte  2  2

Ruta del sur  1  3

De nuevo, estas opciones pueden representarse mediante una matriz de pagos.

Elecciones
japonesas
N S
N 2 2
Elecciones aliadas
S ( 1 3)

¿Qué rutas debían haberse elegido? Si el convoy japonés iba al norte, se expondría a ya sea 1 o 2 días
de bombardeo. Si iba a sur, enfrentaría 2 o 3 días de bombardeo. Ir al norte ciertamente luce mejor.
Desde el punto de vista del General Kenney, al concentrar sus fuerzas en el norte podía garantizar al
menos 2 días de bombardeo; en el sur solo podía garantizar 1 día.
Resulta que ambos comandantes eligieron la ruta del norte. Y como se verá muy pronto, estas
elecciones son consistentes con aquellas predichas por la teoría de juegos.
Estos ejemplos llevan a la siguiente definición:

D Definición 9.1.1
Juego de matrices
Sea A = (aij) una matriz de m × n. Considere un juego determinado por A, jugado entre dos
competidores R y C (renglones y columnas) de acuerdo con las siguientes reglas:

Este ejemplo está adaptado de un caso en Games and Decisions de R. Duncan Luce y Howard Raiffa (New York: Wiley, 1958),
64-65.
```

#### Página 5

```text
9.1  Juegos de dos personas: estrategias puras  5

1. En cada movimiento del juego R elige uno de los m renglones de A y C elige una de las n
columnas de A. Estas elecciones se hacen simultáneamente, y ningún competidor conoce
por adelantado la elección (o movimiento) del otro competidor.
2. Si R elige el i-ésimo renglón y C elige la j-ésima columna, entonces C le paga a R una can-
tidad aij. Si aij es negativa, esto se interpreta como que C recibe una cantidad –aij de R.

Este juego es el juego de matrices de m × n determinado por la matriz A = (aij) de m × n.

El juego de matrices puede terminar después de un movimiento o puede continuar por cualquier
número de movimientos. La matriz A = (aij) del juego se denomina la matriz de juego o la matriz de  Juego de matrices
pagos.  Matriz de pagos
Los siguientes ejemplos ilustran cómo pueden analizarse los juegos de matrices.

EJ EMPLO 9.1.4  Dos juegos de matrices

Describa los juegos de matrices con cada matriz de pagos.

1 0 1 0
1 2
a) A =  b) B =  0 –1 2 0
( –2 3)
( –1 0 3 1)

SOLUCIÓN ►
a) En este juego de matrices de 2 × 2 tanto R como C tienen dos opciones. Si R elige el primer
renglón, R gana 1 unidad si C elige la primera columna, y 2 unidades si C elige la segunda colum-
na. Si R elige el segundo renglón, pierde 2 unidades si C elige la primera columna, y gana 3 uni-
dades si C elige la segunda columna. Si C está jugando racionalmente, C elegirá la primera colum-
na. En este caso, R debería elegir el primer renglón. Con estas elecciones, R garantiza que ganará
al menos 1 unidad y C garantiza que al menos no perderá más de 1 unidad.
b) En este juego de matrices de 3 × 4 R tiene tres elecciones y C tiene cuatro elecciones. Al analizar
todas las elecciones posibles, es claro que a C le irá mejor si elige la segunda columna. Con esta
elección, C garantiza que no sufrirá pérdidas; a R le irá mejor si elige el primer renglón. Si se
hacen estas elecciones, no hay pagos entre los jugadores.

El juego de matrices general de m × n es un ejemplo de un juego de dos personas, de suma cero ya que
hay dos competidores y la suma de sus ganancias es cero. Las ganancias de un competidor son las
pérdidas del otro.
Los dos jugadores del juego de matrices A = (aij) de m × n deben analizar sus movimientos po-
sibles y decidir qué renglones o columnas jugar en los siguientes movimientos. Una estrategia pura  Estrategia pura
para R (o C) es la decisión de jugar el mismo renglón (o columna) en cada movimiento del juego. Se
dice que el jugador R (o C) usa una estrategia mixta si elige más de un renglón (o columna) en dife-  Estrategia mixta
rentes movimientos del juego. Si ambos jugadores emplean estrategias puras, el resultado de cada
movimiento es exactamente el mismo y el juego es completamente predecible. Por ejemplo, si R
siempre elige el i-ésimo renglón y C siempre elige la j-ésima columna, entonces en cada jugada R re-
cibe aij unidades de C. Cuando se usan estrategias mixtas, por uno o ambos jugadores, el juego es más
complicado. Por ejemplo, si R decide usar una estrategia mixta, aleatorizará la elección de renglones
a fin de aumentar su rendimiento.
Para una discusión más precisa de las estrategias se necesitan algunas ideas de la teoría de la
probabilidad.
```

#### Página 6

```text
6  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Un poco de teoría de la probabilidad
Supóngase que se realiza un experimento. Para cada posible resultado E del experimento se asigna un
número entre 0 y 1. Este número se llama la probabilidad del resultado E y está denotada por P(E).
Se subraya que 0 ≤ P(E)≤ 1. Por ejemplo, si se lanza una moneda justa, entonces P(cara) = P(cruz) =
. Otro ejemplo: un mazo de cartas tiene 52 cartas; de estas, 13 son corazones. Por tanto si se elige
una carta aleatoriamente del mazo, entonces
13 1
P(corazón) =  =
52 4
En un experimento la suma de probabilidades de todos los resultados posibles es 1.
Por supuesto, no todas las probabilidades se calculan tan fácilmente. Se han escrito libros ente-
ros sobre la materia. Sin embargo, no es necesario calcular probabilidades para comprender el papel
que la teoría de la probabilidad desempeña en la teoría de juegos.
Una variable aleatoria es una función que asigna un número a cada resultado de un experimento.
El valor esperado de una variable aleatoria es un promedio ponderado de los valores que puede adop-
tar. Para calcular el valor esperado se “acumula” la multiplicación de cada valor adoptado por la va-
riable aleatoria por la probabilidad de obtener dicho valor. Por ejemplo, supóngase que los posibles
1  5
valores adoptados por la variable aleatoria son 7, 5, –3, y 10 con probabilidades P(7) = , P(5) = ,
8  16
1  1
P(–3) = y P(10) = . (Nótese que estas probabilidades suman 1). Se tiene
2  16
2  5  8  1 14 + 25 – 24 + 10
Valor esperado = 7 ·  +5· –3·  + 10 ·  =
16  16  16  16  16
=

Se volverá ahora a la discusión de la estrategia.
¿Cuándo usar una estrategia pura? ¿Cuándo usar una estrategia mixta? Para responder a estas
preguntas debe precisarse más qué significa estrategia.

Vector de  El vector renglón de n componentes p = (p1 p2 … pn) es un vector de probabilidad si todas las
probabilidad  componentes son nonegativas y la suma de componentes es 1:

p1 + p2 + … + pn = 1

E JE M P LO 9.1.5  Seis vectores de probabilidad

Los siguientes son vectores de probabilidad.
1  4  1 1 1  1 1 3  1  1  1  5
a) (  b) (  c) (  d) (
5  5)  3 3 3)  8 2 8)  6  3  12  12)
1  1  2 1  4
e)
(0  2
2)
f) 0
( 5 3 0 14 )
Estrategia  Una estrategia para R en el juego con matriz A = (aij) de m × n es un vector de probabilidad con m
componentes p = (p1 p2 … pm), donde pi es la probabilidad de que R juegue el i-ésimo renglón
para i = 1, 2, …, m. Una estrategia para C es un vector de probabilidad de n componentes
q1
q2
p=
⋮
( )
qn
```

#### Página 7

```text
9.1  Juegos de dos personas: estrategias puras  7

donde qj es la probabilidad que C juegue la j-ésima columna para j = 1, 2, …, n.
Los jugadores R y C deben elegir sus estrategias p y q. En otras palabras, deben elegir las proba-
bilidades pi y qj que determinarán con qué frecuencia jugarán los diversos renglones y columnas. Por
ejemplo, si R y C juegan el primer renglón y la primera columna de A en cada movimiento, están ju-
gando las estrategias puras p = (1 0 … 0) y
q=
⋮
()
Si R y C juegan todos los renglones y columnas con probabilidades iguales, están jugando las estrate-
gias mixtas p = (1/m 1/m … 1/m) y
n
n
q=

()
⋮
n

Cada vector de probabilidad de m componentes es una posible estrategia para R, y cada vector de
probabilidad de n componentes es una posible estrategia para C.
Para ver cuándo puede usarse una estrategia pura, considérese el siguiente ejemplo.

E J EMPLO 9.1.6  Un juego de matrices con un punto de silla

Considérese el juego de matrices cuya matriz de pagos es

6 2 3
6 5 4
A=
7 –1 2
(  2 6 1  )
¿Qué estrategias deben adoptar R y C?

SOLUCIÓN ► R jugará para hacer la cantidad más pequeña que ganará lo más grande posible
(leer de nuevo el último enunciado). Si R juega el renglón 1, ganará al menos 2 unidades, no importa
qué columna juegue C. Si R juega el renglón 2, R ganará al menos 4 unidades. De la misma manera,
si R juega el renglón 3 o el renglón 4 ganará al menos –1 o 1 unidad respectivamente. Por lo tanto su
rendimiento mínimo máximo es de 4 unidades.
Pero, ¿qué debe jugar C? C quiere reducir su pérdida máxima. Si C juega la columna 1, puede
perder hasta 7 unidades; en la columna 2, C puede perder cuando mucho 6 unidades y en la columna
3 C puede perder cuando mucho 4 unidades. Se anotan estos números como sigue:

Mínimo renglón
C  ↓
6 2 3  ⟵ 2
R
6 5 4  ⟵ 4
7 –1 2  ⟵ –1
(
2 6 0  )  ⟵ 1
Máximo  ↑ ↑ ↑
columna ⟶ 7 6 4
```

#### Página 8

```text
8  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

El número 4 en la posición 2,3 es un mínimo en su renglón y un máximo en su columna. Dicho nú-
Punto de silla  mero se llama un punto de silla para la matriz de pagos A. En la siguiente sección se mostrará
que cuando el número aij es un punto de silla, las estrategias óptimas para R y C son, para R, jugar el
i-ésimo renglón y para C jugar la j-ésima columna. Por lo tanto, en el ejemplo, R debe adoptar la es-
trategia pura de jugar el segundo renglón [p = (0 1 0 0)] y C debe adoptar la estrategia pura de
jugar la tercera columna

q= 1
( 1)
Antes de terminar con este ejemplo, una observación que puede simplificar los cálculos. Cada núme-
ro del primer renglón de A es menor que o igual a la componente correspondiente en el segundo
renglón de A. Es decir, 6 ≤ 6, 2 < 5, y 3 < 4. Así, R nunca elegirá el primer renglón porque a R siem-
Renglón recesivo  pre le puede ir mejor si elige el segundo renglón. Al primer renglón se le llama renglón recesivo.
Igualmente, cada número en la primera columna de A es mayor que el número correspondiente en
la tercera columna de A; es decir, 6 > 3, 6 > 4, 7 > 2 y 2 > 1. De ahí que C nunca elegirá la prime-
ra columna, porque entonces C con seguridad perdería más que si hubiera elegido la tercera colum-
Columna recesiva  na (recordar que la ganancia de R es la pérdida de C). A la primera columna se le llama columna re-
cesiva.
Pueden eliminarse el renglón y la columna recesivos de futuras consideraciones. Si se hace así,
se obtiene la nueva matriz de pagos A′:

5 4
Aʹ = –1 2
( 6 1)
Igual que antes, 4 es un mínimo en su renglón y un máximo en su columna y es un punto de silla
para A′. El segundo renglón es recesivo, así que la matriz puede reducirse más para obtener A″ =
5 4  4
( 6 1); entonces A‴ = ( 1) ya que la primera columna de A″ es recesiva. Siguiendo, se observa que el
iv
segundo renglón de A‴ es recesivo, así A = (4). Evidentemente, esto lo más lejos que puede llegarse.

Ahora se describirá una estrategia general para jugar un juego de matrices en aquellos casos
donde hay un punto de silla.

Determinación de estrategias puras para un juego de matrices
Paso 1. Eliminar todos los renglones y columnas recesivos.
Observación  Paso 2. Encontrar el número más bajo en cada renglón. A este se le llama el mí-
nimo de renglón.
En el problema 33 se pide demostrar  Paso 3. Encontrar el número más alto en cada columna. A este se le llama el
que si aij y akl son puntos de silla para  máximo de columna.
A, entonces aij = akl. En este caso, se
mantendrá el mismo resultado en el
Paso 4. Buscar el punto de silla; este es un número que es tanto un mínimo de
Paso 4 si se usa cualquiera de los  renglón como un máximo de columna.4 Si aij es un punto de silla, enton-
puntos de silla.  ces R debe jugar el renglón i y C debe jugar la columna j. En este caso se
dice que el juego de matrices está estrictamente determinado.

A veces se denomina a un punto de silla como la solución minimax a un juego de matrices.
```

#### Página 9

```text
9.1  Juegos de dos personas: estrategias puras  9

Paso 5. Si no hay un punto de silla, entonces ya sea R o C (o ambos) deben jugar una
estrategia mixta. Este juego no está estrictamente determinado.

EJ EMPLO 9.1.7  Determinación de si un juego está estrictamente determinado

Determinar si un juego cuya matriz de pagos está dada está estrictamente determinado. Si es así,
determinar las estrategias óptimas para R y C.

3 0 5  1 6 2
1  0 5
a)  2 1 3  b)  4 2 3  c)
( 1 –5 0)
( 2 –1 –2)  ( 5 1 6)

SOLUCIÓN ►
a) Dado que cada número en el renglón 3 es menor que o igual a el número correspondiente en el
renglón 2, el renglón 3 es recesivo. Igualmente, cada número en la columna 1 es mayor que el
número correspondiente en la columna 2, entonces la columna 1 es recesiva. Al eliminar el ren-
glón 3 y la columna 1 se obtiene

Mínimo renglón
↓
0 5  0
( 1 3)  1
Máximo
columna ⟶ 1 5

Se observa que 1 es en mínimo en este renglón y el máximo en esta columna, así 1 es un punto
de silla y el juego está estrictamente determinado. Dado que 1 es la componente 2,2 de la ma-
triz de pagos, las estrategias óptimas son p = (0 1 0) y

q= 1
( 0)
Es decir, R juega el renglón 2 y C juega la columna 2.5
b) No hay renglones o columnas recesivos. Al reescribir la matriz de pagos se tiene

Mínimo renglón
↓
1 6 2  1
4 2 3  2
( 5 1 6)  1
Máximo
columna ⟶ 5 6 6

En este caso no hay punto de silla porque ningún número es tanto un mínimo en su renglón como
un máximo en su columna. Este juego no está estrictamente determinado y se requiere una estra-
tegia mixta.

5  0 5  0
Se observa más adelante que en ( 1 3 ) la segunda columna es recesiva, entonces la matriz se reduce a ( 1 ). Pero ahora el primer
renglón es recesivo y se termina con la matriz de 1 × 1 (1). Este es el punto de silla.
```

#### Página 10

```text
10  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

c) El renglón 2 es recesivo, como la columna 1. El juego de matrices se reduce a (0 5) y 0 es un
punto de silla. Obsérvese que hay dos ceros en la matriz de pagos pero únicamente el cero en la
posición 1,2 es un punto de silla. El juego está estrictamente determinado y las estrategias ópti-
mas son p = (1 0) y

q=  1
( 0)
Es decir, R juega el renglón 1 y C juega la columna 2.

E JE M P LO 9.1.8  Monedas coincidentes (continuación)

En el juego de las monedas coincidentes del ejemplo 1 la matriz de pagos es

Mínimo renglón
Cara  Cruz  ↓
Cara –1 1  –1
Cruz ( 1 –1)  –1
Máximo
columna ⟶  1  1

No hay puntos de silla, así que se requiere de una estrategia mixta. Se encontrará la estrategia óptima
en la siguiente sección.

E JE M P LO 9.1.9  Un juego de negocios (continuación)

En el juego de negocios del ejemplo 2 la matriz de pagos es

Mínimo renglón
I S D  ↓
I  2 –2 –7  –7
S  6 0 –3  –3
D ( 10 5 3)  3
Máximo
columna ⟶ 10  5  3

En este caso 3 es un punto de silla, así que Big Save debe jugar el renglón 3 y Giant Foods debe jugar
la columna 3. Es decir, si los datos son correctos, ambos deben bajar los precios. Obsérvese que los
renglones 1 y 2 son recesivos y las columnas 1 y 2 son recesivas, así que el juego de matrices se redu-
ce a la matriz de pagos de 1 × 1 (3).

E JE M P LO 9.1.10  Un juego de guerra (continuación)

En el juego de guerra del ejemplo 3 la matriz de pagos es

Norte Sur
Norte 2  2
Sur ( 1  3)

El 2 en la posición 1,1 es un punto de silla, así que ambos comandantes debían elegir la ruta norte.
En efecto, esto es lo que sucedió.
```

#### Página 11

```text
9.1  Juegos de dos personas: estrategias puras  11

En la siguiente sección se usará un teorema de Von Neumann para demostrar por qué siempre
deben usarse las estrategias puras cuando hay un punto de silla. En dicha sección también se demos-
trará cómo encontrar las estrategias óptimas cuando un juego de matrices no está estrictamente de-
terminado.

PROBLEMAS 9.1

En los problemas del 1 al 10 determine si el vector dado es un vector de probabilidad.
1  1  1  1
1. (  2.
2  2)  (3 3)
1  1  1  1  1  1  1  1
3. (  4.
5  5  5  5)  (4 4 4 4)
1  1  1  1  5
5. (  –  1  6.
2  2  )  (3 4 12)

7. (1  0  0  0)  8. (0  1  0  1)

1  2  3  4  5
9. (0.235  0.361  0.162  0.242)  10.  (10 10 10 10 10)
En los problemas de 11 al 20 está dada la matriz de pagos para un juego. Determine si el juego está
estrictamente determinado y, si es así, encuentre las estrategias óptimas para R y C.

1 1 1  0 0 0
11.  2 2 3  12.  1 1 2
( –2 4 5)  ( –3 3 4)

4 6 –2  5 6 4 7
13. 3 5 7  14.  3 2 3 1
( 2 –3 1)  ( 4 6 2 5)

1 6  2 –3 –2 0
15.  3 4  16.  –4 –6 –1 2
( 5 5)  ( 0 –3 2 5)

1  6 2  4
2 –3 –2 0
–1  3 7  5
17.  –4 –6 –1 2  18.
( 0 –2 2 –5)  (  2
1 7
0 –5
4)
4  2  1  3  1  0  0  1
6  4  3  5  0  1  0  1
19.  20.
(  2
0  )  (  1
1)
En los problemas 21 al 30 formule cada situación como un juego de matrices de dos personas y anote
la matriz de pagos para dicho juego. Si el juego está estrictamente determinado, encuentre la estrate-
gia óptima para cada jugador.
```

#### Página 12

```text
12  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

21. Dos personas simultáneamente muestran, cada una, uno o dos dedos. Si el número total de
dedos es par, R le paga a C dicho número de dólares. Si el número es non, C le paga a R dicho
número de dólares.

22. Repita el problema 21, con la excepción de que cada jugador muestra cuatro o cinco dedos.

23. Repita el problema 21, con la excepción de que cada jugador muestra uno, dos o tres dedos.

24. Repita el problema 21, con la excepción de que cada jugador muestra uno, dos, tres, cuatro o
cinco dedos.

25. Dos estaciones de gasolina compiten por el negocio en un pueblo pequeño. La Estación A ha
determinado que si sube sus precios, perderá 1% del mercado si B sube sus precios, 3% del
mercado si B no hace ningún cambio y 11% del mercado si B baja sus precios. Si A no hace
ningún cambio, entonces gana 4% si B aumenta sus precios y pierde 5% si B los baja. No hay
cambios en la cuota de mercado si ambas estaciones no cambian sus precios. Finalmente, si A
baja sus precios, gana 9% si B sube sus precios, gana 3% si B se mantiene y pierde 1% si también
B baja sus precios.

26. Se está construyendo un nuevo centro comercial en Centerville. Dos tiendas de ropa estilo va-
quero, Vince’s y Readywear, comparten el mercado en Centerville y sus alrededores. Si una de
las tiendas se muda al nuevo centro comercial, ganará el 80% del mercado. Si ambas o ninguna
se mudan, continuarán dividiéndose el mercado en partes iguales.

27. Un distrito del Congreso está dividido en dos regiones. Hay un candidato demócrata y un can-
didato republicano compitiendo. Las regiones tienen 60 000 votantes y 40 000 votantes respec-
tivamente. Quedan 2 días de campaña y cada candidato puede pasar 0, 1 o 2 días en cada re-
gión. Los analistas políticos han estimado que si los candidatos pasan el mismo número de días
en una región, se dividirán los votos de dicha región. Sin embargo, si un candidato pasa 1 o 2
días más que su oponente en una región, obtendrá 53% o 57% de los votos de dicha región,
respectivamente.

28. En diversos experimentos, los cuervos y los periquitos han aprendido a reconocer números
hasta 7. Se propone el siguiente experimento: la dieta de un cuervo R y de un periquito C se de-
terminará mediante un juego de matrices. Se muestran tres cartas a cada ave, marcadas con 2,
4 y 7 puntos. Si cada ave elige la misma carta, entonces R recibe de la dieta de C un número de
gusanos equivalente a dos veces el número de puntos en la carta. Si las cartas elegidas son dife-
rentes, entonces C recibe de la dieta de R un número de gusanos igual a la diferencia del núme-
ro de puntos en la carta. Se asume que los movimientos se realizan de forma independiente.

29. Peter quiere llamar a su novia Roberta. Está planeando llamarla en la noche cuando el precio
de una llamada de 3 minutos de estación a estación es de 2 dólares y una llamada de 3 minutos
de persona a persona es de 4.50 dólares. Si Roberta no está en su casa, él sabe que puede lla-
marle al día siguiente en su trabajo y que pagará la tarifa diurna de 3 dólares para una llamada
de 3 minutos de estación a estación. Si hace una llamada de estación a estación y Roberta está
en su casa, Peter ahorra dinero. Por otro lado, si contesta la compañera de habitación de Ro-
berta y ella no está en su casa, Peter pierde dinero.

30. Un granjero cultiva tomates. Mientras más tiempo se quedan los tomates en el racimo, se pon-
drán más rojos y será más alto el precio que puede cobrar por bushel.6 Por otro lado, si llega una
helada, se echarán a perder algunos tomates y descenderá el precio promedio por bushel. Si

Un bushel es una unidad de volumen imperial (Reino Unido) y estadounidense que se usa para medir productos agrícolas; equivale
a 8 galones.
```

#### Página 13

```text
9.1 Juegos de dos personas: estrategias puras  13

corta los tomates el 25 de agosto, puede estar seguro de que no habrá helada y obtendrá un
precio promedio por bushel de 8 dólares. Si espera hasta el 5 de septiembre, obtendría 11 dóla-
res por bushel si no hay helada, y 5 dólares por bushel si hay una helada.
31. La empresa llantera Maxigrip Tire tiene un conflicto con su sindicato. Cada grupo (la gerencia
y los trabajadores) tiene una elección entre cuatro posturas de negociación: dura, mantenerse
firmes; un enfoque razonable basado en la lógica; dejar el asunto a los abogados para buscar
una solución legal al conflicto; ser conciliador. Un experto en relaciones laborales ha determi-
nado que la empresa pagará salarios semanales más altos dependiendo de las posiciones que
ella y el sindicato adopten. Las diversas posibilidades están dadas en la tabla.

Incremento semanal para la empresa llantera por trabajador (en dólares)
Posición
del sindicato
Dura  Lógica  Legal  Conciliatoria
Posición
de la empresa
Dura  20  24  15  17

Lógica  35  30  26  28

Legal  15  23  20  30

Conciliatoria  40  35  23  28

¿Qué debe hacer el sindicato?
32. La Universidad de Montana (UM) juega futbol americano cada año contra la Universidad Es-
tatal de Montana (UEM). En un down, el mariscal de campo de la UM tiene la opción de cinco
jugadas: carrera halfback, carrera fullback, pase corto, pase largo y draw play. La defensa de
UEM tiene cuatro elecciones: defensa normal, defensa preventiva contra un pase largo, defensa
preventiva contra un pase corto, blitz. Un entrenador estimó el número aproximado de yardas
que se ganarían con todas las combinaciones de las opciones ofensivas y defensivas. Dichas
estimaciones están dadas en la tabla.

Yardas por ganar esperadas
UEM  Preventiva  Preventiva
Normal  Blitz
UM  (corto)  (largo)
Carera HB  2  4  8  6

Carrera FB  5  5  7  9

Pase corto  4  0  6  –2
Pase largo  8  3  0  –4
Draw Play  –1  2  4  10

¿Qué debe hacer cada equipo?
33. Demuestre que si una matriz de pagos tiene dos puntos de silla aij y akl, entonces aij = akl. [Pis-
ta: Anote la matriz A y explique qué está implicado en el hecho de que aij es el mínimo en el
i-ésimo renglón y el máximo en la j-ésima columna. Haga lo mismo para akl.]
```

#### Página 14

```text
14  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

9.2 Juegos de dos personas: estrategias mixtas
En la sección 9.1 se mostró cómo determinar las estrategias óptimas cuando un juego está estricta-
mente determinado. Sin embargo, a fin de demostrar que una estrategia es óptima es necesario res-
ponder a la pregunta “¿óptima con respecto a qué?”. En esta sección se demostrará cómo calcular el
rendimiento esperado para los jugadores en un juego. Entonces, una estrategia es óptima para R si
optimiza el rendimiento de R. Se iniciará con un ejemplo.

E JE M P LO 9.2 .1  Cálculo del rendimiento esperado
3 2
Considérese el juego cuya matriz de pagos es A =
( –2 4). ¿Cuál es el rendimiento esperado para
1  2  5
R si R adopta la estrategia p = (  y C adopta la estrategia q =  ?
3  3)  ( 3)  5

SOLUCIÓN ►  Aquí R tiene cuatro posibles rendimientos: 3, 2, –2 y 4. Recibirá 3 unidades,
por ejemplo, si elige el primer renglón (con probabilidad ) y C elige la primera columna (con
probabilidad ). Dado que se asume que ni R ni C saben lo que el otro está haciendo, los eventos
{1er. renglón} y {1a. columna} son independientes.7 Por lo tanto,
1 2 2
P(1er. renglón ∩ 1a. columna) = P(1er. renglón) ⋅ P(1a. columna) = ⋅ =
3 5 15
y tenemos
P(3) = P(rendimiento de 3) =
Igualmente,
1 3 1
P(2) = P(1er. renglón ∩ 2a. columna) =
⋅ =
3 5 5
2 2 4
P(–2) = P(2o. renglón ∩ 1a. columna) = ⋅ =
3 5 15
y
2 3 2
P(4) = P(2o. renglón ∩ 2a. columna) = ⋅ =
3 5 5
Ahora, si E(p, q) denota el valor esperado de la variable aleatoria que adopta valores iguales a los
posibles rendimientos de R, se tiene
E(p, q) = 3P(3) + 2P(2) + (–2)P(–2) + 4P(4)
2  1  4  2 28
=3⋅  + 2 ⋅ – 2 ⋅ + 4 ⋅ = ≈ 1.87
15  5  15  5 15
Ahora se observa que
1  2  3 2  5
pAq = (
3  )
3 ( –2 4)( 3)
1  2  5  12 16 28
=(  =  +  = ≈ 1.87
3  3)(  5
)  15 15 15

Por definición, dos eventos A y B son independientes si P(A ∩ B) = P(A)P(B).
```

#### Página 15

```text
9.2  Juegos de dos personas: estrategias mixtas  15

El Ejemplo 1 puede generalizarse.
Supóngase que R utiliza estrategias p y que C utiliza estrategias q para el juego cuya matriz de  Rendimiento
pagos es la matriz A de m × n. El rendimiento esperado para R, denotado por E(p, q), está dado por  esperado

E(p, q) = rendimiento esperado = pAq  (1)

Nota
EJ EMPLO 9.2. 2  Cálculo del rendimiento esperado  Dado que A es una matriz de m × n y q
es un vector r de n componentes (una
¿Cuál es el rendimiento esperado para R en el juego de matrices de 3 × 4  matriz de n × 1), el producto Aq es una
matriz de m × 1 y pAq es entonces una
matriz de (1 × m) × (m × 1) = 1 × 1, o
2 –1 3 0  simplemente, un número real.
A=  3 –2 –1 2
( 1 4 3 –3)
1  1  1  8
a) si R adopta la estrategia (  y C adopta la estrategia  ?
3  2  6)
()

b) si R y C eligen el 2o. renglón y la 3a. columna, respectivamente?
SOLUCIÓN ►  4
2 –1 3 0  1
1  1  1  8
a)  E(p, q) = (  3 –2 –1 2
6)
3  2
( 1 4 3 –3)
()
1  1  1  7
=(  11  =  = 0.875
3  2  6)  8  8
( )
– 38

b) Aquí p = (0  1  0) y q =  . Entonces
()  1

2 –1 3 0  3
E(p, q) = (0  1  0) 3 –2 –1 2  = (0  1  0) –1 = –1
( 1 4 3 –3) 1
0  ()  ( 3)

Esta es, por supuesto, la componente 2,3 de A.
La pregunta básica permanece: ¿Cómo eligen R y C las estrategias? Esta pregunta se responde
parcialmente mediante un resultado fundamental descubierto por Von Neumann.
```

#### Página 16

```text
16  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Teorema 9.1.1 Teorema de Von Neumann
Para cualquier juego de matriz A de m × n, existen estrategias p0 y q0 y un número v tal que
E(p0, q) ≥ v para cualquier estrategia q y E(p, q0) ≤ v para cualquier estrategia p. Las estrate-
gias p0 y q0 se denominan estrategias óptimas para R y C, respectivamente, y el número v se
denomina el valor del juego.

¿Por qué p0 y q0 son óptimas? Porque si R elige p0 entonces sabe que ganará al menos v unidades. Si
elige alguna otra estrategia, entonces C puede elegir q0 y asegurar que R ganará cuando mucho v uni-
dades. De este modo, asumiendo que C juegue inteligentemente, a R puede irle mejor si elige la estra-
tegia p0. Un razonamiento similar demuestra que la estrategia óptima para C es q0.
Usando el teorema de Neumann es posible demostrar que

Si aij es un punto de silla, entonces el valor del juego es aij y las estrategias óptimas son las
estrategias puras de jugar el renglón i y la columna j con probabilidad 1.

Esto justifica jugar las estrategias puras dictadas por un punto de silla.
El teorema de Von Neumann es limitado en tanto que dice cuáles son las estrategias óptimas y
el valor del juego, pero no dice cómo calcularlos. Resulta que es relativamente sencillo calcularlos
cuando el juego de matrices es una matriz de 2 × 2. Otros casos resultan más difíciles y se discuten
en la siguiente sección.
Sea
a11 a12
A=  (2)
( a21 a22)
Estrategias óptimas para un juego de matrices de 2 × 2. Si la matriz en (2) no está estrictamente de-
terminada, entonces las estrategias óptimas para R y C son

a22 – a21  a11 – a12
p0 = (  (3)
a11 + a22 – a12 – a21 a11 + a22 – a12 – a21)

y

a22 – a21
a11 + a22 – a12 – a21
q0 =  a11 – a12  (4)
(  a11 + a22 – a12 – a21  )
El valor del juego es

a11a22 – a12a21
v=  (5)
a11 + a22 – a12 – a21

En el problema 44 se pide demostrar por qué las ecuaciones (3), (4) y (5) son válidas.
```

#### Página 17

```text
9.2  Juegos de dos personas: estrategias mixtas  17

EJ EMPLO 9.2. 3  Estrategias óptimas para el juego de las monedas coincidentes

Determinar las estrategias óptimas y el valor del juego de las monedas coincidentes del ejemplo 9.1.1
ubicado al inicio del capítulo.

SOLUCIÓN ► La matriz del juego es

Cara  Cruz
Cara –1 1
Cruz ( 1 –1)

Entonces a11 = –1, a12 = 1, a21 = 1, a22 = –1 y, de (3), (4) y (5),
–1 – 1  –1 – 1  1  1
p0 = (  =
–1 – 1 – 1 – 1 –1 – 1 – 1 – 1) (2  2)

–1 – 1  1
–1 – 1 – 1 – 1  2
q0 =  =
–1 – 1
(  ) ()
–1 – 1 – 1 – 1  2

y
(–1)(–1) – (1)(1)
v=  =0
–1 – 1 – 1 – 1
Por lo tanto, en este muy sencillo juego a R y C les irá mejor si eligen una cara o cruz con igual pro-
babilidad. El valor de este juego es cero.

Un juego es imparcial si su valor es cero.  Juego imparcial
Las monedas coincidentes es un ejemplo de juego imparcial.

EJ EMPLO 9.2. 4  Estrategias óptimas para un juego de guerra

Para el juego de guerra del ejemplo 9.1.3 se modificarán los supuestos para obtener la tabla 9.3.

Tabla 9.3 Elecciones para japoneses y aliados
(número de días de bombardeo)
Elecciones
japonesas
Ruta del norte  Ruta del sur
Elecciones
aliadas
Ruta del norte  2  1

Ruta del sur  1  3

¿Cuáles son ahora las estrategias óptimas?
2 1
SOLUCIÓN ► La matriz del juego es (  y no hay un punto de silla, de modo que el
1 3)
juego no está estrictamente determinado. Tenemos a11 = 2, a12 = 1, a21, y a22 = 3. Por lo tanto
3–1  2–1  2  1
p0 = (  =
2 + 3 – 1 – 1 2 + 3 – 1 – 1) (3  3)
```

#### Página 18

```text
18  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

3–1  2
2+3–1–1  3
q0 =  =
2–1
(  ) ()
2+3–1–1  3

y
2·3–1·1  5
v=(  =
2 + 3 – 1 – 1) 3
Esto significa que si este juego se repitiera muchas veces, ambos comandantes elegirían la ruta norte
2  1  5
del tiempo y la ruta sur del tiempo. Habría un promedio de días de bombardeo. Por supuesto,
3  3  3
este procedimiento no se realizará más de una vez. Por lo tanto, la interpretación correcta del vector
2 1  2
p0 = (  es que el General Kenney debe ir al norte con de probabilidad. Él podría hacer esto,
3 3)  3
por ejemplo, colocando dos N y una S en una caja y elegir una letra aleatoriamente. Su número espe-
rado de días de bombardeo sería entonces ; sin embargo, él solo podría tener 1, 2 o 3 días de bom-
bardeo.

E JE M P LO 9.2 .5  Evaluación de riesgos en procedimientos médicos

Como es bien sabido, muchos procedimientos médicos involucran un riesgo considerable para el
paciente y solo deben asumirse cuando el paciente está expuesto a un riesgo mayor si no se le da
el tratamiento. ¿Cómo se determina en una situación dada qué riesgo es mayor? Este problema se
complica aún más cuando no hay una certeza completa de que el paciente padece la enfermedad
sospechada. Por ejemplo, con frecuencia se realiza una cirugía para extirpar tumores, incluso cuando
solo existe una posibilidad relativamente pequeña de que el tumor resulte maligno. ¿Qué tan grande
debe ser esta probabilidad antes de que pueda recomendarse la cirugía?
Para analizar esta cuestión, supóngase que la probabilidad de que un paciente tenga una enfer-
medad particular es q1. (Esta probabilidad ha sido determinada mediante el desempeño de varias
pruebas). El tratamiento para esta enfermedad es una operación importante. Si el paciente padece la
enfermedad pero no se le opera, puede esperar vivir 5 años, pero si el paciente se opera, puede esperar
vivir 20 años. Si el paciente no padece la enfermedad, puede esperar vivir 25 años con la operación y
30 años sin la operación. La decisión de operarlo o no evidentemente depende de q1, la probabilidad
de que el paciente padezca la enfermedad. Si q1 = 0, entonces el paciente no padece la enfermedad y
no debe operársele. Si q1 = 1, el paciente padece la enfermedad y debe operársele. ¿Cuál es el valor
más pequeño de q1 para el cual la operación es recomendable?

SOLUCIÓN ► Este problema puede analizarse como un juego de matrices. Defina

20 25
A=
( 5 30)

como la matriz del juego. El paciente “juega” los renglones; el renglón 1 corresponde a hacerse la
operación y el renglón dos corresponde a no hacerse la operación. El oponente, la naturaleza, juega
las columnas; la columna 1 corresponde a enfermedad y la columna 2 corresponde a no enfermedad.
La estrategia de la naturaleza es

q1
q=
( 1 – q1 )
```

#### Página 19

```text
9.2  Juegos de dos personas: estrategias mixtas  19

donde q1 es la probabilidad de que el paciente padezca la enfermedad. El paciente debe jugar una es-
trategia pura, pero de momento, supóngase que la estrategia del paciente es p = (p1 p2) =
(p1 1 – p1). El rendimiento esperado (en años de vida) es

20 25  q1
E(p, q) = (p1  1 – p1)
( 5 30)( 1 – q1 )

20q1 + 25(1 – q1)
= (p1  1 – p1)
( 5q1 + 30(1 – q1) )
= 20p1q1 – 5p1 – 25q1 + 30

Si se opera al paciente, entonces p = (1 0) y E(p, q) = 25 – 5q1. Si no se opera, entonces p = (1 0)
y E(p, q) = 30 – 25q1. El paciente debe operarse si 25 – 5q1 > 30 – 25q1, es decir, si 20q1 > 5, o q1 >
0.25. Esto significa que el paciente debe operarse si la probabilidad de que padezca la enfermedad es
mayor al 25%. Si la información disponible indica que la probabilidad de la enfermedad es, por ejem-
plo, 15%, no debe realizarse la operación. Debe obtenerse más información antes de recomendar la
operación.

E J EMPLO 9. 2. 6  Eliminación de un renglón y una columna recesivos a fin de
determinar las estrategias óptimas

Considere un juego cuya matriz de pagos es

4 5 7
A=  1 2 4
( 5 8 3)
Este no es un juego de 2 × 2 y no tiene punto de silla, así que no está estrictamente determinado. Sin
embargo, el renglón 2 es recesivo. A R siempre le irá mejor si elige el renglón 1, así que nunca elegirá
el renglón 2. Igualmente, la columna 2 es recesiva y C nunca la elegirá. Al eliminar el renglón y la
columna recesivas, se obtiene

4 7
A′ =
( 5 3)

Las estrategias óptimas y el valor del juego son, de (3), (4) y (5),

2  3  5  23
p′0 = (  ,  q′0 =  y  v=
6)
()
5  1  5

Por lo tanto
2  3
p0 = (  0  y  q0 =
5)
(45)
son las estrategias óptimas para A. El valor del juego sigue siendo  .
```

#### Página 20

```text
20  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Se cerrará esta sección con un magnífico ejemplo del uso de la teoría de juegos aplicado a la fi-
losofía.8

E JE M P LO 9.2 .7  Libre albedrío

¿Jugamos un papel en la dirección de nuestras vidas? ¿O estamos destinados a llevar a cabo un plan
predestinado y movernos a lo largo de la banda transportadora del destino? Una de las columnas de
Martin Gardner que generó una respuesta considerable de sus lectores fue su discusión del libre albe-
drío y el determinismo, ilustrada por lo que se conoce como la paradoja de Newcomb.
La paradoja involucra la habilidad de un “Ser superior” para predecir el comportamiento con
exactitud. Este Ser puede ser un psíquico, un viajero del tiempo, Dios u otra entidad presente.
Una persona está frente a dos cajas. La caja A contiene 1 000 dólares; la caja B contiene ya sea
1 millón de dólares o nada. La persona puede tomar lo que está en ambas cajas, o puede tomar solo
lo que está en la caja B. En algún momento antes de que la persona tome una decisión, el Ser superior
hace una predicción acerca de la elección. Si el Ser cree que la persona solo tomará la caja B, enton-
ces pondrá 1 millón en ella. Si predice que la persona tomará ambas cajas, dejará la caja B vacía. El
Ser no es necesariamente infalible, pero es un predictor extremadamente exacto.
¿Cuál es la elección de la persona? Si toma ambas cajas, el Ser habrá predicho esto y dejado la
caja B vacía. Si la persona solo toma la caja B, obtendrá 1 millón de dólares. En su experiencia, el Ser
nunca se ha equivocado. Tomar la caja B parece ser la elección correcta.

El Ser  El Ser
predice B  predice A y B
Tomar B  $1 000 000  $0

Tomar A y B  $1 001 000  $1 000

Sin embargo, considérese otro argumento. El Ser hizo su predicción hace una semana, o tal vez el día
en el que la persona nació. O puso $1 millón en la caja B o no lo puso, y el dinero no desaparecerá.
Entonces tiene más sentido tomar ambas cajas, porque si la caja B tiene dinero, la persona obtiene
$1 001 000; si no, la persona al menos tiene $1 000. Si la persona solo toma la caja B, incluso hay una
remota posibilidad de que la persona no obtenga nada.
Gardner sugiere que una forma de considerar la paradoja es usar una matriz de pagos. Si se con-
sidera el resultado de ambas elecciones a la luz de las predicciones del Ser, parece que la mejor op-
ción es tomar ambas cajas; a esa opción le asigna el pago máximo más alto ($1 001 000) así como el
pago mínimo más alto ($1 000). Obsérvese que $1 000 es un punto de silla.
Sin embargo, otro enfoque de la teoría de juegos, multiplicar los diversos resultados de cada
elección por la probabilidad de que sucederán, resulta en la conclusión opuesta. Incluso si se asume
que el predictor está en lo correcto el 90% del tiempo, el rendimiento esperado de tomar ambas cajas
es 90% de $1 000 más 10% de $1 001 000, equivaliendo a $101 000. En otras palabras, si la persona
juega el juego diez veces, la toma promedio sería de $101 000. Tomar solo la caja B arroja el 90% de
$1 000 000 más 10% de cero, equivaliendo a $900 000. Es mejor solo tomar la caja B incluso si el Ser
está en lo correcto solo un poco más de la mitad del tiempo.
La paradoja está basada en los conceptos contradictorios del libre albedrío y el determinismo.
Para aquellos que sienten que sus elecciones están totalmente comprometidas con un presente futuro
o son completamente dependientes de lo que el pragmatista del siglo XIX, William James llamó el
“impulso del pasado”, la única elección es tomar la caja B, si así puede llamársele, porque un Ser
omnisciente o u viajero del tiempo estaría consciente de dichas fuerzas.

Usado con permiso de Martin Gardner. Para una discusión más amplia de la paradoja de Newcomb, ver capítulos 13 y 14 de Knotted
Doughnuts and Other Mathematical Entertainments de Gardner (W.H. Freeman & Co., 1986).
```

#### Página 21

```text
9.2 Juegos de dos personas: estrategias mixtas  21

Para aquellos que creen que pueden hacerse elecciones independientes —que existe, no importa
qué tan infinitesimal sea, una libertad de acción más allá de lo ordenado por el pasado o establecido
en el futuro— tomar ambas cajas es la acción correcta. Supóngase que la persona ha observado 1 000
intentos previos a su decisión, y cada persona que tomó la caja B recibió $1 millón, y aquellos que
tomaron ambas cajas encontraron vacía la caja B. Incluso, un amigo de la persona, capaz de ver el
contenido de ambas cajas antes de que la persona tome su decisión, sin importar qué hay en ellas, le
aconsejaría tomar ambas, porque ya sea que la caja B tenga o no $1 millón, la persona todavía saldría
ganando $1 000.
Isaac Asimov, en una respuesta a Gardner, escribió: “Sin duda, yo tomaría ambas cajas. Soy un
determinista, pero me queda perfectamente claro que cualquier ser humano digno de ser considerado
un ser humano (incluido con toda certeza yo mismo) preferiría el libre albedrío, si algo así existe…
Al menos así, usted habrá expresado su disposición a apostar por la no-omnisciencia [de Dios] y por
su propio libre albedrío… Sin embargo, si solo toma la segunda caja usted obtendrá su condenado
millón y no solo usted es un esclavo, pero también habrá demostrado su disposición a ser un esclavo
por ese millón, y usted no es alguien a quien yo reconozca como humano”.
Al parecer Martin Gardner disfruta más proponiendo paradojas como esta que resolviéndolas.
“Soy un indeterminista, lo que quiere decir que no soy un determinista”, asegura. “No creo que la
paradoja se haya explicado adecuadamente aún, pero no voy a perder sueño por eso”.

PROBLEMAS 9.2

En los problemas del 1 al 10 está dada la matriz de pagos de un juego. Encuentre el rendimiento es-
perado para R con el par de estrategias dadas p y q.
3  1
5 3  1  2  4  5 3  2
1. A =
( 3 6); p = (3  3)
,q=  2. A =
( 3 6); p = (1  0), q =
()  ()
1  1
2  2

1  1
4  3
1 3 –1  1  4  1  1 3 –1  1
3. A =  ;p=(  ,q=  4. A =  ; p = (0  1), q =
(2 0  4)  5)  (2 0  4)
()  ()
5  2  3
1  1
4  3

1 3 –1  2  1
5. A =
( 2 0 4); p = (3  3)
,q=  1
( 0)

2 –1 4  1
1  1  1
6. A = 5 7 3 ; p =  ,q=
(3  3)
()
( 6 2 –2)  3

2 –1 4  0
1  1  1
7. A =  5 7 3 ;p=(  ,q=
6)
( 6 2 –2)  2  3
( 1)
```

#### Página 22

```text
22  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

2 –1 4  2
1  1
8. A =  5 7 3 ; p = (0  ,q=
2)
()
( 6 2 –2)  2
–3 4 2 3  1
1  3  5
9. A = –2 6 1 5 ; p = (  0  ,q=
4)
( –4 0 6 7)  4
()

–3 4 2 3  1
1  3  1  4
20. A =  –2 6 1 5 ; p = (  ,q=
5)
( –4 0 6 7)  5  5
()

En los problemas 11 a 23 determine las estrategias óptimas y el valor de la matriz de juego dada. ¿Qué
juegos son imparciales?

2 –1  1  3  1 0
11.  12.  13.
( –1  2)  ( 2 –1)  ( –2 2)

2  – 12  0 1  1 –1
14.  15.  16.
( – 12  1)  ( –1 0)  ( –1 1)

1  3
–1 –1  2  2  3 5
17.  18.  19.
( 0 –2)  ( 12  1)  ( 2 6)

5 3 2
5 –3  7 4 2
20.  21.  22. 3 2 6
( –5 3)  ( 5 3 6)
( 4 0 1)
5  8  4
3  7  1
23.
(  4
2  )
24. Suponga que la matriz de juego en el ejemplo 5 es

10 39
A=
( 5 40)
¿Cuál es el valor mínimo de probabilidad de que tiene el paciente padece la enfermedad para
la cual se puede recomendar la operación?
25. El modelo de toma de decisiones médicas en el ejemplo 5 puede estudiarse de forma más gene-
ral. Defina la matriz de juego
a11 a12
A=
( a21 a22)
```

#### Página 23

```text
9.2 Juegos de dos personas: estrategias mixtas  23

donde a11, a12, a21, y a22 son las duraciones esperadas de vida si el paciente se opera y padece
la enfermedad, se opera y no padece la enfermedad, padecer la enfermedad y no se opera o no
padece la enfermedad y no se opera, respectivamente. Asumiendo que el paciente desea maxi-
mizar la duración esperada de vida, demuestre que la operación puede recomendarse si la
probabilidad de que el paciente padezca la enfermedad es mayor que
a22 – a12
a11 + a22 – a12 – a21
[Pista: Compare el tiempo de vida esperado del paciente si se opera con la duración esperada
de vida si no se opera.]
26. Demuestre que el juego del problema 9.1.21 no es imparcial. ¿Cuál es su valor? ¿Qué estrategia
debe adoptar R?
27. Responda a las preguntas del problema 26 para el juego del problema 9.1.22.
28. En el problema 9.1.25, ¿qué debe hacer el dueño de la estación de gasolina A si sabe que el
dueño de la estación de gasolina B lanzará una moneda para determinar si baja o sube los pre-
cios?
29. Encuentre la estrategia óptima para el granjero en el problema 9.1.30 si la probabilidad de una
helada entre el 25 de agosto y el 5 de septiembre es de 0.5.
30. Responda a la pregunta en el problema 29 si la probabilidad de una helada es de 0.2.
31. Responda a la pregunta en el problema 29 si la probabilidad de una helada es de 0.9.
32. En una cierta región agrícola, el clima promedio durante la temporada de cultivo es ya sea frío
o cálido. Van a plantarse dos cosechas en una granja de 1 500 acres. Si la temporada de cultivo
el clima es frío, las ganancias esperadas son de 20 dólares por acre para la cosecha I, y de 10
dólares por acre para la cosecha II. Si la temporada de cultivo es cálida, las ganancias esperadas
son de 10 dólares por acre para la cosecha I, y de 30 dólares por acre para la cosecha II. Des-
criba la competencia entre el granjero y el clima como un juego de matrices. Si no hay informa-
ción disponible sobre las probabilidades de un clima frío o cálido, ¿cuál es la estrategia óptima
para el granjero?
33. Suponga que el clima en el problema 32 tiene la misma probabilidad de ser frío que de ser cá-
lido. ¿Cuántos acres de cada cosecha debe plantar el granjero?
34. En un experimento, un mono debe elegir uno de tres paneles para recibir un plátano. En cada
intento del experimento, el experimentador coloca ya sea dos plátanos detrás del panel I o un
plátano detrás de los paneles II y III. (Estos son los dos “movimientos” del experimentador).
Describa este experimento como un juego de matrices de 3 × 2. ¿Cuáles son las estrategias
óptimas para el mono y para el experimentador?
35. Si todas las componentes de una matriz de juego son positivas, demuestre que el valor del juego
es positivo.
*36. Dados dos juegos de matrices A = (aij) y B = (bij) de m × n, tales que bij = aij + k para todos
los i y todas las j, demuestre que el valor del juego de B es igual al valor del juego de A más la
constante k. Demuestre que las estrategias óptimas para R y C son las mismas que para B y
para A. (Se dice que los juegos de A y B son juegos de matrices equivalentes).
37. ¿Determine las estrategias óptimas y los valores de los juegos de matrices equivalentes

3  2  5  4
A=
( 2 –3) y B = ( 4 –1)
```

#### Página 24

```text
24  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

38. Establezca las estrategias óptimas y los valores de los juegos de matrices equivalentes

1 1 1  0 0 0
A=  2 2 3  y  B=  1 1 2
( –2 4 5)  ( –3 3 4)
39. Mientras la variable t aumenta de 0 a 1, ¿cómo cambian las estrategias óptimas en los siguientes
juegos?

t 0  1 2t  t  t2
a)  b)  c)
( 0 1 – t)  ( 0 t)  ( 12  1)

40. Determine los valores de los juegos de matrices de 2 × 2 del problema 39 como funciones de t
para 0 ≤ t ≤ 1. ¿Para cuáles valores de t estos juegos son imparciales?
41. a) Demuestre que el juego de matrices de 2 × 2

t  1–t
(1 – t  t )

no está estrictamente determinado para cualquier valor de t.
b) Demuestre que el valor de este juego es una constante independiente de t. Encuentre dicha
constante.
*42. a) Suponga que cada componente de p0A es mayor que o igual a v. Demuestre que E(p0, q) =
p0Aq ≥ v. [Pista: Utilice el hecho de que las componentes de q tienen una suma de 1.]
b) Si E(p0, q) ≥ v para cada estrategia q, demuestre que cada componente de p0A es mayor que
o igual a v. [Pista: Demuestre que la k-ésima componente de p0A es igual a E(p0, q), donde q
es el vector de columna con un 1 en la k-ésima posición y un 0 en todas las demás posicio-
nes.]
*43. Siguiendo un procedimiento similar al del problema 42, demuestre que cada componente de
Aq0 es menor que o igual a v si, y solo si, E(p, q0) ≤ v para cada estrategia p.
*44. Asuma que p0, q0, y v están dados por (3), (4) y (5), respectivamente.
a) Demuestre que p0A ≥ v y Aq0 ≤ v.
b) Utilice los resultados de los problemas 42 y 43 para concluir que (3) y (4) en verdad propor-
cionan estrategias óptimas y que v, dado por (5), es el valor del juego de matrices de 2 × 2.

9.3 Cadenas de Markov
En esta sección se discutirá una técnica matemática que se usa para modelar una gran variedad de
procesos en los negocios y las ciencias sociales, biológicas y físicas. La técnica, las cadenas de Markov,
fue desarrollada en 1906 por el matemático ruso A. A. Markov (1856–1922). En un principio, las
cadenas de Markov se usaron para analizar procesos en la física y en la meteorología. Una aplicación
inicial fue para predecir patrones del clima. Aplicaciones más recientes incluyen el análisis de los
movimientos de los precios de las mercancías, el mantenimiento de maquinaria de alto desempeño,
el comportamiento de animales de laboratorio, la selección de productos por los consumidores, la
longitud de las filas en supermercados y aeropuertos, la variedad y magnitud de inventarios y la ad-
ministración de plantas.
Antes de iniciar la discusión de las cadenas de Markov es necesario abundar en la discusión de
la probabilidad de la sección 9.1.
```

#### Página 25

```text
9.3 Cadenas de Markov  25

Sea E un evento (un resultado o un experimento) con P(E)> 0. Entonces la probabilidad condi-  Probabilidad
cional de un evento A dado que E ha sucedido está denotada por P(A∣E) y está dada por  condicional

P(A ∩ E)
P(A∣E) =  (1)
P(E)

EJ EMPLO 9.3.1  Cálculo de probabilidades

Se lanzan dos dados imparciales (numerados del 1 al 6). ¿Cuál es la probabilidad de que
a) La suma sea 7?
b) La suma sea 7 dado que al menos uno de los números sea 2?

SOLUCIÓN ►
a) Hay 36 posibilidades [(1, 1), (1, 2), …, (1, 6), (2, 1), …, (2, 6), …, (6, 1), (6, 2), …, (6, 6)]. De
estas, seis suman 7: (1, 6), 6, 1), (2, 5), 5, 2), (3, 4), (4, 3). Por lo tanto
6 1
P(7) =  =
36 6
b) Se ha dicho que hay al menos un 2. Por lo tanto, los únicos resultados posibles son (2, 1), (2, 2),
(2, 3), (2, 4), (2, 5), (2, 6), (1, 2), 3, 2), (4, 2), (5, 2), y (6, 2). De estos resultados igualmente
posibles, solamente dos suman 7: (2, 5) y (5, 2). Por lo tanto
P(7∣ al menos un 2) =
Puede obtenerse esta respuesta mediante la fórmula de la probabilidad condicional.
P(7 y al menos un 2)
P(7∣ al menos un 2) =
P(al menos un 2)
36 2
=  =
11 11
Nota
Los resultados en este ejemplo pueden representarse mediante un diagrama de árbol.
Esto se muestra en la figura 9.1. De hecho, en cualquier momento que se tiene un ex-  El evento 7 y al menos un 2 sucede en
perimento de dos (o más) partes las diversas probabilidades pueden representarse  dos sentidos: (2, 5) y (5, 2), así que su
mediante un diagrama de árbol. Los diagramas de árbol se utilizan para ilustrar la  2
probabilidad es .
teoría de las cadenas de Markov.  36
De la ecuación (1) puede obtenerse otro resultado útil.

Teorema de multiplicación

P(A ∩ E) = P(A∣E)P(E)  (2)

EJ EMPLO 9.3. 2  Cálculo de probabilidad usando el teorema de multiplicación

En una cierta ciudad, 60% de los votantes registrados son demócratas mientras que 40% son republi-
canos. 80% de los demócratas y 35% de los republicanos apoyan la prohibición de armas de fuego.
¿Cuál es la probabilidad de que un votante seleccionado de forma aleatoria apoye la prohibición de
armas de fuego?
```

#### Página 26

```text
26  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Primer dado  Segundo dado  Resultado  Suma
1/6
1  (1, 1)  2
1/6
1/6
2  (1, 2)  3
3  (1, 3)  4
1  1/6
1/6
3  (1, 4)  5
1/6 5  (1, 5)  6
6  (1, 6)  7
1  (2, 1)  3
2  (2, 2)  4
1/6  3  (2, 3)  5
1/6  3  (2, 4)  6
5  (2, 5)  7
6  (2, 6)  8
1  (3, 1)  4
2  (3, 2)  5
1/6  3  (3, 3)  6
3  (3, 4)  7
5  (3, 5)  8
6  (3, 6)  9
1/6
1  (4, 1)  5
2  (4, 2)  6
3  (4, 3)  7
1/6  3  (4, 4)  8
5  (4, 5)  9
6  (4, 6)  10
1  (5, 1)  6
2  (5, 2)  7
1/6  3  (5, 3)  8
3  (5, 4)  9
5  (5, 5)  10
6  (5, 6)  11
1  (6, 1)  7
Figura 9.1  2  (6, 2)  8
Diagrama de árbol que  3  (6, 3)  9
muestra los resultados  3  (6, 4)  10
posibles cuando se lanzan  5  (6, 5)  11
dos dados.  6  (6, 6)  12

SOLUCIÓN ► Sea D el evento {demócrata}, R el evento {republicano}, y B el evento {apoya la
prohibición de armas de fuego}. Entonces la información en el problema puede anotarse como sigue:

P(D) = 0.6  P(R) = 0.4  P(B∣D) = 0.8  P(B∣R) = 0.35

Se pide encontrar P(B). Hay dos formas de obtener B (ver figura 9.2):

B = (B ∩ D) ∪ (B ∩ R)

Votantes registrados

B  B

D  R
B∩D  B∩R
Figura 9.2
Un diagrama de Venn que
muestra los conjuntos D
(demócratas), R (republica-
nos), B, B ∩ D y B ∩ D.
```

#### Página 27

```text
9.3  Cadenas de Markov  27

Entonces

de (2)
↓
P(B) = P(B ∩ D) + P(B ∩ R) = P(B∣D)P(D) + P(B∣R)P(R)
= (0.8)(0.6) + (0.35)(0.4) = 0.62

Hay otra forma de representar este resultado. La información en el problema está dada en el diagra-
ma de la figura 9.3.

0.8  B∣D

D
0.6

Figura 9.3
0.35  B∣R
Diagrama de árbol que
muestra las probabilidades en
0.4
R
el problema de la prohibición
de armas de fuego.

El evento {apoya prohibición} = B puede obtenerse ya sea a través de D o a través de R. Por lo tanto
puede multiplicarse a través del árbol para obtener

P(B) = (0.6)(0.8) + (0.4)(0.35) = 0.62

Esto puede hacerse debido al teorema de multiplicación.

Ahora se iniciará la discusión de las cadenas de Markov.
Antes de ofrecer definiciones generales, se iniciará con un ejemplo.

EJ EMPLO 9.3. 3  Una cadena de Markov procedente de los negocios

La empresa de banquetes Gourmet tiene 40% del negocio de banquetes en una cierta ciudad mediana.
Su única competencia, Delicious Foods Services (DFS) tiene el otro 60%. Para ser más competitiva,
Gourmet contrata a una agencia de publicidad para impulsar su imagen. Durante una amplia campa-
ña publicitaria se recopilaron las cifras de ventas mensuales. Se encontró que 90% de los clientes de
Gourmet regresan a Gourmet al siguiente mes, mientras que el 20% de los clientes de DFS se cam-
bian a Gourmet.
a) ¿Qué porcentaje de clientes usa cada servicio después de 1 mes?
b) ¿Qué porcentaje usa cada servicio cada 2 meses?
c) ¿Cuál es la cuota de mercado de largo plazo para cada servicio?

SOLUCIÓN ► Este problema se soluciona en varios pasos. Primero, se presenta alguna termi-
nología. En el lenguaje de las cadenas de Markov el mercado de servicio de banquetes en la ciudad
del ejemplo es un sistema en el cual hay dos estados: Gourmet y DFS. Un cliente de los banquetes
está en el estado Gourmet si usa los servicios de Gourmet. En el caso contrario, está en el estado
DFS. Las probabilidades de moverse de un estado a otro se llaman probabilidades de transición. Para
este problema, las probabilidades de transición se indican en la figura 9.4. Las cuatro probabilidades
en las ramas de la derecha del árbol son todas probabilidades condicionales. Anotando esto se tiene
```

#### Página 28

```text
28  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Después de un mes
Al inicio  Gourmet
0.9  0.4 × 0.9 = 0.36
(G1)
Gourmet
0.4  (G)
0.1  DFS1  0.4 × 0.1 = 0.04

Figura 9.4  Gourmet
0.2  0.6 × 0.2 = 0.12
Diagrama de árbol que  0.6  (G1)
muestra las probabilidades  DFS
en el problema de
banquetes.  0.8  DFS1  0.6 × 0.8 = 0.48

P(Gourmet ∣Gourmet) = 0.9
P(DFS ∣Gourmet) = 0.1
P(Gourmet ∣DFS) = 0.2
P(DFS ∣DFS) = 0.8
a) Al multiplicar a través del árbol, se obtiene (denotando una preferencia por Gourmet después de
1 mes mediante G1 y una preferencia por DFS después de 1 mes mediante DFS1)

P(G1) = P(G1∣G)P(G) + P(G1∣DFS)P(DFS)
= (0.9)(0.4) + (0.2)(0.6) = 0.36 + 0.12 = 0.48

y

P(DFS1) = P(DFS1∣G)P(G) + P(DFS1∣DFS)P(DFS)
= (0.1)(0.4) + (0.8)(0.6) = 0.04 + 0.48 = 0.52

Por lo tanto, después de 1 mes 48% de los clientes de banquetes eligen Gourmet y 52% eligen
DFS. Obsérvese que 0.48 + 0.52 = 1.
Es posible obtener esta respuesta de otra forma. Se define al vector de probabilidad inicial p0
por p0 = (0.4 0.6). Se define a la matriz de transición T por

Hacia
Desde  G DFS
G 0.9 0.1
T=
DFS ( 0.2 0.8)

La matriz de transición exhibe las probabilidades de pasar de un estado a otro durante un intento
del experimento. Por lo tanto, por ejemplo, la componente 1,2 de T es la probabilidad de pasar del
estado 1 (Gourmet) al estado 2 (DFS) en un mes.
Ahora obsérvese que

0.9 0.1
p0T = (0.4  0.6)
( 0.2 0.8) = (0.48 0.52) = p1

es el vector de probabilidad de proporciones después de 1 mes. Debe explicar por qué tomar el
producto de p0T arroja el mismo resultado que multiplicar a través del diagrama de árbol.
b) Hay dos formas de obtener p2, el vector de proporciones después de 2 meses. Primero, puede
trazarse un diagrama de árbol como en la figura 9.5. Al multiplicar a través del árbol se obtiene
```

#### Página 29

```text
9.3 Cadenas de Markov  29

Después de dos meses

Después de un mes  0.9  G2  0.4 × 0.9 × 0.9 = 0.324
G1
Al inicio 0.9  0.1  DFS2  0.4 × 0.9 × 0.1 = 0.036
G
G1  0.2  G2  0.4 × 0.1 × 0.2 = 0.008
0.4  0.1
DFS1
DFS1  0.8  DFS2 0.4 × 0.1 × 0.8 = 0.032

0.9  G2  0.6 × 0.2 × 0.9 = 0.108
G1
0.6  0.2
0.1  DFS2  0.6 × 0.2 × 0.1 = 0.012
Figura 9.5
DFS
Diagrama de árbol que
muestra las probabilidades  0.2  G2  0.6 × 0.8 × 0.2 = 0.096
en el problema de
0.8
DFS1
banquetes después de 2
meses.  0.8  DFS2 0.6 × 0.8 × 0.8 = 0.384

P(G2) = (0.4)(0.9)(0.9) + (0.4)(0.1)(0.2) + (0.6)(0.2)(0.9)
+ (0.6)(0.8)(0.2) = 0.536

y

P(DFS2) = (0.4)(0.9)(0.1) + (0.4)(0.1)(0.8) + (0.6)(0.2)(0.1)
+ (0.6)(0.8)(0.8) = 0.464

Por lo tanto, p2, el vector de proporciones después de 2 meses, está dado por

p2 = (0.536  0.464)

Obsérvese que 0.536 + 0.464 = 1. Alternativamente, por el mismo razonamiento que en la parte
a), se encuentra que

0.9 0.1
p2 = p1T = (0.48  0.52)
( 0.2 0.8) = (0.536 0.464)

c) De las partes a) y b) se concluye que

p1 = p0T
p2 = p1T = (p0T)T = p0T 2
p3 = p2T = (p0T 2)T = p0T 3
p4 = p3T = p0T 4

y así en adelante. Por ejemplo

0.9 0.1
p3 = p2T = (0.536  0.464)
( 0.2 0.8) = (0.5752 0.4248)
```

#### Página 30

```text
30  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Mediante un programa de cálculo se obtienen los resultados de la tabla 9.4. Parece que en la
medida que n (el número de meses) aumenta, las proporciones se acercan al vector de probabili-
dad fijo
2  1
t = (0.6666…  0.3333…) = (
3  3)
A este se le llama un vector fijo para la matriz de probabilidad T porque

2  1  0.9 0.1  2  1
tT = (  =(  =t
3  3 ) ( 0.2 0.8)  3  3)

Es decir, el vector t no cambia cuando se multiplica a la derecha por la matriz T. Por lo tanto, se
concluye que las proporciones de largo plazo de las cuotas son , o 67 %, del mercado para Gour-
met y , o 33 %, del mercado para DFS.

Tabla 9.4
Vector de probabilidad
Mes n  (o proporción)
después de n meses
(Inicial)  0  (0.4  0.6)

1  (0.48  0.52)

2  (0.536  0.464)

3  (0.5752  0.4248)

4  (0.60264  0.39736)

5  (0.621848  0.378152)

7  (0.64470552 0.35529448)

10  (0.6591339934  0.3408660066)

15  (0.6654006503  0.3345993497)

20  (0.6664538873  0.3335461127)

25  (0.6666309048 0.3333690952)

30  (0.6666606562  0.3333393438)

40  (0.6666664969  0.3333335031)

Antes de dar ejemplos adicionales, se discutirán algunas propiedades generales de las matrices
de probabilidad y de las cadenas de Markov.
Matriz de  La matriz P = (pij) de n × n es una matriz de probabilidad si cada uno de sus renglones es un
probabilidad  vector de probabilidad. Esto significa que todas sus componentes son positivas y la suma de las com-
ponentes en cada renglón de P es 1.

E JE M P LO 9.3.4  Cinco matrices de probabilidad

Las siguientes son matrices de probabilidad.
```

#### Página 31

```text
9.3  Cadenas de Markov  31

1  1  1
1  1  4  4  2  1 0  0
1 0  1  1 5
a)  b) 2  2  c)  0 1 0  d)
( 12 12)  ( 14  3)
4  ( 1 1 1)  ( 0 0 1)
4  3 12

3  3  3
1  1
0  2 0 2
1  1 1 5
6  3 12 12
e)  1  1 1 1

(  4
4 4 4
3 2 1
7 7 7
)
Teorema 9.3.1

Sea p un vector de probabilidad de n componentes y sean P = (pij) y Q = (qij) matrices de
probabilidad de n × n. Entonces
i) pP es un vector de probabilidad.
ii) PQ es una matriz de probabilidad.
Es decir,
El producto de un vector de probabilidad (a la izquierda) y una matriz de probabilidad (a la
derecha) es un vector de probabilidad.
El producto de dos matrices de probabilidad es una matriz de probabilidad.

Demostración

i) El vector de probabilidad dado es p = (p1, p2, …, pn) y la matriz de probabilidad dada es
P = (pij) de n × n. Defina el vectror r = pP. Entonces
p11 p12  ⋯  p1n
p21 p22  ⋯  p2n
r = pP = (p1, p2, …, pn)
⋮ ⋮  ⋮
(pn1 pn2  ⋯  pnn
)
= (p1 p11 + p2 p21 + … + pn pn1, …, p1 p1n + p2 p2n + … + pn pnn)

En otras palabras, r = pP es vector de renglón de n componentes, r = (r1, r2, …, rn), con
la i-ésima componente ri = p1 p1i + p2p2i + … + pn pni. Cada ri es positiva dado que es la
suma de números no negativos. Para demostrar que r es un vector de probabilidad, se
debe demostrar que la suma de las componentes es 1.
n  n
∑ ri = ∑ (p1 p1i + p2 p2i + … + pn pni)
i=1  i=1

n  n  n
= ∑ p1 p1i + ∑ p2 p2i + … + ∑ pn pni
i=1  i=1  i=1

n  n  n
= p1 ∑ p1i + p2 ∑ p2i + … + pn ∑ pni
i=1  i=1  i=1

= p1 + p2 + … + pn = 1
```

#### Página 32

```text
32  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

dado que ∑ni =1 pij, la suma de las componentes en el j-ésimo renglón de una matriz de
probabilidad, es 1 para j = 1, 2, …, n.
ii) Si P = (pij) y Q = (qij) son matrices de probabilidad de n × n, la matriz del producto PQ
es una matriz de probabilidad de n × n.
Defina el producto de la matriz R = PQ = (rij). Esta es una matriz de n × n cuya
ij-ésima componente es rij = ∑nk =1 pik qkj. Dado que las componentes de P y de Q son no
negativas, las componentes de R = PQ son positivas. La suma de las componentes en el
i-ésimo renglón de R es
n  n  n  n  n
∑ rij = ∑ ∑ pik qkj = ∑ ∑ pik qkj
j=1  j=1 k=1  k=1 j=1

n  n  n
= ∑ pik ∑ qkj = ∑ pik = 1
k=1  ( k=1 )  k=1

En esta demostración se ha revertido el orden de la doble suma y se han usado los hechos
de que ∑nk =1 pik = ∑nj =1 qkj = 1 dado que P y Q son matrices de probabilidad. Se ha
demostrado así que PQ es una matriz de probabilidad.

E JE M P LO 9.3.5  El producto de un vector de probabilidad y una matriz
de probabilidad es un vector de probabilidad
1  1  1
4  4  2
1  1  3
Sea p = (  yP=  0 1 0 . Verifique que pP es un vector de probabilidad.
8)
8  2
( 1 1 1)
3  3  3

SOLUCIÓN ►
1  1  1
4  4  2
1  1  3  5  21  3
pP = (  =(
8)  16 )
0 1 0
8  2
( 1 1 1)  32  32
3  3  3

5 21 3
es un vector de probabilidad dado que  +  +  = 1.
32 32 16

E JE M P LO 9.3.6  El producto de dos matrices de probabilidad es una matriz
de probabilidad
1  1  1
4  4  2  1 0  0
Sea P =  0 1 0  yQ=  1  1 5  .
( 1 1 1)  ( 0 0 1)
4  3 12

3  3  3

Verifique que PQ es una matriz de probabilidad.

SOLUCIÓN ►
1  1  1  5 1 29
4  4  2  1 0  0  16 12 48
PQ =  0 1 0  =  1  1 5  =  1 1 5

( 1 1 1) ( 0 0 1) (  )
4  3 12  4 3 12
5  1 17
3  3  3  12 9 36
```

#### Página 33

```text
9.3 Cadenas de Markov  33

5  1 29 1 1 5  5 1 17
Las componentes de PQ son todas no negativas. También,  + + = + + = + +
16 12 48 4 3 12 12 9 36
= 1. Por lo tanto, PQ es una matriz de probabilidad.

Para definir una cadena de Markov, considérese un experimento con un espacio muestral finito
S = {E1, E2, …, En}. Considérese una secuencia (o cadena) de intentos de este experimento. Se dice
que el experimento está en el estado Ei en el m-ésimo intento si Ei es el resultado del m-ésimo intento  Estado
del experimento.

D Definición 9.3.1
Cadena de Markov Una secuencia de intentos de un experimento es una cadena de Markov si
1. El resultado del m-ésimo intento solamente depende del resultado del (m – 1)-ésimo inten-
to y no del resultado de intentos anteriores, y
2. La probabilidad de pasar del estado Ei al estado Ej en dos intentos sucesivos del experimen-
to no cambia.

Por ejemplo, si la probabilidad de pasar del estado E2 a E4 en el tercer intento es 0.6, entonces la
probabilidad de pasar de E2 a E4 en el cuarto, décimo o décimo quinto intento también es 0.6.
Nótese que en el ejemplo 3 se asumió que la probabilidad de que un cliente eligiera Gourmet en
un mes particular dependía solamente de la empresa de banquetes que había elegido el mes anterior.
Si el clima de hoy depende solamente del clima de ayer, entonces los problemas de observar y
predecir el clima son un problema que involucra a las cadenas de Markov. Si la probabilidad de elegir
una marca particular de automóvil en la próxima compra depende solamente de automóvil que se
tiene actualmente, entonces el análisis de los patrones de venta es un problema que involucra a las
cadenas de Markov.
Por otro lado, si el clima de hoy está determinado por el clima de varios días pasados, entonces
ya no se tiene una cadena de Markov. Igualmente, si en la compra del próximo automóvil se toman
en consideración los últimos tres autos adquiridos, entonces el análisis del patrón de automóviles no
involucra a una cadena de Markov. Esto resulta así porque la probabilidad de elegir una marca de
automóvil en el m-ésimo intento del experimento (el m-ésimo automóvil) depende de las elecciones
para el (m – 1), (m – 2) y (m – 3) automóviles (las últimas tres elecciones).
Una cadena de Markov se caracteriza por las probabilidades de que el sistema pase de un estado
a cualquier otro estado en intentos sucesivos.
La matriz de transición de una cadena de Markov es la matriz de probabilidad T = (pij) de n × n  Matriz de
cuya ij-ésima componente pij es la probabilidad de que el sistema pase del estado Ei al estado Ej en  transición de una
intentos sucesivos del experimento.  cadena de Markov

EJ EMPLO 9.3.7  Una matriz de transición

0.9 0.1
En el ejemplo 3 la matriz de transición es T =
( 0.2 0.8).
Esto significa, por ejemplo, que la probabilidad de pasar del estado 1 (Gourmet) al estado 2 (DFS)
es 0.1.

Sea T la matriz de transición de una cadena de Markov. Dado que el producto de dos matrices
2  3  2  4 5
de probabilidad es una matriz de probabilidad, resulta que las matrices T = TT, T = T T, T , T , …
son todas matrices de probabilidad.
```

#### Página 34

```text
34  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

D Definición 9.3.2
Matriz regular y cadena de Markov regular Una matriz de probabilidad es regular si todas las
m
componentes de al menos una de sus potencias T son estrictamente positivas (mayores que
cero). Una cadena de Markov es regular si su matriz de transición es regular.

E JE M P LO 9.3.8  Determinación de si una matriz es una matriz de transición para una
cadena de Markov regular

¿Cuáles de las siguientes matrices son matrices de transición para una cadena de Markov regular?
1  1  3  1  1
1  1  1  1
0  2  2  5  5  5
a)  2  2  b)  2  2  c)  1  1  d)  1  1  1
( 13  2)  ( 0 1)  (  0)  (  )
2  2  4  2  4
3  1  1  1  1  1
2  2  4  4  2

SOLUCIÓN ►
1  1
a) T =  2  2 es regular porque todas sus componentes son positivas.
( 13  2)
1  1  1  1  1  3
b) T 2 =  2  2  2  2  =  4  4  ,
( 0 1)( 0 1) ( 0 1)
1  7  1 15
T3 =  8  8  ,  T4 =  16 16  ,
( 0 1)  ( 0 1)
m
y así en adelante. Dado que siempre hay un cero en la posición 2,1 en T , se concluye que T no
es regular.
1  1  1  1  1  1  1
0  2  2  0  2  2  2  4  4
c) T 2 =  1
0  1  1
0  1  =  1  1  1

(  0)(  0) (  )
2  2  2  2  4  2  4
1  1  1  1  1  1  1
2  2  2  2  4  4  2

entonces T es regular.
d) Las componentes son todas positivas, entonces T es regular.

¿Por qué se estudian las cadenas de Markov regulares? En el ejemplo 1 se observó que la cadena
0.9 0.1
de Markov regular (regular porque T =
( 0.2 0.8) tiene todas las componentes positivas) tenía un
2 1  n
vector de probabilidad fijo t = (  y que el vector de probabilidad pn = p0T se acercaba a t a
3 2)
medida que n se hacía más grande. Esto no es accidental.

Teorema 9.3. 2
Existencia de un vector de probabilidad fijo
Si T es una matriz de probabilidad regular, entonces existe un único vector de probabilidad t
n
tal que tT = t. Además, para cualquier vector de probabilidad p, el vector de probabilidad pT
se acerca cada vez más a t a medida que n aumenta. Al vector fijo t se le llama la distribución
estacionaria de la cadena de Markov regular cuya matriz de transición es T. Además, a medida
n
que n aumenta, cada renglón de T se acerca al vector fijo t.
```

#### Página 35

```text
9.3 Cadenas de Markov  35

Se presenta una demostración parcial del teorema 9.3.2 al final de la sección.

EJ EMPLO 9.3. 9  Encontrando vectores fijos

Encuéntrese el vector fijo para cada matriz regular.
3  1  1
1  1  5  5  5
a)  2  2  b)  1  1  1
( 13  2)
3  (
1 )
4  4  2

SOLUCIÓN ► Se busca un vector de probabilidad t tal que tT = t. Si t = (x y), se resuelve la
ecuación
1  1
(x  y)  2  2 = (x  y)
( 13  2)
o
1  1  1  2
(2x + 3y 2x + 3y) = (x y)
Igualando componentes, se obtiene
1  1
x+ y=x
2  3
1  2
x+ y=y
2  3
o
1  1
– x+ y=0
2  3
1 1
x– y=0
2 3
También, dado que t es un vector de probabilidad, deben tenerse x + y = 1. Esto conduce al sistema
1  1
– x+ y=0
2  3
1 1
x– y=0
2 3
x+ y=1
Simplificando renglones se obtiene, sucesivamente,

– 12  1
∣ 0  1 – 23 ∣ 0  R2 → R2 – 12R1  1 – 23 ∣ 0
R1 → –2R1  R3 → R3 – R1
2  – 13  ∣ 0  1
2  – 13 ∣ 0  0  0 ∣ 0
( 1  1 ∣ 1)  (1  1 ∣ 1)  (0  3
∣ 1)
1 – 23 ∣ 0  1 0 ∣  2
5  1 0 ∣  2
R3 → 35R3  R1 → R1 – 23R3  R2 ⇄ R3
0  0 ∣ 0  0 0 ∣ 0  0 1 ∣  3
.
(0  1 ∣  3
)  (0 1 ∣ )  3
( 0 0 ∣ 0)
2  3  2  3
Por lo tanto x = , y = , lo que da el vector único de probabilidad t = (  .
5  5  5  5)

La notación R2 ⇄ R3 significa intercambio entre el renglón 2 y el renglón 3.
```

#### Página 36

```text
36  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

1  1
2  3  2 = 2  3
Comprobación. tT = (  2  =t
5  5)( 1  2) (5  5)
3  3
b) Resolviendo
3  1  1
5  5  5
t = (x  y  z) = tT = (x  y  z)  1  1  1

(  )
4  2  4
1  1  1
4  4  2

o
3  1  1  1  1  1  1  1  1
(x  y z) = ( x + y + z  x+ y+ z  x+ y+ z
5  4  4  5  2  4  5  4  2)
o
3  1  1
x+ y+ z=x
5  4  4
1  1  1
x+ y+ z=y
5  2  4
1  1  1
x+ y+ z=z
5  4  2
Entonces, junto con la condición x + y + z = 1, se obtiene el sistema

x+ y+ z=1
2  1  1
– x+ y+ z=0
5  4  4
1 1  1
x– y+ z=0
5 2  4
1  1 1
x+ y– z=0
5  4 2
Ahora se simplifican renglones:
R2 → R2 + 25R1
1  1  1 ∣ 1  1  1  1 ∣  1
R3 → R3 – 15R1
– 25  1
∣ 0  R4 → R4 – 15R1  0 2013 13
∣  2
– 12  1  ∣ 0  7
0 – 10  1  ∣  – 15
(  5
– 12  ∣ 0  )  (  0 20 1
– 10  ∣  – 15  )
1  1  1 ∣  1
R2 → 20
13R2
0  1  1 ∣  8
0  7
– 10  1  ∣  – 15
(0  1
– 10  ∣  – 15)
R1 → R1 – R2
7  1 0  0 ∣  5
R3 → R3 + 10 R2
R4 → R4 – 20 R2  0 1  1 ∣  8
0 0  3  ∣  3

(0 0  4
– 34  ∣
– 13  )
```

#### Página 37

```text
9.3  Cadenas de Markov  37

1 0  0 ∣  5
R3 → 43R3  0 1  1 ∣  8
0 0  1 ∣  4

(0 0 – ∣  3
– 13  )
1 0 0 ∣  5
R2 → R2 – R3
R4 → R4 + 34R3  0 1 0 ∣  4
0 0 1 ∣  4

( 0 0 0 ∣ 0)  13

5  4  4  5  4  4
Por lo tanto x =  ,y= ,z= ,yt=(  .
13  13  13  13  13  13)

3  1  1
5  5  5
5  4  4  5  4  4
Comprobación. tT = (  1  1  1  =(
13)  13)
Observación
(  )
13  13  4  2  4  13  13
1  1  1
4  4  2  Para la matriz en la parte a) de este
ejemplo se usa una calculadora para
calcular algunas potencias de T.
1  1
T=  2  2 = 0.5  0.5
( 13  2) (0.3333…  0.6666… )
7 7
T =  12 12 = 0.4166…  0.5833…
11 11 ) (0.3888…
( 18  0.6111… )

4  2  2  0.400462963 0.599537037
T =T T ≈
(0.399691358 0.600308642 )

8  4  4  0.4000003572  0.5999996428
T =T T ≈
(0.3999997618  0.6000002382 )

2  3
16  8  8  0.4 0.6
T =T T ≈  = 5  5
( 0.4 0.6) ( 2  3)
5  5

m  0.4 0.6
T =  para m > 16  ¡Revise!
( 0.4 0.6)

Las últimas dos matrices son correctas hasta diez decimales.
Ahora, sea p = (a b) cualquier vector de probabilidad. Entonces para m > 16

m  0.4 0.6
pT = (a  b)
( 0.4 0.6) = (0.4a + 0.4b 0.6a + 0.6b)
= (0.4(a + b)  0.6(a + b))

m  2  3
Dado que a + b = 1, se observa que, hasta diez decimales, pT = (0.4  0.6) = (  para cual-
5  5)
quier vector de probabilidad p inicial.
```

#### Página 38

```text
38  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

E JE M P LO 9.3.10  Un experimento de laboratorio

Se coloca a un ratón dentro de una caja dividida en tres compartimentos, como se muestra en la figu-
ra 9.6. Ante la ausencia de más información, es razonable suponer que el ratón elegirá una puerta
aleatoriamente para pasar de un compartimento a otro. Si este supuesto es válido, puede esperarse
que a la larga el ratón esté en cada uno de los tres compartimentos con la misma frecuencia. Wecker
describió una serie de experimentos con ratones ciervos que puede analizarse en estos términos.10 Al
permitir que el ratón se mueva entre los compartimentos, la mitad en campo abierto y la mitad en un
área boscosa, Wecker pudo estudiar la fuerza de la preferencia del ratón ciervo por el habitat del
campo por sobre el habitat boscoso.

II

I

Figura 9.6  III
Una caja con tres
compartimentos.

Puede analizarse la situación del ratón en términos de una cadena de Markov y demostrar que,
a la larga, es válida la intuición de que el ratón pasará cantidades de tiempo iguales en cada uno de
los compartimentos. Los tres estados obvios en este ejemplo son los compartimentos I, II, y III. Dado
que es igualmente posible que se elijan todas las puertas, la probabilidad es a que el ratón se move-
rá a uno o los dos compartimentos en los que no está. Esto arroja una matriz de transición

1  1
0  2  2
T=  1
0  1

(  0)
2  2
1  1
2  2

Dado que

1  1  1
2  4  4
T =  1  1  1

(  )
4  2  4
1  1  1
4  4  2

T es regular y tiene un único vector de probabilidad fijo t = (x  y  z); entonces x + y + z = 1 y

1  1
0  2  2
(x  y  z)  1
0  1  = (x  y  z)
(  0)
2  2
1  1
2  2

Wecker, Stanley C. "HABITAT SELECTION." Scientific American 211, no. 4 (Oct 1964): 109-17.
```

#### Página 39

```text
9.3 Cadenas de Markov  39

o
1  1
y+ z=x
2  2
1  1
x  + z=y
2  2
1  1
x+ y  =z
2  2
o
x+ y+ z=1
1  1
–x + y + z = 0
2  2
1  1
x– y+ z=0
2  2
1  1
x+ y– z=0
2  2
Simplificando renglones se obtiene
R2 → R2 + R1
1  1  1 ∣ 1  1  1  1 ∣  1
R3 → R3 – 12R1
–1  1
∣ 0  R4 → R4 – 12R1  0  3
∣  1
–1  1  ∣ 0  0  – 32  0 ∣ – 12
(  2
–1 ∣ 0  )  (0 0 – ∣ – )  3

1  1  1 ∣  1
R2 → 32R2  0  1  1 ∣  2
0 – 32  0 ∣  – 12
(0 0 – ∣ )  3
2  – 12

1 0  0 ∣  1
R1 → R1 – R2
R3 → R3 + 32R2  0 1  1 ∣  2
0 0  3  ∣  1

(0 0  2
– 32  ∣
– 12)
1 0  0 ∣  1
R3 → 23R3  0 1  1 ∣  2
0 0  1 ∣  1

(0 0 – ∣ )  3
– 12

1 0 0 ∣  1
R2 → R2 – R3
R4 → R4 + 32R3  0 1 0 ∣  1
0 0 1 ∣  1

( 0 0 0 ∣ 0)  3
```

#### Página 40

```text
40  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

1 1 1
Por lo tanto, t = (  , que significa que, como se esperaba, el ratón pasará cantidades iguales
3 3 3)
de tiempo en cada uno de los tres compartimentos.

E JE M P LO 9.3.11  Predicción del clima

El clima en Montreal es bueno, neutro o malo en un día cualquiera. Si el clima es bueno hoy, será
bueno mañana con una probabilidad de 0.6, neutro con una probabilidad de 0.20, y malo con una
probabilidad de 0.20. Si el clima es neutro hoy, mañana será bueno, neutro o malo con probabilidades
de 0.25, 0.50, y 0.25, respectivamente. Finalmente, si el clima es malo hoy, las probabilidades son de
0.25, 0.25 y 0.50 para un clima bueno, neutro o malo mañana. Esto puede describirse como una ca-
dena de Markov de intentos de un experimento con tres resultados E1, E2, y E3, correspondientes
al clima bueno, neutro y malo en un día cualquiera. La matriz de transición para esta cadena de
Markov es

Hacia
Desde  B  N  M
3  1  1
B  0.60 0.20 0.20  5  5  5
N  0.25 0.50 0.25 = 14  1  1
( 0.25 0.25 0.50) ( 1  )
2  4
M  1  1
4  4  2

54  5
Nota  Esta es regular. En el ejemplo 9 se calculó el vector fijo (
13)
. Esto significa
5  4
que, a la larga, el clima en Montreal será bueno ≈ 38% del tiempo, neutro  ≈ 31%
Este problema pudo resolverse solo al  3  13
suponer que el clima de hoy es  del tiempo, y malo 31% del tiempo.
afectado solamente por el clima de
ayer, no por lo que sucedió en días
previos.

Demostración parcial del Teorema 9.3.2 (opcional)
Teorema 9.3.3

Si P = (pij) es una matriz de probabilidad de n × n, entonces existe un vector renglón t de
n componentes (diferente de cero) tal que tP = t. Es decir, cada matriz de probabilidad tiene
un vector fijo.

Demostración

La ecuación tP = t es equivalente a t(P – I) = 0 o, transponiendo, (P – I)ttt = 0t. Este sistema
homogéneo tiene una solución t diferente de cero si, y solo si,

det(P – I)t = det(P – I) = 0

Esto se deduce de la teoría de los determinantes. Pero det(P – I) = 0 si, y solo si, las columnas
de la matriz P – I son linealmente dependientes. Dado que P es una matriz de probabilidad,
se sabe que

p11 + p12 + … + p1n = p21 + p22 + … + p2n = …
= pn1 + pn2 + … + pnn = 1
```

#### Página 41

```text
9.3 Cadenas de Markov  41

Estas ecuaciones pueden anotarse en la siguiente forma de vector equivalente:

p11 – 1  p12  p1n  0
p21  p22 – 1  p2n  0
+  +…+  =
⋮  ⋮  ⋮  ⋮
(  pn1  ) (  pn2  )  (  pnn – 1  ) () 0

Los vectores a la izquierda de esta ecuación son exactamente las columnas de P – I. Por lo
tanto las columnas de P – I son linealmente dependientes, y se prueba el resultado.

Una vez que se sabe que T tiene un vector fijo, puede demostrarse mediante una simplificación
de renglones que tiene un vector de probabilidad fijo, es decir, un vector fijo con componentes no
negativos que suman 1. Debido a que los cálculos pueden resultar tediosos, se observará qué sucede
en el caso de 2 × 2. Sea

a b
A=
( c d)
donde a, b, c, d ≥ 0, a + b = 1, y c + d = 1. Sea t = (x, y) un vector fijo.
Entonces

a b
(x, y)
( c d) = (x, y)
ax + cy = x  (a – 1)x + cy = 0
o
bx – dy = y  bx + (d – 1)y = 0
Pero d – 1 = –c y a – 1 = –b, entonces el sistema es

–bx + cy = 0
bx – cy = 0

que significa que bx = cy.
Ahora, no es posible que b = c = 0 porque si ese fuera el caso, se tendría

1 0  1 0
T=
( 0 1) y T = ( 0 1)
n

c
lo que contradice el hecho de que T es regular. Supóngase que b ≠ 0; entonces x = y y se establece
b
c  c+b
1=x+y= y+y=  y
b  b
b  c  b  c
yy=  , así que x = ·  =  .
c+b  b c+b c+b
b  c
Por lo tanto, el vector (  es un vector de probabilidad fijo para T. Esta es la parte
c + b c + b)
fácil de comprobar. Aún debe probarse que pTk → t cuando k → ∞ para un vector de probabilidad p.
El esbozo restante se basa en la teoría de valores propios y vectores propios del capítulo 8. Si tT = t,
entonces (tT)t = tt o Tttt = tt. Es decir, tt es un vector propio de Tt correspondiente al valor propio 1.
Dado que T y Tt tiene los mismos valores propios, 1 es un valor propio de T.
Ahora se usa el teorema del círculo de Gershgorin. Si λ es cualquier valor propio de T, entonces

|λ – aii| ≤ ri
```

#### Página 42

```text
42  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

donde ri = |ai1| + |ai2| + … + |ai,i–1| + |ai,i+1| + … + |ain|
En realidad, aquí no se necesitan las barras de valor absoluto porque aij ≥ 0. (T es una matriz de
probabilidad.) Por una versión de la desigualdad del triángulo,

||λ| + |ai1|| ≤ |λ – aii| ≤ ri

así que

–ri ≤ |λ| – aii ≤ ri

o

–ri + aii ≤ |λ| ≤ ri + aii

Pero ri + aii es la suma de las componentes en el i-ésimo renglón de T que es igual a 1. Por lo tanto,

∣λ∣ ≤ 1

Se ha demostrado que cada valor propio de una matriz de probabilidad tiene un valor absoluto menor
que o igual a 1. También es posible demostrar que si Tt es la transposición de una matriz de probabi-
lidad regular, entonces todos los valores propios excepto el valor propio 1 tienen un valor absoluto
menor que 1 y existen n vectores propios lineales independientes para T t.
Supóngase que 1, λ2, λ3, …, λn, son los valores propios de Tt con los correspondientes vectores
n
propios tt, v2, v3, …, vn. Sea pt una columna de vector de probabilidad en ℝ . Entonces, debido a que
n
n vectores lineales independientes forman una base en ℝ , existen escalares c1, c2, … cn tales que

pt = c1tt + c2v2 + c3v3 + … + cnvn

Entonces

T tpt = c1tt + c2Tv2 + c3Tv3 + … + cnTvn
= c1tt + c2λ2v2 + c3λ3v3 + … + cnλnvn

y

(T t)kpt = c1tt + c2λk2v2 + c3λk3v3 + … + cnλknvn

Dado que ∣λi∣ < 1, λki → 0 conforme k → ∞ para i = 2, 3, …, n. Por lo tanto

(T t)kpt → c1tt  cuando k → ∞
Observación
Una demostración completa de este  Pero (Tt)kpt tiene componentes que deben sumar 1 (explique por qué) de modo que
teorema, así como demostraciones de  c1 = 1, y se tiene
los resultados citados en la sección
9.4, pueden encontrarse en el  (T t)kpt → tt  cuando k ⟶ ∞
interesante ensayo “On Markov
Processes in Elementary Mathematics
Courses” de John T. Baldwin en The  Finalmente, transponiendo, se obtiene
American Mathematical Monthly, vol.
96, no. 2, febrero 1989, 147-153.
pT k → t  cuando k → ∞
```

#### Página 43

```text
9.3 Cadenas de Markov  43

El resto de la demostración es sencillo. Si p = (1, 0 …, 0) entonces pT k es el primer renglón de Tk, de
modo que el primer renglón de T k → t cuando k → ∞. Una demostración similar funciona para los
otros renglones.

PROBLEMAS 9.3

En los problemas del 1 al 10 determine si la matriz dada es una matriz de probabilidad.

1  1  1  1  1
2  2  0  2  2  2
1.  1  1  2.  1  1  1
(  0)  (  )
2  2  2  2  2
1  1  1  1  1
2  2  2  2  2

1 0 0  2  1 – 12
2  2
3. 0 1 0  4.  – 13
( 0 0 1)  (  )
3  3
3  3
– 15  5  5

1  1  1  1
0.99 0.22 –0.01  2  4  8  8
5. 0  6.  1  1
1  0  0  0
(1  )
2  2
(0.98 0.1 0.1 )  1  1  1
2  4  8  8

1  1  1
3  3  3  1 0 0
7.  1  1  8.  1 0 0
( 1 0 0)  ( 0 0 0)
2  2

3 1 1
1  1  5 5 5 0
2  2  0  1 1 1 1
1  1  1  6 3 4 4
9.  20.  1 2 3 1
(  )  (  )
4  4  2
1  1  3  7 7 7 7
8  8  4  2 5 1 3
11 11 11 11

En los problemas 11 al 20 están dados una matriz T y un vector inicial de probabilidad p0. Calcule p1,
p2, y p3.
1  1  1  1
11. T =  2  2 ;p = 1  1
12. T =  2  2 ; p = (1  0)
( 34  1) 0 (2  2)  ( 34  1) 0
4  4
1  7  1  7
13. T =  8  8 ; p = (0  1)  14. T =  8  8 ;p = 2  3
( 23  1) 0  ( 23  1) 0 (5  5)
3  3
1  1  1
0 1 0  3  2  6
1  3  1  1  2  2
15. T =  1  1  ; p0 = (  16. T =  1 0 0 ; p0 = (
8)  5)
(  )  ( 1 1 1)
2  2  2  8  5  5
1  1 1
3  3 3  4  4  2

1  3  1
8  4  8  0 0 1
2  1  4
17. T =  1  1
0 ; p0 = (  18. T =  0 1 0 ; p0 = (1  0  0)
7)
(  )  ( 1 0 0)
2  2  7  7
1  1  3
5  5  5
```

#### Página 44

```text
44  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

0 0 1
1  1  1
19. T =  0 1 0 ; p0 = (
( 1 0 0)  3  3  3)

0.16 0.49 0.35
20. T =  0.23 0.58 0.19 ; p0 = (0.31 0.44 0.25)
( 0.37 0.21 0.42)
En los problemas 21 al 30 determine si la matriz de probabilidad dada es regular. Si es regular, en-
cuentre su vector de probabilidad fijo único.
1  3  3  2
21.  4  4  22.  5  5
( 12  1)
( 25  3)
1  4
1 0  5  5
23.  24.
( 34 14)  ( 23  1)

a 1–a
25.
( b 1 – b ), donde 0 < a < 1 y 0 < b < 1
1  1
2  0  2  1 0 0
26.  1  1  1  27.  1  1
(  )  (3  )
3  3  3  2  2
1  1  1  1  1
4  2  4  5  5  5

0.2 0.3 0.5  0.12 0.37 0.51
28.  0.4 0.4 0.2  29.  0.43 0.19 0.38
( 0.3 0.6 0.1)  ( 0.26 0.59 0.15)

0.285  0  0.162  0.555
0  0.217  0.498  0.285
30.
(  0.361
0.085
0.203
0.416
0.092
0.122
0.344
0.377 )
31. a) Calcule el vector de probabilidad fijo para la matriz
2  1  1
3  6  6
T=  1  1  1

( 0 0 1)
4  2  4

b) ¿Este vector es único?
32. a) Calcule el vector de probabilidad fijo para la matriz
1  1  1
2  4  4
T=  0 1 0
( 0 0 1)
b) ¿Este vector es único?
33. En un día cualquiera, una persona está sana o enferma. Si la persona está sana hoy, la probabi-
lidad de que esté sana mañana está estimada en 98%. Si la persona está enferma hoy, la proba-
```

#### Página 45

```text
9.3 Cadenas de Markov  45

bilidad de que esté sana mañana es de 30%. Describa la secuencia de estados de salud como
una cadena de Markov. ¿Cuál es la matriz de transición?
34. Si la persona del problema 33 está enferma hoy, ¿cuáles son las probabilidades de que se recu-
pere mañana, a 2 días de ahora, y a 3 días de ahora?
35. ¿En qué porcentaje de días estará sana la persona del problema 33?
36. Considere el experimento de colocar a un ratón en la caja ilustrada en la figura 9.7.
a) Suponiendo que es igualmente posible que el ratón elija cualquier puerta para salir de un
compartimento, describa este experimento como una cadena de Markov y determine la
matriz de transición.
b) Encuentre el porcentaje de tiempo que, a la larga, pasará el ratón en cada compartimento.

I  IV

II  III

Figura 9.7

37. Un examen consiste en 100 preguntas de tipo verdadero o falso. Para un estudiante promedio
el examen es tal que si contesta correctamente una pregunta la probabilidad de que la siguiente
pregunta se conteste correctamente es . Igualmente, si contesta incorrectamente una pregun-
4  1
ta, la probabilidad de que la próxima pregunta se conteste correctamente es . Estime la califi-
cación promedio de este examen, suponiendo que la primera pregunta se contesta correcta-
mente.
38. Un animal de laboratorio tiene la elección de tres alimentos disponibles en unidades estándar.
Después de una larga observación, se descubre que si el animal elige un alimento en un intento,
elegirá el mismo alimento en el siguiente intento con probabilidad del 50% y elegirá los otros
alimentos en el siguiente intento con probabilidades iguales del 25%.
a) Describa este proceso como una cadena de Markov y determine la matriz de transición.
b) Demuestre que, a la larga, se consumen cantidades iguales de alimento.
39. Hay cinco exámenes en un cierto curso. Las calificaciones posibles para cada examen son A, B,
C, D, y E. Se estima que la probabilidad de que un estudiante obtenga la misma calificación que
en el examen anterior es de 60% y de 10% para cada una de las otras posibilidades. Describa
este proceso como una cadena de Markov. ¿Cuál es la matriz de transición?
40. a) Si un estudiante recibe una A en el primer examen del problema 39, ¿cuál es la probabilidad
de que reciba una calificación de C en el tercer examen?
b) Si un estudiante recibe una B en el segundo examen, ¿cuál es la probabilidad de que todas
sus calificaciones en las tres pruebas restantes sean de B?
```

#### Página 46

```text
46  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

41. La empresa de renta de automóviles UDrive opera en California y carga una sobretasa para los
autos que se rentan en una ubicación y se dejan en otra. Para determinar el cargo adecuado, se
dividió al estado en tres áreas: norte, centro y sur. Se determinaron las siguientes probabilida-
des de que un auto se recoja en un área y se deje en la misma o en un área diferente:

Hacia
Norte  Centro  Sur
Desde
Norte  0.6  0.3  0.1

Centro  0.2  0.5  0.3

Sur  0.1  0.2  0.7

Describa este proceso como una cadena de Markov y determine la matriz de transición.
42. En el problema 41 determine el porcentaje de autos que, a la larga, estarán en cada una de las
tres áreas.
43. Jeffrey Newman es un representante de ventas de una empresa grande de libros de texto. El
señor Newman vende libros de texto en un área que está subdividida en cuatro regiones. Visita
campus universitarios en una región cada semana y nunca visita la misma región en dos sema-
nas consecutivas. Si vende en la región I esta semana, tiene una posibilidad del 70% de ir a la
región II y una posibilidad del 30% de ir a la región IV la siguiente semana. Si vende en la región
III esta semana, venderá en la región II la siguiente semana. Si vende en la región II o IV esta
semana, venderá en una de las otras regiones con igual probabilidad en la siguiente semana.
Describa el calendario de viajes del señor Newman como una cadena de Markov y encuentre
la matriz de transición.
44. En el problema 43, ¿qué porcentaje de tiempo pasará a la larga el señor Newman en cada región?
45. En el problema 44, la empresa del señor Newman gasta $700, $650, $580 y $820, respectiva-
mente, para cubrir los gastos semanales en las cuatro regiones. ¿Cuál será a la larga el gasto
promedio semanal de la empresa?
46. Una empresa debe elegir entre dos fotocopiadoras para rentar. Las copiadoras son indistingui-
bles. Cada máquina está ya sea funcionando o no. De acuerdo con los registros de servicio
anteriores, se ha determinado que si la copiadora I está funcionando un día, la probabilidad de
que esté funcionando al día siguiente es de 0.95. Si no está funcionando, la probabilidad de que
esté funcionando al día siguiente es de 0.75. Si la máquina II está funcionando hoy, la probabi-
lidad de que esté funcionando mañana es de 0.9. Si no está funcionando hoy, la probabilidad
de que esté funcionando mañana es de 0.8. ¿Qué copiadora debe rentar la empresa?
47. En las elecciones para el senado de un cierto estado se ha determinado que una persona cam-
biará sus votos de acuerdo con las siguientes probabilidades:

Hacia
Demócrata  Republicano  Independiente
Desde
Demócrata  0.7  0.2  0.1

Republicano  0.35  0.6  0.05

Independiente  0.4  0.3  0.3

A la larga, ¿qué porcentaje de votantes votará por un demócrata, un republicano o un indepen-
diente?
```

#### Página 47

```text
9.4 Cadenas de Markov absorbentes  47

9.4 Cadenas de Markov absorbentes
En el experimento del ratón del ejemplo 9.3.10 (ver figura 9.6) se introduce la modificación de que
el ratón se saca de la caja cuando llega al compartimento III. Este nuevo procedimiento experimental
puede describirse como una cadena de Markov si se acuerda expresar que el sistema permanece en el
tercer estado en todos los intentos después de que llega al tercer estado. Los estados con esta propie-
dad son muy comunes en las aplicaciones de las cadenas de Markov.
Un estado Ei de una cadena de Markov es absorbente si, una vez que el sistema alcanza el esta-  Estado absorbente
do Ei en algún intento, el sistema permanece en el estado Ei en todos los intentos fu-  Cadena de Markov
turos.  absorbente
Una cadena de Markov es absorbente si tiene uno o más estados absorbentes y si  Nota
es posible alcanzar un estado absorbente desde cada estado no absorbente.
Si el estado Ei es absorbente, la probabilidad de transición de Ei a Ei es 1. En  Puede que sea necesario pasar por
otras palabras, el estado Ei es absorbente si, y solo si, pii = 1. El número de estados  varios estados no absorbentes antes
absorbentes en una cadena de Markov absorbente es igual al número de unos en la  de alcanzar un estado absorbente.
diagonal de su matriz de transición. Los estados no absorbentes de una cadena de
Markov absorbente se llaman estados transitorios. La probabilidad de que el sistema  Estados
esté en un estado transitorio disminuye en la medida en la que aumenta el número de  transitorios
intentos.

EJ EMPLO 9.4 .1  El estado absorbente de un experimento de laboratorio

Si el ratón (ejemplo 9.3.10) permanece en el tercer compartimento una vez que llega ahí, la matriz de
transición es
1  1
0  2  2
T=  1
0  1

( 0 0 1)
2  2

Aquí E1 y E2 son estados transitorios y E3 es un estado absorbente. Se nota que es posible alcanzar
E3 ya sea desde E1 o E2, y por lo tanto, la cadena de Markov es absorbente.

EJ EMPLO 9.4 .2  Una cadena de Markov con un estado absorbente

La matriz
1  1
2  0  2
T=  0 1 0
( 1 1 1)
3  3  3

es la matriz de transición de una cadena de Markov absorbente con tres estados. El segundo estado
es absorbente. Puede alcanzarse desde E3 en un intento y desde E1 después de dos intentos (primero
1  1
va desde E1 a E3 con probabilidad y entonces desde E3 a E2 con probabilidad ).
2  3
EJ EMPLO 9.4 .3  Un juego de canicas

Considérese un juego con dos jugadores en el que cada uno inicia con dos canicas (bolitas, bochas).
En cada jugada, el primer jugador tiene la probabilidad p de ganar una canica y la probabilidad q =
1 – p de perder una canica. El juego termina cuando algún jugador pierde todas sus canicas. Describa
el juego como una cadena de Markov.
```

#### Página 48

```text
48  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

SOLUCIÓN ► Este juego tiene cinco estados, E0, E1, E2, E3, y E4, correspondientes al primer
jugador que tiene 0, 1, 2, 3, o 4 canicas. Los estados E0 y E4 son absorbentes, y los estados E1, E2 y E3
son no absorbentes o transitorios. La matriz de transición es

p00 p01 p02 p03 p04  1  0  0  0  0
p10 p11 p12 p13 p14  q  0  p  0  0
T=  p20 p21 p22 p23 p24  =  0  q  0  p  0

(  p30 p31 p32 p33 p34
p40 p41 p42 p43 p44
) (  0
q
p
)
El sistema inicia en el estado E2; es decir, la distribución inicial de probabilidad es p0 = (0 0 1
0 0). En juegos subsecuentes las distribuciones sucesivas de probabilidad son p1 = p0T =
( 0 q 0 p 0), p2 = (q2 0 2pq 0 p2), p3 = (q2 2pq2 0 2p2q p2), p4 = (q2 + 2pq3
0 4p2q2 0 p2 + 2p3q), … Después de muchos intentos la probabilidad de que el sistema esté en
uno de los estados transitorios se vuelve muy pequeña. Esto significa que después de un gran número
de jugadas es casi una certeza que uno de los jugadores ha perdido todas sus canicas. Por ejemplo, si
2  1
p = , entonces q = y
3  3
1 2  2 1 3  2 2 1 2  2 2  2 3 1
p4 = ( ) + 2( )( )  0  4( ) ( )  0  (3) + 2(3) (3)
3  3 3  3 3
13  16  52
=(  0  0
81  81  81 )

Estas son las probabilidades de estar en un estado transitorio después de 4 jugadas.

El resultado del último ejemplo sugiere que cuando se trata de una cadena de Markov absorbente, el
sistema eventualmente estará en un estado absorbente. Este hecho no se demostrará aquí, pero se
utilizará en el recordatorio de la sección. Por supuesto, surgen dos preguntas:

1. ¿Qué tanto, en promedio, estará el sistema en algún estado transitorio antes de pasar a un estado
absorbente?
2. Si existe más de un estado absorbente, ¿cuáles son las probabilidades en el largo plazo de termi-
nar en un estado absorbente?

Existe una técnica para responder a estas preguntas. La demostración de que esta técnica funciona es
difícil y no se discutirá aquí. En su lugar, se ilustrará la técnica en una matriz específica y después se
utilizará la técnica en otros ejemplos.
Considérese la matriz
1  1  1  1
2  8  8  4
0 1 0 0
T=  1  1  3  1

( 0 0 0 1)
3  6  8  8

Esta es la matriz de transición de una cadena de Markov absorbente con estados absorbentes 2 y 4.

Paso 1. Desde la matriz de transición T, elimine los renglones correspondientes a los estados absor-
bentes; llame a la nueva matriz T′:
1  1  1  1
T′ =  2  8  8  4
( 13  1
1)
```

#### Página 49

```text
9.4 Cadenas de Markov absorbentes  49

Paso 2. Divida la matriz T′ en estados absorbentes y no absorbentes. Llame a la matriz correspon-
diente a los estados absorbentes S y la correspondiente a los estados no absorbentes R.
En este ejemplo, la segunda y cuarta columnas de T′ representan los estados absorbentes:

Estados absorbentes
Estados no absorbentes

1  1  1  1
2  8  8  4
( 13  1
1)

Por lo tanto
1  1  1  1
S=  8  4  y  R=  2  8
( 16  2)
( 13  3)

Paso 3. Calcule la matriz Q = (I – R)–1. Aquí  Nota
1  1  1 1
I–R=
1 0
– 2  8 =  2 –8
( 0 1) ( 1  3) ( 1 5)
–3 8
Se llama Q a la matriz fundamental
para la cadena de Markov absorbente.
3  8
Ahora pueden contestarse las
y  preguntas.
5  1  30 6
48 8
Q = (I – R)–1 =  8 = 13 13
13( 1  1) ( 16 24)
3  2  13 13

Paso 4. La componente qij de Q se interpreta como sigue: si se inicia un estado transitorio i, qij es el
número esperado de veces que se estará en un estado transitorio j antes de alcanzar algún estado ab-
sorbente. En el ejemplo, el número q21 = significa que si se inicia en el segundo estado transitorio
(que es el estado 3 en el problema), entonces se debe regresar al estado transitorio 1 un promedio de
16  16
≈ 1.23 veces antes de pasar a un estado absorbente (estado 2 o estado 4). También, dado que
13  13
24 40
+ = ≈ 3.08, se debe estar en algún estado transitorio un promedio de 3.08 veces si se inicia en
13 13
el estado transitorio 2.

Paso 5. Calcule la matriz de probabilidad A = QS. Aquí
1  1
1 30 6
A = QS =  8  4
13( 16 24)( 1  1)
6  8
13 33  18 33
1 4  0.3654  0.6346
=  4  =  52 52 ≈
13( 6  7)  ( 136 137 ) ( 0.4615  0.5385)

Obsérvese que A es una matriz de probabilidad.
Para interpretar las componentes en A, se añaden etiquetas:

Estado Estado
absorbente 1 absorbente 2
Estado transitorio 1 0.3654 0.6346
Estado transitorio 2 ( 0.4615 0.5385)
```

#### Página 50

```text
50  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Esto significa que si se inicia en el estado transitorio 1 se terminará en el estado absorbente 1 para
0.3654 = 36.54% del tiempo y en el estado absorbente 2 para 0.6346 = 63.46% del tiempo. Se da una
interpretación similar en el segundo renglón de A.
Ahora se aplica la técnica a una situación práctica.

E JE M P LO 9.4 .4  Predicción de tasas de graduación

Centerville Vo-Tech es una escuela estatal, con cursos de 2 años, especializada en entrenamiento vo-
cacional. Cada 2 años, la Junta Estatal de Regidores presenta un presupuesto para Centerville a la
legislatura estatal. El presupuesto está basado tanto en el número de estudiantes que asisten como el
número de quienes se espera se gradúen. Para calcular estos números se agrupa a los estudiantes en
cuatro categorías: primer año, segundo año, graduado y desertor. La última categoría incluye a aque-
llos que se transfirieron a otra escuela.
Después de recopilar datos a lo largo de varios años, la escuela puede predecir la proporción de
estudiantes que se moverán de una categoría a otra en cualquier año. Estos datos están dados en la
tabla 9.5. Si hay 2 000 estudiantes de primer año y 1 500 de segundo año en Centerville este año,
¿cuántos de estos estudiantes se graduarán eventualmente?

Tabla 9.5
Hacia  Primer  Segundo
Graduado  Desertor
Desde  año  año
Primer año  0.15  0.65  0  0.2

Segundo año  0  0.1  0.75  0.15

Graduado  0  0  1  0

Desertor  0  0  0  1

SOLUCIÓN ► Este proceso puede describirse como una cadena de Markov absorbente con
cuatro estados, dos de los cuales (graduado y desertor) son absorbentes. La matriz de transición para
esta cadena de Markov es

Hacia
Desde  1o.  2o.  G  D
1o.  0.15 0.65  0  0.2
2o.  0  0.1  0.75  0.15
T=
G
D
(  0
1  )

0.15 0.65 0  0.2
Paso 1  T′ =
(0  0.1 0.75 0.15 )

0.15 0.65  0  0.2
Paso 2  R=  ,  S=
(0  0.1 )  ( 0.75 0.15 )

1 0  0.15 0.65  0.85 –0.65
I–R=
Paso 3
( 0 1) – ( 0  0.1  ) =
( 0  0.9 )
```

#### Página 51

```text
9.4 Cadenas de Markov absorbentes  51

y
1.17647 0.84967
Q = (I – R)–1 =
(0  1.11111 )

Paso 4 Los números en Q significan que el estudiante promedio, ahora en su primero o segundo
año, pasará aproximadamente 1.18 años en el primer año y 0.85 años en el segundo año antes de al-
canzar un estado absorbente (graduación o deserción). El estudiante promedio de segundo año pasa-
rá 1.11 años en su segundo año antes de graduarse o desertar.

1.17647 0.84967  0  0.2
Paso 5  A = QS ≈
(0  1.11111 )( 0.75 0.15 )

0.6373 0.3627
≈
( 0.8333 0.1667)

Esto significa que 63.7% de los estudiantes de primer año se graduarán (dentro del estado absorben-
te 1) y 36.3% desertarán, mientras que 83.3% y 16.7% de los estudiantes de segundo año se graduarán
y desertarán, respectivamente. Ahora, contestamos las preguntas:  Nota
De los 2 000 estudiantes de primer año,
En el paso 5 se calculó el número de
2 000 × 0.6373 = 1 275 se graduarán  quienes que se graduarán eventual-
mente, mientras que en el paso 4 se
De los 1 500 estudiantes de segundo año,  determinó qué tan realmente largo
“eventualmente” significa para cada
1 500 × 0.8333 = 1 250 se graduarán  estudiante.

E J EMPLO 9. 4 .5  Análisis adicional del experimento de laboratorio

En el ejemplo 9.4.1, E1 y E2 son estados transitorios, mientras que E3 es absorbente. Por lo tanto,
1  1
0  2  2
dado que T =  1
0  1  , se tiene:
( 0 0 1)
2  2

1  1  1  1
0  0
T′ =  2  2 ,  R=  2  y  S=  2
( 12 0  1)
( 12 0)  ( 12)
Dado que solo hay un estado absorbente, es evidente que dicho estado debe alcanzarse desde todos
los estados no absorbentes, así A debe ser la matriz
( 1). Este hecho puede usarse para verificar los
cálculos. Ahora,

4  2
1 – 12
I–R=  y  Q = (I – R)–1 =  3  3
(– 12 1)  ( 23  4)

El significado de q12 = , por ejemplo, es que si el sistema inicia en el estado E1, el número esperado
3  2  4 2
de veces en que el sistema estará en el estado E2 es . Igualmente, q11 + q12 = + = 2. En otras
3  3 3
palabras, si el ratón está en el compartimento I en el primer movimiento, el número esperado de
```

#### Página 52

```text
52  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

movimientos (incluyendo al primer movimiento) antes de alcanzar el compartimento III es 2. Final-
mente,
4  2  1
A = QS =  3  3  2 = 1
( 23  4)( 1) ( 1)
3  2

como ese esperaba.

E JE M P LO 9.4 .6  Análisis adicional del juego de canicas

En el ejemplo 9.4.3 la matriz de transición para el juego es

1  0  0  0 0
q  0  p  0 0
T=  0  q  0  p 0

(  0
q
0 p
0 1
)
De modo que

q 0 p 0 0
T′ =  0 q 0 p 0
( 0 0 q 0 p)
Dado que el primero y el quinto estado son absorbentes, se tiene

0 p 0  q 0
R=  q 0 p  y  S=  0 0
( 0 q 0)  ( 0 p)
Para simplificar, considérese el caso p = q = . Entonces
1  1
0  2  0  0
1  1
R=  2  0  2  ,  S=  0 0
( 0 12 0)  ( 0 12)
1 – 12 0  1 12  2
I – R = – 12 1 – 12  y  (I – R)–1 = 1 2 1 = Q
( 0 – 12 1)  ( 12 1 32)
Esto expresa, por ejemplo, que si el primer jugador inicia con dos canicas, entonces puede esperar
que el juego dure q21 + q22 + q23 = 1 + 2 + 1 = 4 movimientos antes de que gane todo o pierda todo.
Finalmente,

3  3  1
1 12
2 0  4  4
A = QS = 1 2 1  0 0 =  1  1
( 12 1 32)( 0 12)  (
3)
4  4

Por lo tanto, si el jugador 1 inicia con 1 canica (estado transitorio 1) terminará con ninguna canica
3  1
(estado absorbente 1) veces y con todas las 4 canicas (estado absorbente 2) veces.
4  4
```

#### Página 53

```text
9.4 Cadenas de Markov absorbentes  53

PROBLEMAS 9.4

En los problemas del 1 al 10 está dada una matriz. Determine si la matriz es la matriz de transición
de una cadena de Markov absorbente. Si es así, encuentre el número de estados absorbentes.
1  1  1  1
2  2  2  2  1 0
1.  2.  3.
( 0 1)  ( 1 0)  ( 0 1)
1  1  1
1 0 0  0 1 0  3  3  3
4. 0 0 1  5. 1 0 0  6.  0 0 1
( 0 1 0)  ( 0 0 1)  ( 1 1 1)
3  3  3

1  1  1  1  1
2  2  0 0  2  3  6  0
1  1  1
2  6  3  1 0 0 0  0 1 0 0
7.  0 1 0  8.  9.
( 0 0 1)  (0 0
0 0 1 0
1  1)  (
0 0 1 0
1  3  1  )
2  2  2  8  0  8
1  4
5  5  0 0
1  1  1
0  3  3  3
10.
( 0 0 0 1)
0 0 1 0

En los problemas del 11 al 20 está dada la matriz de transición de una cadena de Markov absorbente.
Determine las matrices T′, R, S, Q y A.
1  2
3  3  1 0
11.  12.
( 0 1)  ( 34 14)
1  1  1
3  3  3  0.2 0.7 0.1
13.  1  1  14.
0  0.6 0.1 0.3
( 0 0 1)
2  2
(0 0 1 )
1  1  1
2  3  6  0
0.4 0.4 0.2  1  1  1  1
4  4  4  4
15.  0  1  0  16.
(0 0 1 )
( 0 0 0 1)
0 0 1 0

1 0 0 0
0.21 0.46 0.13  0.20
1  1  1  1
3  3  6  6  0  1  0  0
17.  1  1  18.
( 0 0 0 1)
2  0 0  2
(  0.31 0.25 0.21
0  0  0
0.23
1  )
1  1  1  1  3
8  4  8  6  8
1  2  1  2  1  0.17 0.23 0.15  0.32 0.13
7  7  7  7  7  0  1  0  0  0
1  1  1  1
19.  4  2  0  8  8  20.  0.15 0.21 0  0.38 0.26

(  0 0 0 1 0
0 0 0 0 1
)  (  0
)
```

#### Página 54

```text
54  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

21. Un animal de laboratorio debe completar una cierta tarea para recibir una unidad de alimento. La
probabilidad de la culminación exitosa de la tarea en cualquier intento es . Suponga que el ani-
mal repite la tarea hasta que recibe un total de cuatro unidades de alimento. Describa este proce-
so como una cadena de Markov absorbente con cinco estados. ¿Cuál es la matriz de transición?
22. ¿Cuál es el número esperado de veces que la tarea del problema 21 se repetirá hasta la culmina-
ción exitosa de la tarea?
*23. Dos apostadores, G1 y G2, están jugando un juego; la probabilidad de que G1 gane en cada mo-
vimiento es . Suponga que G1 inicia con 7 dólares y G2 inicia con 1 dólar. En cada jugada
ambos jugadores apuestan 1 dólar y el juego continua hasta que un jugador haya perdido todo
su dinero.
a) Describa este juego como una cadena de Markov absorbente con nueve estados.
b) ¿Cuáles son las distribuciones de probabilidad de los estados después de una jugada y des-
pués de dos jugadas?
c) ¿Cuál es la probabilidad de que G1 gane?
24. En el juego del problema 23 suponga que G2 apuesta todo su dinero en cada jugada del juego.
a) Describa este juego como una cadena de Markov absorbente con cinco estados.
b) ¿Cuál es el número de jugadas esperadas de este juego?
c) ¿Cuál es la probabilidad de que G1 gane?
25. Un animal de laboratorio debe elegir uno de cuatro paneles para recibir alimento. Si se eligen
los paneles I y II, el resultado es una cantidad muy pequeña de alimento. Por su parte, paneles
III y IV contienen mayores cantidades de alimento. Si se elige ya sea el panel III o el panel IV
en un intento, se observa que se elige el mismo panel en todos los intentos futuros. Si se elige
ya sea el panel I o el panel II en un intento, entonces puede elegirse cualquiera de los cuatro
paneles en el siguiente intento con igual probabilidad. Describa este proceso como una cadena
de Markov absorbente con cuatro estados. Si se elige el panel I en el primer intento, ¿cuál es el
número esperado de intentos antes de que se elija el panel III o el panel IV?
26. La empresa Zephyr Electronics fabrica computadoras portátiles. Antes de lanzar a la venta una
computadora pasa una inspección. Las categorías de inspección son: no funciona (NF), regu-
lar, buena y excelente. Las computadoras NF se desechan, mientras que las excelentes de inme-
diato se ponen en venta. Las computadoras regulares y buenas se regresan para ajustes y se re-
visan de nuevo. Las proporciones de computadoras regulares y buenas que cambian de
categoría están dadas en la tabla.

Hacia
NF  Regular  Buena  Excelente
Desde
Regular  0.05  0.25  0.35  0.35

Buena  0  0.15  0.2  0.65

a) Describa este proceso de pruebas como una cadena de Markov absorbente y calcule la ma-
triz de transición.
b) ¿Cuántas veces, en promedio, una computadora calificada como regular se probará de nuevo?
c) ¿Cuántas veces, en promedio, una computadora calificada como buena se probará de nuevo?
d) ¿Cuál es la probabilidad que una computadora regular eventualmente se deseche?
e) ¿Cuál es la probabilidad que una computadora regular eventualmente se ponga a la venta?
f) De 30 000 computadoras que originalmente se calificaron como buenas, ¿cuántas eventual-
mente se pondrán a la venta?
```

#### Página 55

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  55

27. La Mastervise Corporation emite tarjetas de crédito a 20 000 individuos en un cierto estado.
Su auditor descubre que 2 356 de ellos no hicieron sus pagos el mes pasado. Es una política de
la empresa que si no se han hecho pagos durante 3 meses seguidos se cancelan los privilegios
de la tarjeta y la cuenta se entrega a un despacho de cobranza. Experiencias anteriores de Mas-
tervise mostraron las experiencias de cobranza en la tabla.

Hacia  1 mes  2 meses  3 meses  Tarjeta
Pagada
Desde  moroso  moroso  moroso  cancelada
1 mes moroso  0  0.35  0  0.65  0

2 meses moroso  0  0  0.4  0.6  0

3 meses moroso  0  0  0  0.3  0.7

a) Describa este proceso como una cadena de Markov absorbente y encuentre su matriz de
transición.
b) ¿A cuántos de los 2 356 pagadores morosos se les cancelará la tarjeta?
28. Regrese al problema 9.3.36. Asuma que una vez que el ratón llega al compartimento II o al
compartimento IV, se queda ahí.
a) Si un ratón inicia en el compartimento I, ¿cuántos compartimentos visitará en promedio?
b) ¿Qué porcentaje de los ratones que inician en el compartimento III terminarán en el com-
partimento IV?
29. En el ejemplo 9.4.4 se descubre que 30% de los estudiantes de primer año repiten el primer año,
45% pasan al segundo año, y 25% desertan. Si todos los datos permanecen iguales, ¿cuántos de
los actuales 2 000 estudiantes de primer año se graduarán?
*30. a) Considere un juego entre el equipo A y el equipo B con un total de n jugadores en los dos
equipos. En cada jugada del juego un equipo gana un jugador del otro equipo y el juego
continúa hasta que un equipo haya perdido a todos sus integrantes. Si hay k jugadores en el
equipo A y n – k jugadores en el equipo B, la probabilidad de que el equipo A gane un juga-
dor en la siguiente jugada es (k/n)2. Describa este juego como una cadena de Markov absor-
bente. ¿Las reglas son “imparciales”? (Este es un modelo elemental de la competencia entre
especies).
b) Para el juego anterior, suponga que k = 3 y n = 6. ¿Cuál es la distribución de probabilidad
de los equipos después de una jugada? ¿Después de dos jugadas?

9.5 Dos aplicaciones de las cadenas de Markov:
teoría de colas y un modelo en psicología
(opcional)
En esta sección se describen dos aplicaciones interesantes para la teoría de las cadenas de Markov.
La primera aplicación, la teoría de colas, solo necesita del material en la sección 9.3. La segunda
aplicación necesita del material de las secciones 9.3 y 9.4.

Teoría de colas
Una cola es una fila, como en “formémonos en la cola para comprar boletos”. La teoría de colas es la
rama de las matemáticas que describe las filas de espera. Existen muchas aplicaciones de esta teoría.
```

#### Página 56

```text
56  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Por ejemplo, el gerente de un supermercado quiere asegurarse de que 1) no pierde negocio por tener
a muchas personas impacientes esperando en largas filas en las cajas y 2) no pierde dinero pagándole
a empleados de cajas que están ociosos sin clientes a los que atender. Otro ejemplo es suministrado
por los viajeros de una aerolínea. Si alguna vez una persona ha comprado un boleto en el aeropuerto,
tuvo que 1) formarse en una cola para comprar el boleto, 2) formarse en otra cola para pasar la revi-
sión de seguridad, 3) esperar a la salida del avión que está en una cola de aviones esperando para
despegar, 4) hacer lo mismo en el aterrizaje, 5) esperar por el equipaje y 6) esperar en la cola para un
taxi.
En estas y otras situaciones similares resulta de gran interés responder a esta pregunta: ¿Cuál es
el porcentaje de tiempo en que habrá n personas en una cola, donde n = 0, 1, 2, 3, …? Por razones
obvias, el gerente del supermercado o el supervisor en cualquier forma de viaje necesita una respues-
ta a esta pregunta para mantener niveles razonables tanto de satisfacción del cliente como de ganan-
cias. Un análisis general de los modelos de colas está más allá de alcance de este texto. Sin embargo,
se discutirá un modelo simplificado para mostrar cómo puede usarse la teoría de las cadenas de
Markov para obtener una respuesta a la pregunta planteada anteriormente.
Se describe el modelo usando el ejemplo de una sola cola en un mostrador de boletos de una lí-
nea aérea. Se hacen los siguientes supuestos:
1. En un periodo de 1 minuto hay una probabilidad de de que una persona se unirá a la cola y una
probabilidad de de que nadie se unirá a la cola. Por lo tanto, se asume que no más de una per-
sona se unirá a la cola en cualquier intervalo de 1 minuto.
2. Si se atiende a una persona en un periodo, entonces la probabilidad de que una persona haya
recibido su boleto y salga de la cola en el siguiente periodo de tiempo es de .
3. Todas las probabilidades son independientes de qué ha sucedido anteriormente en los periodos.
4. No puede atenderse a una persona en el mismo periodo en el que se unió a la cola.
5. Cuando mucho, puede atenderse a una persona en un solo periodo de 1 minuto.
6. Debido a una política de anticongestionamiento, la cola se cierra si tiene cuatro personas. Es
decir, hay un máximo de cuatro personas en la cola en cualquier tiempo único.

Puede verse este modelo muy simplificado como una cadena de Markov con cinco estados, don-
de el estado del sistema está definido como el número de personas en la cola, incluyendo la persona
a la que se está atendiendo. Los cinco estados están representados por los números 0, 1, 2, 3, y 4. La
matriz de transición para esta cadena de Markov está dada por

0 1 2  3  4
2 1
0  3 3 0 0 0
1 13 5
1  4 24 24 0 0
T= 2  0 14 24
13 5
24 0

(  )
1 13 5
3  0 0 4 24 24
4  0 0 0 38 58

Esto se explica como sigue:
2  1
1.  En el primer renglón se tiene p00 =  y p = . Puede pasarse del estado 0 al estado 0 solo si
3 01 3  2
nadie se une a la cola. De acuerdo con el supuesto 1 este evento tiene una probabilidad de ; el
supuesto 1 también explica por qué p01 = .
```

#### Página 57

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  57

1  13  5
2.  En el segundo renglón se tiene p10 = , p11 = , y p12 = . Para pasar del estado 1 al estado 0
4  24  24
deben ocurrir dos eventos independientes. Primero, se atiende a la persona en la línea, y segun-
do, ninguna persona nueva se une a la cola. La probabilidad del primer evento es (por el su-
puesto 2) y la probabilidad del segundo evento es (por el supuesto 1). Por lo tanto
3 2 1
p10 =  ⋅ =
8 3 4
Después, para pasar del estado 1 al estado 1, una de dos cosas mutuamente excluyentes puede
suceder:
a) No se atiende a nadie y nadie se une a la cola, o
5 2
b) Se atiende a una persona y una persona se une a la cola. La probabilidad de a) es ⋅ y la
8 3
3 1
probabilidad de b) es ⋅ . Por lo tanto
8 3
5 2 3 1 10 13 13
p11 = ⋅ + ⋅ = +  =
8 3 8 3 24 24 24
Finalmente, para pasar del estado 1 al estado 2, se debe tener ninguna persona atendida (con
5  1
probabilidad ) y una persona que se une a la cola (con probabilidad ). Por lo tanto,
8  3
5 1 5
p12 =  ⋅ =
8 3 24
Obsérvese que

1 13 5
p10 + p11 + p12 = +  + =1
4 24 24
3.  Los renglones 3 y 4 se obtienen igual que el renglón 2.
3  5
4.  En el quinto renglón se tiene p43 = y p44 = . Para pasar del estado 4 al estado 3, debe tenerse
8  8
una persona atendida (obsérvese que nadie puede unirse a la cola ahora cerrada, de acuerdo con
el supuesto 6). Igualmente, para pasar del estado 4 al estado 4, no debe haber ninguna persona
atendida (con probabilidad ).
Debe recordarse que una cadena de Markov es regular si alguna potencia Tm de su matriz de
transición T tiene componentes estrictamente positivas. Con una calculadora, se calculan las prime-
ras cuatro potencias de T hasta diez decimales:

0.6667  0.3333  0.0000  0.0000  0.0000
0.2500  0.5417  0.2083  0.0000  0.0000
T≈  0.0000  0.2500  0.5417  0.2083  0.0000

(  0.0000
0.0000
0.0000
0.0000
0.2500
0.0000
0.5417
0.3750
0.2083
0.6250
)
0.5278  0.4028  0.0694  0.0000  0.0000
0.3021  0.4288  0.2257  0.0434  0.0000
T2 ≈  0.0625  0.2709  0.3976  0.2257  0.0434

(  0.0000
0.0000
0.0625
0.0000
0.2709
0.0938
0.4236
0.4375
0.2430
0.4687
)
```

#### Página 58

```text
58  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

0.4526 0.4115 0.1215 0.0145 0.0000
0.3086 0.3894 0.2224 0.0705 0.0090
T3 ≈  0.1094 0.2670 0.3282 0.2214 0.0741

(  0.0156 0.1016 0.2657 0.3770 0.2401
0.0000 0.0234 0.1602 0.4323 0.3841
)
0.4046  0.4041  0.1551 0.0331 0.0030
0.3031  0.3694  0.2192 0.0879 0.0203
T4 ≈  0.1397  0.2631  0.2887 0.2161 0.0924

(  0.0358
0.0059
0.1267
0.0527
0.2593 0.3496 0.2286
0.1997 0.4116 0.3301
)
Dado que T 4 tiene componentes estrictamente positivas, se observa que la cadena de Markov es regular.
Ahora debe recordarse el resultado [ver teorema 9.3.2], que establece que dado que T es una
matriz regular hay un vector de probabilidad t único cuyas componentes son todas positivas tal que
tT = t. Además, las matrices T m se acercan (conforme m se hace más grande) a la matriz P, cada uno
de cuyos renglones es igual al vector t. En este caso las componentes de t son las probabilidades de
largo alcance de la longitud de la cola. Para encontrar t, se inicia con
tT = t
o
2 1
3 3 0 0 0
1 13 5
4 24 24 0 0
(p0  p1  p2  p3  p4)  0 14 24
13 5
24 0  = (p0  p1  p2  p3  p4)

(  )
1 13 5
0 0 4 24 24
0 0 0 38 58
o
2  1
3p0 + 4p1  = p0
1  13  1
3p0 + 24p1 + 4p2  = p1
5  13  1
24p1 + 24p2 + 4p3  = p2
5  13  3
24p2 + 24p3 + 8p4 = p3
5  5
24p3 + 8p4 = p4

Dado que t es un vector de probabilidad, también se tiene
p0 + p1 + p2 + p3 + p4 = 1
Combinando términos, se obtiene el sistema

–13p0 + 14p1  =0
1  11  1
3p0 – 24p1 + 4p2  =0
5  11  1
24p1 – 24p2 + 4p3  =0
5  11  3
24p2 – 24p3 + 8p4 = 0
5  3
24p3 – 8p4 = 0
p0 + p1 + p2 +  p3 + p4= 1
```

#### Página 59

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  59

Ahora se anota el sistema en forma de matriz aumentada y se resuelve mediante reducción de renglo-
nes. Para simplificar, se inicia multiplicando las primeras cinco ecuaciones por 24:

–8  6  0  0 0 ∣ 0
8 –11  6  0 0 ∣ 0
0  5 –11  6 0 ∣ 0
5 –11 9 ∣ 0
(  )
0  0
0  0  0  5 –9 ∣ 0
1  1  1  1 1 ∣ 1

1 –0.75  0  0 0 ∣ 0
8 –11  6  0 0 ∣ 0
R1 → –18R1  0 5  –11  6 0 ∣ 0
5 –11 9 ∣ 0
(  )
0 0
0 0  0  5 –9 ∣ 0
1 1  1  1 1 ∣ 1

1 –0.75  0  0 0 ∣ 0
R2 → R2 – 8R1  0 –5  6  0 0 ∣ 0
R6 → R6 – R1  0 5  –11  6 0 ∣ 0
5 –11 9 ∣ 0
(  )
0 0
0 0  0  5 –9 ∣ 0
0 1.75  1  1 1 ∣ 1

1 –0.75 0  0 0 ∣ 0
0 1  –1.2  0 0 ∣ 0
R2 → –15R2  0 5  –11  6 0 ∣ 0
–11 9 ∣ 0
(  )
0 0  5
0 0  0  5 –9 ∣ 0
0 1.75 1  1 1 ∣ 1

R1 → R1 + 0.75R2  1  0 –0.9  0 0 ∣ 0
R3 → R3 – 5R2  0  1 –1.2  0 0 ∣ 0
R6 → R6 – 1.75R2  0  0 –5  6 0 ∣ 0
–11 9 ∣ 0
(  )
0  0 5
0  0 0  5 –9 ∣ 0
0  0 3.1  1 1 ∣ 1

1 0 –0.9  0  0 ∣ 0
0 1 –1.2  0  0 ∣ 0
R3 → –15R3  0 0 1  –1.2 0 ∣ 0
9 ∣ 0
(  )
0 0 5  –11
0 0 0  5  –9 ∣ 0
0 0 3.1  1  1 ∣ 1
R1 → R1 + 0.9R3
R2 → R2 + 1.2R3  1  0  0  –1.08 0 ∣ 0
R4 → R4 – 5R3  0  1  0  –1.44 0 ∣ 0
R6 → R6 – 3.1R3  0  0  1  –1.2  0 ∣ 0
9 ∣ 0
(  )
0  0  0  –5
0  0  0  5  –9 ∣ 0
0  0  0  4.72 1 ∣ 1
```

#### Página 60

```text
60  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

Dado que el quinto renglón es el negativo del cuarto, se elimina y se continua dividiendo el cuarto
renglón entre –5:

1  0  0 –1.08 0  ∣ 0
0  1  0 –1.44 0  ∣ 0
R4 → –15R4
0  0  1 –1.2  0  ∣ 0

(  0
0 1
0 4.72 1
–1.8 ∣ 0
∣ 1  )
R1 → R1 + 1.08R4
R2 → R2 + 1.44R4  1  0  0  0  –1.944  ∣  0
R3 → R3 + 1.2R4  0  1  0  0  –2.592  ∣  0
R5 → R5 – 4.72R4
0  0  1  0  –2.16  ∣  0

(  0
–1.8
9.496
∣
∣
)
Hasta este punto, todos los números son exactos. Se realizan los cálculos restantes con hasta cinco
decimales de exactitud.

1 0 0 0  –1.944  ∣  0
0 1 0 0  –2.592  ∣  0
R5 → –9.496 R5
0 0 1 0  –2.16  ∣  0

(  0 0 0 1
0 0 0 0
–1.8
∣
∣
0.10531
)
R1 → R1 + 1.944R5
R2 → R2 + 2.592R5  1  0  0  0  0  ∣  0.20472
R3 → R3 + 2.16R5  0  1  0  0  0  ∣  0.27296
R4 → R4 + 1.8R5
0  0  1  0  0  ∣  0.22746

(  0
∣
∣
0.18955
0.10531
)
Por lo tanto, el vector de probabilidad fija está dado por

(p0  p1  p2  p3  p4) = (0.20472 0.27296 0.22746 0.18955 0.10531)

Esto significa, por ejemplo, que el vendedor de boletos está ocioso alrededor de 20% del tiempo (da-
do que p0 ≈ 0.20). Además, la fila está cerrada alrededor del 10% del tiempo dado que p4 ≈ 0.10, y
esto significa que hay cuatro personas en la cola alrededor de 10% del tiempo. Finalmente, se tiene a
una persona en la cola alrededor de 27% del tiempo, dos personas alrededor del 23% del tiempo, y
tres personas alrededor del 19% del tiempo.
De nuevo, se subraya que se ha trabajado con un modelo muy simplificado. No obstante, este
ejemplo muestra el poder de las cadenas de Markov combinado con la teoría de matrices para anali-
zar situaciones interesantes.

Modelo en psicología: aprendizaje asociado por parejas
Como segunda aplicación se presenta un modelo sencillo para analizar un proceso de aprendizaje. Se
procede con cautela porque solo las actividades más elementales y simplificadas de la mente pueden
tratarse con algún tipo de modelo viable. El modelo que se describe fue analizado matemáticamente
por primera vez por G.H. Bower11 y se llama aprendizaje asociado por parejas.

G.H. Bower, “Applications of a Model to Paired Associate Learning”, Psychometrica, 26, (1961): 255-280.
```

#### Página 61

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  61

En el modelo de Bower hay un experimentador y uno o más sujetos. El experimentador diseña
dos conjuntos: un conjunto de estímulos y un conjunto de respuestas. Para cada elemento s en el
conjunto de estímulos S hay una respuesta correcta r en el conjunto de respuestas R. Por lo tanto, en
efecto, el experimentador crea un conjunto de parejas ordenadas de la forma (s, r), donde s ∈ S y r ∈
R. En el experimento original de Bower S y R contienen diez elementos cada uno. Por ejemplo, S
puede contener diez letras y R diez números asignados aleatoriamente a las diez letras. En un contex-
to diferente, S podría contener diez palabras en español y R sus equivalentes en inglés. O, como
ejemplo final, S podría contener diez sílabas sin significado (dah, dum, uph, etc.) y R un grupo de
sílabas adicionales, cada una asociada con las sílabas en S.12
Una vez que se crean S y R, puede iniciar el experimento. En cada intento del experimento, el
experimentador muestra (o dice) un elemento s ∈ S al sujeto, y el sujeto responde con un elemento
r ∈ R. Por supuesto, el sujeto trata de dar la respuesta correcta, la r que está asociada a la s dada. Si
el sujeto da la respuesta correcta, se registra un 0. Si el sujeto da una respuesta incorrecta, se registra
un 1, y el experimentador le dice o muestra la respuesta correcta al sujeto.
Se asume que, inicialmente, el sujeto no sabe las respuestas correctas y debe adivinar. Si el sujeto
adivina incorrectamente, se le da la respuesta correcta y, se supone, empieza a aprender. El experi-
mento continúa hasta que el sujeto es capaz de dar las respuestas correctas al estímulo dado dos veces
seguidas. En este momento se asume que el sujeto ha aprendido completamente las respuestas.
Para analizar este modelo, se deben hacer cinco supuestos más o menos razonables. Se hará re-
ferencia a las parejas estímulo-respuesta con la forma (s, r).

Supuestos

1.  Cada pareja de estímulo-respuesta es uno de dos estados en cualquier intento del experimento:
condicionado (C) o adivinando (G). Está en el estado C si el sujeto ha aprendido la respuesta co-
rrecta (r) a la pregunta dada o estímulo (s). Está en el estado G si el sujeto no sabe la respuesta
correcta y debe adivinar.
2.  Inicialmente, todas las parejas están en el estado G. Es decir, se asume que cuando
inicia el experimento el sujeto no conoce ninguna de las respuestas correctas.
3.  Si un elemento está en el estado C en el n-ésimo intento del experimento, entonces  Nota
permanece en el estado C en todos los intentos futuros. Es decir, una vez que el
sujeto ha aprendido la respuesta correcta a un estímulo dado, ya no la olvida.  El supuesto 4 es el menos razonable
4.  Si un elemento está en el estado G en el n-ésimo intento del experimento, la pro-  de los hechos hasta ahora. Aquí se
está asumiendo que 1) todos los
babilidad es c > 0 de que estará en el estado C en el (n + 1)-ésimo intento del ex-  elementos son igualmente fáciles (o
perimento. Es decir, c es la probabilidad de que el sujeto aprenda la respuesta co-  difíciles) de aprender y 2) no es más
rrecta antes del siguiente intento del experimento.  probable que el sujeto aprenda la
5.  Si el elemento está en el estado G y hay N respuestas posibles, la probabilidad es  respuesta correcta después de muchas
1/N de que el sujeto adivine la correcta. Es decir, en el estado adivinando todas las  adivinanzas que después de solo una.
Se espera que si los sujetos son seres
respuestas tienen igual posibilidad de ser elegidas.
humanos de inteligencia normal, las
probabilidades de aprender se
Con estos supuestos, se puede considerar al proceso de aprender la respuesta correcta  incrementarán después de cada
para cada estímulo como una cadena de Markov con los estados C y G.13 La matriz de  adivinanza y después de cada vez que
transición para esta cadena de Markov es  al sujeto se le da la respuesta correcta.

En el experimento original de Bower el estímulo consistía en diez parejas de letras, y las respuestas eran los números 1 o 2. Es
decir, a los sujetos se les daba una pareja de letras y se les pedía que contestaran “1” o “2”. Después de cada intento, se les decía a
los sujetos si sus respuestas eran correctas o no. Si los sujetos eran capaces de contestar correctamente cada uno de los diez estí-
mulos dos veces seguidas, entonces se asumía que habían aprendido las respuestas correctas y se terminaba el experimento.
Obsérvese que existe una cadena de Markov para cada item de estímulo-respuesta (s, r). Por lo tanto, si hay diez parejas (s, r), como
en el experimento de Bower, entonces hay diez cadenas de Markov. Sin embargo, bajo los supuestos, todas las diez cadenas de
Markov tienen propiedades idénticas.
```

#### Página 62

```text
62  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

C  G
C 1  0
T=  (1)
G ( c 1 – c)
dado que —por el supuesto 3— una vez que se está en C, se queda en C. También —por el supuesto
4— si se está en G, entonces la probabilidad es c de que se estará en C en el siguiente intento del expe-
rimento.
Usando la matriz de transición dada por (1), puede calcularse la probabilidad de que un elemen-
to esté en los estados C o G después de cualquier intento del experimento. Primero, por el supuesto
2, la distribución inicial de probabilidad es

p0 = (0  1)  (2)

Ahora

1  0  1  0  1  0
T2 =
( c 1 – c)( c 1 – c) = ( c[1 + (1 – c)] (1 – c)2)

1  0
T3 =
(c[1 + (1 – c) + (1 – c)2] (1 – c)3)

Siguiendo de esta forma (ver problema 9.5.18), puede demostrarse que

1  0
Tn =  (3)
( c[1 + (1 – c) + (1 – c)2 + … + (1 – c)n–1] (1 – c)n)

La fórmula para la suma de una progresión geométrica es (ver problema 9.5.19)
1 – xn
1 + x + x2 + … + xn–1 =  ,  para x ≠ 1  (4)
1–x
Por lo tanto
1 – (1 – c)n 1 – (1 – c)n
1 + (1 – c) + (1 – c)2 + … + (1 – c)n–1 =  =  (5)
1 – (1 – c)  c
e insertando (5) en (3), se tiene

1  0
Tn =  (6)
(1 – (1 – c)n (1 – c)n)

La probabilidad de que un elemento esté en el estado C o G después del n-ésimo intento es

1  0
pn = p0 T n = (0
(1 – (1 – c)n (1 – c)n) = (1 – (1 – c)  (1 – c)n)
n
1)  (7)

La fórmula (7) es muy reveladora. Dado que 0 < c ≤ 1 (por el supuesto 4), se tiene 0 ≤ 1 – c < 1. Por
n
lo tanto, (1 – c) se acerca cada vez más a cero a medida que n se hace más grande. Esto expresa que
mientas c no sea cero, eventualmente se aprenderá la respuesta correcta al estímulo. Mientras más
grande sea el valor de c, se aprenderá más rápido.

E JE M P LO 9.5.1  Las probabilidades después de 20 intentos

Sea c = 0.25. Entonces 1 – c = 0.75. La siguiente tabla da las probabilidades de que el item esté en el
estado G o C después de cada intento.
```

#### Página 63

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  63

Intento  P(C) = 1 – (0.75)n  P(G) = (0.75)n

0  0  1

1  0.25  0.75

2  0.4375  0.5625

3  0.5781  0.4219

4  0.6836  0.3164

5  0.7627  0.2373

6  0.8220  0.1780

7  0.8665  0.1335

8  0.8999  0.1001

9  0.9249  0.0751

10  0.9437  0.0563

11  0.9578  0.0422

12  0.9683  0.0317

13  0.9762  0.0238

14  0.9822  0.0178

15  0.9866  0.0134

16  0.9000  0.0100

17  0.9925  0.0075

18  0.9944  0.0056

19  0.9958  0.0042

20  0.9968  0.0032

Obsérvese que después del décimo sexto intento hay un 99% de certeza de que el sujeto haya apren-
dido la respuesta correcta.
Resulta interesante analizar esta cadena de Markov en términos de la teoría de cadenas de
Markov absorbentes (ver la sección 9.4). Esta cadena de Markov es absorbente porque el estado C es
absorbente. Ahora se usará la notación de la sección 9.4. Se tiene

G  C
T′ = (1 – c c)

R es la matriz (1 – c) de 1 × 1 e I – R = 1 – (1 – c) = c, de modo que
Q = (I – R)–1 =
c
Es decir, el sujeto estará adivinando —o en estado transitorio G— un promedio de 1/c veces antes de
aprender la respuesta correcta.
```

#### Página 64

```text
64  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

E JE M P LO 9.5.2  Número promedio de adivinanzas antes del aprendizaje

En el ejemplo 9.5.1, c = 0.25, de modo que el sujeto estará adivinando un promedio de 1/0.25 = 4
veces antes de aprender la respuesta correcta.
Se pasará ahora a una situación más complicada (y más interesante). En el modelo ya discutido
no se hizo la distinción entre adivinar correctamente y adivinar incorrectamente para un elemento en
el estado G. Si se desea hacer la distinción entre estas posibilidades, es necesario analizar el modelo
mediante una cadena de Markov con tres estados:

E1: adivinar correctamente
E2: adivinar incorrectamente
E3: condicionado

La matriz de transición para esta cadena de Markov es

E1  E2  E3
(1 – c)  1
(1 – c)(1 –  c
N)
E1
N
T = E2  (1 – c)  1  (8)
(1 – c)(1 – ) c

(  )
N  N
E3  0  0  1

Esto se explica como sigue: p11 es la probabilidad de que un elemento inicie en E1 y se quede en E1.
Para hacer esto, el elemento debe iniciar y permanecer en un estado de adivinando (con probabilidad
1 – c) y debe adivinarse correctamente la respuesta (con probabilidad 1/N, por el supuesto 5). Por lo
tanto
1  1–c
p11 = (1 – c) = (  =
N)  N
Igualmente, p21 = (1 – c)/N. Después, p12 es la probabilidad de que el elemento inicie y permanezca
en un estado adivinando (con probabilidad 1 – c) y que el sujeto adivine incorrectamente (con pro-
babilidad 1 – 1/N). Por lo tanto, p12 = (1 – c)(1 – 1/N). El mismo razonamiento demuestra que p22 =
(1 – c)(1 – 1/N). Finalmente, las otras probabilidades se deducen del modelo más sencillo discutido
anteriormente. De los supuestos, resulta aparente que la distribución inicial de probabilidad es

1  1
p0 = (  1–  0)
N  N

En nuestra nueva cadena de Markov los estados transitorios son E1 y E2, mientras que el estado E3 es
absorbente. La matriz R está dada por

1–c  1
(1 – c)(1 – )
N  N
R=  (9)
(  1–c
N
(1 – c)(1 – )
N  )
E JE M P LO 9.5.3  Número promedio de adivinanzas antes del aprendizaje

Se considera el experimento del ejemplo 9.5.1 con N = 5. Entonces como c = 0.25, se tiene [de (8) y
(9) y del hecho que (1 – c)/N = (1 – 0.25)/5 = 0.75/5 = 0.15]
```

#### Página 65

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  65

0.15 0.6 0.25
0.15 0.6  0.85 –0.6
T=  0.15 0.6 0.25 ,  R=  I–R=
( 0.15 0.6),  ( –0.15 0.4)
(0 0 1 )
y

1  0.4 0.6  1.6 2.4
Q = (I – R)–1 =  =  =
0.25 ( 0.15 0.85 ) ( 0.6 3.3)

Inicialmente, el sujeto está en el estado E1 (adivinanza incorrecta) con probabilidad = 0.2 y el esta-
do E2 con probabilidad 0.8. Por lo tanto el número esperado de veces que estará en el estado E1 es

P(E1) × (número esperado de veces en E1 cuando inicia en E1)
+ P(E2) × (número esperado de veces en E1 cuando inicia en E2)
= (0.2)(1.6) + (0.8)(0.6) = 0.8

Igualmente, el número esperado de veces en E2 es

(0.2)(2.4) + (0.8)(3.4) = 3.2

Es decir, el sujeto adivinará correctamente un promedio de 0.8 veces e incorrectamente un promedio
de 3.2 veces antes de haber aprendido la respuesta correcta.

PROBLEMAS 9.5

1. En el modelo de las colas descrito en esta sección, suponga que la probabilidad de que una
1  4
persona se una a la cola es y de que nadie se una es . Suponga que la probabilidad de que
5  5 1
una persona atendida esté fuera de la cola en un periodo es . Conserve los supuestos 3 al 6.
a) Encuentre la matriz asociada con la cadena de Markov inherente en el modelo.
b) Demuestre que la cadena de Markov es regular.
c) Encuentre las probabilidades de largo alcance de que n personas estarán en la fila, para n =
0, 1, 2, 3, y 4.
2. En un supermercado el número de personas que se unen a la fila de la caja rápida (personas
con menos de 10 artículos) es aleatorio pero promedia siete personas cada 10 minutos entre el
mediodía y las 2 pm. Una persona atendida habrá dejado la fila 1 minuto más tarde con proba-
bilidad . Si cinco personas están formadas, la línea se cierra. Estime el porcentaje de tiempo
que
a) El cajero estará ocioso.
b) La fila estará cerrada.
c) Estarán en la fila exactamente tres personas.
3. Responda las preguntas del problema 2 si se cierra la fila cuando hay seis personas en la fila y
todos los demás hechos permanecen iguales.
4. Un estudiante está tomando un curso de lectura en francés. Aprende el vocabulario mediante
palabras en francés puestas en un lado de una tarjeta y sus equivalentes en inglés en el otro la-
do. Hay 10 tarjetas. Se hacen los siguientes supuestos:
```

#### Página 66

```text
66  CAPÍTULO 9  Cadenas de Markov y teoría de juegos

i. Inicialmente, el estudiante conoce las diez palabras en inglés pero no tiene idea de qué pa-
labra en francés va con qué palabra en inglés. Está adivinando.
ii. Se muestra al estudiante una palabra en francés, él da un equivalente en inglés y si está co-
rrecto, se le muestra el otro lado de la tarjeta. El estudiante conoce la palabra o está adivi-
nando.
iii. Si el estudiante está adivinando, elige una de las diez respuestas en inglés aleatoriamente.
iv. Una vez que el estudiante aprende una palabra, la recuerda.
v. Si adivina (correcta o incorrectamente) y si entonces se le muestra la palabra correcta, la
probabilidad de que sabrá el equivalente en inglés de la palabra en francés que acaba de ver
la próxima vez que la vea es 0.3.
Con estos supuestos, encuentre la matriz de transición de la cadena de Markov con estados K
(para saber una palabra dada) y G (para adivinar).
5. En el problema 4, ¿cuál es la probabilidad de que el estudiante haya aprendido la traducción
correcta de una palabra en francés dada antes de adivinar cuatro veces?
6. En el problema 4, ¿cuántas veces debe repetirse el experimento hasta que la probabilidad de
que el estudiante se haya aprendido la palabra sea del 98%?
7. En el problema 4, ¿cuál es el número esperado de veces en que el estudiante adivinará hasta que
se aprenda la palabra?
8. En el problema 4, encuentre la matriz de transición de la cadena de Markov asociada con tres
estados: adivinando correctamente, adivinando incorrectamente y conociendo.
9. En el problema 8, ¿cuál es el número esperado de veces en que el estudiante adivinará incorrec-
tamente hasta que sepa una palabra dada?
10. En el problema 8, ¿cuál es el número esperado de veces en que el estudiante adivinará correc-
tamente hasta que sepa la palabra?
11. En un experimento se coloca a un mono frente a cuatro puertas. Cada puerta tiene un marca-
dor azul, rojo, verde o café. Detrás de la puerta verde hay un plátano. Se le permite al mono
abrir una de las puertas. Si elige la puerta verde, se le recompensa al obtener el plátano. Si elige
cualquier otra puerta, se le muestra el plátano, pero no se le da. El experimento se repite mo-
viendo los marcadores y de nuevo poniendo el plátano detrás de la puerta verde. El objeto
es determinar cuánto le toma al mono averiguar que no es la puerta sino el color lo que deter-
mina la ubicación de la recompensa. Experimentos previos con otros monos han indicado que
el mono tiene una probabilidad del 40% de aprender de qué se trata después de la primera
adivinanza. Utilice el supuesto del problema 4 y encuentre la matriz de transición de este expe-
rimento.
12. En el problema 11, ¿cuál es la probabilidad de que mono haya averiguado las reglas antes de su
tercer intento por el plátano?
13. En el problema 11, ¿cuántos intentos debe tener el mono para tener al menos 95% de certeza
de que ha aprendido a jugar?
14. En el problema 11, ¿cuántas adivinanzas hará el mono, en promedio, hasta que conozca las
reglas?
15. En el problema 11 encuentre la matriz de transición para la cadena de Markov asociada con
tres estados: adivinando correctamente, adivinando incorrectamente y conociendo las reglas.
16. En el problema 15, ¿cuál es el número esperado de veces en que el mono adivinará correcta-
mente hasta que aprenda a jugar?
```

#### Página 67

```text
9.5  Dos aplicaciones de las cadenas de Markov: teoría de colas y un modelo en psicología  67

17. En el problema 15, ¿cuál es el número esperado de veces en que el mono adivinará correcta-
mente?
*18. Demuestre que la fórmula (3) es verdadera.
19. Sea S = 1 + x + x2 + … + xn.
a) Calcule xS.
b) Calcule (1 – x)S
n+1
c) Demuestre que S = (1 – x )/(1– x) si x ≠ 1.
20. En el modelo en este capítulo se discutieron las cadenas de Markov de dos y tres estados. Sea
que E(G), E(GC), y E(G1) denotan el número esperado de adivinanzas en la cadena de Markov
de dos estados, el número esperado de adivinanzas correctas en la cadena de Markov de tres
estados, y el número esperado de adivinanzas incorrectas en la cadena de Markov de tres esta-
dos, respectivamente.
Demuestre que
E(GC) + E(GI) = E(G)
*21. Si T está dada por (8), demuestre que

1  1
(1 – c)n  1 – (1 – c)n
(1 – N)(1 – c)
n
N
Tn =  1  1
(1 – c)n  1 – (1 – c)n
(1 – N)(1 – c)
n

(  )
N
0  0  1
```


