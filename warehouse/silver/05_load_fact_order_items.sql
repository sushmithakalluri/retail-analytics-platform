INSERT INTO silver.fact_order_items (
    order_id,
    customer_key,
    product_key,
    seller_key,
    date_key,
    order_item_id,
    price,
    freight_value
)
SELECT
    oi.order_id,
    dc.customer_key,
    dp.product_key,
    ds.seller_key,
    dd.date_key,
    oi.order_item_id,
    oi.price,
    oi.freight_value
FROM bronze.order_items oi
JOIN bronze.orders o
    ON oi.order_id = o.order_id
JOIN silver.dim_customer dc
    ON o.customer_id = dc.customer_id
JOIN silver.dim_product dp
    ON oi.product_id = dp.product_id
JOIN silver.dim_seller ds
    ON oi.seller_id = ds.seller_id
JOIN silver.dim_date dd
    ON o.order_purchase_timestamp::DATE = dd.full_date;