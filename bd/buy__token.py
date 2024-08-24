from bd import connected
from models import class__main__data
from bson.objectid import ObjectId
import pymongo
def buy__token__main(token__key,email):
    collection__user=connected.connected("users")
    collection__posts=connected.connected("posts")
    document__user= collection__user.find_one({'email': email})
    document__post = collection__posts.find_one({'key': token__key})
    cripto__user=document__user["cripto"]
    cripto__post=document__post["price"]
    
    if cripto__post<=cripto__user:
        new__cripto__user=cripto__user-cripto__post
        resultado = collection__posts.update_one(
        {
            '_id': ObjectId(document__post["_id"])
        }, 
        {
            '$set': {
                "user__owner":email
            }
        })  
        resultado = collection__user.update_one(
        {
            '_id': ObjectId(document__user["_id"])
        }, 
        {
            '$set': {
                "cripto":new__cripto__user
            }
        })  
        return True
    else:
        return False
    
def donate__token__main(token__key,email):
    collection__user=connected.connected("users")
    collection__posts=connected.connected("posts")
    document__user= collection__user.find_one({'email': email})
    document__post = collection__posts.find_one({'key': token__key})
    cripto__user=document__user["cripto"]
    cripto__post=document__post["price"]
    
    if document__post["user__owner"]==email:
        new__cripto__user=cripto__user+300
        resultado = collection__posts.update_one(
        {
            '_id': ObjectId(document__post["_id"])
        }, 
        {
            '$set': {
                "user__owner":"user_owner",
                "price":(cripto__post+150)
            }
        })  
        resultado = collection__user.update_one(
        {
            '_id': ObjectId(document__user["_id"])
        }, 
        {
            '$set': {
                "cripto":new__cripto__user
            }
        })  
        return True
    else:
        return False
    