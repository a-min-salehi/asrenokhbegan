a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print("double root")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("one root")
    print("x =", x)
else:
    print("no root :)")
