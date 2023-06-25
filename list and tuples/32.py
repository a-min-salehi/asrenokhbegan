countries = {"USA": "Washington D.C.", "France": "Paris", "Germany": "Berlin" , "Iran": "Tehran" , "UAE": "Abu Dhabi" , "Thailand" : "Bangkok" , "Spain" : "Madrid" , "UK": "London" , "Russia": "! FBI WARNING !"}
print("welcome, enter a country name to recive its capital name or enter exit .")

while True:
    country = input("\nEnter a country name: ")
    if country == 'exit':
        break
    elif country.capitalize() in countries:
        print("Capital:", countries[country.capitalize()])
    elif country.upper() in countries :
         print("Capital:", countries[country.upper()])
    else:
        print("Country not found.")
