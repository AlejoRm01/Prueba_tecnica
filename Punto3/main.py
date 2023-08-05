import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

ruta = 'FILE.xls'
# Cargar los datos desde los archivos de Excel
marcas_df = pd.read_excel(ruta, sheet_name='MARCAS')
lineas_df = pd.read_excel(ruta, sheet_name='LINEAS')
colores_df = pd.read_excel(ruta, sheet_name='COLORES')

def consultar_marca():
    while True:
        marca = input("Ingrese el nombre de la marca que desea consultar: ")
        marca_info = marcas_df[marcas_df['DESCRIPCION'] == marca]

        if not marca_info.empty:
            return marca_info.iloc[0]['CODIGO']
        else:
            print("La marca no existe. Por favor, intente nuevamente.")

def main():
    try:
        marca_codigo = consultar_marca()
        marca_info = marcas_df[marcas_df['CODIGO'] == marca_codigo].iloc[0]['DESCRIPCION']

        marca_lineas = lineas_df[lineas_df['CODIGO MARCA'] == marca_codigo]
        marca_colores = colores_df[colores_df['CODIGO'].isin(marca_lineas['CODIGO LINEA'])]

        # Crear un nuevo DataFrame con la información requerida
        result_df = marca_lineas.merge(marca_colores, left_on='CODIGO LINEA', right_on='CODIGO')
        result_df = result_df[['DESCRIPCION_x', 'DESCRIPCION_y']]
        result_df.columns = ['Descripcion Linea', 'Color']

        print("Información de la Marca Consultada:")
        print(f"Marca: {marca_info}")
        print(result_df)

        # Generar un archivo Excel
        wb = Workbook()
        ws = wb.active
        ws.append(["Marca:", marca_info])
        ws.append([])  # Espacio en blanco
        for row in dataframe_to_rows(result_df, index=False, header=True):
            ws.append(row)

        excel_file_path = 'marca_consultada.xlsx'
        wb.save(excel_file_path)

        # Obtener la ruta absoluta del archivo guardado
        absolute_path = os.path.abspath(excel_file_path)

        print("\nProceso completado exitosamente.")
        print(f"El archivo Excel ha sido guardado en: {absolute_path}")


    except Exception as e:
        print("Ha ocurrido un error:", e)

if __name__ == "__main__":
    main()