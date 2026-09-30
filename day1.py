name = 'abhimanyu'
age = 20
cgpa = 9.5
is_student = True
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Is Student:", is_student)

"""operations"""
a=5
b=10
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)   
print("Modulus:", b % a)

sales=[100,200,300,500,400]
print(sales[2])
print(sales[0:3])

print(len(sales))
print(max(sales))
print(min(sales))
print(sum(sales))

sales.append(1000)
sales.remove(100)

student = {"name": "Abhimanyu",
           "age":20,
           "cgpa":9.5,}
print(student["name"])
print(student["age"])

student["city"] = "Delhi"
student["email"] ="xyz"

student['cgpa'] = 7.5


sales = 70000
if sales>5000:
    print("good")
else:
    print("not good")

sales = 75000
if sales >65000:
    print("good")
elif sales>50000:
    print("average")
else:
    print("not good")
    
sales = [100, 250, 300, 150, 400]
for value in sales:
    print(value)

def calculate_total(numbers):
    return sum(numbers)
sales = [100, 250, 300, 150, 400]

total = calculate_total(sales)
print(total)

    

