import requests
from bs4 import BeautifulSoup

response = requests.get('http://yermilovcentre.org/medias/')
soup = BeautifulSoup(response.content, "html.parser")

for media in soup.select('.row-fluid.row.no-gutters > col-6.px-0'):
    print(media.text)
