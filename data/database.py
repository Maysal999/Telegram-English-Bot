from sqlite3 import Cursor
import psycopg2

from config import DBNAME, USER, PASS

conn = psycopg2.connect(f'dbname={DBNAME} user={USER} password={PASS}')
cur = conn.cursor()
class Base():
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn



class AddTaskDB(Base):
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn
    def add_task_with_options(self,content, level_id, photo_id,cate_id):
        self.cur.execute('insert into two(content, level_id, photo_id,cate_id) values(%s,%s,%s,%s)',(content, level_id, photo_id,cate_id,))
        self.conn.commit()
    def add_task_with_options_without_photo(self,content, level_id,cate_id):
        self.cur.execute('insert into two(content, level_id,cate_id) values(%s,%s,%s)',(content, level_id,cate_id,))
        self.conn.commit()
    def add_users(self,fullname, telegram_id, life, balans):
        self.cur.execute('insert into users(fullname, telegram_id, life, balans) values(%s,%s,%s,%s)',(fullname, telegram_id, life, balans))
        self.conn.commit()
    def add_options(self,option, task_id):
        self.cur.execute('insert into options(options, task_id) values(%s,%s)',(option, task_id))
        self.conn.commit()
    def add_words(self,words, value, cate_id,photo_id):
        self.cur.execute('insert into word(words, value, cate_id,photo_id) values(%s,%s,%s,%s)',(words, value, cate_id,photo_id))
        self.conn.commit()

    def add_shop(self,value, user_id):
        self.cur.execute('insert into shop(value, user_id) values(%s,%s)',(value, user_id,))
        self.conn.commit()

    def add_answer(self,answer,task_id):
        self.cur.execute('insert into answer(answer,task_id) values(%s,%s)',(answer,task_id))
        self.conn.commit()
        



# db = view_options_list()
# for i in db:
#     option = i[-1].split()
#     print(option)
# v = ViewDB()
# # v.view_two_with_photo()
# print(v.view_two_with_photo())
# # d = AddTaskDB()
# d.add_task_with_options(content='Oa',level_id='14',cate_id='4',photo_id='bar1')
