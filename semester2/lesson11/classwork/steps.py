from aiogram.dispatcher.filters.state import StatesGroup, State

class Flow(StatesGroup):
    Number = State()
    PIN = State()
    Cash_out = State()
    Money = State()
    