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