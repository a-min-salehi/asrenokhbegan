from random import choice

with open("lottery.txt") as file:
    participants = set(file.read().splitlines())

winner = choice(list(participants))

print(winner)
