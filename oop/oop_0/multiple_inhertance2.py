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
        # super(Flying, self).__init__(can_fly)
        Flying.__init__(self, can_fly)


blue = Bird("parrot")

blue.fly()

# myFunc , my_func , muy-func , MyFunc ,MYFUNC ,myfunc