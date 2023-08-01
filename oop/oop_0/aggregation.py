class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees


class Employee:
    def __init__(self, name):
        self.name = name


employee1 = Employee("John Doe")
employee2 = Employee("Jane smith")

department = Department("Computer Engineering", [employee1, employee2])

print(department.name)
for employee in department.employees:
    print(employee.name)
