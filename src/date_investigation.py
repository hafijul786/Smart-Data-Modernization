import pandas as pd

# Load original dataset
file_path = "data/Super_StoreOrders.csv"
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Show original date strings
print("\nOriginal Order Date Samples:")
print(df["order_date"].head(30).to_string(index=False))

print("\nOriginal Ship Date Samples:")
print(df["ship_date"].head(30).to_string(index=False))


# Find rows where ship date appears before order date
# We will inspect the raw strings first, without converting them.

print("\nRaw Date Examples Around Problematic Records:")

print(
    df.loc[
        50:110,
        ["order_id", "order_date", "ship_date"]
    ].to_string(index=True)
)