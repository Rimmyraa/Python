from bs4 import BeautifulSoup

with open('semester2\lesson6\classwork\\films.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

# тут достаём по фильму
# for data in soup.find_all("h3"):
#     print(data.text)

# тут достаём по жанру, году, стране
for data in soup.select('.genre, .year, .country'):
    print(data.text)
    
for data in soup.select('.header > h1'):
    print(data.text)
    
div = soup.select_one('.header > h1')
print(div)

div_2 = soup.find(id='2')
print(div_2.text.strip())