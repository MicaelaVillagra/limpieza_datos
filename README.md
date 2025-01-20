# Limpieza de Datos con Python

Este proyecto realiza una limpieza básica de un dataset ficticio con los siguientes pasos:
1. Eliminación de filas duplicadas.
2. Reemplazo de valores nulos en la columna "Salario" con la mediana.
3. Filtrado de personas mayores de 30 años.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
- `data/`: Contiene los datasets originales y limpios.
  - `datos_originales.csv`: El dataset original con datos ficticios.
  - `datos_limpios.csv`: El dataset limpio generado después de procesar los datos.
- `src/`: Contiene el script para limpiar los datos.
  - `limpieza_datos.py`: Script de Python que realiza la limpieza de los datos.
- `README.md`: Descripción del proyecto (este archivo).
- `requirements.txt`: Dependencias necesarias para ejecutar el script.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener las siguientes dependencias instaladas:

- **pandas**: Para manipulación de datos.
- **numpy**: Para operaciones numéricas.

Puedes instalar todas las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
