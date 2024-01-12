###################### IMPORT ######################
import mysql.connector
import server_tools as tools


###################### FUNCTIONS ######################

def save_authorization(id:str) -> dict:
    database = mysql.connector.connect(**tools.SQL)
    cursor = database.cursor()

    cursor.execute(f"""
        UPDATE users
        SET authorization = True
        WHERE QR_id = '{id}'
    """)
    database.commit()
    
    cursor.close()
    database.close()

    return {}

###################### TEST ######################

if (__name__ == "__main__"):
    tools.info("users")