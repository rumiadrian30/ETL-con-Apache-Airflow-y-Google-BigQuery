from google.cloud import bigquery

def cargar_a_bigquery(df, tabla_id, credenciales):
    client = bigquery.Client.from_service_account_json(credenciales)
    job = client.load_table_from_dataframe(df, tabla_id)
    job.result()
    print(f"✅ Datos cargados en {tabla_id}")
