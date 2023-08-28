a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

if a + b > c and a + c > b and c + b > a:
    print("we can make a triangle")
else:
    print("error")
