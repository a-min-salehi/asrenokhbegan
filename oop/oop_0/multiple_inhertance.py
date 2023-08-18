class Animal:
    def __init__(self, species):
        self.species = species


class CanFly:
    def fly(self):
        print(f"{self.species} is flying")


class Bird(Animal, CanFly):
    def __init__(self, species):
        super().__init__(species)


blue = Bird("makao")

blue.fly()
