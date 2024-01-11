import glob
from win32api import GetSystemMetrics



MARGIN_X, MARGIN_Y = -100, 0
SCREEN_WIDTH, SCREEN_HEIGHT = GetSystemMetrics(0), GetSystemMetrics(1)


# def get_screen_size():
#   return GetSystemMetrics(0), GetSystemMetrics(1)

def get_favicon():
  return "assets/favicon.ico"

def get_images():
  return glob.glob("assets/images/*.png")

def get_audio():
  return glob.glob("assets/audio/*.mp3")