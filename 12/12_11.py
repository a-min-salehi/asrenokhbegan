def  fib(n):      # 0 1 1 2 3 5 8 13 21 34 ...
    if n == 0 or n == 1 :
        return n
    return (fib(n-2)+ fib(n-1))

n = int (input('Enter n : '))

for i in range(n+1):
    print(fib(i) , end =" ")
