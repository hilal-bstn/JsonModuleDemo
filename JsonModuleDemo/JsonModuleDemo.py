import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUSer={}
        self.loadUser()
    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı oluşturuldu.")
    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn=True
                self.currentUSer=user
                print('login yapıldı')
                break
            else:
                print('yanlış giriş')
    def logout(self):
        self.isLoggedIn=False
        self.currentUSer={}
        print('çıkış yapıldı')
    def identity(self):
       if self.isLoggedIn==True:
           print(f'username:{self.currentUSer.username}')
       else:
           print('giriş yapılmadı')
    def saveToFile(self):
        with open('users.json','w') as file:
            list=[]
            for user in self.users:
                list.append(json.dumps(user.__dict__))
            json.dump(list,file)
repository=UserRepository()
while True:
    print('Menü'.center(50,'*'))
    secim=input("1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeçiminiz:")
    if secim==5:
        break
    else:
        if secim=='1':
            username=input("Username: ")
            password=input("Password: ")
            email=input("Email: ")
            user=User(username=username,password=password,email=email)
            repository.register(user)

        elif secim=='2':
            if repository.isLoggedIn:
                 print("Birden fazla giriş yapılamaz.")
            else:
                 username=input('username:')
                 password=input('password:')
                 repository.login(username,password)
        elif secim=='3':
            repository.logout()
            
        elif secim=='4':
            repository.identity()
 
        else:
            print("Yanlış Seçim!!")

