string = input("enter a string: ".capitalize())
number = int(input("enter a number: ")) # 3

chars_in_use = '' # hello welcome

for char in string :
    if string.count(char) == number and char not in chars_in_use: #
        print(char) # e
        chars_in_use += char # '' + 'e' => 'e' - > 'el'

if chars_in_use == '':
    print("there is no such a character")
