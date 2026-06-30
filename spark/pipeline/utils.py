import os
import sys
from pyspark.sql import SparkSession

sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING


def create_spark_session(app_name: str) -> SparkSession:
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()


def read_csv(spark: SparkSession, table_name: str):
    file_name = CSV_TABLE_MAPPING[table_name]
    file_path = os.path.join(DATA_PATH, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")

    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)


def write_parquet(df, output_path: str):
    df.write \
        .mode("overwrite") \
        .parquet(output_path)


def validate_not_empty(df, dataset_name: str):
    row_count = df.count()

    if row_count == 0:
        raise ValueError(f"Validation failed: {dataset_name} has 0 rows.")

    print(f"Validation passed: {dataset_name} has {row_count} rows.")