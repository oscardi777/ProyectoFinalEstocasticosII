Maestr´ıa en Finanzas
C´alculo Estoc´astico
Medida Equivalente de Martingala
Freddy H. Mar´ın
UniversidadEAFIT
Medell´ın-Colombia
Junio de 2016
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 1/7

Espacio de probabilidad
Definici´on
SeanP unamedidadeprobabilidady{B } unMBEU.Elespacio
t t≥0
de probabilidad en el cual est´a definido {B } y bajo el cual se
t t≥0
calcula E[·] se denotar´a por (Ω,=,P)
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 2/7

Medida equivalente de Martingala
Definici´on
Sea(Ω,=,{= } ,P)unespaciodeprobabilidadcompletoconuna
t t≥0
filtraci´on {= } . Si P∗ es una medida sobre (Ω,P) dada por
t t≥0
Z
P∗(A) = f(w)dP(w); A ∈ =
A
Entonces
dP∗(w) = f(w)dP(w); w ∈ A
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 3/7

| Teorema: | Cameron | - Martin  |          | - Girsanov |     |            |     |              |     |
| -------- | ------- | --------- | -------- | ---------- | --- | ---------- | --- | ------------ | --- |
|          | Sea {B  | } un MBEU | definido | sobre      |     | el espacio | de  | probabilidad |     |
|          |         | t t≥0     |          |            |     |            |     |              |     |
‘2([0,T],R).
|     | (Ω,=,{=     | } ,P) y       | suponga | que       | φ(t) ∈ |        |          | Defina: |     |
| --- | ----------- | ------------- | ------- | --------- | ------ | ------ | -------- | ------- | --- |
|     |             | t t≥0         |         |           |        |        |          |         |     |
|     |             | Rt|φ(u)|2du+  |         | Rtφ(u)dB  |        |        |          |         |     |
|     | i) h(t,φ)   | = −1          |         |           |        | ;      | 0 ≤      | t ≤ T   |     |
|     |             | 2 0           |         |           | 0      | u      |          |         |     |
|     | ii)         | Rtφ(u)du      |         |           |        |        |          |         |     |
|     | B∗          | = B −         |         |           |        |        |          |         |     |
|     | t           | t 0           |         |           |        |        |          |         |     |
|     |             | ξφdP(w);      |         | ξφ        |        |        |          |         |     |
|     | iii) dP∗(w) | =             |         | = eh(t,φ) |        | = f(w) |          |         |     |
|     |             | t             |         | t         |        |        |          |         |     |
|     | Si P∗(Ω)    | = 1, entonces |         | {B∗}      | es un  | MBEU   | definido | sobre   | el  |
t t≥0
,P∗)
|     | espacio | de probabilidad | (Ω,=,{= |     | }   | con | respecto | a la | mis- |
| --- | ------- | --------------- | ------- | --- | --- | --- | -------- | ---- | ---- |
t t≥0
ma filtraci´on {= t } t≥0 . Mas au´n, una condici´on suficiente para que
P∗(Ω) = 1 se cumpla es que existan dos constantes positivas µ y C
|     | tales que |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
E[eµ|φ(t)|2
|     |     |     |     | ] ≤ C; | 0 ≤ | t ≤ | T   |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 4/7

Teorema de Girsanov
| Sea {B         | }     | un MBEU  | definido                  | sobre      | el espacio | de probabilidad |       |
| -------------- | ----- | -------- | ------------------------- | ---------- | ---------- | --------------- | ----- |
|                | t t≥0 |          |                           |            |            |                 |       |
| (Ω,=,{=        | }     | ,P). Sea | S                         | un proceso | de Itˆo    | unidimensional  | sobre |
|                | t t≥0 |          | t                         |            |            |                 |       |
| [0,T] dado     | por   |          |                           |            |            |                 |       |
|                |       | Z t      |                           | Z t        |            |                 |       |
| S              | = S + | f(s)ds   | +                         | g(s)dB     | ; f,g      | ∈ ‘2([0,T],R)   |       |
| t              | 0     |          |                           |            | s          |                 |       |
|                |       | 0        |                           | 0          |            |                 |       |
| Supongaqueφ(t) |       | ∈        | ‘2([0,T],R)yconsidere{B∗} |            |            | yP∗definidos    |       |
|                |       |          |                           |            |            | t t≥0           |       |
como en el teorema anterior. Si P∗(Ω) = 1, entonces S es tambi´en
t
un proceso de Itˆo unidimensional sobre el espacio de probabilidad
|         |         | ,P∗) |              |     | {B∗} |               |        |
| ------- | ------- | ---- | ------------ | --- | ---- | ------------- | ------ |
| (Ω,=,{= | t } t≥0 |      | con respecto | al  | MBEU | t≥0 es decir, | S t es |
t
| soluci´on | de la | ecuaci´on |                   |     |          |     |     |
| --------- | ----- | --------- | ----------------- | --- | -------- | --- | --- |
|           |       | dS =      | [f(t)+g(t)φ(t)]dt |     | +g(t)dB∗ |     |     |
|           |       | t         |                   |     |          | t   |     |
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 5/7

Teorema de Girsanov
| Enformam´asgeneral,siS |     | essoluci´ondelaecuaci´ondS |     | = [f(t)+ |
| ---------------------- | --- | -------------------------- | --- | -------- |
|                        |     | t                          |     | t        |
g(t)φ(t)]dt+g(t)dB sobre el espacio de probabilidad (Ω,=,P), el
t
| teoremadeGirsanovestablecequeS |     |     | tambi´enessoluci´ondelaEDE |     |
| ------------------------------ | --- | --- | -------------------------- | --- |
t
[f(t)+g(t)φ(t)]dt+g(t)dB∗
| dS t = |     |     | sobreelespaciodeprobabilidad |     |
| ------ | --- | --- | ---------------------------- | --- |
t
(Ω,=,P∗).
g(x,t)−1
| Si ambas funciones | f(x,t) | y     | son acotadas, | entonces |
| ------------------ | ------ | ----- | ------------- | -------- |
|                    |        | f(x,S | )             |          |
t
|     |     | φ(t) = − |     |     |
| --- | --- | -------- | --- | --- |
|     |     | g(x,S    | )   |     |
t
| y en consecuencia | la ecuaci´on | se reduce | a   |     |
| ----------------- | ------------ | --------- | --- | --- |
)dB∗
|     |     | dS t = g(t,S | t   |     |
| --- | --- | ------------ | --- | --- |
t
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 6/7

Teorema de Girsanov
Proposici´on
El proceso
Z t
|     |     | S   | = S | + g(u,S | )dB∗ |     |     |
| --- | --- | --- | --- | ------- | ---- | --- | --- |
|     |     | t   | 0   |         | u u  |     |     |
0
| es una Martingala |     | respecto | de  | = ; 0 ≤ τ | ≤ t |     |     |
| ----------------- | --- | -------- | --- | --------- | --- | --- | --- |
τ
Demostraci´on
|     |     | (cid:20) | Z   | t   | (cid:21) |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- |
(cid:12)
| E∗[S | = | ] = | E∗ S | +   | g(u,S )dB∗(cid:12)= |             |     |     |
| -------- | --- | ---- | --- | ------------------- | ----------- | --- | --- |
| t        | τ   |      | 0   | u                   | u(cid:12) τ |     |     |
0
|     |     |     | (cid:20)Z | τ       | Z t         |               | (cid:12) (cid:21) |
| --- | --- | --- | --------- | ------- | ----------- | ------------- | ----------------- |
|     |     | +E∗ |           | )dB∗+   |             | )dB∗(cid:12)= |                   |
|     | =   | S   |           | g(u,S   | g(u,S       |               |                   |
|     |     | 0   |           | u       | u           | u             | u(cid:12) τ       |
|     |     |     | 0         |         | τ           |               |                   |
|     |     |     | Z τ       |         | (cid:20)Z t |               | (cid:21)          |
|     | =   | S + | g(u,S     | )dB∗+E∗ | g(u,S       | )dB∗          |                   |
|     |     | 0   |           | u u     |             | u             | u                 |
|     |     |     | 0         |         | τ           |               |                   |
= S τ
Maestr´ıaenFinanzasC´alculoEstoc´astico:MedidaEquivalentedeMartingala 7/7