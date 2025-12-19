#===LIBRERIAS===#
import pandas as pd
from sqlalchemy import create_engine
#===============#



#EXTRAER
print('Iniciando lectura de archivos...')

#===CONFIGURACIÓN===#

try:
    #CREANDO DATAFRAMES DE CADA ARCHIVO CSV
    df_ventas = pd.read_csv('datos/ventas.csv')
    df_productos = pd.read_csv('datos/productos.csv')
    df_clientes = pd.read_csv('datos/clientes.csv')
    df_vendedores = pd.read_csv('datos/vendedores.csv')

    print('✓ Todos los archivos cargados correctamente\n')
except FileNotFoundError as e:
    print(f'✗ Error: {e}')
    exit()

#===FUNCIONES AUXILIARES===#

#MOSTRAS FILAS Y COLUMNAS
def show_rows_col(csv):
    rows, cols = csv.shape
    print(f'Archivo leido: {rows} filas y {cols} columnas ')
    print("==="*20)

#MOSTRAR PRIMERAS 5 FILAS
def show_first_rows(csv):
    print(f' Las primeras 5 filas:\n {csv.head()}')
    print("==="*20)

#VER TIPOS DE DATOS DE COLUMNAS
def show_types(csv):
    print(f'Tipos de datos de columnas:\n {csv.info()}')
    print("==="*20)

#VERIFICAR SI HAY VALORES NULOS
def verify_null(csv):
    nulls = csv.isnull().any().any()

    if nulls:
        print('⚠ Valores nulos encontrados:')
        null_df = csv.isnull().sum()
        print(null_df[null_df>0])
    else:
        print('✓ No hay valores nulos.')



#================================================#
#            TAREA 1: EXTRAER (EXTRACT)          #
#================================================#

def show_info_complete(name, df):
    print(f"\n{'='*20}")
    print(f"  {name.upper()}")
    print('='*20)
    #COLUMNAS
    show_rows_col(df)
    #PRIMERAS FILAS
    print("\n--- Primeras filas ---")
    show_first_rows(df)
    #DATAFRAME
    print("\n--- Información del DataFrame ---")
    show_types(df)
    #VALORES NULOS
    print("\n--- Valores nulos ---")
    verify_null(df)


#======COMPROBAR LOS DATOS ======#

'''
show_info_complete("ventas", df_ventas)
print("==="*20)
show_info_complete("clientes", df_clientes)
print("==="*20)
show_info_complete("productos", df_productos)
print("==="*20)
show_info_complete("vendedores", df_vendedores)
print("==="*20)

print("\n✓ Exploración completada")
'''



#================================================#
#          TAREA 2: TRANSFORMAR (TRANSFORM)      #
#================================================#

#--- PASO 1: ELIMINAR DUPLICADOS ---#
'''

def delete_duplicates(df, name):
    """

    Elimina duplicados de archivo csv
    
    """

    print(f'\n--- {name.upper()} ---')
    
    #ANTES
    rows_before = len(df) #Longitud
    duplicates = df.duplicated().sum() #Cuenta cuantas filas duplicadas hay

    print(f'Filas antes: {rows_before}')
    print(f'Duplicados encontrados: {duplicates}')

    #Eliminar duplicados
    clean_df = df.drop_duplicates() #Elimina las filas duplicadas

    #DESPUES
    rows_after = len(clean_df)
    rows_deleted = rows_before - rows_after
    
    print(f'Filas despues: {rows_after}')
    print(f'Filas eliminadas: {rows_deleted}') 

    if duplicates == 0:
        print('✓ No se encontro duplicados.')
    else: 
        print(f'✓ Se eliminaron {duplicates} duplicados.')


    return clean_df

print("\n" + "="*60)
print("           ELIMINANDO DUPLICADOS")
print("="*60)

#AGREGAR A LOS ARCHIVOS CSV

#Usamos la misma variable, para luego no andar cambiando, y evitar errores.
df_ventas = delete_duplicates(df_ventas, 'Ventas')
df_vendedores = delete_duplicates(df_vendedores, 'Vendedores')
df_clientes = delete_duplicates(df_clientes, 'Clientes')
df_productos = delete_duplicates(df_productos, 'Productos')


print("\n" + "="*60)
print("✓ DUPLICADOS ELIMINADOS EN TODAS LAS TABLAS")
print("="*60)

'''

#--- PASO 2: MANEJAR NULOS ---#

null_data = df_ventas.isnull()

data_not_null = df_ventas.dropna()

print(data_not_null)



