import numpy as np
sales = np.array([100, 200, 300, 400, 500])
print(np.sum(sales))
print(np.max(sales))
print(np.min(sales))
print(np.mean(sales))

print(sales[0])
print(sales[4])
print(sales[1:3])

print(sales>200)

sales = np.array([12000, 15000, 18000, 11000, 22000, 25000])
# 1. Print the first sale
print(sales[0])

# 2. Print the last sale
print(sales[5])

# 3. Print the first three sales
print(sales[0:3])

# 4. Add 1000 to every sale
sales = sales+1000

# 5. Print sales greater than 18000
print(sales[sales>18000])

# 6. Calculate the average
print(sum(sales)/len(sales))

# 7. Calculate the standard deviation
print(np.std(sales))

sales = np.array ([
    [100,200,300],
    [400,500,600],
    [700,800,900]
])

print(sales[0,0:3])
print(sum(sales))
print(np.mean(sales))
print(np.sum(sales,axis=0))
print(np.sum(sales,axis=1))

print(np.sum(sales[0]))
print(sum(sales)/len(sales))
print(np.sum(sales[:,1]))