c = 0
sum = 0
while True:
    a = int(input("enter a number"))
    sum += a
    c +=1
    if a == 0:
        break
print("avg =",sum/c)
