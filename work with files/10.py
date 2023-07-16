search_word = input("Enter the word to search: ")
file = open("tst.txt", "r")
for line in file:
    if search_word in line:
        print(line)
file.close()
