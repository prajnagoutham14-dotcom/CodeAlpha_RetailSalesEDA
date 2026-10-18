
import pandas as pd

# Load the retail sales dataset
df = pd.read_csv("CodeAlpha_EDA/data/retail_sales_dataset.csv")

# Display the first 5 rows
print(df.head())

# Display the dataset dimensions
print("Dataset shape:", df.shape)

# Display the column names
print("Column names:", df.columns.tolist())

# Check column data types and missing values
print("\nDataset information:")
df.info()

# Count missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Count duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Get statistical summary
print("\nStatistical summary:")
print(df.describe())

# Convert the Date column from text to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Verify the updated data type
print("\nUpdated date data type:")
print(df["Date"].dtype)

# Check the date range
print("Earliest date:", df["Date"].min())
print("Latest date:", df["Date"].max())

# Check whether transaction IDs are unique
print("\nDuplicate transaction IDs:", df["Transaction ID"].duplicated().sum())

# Check whether recorded amounts match quantity × unit price
df["Expected Amount"] = df["Quantity"] * df["Price per Unit"]

df["Amount Difference"] = df["Total Amount"] - df["Expected Amount"]

print("Transactions with amount mismatches:", (df["Amount Difference"] != 0).sum())

# Display any mismatched transactions
print(df.loc[df["Amount Difference"] != 0, [
    "Transaction ID", "Quantity", "Price per Unit",
    "Total Amount", "Expected Amount"
]].head())

# Calculate total sales for each product category
category_sales = df.groupby("Product Category")["Total Amount"].sum()

# Sort categories from highest sales to lowest
category_sales = category_sales.sort_values(ascending=False)

print("\nTotal sales by product category:")
print(category_sales)

import matplotlib.pyplot as plt

# Create a bar chart of sales by product category
plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("CodeAlpha_EDA/outputs/category_sales.png")

# Display the chart
plt.show()

# Extract the month from the transaction date
df["Month"] = df["Date"].dt.to_period("M")

# Calculate total sales for each month
monthly_sales = df.groupby("Month")["Total Amount"].sum()

print("\nTotal sales by month:")
print(monthly_sales)

# Extract the month from the transaction date
df["Month"] = df["Date"].dt.to_period("M")

# Calculate total sales for each month
monthly_sales = df.groupby("Month")["Total Amount"].sum()

print("\nTotal sales by month:")
print(monthly_sales)

import matplotlib.pyplot as plt

# Create a line chart of monthly sales
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the chart
plt.savefig("CodeAlpha_EDA/outputs/monthly_sales.png")

# Display the chart
plt.show()

# Calculate total sales by gender
gender_sales = df.groupby("Gender")["Total Amount"].sum()

print("\nTotal sales by gender:")
print(gender_sales)

# Create a bar chart of sales by gender
plt.figure(figsize=(7, 5))

gender_sales.plot(kind="bar")

plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("CodeAlpha_EDA/outputs/gender_sales.png")

# Display the chart
plt.show()

# Divide customers into age groups
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-64"]
)

# Calculate total sales for each age group
age_group_sales = df.groupby(
    "Age Group", observed=False
)["Total Amount"].sum()

print("\nTotal sales by age group:")
print(age_group_sales)

# Create a bar chart of sales by age group
plt.figure(figsize=(8, 5))

age_group_sales.plot(kind="bar")

plt.title("Total Sales by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("CodeAlpha_EDA/outputs/age_group_sales.png")

# Display the chart
plt.show()

# Count transactions in each product category
category_counts = df["Product Category"].value_counts()

print("\nNumber of transactions by product category:")
print(category_counts)

# Calculate average transaction value by product category
avg_sales = df.groupby("Product Category")["Total Amount"].mean()

# Sort from highest to lowest
avg_sales = avg_sales.sort_values(ascending=False)

print("\nAverage transaction value by product category:")
print(avg_sales.round(2))
