from airflow import DAG
from airflow.operators.python import PythonOperator
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


def print_hello():
    print("Print tercer DAG.")


with DAG(
        dag_id="3-dependencias",
        description="Nuestro primer DAG creando dependecias entre tareas",
        schedule_interval="@once",
        start_date=datetime(2022, 8, 1),
        default_args=default_args,
        tags=[
            "bash_operators",
            "python_operators",
            "custom_dags"
        ],
) as dag:

    t1 = PythonOperator(
        task_id="tarea1",
        python_callable=print_hello
    )
    t2 = BashOperator(
        task_id="tarea2",
        bash_command="echo 'tarea2'"
    )
    t3 = BashOperator(
        task_id="tarea3",
        bash_command="echo 'tarea3'"
    )
    t4 = BashOperator(
        task_id="tarea4",
        bash_command="echo 'tarea4'"
    )

    t1 >> t2 >> [t3, t4]
