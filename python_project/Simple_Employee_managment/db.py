import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees1(
        Id Integer primary key,
        name text,
        age text,
        doj text,
        gender text)"""
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,name,age,doj,gender):
        self.cur.execute("insert into employees1 values (NULL,?,?,?,?)",(name,age,doj,gender))
        self.con.commit()
    #all seect data code
    def fetch(self):
        self.cur.execute("SELECT * from employees1")
        res=self.cur.fetchall()
        #print(res)
        return res
    #delete function
    def remove(self,Id):
        self.cur.execute("delete from employees1 where Id=?",(Id,))
        self.con.commit()

    def update(self,Id,name,age,doj,gender):
        self.cur.execute("update employees1 set name=?, age=?, doj=?, gender=? where Id=? ", (name, age, doj, gender,Id))
        self.con.commit()



o=Database("Employee1.db")
#o.insert("sathishkumar","20","07-10-2004","male")
#o.fetch()
#o.remove("7")
o.update("6","kavi","11","01-01-2001","male")
