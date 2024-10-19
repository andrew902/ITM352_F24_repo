import pandas as pd

# Read the sales data CSV and convert types using pyarrow for better performance
sales_data = pd.read_csv("../sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# Convert 'order_date' to datetime (removed the 'format=mixed' which is not valid)
sales_data['order_date'] = pd.to_datetime(sales_data["order_date"])

# Create a pivot table aggregating by region and showing the average sales by sale type
pivot = sales_data.pivot_table(
    values="sale_price", 
    index="customer_state", 
    columns=["customer_type", "order_type"], 
    aggfunc="mean"
)

# Set the option to display all columns
pd.set_option("display.max_columns", None)

# Set float format to 2 decimal places with dollar sign
pd.set_option("display.float_format", "${:,.2f}".format)

# Print the first 5 rows and the pivot table
print(sales_data.head(5))
print("\nPivot Table:\n", pivot)
