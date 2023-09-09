import requests
from bs4 import BeautifulSoup

def get_book(book_title: str):
    correct_title = book_title.replace(' ', '%20').strip()
    HEADERS = {
        'User-Agen' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = f'https://www.yakaboo.ua/ua/search?q={correct_title}'
   
    response = requests.get(url, headers=HEADERS)
   
    soup = BeautifulSoup(response.content, 'html.parser')
   
    books_soup = soup.select('.category-card.category-layout')
    result = []
    
    # print(len(books_soup))
    x = 0
    for book in books_soup:
        x += 1
        title = book.select_one('.ui-card-title.category-card__name').text.strip()
        author = book.select_one('.creator-label').text.strip()
        availability = book.select_one('.ui-shipment-status > span')
        if availability:
            availability = availability.text.strip()
        else:
            availability = book.select_one('.ui-display-book-type > span').text.strip()
        relative_book_url = book.select_one('.category-card-content-wrapper > a').get('href')
        book_url = f'https://www.yakaboo.ua{relative_book_url}'
        poster = book.select_one('.product-image > img').get('src')

        book_obj = {
        'title' : title,
        'author' : author,
        'availability' : availability,
        'url' : book_url,
        'banner': poster
        }

        result.append(book_obj)
        if x > 5:
            break

    return result

print(get_book(' '))


# def get_topics():
#     url = 'https://www.yakaboo.ua/ua/knigi/vibir-chitachiv.html'
#     HEADERS = {
#         'User-Agen' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url, headers=HEADERS)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     topics_soup = soup.select('.slick-slide slick-active slick-current')
#     result = []
#     for topic in topics_soup:
#         title = topic.slect_one('.category-name')