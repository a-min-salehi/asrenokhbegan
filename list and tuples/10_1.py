def avg(numbers):
    s = 0
    for i in numbers :
        s += i
    return s//len(numbers)

n = int(input('Enter number of participants : '))

slist = []

for i in range(n):
    s = eval(input('Enter scores in a line , use comma between scores :\n'))
    s = avg(s)
    slist.append(s)

print()

for i in slist:
    print('*'*i)
