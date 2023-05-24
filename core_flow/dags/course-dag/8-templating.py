from datetime import (
    datetime,
    timedelta
)
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "IJMadalenA",
    "depends_on_past": False,
    "email": [],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

templated_command = """

"""

with DAG(
    default_args=default_args,
    dag_id="Templating",
    description="Example using templates.",
    schedule_interval="@daily",
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2025, 1, 1),
    tags=["python_operators", "custom_dags"],
    max_active_runs=1,
) as dag:

    t1 = BashOperator(
        task_id="Tarea_1.",
        bash_command=templated_command,
        depends_on_past=True,
    )

    t1
