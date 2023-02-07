import pymongo

client = pymongo.MongoClient("mongodb+srv://caklutfi:toshibacC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# # client = pymongo.MongoClient(
# #     "mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
# db = client.caklufi
collection = db.client

services = {
    "service": "prewedding",
    "package": ["topaz", "ruby", "bundling"]
}

engagement = {
    "service": "engagement",
    "package": ["topaz", "saphire", "bundling"]
}

wisuda = {
    "service": "graduation",
    "package": ["topaz", "ruby"]
}
haha= ["1 hybrid shooter",
 "3 hours event coverage",
 "unlimited photos",
 "edited 35 photos",
 "1 minute teaser video",
 "all files in google drive",
 "bonus print 20x 4r"]

# collection.update_one({"service": "engagement"},
#                       {"$set": {
#                           "package-details":{
#                                 "topaz": [
#                                     "1 photographer",
#                                     "3 hours event coverage",
#                                     "unlimited photos",
#                                     "edited 30 photos",
#                                     "all files in google drive",
#                                     "bonus print 20x 4r",
#                                     "789.000"],
#                                 "saphire": [
#                                     "1 hybrid shooter",
#                                     "3 hours event coverage",
#                                     "unlimited photos",
#                                     "edited 35 photos",
#                                     "1 minute teaser video",
#                                     "all files in google drive",
#                                     "bonus print 20x 4r",
#                                     "1049.000"],
#                                 "diamond": [
#                                     "1 photographer",
#                                     "1 videographer",
#                                     "3 hours event coverage",
#                                     "unlimited photos",
#                                     "edited 40 photos",
#                                     "1 minute teaser video",
#                                     "2-3 minutes highlight video",
#                                     "all files in google drive",
#                                     "bonus print 20x 4r",
#                                     "voucher discount 10% for wedding",
#                                     "1.699.000"]
#
#                                     }}})

user = {"_id":{"$oid":"63e0d5763c5c4a2e199ea87a"},
        "username":"caklutfi",
        "address":"gresik",
        "col12":"kosong",
        "col14":"kosong",
        "date":"2023 10 10",
        "email":"lutfytalker@gmail.com",
        "file":"jpeg",
        "name":"lutfi",
        "password":"password",
        "phone":"089514220808",
        "service":"package",
        "time":"13.30"
        }

# fetch = collection.find({})
#
# for i in fetch:
#     print(i)
collection.insert_one(user)





