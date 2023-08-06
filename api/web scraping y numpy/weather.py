import requests

params = {
  'access_key': '7f98192797a8978433ec110098505805',
  'query': 'Yazd '
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

city = params['query']

condition = api_response['current']['weather_descriptions'][0]

temperature = api_response['current']['temperature']

print(city,condition,temperature,'°C')

