import csv

# Data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '19', 'London'],
    ['Bob', '17', 'Paris']
]

# Open the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print("Data written to output.csv successfully.")
