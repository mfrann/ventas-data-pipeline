#================================================#
#          TAREA 2: TRANSFORMAR (TRANSFORM)      #
#================================================#

# === LIBRERIAS === #
import pandas as pd


#================================================#
#                A.VALIDACION                    #
#================================================#
# TODO: Revisar si existen los ID

def validate_integrity(df_ventas, df_productos, df_clientes, df_vendedores):
        products_id = set(df_productos['producto_id'])
        clientes_id = set(df_clientes['cliente_id'])
        vendedores_id = set(df_vendedores['vendedor_id'])

        #Validar si IDs estan en VENTAS.CSV

        mask_valid = (
            df_ventas['producto_id'].isin(products_id)&
            df_ventas['cliente_id'].isin(clientes_id)&
            df_ventas['vendedor_id'].isin(vendedores_id)
        )

        ventas_validas = df_ventas[mask_valid].copy()
        ventas_invalidas = df_ventas[~mask_valid].copy()

        return ventas_validas, ventas_invalidas


#================================================#
#                B.LIMPIEZA                      #
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

#================================================#
#                C.TIPO DE DATOS                 #
#================================================#
#TODO: CONVERTIR FECHA A DATETIME

def convert_time(df, column, table_name):
    # --- CONVERTIR 
    df[column] = pd.to_datetime(df[column])
    print(f"✓ {table_name}: {column} convertida a datetime.")
    return df




#================================================#
#                D.ENRIQUECER DATOS              #
#================================================#
#TODO: AGREGAR NUEVAS COLUMNAS A VENTAS.CSV

def enrich_ventas(df_ventas, df_productos):
     
    # --- Creamos variable y lo unimos con las columnas seleccionadas de otro archivo **con merge()**
    ventas = df_ventas.merge(
        df_productos[['producto_id', 'costo']],
        on='producto_id',
        how='left'
    )

    # ---METRICAS FINANCIERAS
    ventas['total_ventas'] = ventas['cantidad'] * ventas['precio']  #HACEMOS OPERACIONES TOTAL VENTAS = CANTIDAD * PRECIO
    ventas['costo_total'] = ventas['cantidad'] * ventas['costo'] #COSTO TOTAL = CANTIDAD * COSTO
    ventas['margen'] = ventas['total_ventas'] - ventas['costo_total'] #MARGEN = TOTAL VENTAS - COSTO TOTAL


    # ---VARIABLES TEMPORALES
    ventas['año'] = ventas['fecha'].dt.year #SELECCIONA AÑO
    ventas['mes'] = ventas['fecha'].dt.month #SELECCIONA MES
    ventas['mes_nombre'] = ventas['fecha'].dt.month_name() #SELECCIONA NOMBRE DEL MES

    return ventas


#================================================#
#          E.AGREGACIONES Y METRICAS             #
#================================================#
'''
#TODO: GENERAR TABLAS DE RESULTADOS LISTAS PARA REPORTE, DASHBOARD, SQL
#RESPONDER PREGUNTAS DE NEGOCIO
'''

def business_metrics(df, dfv):
    # ? CUANTO SE VENDE CADA MES ?

    print("\nCUANTO SE VENDE CADA MES?")

    ventas_por_month = df.groupby([
         df['fecha'].dt.year.rename('year'), 
         df['fecha'].dt.month.rename('month'),
         df['fecha'].dt.month_name().rename('month_name')

    ])['total_ventas'].sum().reset_index()

    print(ventas_por_month)
    print("===" * 30)


    # ? QUE PRODUCTOS GENERA MAS DINERO ?
    print("\nQUE PRODUCTOS GENERA MAS DINERO?")

    ventas_por_product = df.groupby('producto_id')[['total_ventas', 'margen']].sum().reset_index().sort_values(by='total_ventas', ascending=False)
    print(ventas_por_product)
    print("===" * 30)


    # ? QUIENES SON LOS CLIENTES MAS VALIOSOS ?
    print("\nQUIENES SON LOS CLIENTES MAS VALIOSOS?")

    ventas_por_cliente = df.groupby('cliente_id')[['total_ventas', 'cantidad']].sum().reset_index().sort_values(by='total_ventas', ascending=False)
    print(ventas_por_cliente)
    print("===" * 30)
    '''

    # ? QUE VENDEDOR VENDE MAS DINERO ? cantidad x precio
    # ? QUIEN VENDE MAS UNIDADES ? cantidad
    # ? CUANTAS VENTAS HIZO CADA VENDEDOR ? 
    # ? EN QUE SUCURSAL RINDEN MEJOR ? 
    
    '''
    
    print("\nPERFORMANCE DE VENDEDORES")

    # * --- AGREGAR METRICAS POR VENDEDOR Y AGRUPAR
    ventas_vendedor = df.groupby('vendedor_id').agg(
         total_ventas=('total_ventas', 'sum'),
         unidades_vendidos =('cantidad', 'sum'),
         num_ventas =('vendedor_id', 'count')
    ).reset_index()


    # * --- JOIN DE VENTAS.CSV CON VENDEDORES.CSV 
    ventas_vendedor = ventas_vendedor.merge(
         dfv[['vendedor_id', 'nombre', 'sucursal']],
         on='vendedor_id',
         how='left'
    )

    # * --- METRICA DERIVADA: TICKET 
    ventas_vendedor['ticket_promedio'] = (
         ventas_vendedor['total_ventas'] / ventas_vendedor['num_ventas']
    ).round(2)


    # * --- ORDENAR POR PERFOMANCE
    ventas_vendedor = ventas_vendedor.sort_values(
         by='total_ventas',
         ascending=False
    )

    print(ventas_vendedor)
    
    return ventas_por_month, ventas_por_product, ventas_por_cliente, ventas_vendedor

