import pandas as pd
from google.cloud import bigquery
import os

# Cargar el cliente de BigQuery con la clave JSON
client = bigquery.Client()

# Ruta del archivo CSV generado por el script de clima
csv_path = "data/datos_clima_argentina.csv"

# Leer los datos del CSV
df = pd.read_csv(csv_path)

# Definir ID del dataset y tabla
project_id = "proyecto-clima-463015"
dataset_id = "clima_argentina"
table_id = "datos_diarios"
full_table_id = f"{project_id}.{dataset_id}.{table_id}"

# Configurar el esquema (opcional: BigQuery puede inferirlo)
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # reemplaza los datos cada vez
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)

# Cargar el archivo CSV a BigQuery
with open(csv_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, full_table_id, job_config=job_config)

job.result()  # Esperar a que termine

print(f"Datos cargados correctamente a {full_table_id}")
