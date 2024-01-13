############ IMPORT ############
from mysql import connector
from pandas import read_csv
import random

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="")
DB_NAME = "summer2021"
USERS_PATH = "users.csv"
ACTIVITIES_PATH = "activities.csv"

######## DEF ########
def generate_id(name:str, surname:str) -> str:
    name = name.lower()
    surname = surname.lower()

    while len(name) < 4:
        name += "_"
    while len(surname) < 4:
        surname += "_"

    _database = connector.connect(**MYSQL,database=DB_NAME)
    _cursor = database.cursor()

    _cursor.execute("SELECT * FROM users")
    i = len(_cursor.fetchall())

    _cursor.close()
    _database.close()

    random.seed(i)
    registNum = str(random.randint(0,9999))
    while len(registNum) < 4:
        registNum = "0" + registNum

    id = "#{0}{1}{2}".format(registNum[:4],name[:4],surname[:4])
    return id

############ CODE ############
#### CREATE DB ####
database = connector.connect(**MYSQL)
cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS {0}".format(DB_NAME))
cursor.close()

database.close()

#### CREATE TABLES ####
database = connector.connect(**MYSQL,database=DB_NAME)
cursor = database.cursor()

cursor.execute(  """CREATE TABLE IF NOT EXISTS users (
                    name VARCHAR(100), surname VARCHAR(100), email VARCHAR(100), status ENUM("Docente","Studente","Tecnico",""),
                    section ENUM("Liceo Scientifico","Liceo Linguistico","Istituto Tecnico",""), classroom VARCHAR(10), photo BLOB,
                    authorization BOOLEAN, birth_date DATE, qr_id VARCHAR(13), PRIMARY KEY (qr_id))"""  )

cursor.execute(  """CREATE TABLE IF NOT EXISTS activities (
                    name VARCHAR(50), day ENUM("Lunedi","Martedi","Mercoledi","Giovedi","Venerdi",""),
                    PRIMARY KEY (name))"""  )

cursor.execute(  """CREATE TABLE IF NOT EXISTS entries (id_entry INT AUTO_INCREMENT, user VARCHAR(13),
                    time_in TIME(0), time_out TIME(0), date DATE,
                    activity_1 VARCHAR(50), activity_2 VARCHAR(50), activity_3 VARCHAR(50),
                    PRIMARY KEY (id_entry, time_in),
                    FOREIGN KEY (activity_1) REFERENCES activities(name),
                    FOREIGN KEY (activity_2) REFERENCES activities(name),
                    FOREIGN KEY (activity_3) REFERENCES activities(name),
                    FOREIGN KEY (user) REFERENCES users(qr_id))"""  )


#### POPULATE USERS ####
user_list = read_csv(USERS_PATH).fillna("").to_dict(orient='records')

for user in user_list:
    id = generate_id(user["name"], user["surname"])
    cursor.execute( """ INSERT INTO users (name, surname, email, status, section, classroom, birth_date, photo, authorization, qr_id)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", tuple(user.values()) + (False, b"", id) )
    database.commit()


#### POPULATE ACTIVITIES ####
activities_list = read_csv(ACTIVITIES_PATH).fillna("").to_dict(orient='records')

for activity in activities_list:
    cursor.execute( """ INSERT INTO activities (name, day) VALUES (%s,%s)""", (activity["activities"],"") )
    database.commit()

cursor.close()
database.close()