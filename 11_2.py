def Pow(a,b):
    x = a**b
    # print (x)
    return x

# global x
x = 0


def square(x): # local x
     return x**0.5


# print(x)

print(square(9))

print(f'answer Pow(2,3) = {Pow(2,3)}')
