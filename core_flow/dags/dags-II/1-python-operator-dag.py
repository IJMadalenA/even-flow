from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(
        dag_id="python-operator.",
        description="DAG utilizando el Python Operator.",
        schedule_interval="@once",
        start_date=datetime(2023, 1, 1)
) as dag:
    t1 = PythonOperator(
        task_id="hello-with-python",
        python_callable=print_hello
    )

    t1
