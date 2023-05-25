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

# https://jinja.palletsprojects.com/en/3.1.x/templates/
templated_command = """
    {% for file in params.filenames %}
        echo "{{ ds }}"
        echo "{{ file }}"
    {% endfor %}
"""

with DAG(
    default_args=default_args,
    dag_id="8-Templating",
    description="Example using templates.",
    schedule_interval="@daily",
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2025, 1, 1),
    tags=["bash_operators", "custom_dags"],
    max_active_runs=1,
) as dag:

    t1 = BashOperator(
        task_id="Tarea_1.",
        bash_command=templated_command,
        params={
            "filenames": ["file1.txt", "file2.txt"]
        },
        depends_on_past=True,
    )

    t1
