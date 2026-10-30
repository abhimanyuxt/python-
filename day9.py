import pandas as pd
employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Aman", "Rahul", "Priya", "Karan", "Neha"],
    "Department_ID": [1, 2, 1, 3, 4],
    "Salary": [50000, 60000, 55000, 70000, 65000]
})

departments = pd.DataFrame({
    "Department_ID": [1, 2, 3, 5],
    "Department": ["Sales", "IT", "HR", "Finance"]
})

mew=pd.merge(employees , departments , on ="Department_ID", how = "inner")
print(mew)

print(mew.groupby("Department")["Salary"].sum())


january = pd.DataFrame({
    "Product": ["Laptop", "Phone"],
    "Sales": [75000, 30000]
})

february = pd.DataFrame({
    "Product": ["Tablet", "Monitor","Phone"],
    "Sales": [25000, 12000, 30000]
})
print(pd.concat([january, february], ignore_index=True))
print(pd.concat([january, february], axis=1))

employees_indexed = employees.set_index("Department_ID")
departments_indexed = departments.set_index("Department_ID")

print(employees_indexed.join(departments_indexed, how="inner"))




