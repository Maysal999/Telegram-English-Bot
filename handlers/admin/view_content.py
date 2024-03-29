from aiogram import Router,F
from aiogram.types import Message


from data.view_database import ViewDB
from data.get_data import view_options_list
from keyboards.admin.view_data import button_next, button_option
# from keyboards.admin.btn_builder import view_opt

veiw_router = Router()
view_db = ViewDB()


@veiw_router.message(F.text == 'Задачи' )
async def veiw_all_list(message: Message):
    title = ''
    for i in view_db.view_two_with_photo():
        title += i
        if title==i:
            await message.answer(text=view_db(),)
@veiw_router.message(F.text == 'Посмотреть все задачи 👀')
async def view_task(message:Message):
    for k in view_options_list():
        id = k[0]
        for i in view_db.view_two_without_photo(id=id):
            if i[-2] == None:
                await message.answer(i[1],reply_markup=button_option().as_markup())
            else:
                await message.answer(i[1],reply_markup=button_option().as_markup())
@veiw_router.message(F.text == 'посмотреть словари 🗂️')
async def main_r(message:Message):
    db = ViewDB()
    info = ''
    num = 0
    number = 0
    for i in db.word_view():
        if F.data == 'next':
            num +=1
            number += 2
            info = f"слова - {i[1]} значения - {i[2]} "
        elif F.data == 'next':
            num +=1
            number += 2
            info = f"слова - {i[1]} значения - {i[2]} "
        await message.answer()