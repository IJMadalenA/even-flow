from airflow.hooks.base import BaseHook

# https://airflow.apache.org/docs/apache-airflow-providers-slack/stable/_api/airflow/providers/slack/operators/slack/index.html#airflow.providers.slack.operators.slack.SlackAPIOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator


SLACK_CONN_ID = 'slack'


def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    slack_msg = """
            :red_circle: Task Failed. 
            *Task*: {task}  
            *Dag*: {dag} 
            *Execution Time*: {exec_date}  
            *Log Url*: {log_url} 
            """.format(
            task=context.get('task_instance').task_id,
            dag=context.get('task_instance').dag_id,
            ti=context.get('task_instance'),
            exec_date=context.get('execution_date'),
            log_url=context.get('task_instance').log_url,
            )
    failed_alert = SlackWebhookOperator(
            task_id='slack_test',
            http_conn_id='slack',
            webhook_token=slack_webhook_token,
            message=slack_msg,
            username='airflow')
    return failed_alert.execute(context=context)
