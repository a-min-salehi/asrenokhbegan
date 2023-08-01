import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="firstdb"
)
mycursor = mydb.cursor()


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("marry", "Londan,street 20")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")