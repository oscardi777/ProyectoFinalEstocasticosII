# Proyecto Final — Procesos Estocásticos II

Valoración de opciones Call europeas sobre la tasa de cambio **CAD/USD** (serie
FRED `DEXCAUS`), modelada como **Movimiento Browniano Geométrico (MBG)**. El
proyecto verifica empíricamente los supuestos del MBG sobre los retornos
logarítmicos, estima sus parámetros y valora las opciones por cuatro métodos:
Black–Scholes (fórmula cerrada), simulación de Monte Carlo, árbol binomial de
Cox–Ross–Rubinstein y diferencias finitas explícitas.

El informe completo del proyecto (paso a paso, resultados y conclusiones) está
en `informe.pdf` (fuente LaTeX en `main.tex`).

## Contenido del repositorio

| Archivo / carpeta | Descripción |
|---|---|
| `main.ipynb` | Notebook principal. Analiza la serie `DEXCAUS`, contrasta los supuestos del MBG, estima $\hat\mu$ y $\hat\sigma$, pronostica sobre la muestra y valora las 20 opciones Call europeas por los cuatro métodos. |
| `data/DEXCAUS.csv` | Serie del tipo de cambio CAD/USD (formato `observation_date,DEXCAUS`), 250 observaciones válidas entre nov-2025 y nov-2026. Es el único insumo del notebook. |
| `extract_series.py` | Script de preprocesamiento (opcional): extrae series desde un Excel de Bloomberg hacia CSV por activo. |
| `cleaning.py` | Script de preprocesamiento (opcional): recorta cada serie a las 250 observaciones más recientes. |
| `main.tex` / `informe.pdf` | Informe del proyecto en LaTeX y su versión compilada en PDF. |
| `Citas.bib` | Bibliografía del informe. |
| `index.html` | Página de inicio que enlaza a los resultados exportados. |
| `results-html/runCAN-USD_Crncy.html` | Ejecución del notebook exportada a HTML (resultados y gráficos sin necesidad de ejecutar). |
| `images/` | Figuras generadas por el notebook y usadas en el informe. |
| `theory/` | Material teórico de referencia (Black–Scholes, valoración riesgo-neutral, martingalas, métodos numéricos). |
| `requirements.txt` | Dependencias de Python del proyecto. |
| `enunciado.pdf` | Enunciado del proyecto. |

## Verificación de los supuestos del MBG

El notebook contrasta sobre los **retornos logarítmicos** y las **perturbaciones
estandarizadas** las tres condiciones que exige el MBG, a un nivel de
significancia del 5 %:

- **Normalidad de los retornos** (incrementos gaussianos): pruebas de
  Jarque-Bera, Kolmogorov-Smirnov, Anderson-Darling y Lilliefors, respaldadas
  por el histograma y el gráfico Q-Q.
- **Estacionariedad de las perturbaciones** (incrementos independientes, sin
  tendencia): prueba de raíz unitaria Dickey-Fuller Aumentada.
- **Homocedasticidad** (volatilidad $\sigma$ constante): test ARCH de Engle y
  prueba de Ljung-Box sobre los residuos al cuadrado, más la gráfica de
  volatilidad acumulada.

Como diagnóstico complementario de la ausencia de memoria de largo plazo se
calculan la **dimensión fractal** y el **exponente de Hurst** (referencia para
un movimiento browniano: DF ≈ 1,5, EH ≈ 0,5, DF + EH ≈ 2).

## Estimación de parámetros y valoración

- **Estimación.** Los parámetros $\hat\mu$ y $\hat\sigma$ se estiman por dos
  vías: retornos simples bajo la discretización de Euler-Maruyama y log-retornos
  con la solución exacta del MBG. Sobre la muestra se evalúa el pronóstico
  (inducido y simulado) con el criterio de un MAPE promedio inferior al 5 %.
- **Valoración.** Con $r=0{,}05$, $S_0$ igual al último precio observado y la
  volatilidad histórica estimada, se simulan 10.000 trayectorias fuera de
  muestra por cada maduración $T\in\{1,\tfrac12,\tfrac13,\tfrac14\}$ años. Los
  cinco precios de ejercicio $K$ por maduración son los percentiles 10, 25, 50,
  75 y 90 de $S_T$. Las 20 combinaciones $(T,K)$ se valoran con los cuatro
  métodos, tomando Black-Scholes como referencia.

## Cómo ejecutarlo

Requisitos previos: **Python 3.11+** y `git`.

### 1. Clonar el repositorio

```bash
git clone https://github.com/oscardi777/ProyectoFinalEstocasticosII.git
cd ProyectoFinalEstocasticosII
```

### 2. Crear el entorno virtual e instalar dependencias

En **Windows (PowerShell)**:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

En **macOS / Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Abrir el notebook

```bash
jupyter lab
```

Abre `main.ipynb` y ejecuta las celdas en orden (menú *Run > Run All*). Los
parámetros configurables (ventanas de estimación, número de simulaciones, tasa
libre de riesgo, etc.) están en la sección **"Parámetros y funciones
configurables"** al inicio del notebook. El notebook está fijado al único
conjunto de datos `data/DEXCAUS.csv`.

### Ver los resultados sin ejecutar

Abre `index.html` en el navegador, o directamente
`results-html/runCAN-USD_Crncy.html`, para consultar la ejecución exportada con
todos los gráficos y tablas.

## Notas

- La carpeta `venv/` está excluida del control de versiones mediante
  `.gitignore`; cada quien crea su propio entorno con `requirements.txt`.
- `extract_series.py` y `cleaning.py` son utilidades de preprocesamiento que
  operan sobre datos crudos (Excel de Bloomberg y carpetas intermedias) no
  incluidos en el repositorio; no son necesarias para ejecutar el análisis, pues
  `data/DEXCAUS.csv` ya está listo.
- No rechazar la hipótesis nula de una prueba no demuestra que el supuesto sea
  cierto; indica que no hay evidencia en contra con la muestra disponible
  (250 observaciones).
