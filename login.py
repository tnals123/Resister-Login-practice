import sqlite3

class Log_In_1:
    def __init__(self):
        pass
    def start(self):
        self.id=input('아이디를 입력하세요: ')
        self.pw=input('비밀번호를 입력하세요: ')
        self.conn=sqlite3.connect('whtnals.db')
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT id,password FROM user WHERE id = '" +self.id+"' and password = '"+self.pw+"'")
        self.result=self.cur.fetchall()
        
        if len(self.result)==0:
            print('로그인 실패')
        elif len(self.result)!=0:
            print('로그인 성공!')
            self.cur.execute("SELECT * FROM user WHERE id='"+self.id+"' and password = '" +self.pw+"'")
            self.result2=self.cur.fetchall()
            
            print('이름: '+ self.result2[0][2])
            print('이메일: '+ self.result2[0][3])
            print('폰 번호: '+ self.result2[0][4])




