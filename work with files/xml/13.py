import json

# Read student records from file
with open('students.json', 'r') as f:
    data = json.load(f)

# Print student information
for student in data['students']:
    name = student['name']
    age = student['age']
    grade = student['grade']
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

print("Student records displayed successfully.")
