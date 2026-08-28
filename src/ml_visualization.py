import pandas as pd
import matplotlib.pyplot as plt

# Load predictions
df = pd.read_csv("data/sales_predictions.csv")

# ------------------------------------------
# Actual vs Predicted Sales
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Actual_Sales"],
    df["Predicted_Sales"],
    alpha=0.4
)

# Perfect prediction reference line
min_value = min(
    df["Actual_Sales"].min(),
    df["Predicted_Sales"].min()
)

max_value = max(
    df["Actual_Sales"].max(),
    df["Predicted_Sales"].max()
)

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--"
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")

plt.tight_layout()

plt.savefig(
    "actual_vs_predicted_sales.png",
    dpi=300
)

plt.show()

print("ML visualization completed!")
print("Chart saved: actual_vs_predicted_sales.png")