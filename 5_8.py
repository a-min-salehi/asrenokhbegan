c = 1
s = 0
while c <= 5:
    number = int(input("enter number")) # 20 17 18 -19 15 18
    if number< 0:
        print("enter a positive number")
        continue
    s += number # 20 , 20 + 17 = 37 + 18 = 55 + 15 = 70 + 18 = 88
    c += 1 # 1 , 2,3 , 4, 5 ,6
    
print(s/5)
