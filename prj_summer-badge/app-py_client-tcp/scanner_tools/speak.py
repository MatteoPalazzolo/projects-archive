############# IMPORT #############
import pyttsx3, datetime
from random import randint as rand

############# DEF #############
def play_phrase(user_info:dict):
    engine = pyttsx3.init()

    phrase_list = get_phrase(user_info)
    phrase = randomize_phrase(phrase_list)

    engine.say(phrase)
    #engine.say("")
    engine.runAndWait()

def randomize_phrase(phrase_list:list) -> str:
    return phrase_list[rand(0,len(phrase_list)-1)]

def get_phrase(user_info:dict) -> list:
    name, surname, classroom, birth_date, activities = tuple(user_info.values())
    today_date = datetime.datetime.now().strftime("%d-%m-%Y")
    
    if birth_date == today_date:
        return ["Happy birthday {0}".format(name)]
    
    if rand(0,2) == 0:
        if name == "Matteo" and surname == "Palazzolo":
            return ["mi è sembrato di vedere una montagna","ma sei enorme","si vede che fai palestra"]
        elif name == "Domenico" and surname == "Giubellini":
            return ["non fate mettere musica a quest'uomo","domanda, con quale dei tuoi 40 nickname vuoi che ti chiami?","bella per il mio bro, che è un po' un fra, grandeeeee"]
        elif name == "Ruben" and surname == "Cuttica":
            return ["on,iciaaaan","rubbiiin, domanda, oggi hai portato il freesbee"]
        elif name == "Tommaso" and surname == "Giachetto-Mena":
            return ["bella per kaneki"]
        elif name == "Pietro" and surname == "Sapia":
            return ["spietraquoriamo?"]
        elif name == "Alessandro" and surname == "Guglielmi":
            return ["one,totem"]
        elif name == "Simone" and surname == "Ruffino":
            return ["àh ruffffì, accendi il radar"]
        elif name == "Roberto" and surname == "Monticone":
            return ["ma è un quattro tempi o va a benzina?"]
        elif name == "Alex" and surname == "Corgiat Mecio":
            return ["grazie per l'aiuto, uomo"]
        elif name == "Marco" and surname == "Bracco":
            return ["salve bracco, sono 500€ per aggiungere una frase personalizzata"]
        elif name == "Andrea" and surname == "Morganti":
            return ["stupido è chi lo stupido fa"]
        elif name == "Alberto" and surname == "Focilla":
            return ["saluti preside"]
        elif name == "Lucrezia" and surname == "Caresio":
            return ["Guarda Shrek prima di uscire con Alessio"]
        elif name == "Alessio" and surname == "Martinetto":
            return ["Porta al sushi Lucrezia, ricordati di offrire la cena"]

    if rand(0,2) == 0:
        if ("Chitarra" in activities) and rand(0,4):
            return ["Benvenuto Jimi Hendrix","Benvenuto Brian May"]
        elif ("Fumetto - manga" in activities) and rand(0,4):
            return ["This is not a Jojo reference"]
        elif ("Teatro al moro" in activities) and rand(0,4):
            return ["Essere, o non essere, questo, è il dilemma"]
        elif any("Torneo" in act for act in activities) and rand(0,4):
            return ["Buona fortuna per il torneo"]
        elif ("Arduino" in activities or "Robotica" in activities) and rand(0,4):
            return ["Bip, bip, bup, bup, robot, hahhaha"]
        elif ("Riprese ed editing video" in activities) and rand(0,4):
            return ["Mi passeresti la crack, di Premier"]
        elif ("Altro - free time al Moro" in activities) and rand(0,4):
            return ["Buona bighellonata"]
    
    if classroom != "Docente" or (name == "Marco" and surname == "Bracco"):
        return [
            f"Ciao {name}, spero che tu abbia portato la pizza",
            f"Tok tok, chi è, un {name} che si vuole divertire",
            f"è spawnato un {name} selvatico",
            f"Ciao {name}, benvenuto nella creew",
            f"{name} è qui come predetto dalla profezia",
            f"Benvenuto {name}, concediti un momento per lodare il sole",
            f"Ora {name} partecipa alla festa",
            f"Allarme, allarme, {name} è riuscito ad acherare il sistema. hahahaha scherzo",
            f"{name} è low, raga pushamo",
            f"{name} è appena atterrato sulla pista {rand(1,10)}",
            f"Ciao {name}, benvenuto nella mia palude",
            f"{name} ha posizionato una carta trappola e ha terminato il suo turno",
            f"Fate largo, sta entrando {name}",
            f"Solo {name} può battere Goku",
            f"Ciao {name}, vorrei farti una domanda, hai mai visto Shrek?",
            f"{name} king della festa, tunz, tunz, tunz"
        ]
    else:
        return ["Buongiorno", "Welcome", "Entri pure","Buona Giornata"]

############# CODE #############
if __name__ == "__main__":
    play_phrase({'name':"Matteo","surname":"Palazzolo","classroom":"","birth_date":"20-01-2021","activities":["Difesa personale","",""]})