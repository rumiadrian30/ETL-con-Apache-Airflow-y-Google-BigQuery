from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 7, 1),
    'retries': 1
}

dag = DAG(
    dag_id='etl_sri_vehiculos',
    description='ETL de Vehículos del SRI con GCS y BigQuery',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

