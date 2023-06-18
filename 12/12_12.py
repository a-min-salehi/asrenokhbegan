def check_divisibility(x, n):
    for i in range(1, x+1):
        if n % i != 0:
            print("no")
            return
    print("yes")

x = int(input("Enter a positive integer x: "))
n = int(input("Enter a positive integer n: "))

# Call the function to check divisibility
check_divisibility(x, n)
