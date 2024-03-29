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

#dag = DAG('tutorial1', default_args=default_args, schedule_interval=timedelta(hours=3))
#dag = DAG('tutorial1', default_args=default_args, schedule_interval='@hourly')
dag = DAG('tutorial1', default_args=default_args, schedule_interval='*/5 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='date_to_file',
    bash_command='date >> ~/study/aflow/froylord.txt',
    dag=dag)

#t2 = BashOperator(
#    task_id='sleep',
#    bash_command='sleep 5',
#    retries=3,
#    dag=dag)
#
#templated_command = """
#    {% for i in range(5) %}
#        echo "{{ ds }}"
#        echo "{{ macros.ds_add(ds, 7)}}"
#        echo "{{ params.my_param }}"
#    {% endfor %}
#"""
#
#t3 = BashOperator(
#    task_id='templated',
#    bash_command=templated_command,
#    params={'my_param': 'Parameter I passed in'},
#    dag=dag)

t2.set_upstream(t1)
#t3.set_upstream(t1)
