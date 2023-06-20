def swap_first_last_digit(num):
    # Convert the number to a string
    num_str = str(num)

    # Check if the number has more than one digit
    if len(num_str) > 1:
        
        new_num_str = num_str[-1] + num_str[1:-1] + num_str[0] 
        
        new_num = int(new_num_str)
        return new_num
    else:
        # Return the same number if it has only one digit
        return num


num = int(input("Enter a number: "))


new_num = swap_first_last_digit(num)

# Display the new number
print("Number with swapped first and last digits:", new_num)
