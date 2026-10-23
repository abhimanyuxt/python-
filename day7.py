import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-18",
        "2026-02-03", "2026-02-10", "2026-02-15",
        "2026-03-02", "2026-03-11", "2026-03-19",
        "2026-04-04", "2026-04-12", "2026-01-05"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop",
        "Phone", "Tablet", "Laptop", "Phone",
        "Monitor", "Tablet", "Laptop", "Laptop"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Accessories",
        "Electronics", " Electronics ", "Electronics"
    ],
    "Sales": [
        75000, 30000, 25000, 82000,
        35000, 28000, 90000, 42000,
        12000, 32000, np.nan, 75000
    ],
    "Profit": [
        12000, 6000, 4500, 14000,
        7000, np.nan, 16000, 8500,
        2000, 5500, 13000, 12000
    ],
    "Units": [5, 10, 8, 6, 12, 9, 7, 14, 4, 10, 6, 5]
})

print(df.head(4))
print(df.shape)
print(df.info())
print("NULL is" ,df.isnull().sum())

print(df.drop_duplicates())
print(df["Product"].str.strip())
df["Profit"] = df["Profit"].fillna(df["Profit"].median())

#total
print("Total Sales" ,df["Sales"].sum())
print("Total Profit" ,df["Profit"].sum())
print("Total Units Sold " ,df["Units"].sum())

# Aggregate data
product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

total_profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Create 4 plots in one figure
fig, ax = plt.subplots(2, 2, figsize=(14, 9))

# 1. Monthly sales trend
monthly_sales = df.groupby(
    pd.to_datetime(df["Date"]).dt.to_period("M")
)["Sales"].sum()

ax[0, 0].plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)
ax[0, 0].set_title("Monthly Sales Trend")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")

# 2. Profit by product
ax[0, 1].bar(
    total_profit.index,
    total_profit.values,
    color="pink"
)
ax[0, 1].set_title("Profit by Product")
ax[0, 1].set_xlabel("Product")
ax[0, 1].set_ylabel("Total Profit")
ax[0, 1].tick_params(axis="x", rotation=30)

# 3. Sales by product
ax[1, 0].bar(
    product_sales.index,
    product_sales.values,
    color="yellow"
)
ax[1, 0].set_title("Sales by Product")
ax[1, 0].set_xlabel("Product")
ax[1, 0].set_ylabel("Total Sales")
ax[1, 0].tick_params(axis="x", rotation=30)

# 4. Sales vs Profit
ax[1, 1].scatter(df["Sales"], df["Profit"])
ax[1, 1].set_title("Sales vs Profit")
ax[1, 1].set_xlabel("Sales")
ax[1, 1].set_ylabel("Profit")

# Final layout
fig.suptitle("Retail Sales Analysis Dashboard", fontsize=16)
plt.tight_layout()
plt.show()

#Insights

#Best Selling Product 
print("Best-selling product:", product_sales.idxmax())
print("Total sales:", product_sales.max())

#product with most profit 
print("Best profit generating product :",total_profit.idxmax())
print("Total Profit :", total_profit.max())
print(df[["Sales", "Profit"]].corr())







