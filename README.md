# Exploratory-Data-Analysis-of-Skincare-Product-Sales-Using-Python
Exploratory Data Analysis of skincare product sales data using Python, Pandas, NumPy, and Matplotlib to identify revenue trends, product performance, and business insights.
# Exploratory Data Analysis of Skincare Product Sales Using Python

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a skincare product sales dataset to understand product performance, revenue trends, and consumer purchasing behaviour.

The project demonstrates data cleaning, handling missing values, statistical analysis, and data visualization to transform raw sales data into meaningful business insights.

## Problem Statement

Businesses generate large amounts of sales data every day. Analysing this data helps organizations understand customer preferences, identify high-performing products, and monitor sales trends.

This project analyses skincare product sales data to identify revenue patterns, product performance, and consumer preferences in the skincare market.

## Objectives

- Load and explore a skincare product sales dataset.
- Identify and handle missing values.
- Clean and preprocess the dataset.
- Calculate total and average revenue.
- Analyse product-wise revenue.
- Create visualizations using charts and graphs.
- Identify sales trends and business insights.
- Understand consumer preferences in the skincare market.

## Dataset Description

- **Dataset:** Skincare Product Sales Dataset
- **Data Format:** CSV
- **Time Period:** 2025
- **Number of Records:** 45 sales records

The dataset contains sales information about various skincare products.

## Tools and Technologies Used

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Spyder IDE | Writing and executing Python programs |
| Pandas | Data loading, cleaning and manipulation |
| NumPy | Numerical and statistical operations |
| Matplotlib | Data visualization |
| CSV | Dataset storage format |

## Implementation Steps

### 1. Data Loading
Loaded the skincare product sales dataset into a Pandas DataFrame.

### 2. Finding Missing Values
Used `isnull().sum()` to identify missing values in the Quantity and Revenue columns.

### 3. Data Cleaning
Replaced missing values using the mean of the respective columns with the `fillna()` function.

### 4. Revenue Analysis
Calculated:
- Total revenue
- Average revenue
- Product-wise revenue

### 5. Data Visualization
Created the following visualizations using Matplotlib:

- **Bar Chart:** Revenue by product.
- **Pie Chart:** Skincare product category distribution.
- **Line Chart:** Monthly revenue trends.

### 6. Business Insight Generation
Analysed the visualizations to identify sales trends, product performance, and consumer purchasing patterns.

## Key Results and Business Insights

- **Total Revenue:** ₹1,765,046
- **Average Revenue per Sales Record:** Approximately ₹39,223
- **Highest Revenue Product:** LED Face Mask Device
- **Lowest Revenue Product:** Acne Patches

### Additional Insights

- Revenue showed an increasing trend towards the end of the year.
- Serums and advanced skincare products contributed significantly to overall sales.
- Sunscreens, moisturizers, and serums continued to play a major role in the skincare market.

## Project Structure

- `DATASET/` – Skincare product sales dataset
- `SRC/` – Python source code
- `RESULTS/` – Output screenshots and visualizations
- `REPORTS/` – Project documentation and report

## Conclusion

This project successfully performed Exploratory Data Analysis on a skincare product sales dataset using Python, Pandas, NumPy, and Matplotlib.

The dataset was inspected, cleaned, and analysed to understand product performance and revenue trends. Visualizations helped identify the highest and lowest revenue-generating products and revealed an increase in revenue during the final months of the year.

Overall, this project demonstrates how data analysis and visualization techniques can transform raw sales data into meaningful business insights that support better decision-making.

## Author

**MCA Student | Aspiring Software Developer & Data Analyst**
