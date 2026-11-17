Valoración de Riesgo Neutral
“Cualquier instrumento derivado dependiente del precio de un activo puede ser valorado
suponiendo que el activo se encuentra en un mundo de riesgo neutral”.
Para propósitos de valoración de una opción, se puede suponer que:
1. El retorno esperado de todos los instrumentos negociados es la tasa de interés
libre de riesgo.
2. Los flujos de caja futuros pueden ser valorados descontando sus valores
esperados a la tasa de interés libre de riesgo.
De este modo, cuando se quiere hacer el paso del “mundo real” al mundo de riesgo
neutral, el retorno esperado del activo experimenta un cambio importante, mientras
que su volatilidad sigue siendo la misma. El paso de un mundo en que existe un
conjunto de preferencias al riesgo, a uno con otro conjunto diferente se conoce como
“Cambio de Medida”.
Como el valor esperado del pago descontado de un instrumento derivado bajo la
probabilidad subjetiva P daría lugar a oportunidades de arbitraje, es necesario
construir una única medida de probabilidad P*equivalente a P tal que:
1. El precio descontado a la tasa de interés libre de riesgo r, sea una Martingala.
2. El valor esperado del pago descontado de un instrumento derivado bajo la
probabilidad P* no presente oportunidades de arbitraje.
La medida de probabilidad que se considera en un mundo de riesgo neutral se conoce
como “Medida equivalente de Martingala”.
Incidencia de la valoración de riesgo neutral sobre la Ecuación Diferencial
Estocástica Lineal Homogénea.
Considere la Ecuación Diferencial Estocástica dada por dS S dtS dB donde
t t t t
, 0 y  B  es un M.B.E.U.
t t0
El precio descontado a la tasa de interés libre de riesgo r, es S* ertS y su
t t
diferencial estocástico está dado por
 
d ertS rertS dtertdS .
t t t
rS
ertdtert
S dtS dB

t t t t
  r  S ertdtertS dB
t t t
dS*   r  S*dtS*dB
t t t t
(1)

Puede observarse que el precio descontado  S*  satisface la misma ecuación que  S ,
|                                              |     |     |     |     |     |     | t   |     |     |     | t   |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                              |     |     |     |     |     |     |   |     |     |     |     |
| donde el retorno   ha sido remplazado por   |     |     |     |     |     |     | r | .   |     |     |     |
De este modo, el valor esperado bajo la probabilidad subjetiva  P del pago descontado
de un instrumento derivado, presentará oportunidades de arbitraje puesto que  S*   no es
t
S* constituya
una Martingala. Para encontrar una medida de probabilidad bajo la cual
t
una Martingala, la ecuación (1) se debe escribir en tal forma que el termino de tendencia
sea “absorbido” dentro del término de la Martingala.

Por el Teorema de Girsanov puede establecerse que si   r   y 1/ son acotadas
|                  |     | r | . Es claro que (t)£2 |     |     |     |     |    |         |     |     |
| ---------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- |
| entonces  (t) |     |     |                            |     |     |     |     | 0,T | ;  .  |     |     |

Por el Teorema de Cameron-Martin-Girsanov,
Defina:
|     |          | 1 t   |     | t          |     |     | 1      |     |     |     |     |
| --- | -------- | ----- | --- | ---------- | --- | --- | ------ | --- | --- | --- | --- |
| 1)  |          | (u) | 2   | du(u)dB |     |     | 2tB |     |     |     |     |
|     | h(t,) |       |     |            |     |   |        |     |     |     |     |
|     |          | 2     |     |            |     | u   | 2      | t   |     |     |     |
|     |          | 0     |     | 0          |     |     |        |     |     |     |     |
| 2)  | B*  B   | t   |     |            |     |     |        |     |     |     |     |
t t
3)  dP*()dP();    eh(t,).
|     |     | t   |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |    |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
e2, se obtiene la relación Ee(u)2
| Para el caso especial en el que  |     |     |     |     |     |  y C |     |     |     |     | C.  |
| ---------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---- |
2

| De este modo puede afirmarse que P* |     |     |     |     |     |             |     |   |                               |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | --- | ----------------------------- | --- | --- |
|                                      |     |     |     |     |     |  1 y asi,  |     | B*  |  es un M.B.E.U en el espacio  |     |     |
t t0
|     |     |     |     |     |     |     |   |    |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Ω,ℱ,{ℱ } , P*) y en consecuencia,  dS*  r  S*dtS*dB .
|     | 𝑡   |     |     |     |     | t   |     |     | t   | t t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡≥0
t
S*S*dB*. Observe que S* es una
| De este modo se obtiene dS* |     |     |     | S*dB* |     | S* |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|                             |     |     |     | t       | t   | t   | t 0 |     | u u |     | t   |
0
Martingala respecto de ℱ para 0t.
𝜏
| Ahora, dS | S | dtS | dB  | dS | S | dtS |     | (dB*dt)  |     |     |     |
| --------- | --- | ----- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- |
|           | t   | t     | t   | t   | t   | t     | t   | t          |     |     |     |
Finalmente,  dS     S dtS dB* dS rS dtS dB*  que  es  el
|     |     | t   |     | t   |     | t t | t   | t   |     | t t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comportamiento del activo subyacente en un mundo de Riesgo Neutral.