from airflow import DAG
from airflow.operators.bash import BashOperator
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
        dag_id="bash-operator-dag",
        description="Descripción del BashOperator DAG.",
        start_date=datetime(2023, 1, 1),
        default_args=default_args,
        tags=[
            "bash_operators",
            "course_dags"
        ],
) as dag:
    t1 = BashOperator(
        task_id="Hello-with-bash",
        bash_command="echo 'Hello.'"
    )

    t1
