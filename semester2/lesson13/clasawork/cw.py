import sqlite3
import requests
from bs4 import BeautifulSoup

def create_table(name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY, name VARCHAR NOT NULL, symbol VARCHAR NOT NULL, price FLOAT NOT NULL);""")
    connection.commit()
    connection.close()

def add_data(name, symbol, price):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO currency (name, symbol, price) VALUES (?, ?, ?);""",(name, symbol, price))
    connection.commit()
    connection.close()

def get_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM currency;""")
    data = cursor.fetchall()
    connection.close()
    return data

response = requests.get('https://privatbank.ua/rates-archive')
soup = BeautifulSoup(response.content, "html.parser")

cur = soup.find_all('div', class_='purchase')
curr = []
for a in cur:
    curr.append(float(a.span.text))
    
add_data('euro', '€', curr[0])
add_data('dollar', '$', curr[1])
add_data('pln', 'zl', curr[2])
print(curr)