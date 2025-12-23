#================================================#
#          TAREA 2: TRANSFORMAR (TRANSFORM)      #
#================================================#

# === LIBRERIAS === #
import pandas as pd

#================================================#
#                A.LIMPIEZA                      #
#================================================#

# TODO: ELIMINAR DUPLICADOS

def del_duplicates(df, name):
    print(f'\n--- {name.upper()} ---')

    # --- ANTES
    rows_before = len(df) #Longitud
    duplicates = df.duplicated().sum() #Cuenta cuantas filas duplicadas hay

    # --- ELIMINAR DUPLICADOS
    df = df.drop_duplicates() #Elimina las filas duplicadas

    # ---DESPUES
    rows_after = len(df)


    print(f"Filas antes: {rows_before}")
    print(f"Duplicados encontrados: {duplicates}")
    print(f"Filas después: {rows_after}")  

    return df

# TODO: IDENTIFICAR NULOS

def identify_nulls(df, name):
    print(f'\n--- {name.upper()} ---')
    
    nulls = df.isnull().sum() # --> cuenta los nulos
    total_nulls = nulls.sum() # --> Suma total de nulls


    if total_nulls == 0: 
        print("✓ Sin valores nulos")
    else: 
        print("⚠ Valores nulos encontrados:") 
        #Comprueba si valores nulos es mayor a 0 
        for column, amount in nulls[nulls > 0].items(): #Y recorre por columna y cantidad en la variable, no usamos sum() pq iterariamos en un solo numero
            print(f"  - {column}: {amount} nulos")    

# TODO: LIMPIEZA ESPECIFICA (CADA ARCHIVO CSV)

#* VENTAS.CSV
def clean_ventas(df, name):
    
    """
        Eliminar filas con nulos en columnas críticas
        Mostrar antes/después
        Retornar DataFrame limpio
    """

    print(f'\n--- LIMPIANDO {name.upper()} ---')

    # --- CONTAR FILAS ANTES
    rows_before = len(df)

    # --- CONTAR NULOS
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
        print('Sin nulos para eliminar')
        print('✓ Productos listos (sin nulos)')
    else:
        print(f'✓ Se eliminaron {rows_deleted} filas con nulos')

    return df 

#* PRODUCTO.CSV
def clean_productos(df, name):

    print(f'\n--- LIMPIANDO {name.upper()} ---')



    #================================================#
    #            PASO 1: CONTAR CRITICOS             #
    #================================================#

    # --- CONTAR FILAS ANTES
    rows_before = len(df)
    print(f'Antes: Hay {rows_before} filas.')

    # --- CONTAR NULOS CRITICOS
    rows_with_critics_nulls = df[['producto_id', 'nombre', 'categoria', 'costo']].isnull().any(axis=1).sum()
    print(f'Filas con nulos criticos: {rows_with_critics_nulls}')
    
    # --- ELIMINAR NULOS CRITICOS
    print('Eliminando nulos criticos...')
    df = df.dropna(subset=['producto_id', 'nombre', 'categoria', 'costo'])

    # --- CONTAR FILAS DESPUES
    rows_after = len(df)
    rows_deleted = rows_before - rows_after
    print(f'Se eliminaron {rows_deleted} filas con nulos')
    


    #================================================#
    #          PASO 2: RELLENAR NO CRITICOS          #
    #================================================#

    # --- CONTAR NULOS EN UNA COLUMNA
    null_category = df['proveedor'].isnull().sum()

    # --- RELLENAR NULOS NO CRITICOS
    df.loc[:, 'proveedor'] = df['proveedor'].fillna('Sin proveedor')

    # --- MOSTRAR NULOS NO CRITICOS
    if null_category > 0:
        print(f"Columna ['proveedor']: {null_category} nulos -> Rellenados con 'Sin proveedor'")
    else:
        print(f'Sin nulos que rellenar.')

    # --- FINAL 
    print(f'\nFilas después: {len(df)}')
    print('✓ Productos listos (sin nulos)')


    return df

#* CLIENTE.CSV
def clean_clientes(df, name):
        
        print(f'\n--- LIMPIANDO {name.upper()} ---')



        #================================================#
        #            PASO 1: CONTAR CRITICOS             #
        #================================================#

        # --- CONTAR FILAS ANTES
        rows_before = len(df)
        print(f'Antes: Hay {rows_before} filas.')

        # --- CONTAR NULOS CRITICOS
        rows_with_critics_nulls = df[['cliente_id', 'nombre']].isnull().any(axis=1).sum()
        print(f'Filas con nulos criticos: {rows_with_critics_nulls}')
    
        # --- ELIMINAR NULOS CRITICOS
        print('Eliminando nulos criticos...')
        df = df.dropna(subset=['cliente_id', 'nombre']) #Elimina valores vacios: dropna()

        # --- CONTAR FILAS DESPUES
        rows_after = len(df)
        rows_deleted = rows_before - rows_after
        print(f'Se eliminaron {rows_deleted} filas con nulos')
    


        #================================================#
        #          PASO 2: RELLENAR NO CRITICOS          #
        #================================================#

        # --- CONTAR NULOS EN UNA COLUMNA
        nulls_email = df['email'].isnull().sum()
        nulls_ciudad = df['ciudad'].isnull().sum()
        nulls_segmento = df['segmento'].isnull().sum()

        # --- RELLENAR NULOS NO CRITICOS
        
        #Creamos un diccionario y luego llenamos con fillna()
        valores_relleno = {
            'email': 'no_email@example.com',
            'ciudad': 'No especifica',
            'segmento': 'Regular'
        }

        df = df.fillna(valores_relleno) 

        # --- MOSTRAR NULOS NO CRITICOS
        if nulls_email > 0:
            print(f"Columna ['email']: {nulls_email} nulos -> Rellenados con 'no_email@example.com'")
        if nulls_ciudad > 0:
            print(f"Columna ['ciudad']: {nulls_ciudad} nulos -> Rellenados con 'No especifica'")
        if nulls_segmento > 0:
            print(f"Columna ['segmento']: {nulls_segmento} nulos -> Rellenados con 'Regular'")     
        else:
            print(f'Sin nulos que rellenar.')

        # --- FINAL 
        print(f'\nFilas después: {len(df)}')
        print('✓ Productos listos (sin nulos)')


        return df

#* VENDEDORES.CSV
def clean_vendedores(df, name):
        
        print(f'\n--- LIMPIANDO {name.upper()} ---')



        #================================================#
        #            PASO 1: CONTAR CRITICOS             #
        #================================================#

        # --- CONTAR FILAS ANTES
        rows_before = len(df)
        print(f'Antes: Hay {rows_before} filas.')

        # --- CONTAR NULOS CRITICOS
        rows_with_critics_nulls = df[['vendedor_id', 'nombre']].isnull().any(axis=1).sum()
        print(f'Filas con nulos criticos: {rows_with_critics_nulls}')
    
        # --- ELIMINAR NULOS CRITICOS
        print('Eliminando nulos criticos...')
        df = df.dropna(subset=['vendedor_id', 'nombre']) #Elimina valores vacios: dropna()

        # --- CONTAR FILAS DESPUES
        rows_after = len(df)
        rows_deleted = rows_before - rows_after
        print(f'Se eliminaron {rows_deleted} filas con nulos')
    


        #================================================#
        #          PASO 2: RELLENAR NO CRITICOS          #
        #================================================#

        # --- CONTAR NULOS EN UNA COLUMNA
        nulls_sucursal = df['sucursal'].isnull().sum()
        nulls_fecha = df['fecha_ingreso'].isnull().sum()

        # --- RELLENAR NULOS NO CRITICOS
        
        #Creamos un diccionario y luego llenamos con fillna()
        valores_relleno = {
            'sucursal': 'Sin asignar',
            'fecha_ingreso': 'No fecha'
        }

        df = df.fillna(valores_relleno) 

        # --- MOSTRAR NULOS NO CRITICOS
        if nulls_sucursal > 0:
            print(f"Columna ['sucursal']: {nulls_sucursal} nulos -> Rellenados con 'Sin asignar'")
        if nulls_fecha > 0:
            print(f"Columna ['fecha_ingreso']: {nulls_fecha} nulos -> Rellenados con 'No fecha'")  
        else:
            print(f'Sin nulos que rellenar.')

        # --- FINAL 
        print(f'\nFilas después: {len(df)}')
        print('✓ Productos listos (sin nulos)')


        return df


#TODO: CONVERTIR FECHA A DATETIME

def convert_time(df, column, table_name):
    # --- CONVERTIR 
    df[column] = pd.to_datetime(df[column])
    print(f"✓ {table_name}: {column} convertida a datetime.")
    return df







