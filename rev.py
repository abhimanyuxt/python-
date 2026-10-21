import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Monitor", "Laptop"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [75000, 30000, 25000, 82000, 35000, 28000, 12000, 500000],
    "Units": [5, 10, 8, 6, 12, 9, 4, 2],
    "Profit": [12000, 6000, 4500, 14000, 7000, 5000, 2000, 30000]
})

print(df.describe())

q1=df["Sales"].quantile(.25)
q3=df["Sales"].quantile(.75)
IQR=q3-q1

lower = q1 - 1.5*IQR
upper = q3 + 1.5*IQR

print(q1)
print(q3)
print(IQR)
print(lower)
print(upper)

outliers = df[
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
]

print(outliers)

print(df.groupby("Category")["Sales"].sum())
print(df[["Sales","Profit"]].corr())

print(df["Sales"]>df["Sales"].mean())

highest_sales = df.loc[df["Sales"].idxmax()]
print(highest_sales)

plt.plot(df["Product"],df["Profit"],marker="o")
plt.title("Product vs Profit")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.show()


