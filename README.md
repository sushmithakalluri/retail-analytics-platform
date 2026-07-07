# Retail Analytics Platform

An end-to-end data engineering project built using Python, PostgreSQL, SQL, PySpark, Apache Airflow, Docker, and Parquet.

The project processes the Brazilian Olist e-commerce dataset through ingestion, warehouse modeling, scalable Spark transformations, and workflow orchestration.

The goal is to demonstrate practical data engineering concepts including:

- Data ingestion
- Bronze, Silver, and Gold data layers
- Dimensional modeling
- Star schema design
- Fact and dimension tables
- Surrogate keys
- SQL transformations
- PySpark DataFrame processing
- Parquet storage
- Data validation
- Workflow orchestration with Apache Airflow
- Modular and configurable pipeline design

---

## Architecture

The project contains multiple complementary data engineering implementations.

### 1. SQL Warehouse Pipeline

```text
Raw CSV Files
      |
      v
Python Ingestion
      |
      v
PostgreSQL Bronze Layer
      |
      v
SQL Transformations
      |
      v
Silver Dimensional Model
      |
      v
Gold Analytical Views
```

This pipeline demonstrates relational data warehousing and dimensional modeling.

### 2. PySpark Transformation Pipeline

```text
Raw Olist CSV Files
      |
      v
PySpark DataFrames
      |
      v
Cleaning and Validation
      |
      v
Joins and Curated Transformations
      |
      v
Silver Sales Dataset
      |
      v
Parquet Output
```

This pipeline demonstrates scalable DataFrame-based transformation and columnar storage.

### 3. Airflow Orchestration

```text
start_pipeline
      |
      v
load_bronze
Python ingestion into PostgreSQL
      |
      v
run_bronze_to_silver
PySpark transformation
      |
      v
end_pipeline
```

Apache Airflow orchestrates existing project components rather than embedding transformation logic directly inside the DAG.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data ingestion and pipeline utilities |
| PostgreSQL | Bronze, Silver, and Gold warehouse layers |
| SQL | Data cleaning, dimensional modeling, and analytics |
| PySpark | Scalable transformation and Silver dataset processing |
| Apache Airflow | Workflow orchestration and task dependency management |
| Parquet | Columnar storage for Spark output |
| Docker | Local PostgreSQL environment |
| Git | Version control |

---

## Dataset

The project uses the Brazilian Olist E-Commerce Public Dataset.

The source data includes:

- Orders
- Order items
- Customers
- Products
- Sellers
- Payments
- Reviews
- Product category translations

Raw dataset files are not committed to the repository.

---

## Project Structure

```text
retail-analytics-platform/
|
├── airflow/
│   └── dags/
│       └── retail_analytics_dag.py
|
├── data/
│   ├── raw/
│   └── parquet/
│       └── silver/
|
├── docs/
│   ├── architecture.md
│   ├── AzureArchitecture.md
│   ├── data-model.md
│   └── storageDesign.md
|
├── ingestion/
│   └── python/
│       ├── config.py
│       ├── load_bronze.py
│       └── load_bronze_from_azure_blob.py
|
├── spark/
│   ├── examples/
│   │   ├── 01_read_orders.py
│   │   ├── 02_payment_transformations.py
│   │   ├── 03_join_orders_customers.py
│   │   ├── 04_build_sales_dataset.py
│   │   └── 05_write_parquet.py
│   |
│   ├── pipeline/
│   │   ├── bronze_to_silver.py
│   │   ├── silver_to_gold.py
│   │   └── utils.py
│   |
│   └── README.md
|
├── sql/
│   ├── bronze/
│   ├── silver/
│   └── gold/
|
└── README.md
```

> Note: `silver_to_gold.py` is reserved for future Spark-based Gold transformations. The current Gold analytical implementation remains SQL-based.

---

## Data Layers

### Bronze Layer

The Bronze layer stores raw source data with minimal transformation.

Python ingestion reads Olist CSV files and loads them into PostgreSQL Bronze tables.

Example datasets:

- `bronze.orders`
- `bronze.order_items`
- `bronze.customers`
- `bronze.products`
- `bronze.sellers`
- `bronze.order_payments`
- `bronze.order_reviews`
- `bronze.product_category_translation`

The ingestion pipeline uses centralized configuration for:

- database connection settings
- source data path
- CSV-to-table mappings

---

### Silver Layer

The project demonstrates two Silver-layer approaches.

#### SQL Silver Layer

The SQL implementation creates a dimensional warehouse model using cleaned and transformed source data.

It includes:

- fact tables
- dimension tables
- surrogate keys
- standardized data types
- dimensional relationships

#### PySpark Silver Layer

The PySpark implementation demonstrates scalable transformation using Spark DataFrames.

The pipeline performs:

- CSV ingestion into Spark DataFrames
- duplicate removal
- null-key filtering
- timestamp conversion
- invalid price filtering
- invalid freight filtering
- customer, order, and order-item joins
- source-system metadata enrichment
- output validation
- Parquet generation

The resulting curated Silver sales dataset is written to:

```text
data/parquet/silver/sales/
```

---

### Gold Layer

The Gold layer provides business-ready analytical outputs.

The current implementation uses SQL-based aggregations and views.

Example metrics include:

- total orders
- total revenue
- total freight
- average item price
- daily sales metrics

The Gold layer is intentionally kept SQL-based rather than duplicating the complete analytical implementation in PySpark.

---

## Dimensional Model

The warehouse follows a star-schema-oriented design.

### Fact Tables

#### Order Items Fact

Grain:

> One row per product sold within an order.

Contains measures such as:

- item price
- freight value

#### Payments Fact

Stores payment-level transactional information separately from order items.

This avoids mixing different business grains in a single fact table.

### Dimension Tables

The model includes dimensions such as:

- Customers
- Products
- Sellers
- Orders
- Date

Surrogate keys are used to separate warehouse identifiers from source-system business keys.

---

## Python Ingestion Pipeline

The Bronze ingestion pipeline is implemented in:

```text
ingestion/python/load_bronze.py
```

The pipeline:

1. Reads centralized configuration.
2. Resolves source CSV paths.
3. Validates source-file availability.
4. Connects to PostgreSQL.
5. Loads source data into Bronze tables.
6. Reports loaded row counts.

Example validated row counts include:

```text
Orders:                         99,441
Order Items:                   112,650
Customers:                      99,441
Products:                       32,951
Sellers:                         3,095
Order Payments:                103,886
Order Reviews:                  99,224
Product Category Translation:       71
```

---

## PySpark Implementation

The Spark module is divided into two areas.

### `spark/examples/`

Contains focused examples used to explore individual PySpark concepts:

- reading CSV files
- selecting columns
- filtering
- transformations
- joins
- aggregations
- writing Parquet

### `spark/pipeline/`

Contains project-oriented Spark pipeline code.

#### `bronze_to_silver.py`

Builds the curated Silver sales dataset.

It performs:

- source reads
- duplicate removal
- null validation
- timestamp conversion
- value validation
- joins
- metadata enrichment
- output validation
- Parquet writing

#### `utils.py`

Provides reusable helpers for:

- SparkSession creation
- CSV reading
- source-file validation
- Parquet writing
- non-empty dataset validation

---

## Apache Airflow Orchestration

The Airflow DAG is defined in:

```text
airflow/dags/retail_analytics_dag.py
```

The DAG orchestrates existing pipeline components.

Current task flow:

```text
start_pipeline
      |
      v
load_bronze
      |
      v
run_bronze_to_silver
      |
      v
end_pipeline
```

### `load_bronze`

Runs:

```text
ingestion/python/load_bronze.py
```

This loads raw CSV datasets into PostgreSQL Bronze tables.

### `run_bronze_to_silver`

Runs:

```text
spark/pipeline/bronze_to_silver.py
```

This creates the curated Silver Parquet dataset using PySpark.

The DAG also demonstrates:

- task dependencies
- TaskFlow-style Python tasks
- retry configuration
- retry delay
- failure propagation
- centralized script execution logic

For local development, the DAG uses:

```text
schedule=None
```

and is triggered manually.

---

## Configuration

Centralized configuration is maintained in:

```text
ingestion/python/config.py
```

Configuration includes:

- PostgreSQL connection details
- raw dataset location
- CSV file mappings
- Parquet output locations

This reduces hardcoded paths inside transformation logic and makes pipeline behavior easier to maintain.

---

## Data Validation

The project includes basic defensive validation.

Examples include:

- checking whether source files exist
- filtering null business keys
- removing duplicate records
- rejecting negative price values
- rejecting negative freight values
- verifying that the Silver output is not empty before writing

These checks prevent obviously invalid outputs from silently progressing through the pipeline.

---

## Running the Project

### Prerequisites

Install and configure:

- Python
- PostgreSQL
- Docker
- Java 17
- PySpark
- Apache Airflow

### Run Bronze Ingestion

From the project root:

```bash
python3 ingestion/python/load_bronze.py
```

### Run PySpark Silver Transformation

```bash
python3 spark/pipeline/bronze_to_silver.py
```

### Run with Airflow

Set the local Airflow home:

```bash
export AIRFLOW_HOME="/path/to/retail-analytics-platform/airflow"
```

Start Airflow:

```bash
airflow standalone
```

Open the Airflow UI and trigger:

```text
retail_analytics_pipeline
```

---

## Azure Architecture Design

The repository includes Azure-oriented architecture documentation describing how the local solution could evolve toward cloud storage and managed data services.

The design considers services such as:

- Azure Blob Storage
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Synapse Analytics

The repository also contains placeholder Python integration code for Azure Blob-based ingestion.

Azure resources are not actively deployed as part of the current project. The cloud architecture is documented as a future deployment path rather than presented as a completed implementation.

---

## Design Decisions

### Why PostgreSQL?

PostgreSQL provides a practical local relational environment for implementing:

- Bronze ingestion
- dimensional modeling
- fact and dimension tables
- SQL transformations
- analytical views

### Why PySpark?

PySpark demonstrates how selected transformation workloads can be implemented using a distributed DataFrame processing model.

The project intentionally implements a focused Silver transformation rather than duplicating the entire SQL warehouse pipeline in Spark.

### Why Parquet?

Parquet provides:

- columnar storage
- schema preservation
- efficient analytical reads
- compatibility with Spark and modern data platforms

### Why Airflow?

Airflow separates orchestration from transformation logic.

The DAG coordinates existing Python and PySpark jobs while providing:

- dependency management
- retries
- execution visibility
- failure tracking

### Why keep Gold SQL-based?

Reimplementing the complete Gold layer in PySpark would duplicate existing business logic without demonstrating significantly different engineering skills.

The project therefore uses:

- SQL for dimensional warehouse and Gold analytics
- PySpark for a focused scalable Silver transformation
- Airflow for orchestration

---

## Current Scope

Implemented:

- Python-based Bronze ingestion
- PostgreSQL Bronze layer
- SQL Silver transformations
- dimensional modeling
- star-schema-oriented design
- fact and dimension tables
- surrogate keys
- SQL Gold analytics
- PySpark examples
- PySpark Silver transformation pipeline
- Parquet output
- source and output validation
- reusable Spark utilities
- Airflow orchestration
- retries and task dependencies
- architecture documentation
- Azure future-state design

---

## Future Enhancements

Potential future improvements include:

- incremental ingestion
- stronger idempotency guarantees
- automated data-quality testing
- unit and integration tests
- CI/CD pipeline
- secrets management
- environment-specific configuration
- partitioned Parquet output
- cloud deployment
- managed Spark execution
- production-grade Airflow deployment
- observability and alerting
- SCD Type 2 implementation where business requirements justify it

These are intentionally treated as future enhancements rather than completed features.

---

## Project Status

The core implementation is complete for the current portfolio scope.

The repository demonstrates an end-to-end progression from raw ingestion and warehouse modeling to Spark-based transformation and Airflow orchestration, while clearly separating implemented functionality from future cloud and production enhancements.