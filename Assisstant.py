import speech_recognition as sr
import pyttsx3
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()

# Dictionary of common applications and their executable paths
applications = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "file explorer": "explorer.exe",
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    # Add more applications and their paths here
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        pass
    return ""

def run_assistant():
    while True:
        command = take_command()
        if command:
            if 'open google' in command:
                talk("Opening Google")
                webbrowser.open("https://www.google.com")
            elif 'search' in command:
                search_query = command.replace('search', '')
                talk(f"Searching Google for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif 'open' in command:
                app_name = command.replace('open', '').strip()
                if app_name in applications:
                    talk(f"Opening {app_name}")
                    os.startfile(applications[app_name])
                else:
                    talk(f"Sorry, I don't know how to open {app_name}")
            elif 'stop recording' in command or 'stop the recording' in command:
                talk("Stopping the recording")
                break
            else:
                talk("I didn't understand that command")

if __name__ == "__main__":
    run_assistant()