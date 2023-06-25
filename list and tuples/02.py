months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

while True:
    try:
        n = int(input('Enter a number (1-12): '))
        if 1 <= n <= 12:
            print(months[n-1])
            break
        else:
            print('Invalid number. Please enter a number between 1 and 12.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')
