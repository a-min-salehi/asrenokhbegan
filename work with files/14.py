file = open("binaryfile.bin", "r")
content = file.read()
count = len(content)//8
print("Number of bytes:", count)
file.close()
