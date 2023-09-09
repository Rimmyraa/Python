from bs4 import BeautifulSoup
import requests
from database import * 

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0'}
           
response = requests.get('https://comfy.ua/ua/smartfon/brand__apple/', headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
devices = soup.select('.products-list-item')

for device in devices:
    item = {
        "name": device.select_one('.products-list-item__name').text,
        "reviews": device.select_one('.products-list-item__reviews').text,
        "price": device.select_one('.products-list-item__actions-price-current').text[:20].replace('₴', '').replace('/n', '').replace(' ', '').strip,
        "old_price": device.select_one('.products-list-item__actions-price-old').text[:20].replace('₴', '').replace('/n', '').replace(' ', '').strip,
        
    }
 
    add_to_database(item)
    # print(item)
 

