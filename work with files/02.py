file1 = open('tst.txt', 'r')
file2 = open('tst1.txt', 'w')

txt = file1.read()

file2.write(txt)

file1.close()
file2.close()
