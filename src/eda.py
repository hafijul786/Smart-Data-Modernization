import pandas as pd

# Load cleaned dataset
file_path = "data/cleaned_superstore.csv"

df = pd.read_csv(file_path)

# Convert dates again because CSV loading converts them to object
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])


# ============================================
# BUSINESS SUMMARY
# ============================================

total_sales = df["sales"].sum()

total_profit = df["profit"].sum()

total_quantity = df["quantity"].sum()

average_discount = df["discount"].mean()

average_shipping_days = df["shipping_days"].mean()


print("\n========== BUSINESS SUMMARY ==========")

print(f"Total Sales: {total_sales:,.2f}")

print(f"Total Profit: {total_profit:,.2f}")

print(f"Total Quantity: {total_quantity:,}")

print(f"Average Discount: {average_discount:.2%}")

print(f"Average Shipping Days: {average_shipping_days:.2f}")


# ============================================
# PROFIT MARGIN
# ============================================

profit_margin = (
    total_profit / total_sales
) * 100

print(f"Profit Margin: {profit_margin:.2f}%")


# ============================================
# DATE INFORMATION
# ============================================

print("\n========== DATE INFORMATION ==========")

print(
    "Order Date Range:",
    df["order_date"].min().date(),
    "to",
    df["order_date"].max().date()
)

print(
    "Ship Date Range:",
    df["ship_date"].min().date(),
    "to",
    df["ship_date"].max().date()
)

# ============================================
# CATEGORY-WISE ANALYSIS
# ============================================

category_analysis = df.groupby("category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")

print(category_analysis)


# Highest Sales Category
highest_sales_category = category_analysis["Total_Sales"].idxmax()

print(
    "\nHighest Sales Category:",
    highest_sales_category
)


# Highest Profit Category
highest_profit_category = category_analysis["Total_Profit"].idxmax()

print(
    "Highest Profit Category:",
    highest_profit_category
)

import matplotlib.pyplot as plt


# ============================================
# CATEGORY-WISE SALES VISUALIZATION
# ============================================

category_sales = (
    df.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("data/category_sales.png")

plt.show()

# ============================================
# CATEGORY SALES VS PROFIT
# ============================================

category_performance = df.groupby("category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
)

print("\n========== CATEGORY SALES VS PROFIT ==========")

print(category_performance)


# ============================================
# Visualization
# ============================================

category_performance.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Sales vs Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("data/category_sales_profit.png")

plt.show()

# ============================================
# SUB-CATEGORY ANALYSIS
# ============================================

subcategory_performance = df.groupby("sub_category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== SUB-CATEGORY ANALYSIS ==========")

print(subcategory_performance)


# ============================================
# Highest Sales Sub-Category
# ============================================

highest_sales_subcategory = (
    subcategory_performance["Total_Sales"].idxmax()
)

print(
    "\nHighest Sales Sub-Category:",
    highest_sales_subcategory
)


# ============================================
# Highest Profit Sub-Category
# ============================================

highest_profit_subcategory = (
    subcategory_performance["Total_Profit"].idxmax()
)

print(
    "Highest Profit Sub-Category:",
    highest_profit_subcategory
)


# ============================================
# Lowest Profit Sub-Category
# ============================================

lowest_profit_subcategory = (
    subcategory_performance["Total_Profit"].idxmin()
)

print(
    "Lowest Profit Sub-Category:",
    lowest_profit_subcategory
)

# ============================================
# REGION-WISE ANALYSIS
# ============================================

region_performance = df.groupby("region").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== REGION-WISE ANALYSIS ==========")

print(region_performance)


# ============================================
# Highest Sales Region
# ============================================

highest_sales_region = (
    region_performance["Total_Sales"].idxmax()
)

print(
    "\nHighest Sales Region:",
    highest_sales_region
)


# ============================================
# Highest Profit Region
# ============================================

highest_profit_region = (
    region_performance["Total_Profit"].idxmax()
)

print(
    "Highest Profit Region:",
    highest_profit_region
)


# ============================================
# Lowest Profit Region
# ============================================

lowest_profit_region = (
    region_performance["Total_Profit"].idxmin()
)

print(
    "Lowest Profit Region:",
    lowest_profit_region
)

# ============================================
# SEGMENT-WISE ANALYSIS
# ============================================

segment_performance = df.groupby("segment").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== SEGMENT-WISE ANALYSIS ==========")

print(segment_performance)


# ============================================
# Highest Sales Segment
# ============================================

highest_sales_segment = (
    segment_performance["Total_Sales"].idxmax()
)

print(
    "\nHighest Sales Segment:",
    highest_sales_segment
)


# ============================================
# Highest Profit Segment
# ============================================

highest_profit_segment = (
    segment_performance["Total_Profit"].idxmax()
)

print(
    "Highest Profit Segment:",
    highest_profit_segment
)


# ============================================
# Lowest Profit Segment
# ============================================

lowest_profit_segment = (
    segment_performance["Total_Profit"].idxmin()
)

print(
    "Lowest Profit Segment:",
    lowest_profit_segment
)

# ============================================
# DISCOUNT VS PROFIT ANALYSIS
# ============================================

discount_analysis = df.groupby("discount").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Number_of_Orders=("order_id", "count")
).sort_index()

print("\n========== DISCOUNT VS PROFIT ANALYSIS ==========")

print(discount_analysis)


# ============================================
# Average Profit by Discount
# ============================================

average_profit_discount = (
    df.groupby("discount")["profit"]
    .mean()
    .sort_index()
)

print("\n========== AVERAGE PROFIT BY DISCOUNT ==========")

print(average_profit_discount)


# ============================================
# Visualization
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(
    average_profit_discount.index,
    average_profit_discount.values,
    marker="o"
)

plt.title("Average Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("data/discount_vs_profit.png")

plt.show()

# ============================================
# YEAR-WISE SALES & PROFIT ANALYSIS
# ============================================

yearly_performance = df.groupby("year").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
)

print("\n========== YEAR-WISE PERFORMANCE ==========")

print(yearly_performance)


# ============================================
# YEAR-WISE SALES TREND
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(
    yearly_performance.index,
    yearly_performance["Total_Sales"],
    marker="o"
)

plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.xticks(yearly_performance.index)

plt.grid(True)

plt.tight_layout()

plt.savefig("data/yearly_sales_trend.png")

plt.show()

# ============================================
# MONTH-WISE SALES ANALYSIS
# ============================================

df["month"] = df["order_date"].dt.month

monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
)

print("\n========== MONTH-WISE SALES ==========")

print(monthly_sales)


# ============================================
# HIGHEST SALES MONTH
# ============================================

highest_sales_month = monthly_sales.idxmax()

highest_sales_value = monthly_sales.max()

print(
    "\nHighest Sales Month:",
    highest_sales_month
)

print(
    "Highest Monthly Sales:",
    f"{highest_sales_value:,.2f}"
)


# ============================================
# MONTHLY SALES VISUALIZATION
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Total Sales")

plt.xticks(range(1, 13))

plt.grid(True)

plt.tight_layout()

plt.savefig("data/monthly_sales_trend.png")

plt.show()

# ============================================
# SHIPPING MODE ANALYSIS
# ============================================

shipping_performance = df.groupby("ship_mode").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Average_Shipping_Days=("shipping_days", "mean"),
    Total_Orders=("order_id", "count")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== SHIPPING MODE ANALYSIS ==========")

print(shipping_performance)


# ============================================
# FASTEST SHIPPING MODE
# ============================================

fastest_shipping_mode = (
    shipping_performance["Average_Shipping_Days"].idxmin()
)

fastest_shipping_days = (
    shipping_performance["Average_Shipping_Days"].min()
)

print(
    "\nFastest Shipping Mode:",
    fastest_shipping_mode
)

print(
    "Average Shipping Days:",
    f"{fastest_shipping_days:.2f}"
)


# ============================================
# HIGHEST SALES SHIPPING MODE
# ============================================

highest_sales_shipping = (
    shipping_performance["Total_Sales"].idxmax()
)

print(
    "\nHighest Sales Shipping Mode:",
    highest_sales_shipping
)
# ============================================
# CUSTOMER ANALYSIS
# ============================================

customer_performance = df.groupby("customer_name").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Total_Orders=("order_id", "count")
)


# ============================================
# TOP 10 CUSTOMERS BY SALES
# ============================================

top_customers_sales = (
    customer_performance
    .sort_values("Total_Sales", ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

print(top_customers_sales)


# ============================================
# TOP 10 CUSTOMERS BY PROFIT
# ============================================

top_customers_profit = (
    customer_performance
    .sort_values("Total_Profit", ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")

print(top_customers_profit)


# ============================================
# UNIQUE CUSTOMERS
# ============================================

unique_customers = df["customer_name"].nunique()

print("\nTotal Unique Customers:", unique_customers)

# ============================================
# CUSTOMER ANALYSIS
# ============================================

customer_performance = df.groupby("customer_name").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Total_Orders=("order_id", "count")
)


# ============================================
# TOP 10 CUSTOMERS BY SALES
# ============================================

top_customers_sales = (
    customer_performance
    .sort_values("Total_Sales", ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

print(top_customers_sales)


# ============================================
# TOP 10 CUSTOMERS BY PROFIT
# ============================================

top_customers_profit = (
    customer_performance
    .sort_values("Total_Profit", ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")

print(top_customers_profit)


# ============================================
# UNIQUE CUSTOMERS
# ============================================

unique_customers = df["customer_name"].nunique()

print("\nTotal Unique Customers:", unique_customers)

# ============================================
# LOSS-MAKING SUB-CATEGORY ANALYSIS
# ============================================

subcategory_profit = df.groupby("sub_category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
)

# Sort by profit
subcategory_profit = subcategory_profit.sort_values(
    "Total_Profit"
)

print("\n========== SUB-CATEGORIES BY PROFIT ==========")

print(subcategory_profit)


# ============================================
# LOSS-MAKING SUB-CATEGORIES
# ============================================

loss_making = subcategory_profit[
    subcategory_profit["Total_Profit"] < 0
]

print("\n========== LOSS-MAKING SUB-CATEGORIES ==========")

print(loss_making)


print(
    "\nNumber of Loss-Making Sub-Categories:",
    len(loss_making)
)

# ============================================
# TABLES LOSS ANALYSIS
# ============================================

tables_data = df[
    df["sub_category"] == "Tables"
]

tables_analysis = {
    "Total Sales": tables_data["sales"].sum(),
    "Total Profit": tables_data["profit"].sum(),
    "Total Quantity": tables_data["quantity"].sum(),
    "Average Discount": tables_data["discount"].mean(),
    "Average Shipping Cost": tables_data["shipping_cost"].mean(),
    "Average Shipping Days": tables_data["shipping_days"].mean()
}

print("\n========== TABLES LOSS ANALYSIS ==========")

for metric, value in tables_analysis.items():
    print(f"{metric}: {value:.2f}")

    # ============================================
# TABLES: DISCOUNT VS PROFIT
# ============================================

tables_discount_analysis = tables_data.groupby("discount").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Average_Profit=("profit", "mean"),
    Total_Quantity=("quantity", "sum")
).sort_index()

print("\n========== TABLES DISCOUNT VS PROFIT ==========")

print(tables_discount_analysis)

# ============================================
# TABLES: SHIPPING COST VS PROFIT
# ============================================

tables_shipping_analysis = tables_data.groupby(
    "ship_mode"
).agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Average_Shipping_Cost=("shipping_cost", "mean"),
    Average_Shipping_Days=("shipping_days", "mean"),
    Total_Orders=("order_id", "count")
).sort_values(
    "Total_Profit"
)

print("\n========== TABLES SHIPPING ANALYSIS ==========")

print(tables_shipping_analysis)

# ============================================
# YEAR-WISE BUSINESS PERFORMANCE
# ============================================

yearly_performance = df.groupby("year").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Total_Orders=("order_id", "count")
)

yearly_performance["Profit_Margin"] = (
    yearly_performance["Total_Profit"]
    / yearly_performance["Total_Sales"]
) * 100

print("\n========== YEAR-WISE BUSINESS PERFORMANCE ==========")

print(yearly_performance.round(2))

# ============================================
# YEAR-OVER-YEAR GROWTH
# ============================================

yearly_growth = yearly_performance.copy()

yearly_growth["Sales_Growth_%"] = (
    yearly_growth["Total_Sales"].pct_change() * 100
)

yearly_growth["Profit_Growth_%"] = (
    yearly_growth["Total_Profit"].pct_change() * 100
)

yearly_growth["Order_Growth_%"] = (
    yearly_growth["Total_Orders"].pct_change() * 100
)

print("\n========== YEAR-OVER-YEAR GROWTH ==========")

print(yearly_growth[
    [
        "Sales_Growth_%",
        "Profit_Growth_%",
        "Order_Growth_%"
    ]
].round(2))

# ============================================
# CATEGORY ANALYSIS
# ============================================

category_analysis = df.groupby("category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Total_Orders=("order_id", "count")
)

category_analysis["Profit_Margin_%"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
) * 100

category_analysis = category_analysis.sort_values(
    "Total_Profit",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")

print(category_analysis.round(2))

# ============================================
# REGION ANALYSIS
# ============================================

region_analysis = df.groupby("region").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum"),
    Total_Orders=("order_id", "count")
)

region_analysis["Profit_Margin_%"] = (
    region_analysis["Total_Profit"]
    / region_analysis["Total_Sales"]
) * 100

region_analysis = region_analysis.sort_values(
    "Total_Profit",
    ascending=False
)

print("\n========== REGION ANALYSIS ==========")

print(region_analysis.round(2))