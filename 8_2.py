while True:
    a = input("Enter a: ")
    try:
        if a == "0":
            break
        elif int(a) < 0 :
            if int(a)%2 == 0:
                print("even")
            else:
                print("odd")
            print(len(a)-1)
        else:
            if int(a)%2 == 0:
                print("even")
            else:
                print("odd")
            print(len(a))
    except:
        print("try again!!!")
