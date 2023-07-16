def sortf(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    print(lines)
    lines.sort(key=len)
    file.close()
    for i in lines:
        if i == '\n':
            continue
        print(i)


filename = input('Enter the file name : ')

sortf(filename)
