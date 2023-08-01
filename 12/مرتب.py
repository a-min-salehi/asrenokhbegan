def مرتب(يک,دو,سه):
    maxi = max (يک,دو,سه)
    mini = min (يک,دو,سه)
    medi = يک+دو+سه - maxi - mini
    return mini , medi , maxi



x = int(input('enter x :'))
y = int(input('enter y :'))
z = int(input('enter z :'))

a , b , c =مرتب(x,y,z)

print(a , b , c)
