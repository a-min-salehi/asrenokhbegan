c = 0
sum = 0
while True:
    a = int(input("enter a number")) # 19 18 15 10 0
    if a == 0:
        break
    sum += a # 19 , 37 , 52 , 62 
    c +=1 # 1 , 2, 3, 4
    
print("avg =",sum/c)
