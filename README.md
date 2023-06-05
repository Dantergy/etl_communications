# Moabits Take Home Challenge
En este proyecto se implemento un ETL en Python que extrae los datos desde un archivo .zip, los transforma y finalmente son cargados en un Data Warehouse en PostgreSQL (Para el proyecto se eligio PostgreSQL como warehouse para simplificar la implementación, sin embargo lo más adecuado sería trabajar con Redshift o BigQuery).

Se realiza un Dashboard en PowerBi con información relevante en base a los datos, en el directorio `dashboard/` se encuentra un archivo `main_dashboard.pdf`, como también el archivo para cargarlo en PowerBi. 

## Data Warehouse
[![Diagram](https://github.com/Dantergy/etl_communications/blob/main/Star%20model.png?raw=true "Diagram")](https://github.com/Dantergy/etl_communications/blob/main/Star%20model.png?raw=true "Diagram")

## Requisitos
- Python 3.6+
- pip
- PostgreSQL

## Configuración
1. Crear un entorno virtual venv y activarlo:
`python3 -m venv venv`
`source venv/bin/activate`

1. Instalar las dependencias desde el archivo requirements.txt
`pip install -r requirements.txt`

1. Tener una base de datos PostgreSQL en local disponible con la siguiente configuracion: `database="moabits", user="postgres", password="password", host="localhost", port="5432"` En caso de ya contar con una BD, modificar las variables de conexión.

1. En el archivo `script.sql` se encuentra el Query para la creación de las tablas

## Ejecución

Para ejecutar el proceso ETL basta con ejecutar el archivo `main.py`.
Una vez finalizada la ejecución, los datos ya deberían estar cargados en la Base de datos.





