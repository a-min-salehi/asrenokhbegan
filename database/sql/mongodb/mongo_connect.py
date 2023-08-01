import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://amin:Fg4l5BGKzuisyOHl@cluster0.qkj6xrx.mongodb.net/?retryWrites=true&w=majority")

print(myclient.list_database_names())

collection = myclient.users

print(collection.list_collection_names())