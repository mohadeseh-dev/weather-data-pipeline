from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
from zoneinfo import ZoneInfo
from sys import path

path.append("/opt/airflow/source")

from extract import extract_weather
from load import load_weather


def extract_task():
    return extract_weather()


def load_task(**context):
    data = context["ti"].xcom_pull(task_ids="extract_weather")
    load_weather(data)


with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2026, 8, 16, tzinfo=ZoneInfo("Asia/Tehran")),
    schedule="0 0,12 * * *",
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract_weather",
        python_callable=extract_task,
    )

    load = PythonOperator(
        task_id="load_weather",
        python_callable=load_task,
    )

    extract >> load