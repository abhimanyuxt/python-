import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.DataFrame({
    "Driver": ["Sebastian","Schumacher","Prost","Senna"],
    "Team":["AMR","Mercedes","Renault","McLaren"],
    "Wins":[4,1,2,6],
    "Points":[213,123,159,256],
    "Poles":[3,1,2,4]
})

print(df["Points"].mean())
print(df["Wins"].sum())
print(df["Poles"].median())
print(df["Wins"].max())
print(df["Points"].min())
print(df["Wins"].std())

print(df["Points"].max()-df["Points"].mean())

q1 = df["Points"].quantile(.25)
q3 = df["Points"].quantile(.75)

iqr = q3-q1
lower = q1-1.5*iqr
upper = q3+1.5*iqr

print("q1:",q1)
print("q3:",q3)
print("Lower Bound:",lower)
print("Upper Bound:",upper)

outliers = df[(df["Points"] < lower) | (df["Points"] > upper)]
print("Outliers:\n",outliers)

print(df[["Wins","Points","Poles"]].corr())

print(df["Points"]>200)



