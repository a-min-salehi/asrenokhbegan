def sort(a,b,c):
    maxi = max (a,b,c)
    mini = min (a,b,c)
    medi = a+b+c - maxi - mini
    return mini , medi , maxi



x = int(input('enter x :'))
y = int(input('enter y :'))
z = int(input('enter z :'))

a , b , c = sort(x,y,z)

print(a , b , c)
