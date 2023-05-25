from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from datetime import (
    datetime,
    timedelta
)

default_args = {
    "owner": "IJMadalenA",
    "depends_on_past": False,
    "email": [],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        default_args=default_args,
        dag_id="BashOperator.",
        description="Primer DAG hecho con Bash.",
        schedule_interval="@daily",
        start_date=days_ago(7),
        tags=[
            "bash_operators",
            "custom_dags"
        ],
        max_active_runs=1,
) as dag:
    start = BashOperator(
        task_id="start_msg",
        bash_command="echo DAG started.",
    )
    t1 = BashOperator(
        task_id="tarea_1",
        bash_command="echo Primer DAG."
    )
    end = BashOperator(
        task_id="end_msg",
        bash_command=" DAG end."
    )
