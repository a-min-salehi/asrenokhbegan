import math

solve_equation = lambda x, y: math.sqrt(x)/ y

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

result = solve_equation(x, y)

print("The solution of √(x)/y is:", result)
