a = int(input("enter a:"))
if 0< a <10:
    if a%2==0:
        print("e1")
    else:
        print("o1")
elif 10 <= a < 100:
    if a%2==0:
        print("e2")
    else:
        print("o2")

#elif 10<= a < 100 and a%2==0:
    #print("e2")
#elif 10<= a < 100 and a%2!=0:
    #print("o2")

else:
    print("error")
