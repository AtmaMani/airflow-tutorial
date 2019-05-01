# Airflow Tutorial notes
 - Tutorial github repo: https://github.com/trallard/airflow-tutorial
 - tutorial website: https://airflow-tutorial.readthedocs.io/en/latest/airflow-intro.html

## Set up MySQL DB

  - `CREATE DATABASE airflowdb CHARACTER SET utf8 COLLATE utf8_unicode_ci;` to create DB
  - `CREATE USER 'airflow'@'localhost' IDENTIFIED BY 'python2019';` to create a `airflow` user.
  - grant the new user all privileges `GRANT ALL PRIVILEGES ON airflowdb.* TO 'airflow'@'localhost';`
  - then for some reason `flush privileges;`
  - create another db `CREATE DATABASE airflow CHARACTER SET utf8 COLLATE utf8_unicode_ci;`
 
The `airflow` user is a global user that can work on both the databases.

## Setting up airflow
 
 - create an env var for airlfow home `export AIRFLOW_HOME=/Users/atma6951/Documents/code/pycon2019/airflow-tutorial`
 - install airflow `pip install apache-airflow`
 - initialize airflow db `airflow initdb`. This db contains the tasks, statuses of tasks etc.

