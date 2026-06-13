# Retail Analytics Platform - End-to-End Data Warehouse Project

## Overview

This project demonstrates the design and implementation of an end-to-end Data Warehouse using a Medallion Architecture (Bronze, Silver, Gold) on top of the Brazilian E-Commerce (Olist) dataset.

The objective of the project is to simulate a real-world Data Engineering workflow, including raw data ingestion, dimensional modeling, warehouse transformations, and business-ready reporting datasets.

## Architecture

CSV Files
    │
    ▼
Python Ingestion Pipeline
    │
    ▼
Bronze Layer (Raw PostgreSQL Tables)
    │
    ▼
Silver Layer (Dimensional Model)
    │
    ▼
Gold Layer (Business Reporting Views)

## Technology Stack

- PostgreSQL
- Python 3
- psycopg2
- SQL
- Git & GitHub
- VS Code

## Project Structure

retail-analytics-platform/
│
├── data/
│   └── raw/
│
├── ingestion/
│   └── python/
│       ├── config.py
│       ├── load_bronze.py
│       └── requirements.txt
│
├── warehouse/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── docs/


## Bronze Layer

Raw source CSV files are loaded into PostgreSQL Bronze tables using a Python ingestion pipeline.

Features:
- Config-driven file mapping
- File existence validation
- Automated bulk loading
- Row count logging
- Re-runnable full refresh using table truncation

## Silver Layer

The Silver layer implements a dimensional model.

### Dimension Tables
- dim_customer
- dim_product
- dim_seller
- dim_date

### Fact Tables
- fact_order_items

Key concepts implemented:
- Surrogate keys
- Natural keys
- Fact table grain definition
- Star schema design
- Data transformations and validations

## Gold Layer

Business-ready reporting views:

- sales_summary
- product_performance
- seller_performance

These views provide reusable business metrics for reporting and dashboarding.

## Python Ingestion Pipeline

A Python-based ingestion pipeline automates loading raw CSV files into Bronze tables.

Pipeline features:
- PostgreSQL connectivity
- Config-driven source mapping
- Dynamic file path generation
- File validation
- Bulk CSV loading
- Logging and row count verification

## Key Data Engineering Concepts Demonstrated

- Data Warehouse Design
- Medallion Architecture
- Star Schema Modeling
- Fact vs Dimension Design
- Surrogate Keys
- ETL / ELT Patterns
- Python Data Ingestion
- SQL-based Transformations
- Data Validation
- Git-based Project Management

## Future Enhancements

- Incremental data loading
- Slowly Changing Dimensions (SCD Type 2)
- Dockerized PostgreSQL environment
- Airflow orchestration
- Azure Data Factory integration
- Databricks / PySpark transformations
- CI/CD pipeline for automated deployment

## Dataset

Brazilian E-Commerce Public Dataset by Olist.

### Planned Cloud Architecture

The project is designed to be cloud-ready. In a production Azure environment:

- Raw files would be stored in Azure Blob Storage.
- Azure Data Factory or Synapse Pipelines would orchestrate ingestion.
- Azure Synapse Analytics would provide scalable data warehousing and analytics capabilities.
- Power BI could connect directly to the Gold reporting layer.