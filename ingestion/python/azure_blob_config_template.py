"""Template configuration for Azure Blob Storage integration.
This file is intentionally not connected to a real Azure account.
It documents how the local ingestion pipeline can be extended to read files from Azure Blob Storage."""

AZURE_BLOB_CONFIG = {
    "storage_account_name": "<your-storage-account-name>",
    "container_name": "retail-raw-data",
    "connection_string": "<stored-securely-in-environment-variable>"
}

BLOB_TABLE_MAPPING = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "product_category_translation": "product_category_name_translation.csv"
}