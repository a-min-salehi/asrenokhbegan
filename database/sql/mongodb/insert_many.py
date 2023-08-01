import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://amin:Fg4l5BGKzuisyOHl@cluster0.qkj6xrx.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient.users
mycol = mydb.customers

mylist = [
  { "name": "Amy", "family": "jackson"},
  { "name": "Hannah", "address": "Mountain 21","username":"hannah1"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "username": "Ben_1", "address": "Park Lane 38"},
  { "username": "Ben_1", "address": "Central st 954"},
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)