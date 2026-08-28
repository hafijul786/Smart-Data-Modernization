import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("data/cleaned_superstore.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# ==========================================
# 2. FEATURE ENGINEERING
# ==========================================

df["order_month"] = df["order_date"].dt.month
df["order_year"] = df["order_date"].dt.year

features = [
    "quantity",
    "discount",
    "shipping_cost",
    "order_month",
    "order_year",
    "category",
    "sub_category",
    "region",
    "ship_mode"
]

target = "sales"

# Sort chronologically
df = df.sort_values("order_date").reset_index(drop=True)

# ==========================================
# 3. TIME-BASED TRAIN / TEST SPLIT
# ==========================================

train_df = df[df["order_year"] < 2014]
test_df = df[df["order_year"] == 2014]

X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

print("\n========== TIME-BASED SPLIT ==========")
print("Training period:", train_df["order_date"].min().date(),
      "to", train_df["order_date"].max().date())

print("Testing period:", test_df["order_date"].min().date(),
      "to", test_df["order_date"].max().date())

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 4. FEATURES
# ==========================================

categorical_features = [
    "category",
    "sub_category",
    "region",
    "ship_mode"
]

numeric_features = [
    "quantity",
    "discount",
    "shipping_cost",
    "order_month",
    "order_year"
]


# ==========================================
# 5. PREPROCESSING
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ==========================================
# 6. MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 7. PIPELINE
# ==========================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ==========================================
# 8. TRAIN
# ==========================================

print("\nTraining Random Forest model...")

pipeline.fit(X_train, y_train)


# ==========================================
# 9. PREDICTION
# ==========================================

y_pred = pipeline.predict(X_test)


# ==========================================
# 10. EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

r2 = r2_score(y_test, y_pred)


print("\n========== MODEL PERFORMANCE ==========")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")


# ==========================================
# 11. SAMPLE PREDICTIONS
# ==========================================

results = pd.DataFrame({
    "Actual_Sales": y_test.values,
    "Predicted_Sales": y_pred
})

print("\n========== SAMPLE PREDICTIONS ==========")
print(results.head(10))


# ==========================================
# 12. SAVE
# ==========================================

results.to_csv(
    "data/sales_predictions.csv",
    index=False
)

print("\nSales prediction completed successfully!")
print("File: data/sales_predictions.csv")