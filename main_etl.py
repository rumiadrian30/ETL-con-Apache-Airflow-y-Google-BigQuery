import os
from dotenv import load_dotenv
from scripts.extract import extraer_csv_desde_gcs
from scripts.transform_dimensiones import transformar_dim_vehiculo, transformar_dim_tiempo,transformar_dim_geografia,transformar_dim_propietario
from scripts.transform_hechos import transform_hechos
from scripts.load_bigquery import cargar_a_bigquery

load_dotenv()
clave = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
bucket = os.getenv("BUCKET_NAME")
blob = os.getenv("BLOB_PATH")
project = os.getenv("PROJECT_ID")
dataset = os.getenv("DATASET_ID")

# 1. Extraer
df = extraer_csv_desde_gcs(bucket, blob, dataset, clave)

# 2. Transformar
dim_vehiculo = transformar_dim_vehiculo(df)
dim_tiempo = transformar_dim_tiempo(df)
dim_geografia = transformar_dim_geografia(df)
dim_propietario_transicion = transformar_dim_propietario(df)
# ...

# 3. Hechos
fact_matriculas = transform_hechos(df, dim_vehiculo, dim_geografia, dim_propietario_transicion, dim_tiempo)

# 4. Cargar
cargar_a_bigquery(dim_vehiculo, f"{project}.{dataset}.dim_vehiculo", clave)
cargar_a_bigquery(fact_matriculas, f"{project}.{dataset}.fact_matriculas", clave)
