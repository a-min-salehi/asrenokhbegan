import mysql.connector


class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bot_user"
        )

    def add_user(self, name, chat_id, username, client=0, client2=0):
        cursor = self.db.cursor()
        try:
            sql = "INSERT INTO user_table VALUES (%s, %s , %s , %s , %s)"
            val = (name, chat_id,username,None,None)
            cursor.execute(sql, val)
            self.db.commit()
        except:
            pass
        finally:
            pass

    def return_user(self, id):
        cursor = self.db.cursor()
        sql = f"SELECT * FROM user_table WHERE chat_id = {id} "
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            return x

    def update_user(self,id,where,client):
        cursor = self.db.cursor()
        sql = f"UPDATE user_table SET {where} = {client} WHERE chat_id = {id}"
        cursor.execute(sql)
        self.db.commit()

