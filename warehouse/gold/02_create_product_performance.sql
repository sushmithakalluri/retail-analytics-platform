CREATE OR REPLACE VIEW gold.product_performance AS
SELECT
    dp.product_id,
    dp.product_category_name,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.price) AS total_revenue,
    SUM(f.freight_value) AS total_freight,
    AVG(f.price) AS average_selling_price
FROM silver.fact_order_items f
JOIN silver.dim_product dp
    ON f.product_key = dp.product_key
GROUP BY
    dp.product_id,
    dp.product_category_name;