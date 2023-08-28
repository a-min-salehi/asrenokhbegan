def reverse_look(d, v):
    for key in d:
        if d[key] == v:
            return key
    return False

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x  = reverse_look(thisdict,"Mutang")
if x:
    print(x)
else:
    print("not found")
