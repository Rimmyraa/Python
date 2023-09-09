import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from steps import *
from database import Database

TOKEN='6208550720:AAFH3OhZZ0Kr0uhiKK57f8JAjoqXMcmUR2k'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Welcome!\nPlease, enter your name')
    await Registration.set_name.set()
    
    
@dp.message_handler(state=Registration.set_name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Nice!\nNow, enter your age')
    await Registration.set_age.set()
    

    
@dp.message_handler(state=Registration.set_age)
async def set_age(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Nice!\nNow, enter your email')
    await Registration.set_email.set()


@dp.message_handler(state=Registration.set_email)
async def set_age(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        name = data['name']
        age = data['age']
        email = message.text
        
    user = await dp.check_user(email)
    if not user:
        await dp.register_student(name, age, email)
        await message.answer('U`ve been successfully registered.')
    else:
        await message.answer('User with such email already exists.')  
    await state.finish()
    



if __name__ == '__main__':
    executor.start_polling(dp)