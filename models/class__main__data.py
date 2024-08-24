import pymongo
import random
from bd import connected
class singup__user:
    def __init__(self,email,password) -> None:
        self.email= email
        self.password= password
        user_index=email.find("@")
        user_num=random.randint(100,999)
        num__random=random.randint(0,9)
        self.username=(email[:user_index]+str(user_num)+str(num__random))
        self.admin=False
        self.cripto=2000
    def save__data(self):
        #data= {"username":[self.email], "email":[self.email],"password":[self.password]}
        bace_data=connected.connected("users")
        #users=bace_data.users
        return bace_data.insert_one({
            "username":self.username, 
            "email":self.email,
            "password":self.password,
            "admin":self.admin,
            "cripto":self.cripto
        }).inserted_id
        
class user__load:
    def __init__(self,email,password,username,admin,cripto) -> None:
        self.email=email
        self.password=password
        self.username=username
        self.admin=admin
        self.cripto=cripto
        
class message:
    def __init__(self,email,message) -> None:
        self.email=email
        self.message=message
    def save__message(self):
        #data= {"username":[self.email], "email":[self.email],"password":[self.password]}
        bace_data=connected.connected("mail")
        #users=bace_data.users
        return bace_data.insert_one({
            "email":self.email,
            "message":self.message
        }).inserted_id
        
class post:
    def __init__(self,url,title,collection,description,price,key,owner,commends) -> None:
        self.url=url
        self.title=title
        self.collection=collection
        self.description=description
        self.price=price
        self.key=key
        self.owner=owner
        self.commends=commends
    def save__post(self,new__owner,price):
        pass