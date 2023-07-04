#NOTICE : put the text file in the same directory

from pathlib import Path

data_file_path = Path(__file__).parent / "test.txt"

myfile = open(data_file_path, "r")

txt = myfile.read()

myfile.close()

print(txt)
