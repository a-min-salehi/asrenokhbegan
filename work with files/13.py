from random import choice

with open("lottery.txt") as file:
    participants = set(file.read().splitlines())
    print(participants)

winner = choice(list(participants))

print(winner)
