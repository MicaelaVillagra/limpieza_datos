import pandas as pd  # Importamos la librería pandas, que nos ayudará a manejar datos

# Cargar el dataset original
def cargar_datos():
    # Leemos el archivo CSV que contiene los datos originales
    return pd.read_csv('../data/datos_originales.csv')

# Eliminar filas duplicadas
def eliminar_duplicados(df):
    # Eliminamos las filas que son duplicadas en el DataFrame
    return df.drop_duplicates()

# Reemplazar valores nulos en la columna 'Salario' con la mediana
def reemplazar_nulos_salario(df):
    # Calculamos la mediana de la columna 'Salario'
    mediana_salario = df['Salario'].median()
    # Reemplazamos los valores nulos en la columna 'Salario' con la mediana
    df['Salario'].fillna(mediana_salario, inplace=True)
    return df

# Filtrar personas mayores de 30 años
def filtrar_mayores_30(df):
    # Filtramos las filas donde la edad sea mayor a 30 años
    return df[df['Edad'] > 30]

# Guardar los datos limpios en un nuevo archivo CSV
def guardar_datos(df):
    # Guardamos el DataFrame limpio en un nuevo archivo CSV llamado 'datos_limpios.csv'
    df.to_csv('../data/datos_limpios.csv', index=False)

# Función principal para ejecutar el proceso
def limpiar_datos():
    # Cargamos los datos originales
    df = cargar_datos()
    
    # Eliminamos filas duplicadas
    df = eliminar_duplicados(df)
    
    # Reemplazamos valores nulos en la columna 'Salario'
    df = reemplazar_nulos_salario(df)
    
    # Filtramos personas mayores de 30 años
    df = filtrar_mayores_30(df)
    
    # Guardamos los datos limpios en un nuevo archivo
    guardar_datos(df)
    
    # Imprimimos un mensaje indicando que los datos fueron limpiados y guardados
    print("Datos limpiados y guardados en 'datos_limpios.csv'.")

# Ejecutar la limpieza de datos
if __name__ == "__main__":
    limpiar_datos()
