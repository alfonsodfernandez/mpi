# Teoría: transformaciones (aplicaciones) lineales

Definición, linealidad, núcleo, imagen, matriz asociada, invertibilidad e isomorfismos.

**Contenido de este archivo:**
- Pizarra Grupo A · Transformaciones lineales
- Live Script: transformaciones geométricas
- Live Script: transformaciones invertibles
- Live Script: 14 problemas resueltos de aplicaciones lineales


## Pizarra Grupo A · Transformaciones lineales

*Fuente: `GRUPO A/TEMA 5 - Transformaciones lineales/MPI1 - Tema 5 - Transformaciones lineales - definición - PIZARRA.pdf`*

#### Transformaciones (o aplicaciones) lineales

##### Definición de transformación (o aplicación)
Una transformación (o aplicación) entre dos e.v. $V$ y $W$ es una regla que relaciona **cada** vector del primer e.v., $v\in V$, con **un** vector del segundo, $T(v)\in W$. (Diagrama: de cada elemento de $V$ sale una sola flecha. Primer conjunto → segundo conjunto; conjunto de entrada → conjunto de salida/llegada. $V$ es el dominio de la función; un subconjunto de $W$ es el recorrido.)

Nomenclatura: $f:\mathbb{R}^3\to\mathbb{R}^2$, $(x,y,z)\mapsto f(x,y,z)=(x+y,\,2z)$; o bien $T:\mathbb{R}^3\to\mathbb{R}^2$, $T\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}x+y\\2z\end{pmatrix}$.

##### Definición de transformación lineal
$T:V\to W$ es una **transformación lineal** de $V$ en $W$ si, para $u,v\in V$ y $\alpha\in\mathbb{R}$:
- $T(u+v)=T(u)+T(v)$
- $T(\alpha v)=\alpha T(v)$

**Ejemplo:** demostrar si $T\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}x+y\\x-y\\3y\end{pmatrix}$ es lineal.
- Con $u=(x_1,y_1)$, $v=(x_2,y_2)$: $T(u+v)=\begin{pmatrix}x_1+x_2+y_1+y_2\\x_1+x_2-(y_1+y_2)\\3(y_1+y_2)\end{pmatrix}=\begin{pmatrix}x_1+y_1\\x_1-y_1\\3y_1\end{pmatrix}+\begin{pmatrix}x_2+y_2\\x_2-y_2\\3y_2\end{pmatrix}=T(u)+T(v)$ ✓
- $T(\alpha u)=\begin{pmatrix}\alpha x+\alpha y\\\alpha x-\alpha y\\3\alpha y\end{pmatrix}=\alpha\begin{pmatrix}x+y\\x-y\\3y\end{pmatrix}=\alpha T(u)$ ✓ ⇒ es lineal.

- **Transformación cero:** $T(v)=0$. **Transformación identidad:** $I(v)=v$.

##### Propiedades de las transformaciones lineales
- $T\left(\sum\alpha_iv_i\right)=\sum\alpha_iT(v_i)$, es decir, $T(\alpha_1v_1+\dots+\alpha_nv_n)=\alpha_1T(v_1)+\dots+\alpha_nT(v_n)$.
- $T(0_V)=0_W$.
- Si $S$ es un s.e.v. de $V$ ⇒ $T(S)$ es un s.e.v. de $W$.
- Basta con conocer la imagen de los vectores de la base de $V$ mediante $T$ para determinar la imagen de cualquier vector de $V$.
  Ejemplo: $T:\mathbb{R}^3\to\mathbb{R}^2$ con $T(1,0,0)=(2,3)$, $T(0,1,0)=(-1,4)$, $T(0,0,1)=(5,-3)$. Entonces $T(3,-4,5)=3T(e_1)-4T(e_2)+5T(e_3)=3(2,3)-4(-1,4)+5(5,-3)=(35,-22)$.


## Live Script: transformaciones geométricas

*Fuente: `AP_LIN_00_R01.mlx`*

###  [Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

### APLICACIONES LINEALES - Transformaciones geométricas

- Table of Contents

- Expansiones ·     Expansión sobre el eje x ·     Expansión sobre el eje y · Compresiones ·     Compresión a lo largo del eje x ·     Compresión a lo largo del eje y · Reflexiones ·     Respecto del eje x ·     Respecto del eje y ·     Respecto del origen ·     Respecto de la bisectriz del primer cuadrante ·     Respecto de la bisectriz del cuarto cuadrante · Cizalladuras ·     Según el eje x ·     Según el eje y · Rotaciones · Transformación lineal genérica

#### Expansiones

Expansión sobre el eje x

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,10])
grid on
xlabel('x')
ylabel('y')
```

Expansión 2x:

```matlab
hold on
c = 2;
T = [c 0;0 1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
2  0
0  1
P1 =
0  0  6  6  0
0  2  2  0  0
[figura]
```

Volver al índice

Expansión sobre el eje y

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,10])
grid on
xlabel('x')
ylabel('y')
```

Expansión 2y:

```matlab
hold on
c = 2;
T = [1 0;0 2]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
1  0
0  2
[figura]
```

Volver al índice

#### Compresiones

Compresión a lo largo del eje x

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,10])
grid on
xlabel('x')
ylabel('y')
```

Compresión 2x:

```matlab
hold on
c = 0.5;
T = [c 0;0 1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
0.5000  0
0  1.0000
[figura]
```

Volver al índice

Compresión a lo largo del eje y

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,10])
grid on
xlabel('x')
ylabel('y')
```

Compresión 2x:

```matlab
hold on
c = 0.5;
T = [1 0;0 c]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
1.0000  0
0  0.5000
[figura]
```

Volver al índice

#### Reflexiones

Respecto del eje x

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [4,0;4,2;6,2;6,0;4,0]';
plot(P(1,:),P(2,:),'b')
axis([-10,10,-10,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
T = [1 0;0 -1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
1  0
0  -1
[figura]
```

Volver al índice

Respecto del eje y

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [4,0;4,2;6,2;6,0;4,0]';
plot(P(1,:),P(2,:),'b')
axis([-10,10,-10,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
T = [-1 0;0 1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
-1  0
0  1
[figura]
```

Volver al índice

Respecto del origen

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [4,0;4,2;6,2;6,0;4,0]';
plot(P(1,:),P(2,:),'b')
axis([-10,10,-10,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
T = [-1 0;0 -1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
-1  0
0  -1
[figura]
```

Volver al índice

Respecto de la bisectriz del primer cuadrante

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [4,0;4,2;6,2;6,0;4,0]';
plot(P(1,:),P(2,:),'b')
axis([-10,10,-10,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
f = @(x) x;
T = [0 1;1 0]
fplot(f,'--k')
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
0  1
1  0
[figura]
```

Volver al índice

Respecto de la bisectriz del cuarto cuadrante

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [4,0;4,2;6,2;6,0;4,0]';
plot(P(1,:),P(2,:),'b')
axis([-10,10,-10,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
f = @(x) -x;
T = [0 -1;-1 0]
fplot(f,'--k')
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
0  -1
-1  0
[figura]
```

Volver al índice

#### Cizalladuras

Según el eje x

$$T\left\lbrack \begin{array}{c}
x\\
y
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
x+\textrm{cy}\\
y
\end{array}\right\rbrack$$

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,5])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
c = 2;
T = [1 c;0 1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
1  2
0  1
[figura]
```

Volver al índice

Según el eje y

$$T\left\lbrack \begin{array}{c}
x\\
y
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
x\\
y+\textrm{cx}
\end{array}\right\rbrack$$

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis([0,10,0,5])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

Reflexión

```matlab
hold on
c = 0.5;
T = [1 0;c 1]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
hold off
legend('original','transformada','Location','best')
```

**Salida:**
```text
T =
1.0000  0
0.5000  1.0000
[figura]
```

Volver al índice

#### Rotaciones

[Imagen: Figura: (a) punto P(x, y) que forma ángulo θ con el eje x, rotado un ángulo φ hasta P'(x', y'); (b) Rotación: vector u y su imagen f(u) girada φ.]

$$f\left(\left\lbrack \begin{array}{c}
x\\
y
\end{array}\right\rbrack \right)=\left\lbrack \begin{array}{cc}
\cos \;\phi  & -\textrm{sen}\;\phi \\
\textrm{sen}\;\phi  & \cos \;\phi
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
x\\
y
\end{array}\right\rbrack$$

Dibujo de la figura

```matlab
clear; clc;
fig = figure;
P = [0,0;0,2;3,2;3,0;0,0]';
plot(P(1,:),P(2,:),'b')
axis equal
grid on
xlabel('x')
ylabel('y')
```

Rotación de 45º

```matlab
hold on
phi = 45;
T = [cosd(phi) -sind(phi);sind(phi) cosd(phi)]
P1 = T*P;
plot(P1(1,:),P1(2,:),':r')
```

**Salida:**
```text
T =
0.7071  -0.7071
0.7071  0.7071
```

Rotación de 30º

```matlab
phi = 30;
T = [cosd(phi) -sind(phi);sind(phi) cosd(phi)]
P1 = T*P;
plot(P1(1,:),P1(2,:),':k')
hold off
legend('original','transformada 45º','transformada 30º','Location','best')
```

**Salida:**
```text
T =
0.8660  -0.5000
0.5000  0.8660
[figura]
```

Volver al índice

#### Transformación lineal genérica

Supongamos que tenemos dos figuras y queremos hallar la transformación lineal que permite pasar de una a otra.

Dibujo de las figuras

```matlab
clear; clc;
fig = figure;
P = [1,1;0.5,3]';
plot(P(1,:),P(2,:),'b')
for i = 1:2
    text(P(1,i),P(2,i)+0.1,['(' num2str(P(1,i)), ',', num2str(P(2,i)), ')' ])
end
hold on
P1 = [4,2.5;5,4.5]';
plot(P1(1,:),P1(2,:),'r')
for i = 1:2
    text(P1(1,i),P1(2,i)+0.1,['(' num2str(P1(1,i)), ',', num2str(P1(2,i)), ')' ])
end

for i = 1:2
    plot([P(1,i) P1(1,i)],[P(2,i) P1(2,i)],':k')
end

axis([0,10,0,5])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')
```

**Salida:**
```text
[figura]
```

La transformación lineal ha de cambiar la matriz de puntos del segmento azul:

```matlab
P(:,1:end-1)
```

**Salida:**
```text
ans =
```

A la matriz de puntos del segmento rojo:

```matlab
P1(:,1:end-1)
```

**Salida:**
```text
ans =
4.0000
2.5000
```

Es decir: $T\cdot P=\textrm{P1}$

Sea $T=\left\lbrack \begin{array}{cc}
a & b\\
c & d
\end{array}\right\rbrack$

```matlab
syms a b c d
T = [a b;c d]
ec = T*P == P1

[A b] = equationsToMatrix(ec)
GJ = rref([A b])

sol = solve(ec)
T = [sol.a sol.b;sol.c sol.d]
```

**Salida:**
```text
T = ([a, b; c, d])
ec = ([a+b=4, (a)/(2)+3⁢b=5; c+d=(5)/(2), (c)/(2)+3⁢d=(9)/(2)])
A = ([1, 1, 0, 0; 0, 0, 1, 1; (1)/(2), 3, 0, 0; 0, 0, (1)/(2), 3])
b = ([4; (5)/(2); 5; (9)/(2)])
GJ = ([1, 0, 0, 0, (14)/(5); 0, 1, 0, 0, (6)/(5); 0, 0, 1, 0, (6)/(5); 0, 0, 0, 1, (13)/(10)])
sol = struct with fields:
a: 14/5
b: 6/5
c: 6/5
d: 13/10
T = ([(14)/(5), (6)/(5); (6)/(5), (13)/(10)])
```

La aplicamos a otro vector:

Dibujo de las figuras

```matlab
fig = figure;
P = [0.5,0.5;1.25,4]';
plot(P(1,:),P(2,:),'b')
for i = 1:2
    text(P(1,i),P(2,i)+0.1,['(' num2str(P(1,i)), ',', num2str(P(2,i)), ')' ])
end

axis([0,10,0,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')

hold on
P1 = double(T*P);
plot(P1(1,:),P1(2,:),'r')
for i = 1:2
    text(P1(1,i),P1(2,i)+0.1,['(' num2str(P1(1,i)), ',', num2str(P1(2,i)), ')' ])
end

for i = 1:2
    plot([P(1,i) P1(1,i)],[P(2,i) P1(2,i)],':k')
end
```

**Salida:**
```text
[figura]
```

Y ahora a una figura geométrica:

La aplicamos a otro vector:

Dibujo de las figuras

```matlab
fig = figure;
P = [0.5,0.5;1.25,4;3,3;4,2;2,2.5;0.5,0.5]';
plot(P(1,:),P(2,:),'b')
for i = 1:length(P)
    text(P(1,i),P(2,i)+0.1,['(' num2str(P(1,i)), ',', num2str(P(2,i)), ')' ])
end

axis([0,20,0,10])
xline(0)
yline(0)
grid on
xlabel('x')
ylabel('y')

hold on
P1 = double(T*P);
plot(P1(1,:),P1(2,:),'r')
for i = 1:length(P1)
    text(P1(1,i),P1(2,i)+0.1,['(' num2str(P1(1,i)), ',', num2str(P1(2,i)), ')' ])
end

for i = 1:2
    plot([P(1,i) P1(1,i)],[P(2,i) P1(2,i)],':k')
end
```

**Salida:**
```text
[figura]
```

Volver al índice

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Live Script: transformaciones invertibles

*Fuente: `AP_LIN_01_R00.mlx`*

###  [Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

### APLICACIONES LINEALES - Ejemplos

- Table of Contents

- Problema 1 - Transformaciones invertibles ·     Solución · Problema 2 - Transformaciones invertibles ·     Solución

#### Problema 1 - Transformaciones invertibles

Muestre que $T:\Re^3 \to \Re^3 \;$ dada por $T\left\lbrack \begin{array}{c}
x\\
y\\
z
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
x+y\\
y+z\\
x+z
\end{array}\right\rbrack$es una transformación lineal invertible. Además, halle $T^{-1}$.

Solución

Hallamos la transformación de la base canónica:

```matlab
clear; clc;
syms a b c d e f g h i x y z
u1 = [1;0;0]
u2 = [0;1;0]
u3 = [0;0;1]
T = [ a b c;d e f;g h i]
Tu1 = [u1(1)+u1(2);u1(2)+u1(3);u1(1)+u1(3)]
Tu2 = [u2(1)+u2(2);u2(2)+u2(3);u2(1)+u2(3)]
Tu3 = [u3(1)+u3(2);u3(2)+u3(3);u3(1)+u3(3)]

U = [u1 u2 u3]
TU = [Tu1 Tu2 Tu3]
ec = T*U == TU
sol = solve(ec)
T = double([sol.a sol.b sol.c;sol.d sol.e sol.f;sol.g sol.h sol.i])
```

**Salida:**
```text
u1 =
u2 =
u3 =
T = ([a, b, c; d, e, f; g, h, i])
Tu1 =
Tu2 =
Tu3 =
U =
1  0  0
0  1  0
0  0  1
TU =
1  1  0
0  1  1
1  0  1
ec = ([a=1, b=1, c=0; d=0, e=1, f=1; g=1, h=0, i=1])
sol = struct with fields:
a: 1
b: 1
c: 0
d: 0
e: 1
f: 1
g: 1
h: 0
i: 1
T =
1  1  0
0  1  1
1  0  1
```

Comprobamos

```matlab
X = [x;y;z]
T*X
```

**Salida:**
```text
X = ([x; y; z])
ans = ([x+y; y+z; x+z])
```

Invertimos la matriz:

```matlab
Ti = inv(T)
```

**Salida:**
```text
Ti =
0.5000  -0.5000  0.5000
0.5000  0.5000  -0.5000
-0.5000  0.5000  0.5000
```

Comprobamos:

```matlab
TX = [x+y;y+z;x+z]
Ti*TX
```

**Salida:**
```text
TX = ([x+y; y+z; x+z])
ans = ([x; y; z])
```

Volver al índice

#### Problema 2 - Transformaciones invertibles

Sea $S:\Re^3 \to \Re^3 \;$ dada por $S\left\lbrack \begin{array}{c}
x\\
y\\
z
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
x+y+2z\\
x+y+2z\\
x+z
\end{array}\right\rbrack$¿Es S una transformación lineal invertible. Además, halle $S^{-1}$ si se atreve.

Solución

Va a salir que no es invertible, dado que las dos primeras coordenadas del vector imagen son idénticas, por lo que la matriz de la transformación saldrá singular y por tanto, no tendrá inversa.

Hallamos la transformación de la base canónica:

```matlab
clear; clc;
syms a b c d e f g h i x y z
u1 = [1;0;0]
u2 = [0;1;0]
u3 = [0;0;1]
S = [ a b c;d e f;g h i]
Su1 = [u1(1)+u1(2)+2*u1(3);u1(1)+u1(2)+2*u1(3);u1(1)+u1(3)]
Su2 = [u2(1)+u2(2)+2*u2(3);u2(1)+u2(2)+2*u2(3);u2(1)+u2(3)]
Su3 = [u3(1)+u3(2)+2*u3(3);u3(1)+u3(2)+2*u3(3);u3(1)+u3(3)]

U = [u1 u2 u3]
SU = [Su1 Su2 Su3]
ec = S*U == SU
sol = solve(ec)
S = double([sol.a sol.b sol.c;sol.d sol.e sol.f;sol.g sol.h sol.i])
X = [x;y;z]
S*X
```

**Salida:**
```text
u1 =
u2 =
u3 =
S = ([a, b, c; d, e, f; g, h, i])
Su1 =
Su2 =
Su3 =
U =
1  0  0
0  1  0
0  0  1
SU =
1  1  2
1  1  2
1  0  1
ec = ([a=1, b=1, c=2; d=1, e=1, f=2; g=1, h=0, i=1])
sol = struct with fields:
a: 1
b: 1
c: 2
d: 1
e: 1
f: 2
g: 1
h: 0
i: 1
S =
1  1  2
1  1  2
1  0  1
X = ([x; y; z])
ans = ([x+y+2⁢z; x+y+2⁢z; x+z])
```

Comprobamos

```matlab
X = [x;y;z]
S*X
```

**Salida:**
```text
X = ([x; y; z])
ans = ([x+y+2⁢z; x+y+2⁢z; x+z])
```

Invertimos la matriz:

```matlab
Si = inv(S)
```

**Salida:**
```text
WARNING: Warning: Matrix is singular to working precision.
Si =
Inf  Inf  Inf
Inf  Inf  Inf
Inf  Inf  Inf
```

Comprobamos:

```matlab
SX = [x+y+2*z;x+y+2*z;x+z]
Si*SX
```

**Salida:**
```text
SX = ([x+y+2⁢z; x+y+2⁢z; x+z])
ans = ([x+z⁢∞+x+y+2⁢z⁢∞; x+z⁢∞+x+y+2⁢z⁢∞; x+z⁢∞+x+y+2⁢z⁢∞])
```

Volver al índice

_Imágenes embebidas: 1 (image1.png)_


## Live Script: 14 problemas resueltos de aplicaciones lineales

*Fuente: `AP_LIN_02_R05.mlx`*

###  [Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

- Table of Contents

- Problema 1 ·     Solución ·         Caso 1 ·         Caso 2 · Problema 2 ·     Solución · Problema 3 ·     Solución · Problema 4 ·     Solución · Problema 5 ·     Solución ·         Inyectiva ·         Suprayectiva · Problema 6 ·     Solución ·         Inyectiva ·         Suprayectiva · Problema 7 ·     Solución ·         Inyectiva ·         Suprayectiva · Problema 8 ·     Solución · Problema 9 ·     Solución · Problema 10 ·     Solución · Problema 11 ·      Solución · Problema 12 ·     Solución  · Problema 13 ·     Solución · Problema 14 ·     Solución · Problema 15 ·     Solución · Problema 16 ·     Solución · Problema 17 ·     Solución · Problema 18 ·     Solución

#### Problema 1

Determinar cuales de las siguientes aplicaciones son lineales:

- $$f:R^3 \to R^2 \;/\;f\left(x,y,z\right)=\left(x-y,y+2z\right)$$

- $$f:R^3 \to R^2 \;/\;f\left(x,y,z\right)=\left(x-y^2 ,y+2z\right)$$

Solución

Caso 1

Sean $v_1 =\left\lbrack \begin{array}{c}
x_1 \\
y_1 \\
z_1
\end{array}\right\rbrack ,v_2 =\left\lbrack \begin{array}{c}
x_2 \\
y_2 \\
z_2
\end{array}\right\rbrack$

$$f\left(v_1 +v_2 \right)=\left(x_1 +x_2 -\left(y_1 +y_2 \right),\left(y_1 +y_2 \right)+2\left(z_1 +z_2 \right)\right)=\left(x_1 -y_1 ,y_1 +2z_1 \right)+\left(x_2 -y_2 ,y_2 +2z_2 \right)=f\left(v_1 \right)+f\left(v_2 \right)$$

$$f\left(\alpha \cdot v_1 \right)=\left(\alpha \left(x_1 -y_1 \right),\alpha \left(y_1 +2z_1 \right)\right)=\alpha \left(x_1 -y_1 ,y_1 +2z_1 \right)=\alpha \cdot f\left(v_1 \right)$$

O sea, la aplicación es lineal.

Caso 2

$$f\left(v_1 +v_2 \right)=\left(x_1 +x_2 -{\left(y_1 +y_2 \right)}^2 ,\left(y_1 +y_2 \right)+2\left(z_1 +z_2 \right)\right)=\left(x_1 +x_2 +\left(y_1^2 +y_2^2 +2y_1 y_2 \right)\right)\not= f\left(v_1 \right)+f\left(v_2 \right)$$

Por tanto, esta aplicación no es lineal.

Índice

#### Problema 2

Se considera $f:R^2 \to R^3$ , aplicación lineal tal que f(1, −1) = (−1, −2, −3) y f(−3, 2) = (0, 5, 3). Determinar, si es posible, f(x, y) donde (x, y) ∈ R² .

Solución

```matlab
clear; clc;
v1 = [1;-1]
v2 = [-3;2]
```

**Salida:**
```text
v1 =
-1
v2 =
-3
```

Los vectores v1 y v2 ¿forman una base de R²?

```matlab
check = rref([v1 v2])
```

**Salida:**
```text
check =
1  0
0  1
```

Son independientes, luego forman base. Por tanto, cualquier vector $\left(x,y\right)\in R^2$ se puede expresar como combinación de ellos. Vamos a hallar la combinación:

```matlab
syms x y a b

ec = [x;y] == a*v1 + b*v2

[a b] = solve(ec, [a b])
```

**Salida:**
```text
ec = ([x=a-3⁢b; y=2⁢b-a])
a = -2⁢x-3⁢y
b = -x-y
```

Ahora, nos basamos en que f es lineal. Por tanto:

$$\left(x,y\right)=a\cdot v_1 +b\cdot v_2 \;\;\;\;\;\to \;\;\;f\left(x,y\right)=f\left(a\cdot v_1 +b\cdot v_2 \right)=f\left(a\cdot v_1 \right)+f\left(b\cdot v_2 \right)=a\cdot f\left(v_1 \right)+b\cdot f\left(v_2 \right)$$

```matlab
fv1 = [-1;-2;-3]
fv2 = [0;5;3]
f = a*fv1 + b*fv2
```

**Salida:**
```text
fv1 =
-1
-2
-3
fv2 =
f = ([2⁢x+3⁢y; y-x; 3⁢x+6⁢y])
```

O sea:

$$f:R^2 \to R^3 :f\left(x,y\right)=\left(2x+3y,y-x,3x+6y\right)$$

Índice

#### Problema 3

Sea la aplicación lineal:

$$f:R^4 \to R^4 \;\;/\;f\left(x,y,z,t\right)=\left\lbrack \begin{array}{c}
x\\
2x-y\\
3x+2y+2z\\
4x+y+5z+7t
\end{array}\right\rbrack$$

Hallar el núcleo y la imagen de f.

Solución

```matlab
clear; clc;
syms x y z t
X = [x;y;z;t]
```

**Salida:**
```text
X = ([x; y; z; t])
```

La matriz de la aplicación es:

```matlab
A = [1 0 0 0;2 -1 0 0;3 2 2 0;4 1 5 7]
```

**Salida:**
```text
A =
1  0  0  0
2  -1  0  0
3  2  2  0
4  1  5  7
```

Sea $Y=\left\lbrack \left\lbrack \begin{array}{c}
a\\
b\\
c\\
d
\end{array}\right\rbrack \right\rbrack$un vector del núcleo. Entonces:

```matlab
syms a b c d
Y = [a;b;c;d]
ecs = A*Y == 0

[A b] = equationsToMatrix(ecs)
GJ = rref([A b])

[a b c d] = solve(ecs)
```

**Salida:**
```text
Y = ([a; b; c; d])
ecs = ([a=0; 2⁢a-b=0; 3⁢a+2⁢b+2⁢c=0; 4⁢a+b+5⁢c+7⁢d=0])
A = ([1, 0, 0, 0; 2, -1, 0, 0; 3, 2, 2, 0; 4, 1, 5, 7])
b = ([0; 0; 0; 0])
GJ = ([1, 0, 0, 0, 0; 0, 1, 0, 0, 0; 0, 0, 1, 0, 0; 0, 0, 0, 1, 0])
a = 0
b = 0
c = 0
d = 0
```

Luego $\textrm{Kerf}=\left\lbrace \left\lbrack \begin{array}{c}
0\\
0\\
0\\
0
\end{array}\right\rbrack \right\rbrace$; por tanto, Nul(f) = 0. Por tanto, f es inyectiva.

Por el famoso teorema ($\dim \;R^4 =\dim \;\ker \;f+\dim \;\textrm{Im}\;f$) sabemos que la dimensión de la imagen será 4. Que además, coincide con el rango de la matriz. Luego la imagen debería tener cuatro vectores.

$f\left(x,y,z,t\right)=\left\lbrack \begin{array}{c}
x\\
2x-y\\
3x+2y+2z\\
4x+y+5z+7t
\end{array}\right\rbrack =x\left\lbrack \begin{array}{c}
1\\
2\\
3\\
4
\end{array}\right\rbrack +y\left\lbrack \begin{array}{c}
0\\
-1\\
2\\
1
\end{array}\right\rbrack +z\left\lbrack \begin{array}{c}
0\\
0\\
2\\
5
\end{array}\right\rbrack +t\left\lbrack \begin{array}{c}
0\\
0\\
0\\
7
\end{array}\right\rbrack$. Es decir, una base es:

$B=\left\lbrace \left\lbrack \begin{array}{c}
1\\
2\\
3\\
4
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
-1\\
2\\
1
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
0\\
2\\
5
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
0\\
0\\
7
\end{array}\right\rbrack \right\rbrace$. Es suprayectiva, dado que B es tambien base de $R^4$, por lo que la imagen coincide con el codominio. Esto es condición necesaria y suficiente para que f sea inyectiva.

Índice

#### Problema 4

La aplicación lineal $f:R^3 \to R^4 \;/\;f\left(x,y,z\right)=\left\lbrack \begin{array}{c}
x\\
x+y\\
y+z\\
x+y+z
\end{array}\right\rbrack$¿es inyectiva?

Solución

```matlab
clear; clc;
syms x y z
X = [x;y;z]
A = [1 1 0 1;0 1 1 1; 0 0 1 1]'
f = A*X
```

**Salida:**
```text
X = ([x; y; z])
A =
1  0  0
1  1  0
0  1  1
1  1  1
f = ([x; x+y; y+z; x+y+z])
```

f es inyectiva sí y solo sí las imágenes de vectores independientes son independientes.

Obtenemos la imágen de la base canónica:

```matlab
BC = [1 0 0;0 1 0;0 0 1]'

f_BC = A*BC

rf_BC = rank(f_BC)
```

**Salida:**
```text
BC =
1  0  0
0  1  0
0  0  1
f_BC =
1  0  0
1  1  0
0  1  1
1  1  1
rf_BC =
```

Luego los tres vectores son l.i.

Por tanto, es inyectiva.

Ker(f):

```matlab
syms a b c
Y = [a;b;c]
ec = A*Y == 0
[a b c] = solve(ec)
```

**Salida:**
```text
Y = ([a; b; c])
ec = ([a=0; a+b=0; b+c=0; a+b+c=0])
a = 0
b = 0
c = 0
```

Nul(f) = 0

dim R3 = 3

dim Im f = 3

Índice

#### Problema 5

Sea la aplicación lineal $f:R^3 \to R^3 :f\left(x\right)=A\cdot x\;\;\;\;\;\;A=\left\lbrack \begin{array}{ccc}
1 & 2 & 0\\
0 & 1 & 1\\
0 & 0 & 1
\end{array}\right\rbrack$

Averiguar si f es inyectiva, suprayectiva o ninguna de ambas cosas.

Solución

```matlab
clear; clc;
syms x y z
A = [1 2 0;0 1 1;0 0 1]
X = [x;y;z]

f = A*X
```

**Salida:**
```text
A =
1  2  0
0  1  1
0  0  1
X = ([x; y; z])
f = ([x+2⁢y; y+z; z])
```

Inyectiva

```matlab
ecs = A*X == 0

[x y z] = solve(ecs)
[A1 b1] = equationsToMatrix(ecs)
GJ = rref([A1 b1])
```

**Salida:**
```text
ecs = ([x+2⁢y=0; y+z=0; z=0])
x = 0
y = 0
z = 0
A1 = ([1, 2, 0; 0, 1, 1; 0, 0, 1])
b1 = ([0; 0; 0])
GJ = ([1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0])
```

Por tanto, $\textrm{Ker}\left(f\right)=\left\lbrace \vec{0} \right\rbrace \;\to \textrm{Nul}\left(f\right)=0$

Suprayectiva

```matlab
dim_Im_f = rank(A)
```

**Salida:**
```text
dim_Im_f =
```

Además:

$$\dim \left(V\right)=\dim \left(\textrm{Ker}\;f\right)+\dim \left(\textrm{Im}\;f\right)\to 3=0+\dim \left(\textrm{Im}\;f\right)\;\to \dim \left(\textrm{Im}\;f\right)=3=\dim \left(W\right)$$

Además, como tanto el conjunto de partida (V) como el de llegada (W) tienen la misma dimensión y f es inyectiva, también es suprayectiva.

Por tanto, es suprayectiva

Índice

#### Problema 6

Sea la aplicación lineal $f:R^2 \to R^3 :f\left(x\right)=A\cdot x\;\;\;\;\;\;A=\left\lbrack \begin{array}{cc}
1 & 2\\
0 & 1\\
0 & 0
\end{array}\right\rbrack$

Averiguar si f es inyectiva, suprayectiva o ninguna de ambas cosas.

Solución

```matlab
clear; clc;
syms x y
A = [1 2;0 1;0 0]
X = [x;y]
f = A*X
```

**Salida:**
```text
A =
1  2
0  1
0  0
X = ([x; y])
f = ([x+2⁢y; y; 0])
```

Inyectiva

```matlab
ecs = A*X == 0
[x y] = solve(ecs)

[A1 b1] = equationsToMatrix(ecs)
GJ = rref([A1 b1])
rA1 = rank(A1)
rext = rank([A1 b1])
length(X)
```

**Salida:**
```text
ecs = ([x+2⁢y=0; y=0; 0=0])
x = 0
y = 0
A1 = ([1, 2; 0, 1; 0, 0])
b1 = ([0; 0; 0])
GJ = ([1, 0, 0; 0, 1, 0; 0, 0, 0])
rA1 =
rext =
ans =
```

Por tanto, $\textrm{Ker}\left(f\right)=\left\lbrace \vec{0} \right\rbrace \;\to \textrm{Nul}\left(f\right)=0$

Suprayectiva

$$\dim \left(V\right)=\dim \left(\textrm{Ker}\;f\right)+\dim \left(\textrm{Im}\;f\right)\to 2=0+\dim \left(\textrm{Im}\;f\right)\;\to \dim \left(\textrm{Im}\;f\right)=2\;\not= \dim \left(W\right)$$

Luego no es suprayectiva.

De otra forma:

```matlab
dim_Im_f = rank(A)
```

**Salida:**
```text
dim_Im_f =
```

Índice

#### Problema 7

Sea la aplicación lineal $f:R^3 \to R^2 :f\left(x\right)=A\cdot x\;\;\;\;\;\;A=\left\lbrack \begin{array}{ccc}
1 & 2 & 0\\
0 & 1 & -1
\end{array}\right\rbrack$

Averiguar si f es inyectiva, suprayectiva o ninguna de ambas cosas.

Solución

```matlab
clear; clc;
syms x y z
X = [x;y;z]
A = [1 2 0;0 1 -1]
f = A*X
```

**Salida:**
```text
X = ([x; y; z])
A =
1  2  0
0  1  -1
f = ([x+2⁢y; y-z])
```

Inyectiva

```matlab
ecs = A*X == 0

[A1 b1] = equationsToMatrix(ecs)
GJ = rref([A1 b1])

rank(A1)
rank([A1 b1])
length(X)

ecs1 = GJ(:,1:3)*X == GJ(:,4)
[x y] = solve(ecs,[x y])
```

**Salida:**
```text
ecs = ([x+2⁢y=0; y-z=0])
A1 = ([1, 2, 0; 0, 1, -1])
b1 = ([0; 0])
GJ = ([1, 0, 2, 0; 0, 1, -1, 0])
ans =
ans =
ans =
ecs1 = ([x+2⁢z=0; y-z=0])
x = -2⁢z
y = z
```

Es decir, $\ker \;f=\left\lbrack \begin{array}{c}
-2z\\
z
\end{array}\right\rbrack =z\left\lbrack \begin{array}{c}
-2\\
1
\end{array}\right\rbrack$

Por lo que una base del kernel de f es $B=\left\lbrace \left\lbrack \begin{array}{c}
-2\\
1
\end{array}\right\rbrack \right\rbrace$y Nul f = 1.

Por tanto no es inyectiva.

Suprayectiva

$$\dim \left(V\right)=\dim \left(\textrm{Ker}\;f\right)+\dim \left(\textrm{Im}\;f\right)\to 3=1+\dim \left(\textrm{Im}\;f\right)\;\to \dim \left(\textrm{Im}\;f\right)=2\;=\dim \left(W\right)$$

Luego es suprayectiva

Índice

#### Problema 8

Hallar la matriz canónica de la aplicación lineal $f:R^3 \to R^{3\;} \;/\;f\left(x,y,z\right)=\left(x-2y,2x+y\right)$

Solución

La matriz canónica es la transformada de la base canónica del espacio vectorial de partida.

```matlab
clear; clc;
syms x y z
f = @(x,y,z) [x - 2*y,2*x + y]
A = [f(1,0,0)' f(0,1,0)' f(0,0,1)']
```

**Salida:**
```text
f = function_handle with value:
@(x,y,z)[x-2*y,2*x+y]
A =
1  -2  0
2  1  0
```

Comprobación:

```matlab
X = [x;y;z]
A*X
```

**Salida:**
```text
X = ([x; y; z])
ans = ([x-2⁢y; 2⁢x+y])
```

Índice

#### Problema 9

Sea $f:R^2 \to R^2$ la aplicación lineal definida por: $f\left(x_1 ,x_2 \right)=\left(x_1 +x_2 ,2x_1 -x_2 \right)$.

Hallar la matriz de f respecto de las bases: $B=\left\lbrace v_1 ,v_2 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
2
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-1\\
1
\end{array}\right\rbrack \right\rbrace$y $B^{\prime } =\left\lbrace w_1 ,w_2 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack \right\rbrace$.

Solución

```matlab
clear; clc;
f = @(x1,x2) [x1 + x2, 2*x1 - x2]

f_v1 = f(1,2)
f_v2 = f(-1,1)
```

**Salida:**
```text
f = function_handle with value:
@(x1,x2)[x1+x2,2*x1-x2]
f_v1 =
3  0
f_v2 =
0  -3
```

Así, la matriz de f respecto de B y B′ se halla tomando estas matrices de coordenadas como columnas:

```matlab
A = [f_v1' f_v2']
```

**Salida:**
```text
A =
3  0
0  -3
```

Índice

#### Problema 10

Sea $D_x :P_2 \to P_1 \;$ el operador derivada que transforma todo polinomio de grado 2 p(x) en su derivada p′(x).

Hallar la matriz de $D_x$ en las bases: $B=\left\lbrace 1,x,x^2 \right\rbrace$ y $B^{\prime } =\left\lbrace 1,x\right\rbrace$.

Solución

Hallamos la imagen de la base B:

```matlab
clear; clc;
syms x
f = @(x) diff(x,1)
Dx1 = f(1)
Dx_x = f(x)
Dx_x2 = f(x^2)
```

**Salida:**
```text
f = function_handle with value:
@(x)diff(x,1)

Dx1 =

[]
Dx_x = 1
Dx_x2 = 2⁢x
```

Expresado en la base B':

$$D_x \left(1\right)=0\cdot 1+0\cdot x$$

$$D_x \left(x\right)=1\cdot 1+0\cdot x$$

$$D_x \left(x^2 \right)=0\cdot 1+2\cdot x^2$$

Por tanto:

$$A=\left\lbrack \left\lbrack \begin{array}{ccc}
0 & 1 & 0\\
0 & 0 & 2
\end{array}\right\rbrack \right\rbrack$$

```matlab
A = [0 1 0;0 0 2]
```

**Salida:**
```text
A =
0  1  0
0  0  2
```

Sea un polinomio de P2: $P=a+\textrm{bx}+{\textrm{cx}}^2$:

```matlab
syms a b c
P = [a;b;c]
Dx_P = A*P
Dx_P = [1 x]*A*P
```

**Salida:**
```text
P = ([a; b; c])
Dx_P = ([b; 2⁢c])
Dx_P = b+2⁢c⁢x
```

Índice

#### Problema 11

Sea $T:R^4 \to R^4$ una transformación definida por $T\left(v_i \right)=w_i \;\;\;\;\;\;\;i=1,2,3,4$, donde:

$$\left\lbrace v_1 ,v_2 ,v_3 ,v_4 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
0\\
0\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
2\\
1\\
0\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-2\\
1\\
2\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
3\\
4\\
2\\
1
\end{array}\right\rbrack \right\rbrace$$

$$\left\lbrace w_1 ,w_2 ,w_3 ,w_4 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
2\\
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
2\\
5\\
3\\
2
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-1\\
-1\\
-1\\
2
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
3\\
7\\
7
\end{array}\right\rbrack \right\rbrace$$

- Verifique que el conjunto vi es una base para $R^4$, y por tanto, que T está bien definida

- Verifique que el conjunto wi es una base para$R^4$. ¿Por qué se puede concluir que T es un isomorfismo?

- Encuentre la representación matricial A respecto de la base canónica

Solución

Es evidente que V es base de R4. No obstante:

```matlab
clear; clc;
v1 = [1;0;0;0]
v2 = [2;1;0;0]
v3 = [-1;1;2;0]
v4 = [3;4;2;1]
V = [v1 v2 v3 v4]
det(V)
```

**Salida:**
```text
v1 =
v2 =
v3 =
-1
v4 =
V =
1  2  -1  3
0  1  1  4
0  0  2  2
0  0  0  1
ans =
```

Procedemos de igual manera con W:

```matlab
w1 = [1;2;1;0]
w2 = [2;5;3;2]
w3 = [-1;-1;-1;2]
w4 = [0;3;7;7]
W = [w1 w2 w3 w4]
det(W)
```

**Salida:**
```text
w1 =
w2 =
w3 =
-1
-1
-1
w4 =
W =
1  2  -1  0
2  5  -1  3
1  3  -1  7
0  2  2  7
ans =
-1
```

Sea $x=\sum \alpha_i v_i$ un vector del núcleo de T. Entonces: $T\left(x\right)=0\;\;\;\to \;\;T\left(\sum_i \alpha_i v_i \right)=0\;\;\;\to \;\;\sum_i \alpha_i T\left(v_i \right)=0\;\;\;\to \;\;\sum_i \alpha_i w_i =0$; pero como los vectores wi son linelamente independientes, se concluye que $\alpha_i =0$, y por tanto, $x=0$, por lo que nulT = 0, y T es inyectiva.

Así, $\dim \left(R^4 \right)=\textrm{NulT}+\dim \left(\textrm{ImT}\right)\;\;\to \;\;4=0+\dim \left(\textrm{ImT}\right)\;\;\;\to \;\;\dim \left(\textrm{ImT}\right)=4$, y T es sobreyectiva. O sea, T es un isomorfismo.

```matlab
bc1 = v1
bc2 = v2 - 2*v1
bc3 = 0.5*v3 - 0.5*v2 + 1.5*v1
bc4 = v4 - v3 - 3*v2 + 2*v1

Tbc1 = w1
Tbc2 = w2 - 2*w1
Tbc3 = 0.5*w3 - 0.5*w2 + 1.5*w1
Tbc4 = w4 - w3 - 3*w2 + 2*w1

```

**Salida:**
```text
bc1 =
bc2 =
bc3 =
bc4 =
Tbc1 =
Tbc2 =
Tbc3 =
-0.5000
Tbc4 =
-3
-7
-1
```

$$T*\textrm{BC}=\textrm{TBC}$$

```matlab
TBC = [Tbc1 Tbc2 Tbc3 Tbc4]
det(TBC)
syms x y z t
X = [x;y;z;t]

ec = TBC*X == 0

sol = solve(ec)

[A1 b1] = equationsToMatrix(ec)
rref([A1 b1])

```

**Salida:**
```text
TBC =
1.0000  0  0  -3.0000
2.0000  1.0000  0  -7.0000
1.0000  1.0000  -0.5000  1.0000
0  2.0000  0  -1.0000
ans =
-0.5000
X = ([x; y; z; t])
ec = ([-3⁢t+x=0; -7⁢t+y+2⁢x=0; t-(z)/(2)+y+x=0; -t+2⁢y=0])
sol = struct with fields:
t: 0
x: 0
y: 0
z: 0
A1 = ([-3, 1, 0, 0; -7, 2, 1, 0; 1, 1, 1, -(1)/(2); -1, 0, 2, 0])
b1 = ([0; 0; 0; 0])
ans = ([1, 0, 0, 0, 0; 0, 1, 0, 0, 0; 0, 0, 1, 0, 0; 0, 0, 0, 1, 0])
```

Índice

#### Problema 12

Sea la transformación lineal $f:R^2 \to R^2$, definida por la matriz $A=\left\lbrack \begin{array}{cc}
3 & 2\\
1 & 4
\end{array}\right\rbrack$. Aplicarla al cuadrado de la figura, definido por los puntos P1(0,0); P2(1,0); P3(1,1) y P4(0,1). Dibujar los autovectores. Calcularlos.

Solución

```matlab
clear; clc;
P1 = [0,0]
P2 = [1,0]
P3 = [1,1]
P4 = [0,1]
A = [3 2;1 4]
```

**Salida:**
```text
P1 =
0  0
P2 =
1  0
P3 =
1  1
P4 =
0  1
A =
3  2
1  4
```

Dibujamos

```matlab
fig = figure;
X = [P1(1), P2(1), P3(1),P4(1),P1(1)];
Y = [P1(2), P2(2), P3(2),P4(2),P1(2)];
plot(X,Y,'r')
hold on
plot(X,Y,'or','MarkerFaceColor','r')
grid on
xlabel('x')
ylabel('y')
xlim([-6,6])
ylim([-6,6])
savefig('original')
```

**Salida:**
```text
[figura]
```

Aplicamos la transformación lineal a los puntos:

```matlab
Pp1 = A*P1'
Pp2 = A*P2'
Pp3 = A*P3'
Pp4 = A*P4'
```

**Salida:**
```text
Pp1 =
Pp2 =
Pp3 =
Pp4 =
```

Dibujamos

```matlab
fig2 = figure;
openfig('original');
Xp = [Pp1(1), Pp2(1), Pp3(1),Pp4(1),Pp1(1)];
Yp = [Pp1(2), Pp2(2), Pp3(2),Pp4(2),Pp1(2)];
plot(Xp,Yp,'--b')
plot(Xp,Yp,'ob','MarkerFaceColor','b')
quiver(P2(1),P2(2),Pp2(1)-P2(1),Pp2(2)-P2(2),1,'g')
quiver(P3(1),P3(2),Pp3(1)-P3(1),Pp3(2)-P3(2),1,'r','LineWidth',2)
quiver(P4(1),P4(2),Pp4(1)-P4(1),Pp4(2)-P4(2),1,'g')
```

Calculamos

```matlab
[V,D] = eig(A)
hold on
quiver(0,0,V(1,1),V(2,1),1)
quiver(0,0,V(1,2),V(2,2),1)
axis equal
```

**Salida:**
```text
V =
-0.8944  -0.7071
0.4472  -0.7071
D =
2  0
0  5
[figura]
```

Índice

#### Problema 13

Hallar la matriz canónica de la aplicación lineal $f:R^3 \to R^2$ definida por:

f(x, y, z)=(x-2y, 2x+y)

Solución

```matlab
clear; clc;
f = @(x,y,z) ([x-2*y;2*x+y])
```

**Salida:**
```text
f = function_handle with value:
@(x,y,z)([x-2*y;2*x+y])
```

Obtenemos la transformada de la base canónica:

```matlab
A = [f(1,0,0), f(0,1,0), f(0,0,1)]
```

**Salida:**
```text
A =
1  -2  0
2  1  0
```

Comprobamos:

```matlab
syms x y z
A*[x;y;z]
```

**Salida:**
```text
ans = ([x-2⁢y; 2⁢x+y])
```

Índice

#### Problema 14

Sea $f:R^2 \to R^2$ la aplicación lineal definida por: $f\left\lbrack \begin{array}{c}
x_1 \\
x_2
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
x_1 +x_2 \\
2x_1 -x_2
\end{array}\right\rbrack$

Hallar la matriz de f respecto de las bases:

$B=\left\lbrace v_1 ,v_2 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
2
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-1\\
1
\end{array}\right\rbrack \right\rbrace$ y $B^{\prime } =\left\lbrace w_1 ,w_2 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack \right\rbrace \;$

Solución

```matlab
clear; clc;
f = @(x1,x2) ([x1 + x2; 2*x1 - x2])

v1 = [1;2]
v2 = [-1;1]
fv1 = f(v1(1),v1(2))
fv2 = f(v2(1),v2(2))
A = [fv1, fv2]
```

**Salida:**
```text
f = function_handle with value:
@(x1,x2)([x1+x2;2*x1-x2])
v1 =
v2 =
-1
fv1 =
fv2 =
-3
A =
3  0
0  -3
```

Índice

#### Problema 15

Sea $D_x :P_2 \to P_1$ el operador derivada que transforma todo polinomio de grado 2 p(x) en su derivada p′(x).

Hallar la matriz de $D_x$ en las bases: $B=\left\lbrace 1,x,x^2 \right\rbrace$ y $B^{\prime } =\left\lbrace 1,x\right\rbrace$.

Solución

```matlab
clear; clc;
syms x a b c
```

Derivadas de los vectores de la base B:

```matlab
Dx1 = diff(1,x,1)
Dxx = diff(x,x,1)
Dxx2 = diff(x^2,x,1)
```

**Salida:**
```text
Dx1 = 0
Dxx = 1
Dxx2 = 2⁢x
```

Las derivadas pertenecen a P1; expresadas en B':

$$\begin{array}{l}
D_x \left(1\right)=\left\lbrace \left\lbrack \begin{array}{c}
0\\
0
\end{array}\right\rbrack \right\rbrace \\
D_x \left(x\right)=\left\lbrace \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack \right\rbrace \\
D_x \left(x^2 \right)=\left\lbrace \left\lbrack \begin{array}{c}
0\\
2
\end{array}\right\rbrack \right\rbrace
\end{array}$$

Por tanto:

$$A=\left\lbrack \begin{array}{ccc}
0 & 1 & 0\\
0 & 0 & 2
\end{array}\right\rbrack$$

Esta matriz produce la derivada de todo polinomio de grado 2:

```matlab
A = [0 1 0;0 0 2]
v = [a;b;c]
B = [1;x;x^2]
v1 = dot(v,B)
Dxv = A*v
Dxv = dot (Dxv,[1;x])
```

**Salida:**
```text
A =
0  1  0
0  0  2
v = ([a; b; c])
B = ([1; x; x^2])
v1 = a‾+x⁢b‾+x^2⁢c‾
Dxv = ([b; 2⁢c])
Dxv = b‾+2⁢x⁢c‾
```

Índice

#### Problema 16

[Imagen: Enunciado: Muestre que $T:\mathbb{R}^3\to\mathbb{R}^3$ dada por $T(x,y,z)=(x+y,\ y+z,\ x+z)$ es una transformación lineal invertible. Además, halle $T^{-1}$.]

Solución

```matlab
clear; clc;
f = @(x,y,z) ([x+y;y+z;x+z])
f1 = f(1,0,0)
f2 = f(0,1,0)
f3 = f(0,0,1)

T = [f1,f2,f3]
det(T)
Ti = inv(T)

syms x y z
X = [x;y;z]
T*X
Ti*(T*X)
```

**Salida:**
```text
f = function_handle with value:
@(x,y,z)([x+y;y+z;x+z])
f1 =
f2 =
f3 =
T =
1  1  0
0  1  1
1  0  1
ans =
Ti =
0.5000  -0.5000  0.5000
0.5000  0.5000  -0.5000
-0.5000  0.5000  0.5000
X = ([x; y; z])
ans = ([x+y; y+z; x+z])
ans = ([x; y; z])
```

Índice

#### Problema 17

[Imagen: Enunciado: Sea $S:\mathbb{R}^3\to\mathbb{R}^3$ dada por $S(x,y,z)=(x+y+2z,\ x+y+2z,\ x+z)$. ¿Es S una transformación lineal invertible? Además, halle $S^{-1}$ si es posible.]

Solución

```matlab
clear; clc;
f = @(x,y,z) ([x+y+2*z;x+y+2*z;x+z])
f1 = f(1,0,0)
f2 = f(0,1,0)
f3 = f(0,0,1)

S = [f1,f2,f3]
det(S)
```

**Salida:**
```text
f = function_handle with value:
@(x,y,z)([x+y+2*z;x+y+2*z;x+z])
f1 =
f2 =
f3 =
S =
1  1  2
1  1  2
1  0  1
ans =
```

Luego S no es invertible

Índice

#### Problema 18

Probar que la aplicación lineal $f:R^3 \to R^3$definida por: f(x,y,z) = (2x + 3y + z,3x + 3y + z,2x + 4y + z) es invertible y hallar su inversa. ¿Es isomorfismo?

Solución

```matlab
clear; clc;
f = @(x,y,z) ([2*x + 3*y + z;3*x + 3*y + z;2*x + 4*y + z])
f1 = f(1,0,0)
f2 = f(0,1,0)
f3 = f(0,0,1)

S = [f1,f2,f3]
det(S)

Si = inv(S)
```

**Salida:**
```text
f = function_handle with value:
@(x,y,z)([2*x+3*y+z;3*x+3*y+z;2*x+4*y+z])
f1 =
f2 =
f3 =
S =
2  3  1
3  3  1
2  4  1
ans =
Si =
-1.0000  1.0000  -0.0000
-1.0000  0  1.0000
6.0000  -2.0000  -3.0000
```

¿Es suprayectiva?

```matlab
rank(S)
```

**Salida:**
```text
ans =
```

Si, porque $\dim \left\lbrack \mathrm{Im}\left(f\right)\right\rbrack =\mathrm{rank}\left(f\right)=3=\dim \left(R^3 \right)$

¿Es inyectiva?

Sí, porque $\mathrm{Nul}\left(f\right)=\dim \left(R^3 \right)-\dim \left\lbrack \mathrm{Im}\left(f\right)\right\rbrack =3-3=0$

Luego es un isomorfismo

Índice

_Imágenes embebidas: 3 (image1.png, image2.png, image3.png)_
