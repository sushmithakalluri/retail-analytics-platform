import os
import sys

from pyspark.sql import SparkSession

sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING

spark = SparkSession.builder \
    .appName("Retail Analytics - Sales Dataset") \
    .getOrCreate()


def read_csv(table_name):
    path = os.path.join(DATA_PATH, CSV_TABLE_MAPPING[table_name])

    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(path)


orders_df = read_csv("orders")
customers_df = read_csv("customers")
order_items_df = read_csv("order_items")


sales_df = (
    orders_df
    .join(customers_df, on="customer_id", how="inner")
    .join(order_items_df, on="order_id", how="inner")
)


sales_df.select(
    "order_id",
    "customer_id",
    "customer_city",
    "order_status",
    "product_id",
    "price",
    "freight_value"
).show(20)


print("Total Sales Records:")
print(sales_df.count())

spark.stop()