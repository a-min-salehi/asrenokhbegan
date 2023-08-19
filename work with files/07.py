filename1 = input("Enter the name of the first file: ")
filename2 = input("Enter the name of the second file: ")
character = input("Enter the character to remove: ")

try:
    with open(filename1, "r") as file1, open(filename2, "w") as file2:
        content = file1.read()
        content.split()
        print(content)
        modified_content = ''
        for i in content:
            if i == character:
               modified_content = content.remove(character)
        file2.writelines(modified_content)
        print("Character removed successfully.")
except FileNotFoundError:
    print("File not found.")
