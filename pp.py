

import requests
from bs4 import BeautifulSoup

url ='https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
div = soup.find('div', class_="product_price")
print(div.p.text)



