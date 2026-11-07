import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print("Oasis:",text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Iam listening. Please speak.")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

def execute_command(command):
    if "hello" in command or "hi" in command:
        speak("hello! how can i help you?")
    
    elif "open chrome" in command:
        speak("opening chrome ")
        webbrowser.open("https://www.chrome.com")

    elif "open google" in command:
        speak("Opening google")
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry,command not recognized.")

    return True

speak("Welcome to Oasis voice Assistant!")

while True:
    command = listen()

    if command:
        if not execute_command(command):
            break