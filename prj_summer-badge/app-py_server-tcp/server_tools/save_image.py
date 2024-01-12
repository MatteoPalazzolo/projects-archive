###################### IMPORT ######################
import mysql.connector
import server_tools as tools

###################### FUNCTIONS ######################

def save_image(id:str, image:bytes) -> dict:

    database = mysql.connector.connect(**tools.SQL)
    cursor = database.cursor()

    cursor.execute("UPDATE users SET photo = %s WHERE qr_id = %s", (image, id))
    database.commit()
    
    cursor.close()
    database.close()

    return {}

###################### TEST ######################

if (__name__ == "__main__"):
    save_image("#8817marcbrac", b"4567864")
    tools.info("users")