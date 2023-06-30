price = {"go" :40 , "solidity" :45 , 'python' : 35 , 'c++' : 32 , 'c#': 37 , 'flutter' : 25 }

print (price.items (), '\n')

k= (1 , 2 ,3 )
k2 = (2 , 5 , 4 , 7)

dictt =  {}

print ( dictt.fromkeys (k ) , '\n' )

print ( dictt.fromkeys (k2 , "$$" ) , '\n' )

price.pop ('go')

print (price , '\n')


price.popitem()
print (price , '\n')


print (price.setdefault ('flutter'  , 28), '\n')


print (price)
