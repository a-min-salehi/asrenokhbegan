s = int(input("Enter speed:"))
d = int(input("Enter distance:"))
t = d/s
# 5.83 -> t1 = 5 // , t2 = 83
t1 = int(t//1)
t2 = round(t%1 * 60)
print("time = " , t1,":",t2)
