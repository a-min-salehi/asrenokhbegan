import requests

x = requests.get('https://digikala.com/')

print(x.text)
