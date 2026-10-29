# Sales_Analytics_Dashboard
Sales data analysis and visualization project using Power BI
📌 Project Overview
The Sales Analytics Platform is an interactive business intelligence dashboard developed using Python, Pandas, Plotly, and Streamlit.

The platform transforms transactional sales data into meaningful visual insights that help users understand revenue, profitability, product performance, customer behavior, regional performance, and business growth.

🎯 Project Objective
The objective of this project is to build an interactive sales analytics platform that converts raw sales data into actionable business insights.

The dashboard helps users:

Monitor overall sales performance
Track profitability
Analyze product performance
Understand customer contribution
Compare regional performance
Identify sales trends
Generate automated business insights
Export filtered data for further analysis
🚀 Key Features
🎯 Executive Overview
Provides high-level business KPIs including:

Total Sales
Total Profit
Total Orders
Customers
Quantity Sold
Profit Margin
Average Order Value
Average Quantity per Order
Profit per Order
Monthly Sales Growth
Monthly Profit Growth
🌎 Business Performance
Provides detailed business analysis through:

Monthly Sales Trends
Monthly Profit Trends
Category-wise Sales
Category-wise Profit
Region-wise Sales
Region-wise Profit
Top Cities by Sales
Regional Performance Table
📦 Product Analytics
Provides product-level analysis including:

Top 10 Products by Sales
Top 10 Products by Profit
Bottom 10 Products by Sales
Product Sales vs Profit Analysis
Category vs Sub-Category Analysis
Product Performance Table
👥 Customer Analytics
Provides customer intelligence through:

Top 10 Customers by Sales
Customer Sales vs Profit Analysis
Customer Segment Analysis
Segment-wise Sales
Segment-wise Profit
Customer Performance Table
🧠 Business Insights
Automatically generates insights such as:

Top-performing Category
Top-performing Region
Top-performing Product
Latest Monthly Sales Growth
Profit Margin
Category Performance
Regional Performance
🔎 Interactive Filters
The dashboard supports interactive filtering based on:

📅 Order Date
🌎 Region
🛍️ Category
👥 Customer Segment
All analytical calculations update according to the selected filters.

📥 Data Export
Users can download the currently filtered dataset as a CSV file.

This allows business users to perform additional analysis or reporting outside the dashboard.

🛠️ Technology Stack
Technology	Purpose
Python	Application development
Pandas	Data processing and analysis
Plotly	Interactive visualizations
Streamlit	Dashboard development
CSV	Dataset storage
Git & GitHub	Version control and project hosting
📂 Project Structure
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
📊 Dataset
The project uses a synthetic sales dataset containing transactional information such as:

Order ID
Order Date
Ship Date
Customer ID
Customer Name
Salesperson
Segment
Region
State
City
Category
Sub-Category
Product Name
Quantity
Unit Price
Discount
Sales
Cost
Profit
Shipping Days
Profit Margin
Order Month
Order Year
The dataset contains 5,000 sales records.

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Navigate to the project
cd Sales_Analytics_Dashboard
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows:

.venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Run the application
streamlit run app.py
📈 Dashboard Workflow
Raw Sales Dataset
        ↓
Data Loading
        ↓
Data Processing
        ↓
Interactive Filters
        ↓
KPI Calculation
        ↓
Data Visualization
        ↓
Business Analysis
        ↓
Automated Insights
        ↓
Filtered Data Export
💡 Business Value
The platform can help business users:

Identify high-performing products
Monitor revenue and profit
Understand customer contribution
Compare regional performance
Detect changes in monthly sales
Identify profitable products and customers
Support data-driven decision-making
Export filtered information for reporting
🔮 Future Scope
Possible future improvements include:

Machine learning-based sales forecasting
Customer churn prediction
Product demand forecasting
Anomaly detection
Real-time database integration
Role-based dashboard access
Automated email reports
Advanced geographic mapping
Cloud database integration
👩‍💻 Developed By
Sudulaguntla Sri Bhramarambica

B.Tech – Computer Science and Engineering

Sales Analytics Internship Project

⭐ Project Highlights
An end-to-end interactive Sales Analytics Platform built with Python, Pandas, Plotly, and Streamlit to transform transactional data into actionable business intelligence.
