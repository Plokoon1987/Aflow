"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 20, hour=16, minute=0, second=0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('x_email', default_args=default_args, schedule_interval='*/5 * * * *')
#dag = DAG('tutorial1', default_args=default_args, schedule_interval='@hourly')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date_1',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='send_email',
    bash_command='~/study/mail_me/mail_me.py from_email=froymoon2015@gmail.com from_email_pass=Saorita2014 to_email=malagacj@tcd.ie',
    dag=dag)

t2.set_upstream(t1)
