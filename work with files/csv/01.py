import csv

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Print each row
        print(row)
