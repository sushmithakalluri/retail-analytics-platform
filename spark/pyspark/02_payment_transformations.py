import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Allow Spark script to import config from ingestion/python
sys.path.append("ingestion/python")

from config import DATA_PATH, CSV_TABLE_MAPPING


spark = SparkSession.builder \
    .appName("Retail Analytics - Payment Transformations") \
    .getOrCreate()


payments_file = CSV_TABLE_MAPPING["order_payments"]
payments_path = os.path.join(DATA_PATH, payments_file)

payments_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(payments_path)


payments_transformed_df = payments_df.withColumn(
    "payment_category",
    when(col("payment_value") >= 500, "High Value")
    .otherwise("Regular")
)


print("Payments schema:")
payments_transformed_df.printSchema()

print("Sample payment records:")
payments_transformed_df.select(
    "order_id",
    "payment_type",
    "payment_installments",
    "payment_value",
    "payment_category"
).show(20)

print("Payment category counts:")
payments_transformed_df.groupBy("payment_category").count().show()


spark.stop()