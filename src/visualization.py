import pandas as pd
import matplotlib.pyplot as plt


# ============================================
# LOAD CLEANED DATA
# ============================================

file_path = "data/cleaned_superstore.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

print("Visualization data ready!")

# ============================================
# YEAR-WISE SALES
# ============================================

yearly_sales = df.groupby("year")["sales"].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker="o"
)

plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("yearly_sales.png")

plt.show()

# ============================================
# CATEGORY-WISE SALES AND PROFIT
# ============================================

category_performance = df.groupby("category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
)

ax = category_performance.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Category-wise Sales and Profit")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("category_sales_profit.png")

plt.show()

# ============================================
# SALES AND PROFIT TREND
# ============================================

yearly_performance = df.groupby("year").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
)

plt.figure(figsize=(10, 6))

plt.plot(
    yearly_performance.index,
    yearly_performance["Total_Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    yearly_performance.index,
    yearly_performance["Total_Profit"],
    marker="o",
    label="Profit"
)

plt.title("Sales and Profit Trend (2011–2014)")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("sales_profit_trend.png")

plt.show()

# ============================================
# SALES AND PROFIT TREND
# ============================================

yearly_performance = df.groupby("year").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
)

plt.figure(figsize=(10, 6))

plt.plot(
    yearly_performance.index,
    yearly_performance["Total_Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    yearly_performance.index,
    yearly_performance["Total_Profit"],
    marker="o",
    label="Profit"
)

plt.title("Sales and Profit Trend (2011-2014)")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("sales_profit_trend.png")
plt.show()

# ============================================
# TABLES: DISCOUNT VS PROFIT
# ============================================

tables_df = df[df["sub_category"] == "Tables"].copy()

discount_profit = tables_df.groupby("discount").agg(
    Total_Profit=("profit", "sum"),
    Total_Sales=("sales", "sum")
)

plt.figure(figsize=(10, 6))

plt.bar(
    discount_profit.index.astype(str),
    discount_profit["Total_Profit"]
)

plt.axhline(
    y=0,
    linewidth=1
)

plt.title("Tables: Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("tables_discount_profit.png")

plt.show()

# ============================================
# REGION PERFORMANCE
# ============================================

region_performance = df.groupby("region").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
)

region_performance["Profit_Margin_%"] = (
    region_performance["Total_Profit"]
    / region_performance["Total_Sales"]
) * 100

region_performance = region_performance.sort_values(
    "Total_Profit",
    ascending=False
)

plt.figure(figsize=(12, 6))

plt.bar(
    region_performance.index,
    region_performance["Total_Profit"]
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("region_profit.png")

plt.show()