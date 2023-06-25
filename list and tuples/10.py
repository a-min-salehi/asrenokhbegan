def avg(numbers):
    s = 0
    for i in numbers:
        s += i
    return s // len(numbers)

n = int(input('Enter number of participants: '))

slist = []

for i in range(n):
    s = input('Enter scores in a line, using spaces between scores: ')
    scores = [int(score) for score in s.split()]
    s = avg(scores)
    slist.append(s)

print()

for i in slist:
    print('*' * i)
