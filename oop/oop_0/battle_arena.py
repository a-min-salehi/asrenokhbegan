from random import randint


class Character:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, enemy):
        damage = randint(1, self.attack_damage)
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} died")


soldier_name = input("enter your name:")

player = Character(soldier_name, 100, 20)
ghol = Character('div sepid', 150, 10)

while True:
    status = input("enter exit for finish the game:")
    if status == 'exit':
        print("exit game")
        break
    else:
        if player.health <= 0:
            print("ghol is won!")
            break
        elif ghol.health <= 0:
            print("player is won!")
            break
        else:
            player.attack(ghol)
            ghol.attack(player)
            print(f'ghol health = {ghol.health} , player health = {player.health}')
