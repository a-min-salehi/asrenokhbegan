# generator to print even numbers
def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i


# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
    print(j, end=" ")
