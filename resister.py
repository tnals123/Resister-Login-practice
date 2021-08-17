import sqlite3
class Sign_Up:
    def __init__(self):
        pass
    def sign(self):
        self.id=input("아이디를 입력하세요: ")
        self.pw=input('비밀번호를 입력하세요: ')
        self.name=input('이름을 입력하세요: ')
        self.email=input('이메일을 입력하세요: ')
        self.phonenumber=input('전화번호를 입력하세요: ')
        self.conn=sqlite3.connect('whtnals.db')
        self.cur=self.conn.cursor()
        #self.cur.execute("DROP TABLE user")
        #self.cur.execute("CREATE TABLE user (id TEXT,password TEXT,name TEXT,email TEXT,phonenumber TEXT)")
        self.cur.execute("INSERT INTO user VALUES('"+self.id+"','"+self.pw+"','"+self.name+"','"+self.email+"','"+self.phonenumber+"')")
        self.cur.execute("SELECT * FROM user WHERE id='"+self.id+"'")
        self.result=self.cur.fetchall()
        
        
        self.conn.commit()
        self.conn.close()


