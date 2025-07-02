from google.cloud import storage
import pandas as pd

def extraer_csv_desde_gcs(bucket_name, blob_path, archivo_local1, credenciales):
    """
    Descarga un CSV desde Google Cloud Storage y lo carga en un DataFrame de pandas.

    Args:
        bucket_name (str): Nombre del bucket en GCS.
        blob_path (str): Ruta completa dentro del bucket al archivo CSV.
        credenciales (str): Ruta al archivo JSON de credenciales.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados del CSV.
    """
    client = storage.Client.from_service_account_json(credenciales)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)

    # Descargar el archivo CSV localmente
    archivo_local = archivo_local1
    blob.download_to_filename(archivo_local)
    print(f"Archivo descargado en {archivo_local}")

    # Cargar en DataFrame
    df = pd.read_csv(archivo_local)
    return df

if __name__ == "__main__":
    bucket = "sri-vehiculos-bucket"
    ruta_blob = "vehiculos/SRI_Vehiculos_Nuevos_Unido.csv"
    credenciales = "dags/keys/level-poetry-464708-f2-3bc7d9da78c6.json"  # Ajusta esta ruta a tu archivo de credenciales
    archivo_local1 = "data/SRI_Vehiculos_Nuevos_Unido.csv"
    
    df_vehiculos = extraer_csv_desde_gcs(bucket, ruta_blob, archivo_local1, credenciales)
    print(df_vehiculos.head())
