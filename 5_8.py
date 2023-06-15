c = 1
s = 0
while c <= 5:
    b = int(input("enter number"))
    if b < 0:
        print("enter a positive number")
        continue
    s += b
    c += 1
    
print(s/5)
