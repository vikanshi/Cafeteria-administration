import sqlite3
class Database:
    def __init__(self,db): 
     #with sqlite3.connect('Users.db') as db:#Table name is 'Details'
     #columns are 1)primaery key 2)name 3)Phoneno 4)TotalPrice 5)date 6)Billno
     self.conn=sqlite3.connect(db)
     self.c = self.conn.cursor()
     self.c.execute("""CREATE TABLE IF NOT EXISTS Details (id INTEGER PRIMARY KEY,name text,
                        Phoneno int,TotalPrice double,Date text,Billno int)""") 
     self.conn.commit()
     
    def fetch(self):
        self.c.execute("SELECT * FROM Details")
        data=self.c.fetchall()
        return data

    def insert(self,name,phn_no,price,date,bill_no):
        self.c.execute("INSERT INTO  Details VALUES(NULL,?,?,?,?,?)",(name,phn_no,price,date,bill_no))
        self.conn.commit()

    def remove(self,id):
        self.c.execute("DELETE FROM Details WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,name,phn_no,price,date,bill_no):
        self.c.execute("UPDATE Details SET name=?,Phoneno=?,TotalPrice=?,Date=?,Billno=? WHERE id=?",(name,phn_no,price,date,bill_no,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()