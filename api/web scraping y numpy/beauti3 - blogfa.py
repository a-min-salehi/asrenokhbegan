import requests
from bs4 import BeautifulSoup

URL = "https://blogfa.com"
page = requests.get(URL)
page = page.text

soup = BeautifulSoup(page, "html.parser")

val = soup.find_all('div',attrs={'class':'card'})

print(len(val) , ' objects founded')

first_content = val[0]

first_title = first_content.find('a')

print(first_title.text)