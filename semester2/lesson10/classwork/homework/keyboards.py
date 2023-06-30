from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# traffic_off = KeyboardButton(text='Вимкнути')

request_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(request_contact=True, text='Share my contact'))

request1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(text = 'Добре! Давайте розпочнемо'),KeyboardButton(text = 'Чому'))