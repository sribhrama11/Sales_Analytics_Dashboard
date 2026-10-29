import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/sales_dashboard_dataset.csv"
    )

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"]
    )

    df["Ship_Date"] = pd.to_datetime(
        df["Ship_Date"]
    )

    return df
