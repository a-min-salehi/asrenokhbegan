def star(*number):
    s = 0
    print('number of numbers is {} .'.format(len(number)))
    for i in range(len(number)):
        s += number[i]
    print(f'sum is {s}')    
