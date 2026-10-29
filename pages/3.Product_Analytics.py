import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.filters import apply_filters


st.set_page_config(
    page_title="Product Analytics",
    page_icon="📦",
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

st.title("📦 Product Analytics")

st.markdown(
    """
    **Product Performance Intelligence**

    Identify top-performing products, profitable products,
    low-performing products, and category-level opportunities.
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
# PRODUCT DATA
# =========================================================

product_data = (
    filtered_df
    .groupby("Product_Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)


# =========================================================
# TOP & BOTTOM PRODUCTS
# =========================================================

st.subheader("🏆 Top & Bottom Products")


# =========================================================
# TOP 10 PRODUCTS BY SALES
# =========================================================

top_products = (
    product_data
    .sort_values(
        "Sales",
        ascending=False
    )
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


# =========================================================
# TOP 10 PRODUCTS BY PROFIT
# =========================================================

top_profit_products = (
    product_data
    .sort_values(
        "Profit",
        ascending=False
    )
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


# =========================================================
# BOTTOM 10 PRODUCTS BY SALES
# =========================================================

bottom_products = (
    product_data
    .sort_values(
        "Sales",
        ascending=True
    )
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


# =========================================================
# PRODUCT PROFITABILITY
# =========================================================

st.divider()

st.subheader("💡 Product Profitability Analysis")

st.markdown(
    """
    Compare product revenue against profitability to identify
    products that generate strong sales and healthy profits.
    """
)


fig_profitability = px.scatter(
    product_data,
    x="Sales",
    y="Profit",
    size="Quantity",
    hover_name="Product_Name",
    title="Sales vs Profit by Product",
    labels={
        "Sales": "Sales ($)",
        "Profit": "Profit ($)",
        "Quantity": "Quantity Sold"
    }
)


fig_profitability.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Profit ($)"
)


st.plotly_chart(
    fig_profitability,
    use_container_width=True
)


# =========================================================
# CATEGORY VS SUB-CATEGORY
# =========================================================

st.divider()

st.subheader("📊 Category vs Sub-Category Performance")


category_product = (
    filtered_df
    .groupby(
        ["Category", "Sub_Category"],
        as_index=False
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)


fig_category_product = px.treemap(
    category_product,
    path=[
        "Category",
        "Sub_Category"
    ],
    values="Sales",
    color="Profit",
    title="Sales Distribution by Category and Sub-Category"
)


st.plotly_chart(
    fig_category_product,
    use_container_width=True
)


# =========================================================
# PRODUCT PERFORMANCE TABLE
# =========================================================

st.divider()

st.subheader("📋 Product Performance Details")


product_display = (
    product_data
    .sort_values(
        "Sales",
        ascending=False
    )
    .copy()
)


product_display["Sales"] = product_display["Sales"].map(
    lambda x: f"${x:,.2f}"
)


product_display["Profit"] = product_display["Profit"].map(
    lambda x: f"${x:,.2f}"
)


st.dataframe(
    product_display,
    use_container_width=True,
    hide_index=True
)
