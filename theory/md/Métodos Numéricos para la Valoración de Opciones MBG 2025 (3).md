Freddy H. Marín                                                                                                                    Universidad EAFIT

METODOS NUMÉRICOS PARA LA VALORACIÓN DE OPCIONES.

FORMULAS DE VALORACIÓN DE OPCIONES DE BLACK-SCHOLES

Las formulas de valoración de opciones para el precio en el tiempo cero de opciones call y
put del tipo europeo sobre un activo que no para dividendos, están dadas por

donde

  es  la  función  de  distribución  de  probabilidad  acumulativa  para  una  variable
la
,  S0  es  el  precio  del  activo  en  el  tiempo  cero,  K  es  el  precio  del  ejercicio,

volatilidad, T el tiempo de maduración y

 la tasa de interés libre de riesgo.

% Valoración de una Opción Call Europea utilizando la Fórmula de Black-
Scholes

clc
clear all

T=1; %Periodo de Expiración
S0=100; %Precio actual
K=100; %Precio de Ejercicio
r=0.05; %Tasa de Interés Libre de Riesgo
sigma=0.3; %Volatilidad Constante
R=(r+((sigma)^2)/2);
d1=(1/(sigma*sqrt(T)))*(log(S0/K)+R*(sqrt(T))^2);
d2=d1-(sigma*sqrt(T));
N1=normcdf(d1);
N2=normcdf(d2);
F=S0*N1-exp(-r*((sqrt(T))^2))*K*N2
%%%Comando Matlab
Call=blsprice(S0,K,r,T,sigma)

1

)()(21dNKedNSfrTocall−−=)()(12dNSdNKeforTput−−−=−TTrKSdo)21(ln21++=Tdd−=12)(xN)1,0(~Nr

Freddy H. Marín                                                                                                                    Universidad EAFIT

SIMULACIÓN MONTE-CARLO

Para  valorar  opciones  usando  simulación  Monte  Carlo,  se  considera  el  principio  de
valoración de riesgo neutral utilizando simulaciones del activo subyacente.

El procedimiento es el siguiente:

1.  Tome  M  simulaciones  de  la  dinámica  de  precios  para  St  en  un  mundo  de  riesgo

neutral según el tiempo de expiración de la opción.
2.  Calcule el pay-off del derivado en cada trayectoria.
3.  Calcule la media de los pay-off de cada trayectoria para estimar el payoff esperado

en un mundo de riesgo neutral.

4.  Descuente el pay-off esperado de la tasa de interés libre de riesgo para obtener una

estimación del valor derivado en el tiempo cero.

Para las simulaciones de la dinámica de precios del activo, se tiene un mejor resultado si se
toma el proceso solución discretizado de la ecuación diferencial homogénea, en lugar de la
aproximación  numérica  de  Euler  puesto  que  esta  última  es  convergente  siempre  que

, mientras que la primera es válida para cualquier

.

Considere  la  dinámica  de  precios  del  activo
valoración de riesgo neutral, el retorno esperado
, luego la ecuación resulta ser
riesgo,

.  Para  efectos  de  la
se cambia por la tasa de interés libre de

.

La  solución  discretizada  toma  la  forma

que  para  efectos  de  la

programación es más útil

donde

.

     Número de Trayectorias

El número de trayectorias depende de la aproximación requerida, si se toman M
trayectorias independientes como las descritas anteriormente, es usual calcular tanto la
media como la desviación estándar del pago descontado dados por las trayectorias
simuladas para obtener el valor de la opción. Se denota por m a la media y la desviación
estándar por w. En últimas, m debería ser el valor estimado del precio de la opción en el

tiempo cero. El error estándar de la estimación es

.

En un intervalo de confianza del 95% para el precio de la opción

 puede escribirse

como

.

2

0→ttttttdBSdtSdS+=rttttdBSdtSrdS+=)()21(2tttBBtrttteSS−+−++=tttrtteSS+−+=)21(12)1,0(~NtMwfMwmfMwm96.196.1+−

Freddy H. Marín                                                                                                                    Universidad EAFIT

Nota: Una ventaja de simulación Monte Carlo, es que puede proporcionar un error estándar
para la estimación que se hace, pero tiene una limitación y es que solo puede ser usada para
estimar el precio de opciones del tipo europeas.

     Técnicas de Reducción de Varianza

Para llevar a cabo la simulación de Monte Carlo, es usualmente necesario un
número muy grande M de trayectorias para la estimación de f con una aproximación
razonable. Este procedimiento puede ser muy costoso en términos del tiempo de
computo, por esta razón se describirán algunas técnicas que pueden reducir
dramáticamente el gasto computacional.

•  Técnica de Variables Antitéticas

En  esta  técnica,  la  simulación  de  trayectorias  involucra  el  cálculo  de  dos
valores  para  el  derivado.  El  primer  valor  f1,  se  calcula  en  forma  usual,  el
segundo  valor  f2  se  calcula  cambiando  el  signo  de  todos  los  números
aleatorias de la distribución normal estándar.

De  este  modo  el  valor  esperado  del  derivado  se  calcula  como  el  promedio

entre  f1  y  f2  es  decir

.  El  error  estándar  de  esta  estimación  es

que  es  mucho  menor  que  el  error  estándar  calculado  con  2M

trayectorias.

•  Técnica de Control Variada

Esta  técnica  es  aplicable  cuando  se  tienen  dos  instrumentos  derivados
similares,  A  y  B.  El  derivado  A  es  el  instrumento  bajo  consideración,  el
derivado B es similar al derivado A y tiene una solución analítica conocida.
Se  llevan  a  cabo  2  simulaciones  en  paralelo  usando  la  misma  muestra  de
.  La  primera  se  usa  para  obtener  una
números  aleatorios  y  el  mismo
  del  valor A; la  segunda se  usa  para obtener una estimación
estimación

 del valor de B. Una buena estimación de

se obtiene con la ecuación

donde

es  el  valor  verdadero  conocido  de  B.  para

efectos  prácticos  el  valor
Black-Scholes, en este caso.

  puede  encontrarse  utilizando  la  formula  de

3

221fff+=Mw*Af*BfAfBBAAffff+−=**BfBf

Freddy H. Marín                                                                                                                    Universidad EAFIT

%Valoración de una opción Call Europea utilizando simulación Monte Carlo

clc
clear all

T=1; %periodo de maduración
S0=100; %Precio actual
K=100; %Precio de ejercicio
r=0.05; %Tasa de interés
sigma=0.3; %Volatilidad

W=1000; % Número de repeticiones
k=10000; %Número de Trayectorias
m=200; %Número de subdivisiones
dt=T/m; %Incremento en el tiempo

for n=1:W
    rn=randn(k,m);
    for i=1:k
        S1(i,1)=S0;%Valor inicial
    end
    for i=1:k
        for j=2:m+1
            S1(i,j)=S1(i,j-1)+r*S1(i,j-1)*dt+sigma*S1(i,j-1)*sqrt(dt)*rn(i,j-
1);%Simulación Trayectorias
        end
    end
    for i=1:k
        Strike1(i)=S1(i,m+1);
    f1(i)=exp(-r*T)*max(Strike1(i)-K,0);
    end
M1(n)=mean(f1);
end

mi=min(M1);
MMC=mean(M1);
ms=max(M1);
Intervalo=[mi MMC ms]
% histfit(M1,20)

4

Freddy H. Marín                                                                                                                    Universidad EAFIT

ÁRBOLES BINOMIALES

Suponga  que  la  vida  de  una  opción  sobre  un  activo  que  no  paga  dividendos,  con  precio
. En cada
inicial

 sub-intervalos de longitud

y precio de ejercicio

, es dividida en

intervalo de tiempo el precio del activo se mueve desde su valor inicial

, a uno de dos

nuevos  valores

  y

.  El  movimiento  de

a

es  un  salto  hacia  arriba  y  el

 a

movimiento de
La probabilidad de un salto hacia arriba se denota por p y la probabilidad de los saltos hacia
abajo es denotada por

es un salto hacia abajo.

.

Como  esta  valoración  se  está  considerando  en  un  mundo  de  riesgo  neutral,  el  retorno
esperado del activo es la tasa de interés libre de riesgo, r. De este modo, el valor esperado
del precio del activo al final del intervalo de tiempo de longitud
, donde So es
el precio del activo al comienzo del intervalo de tiempo, esto es

 es

Por otro lado la varianza del cambio proporcional en el precio del activo en un intervalo de
tiempo de longitud

, luego,

 es

Una solución para esta ecuación está dada por
orden superior para

 son ignorados.

y

donde los términos de

El proceso de ramificación puede extenderse tanto como se quiera dependiendo del número
de  sub-intervalos.  En  general,  en  el  tiempo  cero,  el  precio  del  activo  So  se  conoce  en  el
tiempo

 existen dos posibilidades para el precio del activo

, en el tiempo

y

hay 3 posibilidades

,

y

y así sucesivamente.

5

oSKNtoSuSodSooSuSooSdSo)1(p−ttroeSdudepdppuedSpupSeStrtrootro−−=−+=−+=)1()1(tt22222])1([)1(dppudpput−+−−+=tredpdpu−++=2222trtreddudude−+−−−=2222)()()(trtreddudude−+−−−=2222)()()(.)(2trtreuddue−−+=teu=ted−=ttuSodSot22uSooS2dSo

Freddy H. Marín                                                                                                                    Universidad EAFIT

De este modo en el tiempo
dados por

, para

hay i+1 posibles precios para el activo los cuales están

  (Ver figura 1).

Precio del Activo

S0

S0u

(1)

S2

S0d

(1)

S1

S0u2

(2)

S3

S0ud

(2)

S2

S0u3

(3)

S4

S0u2d

(3)

S3

S0d2u

(3)

S2

S0d2

(2)

S1

2

S0d3

(3)

S1

S0u4

(4)

S5

S0u3d

(4)

S4

S0d2u2

(4)

S3

S0d3u

(4)

S2

S0d4

(4)

S1

tiempo:=

0

1
0

3
0

4
0

Figura 1. Recombinación en árboles binomiales multiplicativa en la cual se ilustra el
comportamiento de ramificación del proceso en cada nodo.

La  valoración  de  opciones  comienza  al  final  del  árbol  en  el  tiempo  T  y  se  procede
calculando los valores hacia atrás, dado que el valor de la opción se conoce en el tiempo T.
Por  ejemplo  para  el  caso  de  una  opción  call  europea  se  sabe  que  el  pay  off  es
.
Puesto que esta valoración está dada en un mundo de riesgo neutral, el valor en cada nodo
, puede ser calculado como el valor esperado en el tiempo T descontado a
del tiempo
la tasa de interés libre de riesgo para un periodo de tiempo
. Así mismo para todos los
tiempos en cada nodo hasta llegar al nodo inicial en el tiempo cero. (Ver figura 2)

 es el precio del activo en el tiempo T con precio de ejercicio

donde

6

tijijOduS−ij,...,2,1,0 =0,KSmáxT−TSKtT−tti

Freddy H. Marín                                                                                                                    Universidad EAFIT

Valor de La  Opción

f

fu

(1)

S2

fd

(1)

S1

fuuu

(3)

S4

fudu

fddu

fuu

(2)

S3

fud

(2)

S2

fdd

(2)

S1

fddd

d

fuuuu

u

fuuud

d

(4)

S4
fuudd

fuddd

fdddd

0

1
0

2

3
0

4
0

tiempo:=

Figura 2. Recombinación en árboles binomiales multiplicativa en la cual se ilustra el
comportamiento de ramificación hacia atrás del precio de la opción en cada nodo.

Aproximación Algebraica

Se  hará  referencia  al  j-ésimo  nodo  en  el  tiempo

  como  el  nodo  (i,j)  donde

. Defina

como el valor de la opción en el nodo (i,j)

o  para una opción call europea, el valor de la opción en su fecha de maduración

está dada por

 por tanto

;

o  para  el  caso  de  una  opción  put  europea,  el  valor  de  la  opción  en  su  fecha  de

maduración está dada por

, por tanto,

7

tiijNi0;0jif,]0,max[KST−MjduSfjNjOjN,...,2,1,0  para]0,max[,==−ij0y1-Ni0  para])1([,11,1,−+=+++−jijitrjifppfef]0,max[TSK−MjduSKfjNjOjN,...,2,1,0  para]0,max[,=−=−ti.ij0y1-Ni0  para])1([,11,1,−+=+++−jijitrjifppfef

Freddy H. Marín                                                                                                                    Universidad EAFIT

%Valoración De Una Opción Call Europea Utilizando El Método De Árboles
%Binomiales

clc
clear all

T=1; %periodo de maduración
S0=100; %Precio actual
K=100; %Precio de ejercicio
r=0.05; %Tasa de interés
sigma=0.3; %Volatilidad

n=1000; %Número de periodos
dt=T/n; %Icremento en el tiempo
u=exp(sigma*sqrt(dt));
d=1/u;
a=exp(-r*dt);
p=1/2+1/(2*sigma)*(r-1/2*sigma^2)*sqrt(dt); %Probabilidad de transición

SF=zeros(n+1,n+1); %Inicialización recombinacióm binomial precios
Opt=zeros(n+1,n+1); %Inicialización recombinacióm binomial opciones

for i=1:n+1
    for j=1:i
        SF(i,j)=S0*u^(j-1)*d^(i-j); %Recombinacióm binomial multilplicativa
precios
    end
end

for j=1:n+1
    Opt(n+1,j)=max(SF(n+1,j)-K,0); %Payoff en el punto final de precios
end

for i=n:-1:1
    for j=1:i
        Opt(i,j)= a*((1-p)*Opt(i+1,j)+p*Opt(i+1,j+1)); %Recombinación traída a
valor presente
    end
end

V=Opt(1,1) %Precio de la opción en el punto inicial

8

Freddy H. Marín                                                                                                                    Universidad EAFIT

MÉTODO DE DIFERENCIAS FINITAS EXPLICITO

Este método determina el valor de la opción resolviendo la ecuación diferenciales de Black-
Scholes-Merton. Esta  ecuación diferencial  es  convertida en un conjunto de ecuaciones  en
diferencia las cuales son resueltas iterativamente.

Considere la ecuación diferencial dada por

Suponga que la vida de la opción es T.

El  intervalo  de  tiempo  [0,T]  es  dividido  en  n  subintervalos  iguales  de  longitud

,

para un total N+1 periodos de tiempo, esto es

.

Suponga que

 es un precio del activo suficientemente grande (3 veces el precio inicial

del  activo  funciona  bien).  Defina

y  considere  un  total  de  M+1  precios

espaciados igualmente, esto es

.

El nivel
activo.

 se escoge de tal modo que uno de los valores

 sea el precio presente del

Los puntos en el tiempo y los puntos del precio del activo definen una malla que consiste
en un total de (M+1)*(N+1) puntos (ver figura).

9

rfSSfSfrStftttt=++222221NTt=Ttt,...,2,,0máxSMSSmáx=máxSSS...,,2,,0máxSStS),(),(Sjtiji=

Freddy H. Marín                                                                                                                    Universidad EAFIT

El nodo (i,j) sobre la malla es el punto que corresponde al tiempo

y al precio del activo

. Así,

 denotará el valor de la opción en el nodo (i,j).

Para un nodo interior (i+1,j) sobre la malla,

puede ser aproximado por

(Diferencia forward)

(Diferencia backward)

Una forma más adecuada es utilizar la aproximación simétrica

Para

se usará la diferencia forward dada por

.

Para

también se usará la diferencia forward dada por

La ecuación en diferencias finitas asociada a la ecuación de Black-Scholes-Merton toma la
forma

10

tiSjjif,SfSffSfjiji−=+++,11,1SffSfjiji−=−++1,1,1SffSfjiji−=−+++21,11,1tftfftfjiji−=+,,122SfSSffSffSfjijijiji−−−=−+++++1,1,1,11,122−+=+−+++2,11,11,122)(2SfffSfjijijijijijijijijijijirfSfffSjSffSrjtff,2,11,11,12221,11,1,,1)(2)(212=−++−+−+−+++−++++jijijijiftrfrjjfjtfrjj,1,122,1221,122)1(2211221+=++−+−+++−+

Freddy H. Marín                                                                                                                    Universidad EAFIT

Luego,

Finalmente,

, donde

Las condiciones de frontera dependen del tipo de opción que se quiera valorar.

A continuación se describirán las condiciones para las opciones call y put del tipo europeo.

•  opciones call

▪  el valor de una opción call en el tiempo T es
es el precio del activo en el tiempo T, luego

donde ST

▪  el valor de una opción call cuando el precio del activo es cero es 0,

luego

▪  el  valor  de  una  call  cuando  el  precio  del  activo  es  Smax    es  Smax-K,

luego

▪  el valor de una call en los nodos internos de la malla están dados por

Para

,

11

1,122,1221,122,2211111122111+++−++++−++−+=jijijijitfrjjtrtfjttrtfrjjtrf1,1,11,1,+++−+++=jijjijjijjifcfbfaf=ja−+221122rjjtrt−+=2211jttrtbj++=221122rjjtrtcj]0,max[KST−MjKSjfjN,...,2,1,0  para]0,max[,=−=Nifi,...,2,1,0  para  00,==NiSfMi,...,2,1,0  paraK  -max,==1,1,11,1,+++−+++=jijjijjijjifcfbfafNi,...,2,1,0  =1,...,2,1  −=Mj

Freddy H. Marín                                                                                                                    Universidad EAFIT

tiempo 0

tiempo T

•  opciones put

▪  el valor de una opción put en el tiempo T es

 donde

ST es el precio del activo en el tiempo T, luego

▪  el  valor  de  una  put  cuando  el  precio  del  activo  es  cero  es  K,  luego

▪  el  valor  de  una  put  cuando  el  precio  del  activo  es  Smax  es  0,  luego

▪  el  valor  de  una  put  en  los  nodos  internos  de  la  malla  están  dados

por

Para

,

12

]0,max[TSK−MjSjKfjN,...,2,1,0  para]0,max[,=−=NiKfi,...,2,1,0  para  0,==NifMi,...,2,1,0  para 0,==1,1,11,1,+++−+++=jijjijjijjifcfbfaf1,...,2,1,0  −=Ni1,...,2,1  −=Mjjif,1,1−+jifjif,1,1++jif0,KSjmáxf−=KSfmáx−=0=f

Freddy H. Marín                                                                                                                    Universidad EAFIT

%Valoración De Una Opción Call Europea Utilizando el Método de
Diferencias finitas explicitas

clc
clear all
T=1; %periodo de maduración
S0=100; %Precio actual
K=100; %Precio de ejercicio
r=0.05; %Tasa de interés
sigma=0.3; %Volatilidad
Smax=2*K; %Valor máximo en el dominio numérico
ds=10; %Incremento en el precio
ns=(Smax/ds); %Número de nodos en el eje del precio
dtp=(ds/(sigma*Smax))^2; %Incremento de prueba para el eje temporal
ntp=T/dtp; %Número de nodos de prueba en el eje temporal
nt=ceil(T/dtp); %Incremento mínimo para el eje temporal
dt=T/nt; %Número de nodos mínimo para el eje temporal
S(1)=0;

for j=2:ns+1
    S(j)=S(j-1)+ds; %Valores en el eje del precio
end

MO=zeros(nt+1,ns+1); %INicialización de la matriz de opciones (Incluye frontera
izquierda)

MO(:,ns+1)=Smax-K; %Fontera Dereha

for j=1:ns
    MO(nt+1,j)= max(S(j)-K,0); %Frontera inferior
end

%Coeficientes de la ecuacion en Diferencias Finitas
for j=1:ns+1
    a(j)= (dt/(1+r*dt))*((-1/2)*r*(j-1)+(1/2)*sigma^2*(j-1)^2);
    b(j)= (dt/(1+r*dt))*((1/dt)-sigma^2*(j-1)^2);
    c(j)=(dt/(1+r*dt))*((1/2)*r*(j-1)+(1/2)*sigma^2*(j-1)^2);
    suma(j)=a(j)+b(j)+c(j);
end
% plot(a)
% plot(b)
% plot(c)
% plot(suma) %Para verificar que los coeficientes entán entre 0 y 1
for i=nt:-1:1
    for j=2:ns
        MO(i,j)=a(j)*MO(i+1,j-1)+b(j)*MO(i+1,j)+c(j)*MO(i+1,j+1); %Esquema
numérico
    end
end

Pos=S0/ds+1; %Ubicación del valor de la opción en la frontera superior
DF=MO(1,Pos) %Valor de la opción
MO %Matriz de opciones
surf(MO) %Superficie de opciones

13

