l1 = ['amin' , 'arian' , 'pouyan' , 12]
l2 = [1 , 22 , 33 , 44]
l3 = ['amin', "arian", 'pouyan' ,12]
l4 = ["surena" , 'nader' , 122 , 'arash' , "tir" , 3]

lpl = l1 + l4
print ("lpl = " , lpl)

lpl2 = l4 + l1
print ("lpl2 = " , lpl2)

print ('surena' in l1)

print ('surena' in l4 )

print (l1 == l3)

print (l1 is l3)

l3[1] = "akbar"
print(l3)
print(l1)

print  (l2 * 4)

l5 = l1

l5[1]= "asghar"
print(l1)

print (l5 is l1)


print(l4[:])
print(l4[:4])
print(l4[2:4])
print(l4[::-1])
print(l4[::-2])
print(l4[::2])
