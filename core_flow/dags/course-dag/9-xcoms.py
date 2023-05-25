from datetime import (
    datetime,
    timedelta
)
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from app_tasks.views.xcom_python_function import xcom_python

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
        dag_id="9-xcoms",
        description=" Try XComs.",
        schedule_interval="@once",
        start_date=days_ago(7),
        default_args=default_args,
        max_active_runs=1,
        tags=[
            "python_operators",
            "course_dags"
        ],
) as dag:
    t1 = BashOperator(
        task_id="task_1",
        bash_command="sleep 5 && echo $((3 * 8))",
    )
    t2 = BashOperator(
        task_id="task_2",
        bash_command="sleep 5 && echo {{ ti.xcom_pull(task_ids='task_1') }}",
    )
    t3 = PythonOperator(
        task_id="task_3",
        python_callable=xcom_python
    )

    t1 >> t2 >> t3
