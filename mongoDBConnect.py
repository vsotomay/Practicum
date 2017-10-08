import pymongo
client = pymongo.MongoClient("mongodb://admin:Utep123@129.108.18.142/test")
db = client.test
db.authenticate("admin", "Utep123")

collection = db.rooms
for item in collection.find():
    print(item)