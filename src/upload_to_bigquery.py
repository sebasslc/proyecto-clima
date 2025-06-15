import os
import pandas as pd
from google.cloud import bigquery

# Ruta al CSV generado (ajustar si cambia)
CSV_PATH = "data/datos_clima_argentina.csv"

# Configuración de BigQuery
PROJECT_ID = "proyecto-clima-463015"
DATASET_ID = "clima_dataset"
TABLE_ID = "clima_diario"

# Cargar el DataFrame
df = pd.read_csv(CSV_PATH)

# Inicializar cliente de BigQuery usando la variable de entorno
client = bigquery.Client()

# Definir el ID completo de la tabla
table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# Configuración de carga
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Reemplaza los datos
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV,
)

# Subir datos a BigQuery
with open(CSV_PATH, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

job.result()  # Espera a que termine

print(f"✅ Carga completada. {job.output_rows} filas subidas a {table_ref}.")
