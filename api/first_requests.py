import requests

# the required first parameter of the 'get' method is the 'url':
x = requests.get('https://www.w3schools.com/python/showpython.asp?filename=demo_requests_get_url')

# print the response text (the content of the requested file):
print(x.text)
