import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.builtin import 
from dotenv import load_dotenv

load_dotenv()

TOKEN = '6140534940:AAHP9O20If2p7JKV0XP-DTQh75oaVPHDGyk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(text=f'Hello {first_name}!\nMy name is Geralt.')

# @dp.message_handler(commands=['info'])
# async def user_info(message: types.Message):
#     first_name = message.from_user.first_name
#     last_name = message 

@dp.message_handler(content_types='text')
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(content_types='text')
async def echo(message: types.Message):
    if message.text == 'погода':
        await message.answer('сегодня хорошая погода, не так ли?')
    else:
        await message.answer(text=f'{message.text}')

@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo_sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)

if __name__ == '__main__':
    executor.start_polling(dp)