food_items = {"bread","apple" ,"banana","milk","katchup","orange","cheese", "eggs","meat", "yogurt","chips","ice cream"}

is_subset = lambda items: items.issubset(food_items)

dairy_products = {"milk", "cheese", "yogurt","ice cream"}

if is_subset(dairy_products):
    print("Dairy products are a subset of food items")
else:
    print("Dairy products are not a subset of food items")
