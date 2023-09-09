import requests
from bs4 import BeautifulSoup

response = requests.get('https://univ.kiev.ua/ua/departments')
soup = BeautifulSoup(response.content, "html.parser")

for faculties in soup.select_one('.b-references'):
    print(faculties.text)

    
    
# response = requests.get('https://shop.karazin.ua/kantselyariya/')
# soup = BeautifulSoup(response.content, "html.parser")

# for pens in soup.select('.catalogCard-info'):
#     print(pens.text.strip())
    

 
# response = requests.get('https://uk.wikipedia.org/wiki/Музеї_Києва#Список_музеїв') 
# soup = BeautifulSoup(response.content , "html.parser") 
 
# for title in soup.select('.wikitable > tbody > tr > td > b'): 
#     print(title.text)   