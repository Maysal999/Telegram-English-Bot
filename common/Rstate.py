from aiogram.fsm.state import State,StatesGroup
from aiogram.filters.callback_data import CallbackData 

class TaskState(StatesGroup):
    title = State()
    content = State()
    photo = State()
    level = State()
    categoria = State()
    options = State()

class AddWordState(StatesGroup):
    word = State()
    value = State()
    categoria = State()
    photo = State()

class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int


