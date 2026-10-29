import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.filters import apply_filters


st.set_page_config(
    page_title="Executive Overview",
    page_icon="🎯",
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

st.title("🎯 Executive Overview")

st.markdown(
    """
    **Executive Sales Intelligence**

    Monitor revenue, profitability, orders, customers,
    and key business performance indicators.
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
# BASIC KPIs
# =========================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_quantity = filtered_df["Quantity"].sum()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales > 0
    else 0
)


# =========================================================
# ADVANCED KPIs
# =========================================================

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


# =========================================================
# KPI SECTION
# =========================================================

st.subheader("🎯 Key Performance Indicators")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "💵 Total Sales",
        f"${total_sales:,.2f}"
    )


with col2:

    st.metric(
        "💰 Total Profit",
        f"${total_profit:,.2f}"
    )


with col3:

    st.metric(
        "🧾 Total Orders",
        f"{total_orders:,}"
    )


col4, col5, col6 = st.columns(3)


with col4:

    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )


with col5:

    st.metric(
        "📦 Quantity Sold",
        f"{total_quantity:,}"
    )


with col6:

    st.metric(
        "📊 Profit Margin",
        f"{profit_margin:.2f}%"
    )


# =========================================================
# ADVANCED KPI SECTION
# =========================================================

st.divider()

st.subheader("📌 Advanced Business KPIs")


col7, col8, col9 = st.columns(3)


with col7:

    st.metric(
        "🛒 Average Order Value",
        f"${average_order_value:,.2f}"
    )


with col8:

    st.metric(
        "📦 Avg Quantity / Order",
        f"{average_quantity_per_order:.2f}"
    )


with col9:

    st.metric(
        "💰 Profit / Order",
        f"${profit_per_order:,.2f}"
    )


# =========================================================
# MONTHLY GROWTH
# =========================================================

st.divider()

st.subheader("📈 Business Growth")


monthly_data = (
    filtered_df
    .groupby("Order_Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)


monthly_data["Month"] = pd.to_datetime(
    monthly_data["Order_Month"]
)


monthly_data = monthly_data.sort_values(
    "Month"
)


monthly_data["Sales_Growth"] = (
    monthly_data["Sales"]
    .pct_change()
    * 100
)


monthly_data["Profit_Growth"] = (
    monthly_data["Profit"]
    .pct_change()
    * 100
)


# =========================================================
# LATEST GROWTH
# =========================================================

latest_sales_growth = 0
latest_profit_growth = 0


if len(monthly_data) >= 2:

    latest_sales_growth = (
        monthly_data.iloc[-1]["Sales_Growth"]
    )

    latest_profit_growth = (
        monthly_data.iloc[-1]["Profit_Growth"]
    )


growth_col1, growth_col2 = st.columns(2)


with growth_col1:

    if pd.notna(latest_sales_growth):

        st.metric(
            "📈 Latest Monthly Sales Growth",
            f"{latest_sales_growth:.2f}%"
        )

    else:

        st.metric(
            "📈 Latest Monthly Sales Growth",
            "N/A"
        )


with growth_col2:

    if pd.notna(latest_profit_growth):

        st.metric(
            "💰 Latest Monthly Profit Growth",
            f"{latest_profit_growth:.2f}%"
        )

    else:

        st.metric(
            "💰 Latest Monthly Profit Growth",
            "N/A"
        )


# =========================================================
# MONTHLY PERFORMANCE TABLE
# =========================================================

st.divider()

st.subheader("📋 Monthly Performance")


monthly_display = monthly_data.copy()


monthly_display["Month"] = (
    monthly_display["Month"]
    .dt.strftime("%Y-%m")
)


monthly_display["Sales"] = (
    monthly_display["Sales"]
    .map(lambda x: f"${x:,.2f}")
)


monthly_display["Profit"] = (
    monthly_display["Profit"]
    .map(lambda x: f"${x:,.2f}")
)


monthly_display["Sales_Growth"] = (
    monthly_display["Sales_Growth"]
    .map(
        lambda x:
        f"{x:.2f}%"
        if pd.notna(x)
        else "N/A"
    )
)


monthly_display["Profit_Growth"] = (
    monthly_display["Profit_Growth"]
    .map(
        lambda x:
        f"{x:.2f}%"
        if pd.notna(x)
        else "N/A"
    )
)


st.dataframe(
    monthly_display[
        [
            "Month",
            "Sales",
            "Profit",
            "Sales_Growth",
            "Profit_Growth"
        ]
    ],
    use_container_width=True,
    hide_index=True
)
