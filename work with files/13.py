from random import choice

with open("lottery.txt") as file:
    participants = file.read().splitlines()

    print(participants)


winner = choice(participants)

print(winner)
