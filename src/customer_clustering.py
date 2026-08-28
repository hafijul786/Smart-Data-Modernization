import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ==========================================
# 1. LOAD RFM DATA
# ==========================================

df = pd.read_csv(
    "data/rfm_customer_segments.csv"
)

print("RFM data loaded!")
print("Total Customers:", len(df))


# ==========================================
# 2. SELECT FEATURES
# ==========================================

features = [
    "Recency",
    "Frequency",
    "Monetary"
]

X = df[features].copy()


# ==========================================
# 3. SCALE FEATURES
# ==========================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# ==========================================
# 4. FIND BEST NUMBER OF CLUSTERS
# ==========================================

print("\n========== CLUSTER EVALUATION ==========")

for k in range(2, 7):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    print(
        f"K={k} | Silhouette Score={score:.4f}"
    )


# ==========================================
# 5. FINAL K-MEANS MODEL
# ==========================================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Customer_Cluster"] = kmeans.fit_predict(
    X_scaled
)


# ==========================================
# 6. CLUSTER SUMMARY
# ==========================================

cluster_summary = (
    df.groupby("Customer_Cluster")
    .agg(
        Customers=("customer_name", "count"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean")
    )
    .round(2)
)

print("\n========== CUSTOMER CLUSTERS ==========")

print(cluster_summary)


# ==========================================
# 7. SAVE RESULTS
# ==========================================

df.to_csv(
    "data/customer_clusters.csv",
    index=False
)

cluster_summary.to_csv(
    "data/customer_cluster_summary.csv"
)

print(
    "\nCustomer clustering completed!"
)

print(
    "File: data/customer_clusters.csv"
)

print(
    "Summary: data/customer_cluster_summary.csv"
)