import csv

# Open the CSV file in read mode
with open('employees.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        name = row['Name']
        age = int(row['Age'])
        department = row['Department']

        # Filter employees from the 'Sales' department
        if department == 'Sales':
            print(f"Name: {name}, Age: {age}, Department: {department}")
