import json

called_player = input("Enter the name of the player to delet")

# Open the JSON file and load it into a Python dictionary
with open("team.json", "r") as f:
    data = json.load(f)

# Iterate over the names array and pop (remove) any object that has a name starting with X
for i in range(len(data["players"])):
    if data["players"][i]["name"] == called_player:
        data["players"].pop(i)
        break  # Break out of the loop after deleting one object

# Add a new player to the team
new_player = {
    "name": "Alex Thompson",
    "position": "Defender",
    "number": 6
}
data['players'].append(new_player)

# Open the JSON file again and write the modified dictionary into it
with open("team.json", "w") as f:
    json.dump(data, f)

print("Soccer team roster updated successfully.")
