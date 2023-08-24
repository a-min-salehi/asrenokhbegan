people = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("David", 22), ("Eve", 28)]
#def set_key(x):
 #   return x[1]
sorted_people = sorted(people,key=lambda x: x[1])
print(sorted_people)
