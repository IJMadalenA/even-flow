from airflow import DAG
from airflow.operators.python import PythonOperator

from app_tasks.views.print_hello import fun_print_hello

from datetime import datetime


with DAG(
        dag_id="python-operator.",
        description="DAG utilizando el Python Operator.",
        schedule_interval="@once",
        start_date=datetime(2023, 1, 1)
) as dag:
    t1 = PythonOperator(
        task_id="hello-with-python",
        python_callable=fun_print_hello
    )

    t1
