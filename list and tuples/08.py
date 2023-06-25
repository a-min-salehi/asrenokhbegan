def del_odd(l):
    for i in l[:]:
        if i % 2 != 0:
            l.remove(i)
    l.sort(reverse=True)
    return l


def remove_odd(l):
    return [x for x in l if x % 2 == 0]


n = input('enter numbers :')
n = n.split()


for i in range(len(n)) :
    n[i] = int(n[i])

print(del_odd(n))
