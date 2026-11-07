import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()

def speak(text):
    print("Assistant:",text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

speak("Hello iam your assistant how can i help you?")