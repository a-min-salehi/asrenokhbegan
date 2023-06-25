n = input ("enter scores :".capitalize())

l = n.split()

#print(l)

for i in range (len (l)):
   l[i] = float(l[i])

ave = sum(l) / len (l)

#print(l)

print ("the average score is : {:.2f}".format (ave))

