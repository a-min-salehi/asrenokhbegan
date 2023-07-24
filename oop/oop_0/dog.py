class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.breed} dog is eating")

    def make_sound(self):
        return f"{self.breed}, {self.age} years old dog is barking"

    def run(self):
        print("Running !!!")


d1 = Dog("Neapolitan Mastiff", "Large", 5, "Black")
my_dog = Dog("Maltese", "Small", 2, "White")
d3 = Dog("Chow Chow", "medium", 3, "Brown")

mylist = [d1, my_dog, d3]

for i in mylist:
    print(i.breed)
    print(i.make_sound())
