# EntansTask

## Introduction
- This project demonstrates a comprehensive approach to analyzing sales data and visualizing insights for better business decision-making. The analysis focuses on identifying patterns, trends, and performance metrics using Python and industry-standard data visualization techniques. This report highlights the methodology, results, and key insights derived from the toolkit.

## Objectives
  1. Data Quality Assessment: Ensure the dataset is free of missing values and duplicates.
  2. Descriptive Analysis: Provide statistical summaries and unique counts of key features.
  3. Visualization: Generate clear and informative charts to depict trends and performance metrics.
  4. Performance Insights: Identify top-performing sub-categories and evaluate profitability and revenue growth.

## Dataset
   The dataset used in this project (sales_data.xlsx) contains the following columns: 
   - Date: Transaction dates.
   - Product_Category: High-level category of products.
   - Sub_Category: Specific sub-categories within each product category.
   - Product: Individual product names.
   - Customer_Age: Age of customers.
   - Customer_Gender: Gender of customers.
   - Age_Group: Grouped age ranges.
   - Revenue: Revenue generated per transaction.
   - Profit: Profit earned per transaction  

## Analysis steps
### Data Preprocessing
1. Null Values: Identified no missing values across all columns.
2. Duplicate Columns: Verified that there were no duplicate column names.
3. Data Types: Confirmed that all columns have appropriate data types for analysis.
### Data Analyzing
1. Statistical summaries were generated for numerical columns, including mean, median, standard deviation, and percentiles.
2. Counted unique values for Product_Category, Sub_Category, and Product.  
### Data Visualiztion
1. Customer Age Distribution: Histogram showing the frequency of customers by age.
2. Gender Distribution: Pie chart displaying the proportion of male and female customers.
3. Revenue by Age Group: Bar chart visualizing revenue across different age groups.
4. Profit by Product Category: Horizontal bar chart depicting profit contribution by each product category.
5. Profit Margin per Product: Scatter plot analyzing average profit margins for products.
6. Revenue and Profit Trends: Line chart showing revenue and profit trends over specific date ranges.
7. Sub-Category Performance: Stacked bar chart comparing sub-category performance within each product category.
### Performance insights
1. Sub-Category Analysis: The sub-category with the highest profit was identified for each product category.
2. Revenue Trends: Analyzed revenue growth over time to detect seasonal trends or anomalies.
3. Profitability Analysis: Assessed profit margins for individual products to identify high-margin items.

## Generated visualizations
- customer_age_histogram.png - Histogram for customer age distribution.
- gender_distribution.png: Pie chart of gender distribution.
- age_group_revenue.png: Revenue by age group.
- product_category_profit.png: Profit by product category.
- profit_margin_scatter.png: Scatter plot of profit margins per product.
- revenue_profit_trends.png: Revenue and profit trends over a specific time range.
- sub_category_profit.png: Sub-category performance by profit.
- sub_category_revenue.png: Sub-category performance by revenue.

## Conclusion
- This project demonstrates the power of data visualization and analysis in deriving meaningful insights from sales data. By identifying trends and performance metrics, businesses can make informed decisions to improve profitability and customer satisfaction.

