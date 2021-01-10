import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser





listner = sr.Recognizer()

alexa = pyttsx3.init()
female_voice = alexa.getProperty('voices')
alexa.setProperty('voice',female_voice[1].id)


def talk(voice):
    alexa.say(voice)
    alexa.runAndWait()



def take_voice():

        try:
            
            with sr.Microphone() as source:
                print(" talk.....")
                voice = listner.listen(source)
                voice = listner.recognize_google(voice)
                voice = voice.lower()
                

        except:
            pass      
        return voice


def alexa_run():
    command = take_voice()
    if 'play' in command:
        name = command.replace('play','')
        talk('playing' + name)
        pywhatkit.playonyt(name)

    elif 'time' in command:
        time =datetime.datetime.now().strftime('%I: %M %p')
        talk(time)
    elif (('open' in command) and ('youtube' in command)) or ('youtube' in command) or ('YouTube' in command):
        talk("opening youtube")
        searc_query = command.replace("youtube", ' ').replace('open', ' ').replace('in', ' ')
        webbrowser.open('https://youtube.com/results?search_query=' + command)
        
alexa_run()
