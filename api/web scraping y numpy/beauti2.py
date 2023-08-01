from bs4 import BeautifulSoup

page = '''<html>
<body>
<h1>Titr</h1>
<p>hello</p>
<h2>Titr 2</h2>
<p>hello paragraph 2</p>
</body>
</html>
'''

soup = BeautifulSoup(page, "html.parser")

resault = soup.find_all('p')

print(resault[1].text)
