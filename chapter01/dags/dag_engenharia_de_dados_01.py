from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG (
    dag_id="carga_api_publica",
    schedule_interval="@once",
    start_date=datetime(2025, 7, 17),
)

get_data = DummyOperator(
    task_id="get_data",
    dag=dag
)

write_on_bronze  = DummyOperator(
    task_id="write_on_bronze",
    dag=dag
)

clean_data = DummyOperator(
    task_id="clean_data",
    dag=dag
)

transform_data = DummyOperator(
    task_id="transform_data",
    dag=dag
)

enrich_data = DummyOperator(
    task_id="enrich_data",
    dag=dag
)

write_on_silver = DummyOperator (
    task_id="write_on_silver",
    dag=dag
)

get_data >> write_on_bronze 
write_on_bronze >> clean_data
clean_data >> [transform_data, enrich_data] >> write_on_silver
