DROP TABLE IF EXISTS silver.fact_order_items;

CREATE TABLE silver.fact_order_items (
    order_item_key SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    customer_key INTEGER,
    product_key INTEGER,
    seller_key INTEGER,
    date_key INTEGER,
    order_item_id INTEGER,
    price NUMERIC(10,2),
    freight_value NUMERIC(10,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_key)
        REFERENCES silver.dim_customer(customer_key),

    CONSTRAINT fk_product
        FOREIGN KEY (product_key)
        REFERENCES silver.dim_product(product_key),

    CONSTRAINT fk_seller
        FOREIGN KEY (seller_key)
        REFERENCES silver.dim_seller(seller_key),

    CONSTRAINT fk_date
        FOREIGN KEY (date_key)
        REFERENCES silver.dim_date(date_key)
);