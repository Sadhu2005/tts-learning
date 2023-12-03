import speech_recognition as sr
import pyttsx3 as ts

engine=ts.init()
rate=engine.getProperty('rate')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices)
engine.setProperty('rate',120)
#print(rate)
def speak(text):
    engine.say(text)


    #engine.say("Hi Sadhu I am your girlfriend")
    #engine.say("how can i help you")
    engine.runAndWait()
r=sr.Recognizer()
speak("Hi Sadhu, I am your friend, How are you?")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what"and"about"and"you" in text:
    speak("I am also fine")
speak("what can i do for you??")