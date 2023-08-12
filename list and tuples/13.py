numbers = [5, 2, 7, 1,-2, 9]
all_positive = all(number > 0 for number in numbers)
if all_positive:
    print("All positive")
else:
    print("Not all positive")
