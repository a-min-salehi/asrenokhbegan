import requests
from bs4 import BeautifulSoup
from time import sleep

URL = "https://blogfa.com"
while True :
    page = requests.get(URL)
    page = page.text

    soup = BeautifulSoup(page, "html.parser")

    val = soup.find_all('div',attrs={'class':'card'})

    print('\n\n' ,len(val) , ' objects founded')

    for content in val :
        title = content.find('a')
        print(title.text)
    sleep(100)
