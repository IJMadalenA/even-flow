from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import (
    datetime,
    timedelta
)

default_args = {
    'owner': 'data_science',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id="externalTaskSensor-7.1",
        description="DAG principal",
        schedule_interval="@daily",
        start_date=datetime(2022, 5, 1),
        end_date=datetime(2022, 8, 1),
        default_args=default_args,
        tags=[
            "bash_operators",
            "custom_dags"
        ],
) as dag:

    t1 = BashOperator(
        task_id="tarea1",
        bash_command="sleep 10 && echo 'DAG finalizado!'",
        depends_on_past=True
    )

    t1
