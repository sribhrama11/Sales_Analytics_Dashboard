import streamlit as st
import pandas as pd
import numpy as np

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Sales Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("📊 Sales Analytics Platform")

st.markdown(
    """
    **Executive Sales Intelligence Dashboard**

    Monitor revenue, profitability, customer performance,
    product performance, regional trends, and business growth
    through interactive analytics.
    """
)

st.divider()
# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/sales_dashboard_dataset.csv"
    )

    # Convert dates
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"]
    )

    df["Ship_Date"] = pd.to_datetime(
        df["Ship_Date"]
    )

    return df


df = load_data()

# ==========================================================
# DATA CLEANING
# ==========================================================

df = df.drop_duplicates()

df = df.dropna(
    subset=[
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Sales",
        "Profit"
    ]
)

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit",
    "Shipping_Days",
    "Profit_Margin"
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.title("📊 Sales Analytics")

st.sidebar.markdown(
    """
    ### Dashboard Controls
    Use the filters below to explore sales performance.
    """
)

st.sidebar.divider()

st.sidebar.subheader("🔎 Filters")
st.sidebar.divider()

st.sidebar.markdown("### ℹ️ About")

st.sidebar.info(
    """
    **Sales Analytics Platform**

    An interactive business intelligence
    dashboard developed using:

    • Python  
    • Pandas  
    • Plotly  
    • Streamlit  

    Designed for sales performance
    monitoring and business decision-making.
    """
)
# ----------------------------------------------------------
# DATE FILTER
# ----------------------------------------------------------

min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

date_range = st.sidebar.date_input(
    "📅 Order Date",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# ----------------------------------------------------------
# REGION FILTER
# ----------------------------------------------------------

regions = sorted(
    df["Region"].unique()
)

selected_regions = st.sidebar.multiselect(
    "🌎 Region",
    options=regions,
    default=regions
)

# ----------------------------------------------------------
# CATEGORY FILTER
# ----------------------------------------------------------

categories = sorted(
    df["Category"].unique()
)

selected_categories = st.sidebar.multiselect(
    "🏷️ Category",
    options=categories,
    default=categories
)

# ----------------------------------------------------------
# SEGMENT FILTER
# ----------------------------------------------------------

segments = sorted(
    df["Segment"].unique()
)

selected_segments = st.sidebar.multiselect(
    "👥 Customer Segment",
    options=segments,
    default=segments
)

# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = df.copy()

# ----------------------------------------------------------
# DATE FILTER
# ----------------------------------------------------------

if len(date_range) == 2:

    start_date = pd.to_datetime(
        date_range[0]
    )

    end_date = pd.to_datetime(
        date_range[1]
    )

    filtered_df = filtered_df[
        (filtered_df["Order_Date"] >= start_date)
        &
        (filtered_df["Order_Date"] <= end_date)
    ]

# ----------------------------------------------------------
# REGION FILTER
# ----------------------------------------------------------

if selected_regions:

    filtered_df = filtered_df[
        filtered_df["Region"].isin(
            selected_regions
        )
    ]

# ----------------------------------------------------------
# CATEGORY FILTER
# ----------------------------------------------------------

if selected_categories:

    filtered_df = filtered_df[
        filtered_df["Category"].isin(
            selected_categories
        )
    ]

# ----------------------------------------------------------
# SEGMENT FILTER
# ----------------------------------------------------------

if selected_segments:

    filtered_df = filtered_df[
        filtered_df["Segment"].isin(
            selected_segments
        )
    ]

# ==========================================================
# CALCULATE KPIs
# ==========================================================
st.subheader("🎯 Executive Overview")
total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_quantity = filtered_df["Quantity"].sum()
# Advanced business KPIs
average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

average_quantity_per_order = (
    total_quantity / total_orders
    if total_orders > 0
    else 0
)

profit_per_order = (
    total_profit / total_orders
    if total_orders > 0
    else 0
)

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)
st.markdown("### 📊 Advanced Business Metrics")

adv1, adv2, adv3 = st.columns(3)

with adv1:
    st.metric(
        "💵 Average Order Value",
        f"${average_order_value:,.2f}"
    )

with adv2:
    st.metric(
        "📦 Avg Quantity / Order",
        f"{average_quantity_per_order:,.2f}"
    )

with adv3:
    st.metric(
        "💰 Profit / Order",
        f"${profit_per_order:,.2f}"
    )
# ==========================================================
# HEADER
# ==========================================================

st.title(
    "📊 Sales Analytics Dashboard"
)

st.markdown(
    "### Sales Performance & Business Intelligence Platform"
)

st.divider()

# ==========================================================
# FILTER STATUS
# ==========================================================

st.info(
    f"Showing {len(filtered_df):,} records "
    f"based on the selected filters."
)

# ==========================================================
# KPI SECTION
# ==========================================================

st.subheader(
    "📈 Key Business Metrics"
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:

    st.metric(
        "Total Sales",
        f"${total_sales:,.0f}"
    )

with col2:

    st.metric(
        "Total Profit",
        f"${total_profit:,.0f}"
    )

with col3:

    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )

with col4:

    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

with col5:

    st.metric(
        "Quantity Sold",
        f"{total_quantity:,}"
    )

with col6:

    st.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )

# ==========================================================
# DATA PREVIEW
# ==========================================================
# ==========================================================
# SALES & PROFIT TRENDS
# ==========================================================
st.subheader("📈 Sales & Profit Trends")
import plotly.express as px

st.divider()

st.subheader("📊 Sales & Profit Trends")

# ----------------------------------------------------------
# CREATE MONTHLY SUMMARY
# ----------------------------------------------------------

monthly_sales = (
    filtered_df
    .groupby("Order_Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# Convert month into a proper date
monthly_sales["Month"] = pd.to_datetime(
    monthly_sales["Order_Month"]
)

monthly_sales = monthly_sales.sort_values(
    "Month"
)

# ==========================================================
# TWO-COLUMN CHART LAYOUT
# ==========================================================
st.subheader("🌎 Business Performance")
chart_col1, chart_col2 = st.columns(2)

# ==========================================================
# MONTHLY SALES
# ==========================================================

with chart_col1:

    st.markdown("#### 📈 Monthly Sales")

    fig_sales = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig_sales.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)",
        hovermode="x unified"
    )

    fig_sales.update_traces(
        hovertemplate="$%{y:,.2f}<extra></extra>"
    )

    st.plotly_chart(
        fig_sales,
        use_container_width=True
    )

# ==========================================================
# MONTHLY PROFIT
# ==========================================================

with chart_col2:

    st.markdown("#### 💰 Monthly Profit")

    fig_profit = px.line(
        monthly_sales,
        x="Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    fig_profit.update_layout(
        xaxis_title="Month",
        yaxis_title="Profit ($)",
        hovermode="x unified"
    )

    fig_profit.update_traces(
        hovertemplate="$%{y:,.2f}<extra></extra>"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )
    st.divider()
st.subheader("📈 Growth Analysis")

growth_data = (
    filtered_df
    .groupby("Order_Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

growth_data["Month"] = pd.to_datetime(growth_data["Order_Month"])
growth_data = growth_data.sort_values("Month")

# Calculate month-over-month growth
growth_data["Sales_Growth"] = (
    growth_data["Sales"]
    .pct_change()
    .fillna(0)
    * 100
)

growth_data["Profit_Growth"] = (
    growth_data["Profit"]
    .pct_change()
    .fillna(0)
    * 100
)

st.markdown("#### 📈 Monthly Sales Growth")

fig_growth = px.bar(
    growth_data,
    x="Month",
    y="Sales_Growth",
    text_auto=".1f",
    title="Month-over-Month Sales Growth"
)

fig_growth.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales Growth (%)"
)

st.plotly_chart(
    fig_growth,
    use_container_width=True
)
st.markdown("#### 📋 Monthly Growth Details")

growth_display = growth_data[
    ["Month", "Sales", "Profit", "Sales_Growth", "Profit_Growth"]
].copy()

growth_display["Sales"] = growth_display["Sales"].map(
    lambda x: f"${x:,.2f}"
)

growth_display["Profit"] = growth_display["Profit"].map(
    lambda x: f"${x:,.2f}"
)

growth_display["Sales_Growth"] = growth_display["Sales_Growth"].map(
    lambda x: f"{x:.2f}%"
)

growth_display["Profit_Growth"] = growth_display["Profit_Growth"].map(
    lambda x: f"{x:.2f}%"
)

st.dataframe(
    growth_display,
    use_container_width=True
)
st.divider()
st.subheader("📊 Category & Regional Performance")

# Category-wise performance
category_data = (
    filtered_df
    .groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🛍️ Sales by Category")

    fig_category = px.bar(
        category_data,
        x="Category",
        y="Sales",
        text_auto=".2s",
        title="Category-wise Sales"
    )

    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales ($)"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with col2:
    st.markdown("#### 💰 Profit by Category")

    fig_category_profit = px.bar(
        category_data,
        x="Category",
        y="Profit",
        text_auto=".2s",
        title="Category-wise Profit"
    )

    fig_category_profit.update_layout(
        xaxis_title="Category",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_category_profit,
        use_container_width=True
    )
# Region-wise performance
region_data = (
    filtered_df
    .groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### 🌎 Sales by Region")

    fig_region = px.bar(
        region_data,
        x="Region",
        y="Sales",
        text_auto=".2s",
        title="Region-wise Sales"
    )

    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales ($)"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

with col4:
    st.markdown("#### 📈 Profit by Region")

    fig_region_profit = px.bar(
        region_data,
        x="Region",
        y="Profit",
        text_auto=".2s",
        title="Region-wise Profit"
    )

    fig_region_profit.update_layout(
        xaxis_title="Region",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_region_profit,
        use_container_width=True
    )
    st.divider()
st.subheader("🏆 Product Performance")

# Product-wise performance
st.subheader("📦 Product Analytics")
product_data = (
    filtered_df
    .groupby("Product_Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

# Top 10 products by sales
top_products = (
    product_data
    .sort_values("Sales", ascending=False)
    .head(10)
)

st.markdown("#### 🏆 Top 10 Products by Sales")

fig_top_products = px.bar(
    top_products.sort_values("Sales"),
    x="Sales",
    y="Product_Name",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Products by Revenue"
)

fig_top_products.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Product"
)

st.plotly_chart(
    fig_top_products,
    use_container_width=True
)
# Top 10 products by profit
top_profit_products = (
    product_data
    .sort_values("Profit", ascending=False)
    .head(10)
)

st.markdown("#### 💰 Top 10 Products by Profit")

fig_top_profit = px.bar(
    top_profit_products.sort_values("Profit"),
    x="Profit",
    y="Product_Name",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Most Profitable Products"
)

fig_top_profit.update_layout(
    xaxis_title="Profit ($)",
    yaxis_title="Product"
)

st.plotly_chart(
    fig_top_profit,
    use_container_width=True
)
# Bottom 10 products by sales
bottom_products = (
    product_data
    .sort_values("Sales", ascending=True)
    .head(10)
)

st.markdown("#### ⚠️ Bottom 10 Products by Sales")

fig_bottom_products = px.bar(
    bottom_products,
    x="Sales",
    y="Product_Name",
    orientation="h",
    text_auto=".2s",
    title="Bottom 10 Products by Revenue"
)

fig_bottom_products.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Product"
)

st.plotly_chart(
    fig_bottom_products,
    use_container_width=True
)
st.markdown("#### 📦 Category vs Product Performance")

category_product = (
    filtered_df
    .groupby(["Category", "Sub_Category"], as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

fig_category_product = px.treemap(
    category_product,
    path=["Category", "Sub_Category"],
    values="Sales",
    color="Profit",
    title="Sales Distribution by Category and Sub-Category"
)

st.plotly_chart(
    fig_category_product,
    use_container_width=True
)
st.divider()
st.subheader("👥 Customer Analytics")

# Customer-wise performance
customer_data = (
    filtered_df
    .groupby(["Customer_ID", "Customer_Name"], as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
)

# Top 10 customers by sales
top_customers = (
    customer_data
    .sort_values("Sales", ascending=False)
    .head(10)
)

st.markdown("#### 🏆 Top 10 Customers by Sales")

fig_customers = px.bar(
    top_customers.sort_values("Sales"),
    x="Sales",
    y="Customer_Name",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Customers by Revenue"
)

fig_customers.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Customer"
)

st.plotly_chart(
    fig_customers,
    use_container_width=True
)
# Segment-wise performance
segment_data = (
    filtered_df
    .groupby("Segment", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 👥 Sales by Customer Segment")

    fig_segment_sales = px.pie(
        segment_data,
        names="Segment",
        values="Sales",
        title="Revenue Distribution by Segment",
        hole=0.4
    )

    st.plotly_chart(
        fig_segment_sales,
        use_container_width=True
    )

with col2:
    st.markdown("#### 💰 Profit by Customer Segment")

    fig_segment_profit = px.bar(
        segment_data,
        x="Segment",
        y="Profit",
        text_auto=".2s",
        title="Profit by Customer Segment"
    )

    fig_segment_profit.update_layout(
        xaxis_title="Segment",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_segment_profit,
        use_container_width=True
    )
    st.divider()
st.subheader("🧠 Automated Business Insights")

# Calculate key insights
st.subheader("🧠 Business Intelligence")
best_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

best_category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .max()
)

best_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

best_region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .max()
)

best_product = (
    filtered_df.groupby("Product_Name")["Sales"]
    .sum()
    .idxmax()
)

best_product_sales = (
    filtered_df.groupby("Product_Name")["Sales"]
    .sum()
    .max()
)
# Overall growth
if len(growth_data) >= 2:
    latest_sales = growth_data.iloc[-1]["Sales"]
    previous_sales = growth_data.iloc[-2]["Sales"]

    if previous_sales != 0:
        latest_growth = (
            (latest_sales - previous_sales)
            / previous_sales
        ) * 100
    else:
        latest_growth = 0
else:
    latest_growth = 0
insight_col1, insight_col2 = st.columns(2)

with insight_col1:

    st.info(
        f"🏆 **Top Category:** {best_category} "
        f"generated ${best_category_sales:,.2f} in sales."
    )

    st.success(
        f"🌎 **Top Region:** {best_region} "
        f"generated ${best_region_sales:,.2f} in sales."
    )

    st.warning(
        f"📦 **Top Product:** {best_product} "
        f"generated ${best_product_sales:,.2f} in sales."
    )


with insight_col2:

    if latest_growth > 0:

        st.success(
            f"📈 **Sales Growth:** Sales increased by "
            f"{latest_growth:.2f}% compared with the previous month."
        )

    elif latest_growth < 0:

        st.error(
            f"📉 **Sales Decline:** Sales decreased by "
            f"{abs(latest_growth):.2f}% compared with the previous month."
        )

    else:

        st.info(
            "➡️ **Sales Trend:** Sales remained stable "
            "compared with the previous month."
        )

    st.info(
        f"💰 **Profit Margin:** "
        f"{profit_margin:.2f}% of sales are retained as profit."
    )
# ==========================================================
# FILTERED DATA
# ==========================================================

st.divider()

st.subheader("📋 Filtered Sales Data")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)
