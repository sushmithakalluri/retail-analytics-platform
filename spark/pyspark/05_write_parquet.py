import os
import sys

from pyspark.sql import SparkSession

sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING

spark = SparkSession.builder \
    .appName("Retail Analytics - Write Parquet") \
    .getOrCreate()


def read_csv(table_name):
    path = os.path.join(DATA_PATH, CSV_TABLE_MAPPING[table_name])

    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(path)


orders_df = read_csv("orders")

output_path = "data/parquet/orders"

orders_df.write \
    .mode("overwrite") \
    .parquet(output_path)

print("Parquet file created successfully!")

spark.stop()