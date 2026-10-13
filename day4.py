import pandas as pd
import numpy as np

data = {
    "Driver": ["Abhi", "Charles", "Alonso", "Carlos", "Charles", "Gasly"],
    "Team": ["Red Bull", "Ferrari", "AMR", "Williams", "Ferrari", "Alpine"],
    "Points": [350, 321, np.nan, 199, 321, np.nan],
    "Wins": [10, 9, 23, 5, 9, 1],
    "Country": ["India", "Monaco", "Spain", "Spain", "Monaco", None]
}

df = pd.DataFrame(data)

print(df)
print(df.info())

print(df.isnull())
print(df.isnull().sum())

df_clean = df.dropna()
print(df_clean)

df["Country"] = df["Country"].fillna("France")
df["Points"]=df["Points"].fillna(df["Points"].mean())


print(df.duplicated())
print(df.duplicated().sum())

df["Team"]=df["Team"].str.strip().str.title()
print(df)

#q1 
print(df.isnull().sum())
#q2
print(df.isnull)
#q3
df=df.drop_duplicates()
#q4
df["Country"]=df["Country"].fillna("Unknown")
#q5
df["Team"]=df["Team"].str.strip().str.title()
#q6
print(df)
print(df.isnull())


