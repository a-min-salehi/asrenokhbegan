class VirtualPet:
    def __init__(self, name, species, energy=100, hunger=50, happiness=0):
        self.name = name
        self.species = species
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness

    def sleep(self):
        self.energy = 100
        self.hunger -= 25

    def play_game(self):
        self.energy -= 25
        self.hunger -= 25
        self.happiness += 10


v1 = VirtualPet("po", "panda")

while True:
    print("game started")
    

