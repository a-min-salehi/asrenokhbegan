
for i in range(101,1000,2): #101
    su = 0 # su = 0
    i_string = str(i) # '101'
    for j in range(3): # 0 1 2
        su += int(i_string[j]) # su -> 0 + 1 + 0 + 1 = 2
    if i % su == 0 :
        print(i)
    else:
        continue
