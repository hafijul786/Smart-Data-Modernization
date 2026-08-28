import streamlit as st
import pandas as pd
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Data Modernization",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    /* ===== Smart Data Modernization - Premium UI ===== */
    .stApp { background: #08111f; }
    [data-testid="stAppViewContainer"] { background: #08111f; }
    [data-testid="stHeader"] { background: rgba(8,17,31,0.92); }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg,#0d1728 0%,#09111f 100%);
        border-right: 1px solid #24324a;
    }
    section[data-testid="stSidebar"] > div { padding-top: 1.1rem; }
    section[data-testid="stSidebar"] * { color: #e6edf7; }
    .brand {
        padding: 8px 4px 18px 4px;
        border-bottom: 1px solid #263650;
        margin-bottom: 18px;
    }
    .brand-name { font-size: 23px; font-weight: 800; letter-spacing: -.5px; }
    .brand-sub { color:#8fa3bd; font-size:12px; margin-top:4px; }
    .topbar {
        display:flex; align-items:center; justify-content:space-between;
        padding:18px 22px; margin:0 0 24px 0;
        background: linear-gradient(135deg,#101d32,#0c1728);
        border:1px solid #263650; border-radius:18px;
        box-shadow:0 12px 35px rgba(0,0,0,.22);
    }
    .top-title { font-size:26px; font-weight:800; color:#f8fafc; }
    .top-sub { font-size:13px; color:#91a4bd; margin-top:4px; }
    .top-status {
        padding:7px 12px; border:1px solid #28553f; border-radius:999px;
        background:#0e2a20; color:#8ce3b1; font-size:12px; font-weight:700;
    }
    .page-head { margin: 4px 0 20px 0; }
    .page-title { font-size:34px; font-weight:800; color:#f8fafc; letter-spacing:-.8px; }
    .page-desc { color:#91a4bd; font-size:14px; margin-top:5px; }
    .section-card {
        background:#0f1b2d; border:1px solid #24344e; border-radius:16px;
        padding:18px 20px; margin:10px 0 18px 0;
    }
    div[data-testid="stMetric"] {
        background:linear-gradient(145deg,#111f34,#0d192b);
        border:1px solid #263650; border-radius:14px; padding:16px 17px;
        box-shadow:0 8px 22px rgba(0,0,0,.16);
    }
    div[data-testid="stMetric"] label { color:#91a4bd; font-size:12px; }
    div[data-testid="stMetricValue"] { color:#f8fafc; font-weight:800; }
    .stButton > button { border-radius:10px; border:1px solid #30415c; background:#132139; }
    .stButton > button:hover { border-color:#6b7f9e; transform:translateY(-1px); }
    div[data-testid="stDataFrame"] { border:1px solid #263650; border-radius:12px; overflow:hidden; }
    .footer {
        margin-top:58px; padding:30px; border-radius:20px;
        background:linear-gradient(135deg,#0f1c30,#0a1424);
        border:1px solid #263650; box-shadow:0 -8px 30px rgba(0,0,0,.18);
    }
    .footer-grid { display:grid; grid-template-columns:1.5fr 1fr 1fr; gap:28px; }
    .footer-brand { font-size:21px; font-weight:800; color:#f8fafc; }
    .footer-heading { font-size:12px; text-transform:uppercase; letter-spacing:1px; color:#a7b7ca; font-weight:800; margin-bottom:10px; }
    .footer-text { color:#8195ae; font-size:13px; line-height:1.7; }
    .footer-pill { display:inline-block; padding:6px 10px; margin:3px; border:1px solid #30415c; border-radius:999px; color:#b8c6d8; font-size:11px; }
    .footer-bottom { margin-top:24px; padding-top:17px; border-top:1px solid #263650; color:#687d98; font-size:11px; display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; }
    @media (max-width: 800px) { .footer-grid { grid-template-columns:1fr; } .top-status { display:none; } .page-title { font-size:28px; } }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MAIN DATA
# ============================================================

@st.cache_data
def load_data():

    file_path = "data/cleaned_superstore.csv"

    if not os.path.exists(file_path):
        return None

    data = pd.read_csv(file_path)

    data["order_date"] = pd.to_datetime(
        data["order_date"],
        errors="coerce"
    )

    data["ship_date"] = pd.to_datetime(
        data["ship_date"],
        errors="coerce"
    )

    # Make sure numeric columns are numeric
    for col in [
        "sales",
        "profit",
        "quantity",
        "discount",
        "shipping_cost",
        "shipping_days"
    ]:

        if col in data.columns:
            data[col] = pd.to_numeric(
                data[col],
                errors="coerce"
            )

    return data


df = load_data()


# ============================================================
# DATA FILE CHECK
# ============================================================

if df is None:

    st.error(
        "cleaned_superstore.csv not found inside the data folder."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div class="brand">
        <div class="brand-name">📊 Smart Data</div>
        <div class="brand-sub">Modernization & Intelligence Platform</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

st.sidebar.subheader("🧭 Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "📊 Executive Dashboard",
        "📈 Sales Analytics",
        "👥 Customer Intelligence",
        "🤖 ML Analytics",
        "🚨 Anomaly Detection",
        "💡 Business Insights",
        "⚙️ Data Quality"
    ]
)

st.sidebar.divider()


# ============================================================
# GLOBAL FILTERS
# ============================================================

st.sidebar.subheader("🔎 Global Filters")

years = sorted(
    df["year"].dropna().unique().tolist()
)

selected_years = st.sidebar.multiselect(
    "Year",
    years,
    default=years
)


categories = sorted(
    df["category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)


regions = sorted(
    df["region"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    df["year"].isin(selected_years)
    &
    df["category"].isin(selected_categories)
    &
    df["region"].isin(selected_regions)
].copy()

# ============================================================
# APPLICATION TOP BAR
# ============================================================

st.markdown(
    """
    <div class="topbar">
        <div>
            <div class="top-title">Smart Data Modernization</div>
            <div class="top-sub">Enterprise Analytics • Customer Intelligence • Machine Learning</div>
        </div>
        <div class="top-status">● SYSTEM ONLINE</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def show_kpis(data):

    total_sales = data["sales"].sum()

    total_profit = data["profit"].sum()

    total_quantity = data["quantity"].sum()

    total_orders = data["order_id"].nunique()

    if total_sales != 0:
        profit_margin = (
            total_profit / total_sales
        ) * 100
    else:
        profit_margin = 0

    if "shipping_days" in data.columns:
        avg_shipping_days = (
            data["shipping_days"].mean()
        )
    else:
        avg_shipping_days = 0

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "💰 Total Sales",
        f"${total_sales:,.0f}"
    )

    col2.metric(
        "📈 Total Profit",
        f"${total_profit:,.0f}"
    )

    col3.metric(
        "📦 Quantity",
        f"{total_quantity:,.0f}"
    )

    col4.metric(
        "🛒 Orders",
        f"{total_orders:,}"
    )

    col5.metric(
        "📊 Profit Margin",
        f"{profit_margin:.2f}%"
    )


# ============================================================
# EMPTY FILTER CHECK
# ============================================================

if len(filtered_df) == 0:

    st.warning(
        "No records found for the selected filters."
    )

    st.stop()


# ============================================================
# PAGE 1
# EXECUTIVE DASHBOARD
# ============================================================

if page == "📊 Executive Dashboard":

    st.markdown(
        '<div class="main-title">📊 Smart Data Modernization</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Interactive Executive Business Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    show_kpis(filtered_df)

    st.divider()

    # --------------------------------------------------------
    # YEARLY SALES
    # --------------------------------------------------------

    st.subheader(
        "📈 Yearly Sales Performance"
    )

    yearly_sales = (
        filtered_df
        .groupby("year")["sales"]
        .sum()
    )

    st.line_chart(
        yearly_sales
    )

    st.divider()

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    with col1:

        st.subheader(
            "📦 Category Sales & Profit"
        )

        category_data = (
            filtered_df
            .groupby("category")[
                ["sales", "profit"]
            ]
            .sum()
        )

        st.bar_chart(
            category_data
        )

    # --------------------------------------------------------
    # REGION
    # --------------------------------------------------------

    with col2:

        st.subheader(
            "🌍 Regional Profit"
        )

        region_profit = (
            filtered_df
            .groupby("region")["profit"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        st.bar_chart(
            region_profit
        )

    st.divider()

    # --------------------------------------------------------
    # TOP CUSTOMERS
    # --------------------------------------------------------

    st.subheader(
        "🏆 Top 10 Customers by Profit"
    )

    top_customers = (
        filtered_df
        .groupby("customer_name")["profit"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    st.bar_chart(
        top_customers
    )


# ============================================================
# PAGE 2
# SALES ANALYTICS
# ============================================================

elif page == "📈 Sales Analytics":

    st.title(
        "📈 Sales Analytics"
    )

    st.caption(
        "Detailed sales, product and shipping analysis"
    )

    st.divider()

    show_kpis(filtered_df)

    st.divider()

    # --------------------------------------------------------
    # MONTHLY SALES
    # --------------------------------------------------------

    st.subheader(
        "📅 Monthly Sales Trend"
    )

    monthly_sales = (
        filtered_df
        .groupby(
            filtered_df[
                "order_date"
            ].dt.to_period("M")
        )["sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["order_date"] = (
        monthly_sales["order_date"]
        .dt.to_timestamp()
    )

    monthly_sales[
        "3_Month_Moving_Average"
    ] = (
        monthly_sales["sales"]
        .rolling(
            window=3
        )
        .mean()
    )

    monthly_chart = (
        monthly_sales
        .set_index("order_date")[
            [
                "sales",
                "3_Month_Moving_Average"
            ]
        ]
    )

    st.line_chart(
        monthly_chart
    )

    st.divider()

    # --------------------------------------------------------
    # CATEGORY ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "📦 Category Analysis"
    )

    category_analysis = (
        filtered_df
        .groupby("category")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
    )

    category_analysis[
        "Profit_Margin_%"
    ] = (
        category_analysis[
            "Total_Profit"
        ]
        /
        category_analysis[
            "Total_Sales"
        ]
        * 100
    )

    category_analysis = (
        category_analysis
        .round(2)
        .sort_values(
            "Total_Sales",
            ascending=False
        )
    )

    st.dataframe(
        category_analysis,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # REGION ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "🌍 Region Analysis"
    )

    region_analysis = (
        filtered_df
        .groupby("region")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
    )

    region_analysis[
        "Profit_Margin_%"
    ] = (
        region_analysis[
            "Total_Profit"
        ]
        /
        region_analysis[
            "Total_Sales"
        ]
        * 100
    )

    st.dataframe(
        region_analysis
        .round(2)
        .sort_values(
            "Total_Profit",
            ascending=False
        ),
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # SHIPPING
    # --------------------------------------------------------

    st.subheader(
        "🚚 Shipping Mode Performance"
    )

    shipping_data = (
        filtered_df
        .groupby("ship_mode")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Average_Shipping_Days=(
                "shipping_days",
                "mean"
            ),
            Total_Orders=(
                "order_id",
                "nunique"
            )
        )
        .sort_values(
            "Total_Sales",
            ascending=False
        )
        .round(2)
    )

    st.dataframe(
        shipping_data,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # LOSS MAKING SUB-CATEGORIES
    # --------------------------------------------------------

    st.subheader(
        "⚠️ Loss-Making Sub-Categories"
    )

    subcategory_profit = (
        filtered_df
        .groupby("sub_category")[
            "profit"
        ]
        .sum()
        .sort_values()
    )

    loss_making = (
        subcategory_profit[
            subcategory_profit < 0
        ]
    )

    if len(loss_making) > 0:

        st.warning(
            f"{len(loss_making)} "
            "sub-category(s) are loss-making."
        )

        st.dataframe(
            loss_making.to_frame(
                "Total Profit"
            ),
            use_container_width=True
        )

    else:

        st.success(
            "No loss-making sub-category "
            "found for the selected filters."
        )


# ============================================================
# PAGE 3
# CUSTOMER INTELLIGENCE
# ============================================================

elif page == "👥 Customer Intelligence":

    st.title(
        "👥 Customer Intelligence"
    )

    st.caption(
        "RFM segmentation, customer risk and clustering"
    )

    st.divider()

    # ========================================================
    # RFM
    # ========================================================

    rfm_file = (
        "data/rfm_customer_segments.csv"
    )

    if os.path.exists(rfm_file):

        rfm_df = pd.read_csv(
            rfm_file
        )

        st.subheader(
            "🎯 RFM Customer Segmentation"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Customers",
            f"{len(rfm_df):,}"
        )

        champions = (
            rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == "Champions"
            ]
        )

        at_risk = (
            rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == "At Risk"
            ]
        )

        col2.metric(
            "🏆 Champions",
            f"{len(champions):,}"
        )

        col3.metric(
            "⚠️ At Risk",
            f"{len(at_risk):,}"
        )

        st.write(
            "### Customer Segment Distribution"
        )

        segment_counts = (
            rfm_df[
                "Customer_Segment"
            ]
            .value_counts()
        )

        st.bar_chart(
            segment_counts
        )

        selected_segment = st.selectbox(
            "Select Customer Segment",
            ["All"]
            +
            sorted(
                rfm_df[
                    "Customer_Segment"
                ].dropna().unique()
            )
        )

        if selected_segment == "All":

            rfm_display = rfm_df

        else:

            rfm_display = rfm_df[
                rfm_df[
                    "Customer_Segment"
                ]
                == selected_segment
            ]

        st.write(
            "### Customer Details"
        )

        rfm_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "RFM_Score",
            "Customer_Segment"
        ]

        available_rfm_columns = [
            col
            for col in rfm_columns
            if col in rfm_display.columns
        ]

        st.dataframe(
            rfm_display[
                available_rfm_columns
            ]
            .sort_values(
                "Monetary",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.info(
            "RFM data not found."
        )

    st.divider()

    # ========================================================
    # CUSTOMER RISK
    # ========================================================

    risk_file = (
        "data/customer_risk_predictions.csv"
    )

    if os.path.exists(risk_file):

        risk_df = pd.read_csv(
            risk_file
        )

        st.subheader(
            "⚠️ Customer Risk Prediction"
        )

        high_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "High Risk"
            ].shape[0]
        )

        medium_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "Medium Risk"
            ].shape[0]
        )

        low_risk = (
            risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == "Low Risk"
            ].shape[0]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🔴 High Risk",
            f"{high_risk:,}"
        )

        col2.metric(
            "🟡 Medium Risk",
            f"{medium_risk:,}"
        )

        col3.metric(
            "🟢 Low Risk",
            f"{low_risk:,}"
        )

        risk_counts = (
            risk_df[
                "Predicted_Risk"
            ]
            .value_counts()
        )

        st.bar_chart(
            risk_counts
        )

        selected_risk = st.selectbox(
            "Filter Risk Level",
            [
                "All",
                "High Risk",
                "Medium Risk",
                "Low Risk"
            ]
        )

        if selected_risk == "All":

            risk_display = risk_df

        else:

            risk_display = risk_df[
                risk_df[
                    "Predicted_Risk"
                ]
                == selected_risk
            ]

        risk_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "Customer_Segment",
            "Predicted_Risk"
        ]

        available_risk_columns = [
            col
            for col in risk_columns
            if col in risk_display.columns
        ]

        st.dataframe(
            risk_display[
                available_risk_columns
            ]
            .sort_values(
                "Monetary",
                ascending=False
            ),
            use_container_width=True
        )

    else:

        st.info(
            "Customer risk predictions not found."
        )

    st.divider()

    # ========================================================
    # CUSTOMER CLUSTERING
    # ========================================================

    cluster_file = (
        "data/customer_clusters.csv"
    )

    if os.path.exists(cluster_file):

        cluster_df = pd.read_csv(
            cluster_file
        )

        st.subheader(
            "🧠 Customer Clustering"
        )

        cluster_counts = (
            cluster_df[
                "Customer_Cluster"
            ]
            .value_counts()
            .sort_index()
        )

        st.bar_chart(
            cluster_counts
        )

        cluster_summary = (
            cluster_df
            .groupby(
                "Customer_Cluster"
            )
            .agg(
                Customers=(
                    "customer_name",
                    "count"
                ),
                Avg_Recency=(
                    "Recency",
                    "mean"
                ),
                Avg_Frequency=(
                    "Frequency",
                    "mean"
                ),
                Avg_Monetary=(
                    "Monetary",
                    "mean"
                )
            )
            .round(2)
        )

        st.write(
            "### Cluster Summary"
        )

        st.dataframe(
            cluster_summary,
            use_container_width=True
        )

        selected_cluster = st.selectbox(
            "Select Customer Cluster",
            [
                "All",
                0,
                1,
                2
            ]
        )

        if selected_cluster == "All":

            cluster_display = cluster_df

        else:

            cluster_display = cluster_df[
                cluster_df[
                    "Customer_Cluster"
                ]
                == selected_cluster
            ]

        cluster_columns = [
            "customer_name",
            "Recency",
            "Frequency",
            "Monetary",
            "Customer_Segment",
            "Customer_Cluster"
        ]

        available_cluster_columns = [
            col
            for col in cluster_columns
            if col in cluster_display.columns
        ]

        st.dataframe(
            cluster_display[
                available_cluster_columns
            ],
            use_container_width=True
        )

    else:

        st.info(
            "Customer clustering data not found."
        )


# ============================================================
# PAGE 4
# MACHINE LEARNING
# ============================================================

elif page == "🤖 ML Analytics":

    st.title(
        "🤖 Machine Learning Analytics"
    )

    st.caption(
        "Predictive modelling and forecasting"
    )

    st.divider()

    # ========================================================
    # SALES PREDICTION
    # ========================================================

    prediction_file = (
        "data/sales_predictions.csv"
    )

    st.subheader(
        "📈 Sales Prediction"
    )

    if os.path.exists(prediction_file):

        prediction_df = pd.read_csv(
            prediction_file
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "MAE",
            "85.38"
        )

        col2.metric(
            "RMSE",
            "251.88"
        )

        col3.metric(
            "R² Score",
            "0.7219"
        )

        st.info(
            "Model: Random Forest Regressor | "
            "Training: 2011–2013 | "
            "Testing: 2014"
        )

        st.write(
            "### Actual vs Predicted Sales"
        )

        if (
            "Actual_Sales" in prediction_df.columns
            and
            "Predicted_Sales" in prediction_df.columns
        ):

            st.scatter_chart(
                prediction_df,
                x="Actual_Sales",
                y="Predicted_Sales"
            )

        st.write(
            "### Prediction Sample"
        )

        st.dataframe(
            prediction_df.head(20),
            use_container_width=True
        )

    else:

        st.warning(
            "Sales prediction file not found."
        )

    st.divider()

    # ========================================================
    # SALES FORECAST
    # ========================================================

    forecast_file = (
        "data/sales_forecast.csv"
    )

    st.subheader(
        "🔮 Future Sales Forecast"
    )

    if os.path.exists(forecast_file):

        forecast_df = pd.read_csv(
            forecast_file
        )

        if "order_date" in forecast_df.columns:

            forecast_df[
                "order_date"
            ] = pd.to_datetime(
                forecast_df[
                    "order_date"
                ],
                errors="coerce"
            )

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        if (
            "order_date" in forecast_df.columns
            and
            "Forecasted_Sales" in forecast_df.columns
        ):

            st.line_chart(
                forecast_df.set_index(
                    "order_date"
                )[
                    "Forecasted_Sales"
                ]
            )

        st.caption(
            "Forecast generated by the sales forecasting module."
        )

    else:

        st.info(
            "Sales forecast file not found. "
            "Run sales_forecasting.py first."
        )


# ============================================================
# PAGE 5
# ANOMALY DETECTION
# ============================================================

elif page == "🚨 Anomaly Detection":

    st.title(
        "🚨 Business Anomaly Detection"
    )

    st.caption(
        "Identify unusual discounts, shipping costs and transactions"
    )

    st.divider()

    anomaly_file = (
        "data/anomalies.csv"
    )

    if os.path.exists(anomaly_file):

        anomaly_df = pd.read_csv(
            anomaly_file
        )

        total_anomalies = len(
            anomaly_df
        )

        discount_anomalies = 0

        shipping_anomalies = 0

        if "discount_anomaly" in anomaly_df.columns:

            discount_anomalies = int(
                anomaly_df[
                    "discount_anomaly"
                ].sum()
            )

        if "shipping_anomaly" in anomaly_df.columns:

            shipping_anomalies = int(
                anomaly_df[
                    "shipping_anomaly"
                ].sum()
            )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🚨 Anomalous Records",
            f"{total_anomalies:,}"
        )

        col2.metric(
            "🏷️ Discount Anomalies",
            f"{discount_anomalies:,}"
        )

        col3.metric(
            "🚚 Shipping Anomalies",
            f"{shipping_anomalies:,}"
        )

        st.divider()

        st.subheader(
            "🔎 Detected Anomalies"
        )

        available_columns = [
            col
            for col in [
                "order_id",
                "customer_name",
                "category",
                "sub_category",
                "sales",
                "discount",
                "profit",
                "shipping_cost",
                "anomaly_score"
            ]
            if col in anomaly_df.columns
        ]

        if "anomaly_score" in anomaly_df.columns:

            anomaly_display = (
                anomaly_df
                .sort_values(
                    "anomaly_score",
                    ascending=False
                )
            )

        else:

            anomaly_display = anomaly_df

        st.dataframe(
            anomaly_display[
                available_columns
            ],
            use_container_width=True
        )

        if "anomaly_score" in anomaly_df.columns:

            st.subheader(
                "🔥 Highest Priority Anomalies"
            )

            high_risk = anomaly_df[
                anomaly_df[
                    "anomaly_score"
                ] >= 2
            ]

            st.dataframe(
                high_risk[
                    [
                        col
                        for col in [
                            "order_id",
                            "category",
                            "sub_category",
                            "sales",
                            "discount",
                            "profit",
                            "shipping_cost",
                            "anomaly_score"
                        ]
                        if col in high_risk.columns
                    ]
                ].head(20),
                use_container_width=True
            )

    else:

        st.warning(
            "Anomaly data not found."
        )


# ============================================================
# PAGE 6
# BUSINESS INSIGHTS
# ============================================================

elif page == "💡 Business Insights":

    st.title(
        "💡 Business Intelligence"
    )

    st.caption(
        "Data-driven business insights from the selected filters"
    )

    st.divider()

    # --------------------------------------------------------
    # BEST CATEGORY
    # --------------------------------------------------------

    category_profit = (
        filtered_df
        .groupby("category")[
            "profit"
        ]
        .sum()
    )

    best_category = (
        category_profit
        .idxmax()
    )

    best_category_profit = (
        category_profit
        .max()
    )

    # --------------------------------------------------------
    # BEST REGION
    # --------------------------------------------------------

    region_profit = (
        filtered_df
        .groupby("region")[
            "profit"
        ]
        .sum()
    )

    best_region = (
        region_profit
        .idxmax()
    )

    best_region_profit = (
        region_profit
        .max()
    )

    # --------------------------------------------------------
    # BEST SHIPPING
    # --------------------------------------------------------

    shipping_sales = (
        filtered_df
        .groupby("ship_mode")[
            "sales"
        ]
        .sum()
    )

    best_shipping = (
        shipping_sales
        .idxmax()
    )

    # --------------------------------------------------------
    # LOSS MAKING
    # --------------------------------------------------------

    subcategory_profit = (
        filtered_df
        .groupby("sub_category")[
            "profit"
        ]
        .sum()
    )

    loss_making = (
        subcategory_profit[
            subcategory_profit < 0
        ]
        .sort_values()
    )

    # --------------------------------------------------------
    # INSIGHT CARDS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"🏆 Highest-profit category: "
            f"**{best_category}**"
        )

        st.write(
            f"Profit generated: "
            f"**${best_category_profit:,.2f}**"
        )

    with col2:

        st.info(
            f"🌍 Highest-profit region: "
            f"**{best_region}**"
        )

        st.write(
            f"Profit generated: "
            f"**${best_region_profit:,.2f}**"
        )

    st.divider()

    st.info(
        f"🚚 Highest-sales shipping mode: "
        f"**{best_shipping}**"
    )

    st.divider()

    # --------------------------------------------------------
    # LOSS MAKING PRODUCTS
    # --------------------------------------------------------

    st.subheader(
        "⚠️ Loss-Making Sub-Categories"
    )

    if len(loss_making) > 0:

        st.warning(
            f"{len(loss_making)} "
            "sub-category(s) are generating negative profit."
        )

        st.dataframe(
            loss_making.to_frame(
                "Total Profit"
            ),
            use_container_width=True
        )

    else:

        st.success(
            "No loss-making sub-category "
            "found for the selected filters."
        )

    st.divider()

    # --------------------------------------------------------
    # DISCOUNT ANALYSIS
    # --------------------------------------------------------

    st.subheader(
        "🏷️ Discount vs Profit"
    )

    discount_analysis = (
        filtered_df
        .groupby("discount")
        .agg(
            Total_Sales=(
                "sales",
                "sum"
            ),
            Total_Profit=(
                "profit",
                "sum"
            ),
            Total_Quantity=(
                "quantity",
                "sum"
            )
        )
        .sort_index()
    )

    st.dataframe(
        discount_analysis.round(2),
        use_container_width=True
    )

    st.line_chart(
        discount_analysis[
            [
                "Total_Profit"
            ]
        ]
    )


# ============================================================
# PAGE 7
# DATA QUALITY
# ============================================================

elif page == "⚙️ Data Quality":

    st.title(
        "⚙️ Data Quality & Validation"
    )

    st.caption(
        "Monitor dataset health before analytics and ML"
    )

    st.divider()

    total_rows = len(df)

    total_columns = len(
        df.columns
    )

    missing_values = int(
        df.isnull()
        .sum()
        .sum()
    )

    duplicate_rows = int(
        df.duplicated()
        .sum()
    )

    total_cells = (
        total_rows
        *
        total_columns
    )

    if total_cells > 0:

        completeness = (
            1
            -
            (
                missing_values
                /
                total_cells
            )
        ) * 100

    else:

        completeness = 100

    if total_rows > 0:

        duplicate_percentage = (
            duplicate_rows
            /
            total_rows
        ) * 100

    else:

        duplicate_percentage = 0

    quality_score = max(
        0,
        completeness
        -
        duplicate_percentage
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📄 Records",
        f"{total_rows:,}"
    )

    col2.metric(
        "📋 Columns",
        f"{total_columns:,}"
    )

    col3.metric(
        "❌ Missing Values",
        f"{missing_values:,}"
    )

    col4.metric(
        "⭐ Quality Score",
        f"{quality_score:.2f}%"
    )

    st.divider()

    # --------------------------------------------------------
    # DUPLICATES
    # --------------------------------------------------------

    if duplicate_rows == 0:

        st.success(
            "✅ No duplicate rows detected."
        )

    else:

        st.warning(
            f"⚠️ {duplicate_rows:,} duplicate "
            "rows detected."
        )

    # --------------------------------------------------------
    # COLUMN QUALITY
    # --------------------------------------------------------

    st.subheader(
        "📋 Column-Level Data Quality"
    )

    quality_data = []

    for column in df.columns:

        quality_data.append(
            {
                "Column": column,
                "Data Type": str(
                    df[column].dtype
                ),
                "Missing Values": int(
                    df[column].isnull().sum()
                ),
                "Unique Values": int(
                    df[column].nunique()
                )
            }
        )

    quality_df = pd.DataFrame(
        quality_data
    )

    st.dataframe(
        quality_df,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------------

    st.subheader(
        "👀 Dataset Preview"
    )

    rows_to_show = st.slider(
        "Rows to display",
        min_value=10,
        max_value=100,
        value=25
    )

    st.dataframe(
        df.head(rows_to_show),
        use_container_width=True
    )


# ============================================================
# PREMIUM PRODUCT FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <div class="footer-grid">
            <div>
                <div class="footer-brand">📊 Smart Data Modernization</div>
                <div class="footer-text" style="margin-top:10px;">
                    An end-to-end analytics platform that converts business data
                    into measurable insights, customer intelligence and predictive decisions.
                </div>
            </div>
            <div>
                <div class="footer-heading">Platform</div>
                <div class="footer-text">
                    Executive Analytics<br>
                    Sales Intelligence<br>
                    Customer Intelligence<br>
                    ML & Forecasting<br>
                    Anomaly Monitoring
                </div>
            </div>
            <div>
                <div class="footer-heading">Technology</div>
                <div>
                    <span class="footer-pill">Python</span>
                    <span class="footer-pill">Pandas</span>
                    <span class="footer-pill">Scikit-Learn</span>
                    <span class="footer-pill">Streamlit</span>
                    <span class="footer-pill">Machine Learning</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <span>Smart Data Modernization</span>
            <span>Data → Insights → Intelligence</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
