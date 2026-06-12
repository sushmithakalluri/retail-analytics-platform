# Azure Architecture Design

## Objective

This document describes how the Retail Analytics Platform can be extended from a local PostgreSQL-based data warehouse into an Azure-based data engineering architecture.

## Current Local Architecture


Local CSV Files
        ↓
Python Ingestion Pipeline
        ↓
PostgreSQL Bronze Layer
        ↓
Silver Dimensional Model
        ↓
Gold Reporting Views