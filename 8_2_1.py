while True:
    a = input("Enter a: ")
    try:
        if a == "0":
            break
        elif int(a)%2 == 0:
            print("even")
        else:
            print("odd")

        if int(a) < 0 :
            print(len(a)-1)
        else:
           print(len(a))
    except:
        print("try again!!!")
