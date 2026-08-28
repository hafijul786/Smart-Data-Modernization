import pandas as pd

# ==========================================
# LOAD CLEANED DATA
# ==========================================

df = pd.read_csv("data/cleaned_superstore.csv")

# ==========================================
# PROFIT ANOMALIES
# ==========================================

profit_q1 = df["profit"].quantile(0.25)
profit_q3 = df["profit"].quantile(0.75)

profit_iqr = profit_q3 - profit_q1

lower_profit = profit_q1 - 1.5 * profit_iqr
upper_profit = profit_q3 + 1.5 * profit_iqr

df["profit_anomaly"] = (
    (df["profit"] < lower_profit) |
    (df["profit"] > upper_profit)
)

# ==========================================
# SHIPPING COST ANOMALIES
# ==========================================

shipping_q1 = df["shipping_cost"].quantile(0.25)
shipping_q3 = df["shipping_cost"].quantile(0.75)

shipping_iqr = shipping_q3 - shipping_q1

upper_shipping = shipping_q3 + 1.5 * shipping_iqr

df["shipping_anomaly"] = (
    df["shipping_cost"] > upper_shipping
)

# ==========================================
# DISCOUNT ANOMALIES
# ==========================================

discount_q1 = df["discount"].quantile(0.25)
discount_q3 = df["discount"].quantile(0.75)

discount_iqr = discount_q3 - discount_q1

upper_discount = discount_q3 + 1.5 * discount_iqr

df["discount_anomaly"] = (
    df["discount"] > upper_discount
)

# ==========================================
# OVERALL ANOMALY
# ==========================================

df["is_anomaly"] = (
    df["profit_anomaly"] |
    df["shipping_anomaly"] |
    df["discount_anomaly"]
)

# ==========================================
# SUMMARY
# ==========================================

print("\n========== ANOMALY DETECTION ==========")

print(
    "Total Records:",
    len(df)
)

print(
    "Profit Anomalies:",
    df["profit_anomaly"].sum()
)

print(
    "Shipping Cost Anomalies:",
    df["shipping_anomaly"].sum()
)

print(
    "Discount Anomalies:",
    df["discount_anomaly"].sum()
)

print(
    "Total Anomalous Records:",
    df["is_anomaly"].sum()
)

# ==========================================
# TOP ANOMALOUS RECORDS
# ==========================================

anomalies = df[df["is_anomaly"]].copy()

anomalies["anomaly_score"] = (
    anomalies["profit_anomaly"].astype(int)
    + anomalies["shipping_anomaly"].astype(int)
    + anomalies["discount_anomaly"].astype(int)
)

print("\n========== TOP ANOMALOUS RECORDS ==========")

print(
    anomalies.sort_values(
        "anomaly_score",
        ascending=False
    )[
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
    ].head(10)
)

# ==========================================
# SAVE
# ==========================================

anomalies.to_csv(
    "data/anomalies.csv",
    index=False
)

print("\nAnomaly detection completed!")
print("File saved: data/anomalies.csv")