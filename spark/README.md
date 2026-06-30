# PySpark Module

This folder contains the PySpark implementation of the Retail Analytics Platform.

## Structure

### examples/

Contains small learning examples for PySpark concepts such as reading CSV files, selecting columns, filtering, joins, grouping, and writing Parquet.

### pipeline/

Contains the actual Spark-based ETL pipeline.

- `bronze_to_silver.py` builds curated Silver datasets from raw source files.
- `silver_to_gold.py` builds business-ready Gold datasets from Silver outputs.
- `utils.py` contains reusable Spark helper functions.

## Purpose

The goal of this module is to evolve the project from a SQL-based warehouse implementation into a Spark-based data engineering pipeline.