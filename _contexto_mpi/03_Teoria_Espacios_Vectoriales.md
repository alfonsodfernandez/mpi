# Teoría: espacios vectoriales

Tema 4 (Grupo A) / Tema 3 (Grupo B): espacios y subespacios, combinación lineal, independencia, bases, dimensión, cambio de base, rango y núcleo.

**Contenido de este archivo:**
- Diapositivas: Espacios vectoriales
- Pizarra · Espacios vectoriales
- Pizarra · Subespacios vectoriales
- Pizarra · Combinación lineal e independencia
- Pizarra · Bases y dimensión
- Pizarra · Cambio de base
- Pizarra · Rango, nulidad, espacio fila y columna
- Live Script: cambio de base
- Live Script: dependencia e independencia lineal
- Live Script: problemas de cambio de base
- Live Script: funciones auxiliares (EV_tools)


## Diapositivas: Espacios vectoriales

*Fuente: `03 - Espacios Vectoriales_R00.pptm`*

#### Diapositiva 1

- ESPACIOS VECTORIALES
- MATEMÁTICAS PARA LA INGENIERÍA I
- Prof. Dr. Josemaría Medina Villaverde
- UFV.ES

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 2

- Concepto
- 01
- Bases y dimensión de un E.V.
- 04
- Subespacios vectoriales
- 02
- Cambio de base
- 05
- Sistemas generadores
- 03
- Rango de una matriz y S.E.L.
- 06
- ÍNDICE
- Combinación lineal de vectores
- 07

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 3

- CONCEPTO
- CAPÍTULO 01
- 3
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Separador de capítulo con foto de la estatua de Francisco de Vitoria ante el convento de San Esteban (Salamanca); se repite en los demás separadores de capítulo de esta presentación.

#### Diapositiva 4

- CONCEPTO
- 4
- UFV.ES
- Un espacio vectorial (o espacio lineal) es el objeto básico de estudio del álgebra lineal.
- A los elementos de los espacios vectoriales se les llama vectores (aunque no siempre tienen la forma de los vectores con los que estamos familiarizados)
- Sobre los vectores pueden realizarse dos operaciones: la multiplicación por escalares y la adición (una asociación entre un par de objetos).
- Estas dos operaciones se tienen que ceñir a un conjunto de axiomas.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ilustración de un vector P en un sistema de ejes 3D.

#### Diapositiva 5

- CONCEPTO
- 5
- UFV.ES
- Definición
- Sea V un conjunto en el que se han definido dos operaciones:
- •	Suma de vectores
- •	Producto de un vector por un escalar
- Se dice que V  tiene estructura de espacio vectorial sobre  R si se verifica para todo u,v,w ∈ V y para todo λ,μ ∈ R las siguientes propiedades:
- u+v ∈ V			La suma es cerrada
- u+v = v+u			Propiedad conmutativa
- u+(v+w) = (u+v)+w		Propiedad asociativa
- ∃ o∈V,∀ u∈V, u+o = u		Elemento neutro de la suma
- ∀ u∈V,∃-u∈V, u+(-u) = o	Elemento inverso de la suma
- λu ∈V			Multiplicación por escalar es cerrada
- λ (u+v) = λu+λv		Propiedad distributiva
- (λ+μ)· u = λu+μu		Propiedad distributiva
- λ(μu) = (λμ)  u			Propiedad asociativa
- 1u = u			Identidad escalar

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Axiomas (imagen): 1. $u+v\in V$ (suma cerrada); 2. $u+v=v+u$ (conmutativa); 3. $u+(v+w)=(u+v)+w$ (asociativa); 4. $\exists\,o\in V: u+o=u$ (neutro); 5. $\forall u\ \exists -u: u+(-u)=o$ (inverso); 6. $\lambda u\in V$ (producto por escalar cerrado); 7. $\lambda(u+v)=\lambda u+\lambda v$; 8. $(\lambda+\mu)u=\lambda u+\mu u$ (distributivas); 9. $\lambda(\mu u)=(\lambda\mu)u$ (asociativa); 10. $1u=u$ (identidad escalar).

#### Diapositiva 6

- CONCEPTO
- 6
- UFV.ES
- Cuando no haya lugar a confusión con respecto a las operaciones consideradas, denotaremos el espacio vectorial simplemente por V .
- Observemos que no debemos confundir el vector neutro 0 y el escalar 0.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ilustración de un profesor con puntero.

#### Diapositiva 7

- CONCEPTO
- UFV.ES
- suma:
- producto por un escalar:
- vector nulo:
- vector opuesto:
- F(x)
- Mnxn

_Imágenes/medios en la diapositiva: 24_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Tabla (imagen) de ejemplos de e.v.: $\mathbb{R}^n$ (suma y producto componente a componente, vector nulo $(0,\dots,0)$, opuesto $-\bar x$); $P_n$ (suma y producto de coeficientes, nulo $0x^n+\dots+0$, opuesto $-p(x)$); $M_{n\times n}$ (suma y producto elemento a elemento, nula $(0)$, opuesta $-A$); $F(x)$ funciones $f:[a,b]\to\mathbb{R}$ ($(f+g)(x)=f(x)+g(x)$, $(\alpha f)(x)=\alpha f(x)$, nula $f(x)=0$, opuesta $(-f)(x)=-f(x)$).

#### Diapositiva 8

- CONCEPTO
- El conjunto de los polinomios de coeficientes reales de grado n
- ¿es un espacio vectorial?
- NO: la suma no es una operación cerrada.
- P1(x) = xn + 2x +1 	 Pn(x)
- P2(x) = - xn + 2x +3 	 Pn(x)
- P1(x) + P2(x) = 4x + 4 	 Pn(x)
- Propiedades de la multiplicación por un escalar
- Sea $𝑉$ un espacio vectorial sobre $ℝ$, si $𝒖,𝒗 ∈𝑉$ y  $𝜆, 𝜇∈ℝ$, se cumplen las siguientes propiedades:
- $0𝒗=𝒐$
- $𝜆𝒐=𝒐$
- $𝑆𝑖 𝜆𝒗=𝒐 ⟹ 𝝀=0 ó 𝒗=𝒐$
- $–𝜆𝒖=−𝝀𝒖=𝝀−𝒖$
- $(𝜆𝒖=𝜇𝒖$ y $𝒖≠𝒐)⟹𝜆=𝜇$
- $(𝜆𝒖=𝝀𝒗$ y $𝝀≠0)⟹𝒖=𝒗$

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: $P_1(x)=x^n+2x+1\in P^n$, $P_2(x)=-x^n+2x+3\in P^n$, $P_1+P_2=4x+4\notin P^n$ (polinomios de grado exactamente n no son e.v.). Propiedades: $0v=o$; $\lambda o=o$; $\lambda v=o\Rightarrow\lambda=0$ ó $v=o$; $-(\lambda u)=(-\lambda)u=\lambda(-u)$; $(\lambda u=\mu u,\ u\neq o)\Rightarrow\lambda=\mu$; $(\lambda u=\lambda v,\ \lambda\neq0)\Rightarrow u=v$.

#### Diapositiva 9

- SUBESPACIOS VECTORIALES
- CAPÍTULO 02
- 9
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 10

- SUBESPACIOS VECTORIALES
- UFV.ES
- Un subconjunto no vacío $𝑊$ de un espacio vectorial $𝑉$, es un subespacio vectorial de $𝑉$  si $𝑊$ es espacio vectorial con las mismas operaciones de suma y producto por un escalar definidas en $𝑉$.
- Para que $𝑊$ pueda ser subespacio de $𝑉$, las dos operaciones han de ser cerradas en $𝑾$.
- Para concluir que un conjunto es espacio vectorial, hay que comprobar los diez axiomas.
- Sin embargo, al ser $𝑊$ un subconjunto de un espacio vectorial $𝑉$ basta con verificar que las dos operaciones son cerradas en $𝑊$, es decir:
- subespacios triviales de V:
- $𝑊={𝒐}$
- $𝑊=𝑉$
- Los demás subespacios se denominan subespacios propios
- $𝒖+𝒗∈𝑊, ∀ 𝒖, 𝒗 ∈𝑊$
- $𝜆𝒖∈𝑊, ∀𝒖∈𝑊 𝑦 ∀𝜆∈ℝ$

_Imágenes/medios en la diapositiva: 6_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Condiciones: 1. $u+v\in W\ \forall u,v\in W$; 2. $\lambda u\in W\ \forall u\in W,\ \lambda\in\mathbb{R}$. Subespacios triviales: $W=\{o\}$, $W=V$.

#### Diapositiva 11

- SUBESPACIOS VECTORIALES
- UFV.ES
- La recta r: y = x, ¿es un subespacio vectorial de R²?
- (0,0)  r
- (a,a), (b,b)  r -> (a+b, a+b)  r
- (a,a)  r, l  R -> (l a, l a)  r
- Luego la recta r: y = x, SÍ es un subespacio vectorial de R²
- Y la recta r: y = 2x + 6, ¿es un subespacio vectorial de R²?

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: la recta $y=x$: $(0,0)\in r$; $(a,a)+(b,b)=(a+b,a+b)\in r$; $\lambda(a,a)\in r$ ⇒ SÍ es s.e.v. de $\mathbb{R}^2$. ¿Y la recta $y=2x+6$? (gráfica de una recta que no pasa por el origen ⇒ no lo es).

#### Diapositiva 12

- SISTEMAS GENERADORES
- CAPÍTULO 03
- 12
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 13

- SISTEMAS GENERADORES
- UFV.ES
- Se dice que los vectores $𝒗1, 𝒗2, …, 𝒗𝑛$ de un espacio vectorial $𝑉$ generan $𝑉$ si todo vector de $𝑽$ se puede escribir como combinación lineal de los mismos.
- Es decir,
- $∀𝒙∈𝑉, ∃ 𝜆1, 𝜆2, …, 𝜆𝑛;𝒙= 𝜆1𝒗1+ 𝜆2𝒗2+…+ 𝜆𝑛𝒗𝑛$
- El conjunto $𝑆={1,0,0, 0,1,0, 0,0,1}$ es un sistema de generadores de $ℝ3$ porque todo vector de $ℝ3$: $𝒖=(𝑢1, 𝑢2, 𝑢3)$ puede expresarse como combinación lineal de los vectores de $𝑆$, de la forma:
- $𝒖=𝑢11,0,0+𝑢20,1,0+𝑢30,0,1=(𝑢1, 𝑢2, 𝑢3)$
- El conjunto $𝑆={1, 𝑥, 𝑥2}$ genera $𝑃2 porque cualquier polinomio px=a+bx+cx2$ de P2 se puede expresar como:
- $𝑝𝑥=𝑎1+𝑏𝑥+𝑐𝑥2$

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\forall x\in V\ \exists\lambda_i: x=\lambda_1v_1+\dots+\lambda_nv_n$. Ejemplos: $u=u_1(1,0,0)+u_2(0,1,0)+u_3(0,0,1)$; $p(x)=a(1)+b(x)+c(x^2)$.

#### Diapositiva 14

- SISTEMAS GENERADORES
- UFV.ES
- Dependencia e independencia lineal
- Dado cualquier conjunto de vectores $𝑆={𝒗1, 𝒗2, …, 𝒗𝑘}$ de un espacio vectorial $𝑉$, la ecuación vectorial:
- $𝜆1𝒗1+𝜆2𝒗2+…+𝜆𝑘𝒗𝑘=𝒐$
- tiene siempre la solución trivial $𝜆1=𝜆2=…=𝜆𝑘=0$
- Se dice que un conjunto de vectores $𝑆={𝒗1, 𝒗2, …, 𝒗𝑘}$ de un espacio vectorial $𝑉$ es linealmente independiente si la ecuación vectorial:
- tiene sólo la solución trivial $𝜆1=𝜆2=…=𝜆𝑘=0$.
- Si hay otras soluciones no triviales, se dice que $𝑆$ es linealmente dependiente.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $\lambda_1v_1+\dots+\lambda_kv_k=o$ con solución trivial $\lambda_i=0$.

#### Diapositiva 15

- SISTEMAS GENERADORES
- UFV.ES
- Dependencia e independencia lineal
- Un conjunto $𝑆=𝒗1, 𝒗2, …, 𝒗𝑘, 𝑘≥2$, es linealmente dependiente sí, y sólo sí, al menos uno de sus vectores $𝒗𝒋$ se puede escribir como combinación lineal de los demás vectores de $𝑆$.
- Propiedad
- Un conjunto de $𝑛$ vectores en $ℝ𝑚$ es siempre linealmente dependiente si $𝒏>𝒎$.
- Teorema

_Imágenes/medios en la diapositiva: 3_

#### Diapositiva 16

- SISTEMAS GENERADORES
- UFV.ES
- Dependencia e independencia lineal
- Un conjunto de $𝑛$ vectores en $ℝ𝑚$ es siempre linealmente dependiente si $𝒏>𝒎$.
- Teorema
- $𝑎11𝛼1+𝑎12𝛼2+…+𝑎1𝑛𝛼𝑛=0𝑎21𝛼1+𝑎22𝛼2+…+𝑎2𝑛𝛼𝑛=0⋮𝑎𝑚1𝛼1+𝑎𝑚2𝛼2+…+𝑎𝑚𝑛𝛼𝑛=0 $
- $𝒏>𝒎$
- r(A) < n
- Hay soluciones diferentes de la trivial - > linealmente dependientes
- $𝛼1𝒗1+ 𝛼2𝒗2+…+𝛼𝑛𝒗𝑛=𝒐$

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Sistema homogéneo $a_{i1}\alpha_1+\dots+a_{in}\alpha_n=0$ (m ecuaciones, n incógnitas); si $n>m$ ⇒ $r(A)<n$ ⇒ hay soluciones distintas de la trivial ⇒ l.d.

#### Diapositiva 17

- SISTEMAS GENERADORES
- UFV.ES
- Dependencia e independencia lineal
- Sean  v1,v2,…,vn,v(n+1), n+1 vectores que están en un espacio vectorial V.
- Si 〖v1,v2,…,vn〗 genera a V, entonces v1,v2,…,vn,v(n+1) también genera a V.
- Es decir, si se agregan uno o más vectores a un conjunto generador, se obtiene otro conjunto generador.
- Teorema
- Sea
- $𝐴=𝑎11𝑎12⋯𝑎1𝑛𝑎21𝑎22⋯𝑎2𝑛⋮⋮⋱⋮𝑎𝑚1𝑎𝑚2⋯𝑎𝑚𝑛$
- Entonces las columnas de $𝐴$ consideradas como vectores son linealmente dependientes si y sólo si el sistema, que se puede escribir como $𝐴𝝀= 𝟎$, tiene soluciones no triviales. $𝝀=𝜆1𝜆2⋮𝜆𝑛$

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Matriz $A=(a_{ij})_{m\times n}$; $A\lambda=0$ con $\lambda=(\lambda_1,\dots,\lambda_n)^T$.

#### Diapositiva 18

- SISTEMAS GENERADORES
- UFV.ES
- Dependencia e independencia lineal
- Sean v1,v2,…,vn, n vectores de Rn y sea A una matriz de n x n cuyas columnas son v1,v2,…,vn. Entonces v1,v2,…,vn son linealmente independientes si y sólo si la única solución al sistema homogéneo Ax = 0 es la solución trivial x = 0
- Teorema
- Cualquier conjunto de n vectores de Rn linealmente independiente, genera Rn

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 19

- BASES Y DIMENSIÓN DE UN ESPACIO VECTORIAL
- CAPÍTULO 04
- 19
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 20

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Un conjunto de vectores $𝑆={𝒗1, 𝒗2, …, 𝒗𝑛}$ de un espacio vectorial $𝑉 $es una base de $𝑉$ si se cumple:
- $𝑆$ genera $𝑉$
- $𝑆$ es linealmente independiente
- Base de un espacio vectorial
- Dimensión de un espacio vectorial
- Si un espacio vectorial tiene una base formada por $𝒏$ vectores, se dice que $𝑉$ tiene dimensión $𝒏$ (o que es $𝑛$-dimensional), y se escribe $dim𝑉=𝑛$.
- Si $𝑽$ contiene sólo el vector cero, se define como de dimensión cero.

_Imágenes/medios en la diapositiva: 3_

#### Diapositiva 21

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Base de un espacio vectorial
- Teorema
- Si $𝑆={𝒗1, 𝒗2, …, 𝒗𝑛}$ es una base de un espacio vectorial $𝑉$, cada vector de $𝑽$ se puede escribir como una, y sólo una, forma como combinación lineal de los vectores de $𝑆$.
- Como $𝑆$ genera $𝑉$, cualquier vector $𝒖∈𝑉$ se puede expresar como:
- $𝒖= 𝜆1𝒗1+ 𝜆2𝒗2,+…+ 𝜆𝑛𝒗𝑛$ .
- Para probar la unicidad, supongamos que $𝒖$ tiene otra expresión de la forma :
- $𝒖= 𝜇1𝒗1+ 𝜇2𝒗2,+…+ 𝜇𝑛𝒗𝑛$.
- Restando ambas expresiones resulta:
- $𝒖−𝒖=(𝜆1−𝜇1)𝒗1+ (𝜆2−𝜇2)𝒗2,+…+ (𝜆𝑛−𝜇𝑛)𝒗𝑛=𝒐$
- Ahora bien, si $𝑆$ es linealmente independiente, la única solución de esta ecuación es la solución trivial:
- $(𝜆1−𝜇1)=0,   (𝜆2−𝜇2)=0,    (𝜆𝑛−𝜇𝑛)=0$
- Lo cual significa que $𝜆𝑖=𝜇𝑖,  ∀𝑖=1, 2, …, 𝑛$. Por tanto, $𝒖$ tiene un único desarrollo en términos de la base 𝑆 dada.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $[x]_B=(\lambda_1,\lambda_2,\dots,\lambda_n)^T$, $x=\sum\lambda_iv_i$.

#### Diapositiva 22

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Coordenadas y componentes de un vector en una base
- Si el espacio vectorial $𝑉$ admite una base $𝐵={𝒗1, 𝒗2, …, 𝒗𝑛}$ se llaman coordenadas de un vector $𝒙∈𝑉$ respecto de la base $𝐵$, a los únicos escalares $𝜆1, 𝜆2, …. , 𝜆𝑛$ para los que:
- $𝒙=𝑖=1𝑛𝜆𝑖𝒗𝑖$
- Los vectores $𝜆𝑖𝒗𝑖$ se llaman componentes del vector $𝒙$ respecto de la base $𝐵$.
- La matriz de coordenadas (o vector de coordenadas) de $𝒙$ en la base $𝐵$ es la matriz columna en $ℝ𝑛$ cuyas componentes son las coordenadas de $𝒙$:
- $[𝒙]𝑩=𝜆1𝜆2⋮𝜆𝑛$

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: sistema de coordenadas cartesianas 3D, vector $\vec P$ con sus componentes X, Y, Z dibujadas.

#### Diapositiva 23

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- EJEMPLO:
- Sistema de coordenadas cartesianas 3D

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** MATLAB: `A = [1 4 0 5]; P = poly2sym(A)` → `P = x^3 + 4*x^2 + 5`. Coordenadas de P en la base $S=\{x^3,x^2,x,1\}$ de $P^3$: [1 4 0 5]; componentes: $\{x^3, 4x^2, 0, 5\}$.

#### Diapositiva 24

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Coordenadas y componentes de un vector en una base
- >> A = [1 4 0 5]
- A =
- 1     4     0     5
- >> P = poly2sym(A)
- P =
- x^3 + 4*x^2 + 5
- Coordenadas de P en la base de P3: S = {x3, x2, x, 1}
- P = [1 4 0 5]
- Componentes de P en la base S de P3
- P = {x3, 4x2, 0, 5}

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 25

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- ¿Y las componentes
- de ambos vectores?
- Coordenadas y componentes de un vector en una base
- Hallar la matriz de coordenadas de p(x) = 3x3 – 2x² + 4 en la base canónica de P3 S = {1, x, x², x3}.
- $𝑝=[4, 0, −2, 3]$
- Hallar la matriz de coordenadas de: $𝑿= −𝟏𝟒𝟑$ en la base canónica de R3:$ 𝑺=𝟏𝟎𝟎,𝟎𝟏𝟎,𝟎𝟎𝟏$
- $𝑋=−1100$+4 $010$+3 $001$
- su matriz de coordenadas en la base S es: $𝑿= −𝟏𝟒𝟑$

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos: $p(x)=3x^3-2x^2+4$ en la base canónica $\{1,x,x^2,x^3\}$ de $P_3$ → $[p]=[4,0,-2,3]$. $X=(-1,4,3)^T$ en la canónica de $\mathbb{R}^3$: $X=-1e_1+4e_2+3e_3$, matriz de coordenadas $(-1,4,3)^T$. Imagen de El Pensador con la pregunta '¿Y las componentes de ambos vectores?'.

#### Diapositiva 26

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Si S = {v1, v2, …, vn } es una base de un espacio vectorial V, todo conjunto que contenga más de n vectores es linealmente dependiente
- Base  sistema generador   ¿recuerdas la diferencia?
- Sea S1 = {u1, u2, …, um} un conjunto de m vectores de V, con m > n.
- Para probar que S1 es linealmente dependiente, debemos encontrar escalares ki (no todos cero), tales que:
- $𝑖=1𝑛𝑘𝑖𝑢𝑖=0$
- Pero como $𝑢𝑖∈𝑉$:   $𝑢𝑖=𝑐𝑗𝑖𝑣𝑗$
- Por tanto:
- $𝑖=1𝑛𝑘𝑖𝑢𝑖=0⇒𝑖=1𝑛𝑗=1𝑚𝑐𝑖𝑗𝑘𝑗𝑣𝑖=0$
- Como los vi son linealmente independientes (por ser una base):
- $𝑖=1𝑛𝑗=1𝑚𝑐𝑖𝑗𝑘𝑗=0$
- Más variables que ecuaciones:
- SEL Compatible Indeterminado.
- En consecuencia, S1 es linealmente dependiente.

_Imágenes/medios en la diapositiva: 5_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Demostración (fórmulas en imagen): $S_1=\{u_1,\dots,u_m\}$, $m>n$; buscar $k_i$ no todos nulos con $\sum k_iu_i=0$; como $u_i=\sum_j c_{ji}v_j$, $\sum_i\sum_j c_{ij}k_jv_i=0$ y, por ser los $v_i$ l.i., $\sum_j c_{ij}k_j=0$: más variables que ecuaciones ⇒ SCI ⇒ $S_1$ l.d.

#### Diapositiva 27

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Si un espacio vectorial V tiene una base formada por n vectores, toda base de V contiene exactamente n vectores.
- Sea S1 = {u1, u2, …, un} la base de V dada, y sea S2 = {v1, v2, …, vm} otra base de V.
- Como S1 es una base y S2 es linealmente independiente, por el teorema anterior, implica que m ≤ n.
- Análogamente n ≤ m porque S1 es linealmente independiente y S2 es una base. Por tanto, m = n.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 28

- BASES Y DIMENSIÓN DE UN E.V.
- UFV.ES
- Si un espacio vectorial V tiene una base formada por n vectores, se dice que V tiene dimensión n (o que es n-dimensional), y se escribe dim(V) = n.
- Si V contiene sólo el vector cero, se define como de dimensión cero.
- Criterio para bases de un espacio vectorial de tipo finito.
- Sea V un espacio vectorial de dimensión n; un sistema de n vectores B = {v1, v2,…, vn} es base sí, y sólo sí, se cumple una cualquiera de las condiciones:
- B es un sistema linealmente independiente
- B es un sistema generador (es decir, genera V).
- Si B es independiente es base, pues de lo contrario se podría encontrar una base con más de n vectores.
- Si B genera V no puede ser dependiente, pues si lo fuese habría una base con menos de n vectores.

_Imágenes/medios en la diapositiva: 1_

#### Diapositiva 29

- CAMBIO DE BASE
- CAPÍTULO 05
- 29
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 30

- CAMBIO DE BASE
- UFV.ES

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Dos gráficas: vector v en base $B_1=\{u_1=(1,0),u_2=(0,1)\}$ y en base $B_2=\{v_1=(1,3),v_2=(-1,2)\}$.

#### Diapositiva 31

- CAMBIO DE BASE
- UFV.ES
- $∀𝑥∈𝑉$
- V

_Imágenes/medios en la diapositiva: 14_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Deducción: $u_1=av_1+bv_2$, $u_2=cv_1+dv_2$ (con $(1,0)=a(1,3)+b(-1,2)$, $(0,1)=c(1,3)+d(-1,2)$); $x=x_1u_1+x_2u_2=(x_1a+x_2c)v_1+(x_1b+x_2d)v_2$ ⇒ $(x)_{B_2}=\begin{pmatrix}a&c\\b&d\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}$.

#### Diapositiva 32

- CAMBIO DE BASE
- UFV.ES
- Mismo vector
- Diferentes coordenadas
- Diferentes componentes

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Gráfica: el mismo vector x expresado en ambas bases — 'Mismo vector, diferentes coordenadas, diferentes componentes'.

#### Diapositiva 33

- CAMBIO DE BASE
- UFV.ES
- Inversa de la matriz de cambio de base.
- Si $𝑃$ es la matriz de cambio de una base $𝐵′$ a otra base $𝐵$ de $ℝ𝑛$, $𝑃$ es invertible, y la matriz del cambio de $𝐵$ a $𝐵′$ viene dada por $𝑃−1$.
- sea $𝑄$ la matriz de cambio de base de $𝐵$ a $𝐵′$.
- $[𝒗]𝐵=𝑃𝒗𝐵′$   y    $𝒗𝐵′=𝑄[𝒗]𝐵$
- $𝒗𝐵=𝑃𝑄𝒗𝐵$
- $𝑃𝑄=𝐼𝑛$
- Sean $𝐵={𝒗1, 𝒗2, …, 𝒗𝑛}$ y $𝐵′={𝒖1, 𝒖2, …, 𝒖𝑛}$ dos bases de $ℝ𝑛$. La matriz de cambio de $𝐵$ a $𝐵′$ se puede hallar aplicando el método de eliminación de Gauss-Jordan a la matriz $[𝐵′⋮𝐵]$ como sigue:
- $𝐵′⋮𝐵⟶[𝐼𝑛⋮𝑃−1]$

_Imágenes/medios en la diapositiva: 7_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $[v]_B=P[v]_{B'}$, $[v]_{B'}=Q[v]_B$ ⇒ $[v]_B=PQ[v]_B$ ⇒ $PQ=I_n$. Gauss-Jordan: $[B'\,\vdots\,B]\to[I_n\,\vdots\,P^{-1}]$.

#### Diapositiva 34

- RANGO DE UNA MATRIZ Y S.E.L.. NÚCLEO DE UNA MATRIZ
- CAPÍTULO 06
- 34
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 35

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- Sea A una matriz m x n
- Se define:
- El espacio de filas de A es el subespacio de ℝm  generado por los vectores fila de A.
- El espacio de columnas de M es el subespacio de ℝn generado por los vectores columna de A.
- Sean A y B matrices m x n. Si A es equivalente por filas a B, el espacio de filas de A es igual al espacio de filas de B.
- Si $𝐴$ es una matriz equivalente por filas a una matriz $𝐵$ escalonada por filas, los vectores fila no nulos de $𝐵$ forman una base del espacio de filas de $𝐴$
- Definición.
- Una matriz se llama escalonada por renglones o simplemente escalonada si cumple con las siguientes propiedades:
- Todos los renglones cero están en la parte inferior de la matriz.
- En cada fila, el elemento delantero diferente de cero está a la derecha del elemento delantero diferente de cero de la fila anterior.

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplos de matrices escalonada reducida, escalonada y no escalonada, con los pivotes resaltados en verde (imagen).

#### Diapositiva 36

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- Hallar una base del espacio de filas de la matriz:
- EJEMPLO
- A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2]
- GJ = rref(A)
- for i = 1:rank(A)
- B(i,:) = GJ(i,:);
- end
- B

_Imágenes/medios en la diapositiva: 4_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejemplo: base del espacio de filas de $A=\begin{pmatrix}1&3&1&3\\0&1&1&0\\-3&0&6&-1\\3&4&-2&1\\2&0&-4&-2\end{pmatrix}$. MATLAB: `A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2]; GJ = rref(A); for i = 1:rank(A) B(i,:) = GJ(i,:); end; B` → base $\{(1,0,-2,0),(0,1,1,0),(0,0,0,1)\}$.

#### Diapositiva 37

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- Hallar una base del espacio de columnas de la matriz:
- EJEMPLO
- clc; clear;
- A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2];
- At = A'
- GJt = rref(At)
- r = rank(At)
- for i = 1:rank(At)
- Bt(i,:) = GJt(i,:);
- end
- Bt
- B = Bt'
- GJt = 4×5
- 1     0     0     0    -1
- 0     1     0     4     3
- 0     0     1    -1    -1
- 0     0     0     0     0

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Base del espacio de columnas de la misma A: `At = A'; GJt = rref(At); r = rank(At); for i = 1:rank(At) Bt(i,:) = GJt(i,:); end; B = Bt'` → GJt = [1 0 0 0 −1; 0 1 0 4 3; 0 0 1 −1 −1; 0 0 0 0 0]; base de columnas $\{(1,0,0,0,-1),(0,1,0,4,3),(0,0,1,-1,-1)\}$.

#### Diapositiva 38

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- El espacio de filas y el espacio de columnas tienen la misma dimensión
- Rango de una matriz
- La dimensión del espacio de filas (o de columnas) de una matriz $𝐴$ se denomina rango de $𝐴$ y se denota por $𝑟𝑎𝑛𝑔𝑜(𝐴)$
- Pero… eso ya te lo esperabas, después de entender los ejemplos anteriores, no lo niegues

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Imagen de Einstein con bocadillo: 'Pero… eso ya te lo esperabas, después de entender los ejemplos anteriores, no lo niegues'.

#### Diapositiva 39

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- Núcleo de una matriz
- Si $𝐴$ es una matriz $𝑚 𝑥 𝑛$, el conjunto solución del sistema lineal homogéneo
- $𝐴𝒙=𝒐$
- es un subespacio de $ℝ𝑛$ que se llama núcleo de $𝑨$ y se denota por $𝑁(𝐴)$. Así pues,
- $𝑁𝐴=𝑥∈ℝ𝑛: 𝐴𝒙=𝒐$
- La dimensión de $𝑁(𝐴)$ se llama nulidad de $𝑨$.
- Dimensión del espacio de soluciones de un sistema lineal
- Si $𝐴$ es una matriz $𝑚 𝑥 𝑛$ de rango $𝑟$, la dimensión del espacio de soluciones del sistema  $𝐴𝒙=𝒐$ es $𝑛−𝑟$, esto es:
- $𝑛=𝑟𝑎𝑛𝑔𝑜𝐴+𝑛𝑢𝑙𝑖𝑑𝑎𝑑(𝐴)$

_Imágenes/medios en la diapositiva: 3_

#### Diapositiva 40

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- ESTARÁS VIENDO QUE TODO ESTO DE LOS ESPACIOS VECTORIALES SE ACABA LIANDO CON LAS MATRICES Y LOS SISTEMAS DE ECUACIONES LINEALES
- Espero que eso no te preocupe demasiado, porque estamos a un tema de liarlo aún más, con las aplicaciones lineales

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ilustración de un profesor con puntero.

#### Diapositiva 41

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- Núcleo de una matriz - utilidad
- Dada la transformación lineal:
- $𝐿:𝑉→𝑊$
- el núcleo de L es el conjunto de todos los vectores de V cuya imagen es el vector nulo de W.

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Diagrama: $L:V\to W$, con $\operatorname{Ker}(L)\subset V$ (que contiene 0) enviado al 0 de W, e $\operatorname{Im}(L)\subset W$.

#### Diapositiva 42

- RANGO DE UNA MATRIZ Y S.E.L.
- UFV.ES
- CASO PRÁCTICO
- Dada la matriz:
- $𝐴=10−2100−1−313−2−11−130390−12$
- Denotemos los vectores columna por $𝒂1, 𝒂𝟐, 𝒂3, 𝒂4, 𝒂5$
- Calcular el rango y la nulidad de $𝐴$
- Hallar un subconjunto de los vectores columna de $𝐴$ que formen base del espacio de columnas de $𝐴$.
- Escribir, si es posible, la tercera columna de $𝐴$ como combinación lineal de las dos primeras.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Caso práctico: $A=\begin{pmatrix}1&0&-2&1&0\\0&-1&-3&1&3\\-2&-1&1&-1&3\\0&3&9&0&-12\end{pmatrix}$, columnas $a_1,\dots,a_5$: a) rango y nulidad; b) subconjunto de columnas que sea base del espacio de columnas; c) escribir la tercera columna como combinación lineal de las dos primeras.

#### Diapositiva 43

- COMBINACIÓN LINEAL DE VECTORES
- CAPÍTULO 07
- 43
- UFV.ES

_Imágenes/medios en la diapositiva: 2_

#### Diapositiva 44

- COMBINACIÓN LINEAL DE VECTORES
- UFV.ES
- Una idea fundamental en álgebra lineal consiste en ver una combinación lineal de vectores como el producto de una matriz y un vector.
- Ya hemos visto cómo escribir un sistema de ecuaciones lineales como una ecuación vectorial que implica una combinación lineal de vectores.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $Ax=[a_1\ a_2\ \cdots\ a_n](x_1,\dots,x_n)^T=x_1a_1+x_2a_2+\dots+x_na_n$.

#### Diapositiva 45

- COMBINACIÓN LINEAL DE VECTORES
- UFV.ES
- Una idea fundamental en álgebra lineal consiste en ver una combinación lineal de vectores como el producto de una matriz y un vector.
- un sistema de ecuaciones lineales puede verse en tres formas diferentes, pero equivalentes:
- como una ecuación matricial,
- como una ecuación vectorial o
- como un sistema de ecuaciones lineales.

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** $Ax=b$ (4) tiene el mismo conjunto solución que $x_1a_1+\dots+x_na_n=b$ (5) y que el sistema con matriz aumentada $[a_1\ a_2\ \cdots\ a_n\ b]$ (6).

#### Diapositiva 46

- COMBINACIÓN LINEAL DE VECTORES
- UFV.ES
- El sistema de ecuaciones lineales $𝐴𝒙=𝒃$ es compatible sí, y sólo sí, $𝒃$ está en el espacio de columnas de $𝐴$ o lo que es lo mismo, $𝒃$ es combinación lineal de las columnas de $𝐴$
- Sean $𝐴=134−42−6−3−2−7$ y $𝒃=𝑏1𝑏2𝑏3$  ¿La ecuación $𝐴𝒙=𝒃$ es compatible para todos los valores de $𝑏1, 𝑏2, 𝑏3$?

_Imágenes/medios en la diapositiva: 3_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Ejercicio: $A=\begin{pmatrix}1&3&4\\-4&2&-6\\-3&-2&-7\end{pmatrix}$, $b=(b_1,b_2,b_3)^T$. ¿Es $Ax=b$ compatible para todos los valores de $b_1,b_2,b_3$?

#### Diapositiva 47

- “No supongas que la matemática es dura y avinagrada y repulsiva para el sentido común. Se trata simplemente de la idealización del sentido común.”
- William Thomson, Lord Kelvin
- Físico, matemático e ingeniero británico(1824 - 1907)
- QUOTE

_Imágenes/medios en la diapositiva: 2_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Cita sobre fondo azul con retrato de Lord Kelvin.

#### Diapositiva 48

- ESPACIOS VECTORIALES
- 91 351 03 03
- INFO@UFV.ESUFV.ES
- CTRA. POZUELO-MAJADAHONDA
- KM 1.800, 28223 POZUELO DE ALARCÓN
- MADRID. ES

_Imágenes/medios en la diapositiva: 1_

**Contenido visual (fórmulas/imágenes transcritas de la diapositiva renderizada):** Contraportada UFV 'Espacios vectoriales'.


## Pizarra · Espacios vectoriales

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - Espacios vectoriales - PIZARRA.pdf`*

#### Espacios vectoriales
*Previo (visto el 1er día como "Tema 0"): vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$, combinación lineal, dependencia e independencia lineal.*

##### Definición de espacio vectorial
Un espacio vectorial $V$ es un conjunto de elementos denominados vectores, junto con dos operaciones definidas para dichos vectores, que tienen que cumplir todos estos axiomas:
1. $x,y\in V\Rightarrow x+y\in V$ (cerradura bajo la suma).
2. $(x+y)+z=x+(y+z)$ (asociativa de la suma).
3. $\exists\,0\in V: x+0=0+x=x$ (vector cero o idéntico aditivo; elemento neutro de la suma).
4. $\forall x\in V\ \exists -x\in V: x+(-x)=0$ (vector opuesto o inverso aditivo).
5. $x+y=y+x$ (conmutativa de la suma).
6. $x\in V,\ \alpha\in\mathbb{R}\Rightarrow\alpha x\in V$ (cerradura bajo la multiplicación por un escalar).
7. $\alpha(x+y)=\alpha x+\alpha y$ (1ª ley distributiva).
8. $(\alpha+\beta)x=\alpha x+\beta x$ (2ª ley distributiva).
9. $\alpha(\beta x)=(\alpha\beta)x$ (asociativa de la multiplicación por escalares).
10. $1\cdot x=x$ (elemento neutro de la multiplicación por escalar).

##### Ejemplos de espacio vectorial
- $\{\mathbb{R}^n,+,\cdot\}$: todos los vectores con n componentes reales, con la suma y el producto por escalar habituales, elemento a elemento ($x+y=(x_1+y_1,\dots,x_n+y_n)$, $\alpha x=(\alpha x_1,\dots,\alpha x_n)$). Cumplen las 10 propiedades: ¡forman un espacio vectorial!
- $\{M_{mn},+,\cdot\}$: matrices $m\times n$ con componentes reales, suma y producto por escalar habituales. ¡Ídem!
- $\{P_n,+,\cdot\}$: polinomios de grado ≤ n con suma y producto por escalar habituales. ¡Ídem!
- $\{C[a,b],+,\cdot\}$: funciones reales continuas en $[a,b]$ con las operaciones habituales. ¡Ídem!

##### Un ejemplo que NO es un espacio vectorial: $\{M_3,\oplus,\cdot\}$
$M_3$ = matrices invertibles 3×3; $\oplus$ = "suma" definida de otra forma ("usamos este símbolo cuando la definición de suma no es la habitual"): $A\oplus B=A\cdot B$ (el producto habitual de matrices); $\cdot$ = producto por escalar habitual.
1. $A,B\in M_3\Rightarrow A\oplus B=AB\in M_3$ ✓ (el producto de dos matrices invertibles es invertible y de las mismas dimensiones).
2. $A\oplus(B\oplus C)=A(BC)=(AB)C=(A\oplus B)\oplus C$ ✓ (propiedad asociativa del producto).
3. Aquí la matriz "0" sería la identidad: $0=I_3$, $0\oplus A=IA=A$, $A\oplus0=AI=A$ ✓.
4. El opuesto se define como la inversa: $-X\equiv A^{-1}$ ⇒ $X\oplus(-X)=AA^{-1}=I=0$ ✓.
5. $A\oplus B=AB\neq BA=B\oplus A$ ✗ — ¡no se cumple! **No es E.V.**

##### Otras propiedades de los E.V.
Sea $V$ un e.v.:
- $\alpha\cdot0=0\ \forall\alpha\in\mathbb{R}$.
- $0\cdot x=0\ \forall x\in V$.
- Si $\alpha x=0\Rightarrow\alpha=0$ ó $x=0$. (Ojo, no es tan obvio; no es difícil encontrar un ejemplo — que NO es e.v. — que no lo cumpliría: $\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&-2\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ y ninguna de las matrices era cero.)
- $(-1)\cdot x=-x\ \forall x\in V$.


## Pizarra · Subespacios vectoriales

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - Subespacios vectoriales - def - PIZARRA.pdf`*

#### Subespacios vectoriales
*Recuerda que $\mathbb{R}^2=\{(x,y): x\in\mathbb{R},y\in\mathbb{R}\}$ es un espacio vectorial.*

##### Definición
Un s.e.v. es un subconjunto de un e.v. que cumple todas sus propiedades y, además, alguna "restricción" adicional. Sea $V$ un e.v.; $H$ es subespacio vectorial de $V$ si:
- $H$ es un subconjunto no vacío de $V$,
- y $H$, junto con las operaciones $+$ (suma de vectores) y $\cdot$ (producto por escalar) definidas para $V$, es también un espacio vectorial. (El subespacio "hereda" las operaciones + y · de $V$.)

##### Comprobación de subespacio vectorial
$H$ es s.e.v. de $V$ si cumple las dos "reglas de cerradura":
1. $x,y\in H\Rightarrow x+y\in H$ (la suma de vectores del s.e.v. pertenece al s.e.v., cumple sus restricciones).
2. $x\in H,\ \alpha\in\mathbb{R}\Rightarrow\alpha x\in H$ (el producto de escalar por vector del s.e.v. pertenece al s.e.v.).

Además: **todo s.e.v. contiene siempre al 0**. $H$ s.e.v. ⇒ $0\in H$ (el recíproco no es cierto): si un conjunto no contiene al 0, NO es s.e.v.; si sí lo contiene, puede ser o no ser s.e.v.

**Ejemplos:**
- $H=\{(x,y)\in\mathbb{R}^2: y=mx,\ m\in\mathbb{R}\}$: $0=(0,0)\in H$ ✓; si $v_1=(x_1,y_1)$, $v_2=(x_2,y_2)$ con $y_i=mx_i$, $v_1+v_2=(x_1+x_2,y_1+y_2)$ y $y_1+y_2=m(x_1+x_2)$ ✓; $\alpha v_1=(\alpha x_1,\alpha y_1)$ con $\alpha y_1=m(\alpha x_1)$ ✓ ⇒ **H es s.e.v. de $\mathbb{R}^2$**.
- $H=\{(x,y,z,t)\in\mathbb{R}^4: x=\beta,y=\beta,z=2\beta,t=\alpha;\ \alpha,\beta\in\mathbb{R}\}=\{(\beta,\beta,2\beta,\alpha)\}$: $0\in H$ (α = β = 0) ✓; $v_1+v_2=(\beta_1+\beta_2,\beta_1+\beta_2,2(\beta_1+\beta_2),\alpha_1+\alpha_2)\in H$ ✓; $c\,v_1=(c\beta_1,c\beta_1,2c\beta_1,c\alpha_1)\in H$ ✓ ⇒ **H es s.e.v. de $\mathbb{R}^4$**.
- $H=\{A\in M_{mn}: a_{11}=0\}$: cumple las dos condiciones (se ve fácil) ⇒ **H es s.e.v. de $M_{mn}$**.

##### Subespacio propio
Un subespacio propio de un e.v. $V$ es un s.e.v. de $V$ diferente de $\{0\}$ y de $V$.

##### Intersección de s.e.v.
La intersección de dos s.e.v. es otro s.e.v.

##### Formas de definir esas restricciones
- **Ecuaciones cartesianas:** ecuaciones que relacionan las coordenadas de los vectores de $H$. Ej.: $H=\{(x,y,z,t)\in\mathbb{R}^4: x-y=0,\ 2x-z=0\}$.
- **Ecuaciones paramétricas:** expresan cada coordenada en función de parámetros reales. Ej.: $H=\{x=\beta,\ y=\beta,\ z=2\beta,\ t=\alpha\}=\{(\beta,\beta,2\beta,\alpha):\alpha,\beta\in\mathbb{R}\}$.
- **Variedad lineal:** se da un conjunto de vectores generadores del s.e.v. Ej.: $H=L\{(0,0,0,1),(1,1,2,0),(1,1,2,1)\}$.


## Pizarra · Combinación lineal e independencia

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - Combinación lineal, independencia lineal - PIZARRA.pdf`*

#### Combinación lineal y espacio generado

##### Combinación lineal
Sean $v_1,\dots,v_n$ vectores de un e.v. Cualquier vector de la forma $v=a_1v_1+a_2v_2+\dots+a_nv_n$ ($a_i\in\mathbb{R}$, escalares) se denomina **combinación lineal** de dichos vectores.

##### Conjunto generador y espacio generado (sea V un e.v.)
$v_1,\dots,v_n\in V$ es **conjunto generador** de $V$ si cualquier $v\in V$ se puede poner como combinación lineal de ellos: $v=a_1v_1+\dots+a_nv_n\ \forall v\in V$.
- $\{(1,0,0),(0,1,0),(0,0,1)\}$ genera $\mathbb{R}^3$; $\{1,x,x^2,\dots,x^n\}$ genera $P_n$; las cuatro matrices canónicas generan $M_{22}$.
- El conjunto de todas las combinaciones lineales de $v_1,\dots,v_k$ se denomina **espacio generado** por ellos o **variedad lineal**: $\operatorname{gen}\{v_1,\dots,v_k\}=\{v: v=a_1v_1+\dots+a_kv_k\}$.
- Si $v_1,\dots,v_k\in V$ (e.v.), entonces $\operatorname{gen}\{v_1,\dots,v_k\}$ es un **s.e.v.** de $V$.

**Ejemplo:** $v_1=(2,-1,4)$, $v_2=(4,1,6)$. $H=\operatorname{gen}\{v_1,v_2\}=\{\alpha(2,-1,4)+\beta(4,1,6)\}$ (variedad lineal) $=\{(2\alpha+4\beta,\ \beta-\alpha,\ 4\alpha+6\beta)\}$ (ecuaciones paramétricas: $x=2\alpha+4\beta,\ y=\beta-\alpha,\ z=4\alpha+6\beta$).
Eliminando parámetros: $\beta=y+\alpha$; $x=6\alpha+4y\Rightarrow10x=60\alpha+40y$; $z=10\alpha+6y\Rightarrow6z=60\alpha+36y$; restando, $10x-6z=4y$ ⇒ ecuación cartesiana: $H=\{(x,y,z)\in\mathbb{R}^3: 5x-2y-3z=0\}$.

#### Independencia lineal
$v_1,\dots,v_n\in V$ son **linealmente dependientes** si existen escalares $c_1,\dots,c_n$ no todos nulos (¡alguno no nulo!) tales que $c_1v_1+\dots+c_nv_n=0$.
- Ejemplos: $v_1=(1,2)$, $v_2=(2,4)$ son l.d. porque $2v_1-v_2=0$. $v_1=(1,2,3)$, $v_2=(-4,1,5)$, $v_3=(-5,8,19)$ son l.d. porque $3v_1+2v_2-v_3=0$.

$v_1,\dots,v_n$ son **linealmente independientes** ⇔ ($c_1v_1+\dots+c_nv_n=0\Rightarrow c_1=\dots=c_n=0$).
- Dos vectores son l.d. sii uno es múltiplo del otro.
- Un conjunto de n vectores de $\mathbb{R}^m$ siempre es l.d. si $n>m$ (demo fácil: al plantear la c.l. = 0 llegamos a un sistema homogéneo de m ecuaciones con n incógnitas, $n>m$, que ya vimos que es seguro un S.C.I.).
- Un conjunto de vectores l.i. de $\mathbb{R}^n$ contiene a lo sumo n vectores.
- Sea $A$ una matriz $m\times n$: sus columnas (vectores) son l.d. sii el sistema $Ac=0$ tiene soluciones no triviales.
- Sean $v_1,\dots,v_n$ n vectores de $\mathbb{R}^n$ y $A_{n\times n}$ la matriz cuyas columnas son esos vectores: son l.i. sii la única solución de $Ax=0$ es la trivial.
- Sea $A_{n\times n}$: $|A|\neq0\iff$ las columnas (o filas) de $A$ son l.i.
- Cualquier conjunto de n vectores l.i. en $\mathbb{R}^n$ es generador de $\mathbb{R}^n$. Ej.: $(2,-1,4),(1,0,2),(3,-1,5)$ generan $\mathbb{R}^3$ porque $\begin{vmatrix}2&1&3\\-1&0&-1\\4&2&5\end{vmatrix}=-1\neq0$.

**Ejemplos:**
- $v_1=(1,2,4)$, $v_2=(2,5,-3)$: l.i. porque uno no es múltiplo del otro.
- $v_1=(1,-2,3)$, $v_2=(2,-2,0)$, $v_3=(0,1,7)$: $c_1+2c_2=0,\ -2c_1-2c_2+c_3=0,\ 3c_1+7c_3=0$ ⇒ S.C.D., $c_1=c_2=c_3=0$ ⇒ **l.i.** (la única forma de que se cumpla es con todos los $c_i=0$).
- $v_1=(1,-3,0)$, $v_2=(3,0,4)$, $v_3=(11,-6,12)$: $c_1+3c_2+11c_3=0,\ -3c_1-6c_3=0,\ 4c_2+12c_3=0$ ⇒ S.C.I. $c_1=-2\alpha,\ c_2=-3\alpha,\ c_3=\alpha$ ⇒ **l.d.** ($c_i=0$ no es la única solución).
- Tres polinomios de $P_2$: $p_1=x-2x^2$, $p_2=x^2-4x$, $p_3=-7x+8x^2$. $c_1p_1+c_2p_2+c_3p_3=0\Rightarrow(c_1-4c_2-7c_3)x+(-2c_1+c_2+8c_3)x^2=0$ ⇒ S.C.I. $c_1=\tfrac{25}7\alpha,\ c_2=-\tfrac67\alpha,\ c_3=\alpha$ ⇒ **l.d.** (admite más soluciones que la (0,0,0)).


## Pizarra · Bases y dimensión

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - Bases y dimensión - PIZARRA.pdf`*

#### Bases y dimensión

##### Base de un e.v.
Un conjunto finito de vectores $\{v_1,\dots,v_n\}$ es una **base** del e.v. $V$ si: (i) son **linealmente independientes**; (ii) es **generador** de $V$.
- Todo conjunto de n vectores l.i. en $\mathbb{R}^n$ es una base de $\mathbb{R}^n$.
- Una **base canónica** la forman vectores con una componente a 1 y el resto a 0: $\mathbb{R}^2$: $\{(1,0),(0,1)\}$; $\mathbb{R}^3$: $\{(1,0,0),(0,1,0),(0,0,1)\}$; $M_{22}$: $\left\{\begin{pmatrix}1&0\\0&0\end{pmatrix},\begin{pmatrix}0&1\\0&0\end{pmatrix},\begin{pmatrix}0&0\\1&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right\}$; $P_n$: $\{1,x,x^2,\dots,x^n\}$.
- Si $\{v_1,\dots,v_n\}$ es base de $V$, las coordenadas de cualquier $v\in V$ respecto de esa base son únicas: $\exists!\,c_1,\dots,c_n\in\mathbb{R}$ con $v=c_1v_1+\dots+c_nv_n\ \forall v\in V$.
- Cualesquiera dos bases de un e.v. $V$ tienen el mismo número de vectores.

##### Dimensión de un e.v.
La dimensión de $V$ es el número de vectores de todas las bases de $V$.
- E.v. de dimensión finita vs. de dimensión infinita. $V=\{0\}\Rightarrow\dim V=0$.
- Ejemplos: $\dim\mathbb{R}^n=n$; $\dim P_n=n+1$; $\dim M_{mn}=m\cdot n$.
- Si $\dim V=n$, un conjunto de vectores l.i. de $V$ tiene a lo sumo n vectores (más de n no pueden ser l.i.): $u_1,\dots,u_m$ l.i. ⇒ $m\le n$.
- Cualquier conjunto de n vectores l.i. en un e.v. de dimensión n constituye una base.

##### Dimensión de un s.e.v. (misma definición que en e.v.)
- Si $V$ es de dimensión finita, cualquier s.e.v. $H\subseteq V$ tiene dimensión finita y $\dim H\le\dim V$.
- Cualquier e.v. que contiene un s.e.v. de dimensión infinita es de dimensión infinita: $\dim H=\infty\Rightarrow\dim V=\infty$.
- Un s.e.v. dado por **ecuaciones cartesianas** en $\mathbb{R}^n$ (también llamados "espacios de solución de un sistema homogéneo" o "espacios nulos"): los únicos subespacios propios de $\mathbb{R}^n$ son conjuntos de vectores solución de un sistema homogéneo, es decir, vienen dados siempre por ecuaciones cartesianas que forman sistemas $Ax=0$. (En $\mathbb{R}^3$ esto se traduce en que son rectas o planos que pasan por el origen.)
  - $\dim H=\dim V-$ nº ecuaciones cartesianas l.i. $=$ nº incógnitas $-$ nº ecuaciones cartesianas l.i. $=$ nº parámetros (al resolver el sistema para pasar a paramétricas).

##### Base de un s.e.v.
Misma definición, pero con una forma especial de obtenerse. Ejemplo: $H=\{(x,y,z): 2x-y+z=0\}$ (ecuaciones cartesianas).
- Resuelvo el sistema: 1 ecuación, 3 incógnitas ⇒ 2 parámetros: $x=\alpha,\ y=2\alpha+\beta,\ z=\beta$ (ecuaciones paramétricas).
- Forma paramétrica: $H=\{(\alpha,2\alpha+\beta,\beta): \alpha,\beta\in\mathbb{R}\}$.
- Dando valores: $\alpha=1,\beta=0\to(1,2,0)$; $\alpha=0,\beta=1\to(0,1,1)$. $\{(1,2,0),(0,1,1)\}$ es base de $H$ porque son l.i. (dos vectores no proporcionales) y generan $H$: $v=\alpha(1,2,0)+\beta(0,1,1)=(\alpha,2\alpha+\beta,\beta)$.
- Así, $H=\operatorname{gen}\{(1,2,0),(0,1,1)\}$ (**variedad lineal** o espacio generado).

**Ejemplo:** base y dimensión del espacio solución $S$ de $x+2y-z=0,\ 2x-y+3z=0$ (subespacio de $\mathbb{R}^3$ porque hay tres incógnitas).
$e_2\to e_2-2e_1$: $-5y+5z=0$; $e_2\to-\tfrac15e_2$: $y-z=0$ (sistema escalonado, ecuaciones l.i.); $e_1\to e_1-2e_2$: $x+z=0$. S.C.I. con un parámetro: $x=-\alpha,\ y=\alpha,\ z=\alpha$.
$S=\{(-\alpha,\alpha,\alpha):\alpha\in\mathbb{R}\}=\operatorname{gen}\{(-1,1,1)\}$, $\dim S=1$; una base (α = 1): $\{(-1,1,1)\}$.


## Pizarra · Cambio de base

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - Cambio de base en e.v - PIZARRA.pdf`*

#### Base canónica vs. otra base
- $B_c=\{(1,0),(0,1)\}$: $(v)_{B_c}=(7,1)=7(1,0)+1(0,1)$.
- $B=\{(2,1),(1,3)\}$: ¿$(v)_B$? $(v)_B=(4,-1)$ porque $4(2,1)-1(1,3)=(7,1)$. ¿Cómo hacemos eso rápido? Matricialmente: $\begin{pmatrix}1&0\\0&1\end{pmatrix}\begin{pmatrix}7\\1\end{pmatrix}=\begin{pmatrix}2&1\\1&3\end{pmatrix}\begin{pmatrix}4\\-1\end{pmatrix}$.
- En general (escribiendo cada base como matriz con los vectores en columnas): $B_c\cdot(v)_{B_c}=B\cdot(v)_B$ ⇒ $(v)_{B_c}=B_c^{-1}B\,(v)_B=B\,(v)_B$ y $(v)_B=B^{-1}(v)_{B_c}$.
- Matrices de cambio de base: $C_B^{B_c}=B$ (de $B$ a $B_c$) y $C_{B_c}^{B}=B^{-1}$ (de $B_c$ a $B$).

#### Dos bases cualesquiera
$B_1(v)_{B_1}=B_2(v)_{B_2}$ ⇒ $(v)_{B_1}=B_1^{-1}B_2(v)_{B_2}$ y $(v)_{B_2}=B_2^{-1}B_1(v)_{B_1}$. Es decir, $C_{B_2}^{B_1}=B_1^{-1}B_2$ y $C_{B_1}^{B_2}=B_2^{-1}B_1$.

#### Ejercicio
Sean $B_c=\{(1,0,0),(0,1,0),(0,0,1)\}$ y $B=\{(1,1,0),(0,2,1),(1,0,2)\}$.
- **a)** Matrices de cambio de base: $C_B^{B_c}=B=\begin{pmatrix}1&0&1\\1&2&0\\0&1&2\end{pmatrix}$; $C_{B_c}^{B}=B^{-1}=\tfrac15\begin{pmatrix}4&1&-2\\-2&2&1\\1&-1&2\end{pmatrix}$ *(inversa recalculada; en la pizarra los signos de algunas entradas son poco legibles)*.
- **b)** $v=(3,-1,2)$ en la base $B$ ⇒ $(v)_{B_c}=B(v)_B=(5,1,3)$.
- **c)** $v=(5,1,3)$ en la canónica ⇒ $(v)_B=B^{-1}(v)_{B_c}=\tfrac15(15,-5,10)=(3,-1,2)$.


## Pizarra · Rango, nulidad, espacio fila y columna

*Fuente: `GRUPO A/TEMA 4 - Espacios Vectoriales/MPI1 - Tema 4 - rango, nulidad, espacio fila, espacio columna.pdf`*

#### Rango, nulidad, espacio fila, espacio columna

##### Espacio nulo y nulidad de una matriz (sea $A_{m\times n}$)
- **Espacio nulo:** $N_A=\{x\in\mathbb{R}^n: Ax=0\}$ — es un s.e.v. de $\mathbb{R}^n$.
- **Nulidad:** $\nu(A)=\dim(N_A)$. Si la única solución de $Ax=0$ es $(0,0,0)$, entonces $\nu(A)=0$ (el s.e.v. sólo contiene el vector 0).

**Ejemplo 1:** $A=\begin{pmatrix}1&2&-1\\2&-1&3\end{pmatrix}$ (2×3). $Ax=0$: $x+2y-z=0,\ 2x-y+3z=0$ → $e_2\to e_2-2e_1$: $-5y+5z=0$ → $e_2\to-\tfrac15e_2$: $y-z=0$ ⇒ $x=-\alpha,\ y=\alpha,\ z=\alpha$.
$N_A=\{(-\alpha,\alpha,\alpha)\}=\operatorname{gen}\{(-1,1,1)\}$, $\nu(A)=1$; una base (α = 1): $(-1,1,1)$.

**Ejemplo 2:** $A=\begin{pmatrix}2&-1&3\\4&-2&6\\-6&3&-9\end{pmatrix}$: ¡son filas l.d.! (veo a ojo que las tres filas son proporcionales). Queda $2x-y+3z=0$ ⇒ $x=\alpha,\ y=2\alpha+3\beta,\ z=\beta$; $\nu(A)=2$; base: α=1, β=0 → $(1,2,0)$; α=0, β=1 → $(0,3,1)$.
$N_A=\{(\alpha,2\alpha+3\beta,\beta)\}=\operatorname{gen}\{(1,2,0),(0,3,1)\}$.

- Sea $A_{n\times n}$: $A$ invertible ⇔ $\nu(A)=0$ (¡claro! A invertible sii $Ax=0$ sólo tiene la solución trivial).

##### Imagen y rango de una matriz (sea $A_{m\times n}$)
- **Imagen:** $\operatorname{im}(A)=\{y\in\mathbb{R}^m: Ax=y \text{ para algún } x\in\mathbb{R}^n\}$ — ¡es un s.e.v. de $\mathbb{R}^m$!
- **Rango:** $\operatorname{rg}(A)=\dim(\operatorname{im}A)$ (también lo veréis como $\rho(A)$).
- $\operatorname{rg}(A)$ = nº de pivotes en su forma escalonada por filas.
- $\operatorname{rg}(A)+\nu(A)=n$ (nº de columnas de $A$).
- $A_{n\times n}$ invertible ⇔ $\operatorname{rg}(A)=n$ (¡claro, cuando $\nu(A)=0$!).

##### Espacio fila y espacio columna
Con $A_{m\times n}$ de filas $f_1,\dots,f_m$ y columnas $c_1,\dots,c_n$:
- **Espacio fila:** $F_A=\operatorname{gen}\{f_1,\dots,f_m\}$.
- **Espacio columna:** $C_A=\operatorname{gen}\{c_1,\dots,c_n\}=\operatorname{im}(A)$.
- $\dim F_A=\dim C_A=\dim\operatorname{im}(A)=\operatorname{rg}(A)$.
- $A,B$ equivalentes por filas ⇒ $F_A=F_B$, $\operatorname{rg}A=\operatorname{rg}B$, $\nu(A)=\nu(B)$.
- $Ax=b$ compatible ⇔ $b\in C_A$ ⇔ $\operatorname{rg}(A)=\operatorname{rg}(A,b)$ (matriz ampliada) — **¡Teorema de Rouché!**

**Ejemplo:** $A=\begin{pmatrix}1&2&-1\\2&-1&3\end{pmatrix}$, obtener $\operatorname{im}(A)$, $\operatorname{rg}(A)$, $F_A$, $C_A$ (ya teníamos $N_A=\operatorname{gen}\{(-1,1,1)\}$, $\nu(A)=1$).
- Imagen (y espacio columna): $\operatorname{im}(A)=C_A=\operatorname{gen}\{(1,2),(2,-1),(-1,3)\}=\mathbb{R}^2$ (son vectores de $\mathbb{R}^2$; los dos primeros son l.i., y 2 vectores l.i. de $\mathbb{R}^2$ son base y por tanto generan todo $\mathbb{R}^2$).
- Rango: $\operatorname{rg}(A)=\dim\operatorname{im}(A)=2$.
- Espacio fila: $F_A=\operatorname{gen}\{(1,2,-1),(2,-1,3)\}$ (dos vectores no proporcionales ⇒ l.i. ⇒ $\dim F_A=2$; además ya sabíamos que $\dim F_A=\dim C_A$). Como $\dim F_A=2=\dim\mathbb{R}^3-$ nº ecuaciones l.i., buscamos UNA ecuación: $(x,y,z)=\alpha(1,2,-1)+\beta(2,-1,3)$ ⇒ $x=\alpha+2\beta,\ y=2\alpha-\beta,\ z=-\alpha+3\beta$; $\beta=2\alpha-y$ ⇒ $x=5\alpha-2y$, $z=5\alpha-3y$ ⇒ $x-z=y$.
$$F_A=\operatorname{gen}\{(1,2,-1),(2,-1,3)\}=\{(\alpha+2\beta,2\alpha-\beta,-\alpha+3\beta)\}=\{(x,y,z)\in\mathbb{R}^3: x-y-z=0\}$$


## Live Script: cambio de base

*Fuente: `EV_01_R02.mlx`*

###  [Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

### ESPACIOS VECTORIALES - CAMBIO DE BASE

- Table of Contents

- Teoría · Problema 1 - Cambio de base ·     Solución · Problema 2 - Cambio de base ·     Solución · Problema 3 - Cambio de base ·     Solución · Problema 4 - Cambio de base ·     Solución · Problema 5 - Cambio de base ·     Solución · Problema 6 - Espacio de filas ·     Solución · Problema 7 - Espacio de columnas ·     Solución

#### Teoría

Supongamos que tenemos dos bases de un espacio vectorial (para simplificar utilizaremos $R^3$), B1 = {u1, u2, u3} y B2 = {v1, v2, v3}, y que queremos establecer un cambio de base de B1 a B2, esto es, si tenemos un vector x en B1, queremos representarlo en B2 por medio de una matriz de transición (de cambio de base) que denominamos A:

$${\left(x\right)}_{\textrm{B2}} =A\cdot {\left(x\right)}_{\textrm{B1}}$$

La matriz se obtiene obteniendo los vectores de B1 en B2:

$$u_j =a_{1j} \cdot v_1 +a_{2j} \cdot v_2 +a_{3j} \cdot v_3 =\sum_{i=1}^3 a_{\textrm{ij}} \cdot v_i$$

Y entonces:

$$A=\left\lbrack \begin{array}{ccc}
a_{11}  & a_{12}  & a_{13} \\
a_{21}  & a_{22}  & a_{23} \\
a_{31}  & a_{32}  & a_{33}
\end{array}\right\rbrack =\left\lbrack \begin{array}{ccc}
{\left(u_1 \right)}_{B_2 }  & {\left(u_2 \right)}_{B_2 }  & {\left(u_3 \right)}_{B_2 }
\end{array}\right\rbrack$$

Con esta matriz, el cambio de base será:

$${\left(x\right)}_{B_2 } =A\cdot {\left(x\right)}_{B_1 }$$

Y el inverso:

$${\left(x\right)}_{B_1 } =A^{-1} \cdot {\left(x\right)}_{B_2 }$$

#### Problema 1 - Cambio de base

Grossman, S.I.; Flores, J.J. (2020): Algebra lineal. Octava edición. Mc Graw - Hill. Ejemplo 5.6

Se considera la base canónica de R²: $B_1 =\left\lbrace u_1 ,u_2 \right\rbrace$, donde son:

$$\begin{array}{l}
u_1 =\left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack \\
u_2 =\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack
\end{array}$$

Se consideran dos vectores $v_1$ y $v_2$, definidos como:

$$\begin{array}{l}
v_1 =\left\lbrack \begin{array}{c}
1\\
3
\end{array}\right\rbrack \\
v_2 =\left\lbrack \begin{array}{c}
-1\\
2
\end{array}\right\rbrack
\end{array}$$

SE PIDE:

- Demostrar que $B_2 =\left\lbrace v_1 ,v_2 \right\rbrace$ es una base de R²

- Encontrar la matriz de cambio de base $B_1 \to B_2$

- Encontrar la matriz de cambio de base $B_2 \to B_1$

- Dado el vector $x_{B_1 } =\left\lbrack \begin{array}{c}
x_1 \\
x_2
\end{array}\right\rbrack$, encontrar el vector $x_{B_2 }$

- Dado el vector $V_{B_1 } =\left\lbrack \begin{array}{c}
3\\
-4
\end{array}\right\rbrack$, encontrar el vector $V_{B_2 }$

Solución

Las coordenadas de los vectores de ambas bases están dadas en una base genérica, común para ambas.

Comprobaremos si v1 y v2 son linealmente independientes, en cuyo caso serán un sistema generador de R² y por tanto, una base:

```matlab
clear; clc;
mB2 = [1 -1;3 2]
detmB2 = det(mB2)
```

**Salida:**
```text
mB2 =
1  -1
3  2
detmB2 =
```

Vemos que la matriz mB2 es regular, por lo que sus columnas (y por tanto los vectores v1 y v2) son linealmente independientes; como consecuencia, B2 es base de R².

Lo que se nos está pidiendo en el segundo apartado es encontrar la matriz de cambio de base de B1 a B2. Dado que ambas son bases de R² se cumple para todo vector $x\;\epsilon \;R^2$:

$$x=x_1 \cdot u_1 +x_2 \cdot u_2 =y_1 \cdot v_1 +y_2 \cdot v_2$$

Es decir, $x_i$ son las coordenadas de x en la base B1 e $y_i$ son las coordenadas de x en la base B2.

Dado que B2 tambien es base de R², escribiremos los vectores de B1 en la base B2:

$$\begin{array}{l}
u_1 =a\cdot v_1 +b\cdot v_2 \to \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack =a\left\lbrack \begin{array}{c}
1\\
3
\end{array}\right\rbrack +b\left\lbrack \begin{array}{c}
-1\\
2
\end{array}\right\rbrack \\
u_2 =c\cdot v_1 +d\cdot v_2 \to \left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack =c\left\lbrack \begin{array}{c}
1\\
3
\end{array}\right\rbrack +d\left\lbrack \begin{array}{c}
-1\\
2
\end{array}\right\rbrack
\end{array}$$

Desarrollando el sistema de ecuaciones anterior:

$$\begin{array}{l}
\textrm{u1x}=a\cdot \textrm{v1x}+b\cdot \textrm{v2x}\\
\textrm{u1y}=a\cdot \textrm{v1y}+b\cdot \textrm{v2y}\\
\textrm{u2x}=c\cdot \textrm{v1x}+d\cdot \textrm{v2x}\\
\textrm{u2y}=c\cdot \textrm{v1y}+d\cdot \textrm{v2y}
\end{array}$$

Podemos escribir este sistema de ecuaciones como:

$$\left\lbrack \begin{array}{cc}
1 & 0\\
0 & 1
\end{array}\right\rbrack =\left\lbrack \begin{array}{cc}
1 & -1\\
3 & 2
\end{array}\right\rbrack \left\lbrack \begin{array}{cc}
a & c\\
b & d
\end{array}\right\rbrack$$

O sea:

$$\left\lbrack \begin{array}{cc}
u_1  & u_2
\end{array}\right\rbrack =\left\lbrack \begin{array}{cc}
v_1  & v_2
\end{array}\right\rbrack \left\lbrack \begin{array}{cc}
a & c\\
b & d
\end{array}\right\rbrack$$

Hallamos los coeficientes a, b, c y d por medio de un sistema de ecuaciones lineales. En otras palabras, vemos que la matriz de cambio de base, también denominada matriz de transición, está formada, por columnas, por las coordenadas de los vectores de la base actual (B1) en la nueva base (B2), ordenadas en el mismo orden que tienen los vectores en la base B1.

Por otra parte:

$$\begin{array}{l}
x=x_1 \cdot u_1 +x_2 \cdot u_2 =x_1 \cdot \left(a\cdot v_1 +b\cdot v_2 \right)+x_2 \cdot \left(c\cdot v_1 +d\cdot v_2 \right)=\\
=\left(x_1 \cdot a+x_2 \cdot c\right)\cdot v_1 +\left(x_1 \cdot b+x_2 \cdot d\right)\cdot v_2
\end{array}$$

De aquí que las coordenadas del vector x en ambas bases son:

$$\begin{array}{l}
{\left(x\right)}_{\textrm{B1}} =\left\lbrack \begin{array}{c}
x_1 \\
x_2
\end{array}\right\rbrack \\
{\left(x\right)}_{\textrm{B2}} =\left\lbrack \begin{array}{c}
a\cdot x_1 +c\cdot x_2 \\
b\cdot x_1 +d\cdot x_2
\end{array}\right\rbrack =\left\lbrack \begin{array}{cc}
a & c\\
b & d
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
x_1 \\
x_2
\end{array}\right\rbrack
\end{array}$$

```matlab
syms a b c d
u1 = [1;0]
u2 = [0;1]
v1 = [1;3]
v2 = [-1;2]

ecs1 = u1 == a*v1 + b*v2
ecs2 = u2 == c*v1 + d*v2

ecs = [ecs1;ecs2]

sol = solve(ecs,[a b c d])

MCB = [sol.a sol.c;sol.b sol.d]
```

**Salida:**
```text
u1 =
u2 =
v1 =
v2 =
-1
ecs1 = ([1=a-b; 0=3⁢a+2⁢b])
ecs2 = ([0=c-d; 1=3⁢c+2⁢d])
ecs = ([1=a-b; 0=3⁢a+2⁢b; 0=c-d; 1=3⁢c+2⁢d])
sol = struct with fields:
a: 2/5
b: -3/5
c: 1/5
d: 1/5
MCB = ([(2)/(5), (1)/(5); -(3)/(5), (1)/(5)])
```

Vamos a comprobar si se cumple:

$$\begin{array}{l}
u_1 =\textrm{MCB}\cdot v_1 \\
u_2 =\textrm{MCB}\cdot v_2
\end{array}$$

```matlab
uu1 = MCB*v1
uu2 = MCB*v2

if u1 == uu1 & u2 == uu2
    disp('Perfecto')
else
    disp('Fracasaste, Morgan')
end
```

**Salida:**
```text
uu1 = ([1; 0])
uu2 = ([0; 1])
Perfecto
```

Y a la inversa, para hallar las coordenadas en la nueva base B2:

$$\begin{array}{l}
{\textrm{MCB}}^{-1} \cdot u_1 =v_1 \\
{\textrm{MCB}}^{-1} \cdot u_2 =v_2
\end{array}$$

Verifiquemos:

```matlab
vv1 = inv(MCB)*u1
vv2 = inv(MCB)*u2

if v1 == vv1 & v2 == vv2
    disp('Perfecto')
else
    disp('Fracasaste, Morgan')
end
```

**Salida:**
```text
vv1 = ([1; 3])
vv2 = ([-1; 2])
Perfecto
```

El vector $x_{\mathrm{B1}} =\left\lbrack \begin{array}{c}
x_1 \\
x_2
\end{array}\right\rbrack$ en B2 será:

```matlab
syms x1 x2
xb2 = MCB*[x1;x2]
```

**Salida:**
```text
xb2 = ([(2⁢x_1)/(5)+(x_2)/(5); (x_2)/(5)-(3⁢x_1)/(5)])
```

Veamos el vector $V_{\textrm{B1}} =\left\lbrack \begin{array}{c}
3\\
-4
\end{array}\right\rbrack$:

```matlab
Vb1 = [3;-4]
Vb2 = MCB*Vb1
```

**Salida:**
```text
Vb1 =
-4
Vb2 = ([(2)/(5); -(13)/(5)])
```

Lo vemos con el resultado genérico anterior (xB2):

```matlab
Vb2_1 = subs(xb2,[x1 x2],[3 -4])
```

**Salida:**
```text
Vb2_1 = ([(2)/(5); -(13)/(5)])
```

Volver al índice

#### Problema 2 - Cambio de base

Dibujar gráficas con los vectores del problema 1.

Solución

```matlab
clear; clc;
```

Dibujamos el vector V en la base B1:

```matlab
u1 = [1;0];
u2 = [0;1];
Vb1 = [3;-4];

fig = figure;
xline(0)
hold on
yline(0)
quiver(0,0,u1(1),u1(2),1,'r','LineWidth',2)
quiver(0,0,u2(1),u2(2),1,'r','LineWidth',2)
quiver(0,0,Vb1(1),Vb1(2),1,'b','LineWidth',2)
grid on
ylim([-6 4])
axis equal
plot([3 3], [-4 0],':b')
plot([3 0], [-4 -4],':b')
text(1,0.2,'u_1')
text(0.2,1,'u_2')
text(1.8,-3,'V')
title('VECTORES EN BASE B1')
```

**Salida:**
```text
[figura]
```

Ahora hacemos lo mismo en la base B2:

```matlab
v1 = [1;3];
v2 = [-1;2];
Vb2 = [2/5;-13/5];

fig = figure;
xline(0)
hold on
yline(0)
quiver(0,0,u1(1),u1(2),1,'k','LineWidth',2)
quiver(0,0,u2(1),u2(2),1,'k','LineWidth',2)
quiver(0,0,v1(1),v1(2),1,'r','LineWidth',2)
quiver(0,0,v2(1),v2(2),1,'r','LineWidth',2)
quiver(0,0,Vb1(1),Vb1(2),1,'b','LineWidth',2)
grid on
ylim([-6 4])
axis equal
plot([Vb2(1)*v1(1) 3],[Vb2(1)*v1(2) -4],':k')
plot([0 Vb2(2)*v2(1)],[0 Vb2(2)*v2(2)],'--k')
plot([Vb2(2)*v2(1) 3],[Vb2(2)*v2(2),-4],':k')
text(1,0.2,'u_1')
text(0.2,1,'u_2')
text(v1(1),v1(2),'v_1')
text(v2(1),v2(2),'v_2')
text(1.8,-3,'V')
title('VECTORES EN BASE B2')
```

**Salida:**
```text
[figura]
```

Volver al índice

#### Problema 3 - Cambio de base

Grossman, S.I.; Flores, J.J. (2020): Algebra lineal. Octava edición. Mc Graw - Hill. Ejemplo 5.6.1

En $R^3$se tiene la base canónica $B_1 =\left\lbrack \vec{i} ,\vec{j} ,\vec{k} \right\rbrack$ y un conjunto de tres vectores de $R^3$:

$B_2 =\left\lbrace \left\lbrack \begin{array}{c}
1\\
0\\
2
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
3\\
-1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
1\\
-2
\end{array}\right\rbrack \right\rbrace$. Se tiene un vector $x\;\epsilon \;R^3$ cuyas coordenadas en B1 son ${\left(x\right)}_{B_1 } =\left\lbrack \begin{array}{c}
x\\
y\\
z
\end{array}\right\rbrack$. Se pide encontrar las coordenadas ${\left(x\right)}_{B_2 }$.

Solución

En primer lugar, comprobaremos que los vectores de B2 son linealmente independientes. Dado que son tres, cumpliendo esa condición, sabemos que constituyen un sistema generador, y por tanto, serán una base de $R^3$.

```matlab
clear; clc;
u1 = [1;0;0];
u2 = [0;1;0];
u3 = [0;0;1];
v1 = [1;0;2];
v2 = [3;-1;0];
v3 = [0;1;-2];
mB2 = [v1 v2 v3]
detMB2 = det(mB2)
```

**Salida:**
```text
mB2 =
1  3  0
0  -1  1
2  0  -2
detMB2 =
```

Dado que $|\textrm{mB2}|\not= 0$, los vectores de B2 son linealmente independientes, y B2 es una base de $R^3$.

Construimos la matriz inv_MCB con las componentes de los vectores de B2 expresados en B1:

```matlab
inv_MCB = mB2
MCB = inv(mB2)
```

**Salida:**
```text
inv_MCB =
1  3  0
0  -1  1
2  0  -2
MCB =
0.2500  0.7500  0.3750
0.2500  -0.2500  -0.1250
0.2500  0.7500  -0.1250
```

El cambio de coordenadas del vector x será:

$${\left(x\right)}_{B_2 } =\textrm{MCB}\cdot {\left(x\right)}_{B_1 }$$

```matlab
syms x y z
xB1 = [x;y;z]
xB2 = MCB*xB1
```

**Salida:**
```text
xB1 = ([x; y; z])
xB2 = ([(x)/(4)+(3⁢y)/(4)+(3⁢z)/(8); (x)/(4)-(y)/(4)-(z)/(8); (x)/(4)+(3⁢y)/(4)-(z)/(8)])
```

En el caso del vector ${\left(x\right)}_{B_1 } =\left\lbrack \begin{array}{c}
1\\
-2\\
4
\end{array}\right\rbrack$, se tiene:

```matlab
xB1 = [1;-2;4]
xB2 = MCB*xB1
```

**Salida:**
```text
xB1 =
-2
xB2 =
0.2500
0.2500
-1.7500
```

Verificamos este resultado:

```matlab
X2 = xB2(1)*v1 + xB2(2)*v2 + xB2(3)*v3
X1 = X2(1)*u1 + X2(2)*u2 + X2(3)*u3
```

**Salida:**
```text
X2 =
-2
X1 =
-2
```

Es decir, la forma de establecer el cambio de base es la siguiente:

- Se construye la matriz de cambio de base a partir de los vectores que componen la primera base B1, en términos de la segunda base B2. Se obtiene la matriz A.

- La transformación de un vector x será ${\left(x\right)}_{\textrm{B2}} =A\cdot {\left(x\right)}_{\textrm{B1}}$

Esto es equivalente a:

- Se construye la matriz de cambio de base a partir de los vectores que componen la segunda base B2, en términos de la primera base B1. Se obtiene la matriz $A^{-1}$.

- La transformación de un vector x será ${\left(x\right)}_{\textrm{B2}} =A\cdot {\left(x\right)}_{\textrm{B1}}$

En este problema hemos hecho el cambio de base de la segunda forma, dado que se tenía la base B2 en términos de la primera, B1.

Comprobamos cómo se puede obtener B1 a partir de B2:

```matlab
MCB*[v1 v2 v3]
```

**Salida:**
```text
ans =
1  0  0
0  1  0
0  0  1
```

Volver al índice

#### Problema 4 - Cambio de base

Repetir el problema anterior, pero esta vez encontrando la base 1 en términos de la B2.

Solución

```matlab
clear; clc;
```

Lo primero es obtener la base B1 en términos de B2:

$$\begin{array}{l}
u_1 =x_{11} \cdot v_1 +x_{21} \cdot v_2 +x_{31} \cdot v_3 =\sum_{i=1}^3 x_{\textrm{i1}} \cdot v_i \\
u_2 =x_{12} \cdot v_1 +x_{22} \cdot v_2 +x_{32} \cdot v_3 =\sum_{i=1}^3 x_{\textrm{i2}} \cdot v_i \\
u_3 =x_{13} \cdot v_1 +x_{23} \cdot v_2 +x_{33} \cdot v_3 =\sum_{i=1}^3 x_{\textrm{i3}} \cdot v_i \;
\end{array}$$

O, lo que es lo mismo:

$$u_j =$$$$\sum_{i=1}^3 x_{\textrm{ij}} \cdot v_i \;\;\;\;\;\;\;\;j=1,2,3$$

Iniciamos el cálculo simbólico e introducimos los vectores:

```matlab
syms x11 x12 x13 x21 x22 x23 x31 x32 x33
u1 = [1;0;0];
u2 = [0;1;0];
u3 = [0;0;1];
v1 = [1;0;2];
v2 = [3;-1;0];
v3 = [0;1;-2];
```

Planteamos el sistema de ecuaciones:

```matlab
ecs1 = u1 == x11*v1 + x21*v2 + x31*v3;
ecs2 = u2 == x12*v1 + x22*v2 + x32*v3;
ecs3 = u3 == x13*v1 + x23*v2 + x33*v3;
ecs = [ecs1;ecs2;ecs3]

sol = solve(ecs)
```

**Salida:**
```text
ecs = ([1=x_11+3⁢x_21; 0=x_31-x_21; 0=2⁢x_11-2⁢x_31; 0=x_12+3⁢x_22; 1=x_32-x_22; 0=2⁢x_12-2⁢x_32; 0=x_13+3⁢x_23; 0=x_33-x_23; 1=2⁢x_13-2⁢x_33])
sol = struct with fields:
x11: 1/4
x12: 3/4
x13: 3/8
x21: 1/4
x22: -1/4
x23: -1/8
x31: 1/4
x32: 3/4
x33: -1/8
```

La matriz de cambio de base será, entonces (recuerda que los vectores ui en la base B2 tienen que ser las columnas de la matriz de transición):

```matlab
A = [sol.x11 sol.x12 sol.x13;sol.x21 sol.x22 sol.x23;sol.x31 sol.x32 sol.x33]
```

**Salida:**
```text
A = ([(1)/(4), (3)/(4), (3)/(8); (1)/(4), -(1)/(4), -(1)/(8); (1)/(4), (3)/(4), -(1)/(8)])
```

Aplicando esta matriz a la base B2 se debería obtener la B1:

```matlab
A*[v1 v2 v3]
```

**Salida:**
```text
ans = ([1, 0, 0; 0, 1, 0; 0, 0, 1])
```

Como, en efecto, ocurre.

Volver al índice

#### Problema 5 - Cambio de base

Grossman, S.I.; Flores, J.J. (2020): Algebra lineal. Octava edición. Mc Graw - Hill. Ejemplo 5.6.3

Sean $B_1 =\left\lbrace \left\lbrack \begin{array}{c}
3\\
1
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
2\\
-1
\end{array}\right\rbrack \right\rbrace$ y $B_2 =\left\lbrace \left\lbrack \begin{array}{c}
2\\
4
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-5\\
3
\end{array}\right\rbrack \right\rbrace$ dos bases en $R^2$. Estas bases están referidas a la base canónica.

- Si se tiene ${\left(x\right)}_{B_1 } =\left\lbrack \begin{array}{c}
b_1 \\
b_2
\end{array}\right\rbrack$, expresa x en término de los vectores de B2.

- Si se tiene $x=\left\lbrack \begin{array}{c}
7\\
4
\end{array}\right\rbrack$ en la base canónica, obtener ${\left(x\right)}_{B_1 }$.

Solución

Como queremos pasar de B1 a B2, debemos expresar los vectores de B1 como combinación lineal de los de B2. Llamaremos $B_1 =\left\lbrace u_1 ,u_2 \right\rbrace$ y $B_2 =\left\lbrace v_1 ,v_2 \right\rbrace$:

$$\begin{array}{l}
u_1 =a_{11} \cdot v_1 +a_{21} \cdot v_2 \\
u_2 =a_{12} \cdot v_1 +a_{22} \cdot v_2
\end{array}$$

Y las matriz de transición será:

$$A=\left\lbrack \begin{array}{cc}
a_{11}  & a_{12} \\
a_{21}  & a_{22}
\end{array}\right\rbrack$$

Primero, comprobamos que, en efecto, se trata de dos bases:

```matlab
clear; clc;
u1 = [3;1]
u2 = [2;-1]
B1 = [u1 u2]
v1 = [2;4]
v2 = [-5;3]
B2 = [v1 v2]
det(B1)
det(B2)
```

**Salida:**
```text
u1 =
u2 =
-1
B1 =
3  2
1  -1
v1 =
v2 =
-5
B2 =
2  -5
4  3
ans =
-5
ans =
```

En efecto, se trata de dos bases, porque los vectores son linealmente independientes, y al ser dos vectores en $R^2$, linealmente independientes, constituyen un sistema generador. Seguimos:

```matlab
syms a11 a12 a21 a22
ecs1 = u1 == a11*v1 + a21*v2
ecs2 = u2 == a12*v1 + a22*v2
ecs = [ecs1;ecs2]
sol = solve(ecs)
```

**Salida:**
```text
ecs1 = ([3=2⁢a_11-5⁢a_21; 1=4⁢a_11+3⁢a_21])
ecs2 = ([2=2⁢a_12-5⁢a_22; -1=4⁢a_12+3⁢a_22])
ecs = ([3=2⁢a_11-5⁢a_21; 1=4⁢a_11+3⁢a_21; 2=2⁢a_12-5⁢a_22; -1=4⁢a_12+3⁢a_22])
sol = struct with fields:
a11: 7/13
a12: 1/26
a21: -5/13
a22: -5/13
```

Por tanto:

```matlab
A = [sol.a11 sol.a12;sol.a21 sol.a22]
```

**Salida:**
```text
A = ([(7)/(13), (1)/(26); -(5)/(13), -(5)/(13)])
```

Y el vector x en la base B2 será:

```matlab
syms b1 b2
A*[b1;b2]
```

**Salida:**
```text
ans = ([(7⁢b_1)/(13)+(b_2)/(26); -(5⁢b_1)/(13)-(5⁢b_2)/(13)])
```

Para expresar el vector x que nos dan en la base canónica, en términos de la base B1, tenemos:

```matlab
A = [3 2;1 -1]
ecs = [7;4] == A*[b1;b2]
```

**Salida:**
```text
A =
3  2
1  -1
ecs = ([7=3⁢b_1+2⁢b_2; 4=b_1-b_2])
```

Ya, únicamente hay que calcular $\left\lbrack \begin{array}{c}
b_1 \\
b_2
\end{array}\right\rbrack$:

```matlab
sol = solve(ecs)
```

**Salida:**
```text
sol = struct with fields:
b1: 3
b2: -1
```

Por tanto:

```matlab
x_B1 = [sol.b1;sol.b2]
```

**Salida:**
```text
x_B1 = ([3; -1])
```

O sea:

$${\left(x\right)}_{B_1 } =\left\lbrack \begin{array}{c}
3\\
-1
\end{array}\right\rbrack$$

Volver al índice

#### Problema 6 - Espacio de filas

Hallar una base del espacio de filas de la matriz:

[Imagen: Matriz $A=\begin{pmatrix}1&3&1&3\\0&1&1&0\\-3&0&6&-1\\3&4&-2&1\\2&0&-4&-2\end{pmatrix}$.]

Solución

Construimos la matriz A:

```matlab
clear; clc;
A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2]
```

**Salida:**
```text
A =
1  3  1  3
0  1  1  0
-3  0  6  -1
3  4  -2  1
2  0  -4  -2
```

Veamos el rango de la matriz:

```matlab
rank(A)
```

**Salida:**
```text
ans =
```

Hay tres filas linealmente independientes.

Buscamos la matriz escalonada, empleando el método de Gauss-Jordan:

```matlab
B = rref(A)
```

**Salida:**
```text
B =
1  0  -2  0
0  1  1  0
0  0  0  1
0  0  0  0
0  0  0  0
```

Sabemos que "Si A es una matriz equivalente por filas a una matriz B escalonada por filas, los vectores fila no nulos de B forman una base del espacio de filas de A".

Por tanto una base del espacio de filas de A será:

```matlab
B1 = B(1:rank(B), :)
```

**Salida:**
```text
B1 =
1  0  -2  0
0  1  1  0
0  0  0  1
```

Dado que solemos escribir los vectores en columnas:

```matlab
B1 = B1'
```

**Salida:**
```text
B1 =
1  0  0
0  1  0
-2  1  0
0  0  1
```

Volver al índice

#### Problema 7 - Espacio de columnas

Hallar una base del espacio de columnas de la matriz:

[Imagen: Matriz $A=\begin{pmatrix}1&3&1&3\\0&1&1&0\\-3&0&6&-1\\3&4&-2&1\\2&0&-4&-2\end{pmatrix}$.]

Solución

Vamos a hacer uso de la propiedad anterior del espacio de filas: "Si A es una matriz equivalente por filas a una matriz B escalonada por filas, los vectores fila no nulos de B forman una base del espacio de filas de A".

Para ello trabajaremos con la matriz traspuesta de A, de forma análoga a lo hecho en el problema anterior:

```matlab
clc; clear;
A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2]
rank(A')
B = rref(A')
B1 = B(1:rank(B), :)
B1 = B1'
```

**Salida:**
```text
A =
1  3  1  3
0  1  1  0
-3  0  6  -1
3  4  -2  1
2  0  -4  -2
ans =
B =
1  0  0  0  -1
0  1  0  4  3
0  0  1  -1  -1
0  0  0  0  0
B1 =
1  0  0  0  -1
0  1  0  4  3
0  0  1  -1  -1
B1 =
1  0  0
0  1  0
0  0  1
0  4  -1
-1  3  -1
```

Otra base:

```matlab
C = rref(A)
```

**Salida:**
```text
C =
1  0  -2  0
0  1  1  0
0  0  0  1
0  0  0  0
0  0  0  0
```

Son independientes las columnas 1, 2 y 4. Por tanto:

```matlab
D = [A(:,1:2) A(:,4)]
rD = rank(D)
```

**Salida:**
```text
D =
1  3  3
0  1  0
-3  0  -1
3  4  1
2  0  -2
ans =
```

Vemos que, en efecto, son independientes y por tanto, forman base del espacio de columnas, al ser todas las independientes de las columnas de A.

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Live Script: dependencia e independencia lineal

*Fuente: `EV_02_R05.mlx`*

###  [Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

### ESPACIOS VECTORIALES - DEPENDENCIA E INDEPENDENCIA LINEAL

- Table of Contents

- Problema 0 - Ejemplos con rref · Problema 1 - Dependencia e independencia lineal ·     Solución · Problema 2 - Dependencia e independencia lineal ·     Solución · Problema 3 - Bases ortonormales ·     Solución ·         1 - Base ·         2 - L = 1 ·         3 - Base canónica ·         4 - Base ortonormal · Problema 4 - Bases ·     Solución ·         Apartado 1 ·         Apartado 2 ·         Apartado 3 · Problema 5 - Espacio de columnas ·     Solución · Problema 6 - Espacio de columnas ·     Solución · Problema 7 - Espacio de columnas ·     Solución · Problema 8 - Espacio nulo ·     Solución · Problema 9 - Espacio de columnas ·     Solución · Problema 10 - Espacio nulo ·     Solución · Problema 11 - Espacio de filas

#### Problema 0 - Ejemplos con rref

Sea la matriz $A=\left\lbrack \begin{array}{cccc}
2 & 3 & -8 & 7\\
2 & -1 & 2 & -7\\
1 & 0 & -3 & 6\\
2 & 0 & -6 & 12
\end{array}\right\rbrack$

Vamos a emplear la función rref para ilustrar su funcionamiento.

```matlab
clear; clc;
A = [2 3 -8 7; 2 -1 2 -7;1 0 -3 6; 2 0 -6 12]
```

**Salida:**
```text
A =
2  3  -8  7
2  -1  2  -7
1  0  -3  6
2  0  -6  12
```

Le aplicamos directamente la función rref. Esta función da la matriz escalonada por filas de A.

```matlab
[GJ,p] = rref(A)
```

**Salida:**
```text
GJ =
1.0000  0  0  -2.4545
0  1.0000  0  -3.5455
0  0  1.0000  -2.8182
0  0  0  0
p =
1  2  3
```

Nos dice que hay tres pivotes en las columnas 1, 2 y 3. La columna 4 de GJ muestra los coeficientes de combinación lineal de la cuarta columna de A en función de las tres primeras:

```matlab
GJ(1,4)*A(:,1) + GJ(2,4)*A(:,2) + GJ(3,4)*A(:,3)
```

**Salida:**
```text
ans =
-7
```

Vemos que la línea anterior nos da la columna 4 de A.

Pero no ocurre igual con la cuarta fila:

```matlab
GJ(1,4)*A(1,:) + GJ(2,4)*A(2,:) + GJ(3,4)*A(3,:)
```

**Salida:**
```text
ans =
-14.8182  -3.8182  21.0000  -9.2727
```

Si queremos ver la combinación lineal de la cuarta fila, tenemos que trabajar con la matriz traspuesta:

```matlab
At = A'
[GJt,pt] = rref(At)
GJt(1,4)*A(1,:) + GJt(2,4)*A(2,:) + GJt(3,4)*A(3,:)
```

**Salida:**
```text
At =
2  2  1  2
3  -1  0  0
-8  2  -3  -6
7  -7  6  12
GJt =
1  0  0  0
0  1  0  0
0  0  1  2
0  0  0  0
pt =
1  2  3
ans =
2  0  -6  12
```

Es decir: rref trabaja por filas, pero da los coeficientes de combinación de las columnas. Si se buscan los coeficientes de combinación de las filas, se ha de trabajar con la traspuesta.

Volver al índice

#### Problema 1 - Dependencia e independencia lineal

Grossman, S.I.; Flores, J.J. (2020): Algebra lineal. Octava edición. Mc Graw - Hill. Ejemplo 5.6.5

En $P^2$, determine si los polinomios:

$$\begin{array}{l}
p_1 \;=3-x\\
p_2 =2+x^2 \\
p_3 \;=\;4+5x-2x^2
\end{array}$$

son linealmente dependientes o independientes.

Solución

Para solucionar este problema, vamos a obtener las coordenadas de cada polinomio en una base común, que será: $B_1 =\left\lbrace 1,x,x^2 \right\rbrace$.

Así, tendremos:

$p_1 =\left\lbrack \begin{array}{c}
3\\
-1\\
0
\end{array}\right\rbrack$, $p_2 =\left\lbrack \begin{array}{c}
2\\
0\\
1
\end{array}\right\rbrack$, $p_3 =\left\lbrack \begin{array}{c}
4\\
5\\
-2
\end{array}\right\rbrack$

Ahora comprobamos si son dependientes o no:

```matlab
clear; clc;
p1 = [3;-1;0]
p2 = [2;0;1]
p3 = [4;5;-2]
P = [p1, p2, p3]
det(P)
```

**Salida:**
```text
p1 =
-1
p2 =
p3 =
-2
P =
3  2  4
-1  0  5
0  1  -2
ans =
-23
```

Vemos que $|P|\not= 0$, siendo $P=\left\lbrack \begin{array}{ccc}
p_1  & p_2  & p_3
\end{array}\right\rbrack$, por lo que los tres polinomios son linealmente independientes.

O también:

```matlab
GJ = rref([p1 p2 p3])
```

**Salida:**
```text
GJ =
1  0  0
0  1  0
0  0  1
```

Es preferible este sistema, porque, en caso de ser l.d., obtenemos también los coeficientes de dependencia.

Volver al índice

#### Problema 2 - Dependencia e independencia lineal

Grossman, S.I.; Flores, J.J. (2020): Algebra lineal. Octava edición. Mc Graw - Hill. Ejemplo 5.6.6

En el espacio vectorial $M_{22}$, determinar si las matrices siguientes son o no linealmente dependientes:

$M_1 =\left\lbrack \begin{array}{cc}
1 & 2\\
3 & 6
\end{array}\right\rbrack$, $M_2 =\left\lbrack \begin{array}{cc}
-1 & 3\\
-1 & 1
\end{array}\right\rbrack$, $M_3 =\left\lbrack \begin{array}{cc}
2 & -1\\
0 & 1
\end{array}\right\rbrack$, $M_4 =\left\lbrack \begin{array}{cc}
1 & 4\\
4 & 9
\end{array}\right\rbrack$

Solución

Empleamos la base canónica:

$B_1 =\left\lbrace U_1 ,U_2 ,U_3 ,U_4 \right\rbrace =\left\lbrace \left\lbrack \begin{array}{cc}
1 & 0\\
0 & 0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{cc}
0 & 1\\
0 & 0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{cc}
0 & 0\\
1 & 0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{cc}
0 & 0\\
0 & 1
\end{array}\right\rbrack \right\rbrace$.

En esta base:

$$\begin{array}{l}
M_1 =U_1 +2\cdot U_2 +3\cdot U_3 +6\cdot U_4 \\
M_2 =-U_1 +3\cdot U_2 -U_3 +U_4 \\
M_3 =2\cdot U_1 -U_2 +U_4 \\
M_4 =U_1 +4\cdot U_2 +4\cdot U_3 +9\cdot U_4
\end{array}$$

Colocamos los cuatro vectores en una matriz:

```matlab
clear;clc;
M = [1 -1 2 1;2 3 -1 4;3 -1 0 4;6 1 1 9]
```

**Salida:**
```text
M =
1  -1  2  1
2  3  -1  4
3  -1  0  4
6  1  1  9
```

Si son linealmente independientes, la matriz será regular:

```matlab
det(M)
```

**Salida:**
```text
ans =
6.6613e-15
```

Vemos que $|M|\simeq 0$, por lo que hay dependencia lineal entre las matrices.

Otra forma de calcularlo es comprobar si el sistema de ecuaciones lineales homogéneo siguiente tiene soluciones distintas de la trivial:

$$a\cdot M_1 +b\cdot M_2 +c\cdot M_3 +d\cdot M_4 =\left\lbrack \begin{array}{cc}
0 & 0\\
0 & 0
\end{array}\right\rbrack$$

```matlab
syms a b c d
M1 = [1 2;3 6]
M2 = [-1 3;-1 1]
M3 = [2 -1;0 1]
M4 = [1 4;4 9]
ecs = a*M1 + b*M2 + c*M3 + d*M4 == [0 0;0 0]
[A b] = equationsToMatrix(ecs)

GJ = rref([A b])
```

**Salida:**
```text
M1 =
1  2
3  6
M2 =
-1  3
-1  1
M3 =
2  -1
0  1
M4 =
1  4
4  9
ecs = ([a-b+2⁢c+d=0, 2⁢a+3⁢b-c+4⁢d=0; 3⁢a-b+4⁢d=0, 6⁢a+b+c+9⁢d=0])
A = ([1, -1, 2, 1; 3, -1, 0, 4; 2, 3, -1, 4; 6, 1, 1, 9])
b = ([0; 0; 0; 0])
GJ = ([1, 0, 0, (29)/(20), 0; 0, 1, 0, (7)/(20), 0; 0, 0, 1, -(1)/(20), 0; 0, 0, 0, 0, 0])
```

De este resultado vemos que el SEL es compatible indeterminado, por lo que hay soluciones diferentes de la trivial, lo que implica que hay dependencia lineal entre las filas. Por otro lado, vemos que la cuarta columna se puede obtener en función de las tres primeras:

```matlab
A4 = GJ(1,4)*A(:,1) + GJ(2,4)*A(:,2) + GJ(3,4)*A(:,3)
A(:,4)
```

**Salida:**
```text
A4 = ([1; 4; 4; 9])
ans = ([1; 4; 4; 9])
```

O directamente, analizando la matriz:

```matlab
GJ = rref(M)
```

**Salida:**
```text
GJ =
1.0000  0  0  1.4500
0  1.0000  0  0.3500
0  0  1.0000  -0.0500
0  0  0  0
```

Vemos que la cuarta columna de M se puede obtener como combinación lineal de las tres primeras, con los coeficientes mostrados en la cuarta columna de GJ.

Volver al índice

#### Problema 3 - Bases ortonormales

En $R^3$ se considera el conjunto B = {(1, −1, 1), (−2, λ, 0), (−1, 1, λ)},

- Hallar los valores de λ para los que B no es una base de $R^3$.

- Para λ = 1, calcular las coordenadas del vector v = (2, 1, 2) respecto de B.

- Para λ = 0, hallar la matriz de cambio de coordenadas de la base canónica de R3 a la base B.

- Para λ = 2, hallar una base ortonormal del subespacio generado por B.

Solución

1 - Base

Para que un conjunto de vectores de $R^n$ sea una base se ha de cumplir una de estas cosas:

- Que sea linealmente independiente

- Que genere a $R^n$

La primera de estas cuestiones es más sencilla de comprobar. Basta verificar que la matriz de vectores columna es regular.

```matlab
clear; clc;
syms L
B = [1 -2 -1;-1 L 1;1 0 L]
ec = det(B) == 0
sol = solve(ec,L)
```

**Salida:**
```text
B = ([1, -2, -1; -1, L, 1; 1, 0, L])
ec = -2-L+L^2=0
sol = ([-1; 2])
```

Por tanto, B es base para cualquier valor de L distinto de L = -1 ó L = 2.

2 - L = 1

```matlab
B1 = subs(B,L,1)
v = [2;1;2]
syms x y z
X = [x;y;z]
ec = B1*X == v
Cv = solve(ec,[x,y,z])
```

**Salida:**
```text
B1 = ([1, -2, -1; -1, 1, 1; 1, 0, 1])
v =
X = ([x; y; z])
ec = ([-z-2⁢y+x=2; z+y-x=1; z+x=2])
Cv = struct with fields:
x: -1
y: -3
z: 3
```

Luego las coordenadas de V en la base B son : $V=\left\lbrack \begin{array}{c}
-1\\
-3\\
3
\end{array}\right\rbrack$

3 - Base canónica

Se trata de obtener las coordenadas de los vectores de la base canónica en la base B. Pero B contiene los vectores de la base en la base canónica, luego la matriz buscada es la inversa de B.

```matlab
B2 = subs(B,L,0)
PBC = inv(B2)
```

**Salida:**
```text
B2 = ([1, -2, -1; -1, 0, 1; 1, 0, 0])
PBC = ([0, 0, 1; -(1)/(2), -(1)/(2), 0; 0, 1, 1])
```

4 - Base ortonormal

Sabemos, por el primer apartado, que B no es base si L = 2. Pero B con L = 2 puede ser sistema generador (no base, por no ser linealmente independiente) de un subespacio vectorial U de R3. Una base de U (dado que r(B) = 2) se puede obtener eliminando uno de los vectores de B:

```matlab
U = subs(B(:,1:2),L,2)
```

**Salida:**
```text
U = ([1, -2; -1, 2; 1, 0])
```

Estos dos vectores no son ortogonales, pues u1·u2 no es igual a 0:

```matlab
u1u2 = dot(U(:,1),U(:,2))
```

**Salida:**
```text
u1u2 = -4
```

Podemos ortogonalizar ahora la base empleando el método de Gram-Schmidt:

```matlab
b1 = subs(B(:,1),L,2)
b2 = subs(B(:,2),L,2)

u1 = b1
u2 = b2 - dot(b2,u1)/dot(u1,u1)*u1
```

**Salida:**
```text
b1 = ([1; -1; 1])
b2 = ([-2; 2; 0])
u1 = ([1; -1; 1])
u2 = ([-(2)/(3); (2)/(3); (4)/(3)])
```

Comprobamos que son ortogonales

```matlab
check = dot(u1,u2)
```

**Salida:**
```text
check = 0
```

Y ahora, normalizamos ambos vectores:

```matlab
u1 = double(u1/norm(u1))
u2 = double(u2/norm(u2))
```

**Salida:**
```text
u1 =
0.5774
-0.5774
0.5774
u2 =
-0.4082
0.4082
0.8165
```

Comprobamos la ortonormalidad:

```matlab
check = dot(u1,u2)
norm(u1)
norm(u2)
```

**Salida:**
```text
check =
ans =
1.0000
ans =
```

Volver al índice

#### Problema 4 - Bases

Sea B = {b1, b2} una base de $R^2$:

$$b_1 =\left\lbrack \begin{array}{c}
-2\\
5
\end{array}\right\rbrack \;\;\;\;\;b_2 =\left\lbrack \begin{array}{c}
0\\
-5
\end{array}\right\rbrack$$

- Comprobar que, efectivamente, es una base de $R^2$

- ¿Es B ortogonal?

- Obtener una nueva base que sea ortonormal

Solución

Apartado 1

```matlab
clear; clc;
b1 = [-2;5]
b2 = [0;-5]

BGJ = rref([b1 b2])
```

**Salida:**
```text
b1 =
-2
b2 =
-5
BGJ =
1  0
0  1
```

Por tanto, es base (son dos vectores linealmente independientes).

Apartado 2

```matlab
orto = dot(b1,b2)
```

**Salida:**
```text
orto =
-25
```

$b_1 \cdot b_2 \not= 0$, luego no son ortogonales

Apartado 3

Sean $v_1 =\left\lbrack \begin{array}{c}
a\\
b
\end{array}\right\rbrack \;\;\;v_2 =\left\lbrack \begin{array}{c}
c\\
d
\end{array}\right\rbrack$dos vectores de $R^2$, ortogonales. Por tanto, seran una base ortogonal.

```matlab
syms a b k1 k2 k3 k4
v1 = [a;b]
v2 = [1;2]
eqort = dot(v1,v2) == 0
ecu1 = [a;b] == k1*b1 + k2*b2
ecu2 = [1;2] == k3*b1 + k4*b2
eq = [eqort;ecu1;ecu2]
eq1 = [ecu1;ecu2];
sol1 = solve(eq1, [k1, k2, k3, k4])
sol2 = solve(eqort)
```

**Salida:**
```text
v1 = ([a; b])
v2 =
eqort = a‾+2⁢b‾=0
ecu1 = ([a=-2⁢k_1; b=5⁢k_1-5⁢k_2])
ecu2 = ([1=-2⁢k_3; 2=5⁢k_3-5⁢k_4])
eq = ([a‾+2⁢b‾=0; a=-2⁢k_1; b=5⁢k_1-5⁢k_2; 1=-2⁢k_3; 2=5⁢k_3-5⁢k_4])
sol1 = struct with fields:
k1: -a/2
k2: - a/2 - b/5
k3: -1/2
k4: -9/10
sol2 = -(a)/(2)
```

Volver al índice

#### Problema 5 - Espacio de columnas

El espacio de columnas consiste en todas las combinaciones lineales de las columnas de una matriz A.

Sea la matriz $A=\left\lbrack \begin{array}{cccc}
2 & 3 & -8 & 7\\
2 & -1 & 2 & -7\\
1 & 0 & -3 & 6
\end{array}\right\rbrack$

De su espacio de columnas, hallar una base y su dimensión.

Solución

Introducimos la matriz en el sistema, y hallamos su forma escalonada reducida.

```matlab
clear; clc;
A = [2 3 -8 7; 2 -1 2 -7;1 0 -3 6]
[AGJ,p] = rref(A')
AGJ = AGJ'
```

**Salida:**
```text
A =
2  3  -8  7
2  -1  2  -7
1  0  -3  6
AGJ =
1  0  0
0  1  0
0  0  1
0  0  0
p =
1  2  3
AGJ =
1  0  0  0
0  1  0  0
0  0  1  0
```

De esta matriz, AGJ, obtenemos los pivotes. Los pivotes son los primeros elementos de cada fila cuyo valor no es nulo. Tenemos tres pivotes, que nos indican que las tres primeras columnas son linealmente independientes. La cuarta columna de la matriz A es combinación lineal de las tres primeras, y los valores de AGJ(:,4) nos dan los coeficientes de combinación, como podemos comprobar a continuación:

```matlab
A(:,1)*AGJ(1,4) + A(:,2)*AGJ(2,4) + A(:,3)*AGJ(3,4)
```

**Salida:**
```text
ans =
```

Por tanto, una base del espacio de columnas de la matriz A está constituída por las tres primeras columnas. Por tanto, la dimensión del EC es 3.

Volver al índice

#### Problema 6 - Espacio de columnas

Sea la matriz $A=\left\lbrack \begin{array}{ccc}
1 & -3 & -4\\
-4 & 6 & -2\\
-3 & 7 & 6
\end{array}\right\rbrack$ y el vector $b=\left\lbrack \begin{array}{c}
3\\
3\\
-4
\end{array}\right\rbrack$. Comprobar si el vector b está en el espacio de columnas de la matriz A.

Solución

En primer lugar, comprobamos si las tres columnas de A constituyen una base; para ello han de ser linealmente independientes.

```matlab
clear; clc;
A = [1 -3 -4;-4 6 -2;-3 7 6]
b = [3;3;-4]
AGJ = rref(A)
```

**Salida:**
```text
A =
1  -3  -4
-4  6  -2
-3  7  6
b =
-4
AGJ =
1  0  5
0  1  3
0  0  0
```

Vemos que sólo dos de las columnas pueden constituir una base. La tercera columna es combinación lineal de las dos primeras con coeficientes 5 y 3:

```matlab
AGJ(1,3)*A(:,1) + AGJ(2,3)*A(:,2)
```

**Salida:**
```text
ans =
-4
-2
```

Veamos si b pertenece a esta base. Para ello, la matriz creada por las dos primera columnas de A y b como tercera columna, debería ser singular (porque la tercera columna debería ser combinación lineal de las dos primeras). Llamamos Ab a la nueva matriz:

```matlab
Ab = [A(:,1:2) b]
AbGJ = rref(Ab)
```

**Salida:**
```text
Ab =
1  -3  3
-4  6  3
-3  7  -4
AbGJ =
1.0000  0  -4.5000
0  1.0000  -2.5000
0  0  0
```

Vemos que sí es combinación lineal, con coeficientes dados por la tercera columna de AbGJ:

```matlab
AbGJ(1,3)*Ab(:,1) + AbGJ(2,3)*Ab(:,2)
```

**Salida:**
```text
ans =
-4
```

Otra forma:

Una combinación lineal entre los vectores X e Y se puede escribir:

$\textrm{cl}=a\cdot X+b\cdot Y$.

Si ambos vectores son linealmente independientes, $\textrm{cl}=0\;\;\to \;a=b=0$

Pues veamos qué ocurre con el vector b y la base del EC de A:

```matlab
syms x y z
ecs = x*A(:,1) + y*A(:,2) + z*b == 0
```

**Salida:**
```text
ecs = ([x-3⁢y+3⁢z=0; -4⁢x+6⁢y+3⁢z=0; -3⁢x+7⁢y-4⁢z=0])
```

Resolvemos el sistema de ecuaciones lineales así obtenido:

```matlab
[A1, b1] = equationsToMatrix(ecs)
A1b1GJ = rref([A1 b1])
```

**Salida:**
```text
A1 = ([1, -3, 3; -4, 6, 3; -3, 7, -4])
b1 = ([0; 0; 0])
A1b1GJ = ([1, 0, -4.5000, 0; 0, 1, -2.5000, 0; 0, 0, 0, 0])
```

Vemos que las dos primeras columnas son independientes (hay pivotes) y la tercera no lo es, con coeficientes:

```matlab
A1b1GJ(1:2,3)
```

**Salida:**
```text
ans = ([-4.5000; -2.5000])
```

distintos de cero. Luego hay combinación lineal y b pertenece al espacio de columnas de A.

Volver al índice

#### Problema 7 - Espacio de columnas

Construya, si es posible, una matriz A, tal que A sea simétrica, y su espacio columna esté generado por los vectores (1 -2 5 0) y (-2 0 2 -4).

Solución

```matlab
clear; clc;
syms x y z
b1 = [1;-2;5;0]
b2 = [-2;0;2;4]
A1 = [b1 b2]
```

**Salida:**
```text
b1 =
-2
b2 =
-2
A1 =
1  -2
-2  0
5  2
0  4
```

Se tienen dos condiciones:

- La matriz ha de ser simétrica. Por tanto, hay elementos que vienen dados

- Las columnas 3ª y 4ª han de ser combinación lineal de las 1ª y 2ª, ya que pertenecen al espacio de columnas generado por éstas.

Por tanto:

```matlab
A1(1,3) = A1(3,1)
A1(1,4) = A1(4,1)
A1(2,3) = A1(3,2)
A1(2,4) = A1(4,2)
```

**Salida:**
```text
A1 =
1  -2  5
-2  0  0
5  2  0
0  4  0
A1 =
1  -2  5  0
-2  0  0  0
5  2  0  0
0  4  0  0
A1 =
1  -2  5  0
-2  0  2  0
5  2  0  0
0  4  0  0
A1 =
1  -2  5  0
-2  0  2  4
5  2  0  0
0  4  0  0
```

Quedan cuatro elementos (que realmente son tres, puesto que la matriz ha de ser simétrica) que son incógnitas:

```matlab
b3 = [5; 2; x; y]
A2 = [A1(:,1:2) b3]
b4 = [0;4;y;z]
A2 = [A2 b4]
A = A2
```

**Salida:**
```text
b3 = ([5; 2; x; y])
A2 = ([1, -2, 5; -2, 0, 2; 5, 2, x; 0, 4, y])
b4 = ([0; 4; y; z])
A2 = ([1, -2, 5, 0; -2, 0, 2, 4; 5, 2, x, y; 0, 4, y, z])
A = ([1, -2, 5, 0; -2, 0, 2, 4; 5, 2, x, y; 0, 4, y, z])
```

Planteamos las ecuaciones de compatibilidad lineal:

```matlab
syms a b c d
ec1 = A(:,3) == a*A(:,1) + b*A(:,2)
ec2 = A(:,4) == c*A(:,1) + d*A(:,2)

ecs = [ec1;ec2]

sol = solve(ecs)
```

**Salida:**
```text
ec1 = ([5=a-2⁢b; 2=-2⁢a; x=5⁢a+2⁢b; y=4⁢b])
ec2 = ([0=c-2⁢d; 4=-2⁢c; y=5⁢c+2⁢d; z=4⁢d])
ecs = ([5=a-2⁢b; 2=-2⁢a; x=5⁢a+2⁢b; y=4⁢b; 0=c-2⁢d; 4=-2⁢c; y=5⁢c+2⁢d; z=4⁢d])
sol = struct with fields:
a: -1
b: -3
c: -2
d: -1
x: -11
y: -12
z: -4
```

Como a, b, c y d son distintos de cero, concluímos que las dos últimas columnas dependen linealmente de las dos primeras.

La matriz A queda:

```matlab
A = subs(A,[x y z],[sol.x sol.y sol.z])
```

**Salida:**
```text
A = ([1, -2, 5, 0; -2, 0, 2, 4; 5, 2, -11, -12; 0, 4, -12, -4])
```

Vemos que su rango es 2:

```matlab
rA = rank(A)
```

**Salida:**
```text
rA =
```

Hacemos un Gauss-Jordan

```matlab
rref(A)
```

**Salida:**
```text
ans = ([1, 0, -1, -2; 0, 1, -3, -1; 0, 0, 0, 0; 0, 0, 0, 0])
```

Y vemos que se obtienen los mismos coeficientes anteriores para a, b, c y d.

Volver al índice

#### Problema 8 - Espacio nulo

Encontrar el espacio nulo de la matriz:

$$A=\left\lbrack \begin{array}{cccc}
1 & 2 & -4 & 3\\
2 & 5 & 6 & -8\\
0 & -1 & -14 & 14\\
3 & 6 & -12 & 9
\end{array}\right\rbrack$$

Solución

El espacio nulo de una matriz A lo constituyen todos aquellos vectores x tales que $A\cdot \vec{x} =\vec{0}$.

```matlab
clear; clc;
syms x1 x2 x3 x4

A = [1 2 -4 3;2 5 6 -8;0 -1 -14 14;3 6 -12 9]
X = [x1;x2;x3;x4]

ecs = A*X == [0;0;0;0]
[A1 b1] = equationsToMatrix(ecs)
GJ = rref([A1 b1])
```

**Salida:**
```text
A =
1  2  -4  3
2  5  6  -8
0  -1  -14  14
3  6  -12  9
X = ([x_1; x_2; x_3; x_4])
ecs = ([x_1+2⁢x_2-4⁢x_3+3⁢x_4=0; 2⁢x_1+5⁢x_2+6⁢x_3-8⁢x_4=0; 14⁢x_4-14⁢x_3-x_2=0; 3⁢x_1+6⁢x_2-12⁢x_3+9⁢x_4=0])
A1 = ([1, 2, -4, 3; 2, 5, 6, -8; 0, -1, -14, 14; 3, 6, -12, 9])
b1 = ([0; 0; 0; 0])
GJ = ([1, 0, -32, 31, 0; 0, 1, 14, -14, 0; 0, 0, 0, 0, 0; 0, 0, 0, 0, 0])
```

El sistema equivalente es:

```matlab
seq = GJ(:,1:end-1)*X == GJ(:,end)
```

**Salida:**
```text
seq = ([x_1-32⁢x_3+31⁢x_4=0; x_2+14⁢x_3-14⁢x_4=0; 0=0; 0=0])
```

El grado de libertad es:

```matlab
GL = length(X) - rank(A1)
```

**Salida:**
```text
GL =
```

Luego resolvemos x1 y x2:

```matlab
[x1, x2] = solve(seq, [x1, x2])
```

**Salida:**
```text
x1 = 32⁢x_3-31⁢x_4
x2 = 14⁢x_4-14⁢x_3
```

Por tanto, cualquier vector que pertenezca al espacio nulo deberá cumplir:

$x=\left\lbrack \begin{array}{c}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
32x_3 -31x_4 \\
{-14x}_3 +14x_4 \\
x_3 \\
x_4
\end{array}\right\rbrack =x_3 \left\lbrack \begin{array}{c}
32\\
-14\\
1\\
0
\end{array}\right\rbrack +x_4 \left\lbrack \begin{array}{c}
-31\\
14\\
0\\
1
\end{array}\right\rbrack$,

por lo que una base del espacio nulo será:

$N=\left\lbrace \left\lbrack \begin{array}{c}
32\\
-14\\
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-31\\
14\\
0\\
1
\end{array}\right\rbrack \right\rbrace$y la nulidad es, por tanto, 2.

Volver al índice

#### Problema 9 - Espacio de columnas

Determinar una base para los cuatro vectores de $R^3$ siguientes:

$$\begin{array}{l}
v_1 =\left\lbrack \begin{array}{c}
1\\
2\\
-3
\end{array}\right\rbrack \\
v_2 =\left\lbrack \begin{array}{c}
-2\\
0\\
4
\end{array}\right\rbrack \\
v_3 =\left\lbrack \begin{array}{c}
0\\
4\\
-2
\end{array}\right\rbrack \\
v_4 =\left\lbrack \begin{array}{c}
-2\\
-4\\
6
\end{array}\right\rbrack
\end{array}$$

Solución

Construimos la matriz:

```matlab
clear; clc;
v1 = [1;2;-3]
v2 = [-2; 0; 4]
v3 = [0; 4; -2]
v4 = [-2; -4; 6]

A = [v1 v2 v3 v4]
```

**Salida:**
```text
v1 =
-3
v2 =
-2
v3 =
-2
v4 =
-2
-4
A =
1  -2  0  -2
2  0  4  -4
-3  4  -2  6
```

Los cuatro vectores son generadores, pero puede que no constituyan una base, pues habrá alguno que sea dependiente de los demás. Veamos:

```matlab
GJ = rref(A)
```

**Salida:**
```text
GJ =
1  0  2  -2
0  1  1  0
0  0  0  0
```

Sólo las dos primeras columnas constituyen la base. Las dos últimas se pueden expresar como:

C3 = 2*C1 + 1*C2

C4 = -2*C1

Volver al índice

#### Problema 10 - Espacio nulo

Sea $A=\left\lbrack \begin{array}{ccc}
1 & -1 & 3\\
2 & 0 & 4\\
-1 & -3 & 1
\end{array}\right\rbrack$

Calcular su nulidad.

Solución

Podemos hacer dos cosas:

- Calcular una base del espacio nulo

- Aplicar el teorema de rango + nulidad = columnas

Según la segunda opción:

```matlab
clear; clc;
A = [1 -1 3; 2 0 4;-1 -3 1]
n = size(A,2)
nul = n - rank(A)
```

**Salida:**
```text
A =
1  -1  3
2  0  4
-1  -3  1
n =
nul =
```

Por el primer sistema:

```matlab
syms x1 x2 x3
X = [x1;x2;x3]
ecs = A*X == zeros(size(A,2),1)
[A1 b1]= equationsToMatrix(ecs)

GJ = rref([A1 b1])
seq = GJ(:,1:end-1)*X + GJ(:,end)
GL = n - rank(A)

[x1 x2] = solve(seq,[x1 x2])
```

**Salida:**
```text
X = ([x_1; x_2; x_3])
ecs = ([x_1-x_2+3⁢x_3=0; 2⁢x_1+4⁢x_3=0; x_3-3⁢x_2-x_1=0])
A1 = ([1, -1, 3; 2, 0, 4; -1, -3, 1])
b1 = ([0; 0; 0])
GJ = ([1, 0, 2, 0; 0, 1, -1, 0; 0, 0, 0, 0])
seq = ([x_1+2⁢x_3; x_2-x_3; 0])
GL =
x1 = -2⁢x_3
x2 = x_3
```

Cualquier vector del núcleo es:

$$x=\left\lbrack \begin{array}{c}
x_1 \\
x_2 \\
x_3
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
{-2x}_3 \\
x_3 \\
x_3
\end{array}\right\rbrack =x_3 \left\lbrack \begin{array}{c}
-2\\
1\\
1
\end{array}\right\rbrack$$

Vemos que sólo hay un vector en la base, por lo que la nulidad es 1

Volver al índice

#### Problema 11 - Espacio de filas

Hallar una base del espacio de filas de la matriz: [Imagen: Misma matriz $A=\begin{pmatrix}1&3&1&3\\0&1&1&0\\-3&0&6&-1\\3&4&-2&1\\2&0&-4&-2\end{pmatrix}$.]

```matlab
clear; clc;
A = [1 3 1 3;0 1 1 0;-3 0 6 -1;3 4 -2 1;2 0 -4 -2]
```

**Salida:**
```text
A =
1  3  1  3
0  1  1  0
-3  0  6  -1
3  4  -2  1
2  0  -4  -2
```

El rango de la matriz es:

```matlab
r = rank(A)
```

**Salida:**
```text
r =
```

Por tanto, hay 3 líneas (filas o columnas) linealmente independientes.

```matlab
[GJ p] = rref(A)
```

**Salida:**
```text
GJ =
1  0  -2  0
0  1  1  0
0  0  0  1
0  0  0  0
0  0  0  0
p =
1  2  4
```

Se ve que las filas linealmente independientes son la 1ª, 2ª y 4ª.

```matlab
for i = 1: length(p)
    B(i,:) = A(p(i),:);
end
B
```

**Salida:**
```text
B =
1  3  1  3
0  1  1  0
3  4  -2  1
```

Volver al índice

_Imágenes embebidas: 2 (image1.png, image2.png)_


## Live Script: problemas de cambio de base

*Fuente: `EV_Cambio_de_Base_R08.mlx`*

[Imagen: Logotipo 'Universidad Francisco de Vitoria – UFV Madrid' (cabecera).]

Prof. Josemaría Medina

### CAMBIOS DE BASE. Problemas de bases

- Tabla de Contenido

- Introducción teórica ·     Ejemplo · Problema 1 ·     Solución · Problema 2 ·     Solución 1 ·     Solución 2

#### Introducción teórica

Sean dos bases del espacio vectorial $R^2$. Estas bases son: $B=\left\lbrace \left\lbrack \begin{array}{c}
b_{1x} \\
b_{1y}
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
b_{2x} \\
b_{2y}
\end{array}\right\rbrack \right\rbrace$y $C=\left\lbrace \left\lbrack \begin{array}{c}
c_{1x} \\
c_{1y}
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
c_{2x} \\
c_{2y}
\end{array}\right\rbrack \right\rbrace$. Para abreviar, nos referiremos a ellas como $B=\left\lbrace b_1 ,b_2 \right\rbrace$ y $C=\left\lbrace c_1 ,c_2 \right\rbrace$. Suponemos que las coordenadas de ambas bases se refieren a la base canónica: $U=\left\lbrace \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack \right\rbrace$.

Supongamos ahora un vector $v\in R^2$. Este vector se podrá representar como combinación lineal de los vectores de ambas bases, es decir:

$$\begin{array}{l}
v_B =a\cdot b_1 +b\cdot b_2 \\
v_C =c\cdot c_1 +d\cdot c_2
\end{array}$$

Se ha utilizado como subíndice en cada caso la base a la que se refiere el vector. Es evidente que:

$v_B =\left\lbrack \begin{array}{c}
a\\
b
\end{array}\right\rbrack$ y $v_C =\left\lbrack \begin{array}{c}
c\\
d
\end{array}\right\rbrack$,

referido a ambas bases.

Pero dado que tanto B como C pertenecen a $R^2$, los vectores de cualquiera de ambas bases se pueden representar como combinación lineal de la otra. Por ejemplo, la base B en función de la C sería:

$$\begin{array}{l}
b_1 =x\cdot c_1 +y\cdot c_2 \\
b_2 =z\cdot c_1 +t\cdot c_2
\end{array}$$

O, en forma matricial:

$$\left\lbrack \begin{array}{c}
b_1 \\
b_2
\end{array}\right\rbrack =\left\lbrack \begin{array}{cc}
x & y\\
z & t
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
c_1 \\
c_2
\end{array}\right\rbrack$$

Volviendo al vector v, es evidente que será siempre el mismo vector, aunque esté definido en dos bases diferentes (en función de la base de referencia, llamaremos a v, respectivamente, $v_B$ ó $v_C$). Más adelante se dibuja el vector en función de ambas bases, para aclarar un poco todo este follón. Si queremos escribir $v_B$ en la base C:

$$v_B =a\cdot b_1 +b\cdot b_2 =a\cdot \left(x\cdot c_1 +y\cdot c_2 \right)+b\cdot \left(z\cdot c_1 +t\cdot c_2 \right)=v_C$$

$$v_B =a\cdot x\cdot c_1 +a\cdot y\cdot c_2 +b\cdot z\cdot c_1 +b\cdot t\cdot c_2 =v_C$$

$$v_B =\left(a\cdot x+b\cdot z\right){\cdot c}_1 +\left(a\cdot y+b\cdot t\right)\cdot c_2 =v_C$$

La forma matricial es más sencilla de conseguir, directamente de la relación entre las bases:

$$v_B =\left\lbrack a\;b\right\rbrack \left\lbrack \begin{array}{c}
b_1 \\
b_2
\end{array}\right\rbrack =\left\lbrack a\;b\right\rbrack \left\lbrack \begin{array}{cc}
x & y\\
z & t
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
c_1 \\
c_2
\end{array}\right\rbrack =v_C$$

De esta última relación vemos que:

$$\begin{array}{l}
v_B =\left\lbrack a\;b\right\rbrack \\
v_C =\left\lbrack a\;b\right\rbrack \left\lbrack \begin{array}{cc}
x & y\\
z & t
\end{array}\right\rbrack
\end{array}$$

Como habitualmente trabajamos con los vectores en columnas, trasponemos las matrices; para ello recuerda que ${\left(A\;x\;B\right)}^t \;=B^t \;{x\;A}^t$:

$$v_C =\left\lbrack \begin{array}{cc}
x & z\\
y & t
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
a\\
b
\end{array}\right\rbrack$$

O bien:

$$\left\lbrack \begin{array}{c}
v_{\textrm{cx}} \\
v_{\textrm{cy}}
\end{array}\right\rbrack =\left\lbrack \begin{array}{cc}
x & z\\
y & t
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
v_{\textrm{bx}} \\
v_{\textrm{by}}
\end{array}\right\rbrack$$

Vemos que la matriz de cambio de base está constituída por las coordenadas de los vectores de la base B en la base C, en columnas.

Si quiero hacer el cambio inverso, multiplico por la izquierda por la inversa de la matriz de cambio de base:

$${\left\lbrack \begin{array}{cc}
x & z\\
y & t
\end{array}\right\rbrack }^{-1} \left\lbrack \begin{array}{c}
v_{\textrm{cx}} \\
v_{\textrm{cy}}
\end{array}\right\rbrack =\left\lbrack \begin{array}{c}
v_{\textrm{bx}} \\
v_{\textrm{by}}
\end{array}\right\rbrack$$

Ejemplo

Consideramos la base canónica de $R^2$: $\textrm{BC}=\left\lbrace \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
0\\
1
\end{array}\right\rbrack \right\rbrace$, y otros dos vectores, que veremos que son linealmente independientes (pues no son uno múltiplo del otro) que, por tanto, también forman base: $V=\left\lbrace \left\lbrack \begin{array}{c}
1\\
3
\end{array}\right\rbrack ,\left\lbrack \begin{array}{c}
-1\\
2
\end{array}\right\rbrack \right\rbrace$.

Los dibujamos a continuación:

```matlab
clear; clc;
fig = figure;
quiver(0,0,1,0,1,'b','LineWidth',1)
text(1.1,0,'i')
hold on
quiver(0,0,0,1,1,'b','LineWidth',1)
text(0.1,1,'j')
grid on
xlim([-4,4])
xticks(-5:5)
axis equal
quiver(0,0,1,3,1,'r','LineWidth',1)
text(1.1,3,'v1')
quiver(0,0,-1,2,1,'r','LineWidth',1)
text(-0.9,2,'v2')
xlabel('x')
ylabel('y')
savefig('cambas')
```

**Salida:**
```text
[figura]
```

Vamos a obtener las coordenadas de V en BC:

```matlab
i = [1;0]
j = [0;1]
v1 = [1;3]
v2 = [-1;2]
syms a b c d
ec1 = v1 == a*i + b*j
ec2 = v2 == c*i + d*j
sol = solve([ec1;ec2])
```

**Salida:**
```text
i =
j =
v1 =
v2 =
-1
ec1 = ([1=a; 3=b])
ec2 = ([-1=c; 2=d])
sol = struct with fields:
a: 1
b: 3
c: -1
d: 2
```

Recuerda que si quieres huir de las estructuras, también puedes obtener explícitamente los valores de las incógnitas:

```matlab
[a b c d] = solve([ec1;ec2])
```

**Salida:**
```text
a = 1
b = 3
c = -1
d = 2
```

La matriz de cambio de base, M, de B a C , será:

```matlab
M = [sol.a sol.c;sol.b sol.d]
```

**Salida:**
```text
M = ([1, -1; 3, 2])
```

Es decir, las columnas son los vectores de C referidos a B. Si la aplicamos a los vectores de la base canónica, deberemos obtener los vectores de V:

```matlab
v1_V = M*i
V2_V = M*j
```

**Salida:**
```text
v1_V = ([1; 3])
V2_V = ([-1; 2])
```

O:

```matlab
V = M*[i j]
```

**Salida:**
```text
V = ([1, -1; 3, 2])
```

Es decir, hemos hallado la base v en función de la BC; el resultado es lógico, dado que los vectores de la BC forman la matriz unidad. M es la matriz que representa los vectores de V en BC.

La matriz de cambio de base de V a BC será $M^{-1}$:

```matlab
i_c = inv(M)*v1
j_c = inv(M)*v2
```

**Salida:**
```text
i_c = ([1; 0])
j_c = ([0; 1])
```

O:

```matlab
BC = inv(M)*V
```

**Salida:**
```text
BC = ([1, 0; 0, 1])
```

Consideremos un vector x referido a la base canónica: $x=\left\lbrace \left\lbrack \begin{array}{c}
3\\
5
\end{array}\right\rbrack \right\rbrace$. Lo referimos a la base V. Para ello necesitamos la MCB que representa los vectores de la base de partida en función de los de la base de llegada; o sea, los vectores de BC en V.

```matlab
x = [3;5]
x_BC = x;
x_V = inv(M)*x_BC
X_V = double(x_V)
```

**Salida:**
```text
x =
x_V = ([(11)/(5); -(4)/(5)])
X_V =
2.2000
-0.8000
```

Dibujamos:

```matlab
openfig("cambas.fig");
hold on
ylim([-2,8])
quiver(0,0,x(1),x(2),1,'g','LineWidth',2)
text(x(1)+0.1,x(2),'x')
quiver(0,0,x(1)*i(1),x(1)*i(2),1,'--b')
quiver(0,0,x(2)*j(1),x(2)*j(2),1,'--b')
quiver(0,0,x_V(1)*v1(1),x_V(1)*v1(2),1,'--r')
quiver(0,0,x_V(2)*v2(1),x_V(2)*v2(2),1,'--r')
plot([x_V(1)*v1(1),x(1)],[x_V(1)*v1(2),x(2)],':r')
plot([x_V(2)*v2(1),x(1)],[x_V(2)*v2(2),x(2)],':r')
plot([x(1)*i(1),x(1)],[x(1)*i(2),x(2)],':b')
plot([x(2)*j(1),x(1)],[x(2)*j(2),x(2)],':b')
```

**Salida:**
```text
[figura]
```

Contenido

#### Problema 1

Escoger una base ortogonal de $R^2$, de la que sabemos que uno de sus vectores, referido a la base canònica, es $b_1 =\left\lbrack \begin{array}{c}
-1\\
2
\end{array}\right\rbrack$. Normalizar la base obtenida.

Solución

El vector $b_2$ que, unido a $b_1$, debe formar una base ortogonal de $R^2$, debe cumplir dos condiciones:

- Ser linealmente independiente de $b_1$; dos vectores linealmente independientes de $R^2$ forman base

- Ambos deben ser perpendiculares. Es decir, su producto escalar debe valer 0. Si son perpendiculares es evidente que son independientes.

```matlab
clear; clc;
syms x y
b1 = [-1;2]
b2 = [x;y]
B = [b1 b2]
ec1 = dot(b1,b2) == 0
y1 = solve(ec1,y)
```

**Salida:**
```text
b1 =
-1
b2 = ([x; y])
B = ([-1, x; 2, y])
ec1 = 2⁢y-x=0
y1 = (x)/(2)
```

Por tanto, una solución para el vector $b_2$ será:

```matlab
x1 = 1
b21 = subs(b2,[x,y],[x1,subs(y1,x,x1)])
B = [b1,b21]
```

**Salida:**
```text
x1 =
b21 = ([1; (1)/(2)])
B = ([-1, 1; 2, (1)/(2)])
```

Ambos vectores son linealmente independientes:

```matlab
GJ = rref(B)
```

**Salida:**
```text
GJ = ([1, 0; 0, 1])
```

Los dibujamos:

```matlab
fig = figure;
quiver(0,0,b1(1),b1(2),1,'b')
xlim([-3,3])
axis equal
grid on
xline(0)
yline(0)
hold on
quiver(0,0,b21(1),b21(2),1,'b')
text(b1(1)+0.1,b1(2),'b1')
text(b21(1)+0.1,b21(2),'b2')
savefig('base')
```

**Salida:**
```text
[figura]
```

La base ortonormal es:

```matlab
Bon = [b1/norm(b1) b21/norm(b21)]
openfig('base');
quiver(0,0,Bon(1,1),Bon(2,1),1,'r','LineWidth',2)
quiver(0,0,Bon(1,2),Bon(2,2),1,'r','LineWidth',2)
Bon1 = double(Bon)
```

**Salida:**
```text
Bon = ([-(sqrt(5))/(5), (2⁢sqrt(5))/(5); (2⁢sqrt(5))/(5), (sqrt(5))/(5)])
[figura]
Bon1 =
-0.4472  0.8944
0.8944  0.4472
v =
0.5000
3.0000
vb = ([v_1; v_2])
ec = [([(1)/(2)=σ_1, (1)/(2)=σ_2; 3=σ_1, 3=σ_2]); ; where; ; σ_1=(2⁢sqrt(5)⁢v_2‾)/(5)-(sqrt(5)⁢v_1‾)/(5); ; σ_2=(2⁢sqrt(5)⁢v_1‾)/(5)+(sqrt(5)⁢v_2‾)/(5)]
A = ([0, 0; 0, 0; 0, 0; 0, 0])
b = ([(sqrt(5)⁢0‾)/(5)-(1)/(2); (sqrt(5)⁢0‾)/(5)-3; (3⁢sqrt(5)⁢0‾)/(5)-(1)/(2); (3⁢sqrt(5)⁢0‾)/(5)-3])
```

Contenido

#### Problema 2

Sean dos bases, B1 y B2 de $R^2$ referidas a la base canónica:

$$B_1 =\left\lbrace \left\lbrack \begin{array}{c}
-1\\
1
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
1\\
0
\end{array}\right\rbrack \right\rbrace$$

$$B_2 =\left\lbrace \left\lbrack \begin{array}{c}
0\\
-2
\end{array}\right\rbrack \left\lbrack \begin{array}{c}
1\\
2
\end{array}\right\rbrack \right\rbrace$$

Se tiene el vector $X_{\textrm{B1}} =\left\lbrack \begin{array}{c}
5\\
-2
\end{array}\right\rbrack$, referido a la base $B_1$. Se pide expresarlo en la base $B_2$.

Solución 1

Se pasa $X_{\textrm{B1}} \;$a la base canónica y de ésta a B2.

```matlab
clear; clc;
% Paso a la BC
MCB = [-1 1;1 0]
x_B1 = [5;-2]

xBC = MCB*x_B1

fig = figure;
quiver(0,0,x_B1(1),x_B1(2),1,'g','LineWidth',2)
hold on
quiver(0,0,MCB(1,1),MCB(2,1),1,'r','LineWidth',2)
quiver(0,0,MCB(1,2),MCB(2,2),1,'r','LineWidth',2)

xlabel('x')
ylabel('y')
grid on
axis equal
xline(0)
yline(0)
xlim([-5,10])
xticks(-5:10)

% Paso a la base B2 desde BC
MCB = inv([0 1;-2 2])
xB2 = MCB * xBC
quiver(0,0,MCB(1,1),MCB(2,1),1,'b','LineWidth',2)
quiver(0,0,MCB(1,2),MCB(2,2),1,'b','LineWidth',2)
```

**Salida:**
```text
MCB =
-1  1
1  0
x_B1 =
-2
xBC =
-7
MCB =
1.0000  -0.5000
1.0000  0
xB2 =
-9.5000
-7.0000
[figura]
```

Solución 2

Se hallan los vectores de $B_1$ en $B_2$. Sus coordenadas, por columnas, serán la matriz de cambio de base:

```matlab
syms a b c d
ec1 = [-1;1] == a*[0;-2] + b*[1;2]
ec2 = [1;0] == c*[0;-2] + d*[1;2]

ec = [ec1;ec2]

[a,b,c,d] = solve(ec)

MCB = [a c;b d]
xB2_1 = MCB*x_B1
xB2_1 = double(xB2_1)
```

**Salida:**
```text
ec1 = ([-1=b; 1=2⁢b-2⁢a])
ec2 = ([1=d; 0=2⁢d-2⁢c])
ec = ([-1=b; 1=2⁢b-2⁢a; 1=d; 0=2⁢d-2⁢c])
a = -(3)/(2)
b = -1
c = 1
d = 1
MCB = ([-(3)/(2), 1; -1, 1])
xB2_1 = ([-(19)/(2); -7])
xB2_1 =
-9.5000
-7.0000
```

Vemos que ambos procedimientos dan el mismo resultado, con lo que nos emocionamos profundamente.

_Imágenes embebidas: 1 (image1.png)_


## Live Script: funciones auxiliares (EV_tools)

*Fuente: `EV_tools.mlx`*

```matlab
clear; clc;
syms a b c d

u1 = [1;0]
u2 = [0;1]
v1 = [1;3]
v2 = [-1;2]

ecs1 = u1 == a*v1 + b*v2
ecs2 = u2 == c*v1 + d*v2
ecs = [ecs1;ecs2]

sol = solve(ecs)
```

**Salida:**
```text
u1 =
u2 =
v1 =
v2 =
-1
ecs1 = ([1=-b+a; 0=2⁢b+3⁢a])
ecs2 = ([0=-d+c; 1=2⁢d+3⁢c])
ecs = ([1=-b+a; 0=2⁢b+3⁢a; 0=-d+c; 1=2⁢d+3⁢c])
sol = struct with fields:
a: 2/5
b: -3/5
c: 1/5
d: 1/5
```
