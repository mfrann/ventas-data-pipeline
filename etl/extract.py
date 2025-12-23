import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "datos"

def extract_csv():
    print('Iniciando lectura de archivos...')

    try:
    # --- CREANDO DATAFRAMES DE CADA ARCHIVO CSV
        df_ventas = pd.read_csv(DATA_DIR / 'ventas.csv')
        df_productos = pd.read_csv(DATA_DIR / 'productos.csv')
        df_clientes = pd.read_csv(DATA_DIR / 'clientes.csv')
        df_vendedores = pd.read_csv(DATA_DIR / 'vendedores.csv')

        print('✓ Todos los archivos cargados correctamente\n')

        return df_ventas, df_productos, df_clientes, df_vendedores
    
    except FileNotFoundError as e:
        print(f'✗ Error: {e}')
        exit()