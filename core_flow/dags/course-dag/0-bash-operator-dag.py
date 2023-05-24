from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        dag_id="bash-operator-dag",
        description="Descripción del BashOperator DAG.",
        start_date=datetime(2023, 1, 1),
        tags=["bash_operators", "custom_dags"],
) as dag:
    t1 = BashOperator(
        task_id="Hello-with-bash",
        bash_command="echo 'Hello.'"
    )

    t1
