from dotenv import load_dotenv
import os

load_dotenv()
ruta_clave = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
bucket_name = os.getenv("BUCKET_NAME")
