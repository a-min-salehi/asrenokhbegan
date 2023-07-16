import os

if os.path.exists("tst2.txt"):
    os.remove("tst2.txt")
else:
    print("The file does not exist")
