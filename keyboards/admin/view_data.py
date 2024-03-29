from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

from data.view_database import ViewDB
from data.get_data import view_options_list
def button_next():
    button = InlineKeyboardBuilder()
    button.add(InlineKeyboardButton(InlineKeyboardButton(text='⏩',callback_data='next')))
    return button

def button_option():
    button1 = InlineKeyboardBuilder()
    button1.add(InlineKeyboardButton(InlineKeyboardButton(text='⏪', callback_data='back')))
    button = InlineKeyboardBuilder()
    simvols = ['⏪','back','⏩','next']
    num = 0
    db = ViewDB()
    for i in view_options_list():
        title = i[0]
        option = i[-1].split(' ')
        
        for j in option:
            button.row(InlineKeyboardButton(text=j,callback_data=j))
            button.as_markup()
        button.attach(button_next())
        button.attach(button1)
        return button
# def button_option_user():
#     db = ViewDB()
#     id = 0
#     button = InlineKeyboardBuilder()
#     simvols = ['⏪','back','⏩','next']
#     num = 0
#     for h in db.view_two_with_photo():
#         id = h[0]
    
#         for i in db.view_options(id=id):
#             title = i[0]
#             option = i[-1].split(' ')
            
#             for j in option:
#                 button.row(InlineKeyboardButton(text=j,callback_data=j))
#         # button.button(text=simvols[num],callback_data=simvols[num+1])
#         # button.button(text=simvols[num+2],callback_data=simvols[num+3])
#                 return button.as_markup()
