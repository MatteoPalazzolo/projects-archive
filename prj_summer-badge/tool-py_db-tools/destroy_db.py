############ IMPORT ############
import mysql.connector

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="")
DB_NAME = "summer2021"

############ CODE ############
database = mysql.connector.connect(**MYSQL)
cursor = database.cursor()

cursor.execute("DROP DATABASE " + DB_NAME)
print("DESTROYED")
cursor.close()
database.close()