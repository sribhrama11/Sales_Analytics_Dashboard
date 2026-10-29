import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.filters import apply_filters


st.set_page_config(
    page_title="Business Insights",
    page_icon="🧠",
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

st.title("🧠 Business Insights")

st.markdown(
    """
    **Automated Business Intelligence**

    Key findings generated from sales, profit,
    product, customer, and regional performance.
    """
)

st.divider()


# =========================================================
# CHECK FILTERED DATA
# =========================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No data available for the selected filters. "
        "Please change your filter selections."
    )

    st.stop()


# =========================================================
# BASIC CALCULATIONS
# =========================================================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales > 0
    else 0
)


# =========================================================
# TOP CATEGORY
# =========================================================

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()


# =========================================================
# TOP REGION
# =========================================================

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_region = region_sales.idxmax()
best_region_sales = region_sales.max()


# =========================================================
# TOP PRODUCT
# =========================================================

product_sales = (
    filtered_df
    .groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()


# =========================================================
# MONTHLY GROWTH
# =========================================================

growth_data = (
    filtered_df
    .groupby("Order_Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

growth_data["Month"] = pd.to_datetime(
    growth_data["Order_Month"]
)

growth_data = growth_data.sort_values("Month")

growth_data["Sales_Growth"] = (
    growth_data["Sales"]
    .pct_change()
    .fillna(0)
    * 100
)


# =========================================================
# EXECUTIVE INSIGHTS
# =========================================================

st.subheader("📊 Executive Insights")


col1, col2 = st.columns(2)


with col1:

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


with col2:

    latest_growth = 0

    if len(growth_data) >= 2:

        latest_sales = growth_data.iloc[-1]["Sales"]
        previous_sales = growth_data.iloc[-2]["Sales"]

        if previous_sales != 0:

            latest_growth = (
                (latest_sales - previous_sales)
                / previous_sales
            ) * 100


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


# =========================================================
# CATEGORY PERFORMANCE
# =========================================================

st.divider()

st.subheader("🏆 Category Performance")


category_table = (
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


st.dataframe(
    category_table,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# REGIONAL PERFORMANCE
# =========================================================

st.subheader("🌎 Regional Performance")


region_table = (
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


st.dataframe(
    region_table,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# FILTERED DATA SUMMARY
# =========================================================

st.divider()

st.subheader("📌 Current Analysis Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)


with summary_col1:

    st.metric(
        "Filtered Records",
        f"{len(filtered_df):,}"
    )


with summary_col2:

    st.metric(
        "Filtered Sales",
        f"${total_sales:,.2f}"
    )


with summary_col3:

    st.metric(
        "Filtered Profit",
        f"${total_profit:,.2f}"
    )
