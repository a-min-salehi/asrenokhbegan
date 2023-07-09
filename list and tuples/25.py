price_buy = {"java": 42, 'arm': 55, 'python': 44, 'c++': 28, 'python': 37}

print(len(price_buy), '\n')

print(price_buy.keys(), '\n')

print(price_buy.values(), '\n')

print(price_buy.get("javascript"), '\n')

print(price_buy.get("c++"), '\n')

print(price_buy, '\n')

price_buy.clear()

print(price_buy, '\n')
