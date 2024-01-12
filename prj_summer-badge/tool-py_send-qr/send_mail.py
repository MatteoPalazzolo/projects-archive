############ IMPORT ############
import os, qrcode, imghdr, smtplib
from email.message import EmailMessage
from mysql import connector

############ CONST ############
MYSQL = dict(host="localhost", user="root", passwd="", database="summer2021")

SUBJECT = "Estate al Moro: Ecco il tuo QR code!"
CONTENT = """Ciao {0}
per gestire al meglio accessi e presenze di questa Estate al Moro ti inviamo questo qr code personale, da esibire per poter entrare. Lo trovi qui sotto, conservalo sul tuo cellulare. La prima volta che parteciperai ad un'attività ti chiediamo di portare con te un documento d'identità. 

Se non ti sei iscritto a nessuna attività, conserva lo stesso il qr code. Potrai usarlo se deciderei di partecipare ai tornei settimanali. Invieremo di settimana in settimana un questionario apposito.

Trovi una sintesi delle attività ed il link al modulo della liberatori (per i minorenni) a questo link: https://www.istitutomoro.it/nx/estate-al-moro/

A presto
Lo staff dell'estate al Moro"""

############ DEF ############
def create_email(name:str, mail:str, QRstring:str):
    path = "./" + QRstring + "_QR"
    qrcode.make(QRstring).save(path + ".png")

    email = EmailMessage()
    email["Subject"] = SUBJECT
    email["From"] = "staff.estate@istitutomoro.edu.it"
    email["To"] = mail
    email.set_content(CONTENT.format(name))
    
    with open(path + ".png", "rb") as img:
        imgData = img.read()

    os.remove(path + ".png")
    
    email.add_attachment(imgData, maintype = 'image', subtype = imghdr.what(None, imgData), filename = "QR_pass.png")
    return email
    
def send_mail(mail_list:list):
    print("SENDING MAILS...")
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("staff.estate@istitutomoro.edu.it", "tvlgalccllz2020")
    for email in mail_list:
        gmail.send_message(email)
    gmail.quit()

############ CODE ############
db = connector.connect(**MYSQL)
cursor = db.cursor()

cursor.execute("SELECT name, email, qr_id FROM users WHERE status != 'Tecnico'")
users_info = cursor.fetchall()

cursor.close()
db.close()

################
email_list = []
send = False
for user in users_info:
    if send:
        new_email = create_email(*user)
        email_list.append(new_email)
    if user[1] == "example@istitutomoro.edu.it":
        send = True

send_mail(email_list)
print("NON SUCCEDE, MA SE SUCCEDE...")