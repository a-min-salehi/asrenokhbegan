import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://amin:Fg4l5BGKzuisyOHl@cluster0.qkj6xrx.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["users"]
mycol = mydb.customers



myquery = { "username": "Ben_1" }

mycol.delete_one(myquery)