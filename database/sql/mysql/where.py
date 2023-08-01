import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="firstdb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = 'Ocean blvd 2'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
