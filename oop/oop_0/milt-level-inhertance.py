class Animal:
    def __init__(self, species):
        self.species = species


class Flying:
    def __init__(self, can_fly):
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.species} is flying")
        else:
            print(f"{self.species} cannot fly")


class Bird(Animal, Flying):
    def __init__(self, species, can_fly=True):
        super().__init__(species)
        Flying.__init__(self, can_fly)


class Parrot(Bird):
    def __init__(self, species, can_fly=True):
        super().__init__(species, can_fly)

    def make_sound(self):
        print(f"{self.species} is chirping")

    def imitate(self, sound):
        print(f"{self.species} : {sound} {sound}")


blue = Parrot("makao")

blue.make_sound()
blue.fly()
blue.imitate("salam")
