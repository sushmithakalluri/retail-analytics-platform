CREATE OR REPLACE VIEW gold.sales_summary AS
SELECT
    d.full_date,
    d.year,
    d.month,
    d.month_name,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.price) AS total_revenue,
    SUM(f.freight_value) AS total_freight,
    AVG(f.price) AS average_item_price
FROM silver.fact_order_items f
JOIN silver.dim_date d
    ON f.date_key = d.date_key
GROUP BY
    d.full_date,
    d.year,
    d.month,
    d.month_name;