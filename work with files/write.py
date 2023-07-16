file = open("output.txt", "w")
file.write("Hello, Worl!")  # Write a string to the file
lines = ["Line 1", "Line 2", "Line 3"]
file.writelines(lines)  # Write a list of strings as separate lines
file.close()
