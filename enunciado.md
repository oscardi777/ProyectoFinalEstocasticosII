Indicaciones y rubrica para la presentación del trabajo ﬁnal

1.   Descargar una base de datos de cualquier variable ﬁnanciera con un mínimo de

250 observaciones a partir del día de consulta hacia atrás.

2.   Veriﬁcar que se cumplen todas las condiciones estadísticas que permiten aﬁrmar
que el activo propuesto puede ser modelado como un Movimiento Browniano
Geométrico, con su respectivo análisis y conclusiones.

3.   Estimar parámetros y hacer el pronóstico inducido sobre la muestra con 10.000

simulaciones reportando las métricas de ajuste y precisión.

4.   Hacer el pronóstico simulado sobre la muestra con 10.000 simulaciones

reportando las métricas de ajuste y precisión.

5.   Realizar una comparación numérica entre la fórmula de Black-Scholes, Simulación
Monte Carlo, Árboles Binomiales y Diferencias Finitas Explícitas para los tiempos de
maduración T=[1, 1/2, 1/3 y 1/4], para 5 precios de ejercicio K tomados de las
múltiples trayectorias simuladas fuera de muestra para cada periodo T.

El informe deberá ser presentado en formato artículo con los siguientes ítems:

1.  Título, autores y asesor, resumen, palabras clave.

2.  Introducción. Entre otras cosas, se debe enfatizar en la siguiente pregunta ¿porqué

es importante en el sector real, la modelación de activos (materias primas,
acciones, divisas, etc.) y la valoración de instrumentos derivados ﬁnancieros como
las opciones?

3.  Preliminares matemáticos. Hacer una breve descripción de los elementos
matemáticos clave bajo los cuales se constituyen tanto la fórmula de Black-
Scholes, como los métodos numéricos para valorar opciones ﬁnancieras (si la serie
de tiempo puede modelarse como un Movimiento Browniano Geométrico) con sus
respectivas referencias bibliográﬁcas.

1.  Metodología.

  Descripción de los datos: Hacer una descripción cualitativa de los datos que
incluya el contexto de la empresa, fenómeno, activo, etc., resaltando algunos
comportamientos importantes de los datos históricos (saltos, picos, mínimos,
máximos, cambios de régimen, etc.) que pueden estar documentados en noticias o
análisis externos, fechas de inicio - ﬁnal y la página web o repositorio de donde se
extrajeron los datos. Así mismo hacer una descripción estadística básica de la
serie.



Indicadores y tests estadísticos: Presentar los resultados de los tests y pruebas
estadísticas que permiten aﬁrmar técnicamente, que los datos pueden ser
modelados como un Movimiento Browniano Geométrico.

  Estimación y pronóstico sobre la muestra: Mostrar los resultados tanto de la

estimación de parámetros, como del MAPE promedio en el que se espera un valor
inferior al 5%.

  Valoración de opciones ﬁnancieras del tipo Call Europeas: Usar la fórmula de

Black-Scholes y los métodos numéricos propuestos para valorar las opciones con
la volatilidad estimada de sus datos históricos, r=0.05, precio spot= ultimo dato de
la serie de tiempo, los precios de ejercicio K y las fechas de maduración T descritas
anteriormente. Los resultados deberán estar tabulados incluyendo el error relativo
entre los resultados de cada método comparado con la fórmula de Black-Scholes y
deberán estar bien etiquetados.

    5. Conclusiones. Se incluyen los resultados en términos de precisión, complejidad
algorítmica, tiempo de computo, etc. y observaciones sobre el comportamiento del precio
de la opción como por  ejemplo, que ocurre cuando el precio de ejercicio K aumenta o
disminuye? y qué ocurre a medida

        que aumenta la fecha de maduración?.

1.  Referencias bibliográﬁcas.

