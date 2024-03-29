

from data.database import Base


class ViewDB(Base):
    def view_two_with_photo(self):
        self.cur.execute('select id from two; ')
        
        return self.cur.fetchall()
    def view_two_without_photo(self,id:int):
        self.cur.execute('select * from two where id = %s; ',(id,))
        return self.cur.fetchall()
    def view_options(self,id):
        self.cur.execute("select two.id, two.content, string_agg(o.options,' ') from two join options o on o.task_id = two.id where two.id = %s group by two.id, two.content;",(id,))
        return self.cur.fetchall()
    def word_view(self):
        self.cur.execute('select * from word; ')
        return self.cur.fetchall()