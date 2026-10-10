import pandas as pd 
data ={
    "Driver":["Abhi","Charles","Alonso","Carlos","Gasly"],
    "Team":["RedBull","Ferrari","AMR","Williams","Alpine"],
    "wins":[10,9,23,5,1],
    "Points":[350,321,475,199,57]
    }
df = pd.DataFrame(data)
print(df)

print(df.head(2))
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.describe())

print(df["Driver"])
print(df[df["Points"]>99])

result = df[
    (df["Points"] > 99) &
    (df["wins"] > 3)
]
print(result)

print(df.sort_values("Points", ascending=False))

print(df["Driver"],df["Points"])
print(df[df["Points"]>200])
print(df[
    (df["Team"] == "Ferrari") &
    (df["wins"] > 2)
])
print(df.sort_values("wins", ascending=False))
print(df.groupby("Team")["Points"].sum())



