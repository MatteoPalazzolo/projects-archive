import pyttsx3, sys

engine = pyttsx3.init()
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[36].id)
engine.say(sys.argv[1:])
engine.runAndWait()