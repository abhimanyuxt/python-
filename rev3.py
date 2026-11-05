import pandas as pd
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Salary": [30000, 40000, 50000]
})

print(pd.concat([df1, df2], axis=0, ignore_index=True))
print(pd.concat([df1, df2], axis=1))

merged_df = pd.merge(df1, df2, on="ID", how="outer")
print(merged_df)

result= merged_df.groupby("ID")["Salary"].sum()
print(result)
