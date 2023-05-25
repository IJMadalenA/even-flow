from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
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


def myfunction():
    raise Exception


with DAG(
        dag_id="monitoring-6.1",
        description="Monitoreando nuestro DAG",
        schedule_interval="@daily",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 2, 1),
        tags=[
            "bash_operators",
            "custom_dags"
        ]
) as dag:
    t1 = BashOperator(
        task_id="tarea1",
        bash_command="sleep 2 && echo 'Primera tarea!'"
    )
    t2 = BashOperator(
        task_id="tarea2",
        bash_command="sleep 2 && echo 'Segunda tarea!"
    )
    t3 = BashOperator(
        task_id="tarea3",
        bash_command="sleep 2 && echo 'Tercera tarea!'"
    )
    t4 = PythonOperator(
        task_id="tarea4",
        python_callable=myfunction
    )
    t5 = BashOperator(
        task_id="tarea5",
        bash_command="sleep 2 && echo 'Cuarta tarea!'"
    )

    t1 >> t2 >> t3 >> t4 >> t5
