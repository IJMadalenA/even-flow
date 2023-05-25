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
    dag_id="1-segundo_dag",
    description="descripción del proceso del dag.",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@weekly",
    tags=["empty_operators", "custom_dags"],
    default_args=default_args,

) as dag:
    t1 = EmptyOperator(
        task_id="dummy"
    )
