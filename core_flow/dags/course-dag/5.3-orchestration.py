from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import (
    datetime,
    timedelta
)

default_args = {
    'owner': 'IJMadalenA',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id="5.3-orchestration",
        description="Probando la orquestacion",
        schedule_interval="@monthly",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 8, 1),
        default_args=default_args,
        tags=[
            "Empty_operators",
            "custom_dags"
        ],
) as dag:

    t1 = EmptyOperator(
        task_id="task1"
    )
    t2 = EmptyOperator(
        task_id="task2"
    )
    t3 = EmptyOperator(
        task_id="task3"
    )
    t4 = EmptyOperator(
        task_id="task4"
    )

    t1 >> t2 >> t3 >> t4
