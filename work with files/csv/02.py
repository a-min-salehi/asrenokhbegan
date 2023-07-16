import csv

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access values using column names as keys
        print(row['Name'], row['Age'], row['City'])
