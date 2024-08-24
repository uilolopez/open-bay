from bd import connected
from models import class__main__data
def get__data(email):
    collection= connected.connected("users")
    document = collection.find_one({'email': email})
    user__objetc=class__main__data.user__load(document["email"],document["password"],document["username"],document["admin"],document["cripto"])
    return user__objetc

def get__post(posts_loader):
    collection= connected.connected("posts")
    for document in collection.find():
        if document["key"] not in posts_loader:
            if document["user__owner"]== "user_owner":
                new_post=class__main__data.post(document["url"],document["title"],document["collection"],document["description"],document["price"],document["key"],document["user__owner"],document["comments"])
                return new_post
    return False
def get__tokens(email):
    collection= connected.connected("posts")
    cards=[]
    for document in collection.find():
        if document["user__owner"]==email:
            dic_token={
                "title": document["title"],
                "collection": document["collection"],
                "url": document["url"],
                "key": document["key"],
                "description": document["description"],
                "user__owner": document["user__owner"],
                "comments":document["comments"],
                "price": document["price"]
            }
            cards.append(dic_token)
    return cards

def get_tokens_trending():
    collection = connected.connected("posts")
    cards = []
    cursor = collection.find().sort("price", -1)
    count = 0
    for doc in cursor:
        if doc.get("user__owner") == "user_owner":
            cards.append(doc)
            count += 1
        if count == 3:
            break
    
    return cards

def get__mails(email):
    collection= connected.connected("mail")
    mails=[]
    for document in collection.find():
        dic__mails={
                "id": document["_id"],
                "email": document["email"],
                "message": document["message"]
        }
        mails.append(dic__mails)
    return mails

def get__users(email):
    collection= connected.connected("users")
    mails=[]
    for document in collection.find():
        dic__mails={
            "username":document["username"], 
            "email": document["email"],
            "password": document["password"],
            "admin": document["admin"],
            "cripto": document["cripto"]
        }
        mails.append(dic__mails)
    return mails