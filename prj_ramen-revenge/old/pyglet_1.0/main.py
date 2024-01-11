import tkinter as tk
import random, glob, cv2, vlc, math
import settings
from package_manager import tools
from package_manager import run_game

# import py_libs.tools as tools
# import py_libs.settings as info
# import py_games.ramen as ramen


### CONSTANTS ###

IMAGES = settings.get_images()
AUDIO = settings.get_audio()
WINDOWS_RECT = [
  # [x, y, w, h],
]


### CODE ###

# play soundtrack
p = vlc.MediaPlayer(AUDIO[1])
p.audio_set_volume(50)
p.play()

# create root window
root = tk.Tk()
root.withdraw()
#root.overrideredirect(1)

# sort IMAGES from the bigger to the smaller image
IMAGES.sort(reverse=True, key=tools.get_image_magnitude)


for i, img in enumerate(IMAGES):
  
  # get image size
  im = cv2.imread(img)
  h, w, c = im.shape

  # get random position
  x, y = tools.get_pseudorandom_position(w, h, WINDOWS_RECT) # get_random_position(w, h)

  # create window
  popup = tk.Toplevel(root)
  popup.title('.'*(len(IMAGES)-i))
  popup.resizable(False, False)
  popup.geometry(f"{w}x{h+50}+{x}+{y}")
  popup.iconbitmap(settings.get_favicon())
  #popup.minsize(w, h)
  #popup.maxsize(w, h)
  #popup.overrideredirect(True)
  #popup.wm_attributes('-fullscreen', 'True')

  tk_img = tk.PhotoImage(master=popup, file=img)
  tk_lab_img = tk.Label(popup, image=tk_img)
  tk_lab_img.image = tk_img
  tk_lab_img.pack()
  
  tk_btn = tk.Button(popup, text="Play", width=100, height=10, command=lambda: run_game.create_game_window(img, (x,y)))
  tk_btn.pack()
  #tk_btn.place(relx=.5, rely=1, anchor=tk.S)


root.mainloop()