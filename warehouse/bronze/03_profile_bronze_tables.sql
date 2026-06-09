SELECT 'orders' AS table_name, COUNT(*) FROM bronze.orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM bronze.order_items
UNION ALL
SELECT 'customers', COUNT(*) FROM bronze.customers
UNION ALL
SELECT 'products', COUNT(*) FROM bronze.products
UNION ALL
SELECT 'sellers', COUNT(*) FROM bronze.sellers
UNION ALL
SELECT 'order_payments', COUNT(*) FROM bronze.order_payments
UNION ALL
SELECT 'order_reviews', COUNT(*) FROM bronze.order_reviews
UNION ALL
SELECT 'product_category_translation', COUNT(*) FROM bronze.product_category_translation;

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT order_id) AS distinct_orders,
    COUNT(DISTINCT product_id) AS distinct_products,
    COUNT(DISTINCT seller_id) AS distinct_sellers,
    SUM(price) AS total_item_revenue,
    SUM(freight_value) AS total_freight
FROM bronze.order_items;