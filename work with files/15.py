import os

file_path = "binaryfile.bin"

if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    print("File size:", file_size, "bytes")
else:
    print("File not found.")
