import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart Data Modernization",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_superstore.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    return df


df = load_data()

# ==========================================
# TITLE
# ==========================================

st.title("📊 Smart Data Modernization")
st.markdown(
    "### End-to-End Business Analytics Dashboard"
)

st.divider()

# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("🔎 Filters")

years = sorted(df["year"].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

categories = sorted(df["category"].unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

regions = sorted(df["region"].unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

# ==========================================
# FILTER DATA
# ==========================================

filtered_df = df[
    (df["year"].isin(selected_years)) &
    (df["category"].isin(selected_categories)) &
    (df["region"].isin(selected_regions))
]

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_quantity = filtered_df["quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)

avg_shipping_days = filtered_df["shipping_days"].mean()

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Quantity",
    f"{total_quantity:,}"
)

col4.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

col5.metric(
    "Avg Shipping Days",
    f"{avg_shipping_days:.2f}"
)

st.divider()

# ==========================================
# YEARLY SALES
# ==========================================

st.subheader("📈 Yearly Sales Trend")

yearly_sales = (
    filtered_df
    .groupby("year")["sales"]
    .sum()
)

st.line_chart(yearly_sales)

# ==========================================
# CATEGORY ANALYSIS
# ==========================================

st.subheader("📦 Category Performance")

category_data = (
    filtered_df
    .groupby("category")[["sales", "profit"]]
    .sum()
)

st.bar_chart(category_data)

# ==========================================
# REGION ANALYSIS
# ==========================================

st.subheader("🌍 Regional Profit")

region_profit = (
    filtered_df
    .groupby("region")["profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_profit)

# ==========================================
# SHIPPING MODE
# ==========================================

st.subheader("🚚 Shipping Mode Performance")

shipping_data = (
    filtered_df
    .groupby("ship_mode")
    .agg(
        Total_Sales=("sales", "sum"),
        Total_Profit=("profit", "sum"),
        Average_Shipping_Days=("shipping_days", "mean"),
        Total_Orders=("order_id", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

st.dataframe(
    shipping_data,
    use_container_width=True
)

# ==========================================
# TOP CUSTOMERS
# ==========================================

st.subheader("🏆 Top 10 Customers by Profit")

top_customers = (
    filtered_df
    .groupby("customer_name")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_customers)

# ==========================================
# TABLES LOSS ANALYSIS
# ==========================================

st.subheader("⚠️ Loss-Making Sub-Categories")

subcategory_profit = (
    filtered_df
    .groupby("sub_category")["profit"]
    .sum()
    .sort_values()
)

loss_making = subcategory_profit[subcategory_profit < 0]

if len(loss_making) > 0:

    st.dataframe(
        loss_making.to_frame("Total Profit"),
        use_container_width=True
    )

    st.warning(
        f"{len(loss_making)} sub-category(s) are currently loss-making."
    )

else:

    st.success(
        "No loss-making sub-category found for the selected filters."
    )

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

st.subheader("💡 Business Insights")

if len(filtered_df) > 0:

    best_category = (
        filtered_df.groupby("category")["profit"]
        .sum()
        .idxmax()
    )

    best_region = (
        filtered_df.groupby("region")["profit"]
        .sum()
        .idxmax()
    )

    best_shipping = (
        filtered_df.groupby("ship_mode")["sales"]
        .sum()
        .idxmax()
    )

    st.write(
        f"• Highest-profit category: **{best_category}**"
    )

    st.write(
        f"• Highest-profit region: **{best_region}**"
    )

    st.write(
        f"• Highest-sales shipping mode: **{best_shipping}**"
    )

# ==========================================
# DATA PREVIEW
# ==========================================

st.subheader("📋 Filtered Dataset Preview")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Smart Data Modernization | Python • SQL • Pandas • Streamlit"
)

# ==========================================
# MONTHLY SALES TREND
# ==========================================

st.subheader("📊 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(filtered_df["order_date"].dt.to_period("M"))["sales"]
    .sum()
    .reset_index()
)

monthly_sales["order_date"] = monthly_sales["order_date"].dt.to_timestamp()

monthly_sales["3_Month_Moving_Average"] = (
    monthly_sales["sales"]
    .rolling(window=3)
    .mean()
)

monthly_chart = monthly_sales.set_index("order_date")[
    ["sales", "3_Month_Moving_Average"]
]

st.line_chart(monthly_chart)

st.caption(
    "The 3-month moving average helps identify the underlying sales trend."
)

# ==========================================
# RFM CUSTOMER SEGMENTATION
# ==========================================

st.subheader("👥 Customer Segmentation (RFM Analysis)")

rfm_file = "data/rfm_customer_segments.csv"

try:
    rfm_df = pd.read_csv(rfm_file)

    # Segment summary
    segment_summary = (
        rfm_df["Customer_Segment"]
        .value_counts()
        .reset_index()
    )

    segment_summary.columns = [
        "Customer_Segment",
        "Customers"
    ]

    # --------------------------------------
    # Segment Distribution
    # --------------------------------------

    st.write("### Customer Segment Distribution")

    st.bar_chart(
        segment_summary.set_index("Customer_Segment")
    )

    # --------------------------------------
    # Segment Filter
    # --------------------------------------

    segments = sorted(
        rfm_df["Customer_Segment"].unique()
    )

    selected_segment = st.selectbox(
        "Select Customer Segment",
        ["All"] + segments
    )

    if selected_segment != "All":

        filtered_rfm = rfm_df[
            rfm_df["Customer_Segment"] == selected_segment
        ]

    else:

        filtered_rfm = rfm_df

    # --------------------------------------
    # Customer Table
    # --------------------------------------

    st.write("### Customer Details")

    st.dataframe(
        filtered_rfm[
            [
                "customer_name",
                "Recency",
                "Frequency",
                "Monetary",
                "RFM_Score",
                "Customer_Segment"
            ]
        ].sort_values(
            "Monetary",
            ascending=False
        ),
        use_container_width=True
    )

    # --------------------------------------
    # Key Metrics
    # --------------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Customers",
        len(rfm_df)
    )

    col2.metric(
        "Champions",
        len(
            rfm_df[
                rfm_df["Customer_Segment"]
                == "Champions"
            ]
        )
    )

    col3.metric(
        "At Risk",
        len(
            rfm_df[
                rfm_df["Customer_Segment"]
                == "At Risk"
            ]
        )
    )

except FileNotFoundError:

    st.warning(
        "RFM data not found. Run rfm_analysis.py first."
    )

    # ==========================================
# ANOMALY DETECTION
# ==========================================

st.subheader("🚨 Business Anomaly Detection")

anomaly_file = "data/anomalies.csv"

try:
    anomaly_df = pd.read_csv(anomaly_file)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Anomalous Records",
        len(anomaly_df)
    )

    col2.metric(
        "High Discount Cases",
        int(anomaly_df["discount_anomaly"].sum())
    )

    col3.metric(
        "Shipping Cost Anomalies",
        int(anomaly_df["shipping_anomaly"].sum())
    )

    # --------------------------------------
    # Anomaly Table
    # --------------------------------------

    st.write("### Detected Anomalies")

    st.dataframe(
        anomaly_df[
            [
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
        ].sort_values(
            "anomaly_score",
            ascending=False
        ),
        use_container_width=True
    )

    # --------------------------------------
    # Highest Risk Records
    # --------------------------------------

    st.write("### Highest Priority Anomalies")

    high_risk = anomaly_df[
        anomaly_df["anomaly_score"] >= 2
    ]

    st.dataframe(
        high_risk[
            [
                "order_id",
                "category",
                "sub_category",
                "sales",
                "discount",
                "profit",
                "shipping_cost",
                "anomaly_score"
            ]
        ].head(20),
        use_container_width=True
    )

except FileNotFoundError:

    st.warning(
        "Anomaly data not found. "
        "Run anomaly_detection.py first."
    )

    # ==========================================
# MACHINE LEARNING - SALES PREDICTION
# ==========================================

st.subheader("🤖 Machine Learning - Sales Prediction")

prediction_file = "data/sales_predictions.csv"

try:
    prediction_df = pd.read_csv(prediction_file)

    # Model Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("MAE", "85.38")
    col2.metric("RMSE", "251.88")
    col3.metric("R² Score", "0.7219")

    st.write("### Actual vs Predicted Sales")

    st.scatter_chart(
        prediction_df,
        x="Actual_Sales",
        y="Predicted_Sales"
    )

    st.write("### Sample Predictions")

    st.dataframe(
        prediction_df.head(20),
        use_container_width=True
    )

    st.info(
        "Model: Random Forest Regressor | "
        "Training Period: 2011–2013 | "
        "Testing Period: 2014"
    )

except FileNotFoundError:

    st.warning(
        "Sales prediction file not found. "
        "Run sales_prediction_model.py first."
    )

    # ==========================================
# CUSTOMER RISK PREDICTION
# ==========================================

st.subheader("⚠️ Customer Risk Analysis")

risk_file = "data/customer_risk_predictions.csv"

try:
    risk_df = pd.read_csv(risk_file)

    # --------------------------------------
    # KEY METRICS
    # --------------------------------------

    high_risk = (risk_df["Predicted_Risk"] == "High Risk").sum()
    medium_risk = (risk_df["Predicted_Risk"] == "Medium Risk").sum()
    low_risk = (risk_df["Predicted_Risk"] == "Low Risk").sum()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🔴 High Risk",
        high_risk
    )

    col2.metric(
        "🟡 Medium Risk",
        medium_risk
    )

    col3.metric(
        "🟢 Low Risk",
        low_risk
    )

    # --------------------------------------
    # RISK DISTRIBUTION
    # --------------------------------------

    st.write("### Risk Distribution")

    risk_summary = (
        risk_df["Predicted_Risk"]
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "Risk_Level",
        "Customers"
    ]

    st.bar_chart(
        risk_summary.set_index("Risk_Level")
    )

    # --------------------------------------
    # FILTER
    # --------------------------------------

    selected_risk = st.selectbox(
        "Select Risk Level",
        ["All", "High Risk", "Medium Risk", "Low Risk"]
    )

    if selected_risk != "All":

        filtered_risk = risk_df[
            risk_df["Predicted_Risk"] == selected_risk
        ]

    else:

        filtered_risk = risk_df

    # --------------------------------------
    # CUSTOMER DETAILS
    # --------------------------------------

    st.write("### Customer Risk Details")

    st.dataframe(
        filtered_risk[
            [
                "customer_name",
                "Recency",
                "Frequency",
                "Monetary",
                "Customer_Segment",
                "Predicted_Risk"
            ]
        ].sort_values(
            "Monetary",
            ascending=False
        ),
        use_container_width=True
    )

except FileNotFoundError:

    st.warning(
        "Customer risk data not found. "
        "Run customer_risk_model.py first."
    )


    # ==========================================
# CUSTOMER CLUSTERING
# ==========================================

st.subheader("🧠 Customer Clustering")

cluster_file = "data/customer_clusters.csv"

try:
    cluster_df = pd.read_csv(cluster_file)

    # Cluster counts
    cluster_counts = (
        cluster_df["Customer_Cluster"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    cluster_counts.columns = [
        "Cluster",
        "Customers"
    ]

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Cluster 0",
        int((cluster_df["Customer_Cluster"] == 0).sum())
    )

    col2.metric(
        "Cluster 1",
        int((cluster_df["Customer_Cluster"] == 1).sum())
    )

    col3.metric(
        "Cluster 2",
        int((cluster_df["Customer_Cluster"] == 2).sum())
    )

    # Distribution
    st.write("### Customer Cluster Distribution")

    st.bar_chart(
        cluster_counts.set_index("Cluster")
    )

    # Cluster summary
    st.write("### Cluster Summary")

    cluster_summary = (
        cluster_df.groupby("Customer_Cluster")
        .agg(
            Customers=("customer_name", "count"),
            Avg_Recency=("Recency", "mean"),
            Avg_Frequency=("Frequency", "mean"),
            Avg_Monetary=("Monetary", "mean")
        )
        .round(2)
    )

    st.dataframe(
        cluster_summary,
        use_container_width=True
    )

    # Customer details
    st.write("### Customer Cluster Details")

    selected_cluster = st.selectbox(
        "Select Cluster",
        ["All", 0, 1, 2]
    )

    if selected_cluster == "All":
        filtered_clusters = cluster_df
    else:
        filtered_clusters = cluster_df[
            cluster_df["Customer_Cluster"] == selected_cluster
        ]

    st.dataframe(
        filtered_clusters[
            [
                "customer_name",
                "Recency",
                "Frequency",
                "Monetary",
                "Customer_Segment",
                "Customer_Cluster"
            ]
        ],
        use_container_width=True
    )

except FileNotFoundError:

    st.warning(
        "Customer clustering file not found. "
        "Run customer_clustering.py first."
    )