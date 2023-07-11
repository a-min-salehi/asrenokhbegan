import os

old_name = "old_file.txt"
new_name = "new_file.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully.")
else:
    print("File not found.")
