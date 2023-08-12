import random

mylist = ["tail", "heads","tail"]
tails_count = 0
heads_count = 0

for i in range(50):
    x = random.choice(mylist)
    if x == 'tail':
    	tails_count += 1
    else:
    	heads_count +=1
        
print(tails_count)
print(heads_count)
