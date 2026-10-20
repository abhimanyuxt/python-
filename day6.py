import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 13500, 18000, 22000, 25000],
    "Profit": [2000, 2800, 2300, 3500, 4500, 5200],
    "Customers": [100, 120, 115, 145, 170, 190]
})

plt.plot(df["Month"],df["Sales"],marker="o")
plt.title("Line chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.scatter(df["Month"],df["Sales"])
plt.title("Scatter Line Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(9,5))
plt.bar(df["Month"],df["Sales"],color="red")
plt.title("Bar Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

plt.hist(df["Sales"], bins=5, edgecolor="pink")
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(df["Sales"])
plt.title("Sales Distribution and Potential Outliers")
plt.ylabel("Sales")
plt.show()