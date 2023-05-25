from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import (
    datetime,
    timedelta
)
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'IJMadalenA',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id="7.3-filesensor",
        description="FileSensor",
        schedule_interval="@daily",
        start_date=days_ago(7),
        end_date=datetime(2022, 8, 1),
        max_active_runs=1,
        default_args=default_args,
        tags=[
            "bash_operators",
            "file_sensor",
            "course_dags",
        ],
) as dag:
    t1 = BashOperator(
        task_id="creating_file",
        bash_command="sleep 10 && touch /tmp/file.txt"
    )

    t2 = FileSensor(
        task_id="waiting_file",
        filepath="/tmp/file.txt"
    )

    t3 = BashOperator(
        task_id="end_task",
        bash_command="echo 'El fichero ha llegado'"
    )

    t1 >> t2 >> t3
