import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.filters import apply_filters


st.set_page_config(
    page_title="Customer Analytics",
    page_icon="👥",
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

st.title("👥 Customer Analytics")

st.markdown(
    """
    **Customer Performance Intelligence**

    Understand customer contribution, purchasing behavior,
    profitability, and segment-level performance.
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
# CUSTOMER ANALYSIS
# =========================================================

customer_data = (
    filtered_df
    .groupby(
        ["Customer_ID", "Customer_Name"],
        as_index=False
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
)


# =========================================================
# TOP CUSTOMERS
# =========================================================

st.subheader("🏆 Top Customers")


top_customers = (
    customer_data
    .sort_values(
        "Sales",
        ascending=False
    )
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


# =========================================================
# CUSTOMER VALUE ANALYSIS
# =========================================================

st.divider()

st.subheader("💎 Customer Value Analysis")

st.markdown(
    """
    Compare customer revenue and profitability to identify
    high-value customers and potential business opportunities.
    """
)


fig_customer_value = px.scatter(
    customer_data,
    x="Sales",
    y="Profit",
    size="Orders",
    hover_name="Customer_Name",
    title="Customer Sales vs Profit",
    labels={
        "Sales": "Sales ($)",
        "Profit": "Profit ($)",
        "Orders": "Number of Orders"
    }
)


fig_customer_value.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Profit ($)"
)


st.plotly_chart(
    fig_customer_value,
    use_container_width=True
)


# =========================================================
# CUSTOMER SEGMENT ANALYSIS
# =========================================================

st.divider()

st.subheader("👥 Customer Segment Analysis")


segment_data = (
    filtered_df
    .groupby(
        "Segment",
        as_index=False
    )
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


# =========================================================
# CUSTOMER PERFORMANCE TABLE
# =========================================================

st.divider()

st.subheader("📋 Customer Performance Details")


customer_display = (
    customer_data
    .sort_values(
        "Sales",
        ascending=False
    )
    .copy()
)


customer_display["Sales"] = customer_display["Sales"].map(
    lambda x: f"${x:,.2f}"
)


customer_display["Profit"] = customer_display["Profit"].map(
    lambda x: f"${x:,.2f}"
)


st.dataframe(
    customer_display,
    use_container_width=True,
    hide_index=True
)
