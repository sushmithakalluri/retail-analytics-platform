import sys

sys.path.append("ingestion/python")

from config import PARQUET_OUTPUT_PATHS
from pyspark.sql.functions import col, to_timestamp, lit
from utils import create_spark_session, read_csv, write_parquet, validate_not_empty


spark = create_spark_session("Retail Analytics - Bronze to Silver")


orders_df = read_csv(spark, "orders")
customers_df = read_csv(spark, "customers")
order_items_df = read_csv(spark, "order_items")


# Clean orders
orders_clean_df = (
    orders_df
    .dropDuplicates(["order_id"])
    .filter(col("order_id").isNotNull())
    .filter(col("customer_id").isNotNull())
    .withColumn(
        "order_purchase_timestamp",
        to_timestamp(col("order_purchase_timestamp"))
    )
)

# Clean customers
customers_clean_df = (
    customers_df
    .dropDuplicates(["customer_id"])
    .filter(col("customer_id").isNotNull())
)

# Clean order items
order_items_clean_df = (
    order_items_df
    .dropDuplicates(["order_id", "order_item_id"])
    .filter(col("order_id").isNotNull())
    .filter(col("product_id").isNotNull())
    .filter(col("seller_id").isNotNull())
    .filter(col("price").isNotNull())
    .filter(col("price") >= 0)
    .filter(col("freight_value") >= 0)
)

# Build Silver sales dataset
silver_sales_df = (
    orders_clean_df
    .join(customers_clean_df, on="customer_id", how="inner")
    .join(order_items_clean_df, on="order_id", how="inner")
    .withColumn("source_system", lit("olist"))
    .select(
        "order_id",
        "order_item_id",
        "customer_id",
        "customer_unique_id",
        "customer_city",
        "customer_state",
        "order_status",
        "order_purchase_timestamp",
        "product_id",
        "seller_id",
        "price",
        "freight_value",
        "source_system"
    )
)

validate_not_empty(silver_sales_df, "silver_sales")
write_parquet(
    silver_sales_df,
    PARQUET_OUTPUT_PATHS["silver_sales"]
)

print("Silver sales dataset created successfully.")
print(f"Total rows: {silver_sales_df.count()}")

spark.stop()