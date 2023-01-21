import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://caklutfi:toshibaC840.@cluster0.rmbyfax.mongodb.net/?retryWrites=true&w=majority")
db = client.caklufi
collection = db.services

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

collection.update_one({"service": "engagement"},
                      {"$set": {
                          "package-details":{
                                "topaz": [
                                    "1 photographer",
                                    "3 hours event coverage",
                                    "unlimited photos",
                                    "edited 30 photos",
                                    "all files in google drive",
                                    "bonus print 20x 4r",
                                    "789.000"],
                                "saphire": [
                                    "1 hybrid shooter",
                                    "3 hours event coverage",
                                    "unlimited photos",
                                    "edited 35 photos",
                                    "1 minute teaser video",
                                    "all files in google drive",
                                    "bonus print 20x 4r",
                                    "1049.000"],
                                "diamond": [
                                    "1 photographer",
                                    "1 videographer",
                                    "3 hours event coverage",
                                    "unlimited photos",
                                    "edited 40 photos",
                                    "1 minute teaser video",
                                    "2-3 minutes highlight video",
                                    "all files in google drive",
                                    "bonus print 20x 4r",
                                    "voucher discount 10% for wedding",
                                    "1.699.000"]

                                    }}})

fetch = collection.find({})

for i in fetch:
    print(i)



