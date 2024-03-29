from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main():
    add_task = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Добавить Задача ✏️'),
    ],[KeyboardButton(text='Посмотреть все задачи 👀'),
       KeyboardButton(text='Добавить словарь 📌')
       ],
       [KeyboardButton(text='посмотреть словари 🗂️')],],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder='enter command')
    return add_task


def main_user():
    main = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='решить тесты ✏️'),
        KeyboardButton(text='изучать словари 🗂️')
    ],[
       KeyboardButton(text='О нас')
       ],
            ],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder='enter command')
    return main