import pyttsx3 as ts

engine=ts.init()
rate=engine.getProperty('rate')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
engine.setProperty('rate',150)
print(rate)

engine.say("Hi pritham, How are You")
engine.runAndWait()
