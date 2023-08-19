myfile = open('tst.txt', 'r')

myfile.seek(43)
txt = myfile.readline()

myfile.close()

print(txt)
