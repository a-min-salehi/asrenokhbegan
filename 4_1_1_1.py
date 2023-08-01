a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

delta = b**2 - 4*a*c

if delta < 0 :
    print("there is not any root")
elif delta == 0 :
    print(-b / (2*a))
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print('x1 = ', x1)
    print('x2 = ', x2)
