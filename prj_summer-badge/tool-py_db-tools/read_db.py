############ IMPORT ############
from mysql import connector

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="", database="summer2021")

############ CODE ############
database = connector.connect(**MYSQL)
cursor = database.cursor()
'''
print("DESCRIBE users")
cursor.execute("DESCRIBE users")
[print(i) for i in cursor]
'''
print("SELECT users")
#cursor.execute("SELECT * FROM users ORDER BY status ASC")
cursor.execute("SELECT * FROM users WHERE surname='Bracco'")
[print(i) for i in cursor]
'''
print("DESCRIBE activities")
cursor.execute("DESCRIBE activities")
[print(i) for i in cursor]
'''
print("SELECT activities")
cursor.execute("SELECT * FROM activities")
[print(i) for i in cursor]
'''
print("DESCRIBE entries")
cursor.execute("DESCRIBE entries")
[print(i) for i in cursor]
'''
print("SELECT entries")
cursor.execute("SELECT * FROM entries")
[print(i) for i in cursor]

cursor.close()
database.close()