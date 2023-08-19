import csv

# Data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alex', '26', 'New York'],
    ['Alice', '17', 'London'],
    ['Bob', '20', 'Paris']
]

# Open the CSV file in write mode
with open('data.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print("Data written to output.csv successfully.")
