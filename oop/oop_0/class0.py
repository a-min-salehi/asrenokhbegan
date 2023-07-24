class Person:
    gender = ""

    def __init__(self, nam, age):
        self.name = nam
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age} years old"

    def greeting(self):
        print(f"hello I'm {self.name}")


p1 = Person("John", 36)

# p1.gender = "man"
# p1.age = input("enter the age")

# print(p1.name)
# print(p1.age)
# print(p1.gender)
print(p1)
p1.greeting()
