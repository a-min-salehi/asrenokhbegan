def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

result = calculate_fibonacci(6)
print(result)  # Output: 8
