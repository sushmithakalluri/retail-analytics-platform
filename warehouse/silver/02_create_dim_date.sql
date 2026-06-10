DROP TABLE IF EXISTS silver.dim_date;

CREATE TABLE silver.dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    day INTEGER,
    day_name VARCHAR(20)
);