class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, grade, fname, lname):
        super().__init__(fname, lname)
        self.grade = grade

    def printgarde(self):
        print(f"garde = {self.grade}")


p1 = Person("mark", "Zuck")
p1.printname()

s1 = Student("max", "jackson", 12)

s1.printname()
s1.printgarde()
