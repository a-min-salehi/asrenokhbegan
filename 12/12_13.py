def check_number_order(n):
    # Convert the number to a string
    num_str = str(n)
    
    
    if num_str == ''.join(sorted(num_str)):
        return "Ascending"


    if num_str == ''.join(sorted(num_str, reverse=True)):
        return "Descending"


    return "Not Sorted"


n = int(input("Enter a number: "))

# Call the function to check the order of digits
result = check_number_order(n)

# Display the result
print("The order of digits in the number is:", result)
