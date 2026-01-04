## Data Overview 

The dataset contains 5000 sales records with the following column:

- order_id - unique identifier of an order 
- order_date - date of the order 
- customer_id - unique identifier of a customer 
- product - product name 
- quantity - number of items sold
- price - price per item 

## Identified Data Quality Issues 

During the initial exploratory analysis, the following data quality issues were identified:

1. Missing values in the "price" column 
   - 280 records have missing price values.
   - These records cannot be used to calculate revenue.

2. Negative and zero value in the "quantity" column
   - Some records contain quantity equal to 0 or negatine values.
   - It is unclear whether these values represent returns or data errors.

3. Incorrect data types for "order_date"
   - The order_date column is stored as an object instead of a datetime type. 

## Business Impact 

Due to the identified data quality issues:

- Revenue calculations cannot be considered reliable.
- Missing prices lead to underestimation of total revenue.
- Negative quantities distort average sales metrics.
- Any conclusions based on the raw data may be misleading.

## Next Steps

Before performing any revenue analysis , the data must be cleaned and validated:

- Convert order_date to datetime format.
- Decide how to handle missing prices.
- Define business rules for negativeand zero quantities.
- Recalculate revenue after data cleaning.