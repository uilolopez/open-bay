import random
from models import class__main__data
from bd import connected
from bson.objectid import ObjectId
def xd(document):
    collection= connected.connected("posts")
    num__random= random.randint(0,10)
    prices=[200,500,900,250,300,650,999,400,800,700,750]
    random__price=prices[num__random]
    resultado = collection.update_one(
        {
            '_id': ObjectId(document["_id"])
        }, 
        {
            '$set': {
                "price":random__price
            }
        })  

def xd2():
    collection= connected.connected("posts")
    for document in collection.find():
        xd(document)
    
xd2()