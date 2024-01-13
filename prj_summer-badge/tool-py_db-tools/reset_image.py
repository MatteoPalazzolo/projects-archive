############ IMPORT ############
import mysql.connector as connector

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="", database="summer2021")
ID = "#1203mattpala"

############ CODE ############
db = connector.connect(**MYSQL)
cursor = db.cursor()

cursor.execute(f"SELECT * FROM users WHERE qr_id = '{id}'")
[print(i) for i in cursor]

cursor.execute(f"""
    UPDATE users
    SET photo = {b""}
    WHERE QR_id = '{id}'
""")
db.commit()

cursor.execute(f"SELECT * FROM users WHERE qr_id = '{id}'")
[print(i) for i in cursor]

cursor.close()
db.close()