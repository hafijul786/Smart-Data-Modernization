import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/cleaned_superstore.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# Reference date
reference_date = df["order_date"].max() + pd.Timedelta(days=1)

# ==========================================
# RFM CALCULATION
# ==========================================

rfm = df.groupby("customer_name").agg(
    Recency=("order_date", lambda x: (reference_date - x.max()).days),
    Frequency=("order_id", "nunique"),
    Monetary=("sales", "sum")
).reset_index()

# ==========================================
# RFM SCORES
# ==========================================

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1],
    duplicates="drop"
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# ==========================================
# CUSTOMER SEGMENTS
# ==========================================

def segment_customer(row):

    if row["RFM_Score"] in ["555", "554", "545", "455"]:
        return "Champions"

    elif row["R_Score"] >= 4 and row["F_Score"] >= 4:
        return "Loyal Customers"

    elif row["R_Score"] >= 4 and row["M_Score"] >= 3:
        return "Potential Loyalists"

    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"

    elif row["R_Score"] <= 2 and row["M_Score"] <= 2:
        return "Lost Customers"

    else:
        return "Regular Customers"


rfm["Customer_Segment"] = rfm.apply(
    segment_customer,
    axis=1
)

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========== RFM CUSTOMER ANALYSIS ==========")

print("\nTotal Customers:")
print(len(rfm))

print("\nCustomer Segments:")
print(
    rfm["Customer_Segment"]
    .value_counts()
)

print("\nTop 10 Customers:")
print(
    rfm.sort_values(
        "Monetary",
        ascending=False
    ).head(10)
)

# ==========================================
# SAVE RESULT
# ==========================================

rfm.to_csv(
    "data/rfm_customer_segments.csv",
    index=False
)

print("\nRFM analysis completed successfully!")

print(
    "File saved: data/rfm_customer_segments.csv"
)