from aiogram import Router,F,Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from data.view_database import ViewDB
from data.get_data import view_options_list
from keyboards.admin.view_data import button_next, button_option
from keyboards.rpbtn import main_user

start = Router()



@start.message(CommandStart())
async def main_r(message:Message):
    await message.answer('Welcome to our bot',reply_markup=main_user())


@start.message(F.text == 'изучать словари 🗂️')
async def main_r(message:Message):
    db = ViewDB()
    for i in db.word_view():
            await message.answer(f'слова - <b>{i[1]}</b>\n<b>{i[2]}</b>',parse_mode=ParseMode('HTML'))
@start.message(F.text == 'решить тесты ✏️')
async def view_task(message:Message):
    db = ViewDB()
    for k in view_options_list():
        id = k[0]
        for i in db.view_two_without_photo(id=id):
            if i[-2] == None:
                await message.answer(i[1],reply_markup=button_option().as_markup())
                # await message.answer(' ________________',reply_markup=button_next())
            else:
                await message.answer(i[1],reply_markup=button_option().as_markup())
                # await message.answer('_________________ ',reply_markup=button_next())
@start.message(F.text == 'О нас')
async def view_task(message:Message):
     await message.answer('Цель задача изучать англиский язык бесплатно  на телеграмм бота\n      Контакты\ntelegram: @ibragimov90\n telephone-nomer: +996700300870')
# @start.message(F.text == 'Посмотреть Задачи ✏️')
# async def task_view_tr(message: Message):
#      db = ViewDB()
#      for i in db.view_two_without_photo():
          