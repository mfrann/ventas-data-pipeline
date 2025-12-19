#===LIBRERIAS===#
import pandas as pd
from sqlalchemy import create_engine
#===============#



#================================================#
#            TAREA 1: EXTRAER (EXTRACT)          #
#================================================#

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


show_info_complete("ventas", df_ventas)
print("==="*20)
show_info_complete("clientes", df_clientes)
print("==="*20)
show_info_complete("productos", df_productos)
print("==="*20)
show_info_complete("vendedores", df_vendedores)
print("==="*20)

print("\n✓ Exploración completada")




#================================================#
#          TAREA 2: TRANSFORMAR (TRANSFORM)      #
#================================================#


print('Eliminando duplicado de archivos...')
#--- PASO 1: ELIMINAR DUPLICADOS ---#
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

# --- EJECUTAR
df_ventas = delete_duplicates(df_ventas, 'Ventas')
df_vendedores = delete_duplicates(df_vendedores, 'Vendedores')
df_clientes = delete_duplicates(df_clientes, 'Clientes')
df_productos = delete_duplicates(df_productos, 'Productos')


print("\n" + "="*60)
print("✓ DUPLICADOS ELIMINADOS EN TODAS LAS TABLAS")
print("="*60)


print("===" * 30)



print('\nManejando nulos de archivos...')
#--- PASO 2: MANEJAR NULOS ---#
def identify_nulls(df, name):
    """
    Solo mostrar donde hay nulos
    """

    print(f'\n--- {name.upper()} ---')

    null_for_column = df.isnull().sum() #Contar nulos por columna
    total_nulls = null_for_column.sum() #Suma total de numeros

    if total_nulls == 0: 
        print("✓ Sin valores nulos")
    else: 
        print("⚠ Valores nulos encontrados:") 
        #Comprueba si valores nulos es mayor a 0 
        for column, amount in null_for_column[null_for_column > 0].items(): #Y recorre por columna y cantidad en la variable, no usamos sum() pq iterariamos en un solo numero
            print(f"  - {column}: {amount} nulos")

# --- EJECUTAR
identify_nulls(df_ventas, 'Ventas')
identify_nulls(df_clientes, 'Clientes')
identify_nulls(df_productos, 'Productos')
identify_nulls(df_vendedores, 'Vendedores')

print("===" * 30)

#====== FUNCION PARA VENTAS ======#
def clean_ventas(df, name):
    
    """
        Eliminar filas con nulos en columnas críticas
        Mostrar antes/después
        Retornar DataFrame limpio
    """

    print(f'\n--- LIMPIANDO {name.upper()} ---')

    # --- CONTAR FILAS ANTES
    rows_before = len(df)
    #CONTAR NULOS
    nulls = df.isnull().sum()
    total_nulls = nulls.sum() #Suma de todos los nulos

    print(f'Filas antes: {rows_before}')
    print(f'Filas con nulos: {total_nulls}')

    # --- ELIMINAR NULOS 
    df = df.dropna() #Elimina los nulos

    # --- CONTAR FILAS DESPUES

    rows_after = len(df)
    rows_deleted = rows_before - rows_after

    print(f'Filas después: {rows_after}')
    print(f'Filas eliminadas: {rows_deleted}')

    # --- MENSAJE DE EXITO

    if rows_deleted == 0:
        print('✓ Sin nulos para eliminar')
    else:
        print(f'✓ Se eliminaron {rows_deleted} filas con nulos')



    return df

print("===" * 30)

#====== FUNCION PARA PRODUCTOS ======#
def clean_productos(df, name):



    print(f'\n--- LIMPIANDO {name.upper()} ---')



    # ====== CONTAR ======#


    # --- CONTAR FILAS ANTES
    rows_before = len(df)
    print(f'Antes: Hay {rows_before} filas.')

    # --- CONTAR NULOS CRITICOS
    rows_with_critics_nulls = df[['producto_id', 'nombre', 'categoria', 'costo']]
    print(f'Filas con nulos criticos: {rows_with_critics_nulls}')
    
    # --- ELIMINAR NULOS CRITICOS
    print('Eliminando nulos criticos...')
    df = df.dropna(subset=['producto_id', 'nombre', 'categoria', 'costo'])

    # --- CONTAR FILAS DESPUES
    rows_after = len(df)
    rows_deleted = rows_before - rows_after
    print(f'Se eliminaron {rows_deleted} filas con nulos')
    


    # ====== RELLENAR ======#

    # --- CONTAR NULOS EN UNA COLUMNA
    null_category = df['proveedor'].isnull().sum()

    # --- RELLENAR NULOS NO CRITICOS
    df['proveedor'] = df['proveedor'].fillna('Sin proveedor')


    # --- MOSTRAR NULOS NO CRITICOS

    if null_category > 0:
        print(f"Columna ['proveedor']: {null_category} nulos -> Rellenados con 'Sin proveedor'")
    else:
        print(f'Sin nulos que rellenar.')


    # --- FINAL 
    print(f'\nFilas después: {len(df)}')
    print('✓ Productos listos (sin nulos)')


    return df

# --- EJECUTAR
df_ventas = clean_ventas(df_ventas, 'Ventas')
df_productos = clean_productos(df_productos, 'Productos')





'''

def clean_clientes(df):
    pass

def clean_vendedores(df):
    pass

'''