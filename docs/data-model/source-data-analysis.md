# Source Data Analysis

## Dataset

Brazilian E-Commerce Public Dataset by Olist.

## Initial Source Tables

| Source File | Business Meaning |
|---|---|
| olist_orders_dataset.csv | Order lifecycle and timestamps |
| olist_order_items_dataset.csv | Products sold per order |
| olist_customers_dataset.csv | Customer location and customer identifiers |
| olist_products_dataset.csv | Product attributes |
| olist_order_payments_dataset.csv | Payment method and payment value |
| olist_sellers_dataset.csv | Seller location and seller identifiers |
| olist_order_reviews_dataset.csv | Customer review score and comments |

## Candidate Facts

- fact_orders
- fact_order_items
- fact_payments
- fact_reviews

## Candidate Dimensions

- dim_customer
- dim_product
- dim_seller
- dim_date
- dim_payment_type

## Notes

The first modeling focus is order and revenue analytics.