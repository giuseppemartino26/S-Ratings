import mysql.connector


class Database:

    def __init__(self):

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="soccer_ratings")

        self.mycursor = self.mydb.cursor()