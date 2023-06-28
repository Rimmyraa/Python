import requests 
from bs4 import BeautifulSoup 
 
def parse_default_news(date=None): 
    if not date: 
        response = requests.get('https://www.pravda.com.ua/news/')   
        soup = BeautifulSoup(response.content, 'html.parser') 
 
        heders = soup.select('.article_header > a') 
        links = [] 
        result = [] 
        for link in heders[:3]: 
            l = link.get('href') 
            links.append(l) if l[0:5] == 'https' else 'https://www.pravda.com.ua' + l 
 
        for link in links: 
            link_response = requests.get(link) 
            link_soup = BeautifulSoup(link_response.content, 'html.parser') 
 
 
            try: 
                title = link_soup.select_one('.post__title').text 
            except: 
                title = link_soup.select_one('.post__title').text 
 
             
            try: 
                texts = link_soup.select('.post_text > p') 
            except: 
                texts = link_soup.select('.post_text > p') 
            print(texts) 
 
            news_body = []
            for i in texts:
                article_text = i.text
                news_body.append(f'{article_text}\n')
                
            article_body = ''.join(news_body)
            
            result.append(
                {
                    "link": link,
                    "title": title,
                    "text": article_body
                }
            )
 
        return result
 
def parse_economic_news(date=None): 
        links = [] 
        result = [] 
        for link in heders[:3]: 
            l = link.get('href') 
            links.append(l) if l[0:5] == 'https' else 'https://www.pravda.com.ua' + l 
 
        for link in links: 
            link_response = requests.get(link) 
            link_soup = BeautifulSoup(link_response.content, 'html.parser') 
 
 
            try: 
                title = link_soup.select_one('.post__title').text 
            except: 
                title = link_soup.select_one('.post__title').text 
 
             
            try: 
                texts = link_soup.select('.post_text > p') 
            except: 
                texts = link_soup.select('.post_text > p') 
            print(texts) 
 
            news_body = []
            for i in texts:
                article_text = i.text
                news_body.append(f'{article_text}\n')
                
            article_body = ''.join(news_body)
            
            result.append(
                {
                    "link": link,
                    "title": title,
                    "text": article_body
                }
            )
 
        return result
 
 
if __name__ == '__main__': 
    print(parse_default_news())