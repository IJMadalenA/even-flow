from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from app_tasks.views.my_function import myfunction
from datetime import (
    datetime,
    timedelta
)
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'IJMadalenA',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id="6.2-monitoring",
        description="Monitoreando nuestro DAG",
        schedule_interval="@daily",
        start_date=days_ago(7),
        end_date=datetime(2022, 6, 1),
        default_args=default_args,
        max_active_runs=1,
        tags=[
            "bash_operators",
            "course_dags"
        ],
) as dag:
    t1 = BashOperator(
        task_id="task1",
        bash_command="sleep 5 && echo 'Primera tarea!'",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        depends_on_past=False
    )
    t2 = BashOperator(
        task_id="task2",
        bash_command="sleep 3 && echo 'Segunda tarea!'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True
    )
    t3 = BashOperator(
        task_id="task3",
        bash_command="sleep 2 && echo 'Tercera tarea!'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALWAYS,
        depends_on_past=True
    )
    t4 = PythonOperator(
        task_id="task4",
        python_callable=myfunction,
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True
    )
    t5 = BashOperator(
        task_id="task5",
        bash_command="sleep 2 && echo 'Cuarta tarea!'",
        retries=2,
        retry_delay=5,
        depends_on_past=True
    )

    t1 >> t2 >> t3 >> t4 >> t5
