import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

df = pd.read_csv(
    "data/cleaned_superstore.csv"
)

df["order_date"] = pd.to_datetime(
    df["order_date"]
)

print("Dataset loaded successfully!")
print("Records:", len(df))


# ==========================================
# 2. CREATE MONTHLY SALES
# ==========================================

monthly_sales = (
    df.groupby(
        df["order_date"].dt.to_period("M")
    )["sales"]
    .sum()
    .reset_index()
)

monthly_sales["order_date"] = (
    monthly_sales["order_date"]
    .dt.to_timestamp()
)


print("\n========== MONTHLY SALES ==========")
print(monthly_sales.tail(12))


# ==========================================
# 3. MOVING AVERAGE
# ==========================================

monthly_sales["moving_average"] = (
    monthly_sales["sales"]
    .rolling(window=3)
    .mean()
)


# ==========================================
# 4. TIME FEATURE
# ==========================================

monthly_sales["time_index"] = np.arange(
    len(monthly_sales)
)

monthly_sales["month"] = (
    monthly_sales["order_date"].dt.month
)


# ==========================================
# 5. TIME-BASED TRAIN / TEST SPLIT
# ==========================================

# Last 6 months → testing
train = monthly_sales.iloc[:-6].copy()
test = monthly_sales.iloc[-6:].copy()

features = [
    "time_index",
    "month"
]

X_train = train[features]
y_train = train["sales"]

X_test = test[features]
y_test = test["sales"]


print("\n========== TRAIN / TEST ==========")

print(
    "Training Period:",
    train["order_date"].min().date(),
    "to",
    train["order_date"].max().date()
)

print(
    "Testing Period:",
    test["order_date"].min().date(),
    "to",
    test["order_date"].max().date()
)


# ==========================================
# 6. TRAIN FORECASTING MODEL
# ==========================================

model = LinearRegression()

print("\nTraining forecasting model...")

model.fit(
    X_train,
    y_train
)


# ==========================================
# 7. TEST PREDICTION
# ==========================================

test["Predicted_Sales"] = model.predict(
    X_test
)


# ==========================================
# 8. MODEL EVALUATION
# ==========================================

mae = mean_absolute_error(
    y_test,
    test["Predicted_Sales"]
)

rmse = mean_squared_error(
    y_test,
    test["Predicted_Sales"]
) ** 0.5


print("\n========== FORECAST MODEL PERFORMANCE ==========")

print("Model: Linear Regression")

print(
    f"MAE  : {mae:.2f}"
)

print(
    f"RMSE : {rmse:.2f}"
)


# ==========================================
# 9. NEXT 6 MONTH FORECAST
# ==========================================

last_date = monthly_sales[
    "order_date"
].max()

future_dates = pd.date_range(
    start=last_date + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

future_time_index = np.arange(
    len(monthly_sales),
    len(monthly_sales) + 6
)

future_df = pd.DataFrame({

    "order_date": future_dates,

    "time_index": future_time_index,

    "month": future_dates.month
})


future_df["Forecasted_Sales"] = (
    model.predict(
        future_df[features]
    )
)


# ==========================================
# 10. FORECAST OUTPUT
# ==========================================

print(
    "\n========== NEXT 6 MONTH SALES FORECAST =========="
)

print(
    future_df[
        [
            "order_date",
            "Forecasted_Sales"
        ]
    ].to_string(index=False)
)


# ==========================================
# 11. SAVE FORECAST
# ==========================================

future_df[
    [
        "order_date",
        "Forecasted_Sales"
    ]
].to_csv(
    "data/sales_forecast.csv",
    index=False
)


# ==========================================
# 12. VISUALIZATION
# ==========================================

plt.figure(
    figsize=(12, 6)
)

plt.plot(
    monthly_sales["order_date"],
    monthly_sales["sales"],
    label="Historical Sales"
)

plt.plot(
    monthly_sales["order_date"],
    monthly_sales["moving_average"],
    label="3-Month Moving Average"
)

plt.plot(
    future_df["order_date"],
    future_df["Forecasted_Sales"],
    marker="o",
    linestyle="--",
    label="6-Month Forecast"
)

plt.xlabel("Date")

plt.ylabel("Sales")

plt.title(
    "Historical Sales and Future Sales Forecast"
)

plt.legend()

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "sales_forecast.png",
    dpi=300
)

plt.show()


print(
    "\nSales forecasting completed successfully!"
)

print(
    "Forecast file: data/sales_forecast.csv"
)

print(
    "Chart saved: sales_forecast.png"
)