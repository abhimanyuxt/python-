import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-18",
        "2026-02-03", "2026-02-10", "2026-02-15",
        "2026-03-02", "2026-03-11", "2026-03-19",
        "2026-04-04", "2026-04-12", "2026-04-25"
    ],
    "Sales": [
        12000, 15000, 13500,
        18000, 22000, 20000,
        25000, 28000, 26000,
        30000, 32000, 35000
    ],
    "Profit": [
        2000, 2500, 2200,
        3500, 4200, 3800,
        5000, 5600, 5200,
        6000, 6500, 7200
    ]
})

print(df.info())
print(df.head())

df["Date"]=pd.to_datetime(df["Date"])
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Month_Name"]=df["Date"].dt.strftime("%B")

print(df.head())

#monthly profit 
print(df.groupby("Month")["Profit"].sum())
monthly = df.groupby("Month").agg(
    total_sales=("Sales","sum"),
    total_profit=("Profit","sum")
)
print(monthly)

#MOM growth 
monthly["Previous_sales"]= monthly["total_sales"].shift(1)
monthly["MoM change"]=(
    monthly["total_sales"]-monthly["Previous_sales"]
)
monthly["MoM change %"]=(
    monthly["MoM change"]/monthly["Previous_sales"]
)*100
print(monthly)

# Yealy growth
print(df.groupby("Year")["Profit"].sum())
yearly=df.groupby("Year").agg(
    yearly_sales=("Sales","sum"),
    yearly_profit=("Profit","sum")
)

print(yearly)

#MoM % in march
march_growth = (
    (monthly.loc[3, "total_sales"] -
     monthly.loc[2, "total_sales"])
    / monthly.loc[2, "total_sales"]
) * 100
print(march_growth,"%")

#line chart 
plt.plot(monthly.index,monthly["total_sales"],marker="o")
plt.title("Total Sales by month")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

