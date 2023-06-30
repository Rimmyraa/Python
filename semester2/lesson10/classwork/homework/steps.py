from aiogram.dispatcher.filters.state import StatesGroup, State

class Flow(StatesGroup):
    RegisterState = State()
    Password = State()
    Email = State()
    Name = State()
    End = State()
