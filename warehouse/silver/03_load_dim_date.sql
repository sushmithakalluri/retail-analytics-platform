INSERT INTO silver.dim_date (
    date_key,
    full_date,
    year,
    quarter,
    month,
    month_name,
    day,
    day_name
)

SELECT DISTINCT
    TO_CHAR(order_purchase_timestamp::DATE, 'YYYYMMDD')::INTEGER,
    order_purchase_timestamp::DATE,
    EXTRACT(YEAR FROM order_purchase_timestamp)::INTEGER,
    EXTRACT(QUARTER FROM order_purchase_timestamp)::INTEGER,
    EXTRACT(MONTH FROM order_purchase_timestamp)::INTEGER,
    TRIM(TO_CHAR(order_purchase_timestamp, 'Month')),
    EXTRACT(DAY FROM order_purchase_timestamp)::INTEGER,
    TRIM(TO_CHAR(order_purchase_timestamp, 'Day'))
FROM bronze.orders
WHERE order_purchase_timestamp IS NOT NULL;