#! /bin/bash

sudo systemctl stop airflow-webserver
sudo systemctl stop airflow-scheduler

sudo rm -rf airflow
dropdb airflow
createdb --encoding=UTF8 --owner=airflow airflow

mkdir -p airflow/dags

cp ../Airflow/modified_files/airflow.cfg airflow/
airflow initdb

cp tutorial1.py airflow/dags/airflow_DAG_tutorial1.py
cp x_email.py airflow/dags/airflow_DAG_x_email.py

sudo systemctl restart airflow-webserver
sudo systemctl restart airflow-scheduler
