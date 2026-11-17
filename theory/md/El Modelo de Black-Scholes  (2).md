EL MODELO DE BLACK-SCHOLES
Propiedad de log-normalidad para precios activos
Definición: se dice que una variable sigue una distribución normal si el logaritmo natural
de la variable, es normalmente distribuida.
Considere la ecuación diferencial estocástica dada por
(1) dS SdtSdB
t t t t
donde ,0 son constantes y {B } es un Movimiento Browniano Estándar
t t0
Unidimensional. Sea Y ln(S ). Aplicando la fórmula de Ito sobre Y se obtiene,
t t t
1 1 1 1
dY  dS   (dS )2 y de (1), dY dtdB  2dt.
t S t 2St2  t t t 2
t
 1 
dY d(ln(S )) 2dtdB , en forma integral
t t  2  t
 1 
ln(S )ln(S ) 2T B , en consecuencia,
T o  2  T
 1  
(2) ln(S T )ln(S o )~ N       2 2  T ,2T    es decir,
 S   1  
(3) ln

 t

~ N

 2T, 2T


 S   2  
O
de otro modo,
  1  
dS t S t dtS t dB t ln(S T )~ N    ln(S o )   2 2  T, 2T    .
De la ecuación (2) es claro que el cambio de ln(S ) entre los tiempos 0 y T sigue una
t
distribución normal. S denota el precio del activo en un tiempo futuro T, S es el precio
T o
del activo en el tiempo 0 y N(m,v) denota una distribución normal con media m y
varianza v. La ecuación (3) muestra que ln(S ) es normalmente distribuido de modo que
T
S sigue una distribución log-normal.
T
Distribución de la tasa de retorno
La propiedad de log-normalidad para precios activos puede ser usada para capturar
información sobre la distribución de probabilidad de la tasa de retorno anual continuamente
aplicada al activo entre los tiempos 0 y t.
1

|     |     |     |     |     | 1 S |    |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
eT
| Se tiene que S |     | S  | luego  |     | ln | T , en consecuencia,  |     |     |     |
| -------------- | --- | --- | -------- | --- | --- | ---------------------- | --- | --- | --- |
|                |     | T o |          |     |    |                       |     |     |     |
|                |     |     |          |     | T  | S                     |     |     |     |
o
|     | 1  | 1  |     |    |     |     |   | 1   |  2  |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | ------ |
~ N  2T, 2T ; de otro modo ~  2T,  es decir, la tasa de
|     |     |     |     |    |     |     |    |     |    |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | T  | 2  |     |     |     |     |   | 2   |  T |
|     |      |     |     |    |     |     |     |     |    |
retorno por año compuesta continuamente es normalmente distribuida con media
|    | 1  |     | 2 |    |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 y varianza 
|  |     |     |     |  .  |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     | 2   |     |    |     |     |     |     |     |     |
|    |    |     |  T |     |     |     |     |     |     |

Volatilidad

La volatilidad, , de un activo es una medida de incertidumbre acerca de los retornos
proporcionados del activo. Los valores típicos de la volatilidad de un activo están en un
rango del 20% al 40% por año. La volatilidad del precio de un activo puede ser definido
como la desviación estándar del retorno previsto por el activo en un año cuando el retorno
es expresado usando composición continua. La volatilidad también puede expresarse como
la desviación estándar del logaritmo natural del precio del activo al final de un año.
Cuando  t es pequeño,  t  es aproximadamente igual a la desviación estándar del
cambio proporcional en el precio del activo en el tiempo.

Estimación de la volatilidad usando los datos históricos

Para estimar la volatilidad del precio de un activo empíricamente, el precio del activo es
habitualmente observado en intervalos de tiempo fijos (diarios, semanales o mensuales).
Se define:

n1: Número de observaciones
S     : Precio del activo al finalizar el i-ésimo intervalo; (i0,1,2,3,.....,n).
i
t   : Longitud del intervalo de tiempo en años.
|         |      |  S       |     |                   |     |     |     |     |     |
| ------- | ---- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- |
| Tome  L | ln | i para (i |     |                   |     |     |     |     |     |
|         |      |          |     | 1,2,3,.....,n).  |     |     |     |     |     |
|         | i    | S          |     |                   |     |     |     |     |     |
|         |      |          |     |                   |     |     |     |     |     |
i1
Como S S eL , L  es el retorno compuesto continuamente (no anualizado) en el i-ésimo
i
|     | i   | i1 i |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
intervalo, esto es, el retorno logarítmico instantáneo.
La estimación usual para la desviación estándar S, de las L  está dada por
i
|         | 1                     | n        |     |     |     | n   |         |    | n  2 |
| ------- | --------------------- | -------- | --- | --- | --- | --- | ------- | --- | ----- |
|         |                       |          |     |     |     | 1   | 1       |     |       |
| S       |                      | (L L)2 |    | S   |    | L2 |        | L |      |
|         |                       | i        |     |     |     |     | i       |     | i     |
|         | n1                   |          |     |     | n1 |     | n(n1) |     |      |
|         |                       | i1      |     |     |     | i1 |         |     | i1   |
| donde L |  es la media de las L |          |     | ’s. |     |     |         |     |       |
i
La desviación estándar S, de las L ’s, es igual a  t.La variable S  es de este modo, un
i
. Se sigue que  en si misma puede ser estimada como *, donde
| estimador de  |     | t  |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
* S . Así, el error estándar de esta estimación es aproximadamente */
 2n.
t
  2

Algunos conceptos asociados a la ecuación diferencial de Black-Scholes-Merton.
La ecuación diferencial de Black-Scholes-Merton es una ecuación que debe satisfacer el
precio f de cualquier instrumento derivado sobre un activo que no paga dividendos.
El análisis de Black-Scholes-Merton está enmarcado en la valoración del riesgo neutral.
Valoración de riesgo neutral
En un mundo de riesgo neutral todos los individuos son indiferentes al riesgo. Ellos no
requieren ninguna compensación por el riego y el retorno esperado de todos los activos es
la tasa de interés libre de riesgo, de este modo el valor de la opción es el pago (pay off)
esperado en un mundo de riesgo neutral descontado a la tasa de interés libre de riesgo.
La valoración de riesgo neutral, es un principio en el cual se establece que para valorar
opciones, es válido suponer que todos los individuos que participan en el mercado se
encuentran en un mundo de riesgo neutral.
Portafolio libre de riesgo
un portafolio libre de riesgo está compuesto por una posición en la opción y una posición
en el activo subyacente. E n ausencia de oportunidades de arbitraje, el retorno del portafolio
deberá ser la tasa de interés libre de riesgo, r.
La razón por la cual puede ser creado este portafolio es que tanto el precio del activo como
el precio de la opción están afectados por el mismo nivel de incertidumbre: movimientos
del precio activo.
Supuestos del modelo de Black-Scholes
1) La dinámica de precios del activo está dada por un Movimiento Browniano Geométrico.
2) No existen costos de transacción.
3) Todos los activos son perfectamente divisibles.
4) No existen dividendos durante la vida de la opción.
5) No existen oportunidades de arbitraje.
6) El activo puede negociarse de manera continua.
7) La tasa de interés libre de riesgo, r, es constante y la misma para todas las maduraciones
(fechas de expiración).
3

Deducción de la Ecuación Diferencial de Black-Scholes-Merton
Suponga que el precio de un activo está dominado por la E.D.EL.H dada por
(4) dS SdtSdB
t t t t
donde ,0 son constantes y {B } es un Movimiento Browniano Estándar
t t0
Unidimensional.
Suponga además que el precio f de una opción call o cualquier otro instrumento derivado
sobre S es una función de S y t, es decir, f  f(t,S ). Al aplicar la formula de Ito sobre
t t t
f se obtiene:
f f 1 2f
df  dt dS  (dS )2
t S t 2 S2 t
t t
f f 1 2f  f
(5) df   S  2S 2dt SdB
 t S t 2 S2 t  S t t
 
t t t
La discretización de las ecuaciones (4) y (5) están dadas por
(6) S StSB
t t t t
f f 1 2f  f
f   S  2S 2t S B
(7)  t S t 2 S2 t  S t t
 
t t t
donde S y f son los cambios en f y S en un intervalo de tiempo pequeño t.
t t
Se construye un portafolio apropiado de tal modo que el tenedor de este portafolio tenga
df
una posición corta en un derivado y una posición larga en una cantidad de partes del
dS
t
activo.
De este modo, el valor del portafolio esta dado por
f
(8)  f  S .
S t
t
4

El cambio  en el valor del portafolio en un intervalo de tiempo pequeño t, toma la
forma

f
| (9)  |     |     |     |   | f |    | S  |     |     |     |
| ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|      |     |     |     |     |      | S  | t   |     |     |     |
t

sustituyendo (6) y (7) en (9) se obtiene,

|     | f |     |      | 2f   |          |     |      |     |              |     |
| --- | --- | --- | ---- | ----- | --------- | --- | ---- | --- | ------------ | --- |
|     |     | f  |      | 1     |           | f  |      |     | f           |     |
|   |  |    | S  |       | 2S 2t |     | SB |    | (StSB)  |     |
|     |    |     | t    |       | t        |     | t    | t   | t            | t t |
|     | t  | S  |      | 2 S2 |           | S  |      |     | S           |     |
|     |    | t   |      | t     |          |     | t    |     | t            |     |

|       |     |     |     |     |      | f 1 | 2f |     |       |     |
| ----- | --- | --- | --- | --- | ---- | ----- | --- | --- | ------ | --- |
| (10)  |     |     |     |   |   |      |     | 2S | 2t   |     |
|       |     |     |     |     |      |      |     |     |       |     |
|       |     |     |     |     |      | t 2  | S2 | t   |        |     |
|       |     |     |     |     |      |      |     |     |       |     |
t

Como ésta ecuación no contiene el término B , este portafolio deberá ser libre de riesgo
t
durante el tiempo t.

Así se sigue que,

| (11)   |     |     |     |     |     |  rt |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
,

donde r es la tasa de interés libre de riesgo. De las ecuaciones (8), (10) y (11) se sigue que

|     |     |    |      | 2f |     |     |      |     |                     |     |
| --- | --- | --- | ---- | --- | ---- | ---- | ---- | --- | -------------------- | --- |
|     |     |     | f 1 |     |      |      |      | f  |                      |     |
|     |     |   |     | 2S | 2t | r | f  |     | S t, finalmente,   |     |
|     |     |    |      |     |     |     |      |     | t                   |     |
|     |     |     | t 2 | S2 | t    |      |      | S  |                      |     |
|     |     |    |      | t   |     |     |      | t   |                     |     |

|       |     |     | f  |     | f   | 1 2f |       |     |     |     |
| ----- | --- | --- | --- | --- | ---- | ----- | ----- | --- | --- | --- |
| (12)  |     |     |     | rS |     | 2S   | 2 rf |     |     |     |
|       |     |     | t  |     | t S | 2 S2 | t     |     |     |     |
|       |     |     |     |     | t    | t     |       |     |     |     |

Esta ecuación diferencial tiene muchas soluciones dependiendo de las condiciones de
frontera:

1) Para una opción call europea la condición es  f max(S K,0)cuando t=T.
t

2) Para una  opción put europea la condición es  f max(K S ,0)cuando t=T.
t

Una característica importante de esta ecuación es que no involucra ninguna variable que sea
afectada por las preferencias de riesgo de los inversionistas, ya que solo aparecen el precio
presente del activo, el tiempo, la volatilidad y la tasa de interés libre de riesgo, r.

  5

Formulas de valoración de opciones de Black-Scholes

Las formulas de valoración de opciones para el precio en el tiempo cero de opciones call y
put del tipo europeo sobre un activo que no para dividendos, están dadas por

| f  S N(d | )KerTN(d | )   |
| --------- | ---------- | --- |
| call o    | 1          | 2   |

KerTN(d
| f   | )S N(d | )   |
| --- | -------- | --- |
| put | 2 o      | 1   |
Donde,
S  1
| ln | o (r  2)T |     |
| --- | ------------- | --- |
 K  2
| d  |     |     |
| --- | --- | --- |
| 1   |  T |     |

| d   | d  T   |     |
| --- | --------- | --- |
| 2   | 1 .       |     |

N(x)  es  la  función  de  distribución  de  probabilidad  acumulativa  para  una  variable
N ~ (0,1), S es el precio del activo en el tiempo cero, K es el precio del ejercicio,  la
0
volatilidad, T el tiempo de maduración y r la tasa de interés libre de riesgo.
  6