#  Text to Speech
import pyttsx3
engine = pyttsx3.init()
# write your name 
name = input("what's your name? ")
engine.say(f"hello {name}")
engine.runAndWait()
