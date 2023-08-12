while True:
    stop = int(input("enter a number: "))
    if stop  < 0 :
        print("***enter a positive number***")
        continue
    else:
        break
    
start = 1

while stop >= start:
    if start % 5 != 0:
        print(start)
    start += 1
