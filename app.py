
import streamlit as st

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Sales Analytics Dashboard")

st.markdown("""
Welcome to the Sales Analytics Dashboard!

Explore your sales data, monitor business performance,
analyze products and customers, and discover useful business insights.
""")

st.divider()

st.subheader("Dashboard Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📈 Executive Overview
    - Total sales and profit
    - Total orders and customers
    - Key performance indicators
    - Monthly sales trends

    ### 🏢 Business Performance
    - Regional performance
    - Category and segment analysis
    - Sales and profit comparisons
    """)

with col2:
    st.markdown("""
    ### 🛍️ Product Analytics
    - Best-selling products
    - Product category analysis
    - Quantity and profit comparisons

    ### 👥 Customer Analytics
    - Customer purchasing behavior
    - Top customers
    - Customer sales analysis

    ### 💡 Business Insights
    - Sales trends
    - Profitability analysis
    - Business recommendations
    """)

st.divider()

st.info(
    "Select a page from the sidebar to explore the dashboard."
)

st.caption("Built with Python, Pandas, Plotly and Streamlit.")
