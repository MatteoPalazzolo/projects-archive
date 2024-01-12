###################### IMPORT ######################
import mysql.connector
import server_tools as tools
from datetime import date, datetime

###################### FUNCTIONS ######################

def get_user_info(id:str) -> dict:
    print(id)
    database = mysql.connector.connect(**tools.SQL)
    cursor = database.cursor()
    cursor.execute("SELECT name, surname, classroom, photo, authorization, birth_date, status FROM users WHERE qr_id = '{0}'".format(id))
    user_fetch = cursor.fetchall()
    cursor.execute("SELECT * FROM entries WHERE user = '{0}' AND time_out = '00:00:00'".format(id))
    entries_fetch = cursor.fetchall()
    cursor.close()
    database.close()

    if len(user_fetch) == 0:
        return {}

    user_info = user_fetch[0]
    print(user_info)
    name, surname, classroom, image, authorization, birth_date = user_info[:6]

    if classroom == "":
        classroom = user_info[6]

    if len(image) < 20:
        image = b""

    if not authorization:
        age = (date.today() - birth_date).days / 365
        if age > 18:
            authorization = 1
    birth_date = birth_date.strftime("%d-%m-%Y")

    entring = (len(user_fetch) > 0) and (len(entries_fetch) == 0)

    return {"name":name,"surname":surname,"classroom":classroom,"birth_date":birth_date,"image":image,"authorization":authorization==1,"entring":entring}


###################### TEST ######################
if (__name__ == "__main__"):
    a = get_user_info("#1203mattpala")
    print(a)