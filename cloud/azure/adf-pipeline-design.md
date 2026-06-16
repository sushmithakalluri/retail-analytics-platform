# Azure Data Factory Pipeline Design

## Purpose

This document describes how Azure Data Factory (ADF) could orchestrate the Retail Analytics Platform in a production Azure environment.

## Current Local Process


CSV Files
      ↓
Python Ingestion
      ↓
Bronze Tables
      ↓
Silver Tables
      ↓
Gold Views


## Conceptual Azure Process


Azure Blob Storage
      ↓
ADF Pipeline
      ↓
Bronze Layer
      ↓
Silver Layer
      ↓
Gold Layer
      ↓
Power BI


## Pipeline Activities

### Activity 1

Copy source files from Azure Blob Storage.

### Activity 2

Load raw files into Bronze tables.

### Activity 3

Build dimension tables:

- dim_customer
- dim_product
- dim_seller
- dim_date

### Activity 4

Build fact table:

- fact_order_items

### Activity 5

Refresh Gold reporting views.

### Activity 6

Run validation checks.

### Activity 7

Send success or failure notification.

## Local Equivalent

| ADF Activity | Current Project |
|-------------|----------------|
| Copy Activity | Python ingestion pipeline |
| Pipeline | End-to-end workflow |
| Trigger | Manual execution |
| Monitoring | Console logging |
| Validation | SQL validation scripts |