from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "Rafael Lima",
    "retries": 1,
    "retry_delay": 0
}


# declare dag
@dag(
    dag_id="load-s3-minio-snowflake",
    start_date=datetime(2022, 11, 25),
    max_active_runs=1,
    schedule_interval=timedelta(hours=24),
    default_args=default_args,
    catchup=False,
    tags=['development', 'elt', 'astrosdk', 's3', 'snowflake']
)

def etl_data():

    # init
    start = DummyOperator(task_id="init")

    def run_spark_job():
        pass

    def run_dbt_task():
        # Logic for running dbt transformations in Dremio
        pass
    def load_into_snowflake():
        # Logic for loading the gold layer into Snowflake
        pass

    # finish task
    finish_data_load = DummyOperator(task_id="finish")

    # define sequence
    start >> raw_load >> spark_task >> dbt_task >> snowflake_task

dag = etl_data()