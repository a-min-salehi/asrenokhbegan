input_file = "input.txt"
output_file = "output.txt"
shift = 3

try:
    with open(input_file, "r") as file:
        content = file.read()
        encrypted_content = ""
        for char in content:
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = char
            encrypted_content += encrypted_char

    with open(output_file, "w") as file:
        file.write(encrypted_content)

    print("Encryption completed successfully.")
except FileNotFoundError:
    print("File not found.")
