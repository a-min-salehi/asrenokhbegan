def word_count(file_name):
    file = open(file_name, 'r')
    words = file.read().split()
    print(words)
    file.close()
    print(len(words))


filename = input('Enter the file name : ')

word_count(filename)
