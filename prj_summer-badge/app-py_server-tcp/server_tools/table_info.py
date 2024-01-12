import mysql.connector
import server_tools as tools


def info(table:str):
    database = mysql.connector.connect(**tools.SQL)
    cursor = database.cursor()

    print("\n")

    cursor.execute("DESCRIBE " + table)
    [print(i) for i in cursor]

    print("\n")

    cursor.execute("SELECT * FROM " + table)
    [print(i) for i in cursor]

    cursor.close()
    database.close()
