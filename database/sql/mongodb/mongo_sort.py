import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://amin:Fg4l5BGKzuisyOHl@cluster0.qkj6xrx.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["users"]
mycol = mydb.customers

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)