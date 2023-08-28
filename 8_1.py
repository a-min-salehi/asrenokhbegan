while True:
    print("!!!")
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a + b)
        break
    except:
        print("enter again")
        continue


