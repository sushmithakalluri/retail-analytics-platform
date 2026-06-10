INSERT INTO silver.dim_customer (
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
)
SELECT DISTINCT
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
FROM bronze.customers;