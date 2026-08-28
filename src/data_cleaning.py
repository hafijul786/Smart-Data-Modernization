import pandas as pd

# ============================================
# 1. Load Original Dataset
# ============================================

file_path = "data/Super_StoreOrders.csv"

df = pd.read_csv(file_path)

print("Original Shape:", df.shape)


# ============================================
# 2. Convert Mixed Date Formats
# ============================================

def convert_date(date_value):

    date_value = str(date_value).strip()

    # Convert "-" to "/" so both formats become consistent
    date_value = date_value.replace("-", "/")

    # Dataset uses day/month/year
    return pd.to_datetime(
        date_value,
        format="%d/%m/%Y"
    )


df["order_date"] = df["order_date"].apply(convert_date)

df["ship_date"] = df["ship_date"].apply(convert_date)


# ============================================
# 3. Convert Sales to Numeric
# ============================================

df["sales"] = (
    df["sales"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)


# ============================================
# 4. Create Shipping Days
# ============================================

df["shipping_days"] = (
    df["ship_date"] - df["order_date"]
).dt.days


# ============================================
# 5. Data Types
# ============================================

print("\nData Types After Cleaning:")

print(df.dtypes)


# ============================================
# 6. Missing Values
# ============================================

print("\nMissing Values:")

print(df.isnull().sum())


# ============================================
# 7. Duplicate Rows
# ============================================

print("\nDuplicate Rows:")

print(df.duplicated().sum())


# ============================================
# 8. Shipping Days Summary
# ============================================

print("\nShipping Days Summary:")

print(df["shipping_days"].describe())


# ============================================
# 9. Negative Shipping Days
# ============================================

negative_shipping = (
    df["shipping_days"] < 0
).sum()

print("\nNegative Shipping Days:")

print(negative_shipping)


# ============================================
# 10. Date Range
# ============================================

print("\nOrder Date Range:")

print(
    df["order_date"].min(),
    "to",
    df["order_date"].max()
)


print("\nShip Date Range:")

print(
    df["ship_date"].min(),
    "to",
    df["ship_date"].max()
)


# ============================================
# 11. Numerical Summary
# ============================================

print("\nNumerical Summary:")

print(
    df[
        [
            "sales",
            "quantity",
            "discount",
            "profit",
            "shipping_cost",
            "shipping_days"
        ]
    ].describe()
)


# ============================================
# 12. Final Shape
# ============================================

print("\nFinal Shape:")

print(df.shape)


# ============================================
# 13. Save Cleaned Dataset
# ============================================

output_path = "data/cleaned_superstore.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved successfully!")

print("File:", output_path)