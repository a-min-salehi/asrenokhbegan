#NOTICE : put the text file in the same directory

import sys

data_file_path = os.path.join(sys.path[0], "test.txt")

myfile = open(data_file_path, "r")

txt = myfile.read()

myfile.close()

print(txt)
