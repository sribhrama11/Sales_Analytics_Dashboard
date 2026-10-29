# Sales Analytics Dashboard

**An interactive sales analysis and business intelligence application developed using Python, Pandas, Plotly, and Streamlit.**

## 📌 Project Overview

The Sales Analytics Dashboard is an interactive business intelligence solution designed to analyze sales transactions and present useful business insights through visual reports.

It helps users evaluate sales revenue, profit, product performance, customer purchasing patterns, regional results, and business growth using interactive charts and analytical summaries.

## 🎯 Project Objective

The primary goal of this project is to convert raw sales records into meaningful information that supports better business decisions.

The application enables users to:

- Evaluate overall sales performance.
- Examine revenue and profitability.
- Identify successful and underperforming products.
- Analyze customer purchasing behavior.
- Compare sales results across regions.
- Track changes in sales over time.
- Discover important business trends automatically.
- Download filtered records for additional analysis.

## 🚀 Key Features

### 1. 🎯 Executive Overview

Displays essential business performance indicators, including:

- Total Revenue from Sales
- Total Profit Earned
- Total Number of Orders
- Total Number of Customers
- Total Units Sold
- Overall Profit Margin
- Average Order Value
- Average Quantity per Order
- Average Profit per Order
- Month-over-Month Sales Growth
- Month-over-Month Profit Growth

### 2. 🌎 Business Performance Analysis

Provides an overview of business results using:

- Monthly Revenue Analysis
- Monthly Profit Analysis
- Sales Comparison by Category
- Profit Comparison by Category
- Regional Sales Analysis
- Regional Profit Analysis
- Highest-Selling Cities
- Detailed Regional Performance Reports

### 3. 📦 Product Analytics

Helps evaluate individual products and product categories through:

- Top 10 Products Based on Sales
- Top 10 Products Based on Profit
- Bottom 10 Products Based on Sales
- Comparison of Product Sales and Profit
- Category and Sub-Category Performance
- Detailed Product Performance Reports

### 4. 👥 Customer Analytics

Analyzes customer contribution and purchasing patterns through:

- Top 10 Customers by Revenue
- Customer-Level Sales and Profit Comparison
- Customer Segment Analysis
- Sales Distribution Across Customer Segments
- Profit Distribution Across Customer Segments
- Detailed Customer Performance Reports

### 5. 🧠 Automated Business Insights

Generates useful summaries from the available sales information, such as:

- Best-Performing Product Category
- Highest-Performing Region
- Leading Product by Sales
- Most Recent Monthly Sales Growth
- Overall Business Profit Margin
- Category-Level Performance Trends
- Regional Business Comparisons

### 6. 🔎 Dynamic Data Filters

Users can customize their analysis by selecting different filter options:

- 📅 Order Date Range
- 🌎 Sales Region
- 🛍️ Product Category
- 👥 Customer Segment

The dashboard recalculates relevant metrics and refreshes its visualizations based on the selected filters.

### 7. 📥 Filtered Data Download

The application allows users to export the selected sales records into a CSV file.

This functionality supports further data exploration, reporting, and analysis using external tools.

## 🛠️ Technologies Used

| Technology | Application |
|---|---|
| Python | Implements the dashboard logic and application features |
| Pandas | Cleans, transforms, and analyzes sales data |
| Plotly | Creates interactive charts and graphs |
| Streamlit | Builds the interactive web dashboard |
| CSV | Stores and manages the sales dataset |
| Git | Tracks source code changes |
| GitHub | Hosts the project repository |

## 📂 Project Directory Structure

```text
Sales_Analytics_Dashboard/
│
├── app.py
│
├── data/
│   └── sales_dashboard_dataset.csv
│
├── pages/
│   ├── 1_Executive_Overview.py
│   ├── 2_Business_Performance.py
│   ├── 3_Product_Analytics.py
│   ├── 4_Customer_Analytics.py
│   └── 5_Business_Insights.py
│
├── utils/
│   ├── data_loader.py
│   └── filters.py
│
├── assets/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 📊 Dataset Information

The application works with a synthetic dataset consisting of **5,000 sales transactions**.

The dataset contains fields related to orders, customers, products, pricing, profitability, and shipping details, including:

- Order ID
- Order Date
- Shipping Date
- Customer ID
- Customer Name
- Salesperson
- Customer Segment
- Region
- State
- City
- Product Category
- Product Sub-Category
- Product Name
- Quantity
- Unit Price
- Discount
- Sales Amount
- Cost
- Profit
- Shipping Duration in Days
- Profit Margin
- Order Month
- Order Year

## ⚙️ Installation and Execution

Use the following instructions to set up and launch the application on your computer.

### Step 1: Download the Repository

Clone the project from GitHub using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Sales_Analytics_Dashboard
```

### Step 3: Set Up a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Enable the Virtual Environment

For Windows users:

```bash
.venv\Scripts\activate
```

### Step 5: Install the Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Launch the Dashboard

```bash
streamlit run app.py
```

Once the application starts, open the local web address shown in the terminal to explore the dashboard.

## 📈 Application Workflow

The dashboard processes sales information through the following stages:

```text
Sales Transaction Dataset
          ↓
       Data Import
          ↓
   Data Preparation
          ↓
    Filter Selection
          ↓
    KPI Computation
          ↓
 Interactive Charts
          ↓
 Performance Evaluation
          ↓
  Business Insight Generation
          ↓
    CSV Data Export
```

## 💡 Business Benefits

This application supports business analysis by helping users:

- Recognize products generating strong sales.
- Measure revenue and profitability.
- Evaluate customer value and contribution.
- Understand differences in regional performance.
- Monitor monthly sales fluctuations.
- Discover products and customers contributing to profit.
- Make informed decisions using data.
- Prepare customized reports using exported records.

## 🔮 Future Enhancements

The platform can be expanded with additional analytical capabilities, including:

- Predictive sales analysis using machine learning.
- Customer churn identification.
- Product demand estimation.
- Detection of unusual sales patterns.
- Integration with live databases.
- User authentication and access permissions.
- Scheduled email-based reports.
- Map-based regional sales visualization.
- Cloud-based data storage and processing.

## 👩‍💻 Project Developer

**Sudulaguntla Sri Bhramarambica**

B.Tech in Computer Science and Engineering

**Project Title:** Sales Analytics Dashboard

## ⭐ Project Summary

The Sales Analytics Dashboard is a data-driven business intelligence application that combines Python-based data analysis with interactive visualizations. It brings together sales monitoring, profitability analysis, product and customer evaluation, regional comparisons, automated business insights, and downloadable reports in one platform.
