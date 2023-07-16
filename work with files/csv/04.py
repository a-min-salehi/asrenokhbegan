import csv

# Open the CSV file in read mode
with open('sales.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    # Dictionary to store total quantity sold for each product
    total_quantity = {}

    # Iterate over each row in the CSV file
    for row in csv_reader:
        product = row['Product']
        quantity_sold = int(row['QuantitySold'])

        # Update the total quantity for the product
        if product in total_quantity:
            total_quantity[product] += quantity_sold
        else:
            total_quantity[product] = quantity_sold

    # Print the total quantity sold for each product
    for product, quantity in total_quantity.items():
        print(f"{product}: {quantity}")
