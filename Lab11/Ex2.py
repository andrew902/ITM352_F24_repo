# Read in a CSV file with sales data, called sales_data.csv, and print the first 5 rows.
# Create a pivot table, aggregating by region, with columns defined by order_type (which is
# either Retail or Wholesale)
import pandas as pd

sales_data = pd.read_csv("../sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# We ask Pandas to parse the order_data field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data["order_date"], format='mixed')

# Create a pivot table .
pivot = sales_data.pivot_table(
    values="sale_price", index="sales_region", columns="order_type",
    aggfunc="sum", margins=True, margins_names="Totals"
)

# Set display.max_columns to None, to force display of all columns
pd.set_option("display.max_column", None)

#Print the first 5 rows and the pivot table
print(sales_data.head(5))
print("\nPivot Table:\n", pivot)
