from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

def save_to_csv(df, filename):
    OUTPUT_DIR.mkdir(exist_ok=True)

    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False)

    print(f"✓ Archivo guardado: {path}")