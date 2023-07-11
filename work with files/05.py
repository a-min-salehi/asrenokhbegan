def wordCount(file_name):
    file = open(file_name,'r')
    words= file.read().split()
    file.close()
    print(len(words))

filename = input('Enter the file name : ')

wordCount(filename)
