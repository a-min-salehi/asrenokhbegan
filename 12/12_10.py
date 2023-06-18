def fact(n):     #4 
    if n > 1 :
        return n*fact(n-1) # 4 * fact(3) - 3 * fact(2) - 2 * fact(1)
    return 1

n = int(input('Enter n :'))

print(f'{n}! = {fact(n)}')
