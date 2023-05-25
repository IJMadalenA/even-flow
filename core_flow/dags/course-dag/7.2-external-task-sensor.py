from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
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
        dag_id="externalTaskSensor-7.2",
        description="DAG Secundario",
        schedule_interval="@daily",
        start_date=datetime(2022, 5, 1),
        end_date=datetime(2022, 8, 1),
        max_active_runs=1,
        default_args=default_args,
        tags=[
            "bash_operators",
            "external_task_sensor",
            "custom_dags",
        ],
) as dag:

    t1 = ExternalTaskSensor(
        task_id="waiting_dag",
        external_dag_id="7.1-externalTaskSensor",
        external_task_id="tarea1",
        poke_interval=10
    )

    t2 = BashOperator(
        task_id="tarea2",
        bash_command="sleep 10 && echo 'DAG 2 finalizado!'",
        depends_on_past=True
    )

    t1 >> t2
