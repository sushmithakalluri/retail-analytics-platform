CREATE OR REPLACE VIEW gold.seller_performance AS
SELECT
    ds.seller_id,
    ds.seller_city,
    ds.seller_state,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.price) AS total_revenue,
    SUM(f.freight_value) AS total_freight,
    AVG(f.price) AS average_item_price
FROM silver.fact_order_items f
JOIN silver.dim_seller ds
    ON f.seller_key = ds.seller_key
GROUP BY
    ds.seller_id,
    ds.seller_city,
    ds.seller_state;