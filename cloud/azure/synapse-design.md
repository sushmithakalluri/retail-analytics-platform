# Azure Synapse Design

## Purpose

This document explains how Azure Synapse Analytics could be integrated into the Retail Analytics Platform.

## Current Local Implementation

Local CSV Files
        ↓
Python Ingestion
        ↓
PostgreSQL Bronze
        ↓
Silver Layer
        ↓
Gold Views


## Conceptual Azure Synapse Architecture

Azure Blob Storage
        ↓
Azure Synapse Workspace
        ↓
Serverless SQL Pool (query raw files)
        ↓
Dedicated SQL Pool (curated warehouse)
        ↓
Power BI / Analytics


## Mapping to This Project

| Retail Analytics Project | Azure Synapse Equivalent |
|--------------------------|--------------------------|
| data/raw/Brazilian dataset | Azure Blob Storage |
| Python Bronze Loader | Synapse Pipeline / ADF |
| PostgreSQL Bronze | Dedicated SQL Pool Landing Layer |
| Silver Dimension Tables | Curated Warehouse Layer |
| Gold Reporting Views | Analytics / Serving Layer |

## Notes

- The local folder structure simulates Azure Blob Storage.
- The PostgreSQL warehouse simulates a Synapse Dedicated SQL Pool.
- The Python ingestion pipeline simulates Azure Data Factory or Synapse Pipelines.
- Actual Azure deployment is intentionally omitted to avoid cloud costs while preserving the architecture.


## Synapse Design Mapping

The local Retail Analytics Platform follows the same logical design principles used by Azure Synapse Analytics.

| Local Implementation | Azure Synapse Equivalent |
|----------------------|--------------------------|
| Local CSV files | Azure Blob Storage / Data Lake |
| Python ingestion pipeline | Synapse Pipelines / Azure Data Factory |
| PostgreSQL Bronze layer | Landing / Raw layer |
| Silver dimension model | Curated warehouse layer |
| Gold reporting views | Analytics serving layer |
| PostgreSQL views | Serverless SQL queries / Power BI semantic layer |

## Warehouse Design Principles

The warehouse follows a star-schema approach:
- Fact table: `fact_order_items`
- Dimension tables:
  - `dim_customer`
  - `dim_product`
  - `dim_seller`
  - `dim_date`

Dimension tables use surrogate keys to simplify joins and support future Slowly Changing Dimension (SCD) implementations.

## Future Enhancements

The following Azure Synapse concepts can be incorporated into future versions of the project:

- Slowly Changing Dimensions (SCD Type 2)
- Partitioning large fact tables
- PySpark transformations using Spark pools
- Power BI integration
- Azure Data Factory orchestration