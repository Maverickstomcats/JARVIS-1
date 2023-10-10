import pyttsx3
import datetime
engine = pyttsx3.init()
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

    speak("hello this is JARVIS.")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# hour = i minuites = m seconds =S 
    speak("the current time as of right now is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(month)
    speak(day)
    speak(year)
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("good afternoon sir!")
    elif hour >=18  and hour <24:
        speak("good evening sir!")
    else:
        speak("good night sir!")
def wishme():
    speak("welcome back sir!")
    time()
    date()
    speak("Jarvis at your service, how can i help you today?")
#while True:
 #   voice = int(input("Press one for a male voice, or two for a female voice.")) 
  #  audio = input("enter the text to convert it into speech:  ")
#     speak(audio)
    
   # getvoices(voice)
#time()
#greeting()
#ime()
#wishme()

def takeCommandCMD():
    query = input("please tell me how i can help you today?")
    return query


if __name__ == "__main__":
