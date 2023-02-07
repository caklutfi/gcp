import pymongo
import datetime



data = {"image":"1.png","title":"Wedding","content":"Nikah menurut bahasa berasal dari kata nakaha yankihu nikahan yang berarti kawin. dalam istilah nikah berarti ikatan suami istri yang sah yang menimbulkan akibat hukum dan hak serta kewajiban bagi suami isteri."}

services = {
    "service": "prewedding",
    "package": ["topaz", "ruby", "bundling"]
}



def fetchall():
    client = pymongo.MongoClient("mongodb+srv://")
    database = client.caklufi
    collection = database.services
    result = collection.find({})
    return result

def fetchone(key):
    client = pymongo.MongoClient("")
    database = client.caklufi
    collection = database.services
    result = collection.find_one({"service": key})
    return result

def create_user(email,username,password,name):
    client = pymongo.MongoClient("mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
    db = client.caklutfi
    collection = db.clients
    collection.insert_one({"email": email,
                           "username": username,
                           "password": password,
                           "name": name
                           })

def find_user(username):
    client = pymongo.MongoClient("mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
    db = client.caklutfi
    collection = db.clients
    result = collection.find_one({"username": username})
    return result

def get_package(service):
    client = pymongo.MongoClient("mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
    db = client.caklutfi
    collection = db.packages
    result = collection.find({"service": service})
    return result




