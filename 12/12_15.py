fibonacci = lambda n : n if n <= 1 else  fibonacci(n - 1) + fibonacci(n - 2) 

result = fibonacci(6)
print(result)

'''
def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

result = calculate_fibonacci(6)
print(result)  # Output: 8
'''
