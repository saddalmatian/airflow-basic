from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from pandas import json_normalize
import json


def processing_user_extracted(ti):
    users = ti.xcom_pull(task_ids=['extracting_user'])
    processed_user = json_normalize(
        {
            'PK': users[0]['PK'],
            'SK': users[0]['SK'],
            'Type': users[0]['Type'],
            'Username': users[0]['Username'],
            'CreatedAt': users[0]['CreatedAt'],
        }
    )
    processed_user.to_csv('test.csv', index=None, header=False)


with DAG(
    'my_dag',
    description='My simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 12),
    catchup=False,
    tags=['example'],
) as dag:

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint='user/GiangHoaTran'
    )

    extracting_user = SimpleHttpOperator(
        task_id='extracting_user',
        http_conn_id='user_api',
        endpoint='user/GiangHoaTran',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    processing_user = PythonOperator(
        task_id='processing_user',
        python_callable=processing_user_extracted
    )

    is_api_available >> extracting_user >> processing_user
