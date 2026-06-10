CREATE TABLE silver.dim_seller (
    seller_key SERIAL PRIMARY KEY,
    seller_id VARCHAR(50) UNIQUE,
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state VARCHAR(10)
);