import resister
import login

if __name__=="__main__":
    lg=login.Log_In_1()
    res=resister.Sign_Up()
    while True:
        choice=input('1: 로그인, 2: 회원가입 : ')
        if choice =='1':
            lg.start()
        elif choice =='2':
            res.sign()