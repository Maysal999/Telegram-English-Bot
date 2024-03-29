from data.database import Base
from data.view_database import ViewDB


class GetTaskDB(Base):
    def __init__(self,) -> None:
        self.list_id = {}
    def get_id_level(self,level):
        self.cur.execute('select id from levels where level = %s;',(level,))
        level_id = self.cur.fetchone()
        for l in level_id:
            return l
    def get_id_categoria(self,title):
        self.cur.execute('select id from categoria where title = %s;',(title,))
        cate_id = self.cur.fetchone()
        for l in cate_id:
            return l

    def get_id_two(self,content):
        self.cur.execute('select id from two where content = %s;',(content,))
        two_id = self.cur.fetchone()
        for l in two_id:
            return l
        
    def answer_filters(self, id:int, otvet:str) -> True | False:
        self.cur.execute('select a.answer from answer a join two t t.id = a.task_id  where id = %s;',(id,otvet,))

def view_options_list() -> list|None:
    db = ViewDB()
    data_list = []
    option = []

    for  i in db.view_options(id=32):
        data_list.append(i)
    # print( data_list )
    return data_list
class GetID(Base):
    def __init__(self) -> None:
        self.id_set = set()
        self.id_list = None
    def get_id_two(self):
        self
        self.cur.execute('select id from two;')
        two_id = self.cur.fetchone()
        for l in two_id:
            self.id_set.add(l)
        return list(self.id_set)
    
