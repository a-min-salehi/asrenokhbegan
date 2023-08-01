# Method Overriding

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Animal sound")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


animal = Animal("rabbit")
animal.make_sound()

cat = Cat("cat")
cat.make_sound()
