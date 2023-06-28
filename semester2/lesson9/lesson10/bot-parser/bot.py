from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv
from keyboard import *


logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot('6251132125:AAEzuykTdK-l6Mcs6_lsyQfDD6apNz9bgXI')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Привіт! Щоб переглянути новини, натисни на кнопку:', reply_markup=news)
    
@dp.message_handler()
async def get_news(message:types.Message, state: FSMContext):
    if message.text == 'Політичні новини':
        await message.answer("Новини були отримані. Обрай їх за дпомогою", reply_markup=choise)
        await state.set_state('read_default_news')
    elif message.tetx == 'Єкономінчні новини':
        await message.answer("Новини були отримані. Обрай їх за дпомогою", reply_markup=choise)
        await state.set_state('read_economic_news')
    
    
@dp.message_query_handler(start='*', tetx='0')
async def end_reading(callback: types.CallbackQuery, state: FSMContext):
    await callback.message('Перегляд завершено. Щоб прочтитати новини зе раз - напишіть "/start"')
    await state.finish()
    
@dp.callback_query_handler



if __name__ == '__main__':
    executor.start_polling(dp)