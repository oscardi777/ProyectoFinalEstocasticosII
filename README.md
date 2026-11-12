# Proyecto Final — Procesos Estocásticos II

Modelación de series financieras como **Movimiento Browniano Geométrico (MBG)**,
verificación de los supuestos del modelo y valoración de opciones europeas mediante
Black–Scholes y simulación de Monte Carlo.

## Contenido del repositorio

| Archivo / carpeta | Descripción |
|---|---|
| `notebookMultiVersion.ipynb` | Notebook principal. Modela varios activos como MBG, estima $\hat\mu$ y $\hat\sigma$, contrasta los supuestos del modelo (C1–C5) y valora opciones europeas. |
| `notebookFelipeVersion.ipynb` | Variante del análisis aplicada al tipo de cambio USD/CAD (serie FRED `DEXCAUS`), incluyendo pronóstico simulado con 10.000 trayectorias. |
| `extract_series.py` | Script que lee el Excel de Bloomberg (`data/raw/tecnology_exchange.xlsx`) y exporta un CSV por activo en `data/`. |
| `requirements.txt` | Dependencias de Python del proyecto. |
| `data/` | Series de precios en CSV (formato `date,<activo>`), listas para los notebooks. |
| `data/raw/` | Datos crudos de origen (Excel de Bloomberg). |
| `theory/` | Material teórico de referencia (Black–Scholes, valoración riesgo-neutral, martingalas, métodos numéricos). |
| `results-html/` | Carpeta de salida para resultados exportados en HTML. |
| `enunciado.pdf` | Enunciado del proyecto. |

### Series de datos en `data/`

- `AAPL_US_Equity.csv`, `MSFT_US_Equity.csv`, `NU_US_Equity.csv`, `CIB_US_Equity.csv` — acciones.
- `NDX_Index.csv`, `SPX_Index.csv` — índices bursátiles.
- `EUR_Curncy.csv`, `COP_REGN_Curncy.csv`, `DEXCAUS.csv` — divisas / tipos de cambio.

## Pruebas aplicadas al supuesto de MBG

Ambos notebooks siguen la misma lógica de contraste:

- **C1** — Normalidad de los log-retornos.
- **C2** — Independencia de los log-retornos.
- **C3** — Varianza constante.
- **C4** — Estabilidad de parámetros entre subperiodos.
- **C5** — Simulación Monte Carlo frente a la trayectoria real.

## Cómo ejecutarlo rápido

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

### 3. (Opcional) Regenerar los CSV desde el Excel original

Los CSV ya están en `data/`, pero si quieres reconstruirlos desde el Excel de Bloomberg:

```bash
python extract_series.py
```

### 4. Abrir los notebooks

```bash
jupyter lab
```

Abre `notebookMultiVersion.ipynb` (análisis principal) o `notebookFelipeVersion.ipynb`
y ejecuta las celdas en orden (menú *Run > Run All*). Los parámetros configurables
(activo a analizar, ventanas de estimación, etc.) están en la sección **"Parámetros
y funciones configurables"** al inicio del notebook.

## Notas

- La carpeta `venv/` está excluida del control de versiones mediante `.gitignore`;
  cada quien crea su propio entorno con `requirements.txt`.
