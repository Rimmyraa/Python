import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
from dotenv import load_dotenv
from threading import Thread
import schedule


from utils import check_query
from parse import get_vacancies 
from database import Database

load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()


@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    user = await db.check_user(message.from_id)
    if not user:
        await db.register_user(
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_id
        )
        await message.answer('Дякую за реєстрацію!')
    else:
        await message.answer('Ви вже зареєстровані')
        await message.answer('Привіт.\nВведи свій пошуковий запит.')
    
@dp.message_handler(content_types='text')
async def get_jobs(message: types.Message):
    if not check_query(message.text):
        await message.answer('Будь ласка, введить пошуковий запис через пролбіли')
    else:
        query = message.text.lower().strip()
        await db.insert_search_query(message.from_id, query)
        vacancies = get_vacancies(query)
        print(vacancies)
        for vacancy in vacancies:
            title = vacancy['title']
            company = vacancy['company']
            url = vacancy['url']
            description = vacancy['description']
        
            msg = (f'<b>Вакансія:</b> {title}\n<b>Компанія:</b> {company}\n<b>Опис:</b> {description}\n\n<b>Посилання:</b> {url}')
            await message.answer(text=msg, parse_mode='html', disable_web_page_preview=True)
    
    
if __name__== '__main__':
    executor.start_polling(dp)
    