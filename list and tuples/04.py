def avg(numbers):
    s = 0
    for i in numbers :
        s += int(i)
    return s//len(numbers)

n = int(input('Enter number of participants : '))

slist = []

for i in range(n):
    s = input('Enter scores in a line , use space between scores :\n')
    s = s.split()
    s = avg(s)
    slist.append(s)

print()

for i in slist:
    print('*'*i)
