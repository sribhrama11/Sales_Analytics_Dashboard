import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.filters import apply_filters


st.set_page_config(
    page_title="Business Performance",
    page_icon="🌎",
    layout="wide"
)


# =========================================================
# LOAD DATA & APPLY FILTERS
# =========================================================

df = load_data()

filtered_df = apply_filters(df)


# =========================================================
# PAGE HEADER
# =========================================================

st.title("🌎 Business Performance")

st.markdown(
    """
    **Sales, Profit & Regional Performance**

    Analyze revenue trends, profitability, categories,
    regional performance, and geographic sales distribution.
    """
)

st.divider()


# =========================================================
# EMPTY DATA CHECK
# =========================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No data available for the selected filters. "
        "Please change your filter selections."
    )

    st.stop()


# =========================================================
# SALES & PROFIT TRENDS
# =========================================================

st.subheader("📈 Sales & Profit Trends")


monthly_sales = (
    filtered_df
    .groupby("Order_Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)


monthly_sales["Month"] = pd.to_datetime(
    monthly_sales["Order_Month"]
)

monthly_sales = monthly_sales.sort_values("Month")


chart_col1, chart_col2 = st.columns(2)


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


# =========================================================
# CATEGORY PERFORMANCE
# =========================================================

st.divider()

st.subheader("🛍️ Category Performance")


category_data = (
    filtered_df
    .groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values(
        "Sales",
        ascending=False
    )
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


# =========================================================
# REGIONAL PERFORMANCE
# =========================================================

st.divider()

st.subheader("🌎 Regional Performance")


region_data = (
    filtered_df
    .groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values(
        "Sales",
        ascending=False
    )
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
        title="Profit by Region"
    )

    fig_region_profit.update_layout(
        xaxis_title="Region",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_region_profit,
        use_container_width=True
    )


# =========================================================
# GEOGRAPHIC SALES ANALYSIS
# =========================================================

st.divider()

st.subheader("📍 Geographic Sales Analysis")

st.markdown(
    """
    Explore sales concentration across cities and identify
    geographic areas contributing strongly to revenue.
    """
)


city_data = (
    filtered_df
    .groupby(
        ["City", "State"],
        as_index=False
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values(
        "Sales",
        ascending=False
    )
)


fig_city = px.bar(
    city_data.head(15).sort_values("Sales"),
    x="Sales",
    y="City",
    orientation="h",
    text_auto=".2s",
    hover_data=[
        "State",
        "Profit",
        "Orders"
    ],
    title="Top 15 Cities by Sales"
)


fig_city.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="City"
)


st.plotly_chart(
    fig_city,
    use_container_width=True
)


# =========================================================
# REGIONAL PERFORMANCE TABLE
# =========================================================

st.divider()

st.subheader("📋 Regional Performance Details")


region_display = region_data.copy()


region_display["Sales"] = region_display["Sales"].map(
    lambda x: f"${x:,.2f}"
)


region_display["Profit"] = region_display["Profit"].map(
    lambda x: f"${x:,.2f}"
)


st.dataframe(
    region_display,
    use_container_width=True,
    hide_index=True
)
