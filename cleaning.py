"""
Limpia cada serie de precios de data/preprocess/ y conserva unicamente los
250 datos MAS NUEVOS (ultimos 250 por fecha) de cada activo.

No se asume que las series vengan ordenadas: cada CSV se ordena por fecha de
forma ascendente antes de recortar, de modo que siempre nos quedamos con las
250 observaciones mas recientes disponibles.

Cada CSV resultante se guarda con el mismo nombre en data/cleaned/ y mantiene
el formato original:
    date,<nombre_activo>
"""

from pathlib import Path

import pandas as pd

# Rutas relativas a la ubicacion del script
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "data" / "preprocess"
OUTPUT_DIR = BASE_DIR / "data" / "cleaned"

# Cantidad de observaciones mas recientes a conservar por serie.
N_LATEST = 250


def clean_series(csv_path: Path) -> int:
    """Lee una serie, conserva los N_LATEST datos mas nuevos y la guarda.

    Devuelve el numero de filas escritas.
    """
    df = pd.read_csv(csv_path)

    # La primera columna siempre es la fecha.
    date_col = df.columns[0]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # Elimina filas sin fecha valida (no se pueden ordenar por tiempo).
    df = df.dropna(subset=[date_col])

    # Ordena ascendente por fecha (las series pueden venir desordenadas)
    # y se queda con las ultimas N_LATEST, es decir, las mas recientes.
    df = df.sort_values(by=date_col).tail(N_LATEST).reset_index(drop=True)

    # Restaura el formato de fecha original (YYYY-MM-DD).
    df[date_col] = df[date_col].dt.strftime("%Y-%m-%d")

    out_path = OUTPUT_DIR / csv_path.name
    df.to_csv(out_path, index=False)
    return len(df)


def main() -> None:
    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"No se encontro la carpeta de entrada: {INPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = sorted(INPUT_DIR.glob("*.csv"))
    if not csv_files:
        print(f"No se encontraron archivos CSV en {INPUT_DIR}")
        return

    total = 0
    for csv_path in csv_files:
        rows = clean_series(csv_path)
        total += 1
        print(f"  {csv_path.name:<24} -> {rows} filas (mas recientes)")

    print(f"\nListo. Se limpiaron {total} series en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
