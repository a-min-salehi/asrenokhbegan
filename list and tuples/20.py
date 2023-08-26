s1 = {1, 2, 3, 4, 5}
s2 = {'a', 'b', 2, 4}
s3 = set(range(1, 8, 2))
print(s3)
s4 = {2, 4}

# print(5 not in s1)


print(s1 | s3)
print(s2 | s3)

print(s1 & s3)
print(s2 & s3)

print(s1 - s3)
print(s2 - s3)

print(s1 ^ s3)
print(s2 ^ s3)

print(s4 < s1)
print(s2 < s1)
print(s1 > s4)
