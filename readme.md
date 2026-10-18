# Retail Sales Exploratory Data Analysis (EDA)

## Project Overview
This project uses Python to explore retail transaction data, identify sales patterns, and understand customer purchasing behavior.

## Objectives
- Inspect data quality and missing values.
- Analyze sales by product category.
- Explore monthly sales trends.
- Compare sales by gender and customer age group.
- Calculate transaction counts and average transaction values.
- Create charts to communicate findings.

## Tools Used
- Python
- Pandas
- Matplotlib
- Visual Studio Code

## Dataset
The dataset contains 1,000 retail transactions and 9 original columns, including transaction date, customer details, product category, quantity, unit price, and total amount.

## Data Quality Checks
- No missing values were found.
- No duplicate rows or transaction IDs were found.
- Dates were converted to datetime format.
- Recorded amounts matched quantity multiplied by unit price for all transactions.

## Key Findings
- Electronics recorded the highest total sales: 156,905.
- Clothing had the highest number of transactions: 351.
- Beauty had the highest average transaction value: 467.48.
- Customers aged 46–55 recorded the highest total sales: 100,690.
- May 2023 had the highest monthly sales: 53,150.
- Female-customer transactions contributed 232,840 in sales, compared with 223,160 for male-customer transactions.

## Visualizations
The following charts are included in this repository:
- `category_sales.png`
- `monthly_sales.png`
- `gender_sales.png`
- `age_group_sales.png`

## How to Run
Install the required libraries:

`pip install pandas matplotlib`

Run the script from the parent project folder:

`python CodeAlpha_EDA/eda_analysis.py`

## Conclusion
This project demonstrates the use of Python for data cleaning checks, exploratory analysis, and visualization of retail sales data.

## Disclaimer
The results describe the available dataset and do not establish the causes of customer purchasing behavior.
