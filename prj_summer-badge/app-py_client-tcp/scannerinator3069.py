######## IMPORT ########
import json
import tkinter as tk
from tkinter import messagebox
import PIL, cv2, os
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import scanner_tools as tools
from threading import Thread
import pyautogui

######## CONSTANTS ########
SCANNER_CAM = 1
PHOTO_CAM = 1
DEBUG_MODE, TEST_ID = False, "#8817marcbrac"

######## GLOBAL ########
qr_id = ""
user_info = {}
chosen = []
window_pos = (0,0)

######## OTHERS ########
def get_window(window_size:tuple):
    window = tk.Tk()
    window.geometry('{0}x{1}+{2}+{3}'.format(* (window_size + window_pos)))
    window.title("SCANNERINATOR-3069")
    window.resizable(False,False)
    return window

def set_window_pos(window):
    global window_pos
    window_pos = (window.winfo_x(), window.winfo_y())

def init_window_pos(window_size:tuple):
    screen_size = pyautogui.size()
    
    window_x = (screen_size[0]/2) - (window_size[0]/2)
    window_y = (screen_size[1]/2) - (window_size[1]/2) - 50

    global window_pos
    window_pos = (int(window_x),int(window_y))

def show_user_windows(_window,_cap):
        _cap.release()
        set_window_pos(_window)
        _window.destroy()
        if user_info == {}:
            user_not_found_window()
        elif len(user_info["image"]) > 10:
            with open(tools.IMAGE_NAME,"wb") as img:
                img.write(user_info["image"])
        photo_window(user_info['name'], user_info['surname'], user_info['classroom'], user_info['entring'])

#homepage
def homepage():
    WINDOW_SIZE = (600,600)
    init_window_pos(WINDOW_SIZE)
    window = get_window(WINDOW_SIZE)
    Title = tk.Label(window, text = "SCANNERINATOR-3069")
    Title.config(font=("Courier", 30))
    Title.pack(pady = 50)
    Button = tk.Button(window, text = "clicca per scannerizzare", command=lambda:[set_window_pos(window),window.destroy(),scannerQR()])
    Button.pack(ipady=20, pady=40)
    window.mainloop()

#scanner QR
def scannerQR():
    window = get_window((600,600))
    cap = cv2.VideoCapture(SCANNER_CAM)
    cap.set(3, 480)
    cap.set(4, 480)
    
    tk_scanner = tk.Label(window)
    tk_scanner.pack()
    def show_vid():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        tk_scanner.imgtk = imgtk
        tk_scanner.configure(image=imgtk)
        global qr_id
        global user_info
        if not DEBUG_MODE:
            for code in decode(frame):
                qr_id = code.data.decode("utf-8")
                user_info = tools.get_user_info(qr_id)
                show_user_windows(window, cap)
        else:
            qr_id = TEST_ID
            user_info = tools.get_user_info(qr_id)
            show_user_windows(window, cap)

        tk_scanner.after(10, show_vid)

    show_vid()    
    window.mainloop()

#utente non trovato
def user_not_found_window():
    window = get_window((500,600))
    Title = tk.Label(window, text = "utente non trovato")
    Title.config(font=("Courier", 30))
    Title.pack(pady = 50)
    Button = tk.Button(window, text = "clicca per tornare alla home", command=lambda:[set_window_pos(window),window.destroy(),homepage()])
    Button.pack()
    window.mainloop()

#foto
def photo_window(name:str, surname:str, classroom:str, entring:bool):
    window = get_window((1200,900))

    def photo():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        smaller_frame = cv2.resize(frame, (0,0), fx=1, fy=1)
        cv2.imwrite(tools.IMAGE_NAME, smaller_frame)

    def chose_window():
        if entring:
            activities()
        else:
            end_window()

    def show_vid():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        tk_scanner.imgtk = imgtk
        tk_scanner.configure(image=imgtk)
        
        tk_scanner.after(10, show_vid)

    subTitle = tk.Label(text="CONFERMA")
    subTitle.config(font=("Courier", 30))
    subTitle.grid(column=0, row=5, padx=5, pady=20, columnspan=2)
    
    Frameb = tk.Frame(window).grid(columnspan=2, row=6)

    if len(user_info['image']) < 10:
        Button1 = tk.Button(window, text="non accettare", command=lambda:[set_window_pos(window),window.destroy(),cap.release(),homepage()])
        Button1.config(width=20)
        Button1.grid(Frameb, columnspan=2, row=6, ipady=20, pady=10,  )

        Button2 = tk.Button(window, text="scatta foto", command=lambda:[set_window_pos(window),window.destroy(),photo(),cap.release(),image_save_window()])
        Button2.config(width=20)
        Button2.grid(Frameb, columnspan=2, row=7, ipady=20, pady=20, )
    else:
        Button1 = tk.Button(window, text="non accettare", command=lambda:[set_window_pos(window),window.destroy(),homepage()])
        Button1.config(width=20)
        Button1.grid(Frameb, columnspan=2, row=6, ipady=20, pady=10,  )

        Button2 = tk.Button(window, text="accetta", command=lambda:[update_exit(),set_window_pos(window),window.destroy(),chose_window()])
        Button2.config(width=20)
        Button2.grid(Frameb, columnspan=2, row=7, ipady=20, pady=20)

    if entring:
        in_out = "entrando"
    else:
        in_out = "uscendo"
    
    Title = tk.Label(text="sta {0}:".format(in_out).upper())
    Title.config(font=("Courier", 30))
    Title.grid(column=0, row=0, padx=5, pady=10, columnspan=2)
    
    Name = tk.Label(text=name.split(" ")[0])
    Name.config(font=("Courier", 20), relief='solid', borderwidth=1, width=15)
    Name.grid(column=0, row=1, padx=20)
    
    Surname = tk.Label(text=surname.split(" ")[0])
    Surname.config(font=("Courier", 20), relief='solid', borderwidth=1, width=15)
    Surname.grid(column=0, row=2, padx=20)
    
    Classroom = tk.Label(text=classroom)
    Classroom.config(font=("Courier", 20), relief='solid', borderwidth=1, width=15)
    Classroom.grid(column=0, row=3, padx=20)
    
    if len(user_info['image']) < 10:
        cap = cv2.VideoCapture(PHOTO_CAM)
        cap.set(3, 5)
        cap.set(4, 5)
        
        tk_scanner = tk.Label(window)
        tk_scanner.grid(column=1, row=1, rowspan=3, padx=15)
        show_vid()

    else:
        image = Image.open(tools.IMAGE_NAME)
    
        image.thumbnail((300,300))
        test = ImageTk.PhotoImage(image)
        ph_lab = tk.Label(image=test)
        ph_lab.image = test
        ph_lab.grid(column=1, row=1, rowspan=3, padx=15)

    window.mainloop()

#salva immagine
def image_save_window():
    window = get_window((450,450))
    
    Title = tk.Label(window, text="Vuoi salvare l'immagine?" )
    Title.config(font=("Courier", 30))
    Title.grid(column=0,row=0,pady = 10)
    image = Image.open(tools.IMAGE_NAME)
    image.thumbnail((300,300))
    test = ImageTk.PhotoImage(image)
    ph_lab = tk.Label(image=test)
    ph_lab.image = test
    ph_lab.grid(row=1, column=0)
    
    tk_btnRedo = tk.Button(window, text="rifare la foto", command=lambda:[set_window_pos(window),window.destroy(),photo_window(user_info['name'], user_info['surname'], user_info['classroom'], user_info['entring'])] )
    tk_btnRedo.grid(row=2,column=0, ipady=10, pady=20,  padx=15, ipadx=30)
    tk_btnSave = tk.Button(window, text="salvare la foto", command=lambda:[set_window_pos(window),window.destroy(),save_image()] )
    tk_btnSave.grid(row=3,column=0, ipady=10, pady=20,  padx=15, ipadx=30)
    window.mainloop()

def save_image():
    with open(tools.IMAGE_NAME,"rb") as img:
        data = img.read()
    #print("image data:",data)
    tools.save_image(qr_id,data)
    os.remove(tools.IMAGE_NAME)

    if user_info['entring']:
        activities()
    else:
        update_exit()
        display_authorization_box()
        end_window()

#attività
def activities():    
    window = get_window((600,500))
    def selected():
        global chosen
        chosen = []
        selection = tk_listbox.curselection()
        for i in selection:
            select = tk_listbox.get(i)
            chosen.append(select)
            
        if len(chosen) > 3:
            warning_box = tk.messagebox.showerror("attenzione", message="troppe attività scelte il numero massimo è 3", icon='info')

        elif len(chosen) == 0:
            sms_box_return = tk.messagebox.askquestion("attenzione", message="nessuna attività scelta, vuoi tornare alla home?", icon='info')
            if sms_box_return == 'yes':
                set_window_pos(window)
                window.destroy()
                homepage()
        else:
            while len(chosen) < 3:
                chosen.append("")
            chosen_to_display = [act for act in chosen if act != ""]
            sms_box = tk.messagebox.askquestion("attenzione", message="Le attività sono: {0}?".format(", ".join(chosen_to_display)), icon='info')
            if sms_box == 'yes':
                set_window_pos(window)
                display_authorization_box()
                window.destroy()
                tools.update_entries(qr_id,chosen)
                end_window()

    Title = tk.Label(window, text="Quali attività\nsi vogliono svolgere?" )
    Title.config(font=("Courier", 25))
    Title.grid(row=0, column=0, pady=10, padx=('10','0'))
    
    tk_listbox = tk.Listbox(window, selectmode = tk.MULTIPLE)
    tk_listbox.grid(row=1, column=0, sticky='ew', pady=20, padx=('20','0'))

    list_scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=tk_listbox.yview)
    list_scroll.grid(row=1, column=1, sticky='ns',pady=20) 
    tk_listbox['yscrollcommand'] = list_scroll.set

    for i in range(len(tools.ACTIVITIES)):
        tk_listbox.insert(int(i), tools.ACTIVITIES[i])
    
    Button = tk.Button(text='avanti', command=selected)
    Button.config(width=20)
    Button.grid(column=0, row=2, ipady=20, pady=10, columnspan=2)

    window.mainloop()

def update_exit():
    if not user_info['entring']:
        tools.update_entries(qr_id,[])

def display_authorization_box():
    if not user_info['authorization']:
        authorization = messagebox.askquestion("attenzione", message="Risulta che l'utente non abbia ancora firmato l'autorizzazione\nL'autorizzazione è stata firmata in questo momento?", icon='info')
        if authorization == 'yes':
            tools.save_authorization(qr_id)

def end_window():
    window = get_window((600,500))
    Title = tk.Label(window,text='buona giornata...')
    Title.config(font=("Courier", 25))
    Title.pack()
    Button = tk.Button(window, text='torna alla home', command=lambda:[set_window_pos(window),window.destroy(),homepage()])
    Button.pack(ipady=10, pady=20, ipadx=30)
    min_user_info =  dict(name=user_info['name'], surname=user_info['surname'], classroom=user_info['classroom'], birth_date=user_info['birth_date'], activities=chosen)
    Thread(target=tools.play_phrase,args=(min_user_info,)).start()
    window.mainloop()

########### CODE ###########
if __name__ == '__main__':
    homepage()