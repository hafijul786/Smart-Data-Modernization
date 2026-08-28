import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


# ==========================================
# 1. LOAD RFM DATA
# ==========================================

df = pd.read_csv(
    "data/rfm_customer_segments.csv"
)

print("RFM data loaded!")
print("Customers:", len(df))


# ==========================================
# 2. CREATE RISK LABEL
# ==========================================

def assign_risk(segment):

    if segment in ["At Risk", "Lost Customers"]:
        return "High Risk"

    elif segment in ["Regular Customers", "Potential Loyalists"]:
        return "Medium Risk"

    else:
        return "Low Risk"


df["Risk_Level"] = df["Customer_Segment"].apply(
    assign_risk
)


# ==========================================
# 3. FEATURES
# ==========================================

features = [
    "Recency",
    "Frequency",
    "Monetary"
]

X = df[features]
y = df["Risk_Level"]


# ==========================================
# 4. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 5. MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


print("\nTraining Customer Risk Model...")

model.fit(
    X_train,
    y_train
)


# ==========================================
# 6. PREDICTION
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 7. EVALUATION
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n========== CUSTOMER RISK MODEL ==========")

print(
    f"Accuracy: {accuracy:.4f}"
)

print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# 8. PREDICT ALL CUSTOMERS
# ==========================================

df["Predicted_Risk"] = model.predict(X)


# ==========================================
# 9. RISK SUMMARY
# ==========================================

print("\n========== RISK DISTRIBUTION ==========")

print(
    df["Predicted_Risk"].value_counts()
)


# ==========================================
# 10. SAVE RESULTS
# ==========================================

output_columns = [
    "customer_name",
    "Recency",
    "Frequency",
    "Monetary",
    "Customer_Segment",
    "Predicted_Risk"
]

df[output_columns].to_csv(
    "data/customer_risk_predictions.csv",
    index=False
)

print(
    "\nCustomer risk prediction completed!"
)

print(
    "File saved: data/customer_risk_predictions.csv"
)