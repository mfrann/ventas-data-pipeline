from extract import extract_csv
from transform import (
    del_duplicates,
    identify_nulls,
    clean_ventas,
    clean_productos,
    clean_clientes,
    clean_vendedores,
    convert_time
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
    #                A.LIMPIEZA                      #
    #================================================#
    print("\nELIMINANDO DUPLICADOS")
    df_ventas = del_duplicates(df_ventas, 'VENTAS')
    df_productos = del_duplicates(df_productos, 'PRODUCTOS')
    df_clientes = del_duplicates(df_clientes, 'CLIENTES')
    df_vendedores = del_duplicates(df_vendedores, 'VENDEDORES')

    print("\nIDENTIFICANDO NULOS")
    identify_nulls(df_ventas, 'VENTAS')
    identify_nulls(df_productos, 'PRODUCTOS')
    identify_nulls(df_clientes, 'CLIENTES')
    identify_nulls(df_vendedores, 'VENDEDORES')

    print("\n✓ LIMPIEZA COMPLETADA")
    #================================================#
    #                B.TIPO DE DATOS                 #
    #================================================#

    print("\nCAMBIANDO DATOS A DATETIME")

    df_ventas = convert_time(df_ventas, 'fecha', 'VENTAS')
    df_clientes = convert_time(df_clientes, 'fecha_registro', 'CLIENTES')
    df_vendedores = convert_time(df_vendedores, 'fecha_ingreso', 'VENDEDORES')

    print("\n✓ TRANSFORMACIÓN COMPLETADA")

    return df_ventas, df_productos, df_clientes, df_vendedores

if __name__ == "__main__":
    run_etl()