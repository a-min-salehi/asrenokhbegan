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

    def feed(self):
        self.hunger += 25

    def show_situation(self):
        print(f"{self.name} : hunger = {self.hunger} , happiness = {self.happiness}, energy = {self.energy}")


v1 = VirtualPet("po", "panda")

day = 1
print("game started")
while True:
    print(f"day = {day}")
    choice = input("play game:")
    if choice == "play game":
        if v1.hunger != 0 and v1.energy != 0:
            v1.play_game()
            print("game played,the pet is more happy now")
            v1.show_situation()
        elif v1.hunger == 0:
            print("pet is hungry")
        else:
            print("pet is tiered")
    elif choice == "feed":
        v1.feed()
        print("feed,the pet is full")
        v1.show_situation()
    elif choice == "sleep":
        if v1.hunger != 0:
            v1.sleep()
            print("game slept,the pet is more energetic now")
            v1.show_situation()
            day += 1
        else:
            print("pet is hungry")
    else:
        print("wtf!!!")




