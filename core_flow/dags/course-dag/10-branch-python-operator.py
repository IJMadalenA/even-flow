from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import (
    datetime,
    timedelta,
    date
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
        dag_id="10-branching",
        description="try branching a dag.",
        schedule_interval="@daily",
        default_args=default_args,
        max_active_runs=1,
        tags=[
            "python_operators",
            "course_dags"
        ],
) as dag:

    branching = BranchPythonOperator(
        task_id="branch_operator"
    )

    finish_14 = BashOperator(
        task_id="finish_10",
        bash_command="echo 'Running {{ds}}'"
    )
    start_15 = BashOperator(
        task_id="start_15",
        bash_command="echo 'Running {{ds}}'"
    )
