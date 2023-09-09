import requests
from bs4 import BeautifulSoup

response = requests.get('http://yermilovcentre.org/medias/')
soup = BeautifulSoup(response.content, "html.parser")

for title in soup.find_all('.div > col-12 row no-gutters title-text px-0'):
    print(title.text)

# for images in soup.find('.div'):
#     print(images.text)
    