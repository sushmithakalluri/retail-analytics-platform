DROP TABLE IF EXISTS silver.dim_customer;

CREATE TABLE silver.dim_customer (

    customer_key SERIAL PRIMARY KEY,

    customer_id VARCHAR(50),

    customer_unique_id VARCHAR(50),

    customer_city VARCHAR(100),

    customer_state VARCHAR(10)

);