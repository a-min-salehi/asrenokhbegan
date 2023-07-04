#NOTICE : put the text file in the same directory 
import os

data_file_path = os.path.join(os.path.dirname(__file__), "test.txt")

myfile = open(data_file_path, "r")

txt = myfile.read()

myfile.close()

print(txt)
