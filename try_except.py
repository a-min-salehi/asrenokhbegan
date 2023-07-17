x = "67"
try:
  print(x+ 3)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
