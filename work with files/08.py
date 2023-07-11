import os
if os.path.exists("tst.txt"):
  os.remove("tst.txt")
else:
  print("The file does not exist")
