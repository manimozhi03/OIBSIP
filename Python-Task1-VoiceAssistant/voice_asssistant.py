import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Oasis:",text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening. Please speak.")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("you said:",command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not Understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

command = listen()
speak("You said " +command)