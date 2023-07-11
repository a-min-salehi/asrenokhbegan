input_file = "output.txt"
output_file = "decrypted.txt"
shift = 3

try:
    with open(input_file, "r") as file:
        encrypted_content = file.read()
        decrypted_content = ""
        for char in encrypted_content:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = char
            decrypted_content += decrypted_char

    with open(output_file, "w") as file:
        file.write(decrypted_content)

    print("Decryption completed successfully.")
except FileNotFoundError:
    print("File not found.")
