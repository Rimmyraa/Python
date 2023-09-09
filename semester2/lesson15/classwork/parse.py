import requests
from bs4 import BeautifulSoup

def get_vacancies(vacancy_title: str):
    correct_title = vacancy_title.replace(' ', '+')
    url = f'https://www.work.ua/jobs-{correct_title}/'\
        
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs_soup = soup.select('.job-link')
    result = []
    
    for job in jobs_soup:
        title = job.select_one('h2 > a').text
        relative_job_url = job.select_one('h2 > a').get('href')
        job_url = f'https://www.work.ua{relative_job_url}'
        company = job.select_one('.add-top-xs > span > b').text
        description = job.select_one('p').text.strip().replace('\n', '').replace('                           ', '').replace('\xa0', ' ')
        print(description)
    
        job_obj = {
            "title": title,
            "url": job_url,
            "company": company,
            "description": description
        }

        result.append(job_obj)
    
    return result

print(get_vacancies('fronted developer'))