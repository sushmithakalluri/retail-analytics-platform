import os
import sys

from pyspark.sql import SparkSession

sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING


spark = SparkSession.builder \
    .appName("Retail Analytics - Join Orders and Customers") \
    .getOrCreate()


orders_path = os.path.join(
    DATA_PATH,
    CSV_TABLE_MAPPING["orders"]
)

customers_path = os.path.join(
    DATA_PATH,
    CSV_TABLE_MAPPING["customers"]
)


orders_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(orders_path)


customers_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(customers_path)


orders_with_customer_df = orders_df.join(
    customers_df,
    on="customer_id",
    how="inner"
)


orders_with_customer_df.select(
    "order_id",
    "customer_id",
    "customer_city",
    "customer_state",
    "order_status"
).show(20)


print("Joined rows:")
print(orders_with_customer_df.count())


spark.stop()