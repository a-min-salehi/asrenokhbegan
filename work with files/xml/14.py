import json

# Read recipe book from file
with open('recipes.json', 'r') as f:
    data = json.load(f)

# Display recipe details
for recipe in data['recipes']:
    name = recipe['name']
    ingredients = ', '.join(recipe['ingredients'])
    instructions = recipe['instructions']
    print(f"Recipe: {name}")
    print(f"Ingredients: {ingredients}")
    print(f"Instructions: {instructions}")
    print()

print("Recipe book displayed successfully.")
