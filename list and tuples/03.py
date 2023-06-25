Sum = 0
n = input ("enter scores :".capitalize())

l = n.split()

for i in range (len (l)):
   Sum += float(l[i])

ave = Sum / len (l)

print ("the average score is : {:.2f}".format (ave))
