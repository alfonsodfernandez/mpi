# Proyecto 01: red logística

Enunciado del proyecto, datos (Excel) y plantilla MATLAB.

**Contenido de este archivo:**
- Enunciado del proyecto
- Datos del proyecto
- Plantilla MATLAB


## Enunciado del proyecto

*Fuente: `PROYECTO/P01 Red Logistica.pdf`*

#### Página 1

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para
proporcionar información objetiva que apoye la toma de decisiones
estratégicas sobre su diseño, funcionamiento y optimización.
____________________________________________________________

1  INTRODUCCIÓN .....................................................................................................................2
1.1  METODOLOGÍA DE TRABAJO ................................................................................................2
1.2  REQUISITOS PREVIOS ............................................................................................................2
2  COMPRENSIÓN DEL PROBLEMA Y ANÁLISIS DEL CONTEXTO ................................3
2.1  CONTEXTO ...........................................................................................................................3
2.2  INFORMACIÓN DISPONIBLE ..................................................................................................3
2.3  OBJETIVO DEL PROYECTO .....................................................................................................5
2.4  RESTRICCIONES ....................................................................................................................5
3  RETOS DE INVESTIGACIÓN ................................................................................................5
3.1  RETO 1. ESTIMACIÓN DE LA DEMANDA LOGÍSTICA FUTURA .................................................5
3.1.1  Contexto ........................................................................................................................5
3.1.2  Objetivo .........................................................................................................................6
3.1.3  Producto esperado ........................................................................................................6
3.1.4  Formato de resultados numéricos: ..............................................................................7
3.1.5  Recursos recomendados: ..............................................................................................7
3.1.6  Funciones Matlab ..........................................................................................................7
3.2  RETO 2. REPRESENTACIÓN MATEMÁTICA DE LA RED LOGÍSTICA ..........................................7
3.2.1  Contexto ........................................................................................................................7
3.2.2  Objetivo .........................................................................................................................7
3.2.3  Producto esperado ........................................................................................................8
3.2.4  Formato de resultados numéricos: ..............................................................................8
3.2.5  Recursos recomendados: ..............................................................................................8
3.2.6  Funciones Matlab: .........................................................................................................8
3.3  RETO 3. ALMACENAMIENTO Y REPRESENTACIÓN COMPUTACIONAL DE LA RED ...................8
3.3.1  Contexto ........................................................................................................................8
3.3.2  Objetivo .........................................................................................................................8
3.3.3  Producto esperado y formato.......................................................................................9
3.3.4  Formato de resultados numéricos: ..............................................................................9
3.3.5  Recursos recomendados: ..............................................................................................9
3.3.6  Funciones Matlab: .........................................................................................................9
3.4  RETO 4. ANÁLISIS DEL COMPORTAMIENTO DINÁMICO DE LA RED ........................................9
3.4.1  Contexto ........................................................................................................................9
3.4.2  Objetivo ....................................................................................................................... 10
3.4.3  Producto esperado ...................................................................................................... 10
3.4.4  Formato de resultados numéricos: ............................................................................ 10
3.4.5  Recursos recomendados: ............................................................................................ 10
3.4.6  Funciones Matlab: ....................................................................................................... 11
3.5  RETO 5. ANÁLISIS DE LA IMPORTANCIA ESTRUCTURAL DE LA RED LOGÍSTICA .................... 11
3.5.1  Contexto ...................................................................................................................... 11
3.5.2  Objetivo ....................................................................................................................... 11
3.5.3  Producto esperado ...................................................................................................... 11
3.5.4  Formato de resultados numéricos: ............................................................................ 12
3.5.5  Recursos recomendados: ............................................................................................ 12
3.5.6  Funciones Matlab: ....................................................................................................... 12
3.6  RETO 6. ANÁLISIS DE ESCENARIOS Y APOYO A LA TOMA DE DECISIONES ............................ 12
3.6.1  Contexto ...................................................................................................................... 12
3.6.2  Objetivo ....................................................................................................................... 12
3.6.3  Producto esperado ...................................................................................................... 13
3.6.4  Formato de resultados numéricos: ............................................................................ 13

__________________________________________________________________________________________________________

Página 1 de 16
```

#### Página 2

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

3.6.5  Fuentes......................................................................................................................... 14
3.6.6  Funciones Matlab ........................................................................................................ 14
3.7  FUENTES: ........................................................................................................................... 14
3.8  CALENDARIO, INFORME FINAL Y RÚBRICAS DE EVALUACIÓN ............................................. 14
3.8.1  Calendario de entregas ............................................................................................... 14
3.8.2  Estructura de las entregas parciales y el informe Final ............................................ 14
3.9  RÚBRICAS DE EVALUACIÓN................................................................................................ 15
3.10  USO DE HERRAMIENTAS DE INTELIGENCIA ARTIFICIAL ...................................................... 16

1  Introducción

Bienvenidos al Proyecto P01: Análisis de una red logística para el apoyo a la toma de decisiones.

A diferencia de las prácticas tradicionales, este proyecto no consiste en resolver una sucesión de
ejercicios independientes ni en aplicar procedimientos previamente explicados en clase.

Durante las próximas semanas formaréis parte de un equipo de consultoría contratado por la
empresa ficticia LOGISPAÑA. Vuestra misión será desarrollar una metodología matemática y
computacional capaz de analizar una red logística y proporcionar información útil para apoyar
decisiones estratégicas.

A lo largo del proyecto os enfrentaréis a distintos problemas para los que inicialmente quizá no
conozcáis la solución. Esto es completamente intencionado. En la práctica profesional, los
ingenieros rara vez disponen de todos los conocimientos necesarios antes de comenzar un
proyecto. Deben investigar, seleccionar herramientas, justificar sus decisiones y construir
progresivamente una solución.

Por este motivo, este proyecto combina tres tipos de aprendizaje:
i.  Investigación autónoma, apoyada en bibliografía y documentación técnica.
ii.  Modelización matemática, utilizando los conocimientos adquiridos durante la
asignatura.
iii.  Desarrollo computacional, mediante MATLAB.

El objetivo no es únicamente obtener un resultado correcto, sino justificar todo el proceso seguido
hasta alcanzarlo.
No existe una única solución válida. Se valorará especialmente la capacidad para razonar,
justificar las decisiones adoptadas y comunicar los resultados de forma clara y rigurosa.
Esperamos que al finalizar el proyecto no solo hayáis aprendido nuevos conceptos matemáticos,
sino también una forma de trabajar más cercana a la realidad de la ingeniería.

1.1  Metodología de trabajo

Para resolver cada reto no se espera que el estudiante conozca previamente todas las
herramientas matemáticas necesarias.

Cada fase requiere una investigación autónoma apoyada en la bibliografía recomendada, la
documentación oficial de MATLAB y otras fuentes académicas fiables.

El informe deberá explicar no solamente la solución obtenida sino también el proceso seguido
para llegar a ella.

1.2  Requisitos previos
```

#### Página 3

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

Para desarrollar el proyecto se presupone que todos los integrantes del equipo han adquirido las
competencias básicas en MATLAB mediante la realización de los siguientes cursos oficiales de
MathWorks:
  MATLAB Onramp
  Make and Manipulate Matrices
  Calculations with Vectors and Matrices
  Introduction to Linear Algebra with MATLAB

Estos cursos proporcionan los conocimientos necesarios para el manejo del entorno MATLAB y
las operaciones matriciales básicas. El proyecto se centrará en la aplicación de dichas
herramientas a la resolución de un problema de ingeniería, por lo que no se desarrollarán
contenidos básicos de programación durante las sesiones del proyecto.

La realización de los citados cursos es condición previa a la evaluación del proyecto

2  Comprensión del problema y análisis del contexto
2.1  Contexto

La empresa LOGISPAÑA es uno de los principales operadores logísticos nacionales. Cada día
coordina el transporte de mercancías entre numerosos centros de distribución repartidos por toda
España.

Durante los últimos años la empresa ha experimentado un importante crecimiento. Como
consecuencia, la red logística se ha vuelto cada vez más compleja y actualmente resulta difícil
responder con rapidez a cuestiones estratégicas relacionadas con su funcionamiento.

La Dirección de Operaciones considera que muchas decisiones se siguen tomando, apoyándose
únicamente en la experiencia de los responsables regionales, sin disponer de herramientas
objetivas que permitan analizar el comportamiento global de la red.

Con el fin de mejorar la planificación logística, la empresa desea desarrollar una metodología
capaz de representar matemáticamente la red de distribución y proporcionar información útil
para la toma de decisiones. Para ello ha contratado a vuestro equipo de consultoría.

Vuestra misión consiste en estudiar la red actual y proponer un procedimiento que permita
analizarla de forma automática.

2.2  Información disponible

La empresa os facilita inicialmente la siguiente información.

CENTROS DE DISTRIBUCIÓN
Código  Localidad  Tipo
M  Madrid  hub nacional
B  Barcelona  hub nacional
V  Valencia  hub nacional
Z  Zaragoza  hub regional
S  Sevilla  hub regional
BI  Bilbao  hub regional
MA  Málaga  distribución
MU  Murcia  distribución
```

#### Página 4

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

VA  Valladolid  distribución
CO  Córdoba  distribución
AL  Alicante  distribución
GE  Gerona  distribución

FLUJOS SEMANALES
Origen  Destino  Flujo
Madrid  Zaragoza 850
Madrid  Valencia  780
Madrid  Sevilla  620
Madrid  Valladolid 430
Zaragoza Barcelona 760
Zaragoza Bilbao  410
Zaragoza Valencia  390
Barcelona Gerona  520
Barcelona Valencia  610
Barcelona Zaragoza 300
Valencia  Murcia  570
Valencia  Alicante  640
Valencia  Madrid  350
Sevilla  Córdoba  480
Sevilla  Málaga  530
Córdoba  Madrid  260
Málaga  Sevilla  240
Bilbao  Valladolid 310
Valladolid Madrid  290
Murcia  Valencia  220
Alicante  Valencia  260
Gerona  Barcelona 180

  Cada centro logístico puede enviar mercancías a uno o varios centros.
  No todas las conexiones tienen la misma intensidad.
  El volumen semanal de mercancías en toneladas transportadas entre dos centros es
conocido.
  Algunas conexiones son bidireccionales y otras únicamente funcionan en un sentido.
  La empresa prevé ampliar considerablemente la red durante los próximos años.
  En una primera fase del estudio se trabajará con una versión reducida de la red formada
por las siguientes localidades:
o Madrid, Barcelona, Zaragoza, Valencia, Sevilla, Bilbao, Valladolid, Málaga,
Córdoba, Murcia, Alicante y Gerona.
  Posteriormente el mismo procedimiento deberá ser capaz de analizar una red formada
por varios cientos de centros logísticos.

2.2.1  Fuente de los datos

Los datos necesarios para desarrollar el proyecto se proporcionan en el archivo P01 Datos.xlsx.
```

#### Página 5

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

Este archivo contiene, en distintas hojas, la información relativa a los centros de distribución, los
flujos semanales entre centros y la evolución histórica del volumen de mercancías.

Los datos deberán importarse directamente desde MATLAB. No se permite copiarlos
manualmente en el Live Script mediante la definición explícita de vectores o matrices.

Esta forma de trabajo responde a uno de los objetivos fundamentales del proyecto: desarrollar un
procedimiento automatizable y escalable. El código deberá funcionar sin modificaciones
sustanciales cuando se añadan nuevos centros, rutas o datos históricos a la hoja de cálculo.
2.3  Objetivo del proyecto

La Dirección General desea disponer de una herramienta que permita responder, entre otras, a
las siguientes cuestiones:

  ¿Qué centros desempeñan un papel más importante dentro de la red logística?
  ¿Qué centros podrían cerrarse o fusionarse con otros minimizando el impacto sobre el
funcionamiento global?
  ¿Cómo afectaría a la red la interrupción temporal de un determinado centro logístico?
  ¿Qué centros deberían priorizarse en futuras inversiones?

Actualmente ninguna de estas preguntas puede responderse de forma objetiva utilizando
únicamente la información disponible.
2.4  Restricciones

La empresa establece además las siguientes condiciones:
  El procedimiento desarrollado deberá poder aplicarse tanto a la red reducida como a
redes mucho mayores.
  La metodología utilizada deberá ser fácilmente automatizable mediante herramientas
informáticas.
  Todas las decisiones deberán estar justificadas mediante criterios objetivos y
reproducibles.
  La empresa no presupone qué técnicas matemáticas deberán utilizarse. Será
responsabilidad del equipo de consultoría investigar y seleccionar aquellas herramientas
que consideren más adecuadas.

Observación: En proyectos reales de ingeniería es habitual que el cliente describa el problema, pero
no indique el método matemático que debe emplearse para resolverlo.

No existe una única solución correcta para este proyecto. Se valorará especialmente la capacidad
para justificar las decisiones adoptadas y la solidez del razonamiento empleado.

3  Retos de investigación
3.1  Reto 1. Estimación de la demanda logística futura
3.1.1  Contexto

Antes de acometer cualquier inversión en infraestructuras o de rediseñar su red de distribución,
la Dirección General de LOGISPAÑA desea conocer cómo evolucionará previsiblemente la
demanda logística durante los próximos años.

La empresa dispone únicamente del histórico del volumen total de mercancías gestionadas
durante la última década. Aunque estos datos reflejan una tendencia creciente, la Dirección
considera que una simple inspección visual resulta insuficiente para estimar con fiabilidad la
demanda futura y fundamentar decisiones de inversión.
```

#### Página 6

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

Con el fin de planificar adecuadamente la capacidad de la red logística, la empresa solicita a
vuestro equipo el desarrollo de un modelo matemático que describa la evolución observada y
permita realizar estimaciones para los próximos años.

Los datos históricos disponibles son los siguientes:

Volumen de
mercancías
Año
(miles de
toneladas)
2016  15.2
2017  16.1
2018  17.0
2019  18.4
2020  18.0
2021  19.6
2022  20.8
2023  22.1
2024  23.4
2025  24.8

La Dirección General desea conocer cuál podría ser la demanda esperada en el año 2028, ya que
esta previsión servirá como punto de partida para el estudio de la red logística desarrollado en
los siguientes retos del proyecto.

3.1.2  Objetivo

Desarrollar un modelo matemático que describa la evolución temporal del volumen de
mercancías gestionado por LOGISPAÑA y que permita realizar una estimación razonada de la
demanda futura.

Para ello será necesario:
a) representar gráficamente los datos históricos proporcionados
b) investigar qué tipo de modelo matemático resulta adecuado para describir la tendencia
observada;
c) comparar distintas alternativas y justificar la elección del modelo finalmente adoptado;
d) utilizar dicho modelo para estimar el volumen de mercancías esperado en el año 2028;
e) valorar la fiabilidad de la predicción obtenida y discutir las limitaciones del modelo
utilizado.

Las conclusiones obtenidas deberán servir para justificar la necesidad del estudio de la red
logística desarrollado en el resto del proyecto.

3.1.3  Producto esperado

Al finalizar este reto, el equipo deberá presentar:
a) una representación gráfica de los datos históricos y las funciones polinómicas
consideradas (en una sola gráfica) 1
b) una comparación entre los distintos modelos considerados empleando el RMSE de cada
uno de ellos (ver función rmse)
c) el modelo matemático seleccionado (su ecuación) y la justificación de su elección;
d) la estimación del volumen de mercancías para el año 2028 y el incremento porcentual
previsto para 2028

1 Se aconseja desplazar el origen del eje de abscisas de modo que el primer año corresponda a 0
```

#### Página 7

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

e) una valoración crítica sobre la calidad del ajuste obtenido y la fiabilidad de las
predicciones realizadas.
f) una breve conclusión en la que se explique cómo las previsiones obtenidas justifican el
análisis de la red logística que se desarrollará en los siguientes retos del proyecto.

3.1.4  Formato de resultados numéricos:

a)  Gráfica hasta 2028
b)  Tabla en la que las filas representan cada modelo y la columna su error de ajuste
c)  Ecuación con fprintf cada coeficiente con 8 decimales
d)  Se deben dar los resultados en forma de tabla cuyas columnas sean el grado del
polinomio, su RMSE, su predicción para 2028 y el % de incremento respecto a 2025

3.1.5  Recursos recomendados:

[1] P.36
[3] P.91
[4] P.78, 207
Ajuste polinomial de curvas. MathWorks
[6] Anexo: Ajuste por mínimos cuadrados.
[7] Anexo: Interpolación y ajuste de curvas. Pags 15-22

3.1.6 Funciones Matlab
polyfit, polyval, rmse, zeros, cell, figure, plot, hold, numel, xlabel
, ylabel, legend, grid, table, disp, fprintf, abs

3.2  Reto 2. Representación matemática de la red logística

3.2.1  Contexto

La empresa LOGISPAÑA os ha facilitado una relación de localidades españolas entre las que
existe un flujo habitual de mercancías, así como el volumen medio semanal transportado entre
cada par de localidades.

En estos momentos la información únicamente está disponible en forma de tabla de datos. Sin
embargo, los responsables de la empresa consideran que este formato resulta poco adecuado para
analizar el comportamiento global de la red y dificulta enormemente la automatización de
futuros estudios.

3.2.2  Objetivo

El segundo objetivo del proyecto consiste en encontrar una forma de representar
matemáticamente la red de distribución de manera que:

a)  permita visualizar las relaciones existentes entre las distintas localidades;
b)  facilite el almacenamiento de la información en un ordenador;
c)  pueda ampliarse fácilmente cuando la red aumente de tamaño;
d)  constituya la base para los análisis posteriores.

Como equipo de consultoría, debéis investigar qué herramientas matemáticas permiten modelar
este tipo de problemas y justificar cuál de ellas resulta más adecuada para el caso planteado.

Una vez seleccionada la representación matemática, deberéis construir el modelo
correspondiente para la red suministrada por la empresa.
```

#### Página 8

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

3.2.3  Producto esperado

Al finalizar este reto, el equipo deberá haber obtenido una representación matemática completa
de la red logística y justificar las razones por las que considera que dicha representación resulta
adecuada para el problema planteado.

Investiga y responde:
a)  ¿Qué estructura matemática permite representar este tipo de problemas?
b)  ¿Qué representan sus elementos?
c)  ¿Qué ventajas ofrece frente a una simple tabla?
d)  Busca dos aplicaciones distintas de esta estructura.

3.2.4  Formato de resultados numéricos:

Se debe dar una representación gráfica de la red

3.2.5  Recursos recomendados:

[1] P.164
[2] P.247
[3] P.561
[4] P.125
Directed and Undirected Graphs. MathWorks.

3.2.6  Funciones Matlab:

digraph, plot, title, numnodes, numedges, fprintf, clear, clc, close

3.3  Reto 3. Almacenamiento y representación computacional de la red

3.3.1  Contexto

Tras el estudio realizado en la fase anterior, la empresa LOGISPAÑA dispone ya de una
representación matemática adecuada de su red logística. Sin embargo, la Dirección de Sistemas
plantea una nueva dificultad.

Aunque la representación gráfica resulta muy útil para comprender visualmente la estructura de
la red, deja de ser práctica cuando el número de centros logísticos aumenta considerablemente.
La empresa prevé ampliar su red en los próximos años hasta varios cientos de localidades
distribuidas por todo el territorio nacional.

En estas condiciones, representar y analizar la red únicamente mediante diagramas deja de ser
viable. Además, la empresa desea desarrollar una aplicación informática capaz de realizar
automáticamente distintos análisis sobre la red, lo que exige almacenar toda la información en
un formato adecuado para su tratamiento mediante ordenador.

Como equipo de consultoría, debéis investigar qué representación matemática permite
almacenar una red de este tipo de forma eficiente, facilitando tanto su manipulación mediante
MATLAB como el desarrollo de algoritmos de análisis posteriores.

3.3.2  Objetivo

El objetivo de esta fase consiste en diseñar una estructura matemática que permita representar de
forma completa la red logística en un ordenador.
```

#### Página 9

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

La representación elegida deberá:
a)  almacenar todas las conexiones existentes entre las distintas localidades;
b)  incorporar el volumen de mercancías transportado entre ellas;
c)  ser fácilmente ampliable cuando aumente el número de centros logísticos;
d)  permitir el desarrollo de algoritmos de análisis de forma eficiente;
e)  servir como base para las fases posteriores del proyecto.

Una vez seleccionada la representación más adecuada, deberéis construirla para la red logística
proporcionada por la empresa utilizando MATLAB.

3.3.3  Producto esperado y formato

Al finalizar esta fase, el equipo deberá haber obtenido una representación matemática completa
de la red logística y justificar por qué constituye una solución adecuada para el almacenamiento
y tratamiento computacional de la información.

3.3.4  Formato de resultados numéricos:

El resultado debe presentarse en dos tablas:
a) En la primera tabla se muestran los flujos entre centros mostrando los nombres de filas y
columnas de modo que pueda verificarse el resultado con los datos proporcionados
b) En la segunda tabla las columnas deben mostrar el flujo entrante y saliente de cada centro

Asimismo, deberá explicarse el significado de cada elemento de la matriz construida y cómo
puede recuperarse a partir de ella la información original de la red.
Debe verificarse que los datos son correctos mediante los flujos entrantes/salientes así como el
número total de rutas

3.3.5  Recursos recomendados:

Los mismos del Reto 1

3.3.6 Funciones Matlab:
adjacency, full, array2table, cellstr, disp, sum, table, abs

3.4  Reto 4. Análisis del comportamiento dinámico de la red

3.4.1  Contexto

Una vez construida la representación computacional de la red logística, la Dirección de
Operaciones plantea una nueva cuestión.

Hasta este momento el análisis realizado se ha centrado exclusivamente en la estructura de la red:
qué centros están conectados entre sí y cuál es el volumen de mercancías transportado entre ellos.
Sin embargo, los responsables de la empresa consideran que esta información resulta insuficiente
para comprender el funcionamiento global del sistema.

En la práctica, las mercancías no permanecen indefinidamente en un centro logístico. Tras ser
recibidas, son clasificadas y expedidas hacia otros centros de la red siguiendo los flujos habituales
de distribución.

La Dirección desea conocer cómo evolucionaría la distribución de la actividad logística si este
proceso de redistribución se mantuviera durante un largo periodo de tiempo.

En particular, interesa responder a cuestiones como:
```

#### Página 10

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

a)  ¿La actividad tenderá a concentrarse en determinados centros logísticos?
b)  ¿Existirá una distribución estable del tráfico dentro de la red?
c)  ¿Dependerá dicha distribución de la situación inicial?
d)  ¿Puede conocerse este comportamiento sin necesidad de realizar miles de simulaciones
individuales?

Responder a estas preguntas permitirá comprender mucho mejor el funcionamiento global de la
red y servirá de base para las decisiones estratégicas que deberán adoptarse en las siguientes fases
del proyecto.

Como equipo de consultoría, debéis investigar qué herramientas matemáticas permiten estudiar
la evolución temporal de sistemas formados por estados interconectados y cómo pueden
aplicarse al problema planteado.

3.4.2  Objetivo

El objetivo de esta fase consiste en desarrollar un modelo matemático que permita analizar la
evolución de la actividad logística dentro de la red cuando las mercancías circulan continuamente
entre los distintos centros de distribución.

La metodología propuesta deberá permitir:
a)  describir matemáticamente la evolución del sistema;
b)  estudiar su comportamiento tras un gran número de etapas;
c)  determinar si existe una situación de equilibrio o estabilidad;
d)  analizar el significado logístico de dicho equilibrio;
e)  automatizar completamente el proceso mediante MATLAB.

3.4.3  Producto esperado

Al finalizar esta fase, el equipo deberá haber desarrollado un procedimiento que permita estudiar
el comportamiento dinámico de la red logística y obtener la distribución de actividad cuando el
sistema alcanza un régimen estable.

El informe deberá explicar:
a)  el modelo matemático adoptado;
b)  las hipótesis realizadas;
c)  la interpretación física o logística de los resultados obtenidos;
d)  las limitaciones del modelo.

3.4.4  Formato de resultados numéricos:

La situación de equilibrio debe calcularse mediante tres métodos matemáticos. Se debe calcular
la situación de equilibrio mediante los tres métodos con un error menor que 10−12 . El resultado
debe darse mediante una tabla ordenada de mayor a menor indicando los nombres de los centros
(filas) y el % de flujo de mercancías

Finalmente se debe calcular la bondad de cada método mediante la norma del residuo
correspondiente y dar los resultados mediante una tabla

3.4.5  Recursos recomendados:

[1] P.72
[2] P.236, P336
[3] P.336
[4] P.149
[5] Anexo. Residuo
```

#### Página 11

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

3.4.6 Funciones Matlab:
sum, eig, null, norm, table, disp

3.5  Reto 5. Análisis de la importancia estructural de la red logística

3.5.1  Contexto

La Dirección General de LOGISPAÑA debe decidir durante el próximo ejercicio qué centros
logísticos serán objeto de un plan de modernización. Debido a las limitaciones presupuestarias,
únicamente podrán acometerse actuaciones en un número reducido de instalaciones.

Hasta el momento, estas decisiones se han basado principalmente en el volumen de mercancías
gestionado por cada centro. Sin embargo, distintos responsables consideran que este criterio
puede no reflejar la verdadera importancia de un centro dentro del funcionamiento global de la
red.

La Dirección General solicita a vuestro equipo que desarrolle un procedimiento objetivo que
permita comparar distintas formas de clasificar los centros logísticos y determinar cuáles
deberían considerarse estratégicos para el funcionamiento de la empresa.

3.5.2  Objetivo

El objetivo de este reto consiste en ayudar a la Dirección General de LOGISPAÑA a identificar
los centros logísticos más importantes de la red.

Para ello deberéis desarrollar un procedimiento que permita responder, al menos, a las siguientes
cuestiones:
a) ¿Qué centros logísticos gestionan un mayor volumen de mercancías? (Criterio 1)
b) ¿Qué centros poseen un mayor número de conexiones con el resto de la red? (Criterio 2)
c) ¿Cuál es la distribución estable del tráfico dentro de la red? (Criterio 3)
d) ¿Con qué frecuencia un centro aparece en caminos mínimos entre otros nodos? (Criterio
4) Esto se mide mediante la centralidad de intermediación (ver ayuda de la función
centrality de Matlb)
e) ¿Coinciden todos criterios de clasificación?
f) Si las clasificaciones obtenidas son diferentes, ¿a qué creéis que puede deberse?
g) ¿Puede un centro con menor volumen de mercancías desempeñar un papel más
importante para el funcionamiento global de la red?

Utilizando el modelo desarrollado en el reto anterior, elaborad un nuevo criterio de clasificación
basado en el comportamiento dinámico de la red y comparad los resultados obtenidos con los
anteriores.

Investigad si MATLAB dispone de herramientas específicas para calcular medidas de
importancia de los nodos de una red y comparad sus resultados con los obtenidos mediante
vuestro propio procedimiento.

Finalmente, justificad qué criterio recomendaríais utilizar a la Dirección General para priorizar
futuras inversiones en la red logística.

3.5.3  Producto esperado

Al finalizar este reto, el equipo deberá presentar:
a)  una descripción de los distintos criterios de clasificación analizados;
b)  el ranking completo de los centros logísticos obtenido mediante cada uno de ellos;
c)  una comparación crítica entre los diferentes resultados;
d)  una justificación del criterio que consideran más adecuado para la empresa;
```

#### Página 12

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

e) una breve reflexión sobre las ventajas e inconvenientes de cada método de clasificación.
f) Una recomendación sobre qué centros serán objetivo de inversión o modernización

3.5.4  Formato de resultados numéricos:

Los resultados deben darse en el siguiente formato:
a) Una sola tabla donde se muestren los centros con la valoración según cada criterio de
clasificación
b) Gráfica de barras con las valoraciones de cada centro en tanto por uno (valor máximo 1)
El resto de las cuestiones se responderán mediante el editor de texto y ecuaciones

3.5.5  Recursos recomendados:

[2] P.236, P336
[3] P.706
Use PageRank Algorithm to Rank Websites. MathWorks

3.5.6  Funciones Matlab:

sum, indegree, outdegree, centrality, sort, table, disp

3.6  Reto 6. Análisis de escenarios y apoyo a la toma de decisiones

3.6.1  Contexto

Durante las fases anteriores se ha desarrollado un modelo matemático capaz de representar el
funcionamiento de la red logística de LOGISPAÑA y de analizar la importancia relativa de los
distintos centros de distribución.

La Dirección General considera que el modelo desarrollado constituye una herramienta muy útil
para comprender el comportamiento de la red en condiciones normales de funcionamiento. No
obstante, desea comprobar también su utilidad para apoyar la toma de decisiones ante
situaciones excepcionales.

Mientras el proyecto se encuentra en su fase final de desarrollo, se produce un acontecimiento
inesperado.

3.6.1.1  Incidencia extraordinaria

Durante la última semana, una Depresión Aislada en Niveles Altos (DANA) ha provocado
lluvias torrenciales e importantes inundaciones en la Comunidad Valenciana.

Como consecuencia del temporal, el centro logístico de Valencia ha quedado completamente
inoperativo durante un periodo inicialmente estimado de varias semanas.

Además, varias de las rutas de transporte con origen o destino en Valencia han quedado
interrumpidas, impidiendo la circulación habitual de mercancías.

La Dirección General solicita con carácter urgente un informe técnico que permita evaluar el
impacto de esta incidencia sobre el funcionamiento global de la red logística y facilite la adopción
de medidas provisionales mientras se restablece la normalidad.

3.6.2  Objetivo
```

#### Página 13

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

Utilizando el modelo matemático desarrollado durante las fases anteriores, deberéis analizar las
consecuencias que tiene la pérdida temporal del centro logístico de Valencia sobre el
comportamiento global de la red.

Para ello será necesario modificar adecuadamente el modelo y estudiar cómo cambian los
resultados obtenidos anteriormente.

El análisis deberá permitir responder, al menos, a las siguientes cuestiones.
a) Modificar el modelo de la red teniendo en cuenta que el centro logístico de Valencia deja
de estar operativo. Justificad las modificaciones realizadas.
b) Representar gráficamente la nueva red logística e identificar las conexiones que han
desaparecido como consecuencia de la incidencia.
c) Calcular nuevamente el comportamiento a largo plazo de la red utilizando el algoritmo
Page Rank de la función centrality de Matlab. Obtener una nueva clasificación de
importancia de los centros logísticos.
d) Analizad qué localidades aumentan o disminuyen su importancia relativa y justificad las
posibles causas.
e) Identificar los centros logísticos que previsiblemente absorberán una mayor parte del
tráfico que anteriormente gestionaba Valencia. Justificad vuestra respuesta apoyándoos
en los resultados obtenidos.
f) Desde un punto de vista técnico, ¿consideráis que la red continúa siendo suficientemente
robusta para garantizar el servicio? Argumentad vuestra respuesta.
g) La Dirección General dispone de un presupuesto extraordinario que únicamente permite
reforzar dos centros logísticos durante la duración de la emergencia. Indicad cuáles
seleccionaríais y justificad vuestra decisión utilizando los resultados del análisis
realizado.

3.6.3  Producto esperado

El equipo deberá elaborar un Informe Técnico de Emergencia dirigido a la Dirección General de
LOGISPAÑA.

El informe deberá contener, al menos:
1.  una breve descripción de la incidencia;
2.  la metodología utilizada para realizar el análisis;
3.  los principales resultados obtenidos;
4.  una interpretación de dichos resultados desde el punto de vista logístico;
5.  las recomendaciones que el equipo considera oportunas para minimizar el impacto de la
incidencia.

3.6.4  Formato de resultados numéricos:

Los resultados de las preguntas del apartado anterior se mostrarán en los siguientes formatos:
a) Dar el resultado mediante una tabla indicando los centros origen/destino y flujo entre
ellos
b) Grafo
c) Tabla de clasificación ordenada por importancia de los centros operativos cuyas
columnas sean el valor del vector rank de mayor a menor en %
d) Tabla comparativa de posición en el ranking antes y después de la DANA calculando la
diferencia de posición para identificar los movimientos de posición

Responder a las preguntas e) f) y g) empleando los resultados anteriores

A la vista de los resultados obtenidos, elabore una recomendación dirigida al Director General
indicando las actuaciones que considera prioritarias durante las primeras 72 horas tras la
incidencia. Todas las recomendaciones deberán estar justificadas mediante el análisis matemático
realizado.
```

#### Página 14

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

3.6.5  Fuentes

3.6.6 Funciones Matlab
find, setdiff, digraph, adjacency, sum, sort, ismember, disp

3.7  Fuentes:
1. Algebra Lineal. Stanley Grossman, José Flores. McGraw Hill 7ªEd.
2. Álgebra Lineal. Una introducción moderna. David Poole. 3ª Ed.
3. Elementary Linear Algebra. Applications Version. (en inglés) Howard Anton Chris Rorres.11ª
Ed. Wiley
4. Algebra Lineal. Bernard Kolman, David R. Hill. 8ª Ed. Pearson
5. Anexo. Residuo
6. Anexo: Ajuste por mínimos cuadrados.
7. Anexo: Interpolación y ajuste de curvas. Pags 15-22

3.8  Calendario, informe final y rúbricas de evaluación
3.8.1  Calendario de entregas

Semana  Entregas
1  21-sept 25-sept Cursos: Matlab Onramp, Make and manipulate Matrices, Cálculos
2  28-sept 2-oct con vectores y matrices, Introduction to Linear Algebra with Matlab
3  5-oct  9-oct  Lectura del proyecto y organización del grupo
4  12-oct  16-oct Entrega informe Reto 1
5  19-oct  23-oct Entrega informe Reto 2
6  26-oct  30-oct Entrega informe Reto 3
7  2-nov  6-nov Entrega informe Reto 4
8  9-nov  13-nov Entrega informe Reto 5
9  16-nov 20-nov Entrega informe Reto 6
10 23-nov 27-nov Entrega informe final
11 30-nov  4-dic  Presentación y defensa del Informe Final
12  7-dic  11-dic

3.8.2  Estructura de las entregas parciales y el informe Final

El informe final se entregará en formato Live Script de Matlab y se compondrá de las siguientes
secciones:
Encabezado con los siguientes datos
  Información del proyecto:
  Título del proyecto
  número de grupo
  nombres de los miembros
  fecha

1. Descripción del problema
2. Reto 1. Estimación de la demanda logística futura
3. Reto 2. Representación matemática de la red logística
4. Reto 3. Almacenamiento y representación computacional de la red
```

#### Página 15

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

5. Reto 4. Análisis del comportamiento dinámico de la red
6. Reto 5. Análisis de la importancia estructural de la red logística
7. Reto 6. Análisis de escenarios y apoyo a la toma de decisiones
8. Conclusiones
9. Reflexión final
10. Referencias

El Live Script constituye un informe técnico ejecutable. Por tanto, el código deberá utilizarse
exclusivamente como soporte del razonamiento desarrollado y no como elemento principal del
documento. Cada bloque de código deberá ir precedido de una explicación de su finalidad y
seguido de una interpretación de los resultados obtenidos.

Se entrega un archivo P01_Plantilla.mlx sobre el que debéis escribir el informe
renombrándolo como P01_GrupoX.mlx. En cada apartado se dan las recomendaciones
pertinentes

Todas las gráficas deben incluir: título, etiquetas de ejes (con unidades si procede) y leyenda

3.9  Rúbricas de evaluación

RÚBRICA DEL PROYECTO
Evidencia
Reto 1. Estimación de la demanda logística futura  5%
Reto 2. Representación matemática de la red logística  5%
Reto 3. Almacenamiento y representación computacional de la red  5%
Reto 4. Análisis del comportamiento dinámico de la red  5%
Reto 5. Análisis de la importancia estructural de la red logística  5%
Reto 6. Análisis de escenarios y apoyo a la toma de decisiones  5%
Informe final  20%
Presentación y defensa  50%
TOTAL  100%

RÚBRICA DE LOS INFORMES PARCIALES
Criterio  Peso
Comprensión del problema  20%
Investigación realizada  20%
Calidad del modelo matemático  30%
Implementación MATLAB  20%
Claridad de la documentación  10%

RÚBRICA DEL INFORME FINAL
Criterio  Peso
Organización  20%
Claridad  20%
Calidad de las figuras  15%
Interpretación global  25%
Conclusiones  20%
```

#### Página 16

```text
PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de
decisiones estratégicas sobre su diseño, funcionamiento y optimización.
__________________________________________________________________________________________________________

RÚBRICA DE LA PRESENTACIÓN FINAL GRUPAL (30%)
Criterio  Peso
Organización y estructura de la presentación  20%
Claridad en la exposición del problema y objetivos  15%
Rigor en la explicación de la metodología seguida  20%
Calidad de la presentación (gráficos, tablas, demostraciones MATLAB, etc.)  15%
Interpretación de los resultados obtenidos  20%
Calidad de las conclusiones y recomendaciones finales  10%

En la presentación todos los miembros del grupo deberán intervenir en igual proporción.
Se valorará especialmente:
la capacidad para explicar el proyecto como una historia coherente;
el reparto equilibrado del tiempo entre los miembros del grupo;
la claridad de las figuras y gráficos;
que no se limite a leer diapositivas.

Tras la presentación, el profesorado realizará preguntas individualizadas a cada miembro del
equipo.
Las preguntas podrán referirse a cualquier parte del proyecto, independientemente de la parte
desarrollada por cada estudiante.

RÚBRICA DE LA PRESENTACIÓN FINAL INDIVIDUAL (70%)
Criterio  Peso
Comprensión del proyecto y de los fundamentos matemáticos  40%
Dominio de la implementación en MATLAB  30%
Capacidad de análisis, razonamiento y comunicación  30%

Durante las preguntas individuales se valorará que el estudiante sea capaz de:
a)  explicar con sus propias palabras los conceptos utilizados;
b)  justificar por qué se ha elegido un determinado modelo matemático;
c)  interpretar correctamente los resultados obtenidos;
d)  responder a pequeñas modificaciones del problema planteado;
e)  relacionar las distintas fases del proyecto.
f)  interpretar cualquiera de las funciones de Matlab incluidas en el informe

3.10  Uso de herramientas de Inteligencia Artificial

El empleo de herramientas de Inteligencia Artificial (como ChatGPT, MATLAB Copilot u otras
similares) está permitido como apoyo a la investigación, la búsqueda de información y el
desarrollo del proyecto. No obstante, el informe presentado deberá reflejar el trabajo intelectual
del equipo y todas las decisiones técnicas, modelos matemáticos, resultados y fragmentos de
código deberán ser plenamente comprendidos y poder ser justificados por cualquiera de sus
integrantes.

Durante la presentación y la defensa individual, el profesorado podrá solicitar la explicación
detallada de cualquier parte del informe o del código desarrollado. La incapacidad para justificar
adecuadamente el trabajo realizado evidenciará la no adquisición de las competencias evaluadas
y se reflejará en la calificación individual del estudiante, con independencia de la calidad del
documento entregado por el grupo.
```


## Datos del proyecto

*Fuente: `PROYECTO/P01 Datos.xlsx`*

#### Hoja: centros de distribución

| Código | Localidad | Tipo |
|---|---|---|
| M | Madrid | hub nacional |
| B | Barcelona | hub nacional |
| V | Valencia | hub nacional |
| Z | Zaragoza | hub regional |
| S | Sevilla | hub regional |
| BI | Bilbao | hub regional |
| MA | Málaga | distribución |
| MU | Murcia | distribución |
| VA | Valladolid | distribución |
| CO | Córdoba | distribución |
| AL | Alicante | distribución |
| GI | Gerona | distribución |

#### Hoja: flujos semanales

| Origen | Destino | Flujo |
|---|---|---|
| Madrid | Zaragoza | 850 |
| Madrid | Valencia | 780 |
| Madrid | Sevilla | 620 |
| Madrid | Valladolid | 430 |
| Zaragoza | Barcelona | 760 |
| Zaragoza | Bilbao | 410 |
| Zaragoza | Valencia | 390 |
| Barcelona | Gerona | 520 |
| Barcelona | Valencia | 610 |
| Barcelona | Zaragoza | 300 |
| Valencia | Murcia | 570 |
| Valencia | Alicante | 640 |
| Valencia | Madrid | 350 |
| Sevilla | Córdoba | 480 |
| Sevilla | Málaga | 530 |
| Córdoba | Madrid | 260 |
| Málaga | Sevilla | 240 |
| Bilbao | Valladolid | 310 |
| Valladolid | Madrid | 290 |
| Murcia | Valencia | 220 |
| Alicante | Valencia | 260 |
| Gerona | Barcelona | 180 |

#### Hoja: volumen de mercancías

| Año | Volumen de mercancías (miles de toneladas) |
|---|---|
| 2016 | 15.2 |
| 2017 | 16.1 |
| 2018 | 17 |
| 2019 | 18.4 |
| 2020 | 18 |
| 2021 | 19.6 |
| 2022 | 20.8 |
| 2023 | 22.1 |
| 2024 | 23.4 |
| 2025 | 24.8 |


## Plantilla MATLAB

*Fuente: `PROYECTO/P01_Plantilla.mlx`*

### PROYECTO 01: Análisis de una red logística de gran tamaño para proporcionar información objetiva que apoye la toma de decisiones estratégicas sobre su diseño, funcionamiento y optimización.

Grupo: [NÚMERO DE GRUPO]

Miembros: [NOMBRES Y APELLIDOS DE TODOS LOS MIEMBROS]

Fecha: [FECHA DE ENTREGA]

#### Uso de la plantilla

Guía de cumplimentación: sustituid los marcadores entre corchetes por vuestro trabajo. Mantened el orden de las secciones. Los bloques de código contienen únicamente comentarios y deben completarse por el equipo. Los textos identificados como extractos del PDF son indicaciones del enunciado; las guías y los marcadores son espacios para redactar el informe.

Se entrega un archivo P01_Plantilla.mlx sobre el que debéis escribir el informe renombrándolo como P01_GrupoX.mlx. En cada apartado se dan las recomendaciones pertinentes

Se debe seguir las indicaciones del archivo Formato_archivo_Proyectos.mlx

Todas las gráficas deben incluir: título, etiquetas de ejes (con unidades si procede) y leyenda

Los datos deberán importarse directamente desde MATLAB. No se permite copiarlos manualmente en el Live Script mediante la definición explícita de vectores o matrices.

El Live Script constituye un informe técnico ejecutable. Por tanto, el código deberá utilizarse exclusivamente como soporte del razonamiento desarrollado y no como elemento principal del documento. Cada bloque de código deberá ir precedido de una explicación de su finalidad y seguido de una interpretación de los resultados obtenidos.

#### 1. Descripción del problema

[ESCRIBID AQUÍ la descripción del problema, su contexto, la información disponible, el objetivo del proyecto y las restricciones, atendiendo al apartado 2 del enunciado del proyecto.]

#### 2. Reto 1. Estimación de la demanda logística futura

Objetivo — extracto del apartado 3.1.2 del enunciado del proyecto

Desarrollar un modelo matemático que describa la evolución temporal del volumen de mercancías gestionado por LOGISPAÑA y que permita realizar una estimación razonada de la demanda futura.

Para ello será necesario:

a) representar gráficamente los datos históricos proporcionados

b) investigar qué tipo de modelo matemático resulta adecuado para describir la tendencia observada;

c) comparar distintas alternativas y justificar la elección del modelo finalmente adoptado;

d) utilizar dicho modelo para estimar el volumen de mercancías esperado en el año 2028;

e) valorar la fiabilidad de la predicción obtenida y discutir las limitaciones del modelo utilizado.

Las conclusiones obtenidas deberán servir para justificar la necesidad del estudio de la red logística desarrollado en el resto del proyecto.

Producto esperado — extracto del apartado 3.1.3 del enunciado del proyecto

Al finalizar este reto, el equipo deberá presentar:

a) una representación gráfica de los datos históricos y las funciones polinómicas consideradas (en una sola gráfica) 1

b) una comparación entre los distintos modelos considerados empleando el RMSE de cada uno de ellos (ver función rmse)

c) el modelo matemático seleccionado (su ecuación) y la justificación de su elección;

d) la estimación del volumen de mercancías para el año 2028 y el incremento porcentual previsto para 2028

e) una valoración crítica sobre la calidad del ajuste obtenido y la fiabilidad de las predicciones realizadas.

f) una breve conclusión en la que se explique cómo las previsiones obtenidas justifican el análisis de la red logística que se desarrollará en los siguientes retos del proyecto.

1 Se aconseja desplazar el origen del eje de abscisas de modo que el primer año corresponda a 0

Formato de resultados numéricos: — extracto del apartado 3.1.4 del enunciado del proyecto

a) Gráfica hasta 2028

b) Tabla en la que las filas representan cada modelo y la columna su error de ajuste

c) Ecuación con fprintf cada coeficiente con 8 decimales

d) Se deben dar los resultados en forma de tabla cuyas columnas sean el grado del polinomio, su RMSE, su predicción para 2028 y el % de incremento respecto a 2025

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

Datos históricos y funciones polinómicas: una sola gráfica hasta 2028

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 1 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Comparación de modelos: tabla del error de ajuste

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 1 - Bloque 2
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Modelo seleccionado: ecuación y justificación

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 1 - Bloque 3
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Predicción para 2028 e incremento respecto a 2025

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 1 - Bloque 4
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Valorad la calidad del ajuste, la fiabilidad de las predicciones y las limitaciones del modelo.]

Conclusiones del reto

[ESCRIBID AQUÍ cómo las previsiones justifican el análisis de la red logística de los siguientes retos.]

#### 3. Reto 2. Representación matemática de la red logística

Objetivo — extracto del apartado 3.2.2 del enunciado del proyecto

El segundo objetivo del proyecto consiste en encontrar una forma de representar matemáticamente la red de distribución de manera que:

a) permita visualizar las relaciones existentes entre las distintas localidades;

b) facilite el almacenamiento de la información en un ordenador;

c) pueda ampliarse fácilmente cuando la red aumente de tamaño;

d) constituya la base para los análisis posteriores.

Como equipo de consultoría, debéis investigar qué herramientas matemáticas permiten modelar este tipo de problemas y justificar cuál de ellas resulta más adecuada para el caso planteado.

Una vez seleccionada la representación matemática, deberéis construir el modelo correspondiente para la red suministrada por la empresa.

Producto esperado — extracto del apartado 3.2.3 del enunciado del proyecto

Al finalizar este reto, el equipo deberá haber obtenido una representación matemática completa de la red logística y justificar las razones por las que considera que dicha representación resulta adecuada para el problema planteado.

Investiga y responde:

a) ¿Qué estructura matemática permite representar este tipo de problemas?

b) ¿Qué representan sus elementos?

c) ¿Qué ventajas ofrece frente a una simple tabla?

d) Busca dos aplicaciones distintas de esta estructura.

Formato de resultados numéricos: — extracto del apartado 3.2.4 del enunciado del proyecto

Se debe dar una representación gráfica de la red

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

Representación gráfica de la red

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 2 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Responded a las preguntas a), b), c) y d) del apartado 3.2.3.]

Conclusiones del reto

[ESCRIBID AQUÍ las conclusiones justificadas a partir del análisis realizado.]

#### 4. Reto 3. Almacenamiento y representación computacional de la red

Objetivo — extracto del apartado 3.3.2 del enunciado del proyecto

El objetivo de esta fase consiste en diseñar una estructura matemática que permita representar de forma completa la red logística en un ordenador.

La representación elegida deberá:

a) almacenar todas las conexiones existentes entre las distintas localidades;

b) incorporar el volumen de mercancías transportado entre ellas;

c) ser fácilmente ampliable cuando aumente el número de centros logísticos;

d) permitir el desarrollo de algoritmos de análisis de forma eficiente;

e) servir como base para las fases posteriores del proyecto.

Una vez seleccionada la representación más adecuada, deberéis construirla para la red logística proporcionada por la empresa utilizando MATLAB.

Producto esperado — extracto del apartado 3.3.3 del enunciado del proyecto

Al finalizar esta fase, el equipo deberá haber obtenido una representación matemática completa de la red logística y justificar por qué constituye una solución adecuada para el almacenamiento y tratamiento computacional de la información.

Formato de resultados numéricos: — extracto del apartado 3.3.4 del enunciado del proyecto

El resultado debe presentarse en dos tablas:

a) En la primera tabla se muestran los flujos entre centros mostrando los nombres de filas y columnas de modo que pueda verificarse el resultado con los datos proporcionados

b) En la segunda tabla las columnas deben mostrar el flujo entrante y saliente de cada centro

Asimismo, deberá explicarse el significado de cada elemento de la matriz construida y cómo puede recuperarse a partir de ella la información original de la red. Debe verificarse que los datos son correctos mediante los flujos entrantes/salientes así como el número total de rutas

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

Tabla de flujos entre centros con nombres de filas y columnas

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 3 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Tabla del flujo entrante y saliente de cada centro

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 3 - Bloque 2
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Explicad el significado de cada elemento de la matriz y cómo recuperar la información original de la red.]

Conclusiones del reto

[ESCRIBID AQUÍ las conclusiones justificadas a partir del análisis realizado.]

#### 5. Reto 4. Análisis del comportamiento dinámico de la red

Objetivo — extracto del apartado 3.4.2 del enunciado del proyecto

El objetivo de esta fase consiste en desarrollar un modelo matemático que permita analizar la evolución de la actividad logística dentro de la red cuando las mercancías circulan continuamente entre los distintos centros de distribución.

La metodología propuesta deberá permitir:

a) describir matemáticamente la evolución del sistema;

b) estudiar su comportamiento tras un gran número de etapas;

c) determinar si existe una situación de equilibrio o estabilidad;

d) analizar el significado logístico de dicho equilibrio;

e) automatizar completamente el proceso mediante MATLAB.

Producto esperado — extracto del apartado 3.4.3 del enunciado del proyecto

Al finalizar esta fase, el equipo deberá haber desarrollado un procedimiento que permita estudiar el comportamiento dinámico de la red logística y obtener la distribución de actividad cuando el sistema alcanza un régimen estable.

El informe deberá explicar:

a) el modelo matemático adoptado;

b) las hipótesis realizadas;

c) la interpretación física o logística de los resultados obtenidos;

d) las limitaciones del modelo.

Formato de resultados numéricos: — extracto del apartado 3.4.4 del enunciado del proyecto

La situación de equilibrio debe calcularse mediante tres métodos matemáticos. Se debe calcular la situación de equilibrio mediante los tres métodos con un error menor que 10−12. El resultado debe darse mediante una tabla ordenada de mayor a menor indicando los nombres de los centros (filas) y el % de flujo de mercancías

Finalmente se debe calcular la bondad de cada método mediante la norma del residuo correspondiente y dar los resultados mediante una tabla

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

Situación de equilibrio mediante tres métodos matemáticos

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 4 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Tabla de la norma del residuo de cada método

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 4 - Bloque 2
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Explicad las hipótesis, la interpretación física o logística y las limitaciones del modelo. Responded a las cuestiones del contexto.]

Conclusiones del reto

[ESCRIBID AQUÍ las conclusiones justificadas a partir del análisis realizado.]

#### 6. Reto 5. Análisis de la importancia estructural de la red logística

Objetivo — extracto del apartado 3.5.2 del enunciado del proyecto

El objetivo de este reto consiste en ayudar a la Dirección General de LOGISPAÑA a identificar los centros logísticos más importantes de la red.

Para ello deberéis desarrollar un procedimiento que permita responder, al menos, a las siguientes cuestiones:

a) ¿Qué centros logísticos gestionan un mayor volumen de mercancías? (Criterio 1)

b) ¿Qué centros poseen un mayor número de conexiones con el resto de la red? (Criterio 2)

c) ¿Cuál es la distribución estable del tráfico dentro de la red? (Criterio 3)

d) ¿Con qué frecuencia un centro aparece en caminos mínimos entre otros nodos? (Criterio 4) Esto se mide mediante la centralidad de intermediación (ver ayuda de la función centrality de Matlb)

e) ¿Coinciden todos criterios de clasificación?

f) Si las clasificaciones obtenidas son diferentes, ¿a qué creéis que puede deberse?

g) ¿Puede un centro con menor volumen de mercancías desempeñar un papel más importante para el funcionamiento global de la red?

Utilizando el modelo desarrollado en el reto anterior, elaborad un nuevo criterio de clasificación basado en el comportamiento dinámico de la red y comparad los resultados obtenidos con los anteriores.

Investigad si MATLAB dispone de herramientas específicas para calcular medidas de importancia de los nodos de una red y comparad sus resultados con los obtenidos mediante vuestro propio procedimiento.

Finalmente, justificad qué criterio recomendaríais utilizar a la Dirección General para priorizar futuras inversiones en la red logística.

Producto esperado — extracto del apartado 3.5.3 del enunciado del proyecto

Al finalizar este reto, el equipo deberá presentar:

a) una descripción de los distintos criterios de clasificación analizados;

b) el ranking completo de los centros logísticos obtenido mediante cada uno de ellos;

c) una comparación crítica entre los diferentes resultados;

d) una justificación del criterio que consideran más adecuado para la empresa;

e) una breve reflexión sobre las ventajas e inconvenientes de cada método de clasificación.

f) Una recomendación sobre qué centros serán objetivo de inversión o modernización

Formato de resultados numéricos: — extracto del apartado 3.5.4 del enunciado del proyecto

Los resultados deben darse en el siguiente formato:

a) Una sola tabla donde se muestren los centros con la valoración según cada criterio de clasificación

b) Gráfica de barras con las valoraciones de cada centro en tanto por uno (valor máximo 1) El resto de las cuestiones se responderán mediante el editor de texto y ecuaciones

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

Tabla única de valoraciones según cada criterio de clasificación

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 5 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Gráfica de barras con las valoraciones en tanto por uno (valor máximo 1)

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 5 - Bloque 2
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Incluid el ranking completo de cada criterio, la comparación crítica, las ventajas e inconvenientes y las respuestas a las cuestiones del objetivo. Utilizad el editor de texto y ecuaciones.]

Conclusiones del reto

[ESCRIBID AQUÍ el criterio recomendado y qué centros serán objetivo de inversión o modernización.]

#### 7. Reto 6. Análisis de escenarios y apoyo a la toma de decisiones

Informe Técnico de Emergencia dirigido a la Dirección General de LOGISPAÑA

Descripción de la incidencia

[ESCRIBID AQUÍ una breve descripción de la incidencia del apartado 3.6.1.1.]

Objetivo — extracto del apartado 3.6.2 del enunciado del proyecto

Utilizando el modelo matemático desarrollado durante las fases anteriores, deberéis analizar las consecuencias que tiene la pérdida temporal del centro logístico de Valencia sobre el comportamiento global de la red.

Para ello será necesario modificar adecuadamente el modelo y estudiar cómo cambian los resultados obtenidos anteriormente.

El análisis deberá permitir responder, al menos, a las siguientes cuestiones.

a) Modificar el modelo de la red teniendo en cuenta que el centro logístico de Valencia deja de estar operativo. Justificad las modificaciones realizadas.

b) Representar gráficamente la nueva red logística e identificar las conexiones que han desaparecido como consecuencia de la incidencia.

c) Calcular nuevamente el comportamiento a largo plazo de la red utilizando el algoritmo Page Rank de la función centrality de Matlab. Obtener una nueva clasificación de importancia de los centros logísticos.

d) Analizad qué localidades aumentan o disminuyen su importancia relativa y justificad las posibles causas.

e) Identificar los centros logísticos que previsiblemente absorberán una mayor parte del tráfico que anteriormente gestionaba Valencia. Justificad vuestra respuesta apoyándoos en los resultados obtenidos.

f) Desde un punto de vista técnico, ¿consideráis que la red continúa siendo suficientemente robusta para garantizar el servicio? Argumentad vuestra respuesta.

g) La Dirección General dispone de un presupuesto extraordinario que únicamente permite reforzar dos centros logísticos durante la duración de la emergencia. Indicad cuáles seleccionaríais y justificad vuestra decisión utilizando los resultados del análisis realizado.

Producto esperado — extracto del apartado 3.6.3 del enunciado del proyecto

El equipo deberá elaborar un Informe Técnico de Emergencia dirigido a la Dirección General de LOGISPAÑA.

El informe deberá contener, al menos: 1. una breve descripción de la incidencia; 2. la metodología utilizada para realizar el análisis; 3. los principales resultados obtenidos; 4. una interpretación de dichos resultados desde el punto de vista logístico; 5. las recomendaciones que el equipo considera oportunas para minimizar el impacto de la incidencia.

Formato de resultados numéricos: — extracto del apartado 3.6.4 del enunciado del proyecto

Los resultados de las preguntas del apartado anterior se mostrarán en los siguientes formatos:

a) Dar el resultado mediante una tabla indicando los centros origen/destino y flujo entre ellos

b) Grafo

c) Tabla de clasificación ordenada por importancia de los centros operativos cuyas columnas sean el valor del vector rank de mayor a menor en %

d) Tabla comparativa de posición en el ranking antes y después de la DANA calculando la diferencia de posición para identificar los movimientos de posición

Responder a las preguntas e) f) y g) empleando los resultados anteriores

A la vista de los resultados obtenidos, elabore una recomendación dirigida al Director General indicando las actuaciones que considera prioritarias durante las primeras 72 horas tras la incidencia. Todas las recomendaciones deberán estar justificadas mediante el análisis matemático realizado.

Explicación / metodología

[EXPLICAD AQUÍ el procedimiento elegido, la investigación realizada y las decisiones adoptadas para responder al objetivo y al producto esperado de este reto. Incluid las ecuaciones y las referencias que correspondan.]

a) Tabla de centros origen/destino y flujo entre ellos

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 6 - Bloque 1
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

b) Grafo de la nueva red logística

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 6 - Bloque 2
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

c) Clasificación de los centros operativos: vector rank en %

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 6 - Bloque 3
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

d) Tabla comparativa del ranking antes y después de la DANA

[EXPLICAD AQUÍ la finalidad del siguiente bloque de código y su relación con el procedimiento descrito.]

```matlab
% Reto 6 - Bloque 4
% Escribid aquí vuestro código MATLAB.
% Generad los resultados con el formato indicado en el enunciado.
```

Resultados

[MOSTRAD AQUÍ los resultados generados por el bloque anterior con el formato indicado. No introduzcáis resultados de ejemplo.]

Interpretación de los resultados

[INTERPRETAD AQUÍ los resultados anteriores y relacionadlos con las cuestiones del reto.]

Interpretación y respuesta a las cuestiones del reto

[ESCRIBID AQUÍ. Responded a e), f) y g) empleando los resultados anteriores: tráfico, robustez y selección justificada de dos centros.]

Conclusiones del reto

[ESCRIBID AQUÍ la recomendación dirigida al Director General sobre las actuaciones prioritarias durante las primeras 72 horas, justificada mediante el análisis matemático realizado.]

#### 8. Conclusiones

[REDACTAD AQUÍ las conclusiones globales del proyecto y las recomendaciones para LOGISPAÑA, apoyándoos en los resultados de los seis retos.]

#### 9. Reflexión final

[ESCRIBID AQUÍ la reflexión final del equipo sobre el trabajo realizado y el aprendizaje adquirido.]

#### 10. Referencias

[INCLUID AQUÍ las fuentes realmente consultadas y citadas en el informe, de forma uniforme y con información suficiente para identificarlas.]
