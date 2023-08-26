myfile = open('tst.txt', 'r')

myfile.seek(43)
txt = myfile.readlines()

myfile.close()

print(txt)
