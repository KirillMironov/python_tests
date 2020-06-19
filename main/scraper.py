import requests
from bs4 import BeautifulSoup

URL = 'https://www.mvideo.ru/products/noutbuk-apple-macbook-pro-16-tb-i7-2-6-16-512-ssd-sg-mvvj2ru-a-30046921'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                         ' like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(attrs={'e-h1 sel-product-title'}).get_text().strip()
price = soup.find(attrs={'c-pdp-price__current sel-product-tile-price'}).get_text()
converted_price = float(price[0:3]+price[4:7])

print(title)
print(converted_price)



