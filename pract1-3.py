sales = [12000, 18000, 9000, 25000, 30000, 15000]
print(sum(sales))
print(sum(sales)/len(sales))
count = 0
for sale in sales:
    if sale > 15000:
        count += 1
print(count)

import numpy as np
scores = np.array([45, 78, 92, 34, 88, 61, 95, 50])
bonus =5 
print(scores + bonus)
score=scores + bonus
print(score>80)
print(np.mean(score))
print(np.std(score))

import pandas as pd
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "Sales", "IT", "HR", "Sales"],
    "Salary": [45000, 35000, 60000, 30000, 50000],
    "Experience": [2, 1, 5, 1, 4]
})
print(df[(df["Salary"] > 40000) & (df["Department"] == "IT")])
print(df[df["Experience"] > 3])
print(df.groupby("Department")["Salary"].mean())