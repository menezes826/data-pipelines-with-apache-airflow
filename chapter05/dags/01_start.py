import airflow

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="01_start",
    start_date=datetime(2025, 7, 15),
    schedule_interval="@once",
) as dag:
    start = DummyOperator(task_id="start")

    fetch_sales = DummyOperator(task_id="fetch_sales")
    clean_sales = DummyOperator(task_id="clean_sales")

    fetch_weather = DummyOperator(task_id="fetch_weather")
    clean_weather = DummyOperator(task_id="clean_weather")

    join_datasets = DummyOperator(task_id="join_datasets")
    train_model = DummyOperator(task_id="train_model")
    deploy_model = DummyOperator(task_id="deploy_model")

    start >> [fetch_sales, fetch_weather]
    fetch_sales >> clean_sales
    fetch_weather >> clean_weather
    [clean_sales, clean_weather] >> join_datasets
    join_datasets >> train_model >> deploy_model
