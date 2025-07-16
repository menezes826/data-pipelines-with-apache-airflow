from urllib import request

import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

dag = DAG(
    dag_id="listing_4_13",
    start_date=datetime(2025, 7, 16),
    schedule_interval="15 16 * * *",
)


def _get_data(year, month, day, hour, output_path, **_):
    hour = str(int(hour) - 4)
    url = (
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    print(url)
    request.urlretrieve(url, output_path)


get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    op_kwargs={
        "year": "{{ execution_date.year }}",
        "month": "{{ execution_date.month }}",
        "day": "{{ execution_date.day }}",
        "hour": "{{ execution_date.hour }}",
        "output_path": "/usr/data/wikipageviews3.gz",
    },
    dag=dag,
)
