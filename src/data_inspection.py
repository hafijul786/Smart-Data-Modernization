import pandas as pd

# Dataset path
file_path = "data/Super_StoreOrders.csv"

# Load dataset
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")

# Dataset shape
print("\nShape:")
print(df.shape)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check dates
print("\nOrder Date:")
print(df["order_date"].head())

print("\nShip Date:")
print(df["ship_date"].head())

print("\nSales Sample Values:")
print(df["sales"].head(20).tolist())

print("\nSales Data Type:")
print(df["sales"].dtype)

print("\nSales Unique Sample:")
print(df["sales"].unique()[:20])