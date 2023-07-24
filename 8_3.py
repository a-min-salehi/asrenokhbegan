import random

mylist = ["tails", "heads"]
while True:
    for i in range(3):
        print(random.choice(mylist))
    a = input("tamayol dari? (y/n)")
    if a == "n":
        break
    else:
        continue
