import csv

# Open the CSV file in read mode
with open('grades.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    total_students = 0
    total_grade = 0
    total_percentage = 0

    # Iterate over each row in the CSV file
    for row in csv_reader:
        name = row['Name']
        grade = int(row['Grade'])
        percentage = float(row['Percentage'])

        total_students += 1
        total_grade += grade
        total_percentage += percentage

    # Calculate average grade and percentage
    average_grade = total_grade / total_students
    average_percentage = total_percentage / total_students

    print(f"Average Grade: {average_grade}")
    print(f"Average Percentage: {average_percentage}%")

