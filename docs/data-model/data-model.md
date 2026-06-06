# Data Model Design

## 1. Business Context

This project models an e-commerce retail platform where customers place orders for products sold by sellers. The objective is to build an analytics-ready data warehouse that supports revenue analysis, product performance, seller performance, customer location analysis, payment analysis, and order lifecycle tracking.

## 2. Primary Business Process

The primary business process is:

> Customer places an order containing one or more products from one or more sellers.

## 3. Fact Table Grain

### Selected Grain

The main fact table will use:

> One row per order item.

This means each row represents a specific product sold within an order.

### Reason

An order can contain multiple products. If the warehouse stores only one row per order, product-level analysis becomes difficult or inaccurate.

Using order-item grain allows analysis such as:

- Revenue by product
- Revenue by seller
- Number of items sold
- Freight cost by product/seller
- Product category performance
- Customer purchase behavior

## 4. Candidate Fact Tables

### fact_order_items

Main transaction fact table.

Measures:

- price
- freight_value
- total_item_value
- item_count

Foreign keys:

- customer_key
- product_key
- seller_key
- order_date_key
- delivered_date_key
- estimated_delivery_date_key

### fact_payments

Separate payment fact table.

Reason:

One order can have multiple payment records or installments. Keeping payments separate avoids duplicating payment values across order items.

Measures:

- payment_value
- payment_installments

Dimensions:

- payment_type
- order_date

### fact_reviews

Optional future fact table.

Measures:

- review_score

Used for customer satisfaction analysis.

## 5. Candidate Dimensions

### dim_customer

Describes customer location and customer identity.

Attributes:

- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

### dim_product

Describes product attributes.

Attributes:

- product_id
- product_category_name
- product_category_name_english
- product_name_length
- product_description_length
- product_photos_qty
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

### dim_seller

Describes seller location.

Attributes:

- seller_id
- seller_zip_code_prefix
- seller_city
- seller_state

### dim_date

Standard calendar dimension used for order, delivery, and estimated delivery dates.

Attributes:

- date_key
- full_date
- year
- quarter
- month
- month_name
- week
- day
- day_name

### dim_order_status

Describes order status.

Attributes:

- order_status

### dim_payment_type

Describes payment method.

Attributes:

- payment_type

## 6. Source-to-Warehouse Mapping

| Source File | Warehouse Usage |
|---|---|
| olist_orders_dataset.csv | Order dates, customer relationship, order status |
| olist_order_items_dataset.csv | Main transaction line items |
| olist_customers_dataset.csv | Customer dimension |
| olist_products_dataset.csv | Product dimension |
| product_category_name_translation.csv | Product category enrichment |
| olist_sellers_dataset.csv | Seller dimension |
| olist_order_payments_dataset.csv | Payment fact |
| olist_order_reviews_dataset.csv | Review fact / customer satisfaction analysis |

## 7. Initial Gold Layer Model

```text
dim_customer
      |
dim_product
      |
dim_seller
      |
dim_date
      |
fact_order_items