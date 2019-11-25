#! /bin/bash

# Downloading Airflow config repository
git clone https://github.com/Plokoon1987/Airflow.git

# Running Script
./Airflow/init.sh

# Removing Repository
rm -rf Airflow
