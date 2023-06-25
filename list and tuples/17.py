students = [("Alice", [80, 85, 90]), ("Bob", [75, 82, 88]), ("Charlie", [90, 95, 92])]
sorted_students = sorted(students, key=lambda x: sum(x[1]), reverse=True)
print(sorted_students)
