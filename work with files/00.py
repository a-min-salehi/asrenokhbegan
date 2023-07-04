#NOTICE : replace the ::mypath:: with the path you want

myfile = open('::mypath::\test.txt', 'r')

txt = myfile.read()

myfile.close()

print(txt)
