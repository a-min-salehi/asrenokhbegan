string = input("enter a string: ".capitalize())

chars_in_use = ''  # hello welcome

for char in string:
    if char not in chars_in_use:  #
        print('count {} = {}'.format(char, string.count(char)))  # e
        chars_in_use += char  # '' + 'e' => 'e' - > 'el'

if len(string) == 0:
    print("there is no character in this string")
