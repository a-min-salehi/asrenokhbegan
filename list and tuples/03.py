sum_ = 0
n = input ("enter scores :".capitalize())

l = n.split()

#print(l)

for i in range (len (l)):
   sum_ += float(l[i])

ave = sum_ / len (l)

print ("the average score is : {:.2f}".format (ave))

