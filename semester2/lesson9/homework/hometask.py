import requests
from bs4 import BeautifulSoup

response = requests.get('http://yermilovcentre.org/medias/')

soup = BeautifulSoup(response.content, 'html.parser')

for media in soup.select('.row title-text'):
    print(media.text)
