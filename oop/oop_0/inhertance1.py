class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    grade = 0


y = Person("ali", "bahman")
# print(y.grade)
# Use the Person class to create an object, and then execute the printname method:
x = Student("John", "Doe")
x.printname()
print(x.grade)
