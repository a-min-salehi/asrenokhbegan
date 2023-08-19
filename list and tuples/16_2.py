participant_list = [
    ('Alison', 50, 18),
    ('David', 75, 20),
    ('Terence', 75, 12),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return error, age


sorted_list = sorted(participant_list, key=sorter)

print(sorted_list)
