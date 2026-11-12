"""
Extrae cada serie de precios del archivo Excel de Bloomberg y guarda un CSV
por activo en la carpeta data/.

Estructura del Excel de commodities (hoja 'Hoja1'):
    - Fila 0: nombres de los activos (la primera celda esta vacia).
    - Fila 1: subencabezado basura ('#N/A Requesting Data...').
    - Fila 2: subencabezado de columnas ('Dates' / 'PX_LAST').
    - Columna 0: fechas (a partir de la fila 3).
    - Columnas 1..N: precios de cada activo.

Cada CSV resultante tiene el formato:
    date,<nombre_activo>
"""

from pathlib import Path

import pandas as pd

# Rutas relativas a la ubicacion del script
BASE_DIR = Path(__file__).resolve().parent
EXCEL_PATH = BASE_DIR / "data" / "raw" / "comodities.xlsx"
OUTPUT_DIR = BASE_DIR / "data"
SHEET_NAME = "Hoja1"

# Numero de filas de cabecera antes de que empiecen los datos reales.
# Fila 0: nombres de activos, fila 1: '#N/A...', fila 2: 'Dates'/'PX_LAST'.
HEADER_ROWS = 3


def sanitize_filename(name: str) -> str:
    """Convierte el nombre de un activo en un nombre de archivo seguro.

    Reemplaza espacios por guiones bajos y elimina caracteres no validos
    para nombres de archivo en Windows.
    """
    invalid = '<>:"/\\|?*'
    cleaned = "".join("_" if ch in invalid else ch for ch in name.strip())
    cleaned = cleaned.replace(" ", "_")
    # Colapsa guiones bajos repetidos
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_")


def main() -> None:
    if not EXCEL_PATH.exists():
        raise FileNotFoundError(f"No se encontro el archivo Excel: {EXCEL_PATH}")

    # Leemos sin encabezado para manejar manualmente las dos filas de cabecera.
    raw = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME, header=None)

    # Fila 0: nombres de activos. Columna 0 esta vacia (es la de fechas).
    asset_names = raw.iloc[0].tolist()

    # Los datos reales empiezan despues de las filas de cabecera.
    data = raw.iloc[HEADER_ROWS:].reset_index(drop=True)

    # Columna 0 -> fechas
    dates = pd.to_datetime(data.iloc[:, 0]).dt.strftime("%Y-%m-%d")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    exported = []
    # Recorremos cada columna de activos (desde la 1 en adelante)
    for col_idx in range(1, raw.shape[1]):
        asset = asset_names[col_idx]
        if asset is None or (isinstance(asset, float) and pd.isna(asset)):
            continue  # salta columnas sin nombre de activo

        asset = str(asset).strip()
        series = pd.to_numeric(data.iloc[:, col_idx], errors="coerce")

        out_df = pd.DataFrame({"date": dates, asset: series})
        # Elimina filas donde no hay fecha o no hay precio
        out_df = out_df.dropna(subset=["date", asset])

        filename = sanitize_filename(asset) + ".csv"
        out_path = OUTPUT_DIR / filename
        out_df.to_csv(out_path, index=False)

        exported.append((asset, filename, len(out_df)))
        print(f"  {asset:<18} -> {filename:<22} ({len(out_df)} filas)")

    print(f"\nListo. Se exportaron {len(exported)} series a: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
