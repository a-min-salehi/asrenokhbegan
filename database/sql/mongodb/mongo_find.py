import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://amin:Fg4l5BGKzuisyOHl@cluster0.qkj6xrx.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["users"]
mycol = mydb["customers"]


for x in mycol.find():
  print(x)