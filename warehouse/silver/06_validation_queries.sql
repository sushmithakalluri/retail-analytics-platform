-- ========================================
-- Silver Layer Validation Queries
-- ========================================

-- Dimension row counts
SELECT 'dim_customer' AS table_name, COUNT(*) AS row_count
FROM silver.dim_customer

UNION ALL

SELECT 'dim_product', COUNT(*)
FROM silver.dim_product

UNION ALL

SELECT 'dim_seller', COUNT(*)
FROM silver.dim_seller

UNION ALL

SELECT 'dim_date', COUNT(*)
FROM silver.dim_date;


-- Check for duplicate business keys
SELECT customer_id, COUNT(*)
FROM silver.dim_customer
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT product_id, COUNT(*)
FROM silver.dim_product
GROUP BY product_id
HAVING COUNT(*) > 1;

SELECT seller_id, COUNT(*)
FROM silver.dim_seller
GROUP BY seller_id
HAVING COUNT(*) > 1;


-- Verify date range
SELECT
    MIN(full_date) AS earliest_date,
    MAX(full_date) AS latest_date,
    COUNT(*) AS distinct_dates
FROM silver.dim_date;


-- Fact table validation
SELECT
    COUNT(*) AS total_rows,
    SUM(price) AS total_revenue,
    SUM(freight_value) AS total_freight
FROM silver.fact_order_items;

-- Compare Bronze vs Silver fact totals
SELECT
    'bronze_order_items' AS layer,
    COUNT(*) AS total_rows,
    SUM(price) AS total_revenue,
    SUM(freight_value) AS total_freight
FROM bronze.order_items

UNION ALL

SELECT
    'silver_fact_order_items' AS layer,
    COUNT(*) AS total_rows,
    SUM(price) AS total_revenue,
    SUM(freight_value) AS total_freight
FROM silver.fact_order_items;