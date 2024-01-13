############ IMPORT ############
from mysql import connector

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="", database="summer2021")

############ CODE ############
database = connector.connect(**MYSQL)
cursor = database.cursor()

print("########## ENTRATE ##########")
cursor.execute("SELECT * FROM entries")
[print(i) for i in cursor]

cursor.close()
database.close()