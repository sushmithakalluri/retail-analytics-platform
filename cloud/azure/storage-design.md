# Azure Storage Design

## Purpose

This document explains how Azure Blob Storage would be used as the raw data landing zone for the Retail Analytics Platform.

The project currently runs locally to avoid Azure costs, but the folder structure and ingestion design are aligned with how the same pipeline would work with Azure Blob Storage.

## Storage Role in the Architecture

Azure Blob Storage would act as the first cloud landing layer for raw source files.


Source CSV Files
        ↓
Azure Blob Storage
        ↓
Ingestion Pipeline / Azure Data Factory
        ↓
PostgreSQL or Azure SQL Bronze Layer
        ↓
Silver Dimensional Model
        ↓
Gold Reporting Views



Storage Account: retailanalyticsstorage
│
└── Container: retail-raw-data
    │
    ├── orders/
    │   └── olist_orders_dataset.csv
    │
    ├── order_items/
    │   └── olist_order_items_dataset.csv
    │
    ├── customers/
    │   └── olist_customers_dataset.csv
    │
    ├── products/
    │   └── olist_products_dataset.csv
    │
    ├── sellers/
    │   └── olist_sellers_dataset.csv
    │
    ├── payments/
    │   └── olist_order_payments_dataset.csv
    │
    ├── reviews/
    │   └── olist_order_reviews_dataset.csv
    │
    └── reference/
        └── product_category_name_translation.csv