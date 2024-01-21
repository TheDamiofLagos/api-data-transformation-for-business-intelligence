{{ config(
  materialized='view',
  alias='order_source'
) }}

SELECT * FROM orders_raw