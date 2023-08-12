while True:
    stop = int(input("enter a number: "))
    if stop  <= 0 :
        print("***enter a positive number***")
        continue
    else:
        break
for i in range(1,stop+1):
    if i % 5 != 0:
        print(i)
    else:
        continue
