file = open("tst.txt", "r")
lines = file.readlines()
count = len(lines)
print("Number of lines:", count)
file.close()