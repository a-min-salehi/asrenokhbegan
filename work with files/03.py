myfile = open('tst.txt', 'a')

lines = ["\n","Line 1\n", "Line 2\n", "Line 3\n"]
myfile.writelines(lines)

myfile.close()

