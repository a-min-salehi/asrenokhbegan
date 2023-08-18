class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, grade):
        Person.__init__(self, fname, lname)
        self.grade = grade

    def printgarde(self):
        print(f"garde = {self.grade}")


s1 = Student("max", "jackson", 12)

s1.printname()
s1.printgarde()
