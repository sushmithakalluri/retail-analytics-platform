-- Gold layer validation

SELECT COUNT(*) AS sales_summary_days
FROM gold.sales_summary;

SELECT COUNT(*) AS product_count
FROM gold.product_performance;

SELECT COUNT(*) AS seller_count
FROM gold.seller_performance;

-- Top 5 revenue days
SELECT *
FROM gold.sales_summary
ORDER BY total_revenue DESC
LIMIT 5;

-- Top 5 products
SELECT *
FROM gold.product_performance
ORDER BY total_revenue DESC
LIMIT 5;

-- Top 5 sellers
SELECT *
FROM gold.seller_performance
ORDER BY total_revenue DESC
LIMIT 5;