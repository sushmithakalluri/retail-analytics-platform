\copy bronze.orders FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_orders_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.order_items FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_order_items_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.customers FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_customers_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.products FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_products_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.sellers FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_sellers_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.order_payments FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_order_payments_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.order_reviews FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/olist_order_reviews_dataset.csv' DELIMITER ',' CSV HEADER;

\copy bronze.product_category_translation FROM '/Users/sushmithakalluri/Documents/GitHub/retail-analytics-platform/data/raw/Brazilian dataset/product_category_name_translation.csv' DELIMITER ',' CSV HEADER;