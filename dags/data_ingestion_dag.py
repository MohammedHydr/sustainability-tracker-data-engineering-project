from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.crawling.api_ingestion import fetch_api_data

with DAG('data_ingestion', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    fetch_data = PythonOperator(
        task_id='fetch_api_data',
        python_callable=fetch_api_data
    )
