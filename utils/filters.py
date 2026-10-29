import streamlit as st


def apply_filters(df):

    # =====================================================
    # SIDEBAR HEADER
    # =====================================================

    st.sidebar.title("📊 Sales Analytics")

    st.sidebar.markdown(
        """
        **Dashboard Controls**

        Use the filters below to explore
        sales performance and business insights.
        """
    )

    st.sidebar.divider()

    st.sidebar.subheader("🔎 Filters")


    # =====================================================
    # DATE FILTER
    # =====================================================

    min_date = df["Order_Date"].min().date()
    max_date = df["Order_Date"].max().date()

    selected_dates = st.sidebar.date_input(
        "📅 Order Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )


    # =====================================================
    # REGION FILTER
    # =====================================================

    regions = sorted(
        df["Region"]
        .dropna()
        .unique()
    )

    selected_regions = st.sidebar.multiselect(
        "🌎 Region",
        regions,
        default=regions
    )


    # =====================================================
    # CATEGORY FILTER
    # =====================================================

    categories = sorted(
        df["Category"]
        .dropna()
        .unique()
    )

    selected_categories = st.sidebar.multiselect(
        "🛍️ Category",
        categories,
        default=categories
    )


    # =====================================================
    # SEGMENT FILTER
    # =====================================================

    segments = sorted(
        df["Segment"]
        .dropna()
        .unique()
    )

    selected_segments = st.sidebar.multiselect(
        "👥 Segment",
        segments,
        default=segments
    )


    # =====================================================
    # APPLY FILTERS
    # =====================================================

    filtered_df = df.copy()


    # Date filtering
    if len(selected_dates) == 2:

        start_date = selected_dates[0]
        end_date = selected_dates[1]

        filtered_df = filtered_df[
            (filtered_df["Order_Date"].dt.date >= start_date)
            &
            (filtered_df["Order_Date"].dt.date <= end_date)
        ]


    # Region filtering
    if selected_regions:

        filtered_df = filtered_df[
            filtered_df["Region"].isin(
                selected_regions
            )
        ]


    # Category filtering
    if selected_categories:

        filtered_df = filtered_df[
            filtered_df["Category"].isin(
                selected_categories
            )
        ]


    # Segment filtering
    if selected_segments:

        filtered_df = filtered_df[
            filtered_df["Segment"].isin(
                selected_segments
            )
        ]


    # =====================================================
    # FILTER SUMMARY
    # =====================================================

    st.sidebar.divider()

    st.sidebar.caption(
        f"📌 Showing {len(filtered_df):,} records"
    )


    # =====================================================
    # DOWNLOAD FILTERED DATA
    # =====================================================

    st.sidebar.divider()

    st.sidebar.subheader("📥 Export Data")

    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")


    st.sidebar.download_button(
        label="📥 Download Filtered CSV",
        data=csv_data,
        file_name="filtered_sales_data.csv",
        mime="text/csv"
    )


    return filtered_df
