import requests
from bs4 import BeautifulSoup


# response = requests.get('https://quotes.toscrape.com/')
# # print(response.content)
# soup = BeautifulSoup(response.content, "html.parser")

# for post in soup.select('.text, .author'):
#     print(post.text)


# response = requests.get('https://books.toscrape.com/')
# book_soup = BeautifulSoup(book_response.content, "html.parser")

# with open('info.txt', 'w') as file:
#     for row in book_soup.select('.product_pod > h3 > a'):
#         a = f"{row.text} - {row.get('href')}"
#         file.write(a)
