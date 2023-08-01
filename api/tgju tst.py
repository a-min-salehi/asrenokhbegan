import requests


response = requests.get("http://www.tgju.org/?act=sanarateservice&client=tgju&noview&type=json")

dictt = response.json()
print(dictt)
keys = list(dictt.keys())
print(keys)
