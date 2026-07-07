from datetime import datetime, timedelta
import subprocess

from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.providers.standard.sensors.filesystem import FileSensor


PROJECT_ROOT = "/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform"


default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


def run_project_script(script_path: str):
    result = subprocess.run(
        ["python3", script_path],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)


with DAG(
    dag_id="retail_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["retail", "data-engineering"],
) as dag:

    # Task 1: Start marker
    start = EmptyOperator(
        task_id="start_pipeline"
    )

    # Task 2: Wait until source file exists
    wait_for_orders_file = FileSensor(
        task_id="wait_for_orders_file",
        filepath=(
            "/Users/sushmithakalluri/Documents/GitHub/"
            "retail-analytics-platform/data/raw/Brazilian dataset/"
            "olist_orders_dataset.csv"
        ),
        poke_interval=30,
        timeout=300,
        mode="reschedule",
    )

    # Task 3: Load raw CSV files into PostgreSQL Bronze
    @task(task_id="load_bronze")
    def load_bronze():
        run_project_script(
            "ingestion/python/load_bronze.py"
        )

    # Task 4: Run PySpark Bronze to Silver transformation
    @task(task_id="run_bronze_to_silver")
    def run_bronze_to_silver():
        run_project_script(
            "spark/pipeline/bronze_to_silver.py"
        )

    # Task 5: End marker
    end = EmptyOperator(
        task_id="end_pipeline"
    )

    # Define execution order
    start >> wait_for_orders_file >> load_bronze() >> run_bronze_to_silver() >> end