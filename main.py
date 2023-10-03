import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, this is Jarvis 2.0")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty("voice",voices[0].id)

    if voice == 2:
        engine.setProperty("voice",voices[1].id)

    speak("hello this is JARVIS. ")
while True:
    voice = int(input("Press one for a male voice, or two for a female voice.")) 
    audio = input("enter the text to convert it into speech:  ")
#     speak(audio)
    
    getvoices(voice)
