import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, this is Jarvis 2.0")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices():
    voices = engine.getProperty('voices')
    print(voices[0].id)
while True: 
    audio = input("enter the text to convert it into speech:  ")
    speak(audio)

