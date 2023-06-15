while True:
    w = float(input("enter width:"))
    l =  float(input("enter length:"))
    if l < w :
        print("...")
        continue
    else:
        break
print("mohit ",(w+l)*2)
print("masahat ",w*l)
