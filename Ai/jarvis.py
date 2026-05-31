import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit
import wikipedia

# Voice engine
engine = pyttsx3.init()

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speaking function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Listening function
def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
        return command

    except:
        return ""

# Welcome message
speak("Hello Sir. Jarvis is now online.")

# Main loop
while True:

    command = take_command()

    # Open YouTube
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # Open ChatGPT
    elif "open chat g p t" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    # Open VS Code
    elif "open code" in command:
        speak("Opening Visual Studio Code")

        code_path = r"C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        os.startfile(code_path)

    # Tell time
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    # Search on Google
    elif "search" in command:
        search = command.replace("search", "")
        speak("Searching for " + search)
        pywhatkit.search(search)

    # Wikipedia
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        speak(info)

    # W.App
    elif "WhatsApp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

     # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye Sir")
        break

    # Default response
    elif command != "":
        speak("I did not understand that command.")