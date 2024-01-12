###################### IMPORT ######################
import mysql.connector
import time
import server_tools as tools

###################### FUNCTIONS ######################

def update_entries(id:str, activities:list) -> dict:
    print("STA ESEGUENDO: update_entries")
    database = mysql.connector.connect(**tools.SQL)
    cursor = database.cursor()

    cursor.execute("SELECT * FROM entries WHERE user = '{0}' AND time_out = '00:00:00'".format(id))
    entries_fetch = cursor.fetchall()

    date = time.strftime('%Y-%m-%d')
    current_time = time.strftime('%H:%M:%S')

    print("entries_fetch:",entries_fetch)
    
    entring = len(entries_fetch) == 0
    if entring:
        cursor.execute(  
            """INSERT INTO entries (user, time_in, time_out, date,
            activity_1, activity_2, activity_3) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
            (id, current_time, '00:00:00', date, activities[0], activities[1], activities[2]))
        database.commit()
    else:
        cursor.execute("""
            UPDATE entries
            SET time_out = '{0}'
            WHERE user = '{1}' AND time_out = '00:00:00'
        """.format(current_time,id))
        database.commit()
    
    cursor.close()
    database.close()

    return {}


###################### TEST ######################
if (__name__ == "__main__"):
    update_entries("#0908mattpala", ['Film in inglese','',''])
    tools.info("entries")