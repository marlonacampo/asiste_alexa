import speech_recognition as sr
import pyttsx3

name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices [0].id)

for voices in voices:
    print(voices)

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:
   with sr.Microphone() as source:
       print("Escuchando...")
       voice = listener.listen(source)
       rec = listener.recognize_google(voice)
       rec = rec.lower()
       if name in rec:
           talk(rec)
except:
    pass
