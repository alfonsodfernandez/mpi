# Ejercicios de repaso resueltos (Grupo B)

Ejercicios con solución de los 5 temas. Los temas 2–5 eran escaneos y están transcritos a mano.

**Contenido de este archivo:**
- Tema 1 · Sistemas lineales
- Tema 2 · Matrices
- Tema 3 · Espacios vectoriales
- Tema 4 · Aplicaciones lineales
- Tema 5 · Autovalores y diagonalización


## Tema 1 · Sistemas lineales

*Fuente: `GRUPO B/EJERCICIOS DE REPASO/Ejercicios de repaso Tema 1 Sistemas Lineales.pdf`*

#### Página 1

```text
Boletín 1. Sistemas de Ecuaciones
Lineales y Matrices.

1. Resolver los siguientes sistemas por el método de Gauss-Jordan y por el método de Gauss.
;  ;
?  x1 + x2 + 2x3 = 8  ? 2x1 + 2x2 + 2x3 = 0
a)  −x1 − 2x2 + 3x3 = 1  b)  −2x1 + 5x2 + 2x3 = 1
=  =
3x1 − 7x2 + 4x3 = 10  8x1 + x2 + 4x3 = −1
;
A  x − y + 2z − w = −1  ;
A
?  ?  −2b + 3c = 1
2x + y − 2z − 2w = −2
c)  d)  3a + 6b − 3c = −2
A
A  −x + 2y − 4z + w = 1  =
=  6a + 6b + 3c = 5
3x − 3w = −3
;  ;
? 2x1 − 3x2 = −2  ? 4x1 − 8x2 = 12
e)  2x1 + x2 = 1  f)  3x1 − 6x2 = 9
=  =
3x1 + 2x2 = 1  −2x1 + 4x2 = −6
½  ½
5x1 − 2x2 + 6x3 = 0  x1 − 2x2 + 3x3 = 0
g)  h)
−2x1 + x2 + 3x3 = 1  −2x1 + 4x2 − 6x3 = 1
Solución:
En todos los apartados aplicaremos primeramente el método de Gauss y a continuación el método
de Gauss—Jordan.
3  4  3  4  3  4
1  1 2  8  1  1  2  8  1  1  2  8
F21 (1)  F2 (−1)
(a) C −1 −2 3  1 D −→ C 0  −1  5  9 D −→ C 0  1 −5  −9 D
F31 (−3)
3 −7 4 10  0 −10 −2 −14  0 −10 −2 −14
3  4  3  4
1 1  2  8  1 1  2  8
F32 (10)  F3 (−1/52)
−→ C 0 1  −5  −9 D −→ C 0 1 −5 −9 D.
0 0 −52 −104  0 0  1  2
Por consiguiente, el sistema inicial es equivalente al sistema triangular superior
;
? x1 + x2 + 2x3 = 8
x2 − 5x3 = −9
=
x3 = 2

Así, el sistema dado es compatible determinado (C.D.) y usando el método de subida su
única solución es x1 = 3, x2 = 1, x3 = 2.
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
(forma escalonada).
3  4  3  4  3  4
1 1  2  8  1 1 0 4  1 0 0 3
F23 (5)  F12 (−1)
C 0 1 −5 −9 D −→ C 0 1 0 1 D −→ C 0 1 0 1 D .
F13 (−2)
0 0  1  2  0 0 1 2  0 0 1 2

```

#### Página 2

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  4
;
? x1 = 3
Luego, el sistema inicial es equivalente a x2 = 1 y su solución ya está dada.
=
x3 = 2
3  4  3  4  3  4
2 2 2  0  1 1 1  0  1  1  1  0
F2 (1/2)  F21 (2)  F2 (1/7)
(b) C −2 5 2  1 D −→ C −2 5 2  1 D −→ C 0  7  4  1 D −→
F31 (−8)
8 1 4 −1  8 1 4 −1  0 −7 −4 −1
3  4  3  4
1  1  1  0  1 1  1  0
F23 (7)
C 0  1 4/7 1/7 D −→ C 0 1 4/7 1/7 D .
0 −7 −4 −1  0 0  0  0
En consecuencia, el sistema es compatible indeterminado (C.I.), ya que la matriz escalonada
posee dos unos principales
½ y aparece, por tanto, x3 como variable libre. El sistema inicial es
x1 + x2 + x3 = 0
equivalente al sistema  y el conjunto de sus soluciones puede escribirse
x2 + 4x3 /7 = 1/7
;
? x1 = −1/7 − 3t/7
en la forma  x2 = 1/7 − 4t/7  con t ∈ R.
=
x3 = t
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
(forma escalonada).
3  4  3  4
1 1  1  0  1 0 −3/7 −1/7
C 0 1 4/7 1/7 D F12  (−1)
−→ C 0 1  4/7  1/7 D .
0 0  0  0  0 0  0  0
½
x1 − 3x3 /7 = −1/7
Por tanto, el sistema inicial equivale a  y el conjunto de soluciones
x2 + 4x3 /7 = 1/7
;
? x1 = −1/7 − 3s
también puede expresarse en la forma  x = 1/7 − 4s  con s ∈ R.
= 2
x3 = 7s
3  4  3  4
1 −1  2 −1 −1  1 −1  2 −1 −1
E 2  1 −2 −2 −2 F  (−2) E 0  3 −6  0  0 F
(c) E  F F21 −→ E
(1/3)
F F2−→
C −1  2 −4  1  1 D  F31 (1) C  0  1 −2  0  0 D
F41 (−3)
3  0  0 −3 −3  0  3 −6  0  0
3  4  3  4
1 −1  2 −1 −1  1 −1  2 −1 −1
E 0  1 −2  0  0 F  (−1) E 0  1 −2  0  0 F
E  F F32
−→  E  F.
C 0  1 −2  0  0 D F42 (−3) C 0  0  0  0  0 D
0  3 −6  0  0  0  0  0  0  0
½
x − y + 2z − w = −1
En consecuencia, el sistema inicial es quivalente al sistema
y − 2z = 0
Aparecen dos unos principales en la matriz escalonada y el sistema tiene a las incógnitas z
y w como variables libres.
; El sistema es, por tanto, C.I. y sus inﬁnitas soluciones pueden
A
A x = −1 + µ
?
y = 2λ
escribirse en la forma  con λ, µ ∈ R.
A
A z=λ
=
w=µ
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
```

#### Página 3

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  5

(forma escalonada).
3  4  3  4
1 −1  2  −1  −1  1 0  0 −1 −1
E 0  1  −2  0  0 F  E 0 1 −2  0  0 F
E  12 (1)
F F−→  E  F.
C 0  0  0  0  0 D  C  0 0  0  0  0 D
0  0  0  0  0  0 0  0  0  0
½
x − w = −1
Por tanto, el sistema inicial es equivalente a  y es sencillo escribir x e y en
y − 2z = 0
función de las variables libres z y w.
3  4  3  4  3  4
0 −2  3  1  3  6 −3 1  1  2 −1 1/3
P12 C  F1 (1/3)  F31 (−6)
(d) C 3  6 −3 −2 D −→  0 −2  3 1 D −→ C 0 −2  3  1 D −→
6  6  3  5  6  6  3 5  6  6  3  5
3  4
1  2 −1 1/3
F2 (−1/2)
C 0 −2  3  1 D −→
0 −6  9  3
3  4  3  4
1  2  −1  1/3  1 2  −1  1/3
F32 (6)
C 0  1 −3/2 −1/2 D −→ C 0 1 −3/2 −1/2 D.
0 −6  9  3  0 0  0  0
½
a + 2b − c = 1/3
Por consiguiente, el sistema es equivalente al sistema  y es C.I. Las
b − 3c/2 = −1/2
;
? a = 4/3 − 2λ
inﬁnitas soluciones pueden escribirse en la forma  b = −1/2 + 3λ/2 con λ ∈ R.
=
c=λ
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
(forma escalonada).
3  4  3  4
1 2  −1  1/3  1 0  2  4/3
C 0 1 −3/2 −1/2 D F12  (−2)
−→ C 0 1 −3/2 −1/2 D .
0 0  0  0  0 0  0  0
½
a + 2c = 4/3,
El sistema dado es equivalente a  la variable c es libre y las inﬁnitas
b − 3c/2 = −1/2,
;
? a = 4/3 − 2λ
soluciones se pueden expresar en la forma  b = −1/2 + 3λ/2 con λ ∈ R.
=
c=λ
3  4  3  4  3  4
2 −3 −2  1 −3/2 −1  1 −3/2 −1
F1 (1/2)  F12 (−2)  F2 (1/4)
(e) C 2  1  1 D −→ C 2  1  1 D −→ C 0  4  3 D −→
F31 (−3)
3  2  1  3  2  1  0 13/2  4
3  4  3  4
1 −3/2 −1  1 −3/2  −1
F32 (−13/2)
C 0  1 3/4 D −→ C 0  1  3/4 D . El sistema es equivalente a
0 13/2  4  0  0 −7/8
;
? x1 − 3x2 /2 = −1
x2 = 3/4 y por tanto, incompatible.
=
0 = −7/8
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
(forma escalonada).
3  4  3  4
1 −3/2  −1  1 0 −17/8
F12 (−3/2)
C 0  1  3/4 D −→ C 0 1  3/4 D
0  0 −7/8  0 0  −7/8
```

#### Página 4

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  6
;
? x1 = −17/8
El sistema es equivalente a  x2 = 3/4 y de nuevo vemos que es incompatible.
=
0 = −7/8
3  4  3  4  3  4
4 −8 12  1 −2  2  1 −2 2
F1 (1/4)  F21 (−3)
(f) C 3 −6  9 D −→ C 3 −6  9 D −→ C 0  0 0 D.
F31 (2)
−2  4 −6  −2  4 −6  0  0 0
El sistema inicial es C.I. y equivalente al sistema con una ecuación y dos incógnitas
½
x1 = 3 + 2t
x1 −2x2 = 3. Por tanto, las inﬁnitas soluciones pueden escribirse en la forma
x2 = t
con t ∈ R.
En este caso, la matriz escalonada anterior es también escalonada reducida por lo que los
métodos de Gauss y Gauss—Jordan “coinciden”.
µ  ¶  µ  ¶  µ  ¶
5 −2 6 0  F1 (1/5)  1 −2/5 6/5 0  F21 (2)  1 −2/5 6/5 0  F2 (5)
(g)  −→  −→  −→
−2  1 3 1  −2  1  3 1  0  1/5 3/5 1
µ  ¶
1 −2/5 6/5 0
.
0  1  3 5
½
x1 − 2x2 /5 + 6x3 /5 = 0,
El sistema inicial es C.I. y equivalente al sistema
x2 + 3x3 = 5.
;  12
? x1 = 2 − 5 t
Así, el conjunto de soluciones adquiere la forma  x = 5 − 3t con t ∈ R.
= 2
x3 = t
Seguimos realizando las transformaciones elementales (t.e.) en la última matriz ampliada
(forma escalonada).
µ  ¶  µ  ¶
1 −2/5 6/5 0  F12 (2/5)  1 0 12/5 2
−→  . Observamos que el sistema inicial
0  1  3 5  0 1  3 5
½
x1 + 12x3 /5 = 0,
es equivalente a
x2 + 3x3 = 5.
µ  ¶  µ  ¶
1 −2  3 0  F21 (2)  1 −2 3 0
(h)  −→  . El sistema es incompatible y la forma
−2  4 −6 1  0  0 0 1
escalonada anterior es escalonada reducida.

2. Sin usar lápiz y papel, determinar cuáles de los siguientes sistemas homogéneos tienen soluciones
no triviales.
;  ;
? 2x1 − 3x2 + 4x3 − x4 = 0  ? x1 + 3x2 − x3 = 0
a)  7x1 + x2 − 8x3 + x4 = 0  b)  x2 − 8x3 = 0
=  =
2x1 + 8x2 + x3 − x4 = 0  4x3 = 0
½
3x − 2y = 0
c)
6x − 4y = 0
Solución:

(a) En este caso, el sistema es C.I. pues se trata de un sistema homogéneo con más incógnitas
que ecuaciones. Es decir, el sistema posee soluciones no triviales.
(b) El sistema es C.D., ya que es claro que el método de subida nos proporcinaría como única
solución del sistema, la solución trivial.
(c) La segunda ecuación es proporcional a la primera y el sistema es, por tanto, C.I., es decir,
tiene soluciones no triviales.
```

#### Página 5

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  7

3. Resolver los siguientes sistemas homogéneos, por cualquier método
;
;  A  v + 3w − 2x = 0
? 2x − y − 3z = 0  A
?
2u + v − 4w + 3x = 0
a)  −x + 2y − 3z = 0  b)
=  A
A  2u + 3v + 2w − x = 0
x + y + 4z = 0  =
−4u − 3v + 5w − 4x = 0
Solución:
En ambos casos utilizaremos el método de Gauss.
3  4  3  4
2 −1 −3 0  1 −1/2 −3/2 0
F1 (1/2)  F21 (1)
(a) C −1  2 −3 0 D −→ C −1  2  −3 0 D −→
F31 (−1)
1  1  4 0  1  1  4 0
3  4  3  4
1 −1/2 −3/2 0  1 −1/2 −3/2 0
F2 (2/3)  F32 (−3/2)
C 0  3/2 −9/2 0 D −→ C 0  1  −3 0 D −→
0  3/2 11/2 0  0  3/2 11/2 0
3  4  3  4
1 −1/2 −3/2 0  1 −1/2 −3/2 0
F3 (1/10)
C 0  1  −3 0 D −→ C 0  1  −3 0 D.
0  0  10 0  0  0  1 0
Puesto que la matriz escolonada posee tres unos principales, el mismo número que incóg-
nitas, el sistema es C.D. y la única solución del mismo es la trivial (x = y = z = 0).
3  4  3  4
0  1  3 −2 0  2  1 −4  3 0
E 2  1 −4  3 0 F  P21 E  3 −2 0 F
(b) E  F −→  E 0  1  F F1−→ (1/2)
C 2  3  2 −1 0  D  C  2  3  2 −1 0  D
−4 −3  5 −4 0  −4 −3  5 −4 0
3  4  3  4
1 1/2 −2 3/2 0  1 1/2 −2 3/2 0
E 0  1  3 −2 0 F  (−2) E 0  1  3 −2 0 F
E  F F31 −→ E  F F32 −→
(−2)
C 2  3  2 −1 0  D  F41 (4)  C  0  2  6 −4 0  D  F41 (1)
−4 −3  5 −4 0  0 −1 −3  2 0
3  4
1 1/2 −2 3/2 0
E 0  1  3 −2 0 F
E  F.
C 0  0  0  0 0 D
0  0  0  0 0
½
u − v/2 − 2w + 3x/2 = 0,
El sistema inicial es equivalente a  es C.I. y tomamos w y x
v + 3w − 2x = 0,
como variables libres. Así, el conjunto
;  de soluciones puede escribirse, después de aplicar el
A
A  u =  t/2 − s/2
?
v = −3t + 2s
método de subida, en la forma  con t, s ∈ R.
A
A  w=t
=
x=s

4. Resolver los siguientes sistemas, donde a, b y c son constantes.
;
½  ? x1 + x2 + x3 = a
2x + y = a
a)  b)  2x1 + 2x3 = b
3x + 6y = b  =
3x2 + 3x3 = c
Solución:
Aplicaremos en ambos casos el métdo de Gauss.
µ  ¶  µ  ¶  µ  ¶
2 1 a  F1 (1/2)  1 1/2 a/2  F21 (−3)  1  1/2  a/2  F2 (2/9)
(a)  −→  −→  −→
3 6 b  3  6  b  0  9/2  b − 32 a
```

#### Página 6

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  8
µ  ¶  ½
1 1/2  a/2  x + 12 y = 12 a
2  1  . El sistema  inicial es  C.D y equivalente  a  y
0  1 9b − 3a  y = 29 b − 13 a
aplicando el método de subida la única solución es
µ  ¶
2  1  1  1  1  1 2  1  2  1
y = b − a,  x= a− y = a−  b − a = a − b.
9  3  2  2  2  2 9  3  3  9
3  4  3  4  3  4
1 1 1 a  1  1 1  a  1 1 1  a
F21 (−2)  F2 (−1/2)  F32 (−3)
(b) C 2 0 2 b D −→ C 0 −2 0 b − 2a D −→ C 0 1 0 a − 12 b D −→
0 3 3 c  0  3 3  c  0 3 3  c
3  4  3  4
1 1 1  a  1 1 1  a
C 0 1 0  a − 12 b  D F3−→(1/3)
C 0 1 0  a − 12 b  D.
3  1  1
0 0 3 c − 3a + 2 b  0 0 1 3c − a + 2b
;
? x1 + x2 + x3 = a
El sistema inicial es C.D., equivalente a  x2 = a − 12 b  y aplicando el
=
x3 = 13 c − a + 12 b
;
? x1 = a − 13 c
método de subida la única solución es  x = a − 1b
= 2 1 2
x3 = 3 c − a + 12 b
;
?  x + 2y − 3z = 4
5. ¿Para qué valores de a el sistema  3x − y + 5z = 2 no tiene solución, tiene exac-
=
4x + y + (a2 − 14)z = a + 2
tamente una solución o inﬁnitas soluciones?
Solución:
Realizaremos t.e. en la matriz ampliada.
3  4  3  4
1  2  −3  4  1  2  −3  4
F21 (−3)  F2 (−1/7)
C 3 −1  5  2 D −→ C 0 −7  14  −10 D −→
F  (−4)
4  1 a2 − 14 a + 2  31
0 −7 a2 − 2 a − 14
3  4  3  4
1  2  −3  4  1 2  −3  4
F32 (7)
C 0  1  −2  10/7 D −→ C 0 1  −2  −10/7 D.
0 −7 a − 2 a − 14  2
0 0 a − 16 a − 4
Por tanto, si a2 − 16 6= 0 (o equivalentemente, a 6= 4 y a 6= −4) podemos continuar realizando
t.e.
3  4 ³  ´ 3  4
1 2  −3  4  F3 2 1  1 2 −3  4
C 0 1  −2  −10/7 D −→ C 0 1 −2 −10/7 D =
a −16

a−4
0 0 a2 − 16 a − 4  0 0 1  a2 −16
3  4
1 2 −3  4
C 0 1 −2 −10/7 D . Así, el sistema es C.D. (posee una única solución)
0 0 1  a+4
Si a = 4, el primer bloque de t.e. sigue siendo válido y llegamos a la matriz ampliada
3  4
1 2 −3  4
C 0 1 −2 −10/7 D. En consecuencia, el sistema es C.I. (posee inﬁnitas soluciones).
0 0 0  0
3  4
1 2 −3  4
Si a = −4, la última matriz ampliada del primer bloque de t.e. es C 0 1 −2 −10/7 D y
0 0 0  −8
el sistema es imcompatible (no posee solución).
```

#### Página 7

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  9
½
(a − 3)x + y = 0
6. ¿Para qué valores de a el sistema  tiene soluciones no triviales?
x + (a − 3)y = 0
Solución:
Realizaremos t.e. en la matriz ampliada.

— Comenzamos suponiendo que a − 3 6= 0 (es decir, a 6= 3).
µ  ¶  1  µ  1  ¶  µ  1  ¶
a−3  1  0  F1 ( a−3 )  1  0  F21 (−1)  1  0
−→  a−3  −→  a−3  =
1  a−3 0  1 a−3 0  0  a − 3 − a−3  0
Ã  1
!
1  a−3  0
(a−3)2 −1  .
0  a−3  0
Ahora consideramos, además, que (a − 3)2 − 1 6= 0 (esto es, a 6= 2 y a 6= 4). Entonces,
podemos continuar con las t.e.
Ã  1
! ³ a−3 ´ µ  ¶
1  0  F2  1
a−3  (a−3)2 −1  1 a−3  0
2  −→  y deducir que el sistema es C.D.; es
0 (a−3)a−3
−1
0  0  1  0
decir, sólo posee la solución trivial x = 0, y = 0.
Seguidamente, tomamos a =µ2 o a = 4. Entonces,  ¶  después del primer bloque de t.e. con-
1 a−3  0
seguimos la matriz ampliada  y el sistema es C.I.; es decir, posee soluciones
0  0  0
no triviales.
½
y=0
— Suponemos que a = 3, entonces el sistema inicial es  y, naturalmente, su única
x=0
solución es la trivial.

Resumiendo, el sistema posee soluciones no triviales si y sólo si a = 2 o a = 4.
µ  ¶
a b
7. Demostrar que si ad − bc 6= 0 entonces la forma escalonada reducida de la matriz  es
c d
µ  ¶
1 0
.
0 1
Solución:
µ  ¶
a b
Realizaremos transformaciones elmentales (t.e.) en la matriz  .
c d

En primer lugar, suponemos que a 6= 0. De esta forma, podemos hacer las siguientes t.e.
µ  ¶  µ  ¶  µ  ¶  µ  b
¶ µ  b
¶
a b F1 (1/a) 1 ab  F21 (−c)  1 ab  F21 (−c)  1  a  1  a
−→  −→  −→  =
c d  c d  c d  0 d − ab c  0 ad−bc
a
Ahora, si ad − bc 6= 0 podemos continuar realizando t.e.
µ  b
¶  a  µ  ¶  µ  ¶
1  a
F2 ( ad−bc ) 1 b  F12 (−b/a)  1 0
−→  a  −→  .
0 ad−bc
a  0 1  0 1
µ  ¶
a b
Por consiguiente, si a 6= 0 y ad − bc 6= 0 la forma escalonada reducida de  es la
c d
identidad.
¶ µ  µ  ¶
0 b  P12  c d
A continuación suponemos que a = 0 . Entonces, la primera t.e es:  −→  .
c d  0 b
µ  ¶  µ  ¶
c d F1 (1/c) 1 d/c
Si además c 6= 0 podemos continuar realizando t.e.:  −→  .
0 b  0  b
```

#### Página 8

```text
Boletín 1. Sistemas de Ecuaciones Lineales y Matrices  10
µ  ¶  µ  ¶
1 d/c  F2 (1/b)  1 d/c  F12 (−d/c)
Si además b 6= 0 podemos continuar realizando t.e.:  −→  −→
0  b  0  1
µ  ¶
1 0
.
0 1
Por tanto, si a 6= 0, b 6= 0 y c 6= 0 (o equivalentemente, a 6= 0 y bc 6= 0 ), entonces la forma
µ  ¶
a b
escalonada reducida de  es la identidad.
c d

Nótese que para a = 0,µla desigualdad
¶  ad − bc 6= 0 se convierte en bc 6= 0, por que la forma
a b
escalonada reducida de  es la matriz identidad siempre que ad − bc 6= 0.
c d
3  4  3  4
3 0  µ  ¶  µ  ¶  1 5 2
4  −1  1  4  2
8. Considerar las matrices A = C −1 2 D , B =  ,C =  , D = C −1 0 1 D ,
0  2  3 1 5
1 1  3 2 4
3  4
6 1 3
E = C −1 1 2 D . Calcular, cuando sea posible:
4 1 3
¡  ¢
a) D − E, b) 2E T − 3DT c) A(BC) d) (DA)T e) C T B AT f) (−AC)T + 5DT
Solución:
3  4
−5  4 −1
(a) D − E = C 0 −1 −1 D.
−1  1  1
3  4
9 1 −1
(b) 2E T − 3DT = C −13 2 −4 D.
0 1 −6
3  4
3  45 9
(c) A(BC) = C −11 −11 17 D.
7  17 13
µ  ¶
0 −2 11
(d) (DA)T =  .
12  1 8
3  4
¡ T ¢ T  12  6 9
(e) C B A = C 48 −20 14 D.
24  8 16
3  4
2 −10 11
(f) (−AC)T + 5DT = C 13  2 5 D.
4 −3 13
3  4  3  4
3 −2 7  6 −2 4
9. Considerar las matrices A = C 6  5 4 D y B = C 0  1 3 D . Calcular, sin realizar el
0  4 9  7  7 5
producto de las dos matrices completamente,
a) la segunda columna de AB.  b) la primera columna de BA.  c) la tercera columna de
AA.
Solución:
```


## Tema 2 · Matrices

*Fuente: `GRUPO B/EJERCICIOS DE REPASO/Ejercicios de repaso Tema 2 Matrices.pdf`*

#### Página 1

**5. Calcular** $V=\begin{vmatrix}1&1&1\\b+c&c+a&a+b\\bc&ac&ab\end{vmatrix}$

**Solución:**
$$V\overset{(a)}{=}\begin{vmatrix}1&0&0\\b+c&a-b&a-c\\bc&ac-bc&ab-bc\end{vmatrix}\overset{(b)}{=}\begin{vmatrix}a-b&a-c\\c(a-b)&b(a-c)\end{vmatrix}=(a-b)(a-c)\begin{vmatrix}1&1\\c&b\end{vmatrix}=(a-b)(a-c)(b-c)$$
(a) restando la primera columna a la segunda y tercera; (b) desarrollando por la primera fila.

**8. Sin efectuar el desarrollo, probar que** $\Delta=\begin{vmatrix}1&a&b+c\\1&b&c+a\\1&c&a+b\end{vmatrix}=0$

**Solución:** no se altera un determinante si a una línea se le suma una combinación lineal de las demás. Sumando a la tercera columna la segunda:
$$\Delta=\begin{vmatrix}1&a&a+b+c\\1&b&b+c+a\\1&c&c+a+b\end{vmatrix}=(a+b+c)\begin{vmatrix}1&a&1\\1&b&1\\1&c&1\end{vmatrix}=0$$
(hay dos columnas iguales).

#### Página 2

**2. Determinar la inversa de** $A=\begin{pmatrix}1&4&8\\0&1&2\\-1&2&3\end{pmatrix}\in M_3(\mathbb{R})$ **por el método del pivote.**

**Solución:** se yuxtapone $A$ con la identidad: $\bar A=(A\,|\,I)$.

#### Página 3

Se hacen transformaciones elementales de filas hasta convertir $A$ en $I$; lo que queda en el lugar de $I$ es $A^{-1}$:
$$\left(\begin{smallmatrix}1&4&8&|&1&0&0\\0&1&2&|&0&1&0\\0&6&11&|&1&0&1\end{smallmatrix}\right)\sim\left(\begin{smallmatrix}1&4&8&|&1&0&0\\0&1&2&|&0&1&0\\0&0&1&|&-1&6&-1\end{smallmatrix}\right)\sim\left(\begin{smallmatrix}1&4&8&|&1&0&0\\0&1&0&|&2&-11&2\\0&0&1&|&-1&6&-1\end{smallmatrix}\right)\sim\left(\begin{smallmatrix}1&4&0&|&9&-48&8\\0&1&0&|&2&-11&2\\0&0&1&|&-1&6&-1\end{smallmatrix}\right)\sim\left(\begin{smallmatrix}1&0&0&|&1&-4&0\\0&1&0&|&2&-11&2\\0&0&1&|&-1&6&-1\end{smallmatrix}\right)$$
$$A^{-1}=\begin{pmatrix}1&-4&0\\2&-11&2\\-1&6&-1\end{pmatrix}$$
Pasos: (a) $F_3\leftarrow F_3+F_1$; (b) $F_3\leftarrow -F_3+6F_2$; (c) $F_2\leftarrow F_2-2F_3$; (d) $F_1\leftarrow F_1-8F_3$; (e) $F_1\leftarrow F_1-4F_2$.

#### Página 4

**12. Forma escalonada y escalonada reducida de la matriz 3×3 con** a) $a_{ij}=i+j$; b) $a_{ij}=i^{j-1}$; c) $a_{ij}=1$ si $|i-j|>1$, $-1$ si $|i-j|\le1$.

(a) $A=\begin{pmatrix}2&3&4\\3&4&5\\4&5&6\end{pmatrix}\xrightarrow{F_1(1/2)}\xrightarrow{F_{21}(-3),F_{31}(-4)}\begin{pmatrix}1&3/2&2\\0&-1/2&-1\\0&-1&-2\end{pmatrix}\xrightarrow{F_2(-2)}\xrightarrow{F_{32}(1)}\begin{pmatrix}1&3/2&2\\0&1&2\\0&0&0\end{pmatrix}\xrightarrow{F_{12}(-3/2)}\begin{pmatrix}1&0&-1\\0&1&2\\0&0&0\end{pmatrix}$.
Escalonada: $\begin{pmatrix}1&3/2&2\\0&1&2\\0&0&0\end{pmatrix}$; escalonada reducida: $\begin{pmatrix}1&0&-1\\0&1&2\\0&0&0\end{pmatrix}$.

(b) $A=\begin{pmatrix}1&1&1\\1&2&4\\1&3&9\end{pmatrix}\to\begin{pmatrix}1&1&1\\0&1&3\\0&2&8\end{pmatrix}\to\begin{pmatrix}1&1&1\\0&1&3\\0&0&2\end{pmatrix}\to\begin{pmatrix}1&1&1\\0&1&3\\0&0&1\end{pmatrix}$. Escalonada: la última; escalonada reducida: la identidad (tres unos principales ⇒ $A$ regular).

(c) $A=\begin{pmatrix}-1&-1&1\\-1&-1&-1\\1&-1&-1\end{pmatrix}\xrightarrow{F_1(-1)}\begin{pmatrix}1&1&-1\\-1&-1&-1\\1&-1&-1\end{pmatrix}\xrightarrow{F_{21}(1),F_{31}(-1)}\begin{pmatrix}1&1&-1\\0&0&-2\\0&-2&0\end{pmatrix}\xrightarrow{P_{23}}\begin{pmatrix}1&1&-1\\0&-2&0\\0&0&-2\end{pmatrix}\xrightarrow{F_2(-1/2),F_3(-1/2)}\begin{pmatrix}1&1&-1\\0&1&0\\0&0&1\end{pmatrix}$.
*(El original escribe la escalonada como $\begin{pmatrix}1&1&-1\\0&-1&0\\0&0&1\end{pmatrix}$.)* La reducida es la identidad; $A$ es regular.

**14. Sean $A$, $B$ cuadradas del mismo tamaño. ¿Es cierto que $(AB)^2=A^2B^2$?**
En general es falso. Con $A=\begin{pmatrix}1&2\\-1&3\end{pmatrix}$, $B=\begin{pmatrix}-1&0\\2&1\end{pmatrix}$: $(AB)^2=\begin{pmatrix}23&12\\42&23\end{pmatrix}\neq\begin{pmatrix}-1&8\\-4&7\end{pmatrix}=A^2B^2$. Si $A$ y $B$ conmutan ($AB=BA$) sí se cumple: $(AB)^2=ABAB=AABB=A^2B^2$.

#### Página 5

**8. Con** $A=\begin{pmatrix}3&0\\-1&2\\1&1\end{pmatrix}$, $B=\begin{pmatrix}4&-1\\0&2\end{pmatrix}$, $C=\begin{pmatrix}1&4&2\\3&1&5\end{pmatrix}$, $D=\begin{pmatrix}1&5&2\\-1&0&1\\3&2&4\end{pmatrix}$, $E=\begin{pmatrix}6&1&3\\-1&1&2\\4&1&3\end{pmatrix}$, **calcular cuando sea posible:**
- (a) $D-E=\begin{pmatrix}-5&4&-1\\0&-1&-1\\-1&1&1\end{pmatrix}$
- (b) $2E^T-3D^T=\begin{pmatrix}9&1&-1\\-13&2&-4\\0&1&-6\end{pmatrix}$
- (c) $A(BC)=\begin{pmatrix}3&45&9\\-11&-11&17\\7&17&13\end{pmatrix}$
- (d) $(DA)^T=\begin{pmatrix}0&-2&11\\12&1&8\end{pmatrix}$
- (e) $(C^TB)A^T=\begin{pmatrix}12&6&9\\48&-20&14\\24&8&16\end{pmatrix}$
- (f) $(-AC)^T+5D^T=\begin{pmatrix}2&-10&11\\13&2&5\\4&-3&13\end{pmatrix}$

**18. Con** $A=\begin{pmatrix}3&4&1\\2&-7&-1\\8&1&5\end{pmatrix}$, $B=\begin{pmatrix}8&1&5\\2&-7&-1\\3&4&1\end{pmatrix}$, $C=\begin{pmatrix}3&4&1\\2&-7&-1\\2&-7&3\end{pmatrix}$, **encontrar matrices elementales con** $E_1A=B$, $E_2B=A$, $E_3A=C$, $E_4C=A$.
- (a) $B$ es $A$ con filas 1 y 3 intercambiadas: $E_1=P_{13}=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$, y también $E_2=P_{13}$.
- (b) $C$ se obtiene sumando a la fila 3 de $A$ la fila 1 por −2: $E_3=F_{31}(-2)=\begin{pmatrix}1&0&0\\0&1&0\\-2&0&1\end{pmatrix}$; y $E_4=F_{31}(2)=\begin{pmatrix}1&0&0\\0&1&0\\2&0&1\end{pmatrix}$.

#### Página 6

**20. Sea** $A=\begin{pmatrix}1&0\\-5&2\end{pmatrix}$. (a) Encontrar $E_1,E_2$ elementales con $E_2E_1A=I$. (b) Escribir $A^{-1}$ como producto de dos elementales. (c) Escribir $A$ como producto de dos elementales.
- (a) $A\xrightarrow{F_{21}(5)}\begin{pmatrix}1&0\\0&2\end{pmatrix}\xrightarrow{F_2(1/2)}I$; luego $E_1=F_{21}(5)=\begin{pmatrix}1&0\\5&1\end{pmatrix}$, $E_2=F_2(\tfrac12)=\begin{pmatrix}1&0\\0&\tfrac12\end{pmatrix}$.
- (b) $A^{-1}=E_2E_1=\begin{pmatrix}1&0\\0&\tfrac12\end{pmatrix}\begin{pmatrix}1&0\\5&1\end{pmatrix}$.
- (c) $A=E_1^{-1}E_2^{-1}=\begin{pmatrix}1&0\\-5&1\end{pmatrix}\begin{pmatrix}1&0\\0&2\end{pmatrix}$.

**21. Expresar** $A=\begin{pmatrix}0&1&7&8\\1&3&3&8\\-2&-5&1&-8\end{pmatrix}$ **como** $A=EFGR$ **con $E,F,G$ elementales y $R$ escalonada.**
$A\xrightarrow{P_{21}}\begin{pmatrix}1&3&3&8\\0&1&7&8\\-2&-5&1&-8\end{pmatrix}\xrightarrow{F_{31}(2)}\begin{pmatrix}1&3&3&8\\0&1&7&8\\0&1&7&8\end{pmatrix}\xrightarrow{F_{32}(-1)}\begin{pmatrix}1&3&3&8\\0&1&7&8\\0&0&0&0\end{pmatrix}=R$.
$F_{32}(-1)F_{31}(2)P_{21}A=R\Rightarrow A=P_{21}^{-1}F_{31}(2)^{-1}F_{32}(-1)^{-1}R=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\-2&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\0&1&1\end{pmatrix}R$.

#### Página 7

**22. Condiciones sobre las $b$ para que el sistema tenga solución** (método de Gauss):
- a) $6x_1-4x_2=b_1,\ 3x_1-2x_2=b_2$ → $\begin{pmatrix}1&-4/6&b_1/6\\0&0&b_2-b_1/2\end{pmatrix}$: hay solución si $2b_2-b_1=0$ (infinitas, dependiendo de un parámetro).
- b) $x_1-2x_2+5x_3=b_1,\ 4x_1-5x_2+8x_3=b_2,\ -3x_1+3x_2-3x_3=b_3$ → $\begin{pmatrix}1&-2&5&b_1\\0&1&-4&\frac{b_2-4b_1}{3}\\0&0&0&b_3+b_2-b_1\end{pmatrix}$: solución sii $b_3+b_2-b_1=0$ (infinitas, un parámetro).
- c) $x_1-2x_2-x_3=b_1,\ -4x_1+5x_2+2x_3=b_2,\ -4x_1+7x_2+4x_3=b_3$ → $\begin{pmatrix}1&-2&5&b_1\\0&1&0&-4b_1-b_3\\0&0&1&\frac{8b_1-b_2+3b_3}{2}\end{pmatrix}$: siempre tiene solución, y es única para cada $b$.

**26. Valores de $a$ y $b$ para los que** $A=\begin{pmatrix}a+b-1&0\\0&3\end{pmatrix}$ **y** $B=\begin{pmatrix}5&0\\0&2a-3b+7\end{pmatrix}$ **no son invertibles.**
$A$ invertible ⇔ $a+b-1\neq0$; $B$ invertible ⇔ $2a-3b+7\neq0$. Ninguna es invertible (simultáneamente) si $a+b=1$ y $2a-3b=-7$ ⇒ por Gauss $a=-\tfrac45$, $b=\tfrac95$.

#### Página 8

**23. Sea** $A=\begin{pmatrix}2&1&2\\2&2&-2\\3&1&1\end{pmatrix}$, $x=(x_1,x_2,x_3)^T$. (a) Demostrar que $Ax=x$ equivale a $(A-I)x=0$ y resolver. (b) Resolver $Ax=4x$.
- (a) $Ax=Ix\Leftrightarrow(A-I)x=0$, sistema homogéneo con $\begin{pmatrix}1&1&2\\2&1&-2\\3&1&0\end{pmatrix}$; por Gauss se llega a $\begin{pmatrix}1&1&2\\0&1&6\\0&0&1\end{pmatrix}$: sólo la solución trivial $x_1=x_2=x_3=0$.
- (b) $(A-4I)x=0$ con $\begin{pmatrix}-2&1&2\\2&-4&-2\\3&1&-3\end{pmatrix}$ → $\begin{pmatrix}1&-2&-1\\0&1&0\\0&0&0\end{pmatrix}$: infinitas soluciones $x_1=t,\ x_2=0,\ x_3=t$. Comprobación: $A(t,0,t)^T=(4t,0,4t)^T=4(t,0,t)^T$.

#### Página 9

**25. Valores de $a,b,c$ para los que** $A=\begin{pmatrix}2&a-2b+2c&2a+b+c\\3&5&a+c\\0&-2&7\end{pmatrix}$ **es simétrica.**
$A=A^T$ ⇔ $a-2b+2c=3,\ 2a+b+c=0,\ a+c=-2$. Por Gauss: $a=11,\ b=-9,\ c=-13$.

**27. Sea $A$ simétrica.** (a) $A^2$ es simétrica: $(A^2)^T=A^TA^T=AA=A^2$. (b) $2A^2-3A+I$ es simétrica: $(2A^2-3A+I)^T=2(A^2)^T-3A^T+I^T=2A^2-3A+I$.

**28. Descomposición LU de la matriz de coeficientes y resolución del sistema:**
- a) $\begin{pmatrix}-5&-10\\6&5\end{pmatrix}x=\begin{pmatrix}-10\\19\end{pmatrix}$
- b) $\begin{pmatrix}2&8\\-1&-1\end{pmatrix}x=\begin{pmatrix}-2\\2\end{pmatrix}$
- c) $\begin{pmatrix}2&-2&-2\\0&-2&2\\-1&5&2\end{pmatrix}x=\begin{pmatrix}-4\\-2\\6\end{pmatrix}$
- d) $\begin{pmatrix}-3&12&-6\\1&-2&2\\0&1&1\end{pmatrix}x=\begin{pmatrix}-33\\7\\-1\end{pmatrix}$
- e) $\begin{pmatrix}-1&-3&-4\\3&10&-10\\-2&-4&11\end{pmatrix}x=\begin{pmatrix}-6\\-3\\9\end{pmatrix}$
- f) $\begin{pmatrix}2&-4&0&0\\1&2&1&0\\0&-1&0&0\\0&0&0&2\end{pmatrix}x=\begin{pmatrix}8\\0\\1\\0\end{pmatrix}$

(a) $A=LU=\begin{pmatrix}-5&0\\6&-7\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}$. $Ly=b$: $-5y_1=-10,\ 6y_1-7y_2=19\Rightarrow y=(2,-1)$; $Ux=y$: $x_1+2x_2=2,\ x_2=-1\Rightarrow x=(4,-1)$.

#### Página 10

(b) $A=LU=\begin{pmatrix}2&0\\-1&3\end{pmatrix}\begin{pmatrix}1&4\\0&1\end{pmatrix}$; $y=(-1,\tfrac13)$; $x=(-\tfrac73,\tfrac13)$.

(c) $A=LU=\begin{pmatrix}2&0&0\\0&-2&0\\-1&4&5\end{pmatrix}\begin{pmatrix}1&-1&-1\\0&1&-1\\0&0&1\end{pmatrix}$; $y=(-2,1,0)$; $x=(-1,1,0)$.

(d) $A=LU=\begin{pmatrix}-3&0&0\\1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}1&-4&2\\0&1&0\\0&0&1\end{pmatrix}$; $y=(11,-2,1)$; $x=(1,-2,1)$.

#### Página 11

(e) $A=LU=\begin{pmatrix}-1&0&0\\3&1&0\\-2&2&63\end{pmatrix}\begin{pmatrix}1&3&4\\0&1&-22\\0&0&1\end{pmatrix}$; $y=(6,-21,1)$; $x=(-1,1,1)$.

(f) $A=LU=\begin{pmatrix}2&0&0&0\\1&4&0&0\\0&-1&\tfrac14&0\\0&0&0&2\end{pmatrix}\begin{pmatrix}1&-2&0&0\\0&1&\tfrac14&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$; $y=(4,-1,0,0)$; $x=(2,-1,0,0)$.

#### Página 12

**29. Valores de $a$ para los que existe la descomposición LU de $A$, y obtenerla cuando sea posible.** a) $A=\begin{pmatrix}1&1&2\\-1&a&3\\0&2&0\end{pmatrix}$; b) $A=\begin{pmatrix}1&a^2&2\\2&8&-1\\-1&0&0\end{pmatrix}$.

(a) $F_{21}(1)$ da $\begin{pmatrix}1&1&2\\0&a+1&5\\0&2&0\end{pmatrix}$.
**a1)** Si $a\neq-1$ se sigue sin intercambio de filas y
$$A=LU=\begin{pmatrix}1&0&0\\-1&a+1&0\\0&2&\frac{-10}{a+1}\end{pmatrix}\begin{pmatrix}1&1&2\\0&1&\frac{5}{a+1}\\0&0&1\end{pmatrix}$$
(La página repite el enunciado y el apartado a1.)

**b2)** Si $8-2a^2=0$, es decir $a=\pm2$, tras las dos primeras transformaciones queda $\begin{pmatrix}1&4&2\\0&0&-5\\0&4&2\end{pmatrix}$; hay que intercambiar filas ($P_{32}$) para llegar a $U=\begin{pmatrix}1&4&2\\0&1&2\\0&0&1\end{pmatrix}$, por lo que **no es posible obtener la descomposición LU**.


## Tema 3 · Espacios vectoriales

*Fuente: `GRUPO B/EJERCICIOS DE REPASO/Ejercicios de repaso Tema 3 Espacios vectoriales.pdf`*

#### Página 1

**1. Determinar el valor de b para que el siguiente sistema de vectores sea linealmente dependiente:**

a) $\{(2,3),(4,b)\}$. Para que sean linealmente dependientes debe verificarse $(2,3)=\alpha(4,b)$, lo que permite plantear el sistema
$$\begin{cases}2=4\alpha\\3=\alpha b\end{cases}$$
De la primera ecuación $\alpha=\tfrac12$ y, sustituyendo en la segunda, debe ser $b=6$.

b) $\{(1,1,b),(b,3,2),(0,0,b)\}$. Basta con que uno de los vectores sea combinación lineal de los otros dos, es decir, dar a $b$ un valor tal que la matriz
$$\begin{pmatrix}1&b&0\\1&3&0\\b&2&b\end{pmatrix}$$
tenga rango 2:
$$\begin{vmatrix}1&b&0\\1&3&0\\b&2&b\end{vmatrix}=3b-b^2=b(3-b)=0\;\Rightarrow\;b=0\ \text{ó}\ b=3$$

**6. Determinar cuáles de los siguientes conjuntos son base del espacio vectorial que se indica en cada caso.**

a) $\{(1,2,3,4),(0,0,0,0),(-1,5,4,2)\}$ de $\mathbb{R}^4$. **NO**, ya que no es un sistema linealmente independiente (contiene el vector nulo).

b) $\{(0,1,0,0),(1,0,0,0),(0,0,-1,0),(0,0,0,5),(0,0,3,2)\}$ de $\mathbb{R}^4$. **NO**, puesto que hay más vectores que la dimensión del espacio y por tanto es un sistema ligado.

c) $\{(0,1,0,0),(1,0,0,0),(0,0,3,0),(0,0,0,4)\}$ de $\mathbb{R}^4$. **SÍ**, ya que
$$\begin{vmatrix}0&1&0&0\\1&0&0&0\\0&0&3&0\\0&0&0&4\end{vmatrix}=-12\neq0$$
y tenemos tantos vectores LI como dimensión tiene el espacio.

#### Página 2

**4. Expresar el vector $\vec v$ como combinación lineal de los vectores que se indican en cada caso:**

a) $\vec v=(1,-2,3)$ en función de $\{(1,1,1),(2,0,4),(0,3,5)\}$. Buscamos $x,y,z\in\mathbb{R}$ tales que $(1,-2,3)=x(1,1,1)+y(2,0,4)+z(0,3,5)$, es decir,
$$\begin{cases}1=x+2y\\-2=x+3z\\3=x+4y+5z\end{cases}\quad\text{con solución } x=-\tfrac{10}{11},\ y=\tfrac{21}{22},\ z=-\tfrac{4}{11}$$
Por tanto $(1,-2,3)=-\tfrac{10}{11}(1,1,1)+\tfrac{21}{22}(2,0,4)-\tfrac{4}{11}(0,3,5)$.

b) $\vec v=(1,-2,k)$ en función de $\{(3,0,-2),(2,-1,-5)\}$. Buscamos $x,y$ con $(1,-2,k)=x(3,0,-2)+y(2,-1,-5)$:
$$\begin{cases}1=3x+2y\\-2=-y\\k=-2x-5y\end{cases}$$
De la segunda $y=2$ y, sustituyendo en la primera, $x=-1$. Por tanto sólo si $k=-8$ hay dependencia lineal (con coeficientes/coordenadas $x=-1$, $y=2$). *(El original escribe "x = 1", pero del cálculo se obtiene x = −1.)*

**7. ¿Es el conjunto $\{(1,1,4),(0,2,-1),(4,-12,6)\}$ una base de $\mathbb{R}^3$? Hallar las coordenadas respecto de esa base del vector $(1,1,1)$.**

$$\begin{vmatrix}1&0&4\\1&2&-12\\4&-1&6\end{vmatrix}=-36\neq0$$
y tenemos tantos vectores LI como dimensión tiene el espacio, luego es una base. Las coordenadas de $(1,1,1)$ son la solución del sistema $(1,1,1)=x(1,1,4)+y(0,2,-1)+z(4,-12,6)$ *(el original no termina el cálculo)*.

#### Página 3

**14. En $\mathbb{R}^3$ se considera $S=\{(1,1,a),(1,a,1),(a,1,1)\}$ referido a la base canónica. Estudiar la dimensión del subespacio engendrado $L(S)$ en función de $a$.**

La dimensión es el rango del sistema generador: $\operatorname{rg}S=\dim L(S)$.
$$\begin{vmatrix}1&1&a\\1&a&1\\a&1&1\end{vmatrix}=3a-2-a^3=-(a+2)(a-1)^2$$
- a) $a\neq-2,1\Rightarrow\dim L(S)=3$
- b) $a=-2\Rightarrow\dim L(S)=2$
- c) $a=1\Rightarrow\dim L(S)=1$

**15. Determinar una base del subespacio engendrado por $\{(1,2,3,1),(1,3,3,3),(0,1,4,-1),(2,-3,1,1),(4,1,7,3)\}$.**

Hay que quedarse con el mayor subsistema linealmente independiente, es decir, calcular el rango. Mejor que determinantes, usar Gauss con los vectores por filas:
$$\begin{pmatrix}1&2&3&1\\1&3&3&3\\0&1&4&-1\\2&-3&1&1\\4&1&7&3\end{pmatrix}\sim\begin{pmatrix}1&2&3&1\\0&1&0&2\\0&0&4&-3\\0&0&-5&-15\\0&0&0&0\end{pmatrix}$$
Luego el rango es 4 y una base es $\{(1,2,3,1),(1,3,3,3),(0,1,4,-1),(2,-3,1,1)\}$.

#### Página 4

**16. Decidir si los siguientes subconjuntos de $\mathbb{R}^n$ son subespacios vectoriales.**

a) $D=\{(x,y,z,t)\in\mathbb{R}^4: x=y=z=t\}$. Dos elementos se escriben $(x,x,x,x)$ e $(y,y,y,y)$; para $\alpha,\beta\in\mathbb{R}$:
$\alpha(x,x,x,x)+\beta(y,y,y,y)=(\alpha x+\beta y,\ \alpha x+\beta y,\ \alpha x+\beta y,\ \alpha x+\beta y)\in D$. Además $(0,0,0,0)\in D$ (no vacío). **Es subespacio.**

b) $K=\{(x,y,z,t)\in\mathbb{R}^4: 2x+5z=5\}$. Si $(x_1,..,x_4),(y_1,..,y_4)\in K$ entonces $2x_1+5x_3=5$ y $2y_1+5y_3=5$. Para la combinación lineal:
$2(\alpha x_1+\beta y_1)+5(\alpha x_3+\beta y_3)=\alpha(2x_1+5x_3)+\beta(2y_1+5y_3)=5\alpha+5\beta$,
que para $\alpha=\beta=1$ vale 10 ≠ 5. **No es subespacio vectorial.**

#### Página 5

(Repite el apartado 16 b.)

**9. Sea $P_3$ el espacio de polinomios de grado ≤ 3 con coeficientes reales.**
a) Probar que los polinomios $p\in P_3$ con $p(1)=p'(1)=0$ forman un subespacio $F$ de $P_3$. Dar su dimensión.
b) ¿Son $(x-1)^2$ y $x(x-1)^2$ linealmente independientes? Dar una base de $F$.

**Solución a)** Sean $p,q\in F$; veamos si $\lambda p-\mu q\in F$:
$(\lambda p-\mu q)(1)=\lambda p(1)-\mu q(1)=0$ y $(\lambda p-\mu q)'(1)=\lambda p'(1)-\mu q'(1)=0$.

#### Página 6

Luego $\lambda p-\mu q\in F$ y $F$ es subespacio. Si $p(x)=a_3x^3+a_2x^2+a_1x+a_0\in F$:
$$p(1)=a_3+a_2+a_1+a_0=0,\quad p'(1)=3a_3+2a_2+a_1=0\;\Rightarrow\;a_1=-3a_3-2a_2,\ a_0=2a_3+a_2$$
$$p(x)=a_3(x^3-3x+2)+a_2(x^2-2x+1)=a_3p_1(x)+a_2p_2(x)$$
$p_1,p_2\in F$ y son generadores; son independientes (de $a_3p_1+a_2p_2=0$ se sigue $a_3=a_2=0$), luego son base y $\dim F=2$.

Otra forma: si $p\in F$ entonces $p(x)=(x-1)^2(ax+b)=a\,x(x-1)^2+b(x-1)^2$, luego $F$ está generado por dos polinomios independientes y $\dim F=2$.

**b)** $\lambda(x-1)^2+\mu x(x-1)^2=0\Rightarrow \mu x^3+(\lambda-2\mu)x^2+(\mu-2\lambda)x+\lambda=0\Rightarrow\lambda=\mu=0$: son independientes. Como ambos están en $F$ (tienen 1 como raíz de multiplicidad ≥ 2), son base de $F$.

**10. Sean $A=\{a_1,a_2,a_3\}$, $B=\{b_1,b_2,b_3\}$ bases de $\mathbb{R}^3$ con**
$$a_1=b_1-3b_2+4b_3,\quad a_2=b_2+b_3,\quad a_3=b_1+b_2+b_3$$
a) Hallar la matriz que transforma las coordenadas de la base $B$ a la $A$.
b) Sea $C=\{c_1,c_2,c_3\}$ con $c_1=b_1-b_2+b_3$, $c_2=-b_1+b_2$, $c_3=b_2-b_3$. Hallar la matriz de transformación de $B$ a $C$ y de $A$ a $C$.

#### Página 7

**Solución a)** La matriz $S$ de paso de $A$ a $B$ tiene por columnas las coordenadas de los vectores de $A$ en la base $B$:
$$S=\begin{pmatrix}1&0&1\\-3&1&1\\4&1&1\end{pmatrix}\quad(\text{paso de }A\text{ a }B)$$
Multiplicada por un vector columna de coordenadas en $A$ da las coordenadas del mismo vector en $B$. La matriz de paso de $B$ a $A$ es
$$S^{-1}=\frac17\begin{pmatrix}0&-1&1\\-7&3&4\\7&1&-1\end{pmatrix}$$
(hay que invertir el sistema dado para expresar $B$ en función de $A$).

**b)** Matriz de paso de $C$ a $B$: $T=\begin{pmatrix}1&-1&0\\-1&1&1\\1&0&-1\end{pmatrix}$; de $B$ a $C$: $T^{-1}=\begin{pmatrix}1&1&1\\0&1&1\\1&1&0\end{pmatrix}$.
Componiendo: $T^{-1}\circ S=\begin{pmatrix}2&2&3\\1&2&2\\-2&1&2\end{pmatrix}$ es la matriz de paso de $A$ a $C$.

#### Página 8

**11. Estudiar si $w_1=(0,1,-2,1)$, $w_2=(1,1,2,-1)$, $w_3=(1,0,0,1)$, $w_4=(2,2,0,-1)$ forman una base de $\mathbb{R}^4$.**

Forman base si y sólo si son LI: $\lambda_1w_1+\dots+\lambda_4w_4=0\Leftrightarrow\lambda_i=0$, es decir, el sistema homogéneo tiene solución única, lo que equivale a
$$D=\begin{vmatrix}0&1&1&2\\1&1&0&2\\-2&2&0&0\\1&-1&1&-1\end{vmatrix}\neq0$$
$D=-8\neq0$, luego son base.

Observación: para ver si $n$ vectores de un espacio de dimensión $n$ forman base basta calcular el determinante de la matriz cuyas columnas son sus coordenadas respecto de una base y ver si es distinto de cero.


## Tema 4 · Aplicaciones lineales

*Fuente: `GRUPO B/EJERCICIOS DE REPASO/Ejercicios de repaso Tema 4 Aplicaciones lineales.pdf`*

#### Página 1

**2. Dadas $f,g:\mathbb{R}^3\to\mathbb{R}^3$, $f(x_1,x_2,x_3)=(x_1,x_2,x_1+x_2-x_3)$ y $g(x_1,x_2,x_3)=(2x_1,x_2-1,x_3)$, ver si son lineales y, en ese caso, hallar núcleo e imagen.**

$f$ es lineal (comprobación como ejercicio). $g$ **no** es lineal: $g(0,0,0)\neq(0,0,0)$.
$\operatorname{Ker}(f)=\{\bar x: f(\bar x)=\bar0\}$, de ecuaciones $x_1=0,\ x_2=0,\ x_1+x_2-x_3=0$ ⇒ $\operatorname{Ker}(f)=\{(0,0,0)\}$.
$\operatorname{Im}(f)=L(f(B))$ con $B$ cualquier base (p. ej. canónica): $L((1,0,1),(0,1,1),(0,0,-1))=\mathbb{R}^3$.

**3. Dimensión y bases de $\operatorname{Ker}(f)$ e $\operatorname{Im}(f)$:**

a) $f(x_1,x_2,x_3)=(2x_1,x_1+x_2,3x_3)$: $\operatorname{Ker}(f)=\{(0,0,0)\}$, dim 0, sin base. $\operatorname{Im}(f)=L((2,1,0),(0,1,0),(0,0,1))=\mathbb{R}^3$. Bastaba la fórmula de dimensiones: $\dim\operatorname{Im}(f)=3$; una base es cualquier base de $\mathbb{R}^3$.

#### Página 2

b) $f(x_1,x_2)=(2x_1+x_2,\ x_1-2x_2,\ x_2)$: $\operatorname{Ker}(f)=\{(0,0)\}$, dim 0. $\operatorname{Im}(f)=L((2,1,0),(1,-2,1))$, dim 2, base $\{(2,1,0),(1,-2,1)\}$.

c) $f(x_1,x_2,x_3)=(x_1,x_2,x_1+x_2-x_3)$: $\operatorname{Ker}(f)=\{(0,0,0)\}$, sin base. Por la fórmula de dimensiones $3=\dim\operatorname{Ker}+\dim\operatorname{Im}$ ⇒ $\operatorname{Im}(f)=\mathbb{R}^3$.

d) $f(x_1,x_2,x_3,x_4)=(x_1-x_2,\ 2x_3+x_4)$: $\operatorname{Ker}(f)\equiv\{x_1-x_2=0,\ 2x_3+x_4=0\}$; paramétricas $x_1=\lambda,\ x_2=\lambda,\ x_3=-\mu,\ x_4=2\mu$. $\dim\operatorname{Ker}=2$, base $\{(1,1,0,0),(0,0,-1,2)\}$. $\dim\operatorname{Im}=4-2=2$ ⇒ $\operatorname{Im}(f)=\mathbb{R}^2$, base $\{(1,0),(0,1)\}$.

#### Página 3

**7. Sea $f:E\to F$, $\dim E=3$, $\dim F=4$, con $f(e_2)=-e'_1+e'_2-e'_4$, $f(e_3)=e'_1+e'_2-e'_3+e'_4$ y $e_1\in\operatorname{Ker}(f)$. Hallar dimensión y base de $\operatorname{Ker}(f)$ e $\operatorname{Im}(f)$.**

$A=M(f,B,B')=\begin{pmatrix}0&-1&1\\0&1&1\\0&0&-1\\0&-1&1\end{pmatrix}$, $\dim\operatorname{Im}(f)=r(A)=2$, $\dim\operatorname{Ker}(f)=3-2=1$.
$\operatorname{Im}(f)=L((-1,1,0,1),(1,1,-1,1))$ (coordenadas en $B'$), es decir base $\{-e'_1+e'_2-e'_4,\ e'_1+e'_2-e'_3+e'_4\}$.
$\operatorname{Ker}(f)\equiv\{-x_2+x_3=0,\ x_2+x_3=0,\ x_3=0,\ -x_2+x_3=0\}$ ⇒ $x_1=\lambda,\ x_2=0,\ x_3=0$; base $\{e_1\}$.

#### Página 4

**8. Sea $f:\mathbb{R}^2\to\mathbb{R}^4$ con $f(2,-1)=(1,0,-1,3)$ y $f(4,1)=(2,-2,3,1)$. Calcular a) la matriz respecto de las canónicas; b) las ecuaciones de $\operatorname{Im}(f)$.**

a) $f(1,0)=\tfrac16\big(f(2,-1)+f(4,1)\big)=\left(\tfrac12,-\tfrac13,\tfrac13,\tfrac23\right)$; $f(0,1)=\tfrac13\big(-2f(2,-1)+f(4,1)\big)=\left(0,-\tfrac23,\tfrac53,-\tfrac53\right)$.
$$A=M(f,B_c,B'_c)=\begin{pmatrix}1/2&0\\-1/3&-2/3\\1/3&5/3\\2/3&-5/3\end{pmatrix}$$
También: $M(f,B_c,B'_c)=M(f,B,B'_c)\,M(B_c,B)$ con $B=\{(2,-1),(4,1)\}$, $M(f,B,B'_c)=\begin{pmatrix}1&2\\0&-2\\-1&3\\3&1\end{pmatrix}$,

#### Página 5

$M(B_c,B)=M(B,B_c)^{-1}=\begin{pmatrix}2&4\\-1&1\end{pmatrix}^{-1}=\begin{pmatrix}1/6&-2/3\\1/6&1/3\end{pmatrix}$, y el producto da la misma $A$.

b) $\operatorname{Im}(f)=L((1,0,-1,3),(2,-2,3,1))$; paramétricas $y_1=\lambda+2\mu,\ y_2=-2\mu,\ y_3=-\lambda+3\mu,\ y_4=3\lambda+\mu$. Imponiendo rango 2 a $\begin{pmatrix}1&0&-1&3\\2&-2&3&1\\y_1&y_2&y_3&y_4\end{pmatrix}$:
$$\operatorname{Im}(f)\equiv\begin{cases}-2y_1-5y_2-2y_3=0\\6y_1+5y_2-2y_4=0\end{cases}$$

**10. Sea $f:\mathbb{R}^3\to\mathbb{R}^2$ con $f(1,0,1)=(0,1)$, $f(0,0,-1)=(1,1)$, $f(2,1,1)=(1,0)$.** a) Matriz respecto de las canónicas. b) Matriz respecto de $B_1=\{(1,0,1),(0,0,-1),(2,1,1)\}$ y $B_2=\{(0,1),(1,0)\}$. c) Ecuaciones y dimensión de $\operatorname{Ker}(f)$ e $\operatorname{Im}(f)$.

#### Página 6

a) $f(1,0,0)=f(1,0,1)+f(0,0,-1)=(1,2)$; $f(0,1,0)=f(2,1,1)-2f(1,0,1)-f(0,0,-1)=(0,-3)$; $f(0,0,1)=-f(0,0,-1)=(-1,-1)$.
$$A=\begin{pmatrix}1&0&-1\\2&-3&-1\end{pmatrix}$$
b) $M(f,B_1,B_2)=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$.
c) $\operatorname{Im}(f)=L((1,2),(0,-3),(-1,-1))=\mathbb{R}^2$, $\dim=2$; $\dim\operatorname{Ker}(f)=3-2=1$, con $\operatorname{Ker}(f)\equiv\{x_1-x_3=0,\ 2x_1-3x_2-x_3=0\}$.

#### Página 7

**13. Sean $B_1=\{(1,1,0),(1,0,1),(0,1,1)\}$ y $B'_1=\{(1,-1,1),(-1,1,1),(1,1,-1)\}$ bases de $\mathbb{R}^3$, $B_c$ la canónica y $B_2=\{(1,0,1,1),(0,1,1,1),(1,1,0,1),(1,1,1,0)\}$ base de $\mathbb{R}^4$.**
a) ¿Qué vector tiene coordenadas $(1,2,-1)$ en $B_1$ y cuáles son sus coordenadas en $B'_1$?
b) Matrices de cambio de base de $B_1$ a $B'_1$ y de $B_c$ a $B_2$.
c) Con $f(1,1,0)=(1,1,0,0)$, $f(1,0,1)=(1,0,1,0)$, $f(0,1,1)=(0,0,1,1)$, hallar la matriz de $f$ respecto de $B_1,B_c$; $B_1,B_2$; $B'_1,B_c$; $B'_1,B_2$.

a) $\bar x=1(1,1,0)+2(1,0,1)-1(0,1,1)=(3,0,1)$. $X_{B'_1}=M(B'_c,B'_1)X_{B'_c}$ con $M(B'_1,B'_c)^{-1}=\begin{pmatrix}1&-1&1\\-1&1&1\\1&1&-1\end{pmatrix}^{-1}=\begin{pmatrix}1/2&0&1/2\\0&1/2&1/2\\1/2&1/2&0\end{pmatrix}$, luego $X_{B'_1}=(2,\tfrac12,\tfrac32)$.

#### Página 8

b) $P=M(B_1,B'_1)=M(B'_c,B'_1)M(B_1,B'_c)=\begin{pmatrix}1/2&0&1/2\\0&1/2&1/2\\1/2&1/2&0\end{pmatrix}\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}=\begin{pmatrix}1/2&1&1/2\\1/2&1/2&1\\1&1/2&1/2\end{pmatrix}$.
$Q=M(B_c,B_2)=M(B_2,B_c)^{-1}=\begin{pmatrix}1&0&1&1\\0&1&1&1\\1&1&0&1\\1&1&1&0\end{pmatrix}^{-1}=\begin{pmatrix}1/3&-2/3&1/3&1/3\\-2/3&1/3&1/3&1/3\\1/3&1/3&-2/3&1/3\\1/3&1/3&1/3&-2/3\end{pmatrix}$.

c) $F=M(f,B_1,B_c)=\begin{pmatrix}1&1&0\\1&0&0\\0&1&1\\0&0&1\end{pmatrix}$.
$G=M(f,B_1,B_2)=QF=\begin{pmatrix}-1/3&2/3&2/3\\-1/3&-1/3&2/3\\2/3&-1/3&-1/3\\2/3&2/3&-1/3\end{pmatrix}$.
$H=M(f,B'_1,B_c)=FP^{-1}=\begin{pmatrix}1&-1&1\\-1/2&-1/2&3/2\\1&1&-1\\-1/2&3/2&-1/2\end{pmatrix}$.

#### Página 9

$I=M(f,B'_1,B_2)=QH=\begin{pmatrix}5/6&5/6&-7/6\\-2/3&4/3&-2/3\\-2/3&-2/3&4/3\\5/6&-7/6&5/6\end{pmatrix}$.

**14. Sea $f:M_{2\times2}(\mathbb{R})\to\mathbb{R}^3$, $f\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a,\ a+b+c,\ 0)$.** a) Probar que es lineal y hallar su matriz respecto de las canónicas. b) Bases, dimensión y ecuaciones implícitas de $\operatorname{Ker}(f)$ e $\operatorname{Im}(f)$.

a) Linealidad rutinaria. $F=\begin{pmatrix}1&0&0&0\\1&1&1&0\\0&0&0&0\end{pmatrix}$.
b) $\dim\operatorname{Im}(f)=r(F)=2$; $\dim\operatorname{Ker}(f)=4-2=2$. Base de la imagen (columnas de $F$): $\{(1,1,0),(0,1,0)\}$; ecuación implícita $\operatorname{Im}(f)\equiv\{y_3=0\}$.
Núcleo: $a=0,\ a+b+c=0$ ⇒ $a=0,\ b=-\lambda,\ c=\lambda,\ d=\mu$ ⇒ $\begin{pmatrix}a&b\\c&d\end{pmatrix}=\lambda\begin{pmatrix}0&-1\\1&0\end{pmatrix}+\mu\begin{pmatrix}0&0\\0&1\end{pmatrix}$. Base de $\operatorname{Ker}f=\left\{\begin{pmatrix}0&-1\\1&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right\}$.


## Tema 5 · Autovalores y diagonalización

*Fuente: `GRUPO B/EJERCICIOS DE REPASO/Ejercicios de repaso Tema 5 Autovalores y diagonalizacion.pdf`*

#### Páginas 1–5 · Ejercicio 1

**1. Obtener los autovalores y bases de los subespacios propios de:**
$\begin{pmatrix}10&-9\\4&-2\end{pmatrix}$, $\begin{pmatrix}0&3\\4&0\end{pmatrix}$, $\begin{pmatrix}0&0\\0&0\end{pmatrix}$, $\begin{pmatrix}1&0\\0&1\end{pmatrix}$, $\begin{pmatrix}4&0&1\\-2&1&0\\-2&0&1\end{pmatrix}$, $\begin{pmatrix}-1&0&1\\-1&3&0\\-4&13&-1\end{pmatrix}$, $\begin{pmatrix}5&0&1\\1&1&0\\-7&1&0\end{pmatrix}$.

- $A=\begin{pmatrix}10&-9\\4&-2\end{pmatrix}$: $p_A(\lambda)=(10-\lambda)(-2-\lambda)+36=\lambda^2-8\lambda+16$ → único autovalor $\lambda_1=4$, m.a. 2. $(A-4I)=\begin{pmatrix}6&-9\\4&-6\end{pmatrix}$ ⇒ $2x-3y=0$ ⇒ $V(4)=\operatorname{lin}\{(3,2)\}$. Comprobación: $A(3,2)^T=(12,8)^T=4(3,2)^T$.
- $A=\begin{pmatrix}0&3\\4&0\end{pmatrix}$: $p_A=\lambda^2-12$ ⇒ $\lambda_{1,2}=\pm2\sqrt3$ (m.a. 1 cada uno). $V(2\sqrt3)=\operatorname{lin}\{(\sqrt3,2)\}$, $V(-2\sqrt3)=\operatorname{lin}\{(-\sqrt3,2)\}$; se verifica $Av_i=\lambda_iv_i$.
- Matriz nula: único autovalor 0 con m.a. 2; $V(0)=\mathbb{R}^2$, base canónica.
- $I_2$: único autovalor 1 con m.a. 2; $I-1\cdot I=0$ ⇒ $V(1)=\mathbb{R}^2$, base $\{(1,0),(0,1)\}$.
- $A=\begin{pmatrix}4&0&1\\-2&1&0\\-2&0&1\end{pmatrix}$: $p_A=(1-\lambda)[(4-\lambda)(1-\lambda)+2]=(1-\lambda)(2-\lambda)(3-\lambda)$ ⇒ $\lambda=1,2,3$ (m.a. 1). $V(1)=\operatorname{lin}\{(0,1,0)\}$; $V(2)=\operatorname{lin}\{(1,-2,-2)\}$ *(el original escribe (1,−2,−1); de $2x+z=0$ sale $z=-2t$)*; $V(3)=\operatorname{lin}\{(-1,1,1)\}$.
- $A=\begin{pmatrix}-1&0&1\\-1&3&0\\-4&13&-1\end{pmatrix}$: $p_A=-\lambda^3+\lambda^2+\lambda+2=-(\lambda-2)(\lambda^2+\lambda+1)$ ⇒ único autovalor real $\lambda=2$ (las otras raíces son complejas $\frac{-1\pm\sqrt3 i}{2}$). Por Gauss, $x-\tfrac13z=0,\ y-\tfrac13z=0$ ⇒ $V(2)=\operatorname{lin}\{(1,1,3)\}$; $A(1,1,3)^T=(2,2,6)^T$.
- $A=\begin{pmatrix}5&0&1\\1&1&0\\-7&1&0\end{pmatrix}$: $p_A=-\lambda^3+6\lambda^2-12\lambda+8=-(\lambda-2)^3$ ⇒ $\lambda=2$ con m.a. 3. $(A-2I)=\begin{pmatrix}3&0&1\\1&-1&0\\-7&1&-2\end{pmatrix}$, por Gauss $x+\tfrac13z=0,\ y+\tfrac13z=0$ ⇒ $V(2)=\operatorname{lin}\{(-1,-1,3)\}$; $A(-1,-1,3)^T=(-2,-2,6)^T=2(-1,-1,3)^T$.

#### Páginas 5–6 · Ejercicio 4 (diagonalizabilidad)

**4. Determinar cuáles son diagonalizables:** $\begin{pmatrix}2&0\\1&2\end{pmatrix}$, $\begin{pmatrix}2&-3\\1&-1\end{pmatrix}$, $\begin{pmatrix}3&0&0\\0&2&0\\0&1&2\end{pmatrix}$, $\begin{pmatrix}4&0&0&0\\1&-1&0&0\\0&1&2&0\\0&1&4&3\end{pmatrix}$, $\begin{pmatrix}2&-1&0&1\\0&2&1&-1\\0&0&3&2\\0&0&0&3\end{pmatrix}$.

- $\begin{pmatrix}2&0\\1&2\end{pmatrix}$: $\lambda=2$, m.a. $m_1=2$. $\mu_1=\dim V(\lambda_1)=2-\operatorname{rg}(A-2I)=2-1=1\neq2$ ⇒ **no diagonalizable**. *Otra forma:* si lo fuera, $D=\lambda_1I$ y $A=P\lambda_1IP^{-1}=\lambda_1I$, pero $A\neq2I$. **Nota:** si $A\in\mathcal M_n$ tiene un único autovalor con m.a. $n$, es diagonalizable ⇔ $A=\lambda_1I$.
- $\begin{pmatrix}2&-3\\1&-1\end{pmatrix}$: $p_A=\lambda^2-\lambda+1$, raíces complejas $\frac{1\pm\sqrt3i}{2}$ ⇒ **no diagonalizable en $\mathbb{R}$**.
- $\begin{pmatrix}3&0&0\\0&2&0\\0&1&2\end{pmatrix}$ (triangular inferior): autovalores 3 (m.a. 1) y 2 (m.a. 2). Se cumple $1\le\mu\le m$. $\operatorname{rg}(A-2I)=2$ ⇒ $\mu_2=3-2=1\neq2$ ⇒ **no diagonalizable**. *(El original escribe "λ₁ = 1" para el primer autovalor; por la diagonal es 3.)*
- $\begin{pmatrix}4&0&0&0\\1&-1&0&0\\0&1&2&0\\0&1&4&3\end{pmatrix}$: autovalores 4, −1, 2, 3, todos distintos ⇒ **diagonalizable**.
- $\begin{pmatrix}2&-1&0&1\\0&2&1&-1\\0&0&3&2\\0&0&0&3\end{pmatrix}$: autovalores 2 (m.a. 2) y 3 (m.a. 2). $\operatorname{rg}(2I-A)=3$ ⇒ $\dim V(2)=1\neq2$ ⇒ **no diagonalizable**.

#### Página 7 · Ejercicios 6, 7 y 9

**6. Matriz 2×2 con autovalores 1 y 2, $V(1)=\operatorname{lin}\{(1,1)\}$, $V(2)=\operatorname{lin}\{(1,0)\}$.**
$A=PDP^{-1}$ con $D=\begin{pmatrix}2&0\\0&1\end{pmatrix}$, $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $P^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$ ⇒ $A=\begin{pmatrix}2&-1\\0&1\end{pmatrix}$. Comprobación: $A(1,0)^T=2(1,0)^T$, $A(1,1)^T=(1,1)^T$.

**7. Matriz 3×3 con autovalores −1 y 2, $V(2)=\operatorname{lin}\{(1,1,-1)\}$, $V(-1)=\{x-z=0\}$.**
$V(-1)=\operatorname{lin}\{(0,1,0),(1,0,1)\}$. $P=\begin{pmatrix}0&1&1\\1&0&1\\0&1&-1\end{pmatrix}$, $D=\operatorname{diag}(-1,-1,2)$,
$$A=PDP^{-1}=\begin{pmatrix}\tfrac12&0&-\tfrac32\\\tfrac32&-1&-\tfrac32\\-\tfrac32&0&\tfrac12\end{pmatrix}$$

**9. Encontrar una matriz de paso ortogonal que diagonalice ortogonalmente:** $\begin{pmatrix}6&-2\\-2&3\end{pmatrix}$, $\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}$, $\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$, $\begin{pmatrix}3&2&4\\2&0&2\\4&2&3\end{pmatrix}$, $\begin{pmatrix}5&4&2\\4&5&2\\2&2&2\end{pmatrix}$. Todas son simétricas, luego diagonalizables ortogonalmente.

- $\begin{pmatrix}6&-2\\-2&3\end{pmatrix}$: $p_A=\lambda^2-9\lambda+14=(\lambda-2)(\lambda-7)$. $V(2)=\operatorname{lin}\{(1,2)\}$, $V(7)=\operatorname{lin}\{(-2,1)\}$ (ortogonales: $(1,2)\cdot(-2,1)=0$).

#### Página 8

Normalizando: $w_1=\left(\tfrac1{\sqrt5},\tfrac2{\sqrt5}\right)$, $w_2=\left(\tfrac{-2}{\sqrt5},\tfrac1{\sqrt5}\right)$, $Q=(w_1|w_2)$ y $Q^{-1}AQ=Q^tAQ=\begin{pmatrix}2&0\\0&7\end{pmatrix}$.

- $\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}$: $|\lambda I-A|=\lambda^2(\lambda-2)$ ⇒ $\lambda=0$ (m.a. 2), $\lambda=2$ (m.a. 1). $V(0)=\operatorname{lin}\{(-1,1,0),(0,0,1)\}$, $V(2)=\operatorname{lin}\{(1,1,0)\}$. Ya son ortogonales; normalizando:
$P=\begin{pmatrix}-\tfrac1{\sqrt2}&0&\tfrac1{\sqrt2}\\\tfrac1{\sqrt2}&0&\tfrac1{\sqrt2}\\0&1&0\end{pmatrix}$, $D=\operatorname{diag}(0,0,2)$.

#### Página 9

- $\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$: $p_A=-\lambda^3+6\lambda^2-9\lambda=-\lambda(\lambda-3)^2$ ⇒ $\lambda=0$ (m.a. 1), $\lambda=3$ (m.a. 2). $V(0)=\operatorname{lin}\{(1,1,1)\}$ → $\left(\tfrac1{\sqrt3},\tfrac1{\sqrt3},\tfrac1{\sqrt3}\right)$. Para $V(3)$, Gram-Schmidt sobre $\{u_1=(1,0,-1),u_2=(0,1,-1)\}$: $w_1=\left(\tfrac1{\sqrt2},0,\tfrac{-1}{\sqrt2}\right)$; $v_2=u_2-(u_2\cdot w_1)w_1=\left(-\tfrac12,1,-\tfrac12\right)$, $w_2=\left(\tfrac{-1}{\sqrt6},\tfrac2{\sqrt6},\tfrac{-1}{\sqrt6}\right)$.
$$Q=\begin{pmatrix}\tfrac1{\sqrt3}&\tfrac1{\sqrt2}&\tfrac{-1}{\sqrt6}\\\tfrac1{\sqrt3}&0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt3}&\tfrac{-1}{\sqrt2}&\tfrac{-1}{\sqrt6}\end{pmatrix},\quad D=\operatorname{diag}(0,3,3)$$

#### Página 10

- $\begin{pmatrix}5&4&2\\4&5&2\\2&2&2\end{pmatrix}$: $|\lambda I-A|=\lambda^3-12\lambda^2+21\lambda-10=(\lambda-1)^2(\lambda-10)$ ⇒ $\lambda=1$ (m.a. 2), $\lambda=10$ (m.a. 1). $V(1)$: $x+y+\tfrac12z=0$ ⇒ $\operatorname{lin}\{(-1,1,0),(-1,0,2)\}$; $V(10)=\operatorname{lin}\{(2,2,1)\}$. $P=\begin{pmatrix}-1&-1&2\\1&0&2\\0&2&1\end{pmatrix}$ no es ortogonal; Gram-Schmidt en $V(1)$: $v_1=(-1,1,0)$, $v_2=(-1,0,2)-\tfrac12(-1,1,0)=\left(-\tfrac12,-\tfrac12,2\right)\sim(-1,-1,4)$. Base ortogonal $\{(2,2,1),(-1,1,0),(-1,-1,4)\}$; normalizando,
$$P=\begin{pmatrix}-\tfrac1{\sqrt2}&-\tfrac1{\sqrt{18}}&\tfrac23\\\tfrac1{\sqrt2}&-\tfrac1{\sqrt{18}}&\tfrac23\\0&\tfrac4{\sqrt{18}}&\tfrac13\end{pmatrix}$$
*(El original pone $\tfrac23$ en la última entrada; normalizando $(2,2,1)$ sale $\tfrac13$.)*

**10. Los autovalores de una matriz simétrica $A$ de orden 3 son 1, −2 y 3, con $V(1)=\operatorname{lin}\{(1,1,-1)\}$ y $V(-2)=\operatorname{lin}\{(0,1,1)\}$. Obtener una base de $V(3)$ y la matriz $A$.**
Al ser simétrica, $V(3)\perp V(1)$ y $V(3)\perp V(-2)$: $x+y-z=0,\ y+z=0$ ⇒ $V(3)=\operatorname{lin}\{(2,-1,1)\}$.

#### Página 11

$A=PDP^T$ con $P=\begin{pmatrix}\tfrac1{\sqrt3}&0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt3}&\tfrac1{\sqrt2}&\tfrac{-1}{\sqrt6}\\\tfrac{-1}{\sqrt3}&\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix}$, $D=\operatorname{diag}(1,-2,3)$, resultando (según el original)
$$A=\begin{pmatrix}\tfrac{14}{6}&-\tfrac46&\tfrac46\\-\tfrac46&-\tfrac16&-\tfrac{11}6\\\tfrac46&-\tfrac{11}6&-\tfrac16\end{pmatrix}$$
