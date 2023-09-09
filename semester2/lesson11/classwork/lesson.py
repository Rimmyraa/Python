import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from steps import Flow
from config import TOKEN

logging.basicConfig(level=logging.INFO) 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await Flow.Number.set()
    await message.answer('Доброго дня, це бот - банкомат.\nДля старту опреції, спочатку, введіть номер картки.')
    
@dp.message_handler(content_types='text', state=Flow.Number)
async def pincod(message: types.Message):
    await Flow.PIN.set()
    await message.answer('Дякую, тепер введіть свій PIN-код')
    
@dp.message_handler(content_types='text', state=Flow.PIN)
async def cashout(message: types.Message):
    await Flow.Cash_out.set()
    balance = 5000
    await message.answer(f'Для зняття грошей, треба визначити який у вас баланс. Баланс на вашому рахунку становить - {balance}\nВизначте сумму, яку бажаєте зняти. Ліміт 5000 грн.')
    
@dp.message_handler(content_types='text', state=Flow.Cash_out)
async def monney(message: types.Message):
    await Flow.Money.set()
    await message.answer('Ви зняйли потрібну сумму, оперція пройшла без питанн. Для повторної операції напишіть /start')
 
    
if __name__=='__main__':
    executor.start_polling(dp)
    
    