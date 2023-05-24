from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime


with DAG(
    dag_id="segundo_dag",
    description="descripción del proceso del dag.",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@weekly",
    tags=["empty_operators", "custom_dags"],

) as dag:
    t1 = EmptyOperator(task_id="dummy")
