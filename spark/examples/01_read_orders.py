import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Allow Spark script to import config from ingestion/python
sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING


spark = SparkSession.builder \
    .appName("Retail Analytics - Read Orders") \
    .getOrCreate()


orders_file = CSV_TABLE_MAPPING["orders"]
orders_path = os.path.join(DATA_PATH, orders_file)

orders_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(orders_path)


print("Orders schema:")
orders_df.printSchema()

delivered_orders = orders_df.filter(
    col("order_status") == "delivered"
)

print("Delivered Orders:")
delivered_orders.show(10)

print("Total Delivered Orders:")
print(delivered_orders.count())

print("Total orders:")
print(orders_df.count())

spark.stop()