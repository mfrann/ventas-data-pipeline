from extract import extract_csv
from transform import (
    del_duplicates,
    identify_nulls,
    clean_ventas,
    clean_productos,
    clean_clientes,
    clean_vendedores,
    convert_time,
    validate_integrity,
    enrich_ventas,
    business_metrics
)

def run_etl():
    #================================================#
    #            TODO: EXTRAER (EXTRACT)             #
    #================================================#

    df_ventas, df_productos, df_clientes, df_vendedores = extract_csv()

    #================================================#
    #          TODO: TRANSFORMAR (TRANSFORM)         #
    #================================================#

    #================================================#
    #                A.VALIDACION                    #
    #================================================#
    print("\nVALIDANDO IDs")
    ventas_ok, ventas_error = validate_integrity(
        df_ventas,
        df_productos,
        df_clientes,
        df_vendedores
    )

    print(f'Ventas validad: {len(ventas_ok)}')
    print(f'Ventas invalidad: {len(ventas_error)}')
    
    print("\n✓ VALIDACION COMPLETADA")
    
    print("===" * 30)
    #================================================#
    #                B.LIMPIEZA                      #
    #================================================#
    print("\nELIMINANDO DUPLICADOS")
    df_ventas = del_duplicates(df_ventas, 'VENTAS')
    df_productos = del_duplicates(df_productos, 'PRODUCTOS')
    df_clientes = del_duplicates(df_clientes, 'CLIENTES')
    df_vendedores = del_duplicates(df_vendedores, 'VENDEDORES')

    print("===" * 30)

    print("\nIDENTIFICANDO NULOS")
    identify_nulls(df_ventas, 'VENTAS')
    identify_nulls(df_productos, 'PRODUCTOS')
    identify_nulls(df_clientes, 'CLIENTES')
    identify_nulls(df_vendedores, 'VENDEDORES')

    print("===" * 30)

    print("\nELIMINANDO NULOS")
    clean_ventas(df_ventas, 'VENTAS')
    clean_productos(df_productos, 'PRODUCTOS')
    clean_clientes(df_clientes, 'CLIENTES')
    clean_vendedores(df_vendedores, 'VENDEDORES')

    print("\n✓ LIMPIEZA COMPLETADA")

    print("===" * 30)
    #================================================#
    #                C.TIPO DE DATOS                 #
    #================================================#

    print("\nCAMBIANDO DATOS A DATETIME")

    df_ventas = convert_time(df_ventas, 'fecha', 'VENTAS')
    df_clientes = convert_time(df_clientes, 'fecha_registro', 'CLIENTES')
    df_vendedores = convert_time(df_vendedores, 'fecha_ingreso', 'VENDEDORES')

    print("\n✓ TRANSFORMACIÓN COMPLETADA")

    print("===" * 30)
    #================================================#
    #                D.ENRIQUECER DATOS              #
    #================================================#
    
    print("\nAGREGANDO NUEVAS COLUMNAS")
    
    df_ventas = enrich_ventas(df_ventas, df_productos)
    print("✓ Ventas enriquecidas")
    print(df_ventas.head())

    print("\n✓ COLUMNAS AGREGADAS")


    print("===" * 30)
    #================================================#
    #          E.AGREGACIONES Y METRICAS             #
    #================================================#
    print("\nRESPONDIENDO PREGUNTAS DE NEGOCIO")   
    df_ventas = business_metrics(df_ventas, df_vendedores)

    print("\n✓ PREGUNTAS CONTESTADAS")
    
    return df_ventas, df_productos, df_clientes, df_vendedores

if __name__ == "__main__":
    run_etl()