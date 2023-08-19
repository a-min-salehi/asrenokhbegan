fruits_in_stock = {"apple", "banana", "orange", "kiwi", "grape"}
new_arrivals = {"banana", "watermelon", "kiwi","mango","blueberry"}

common_fruits = fruits_in_stock.intersection(new_arrivals)
common = new_arrivals & fruits_in_stock

print("Common fruits between stock and new arrivals:")
print(common_fruits)
print(common)
