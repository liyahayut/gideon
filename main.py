import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile
import os
import time
import datetime
import webbrowser
import spacy
from tools import speak,listen,log_memory
import wikipedia

nlp = spacy.load("en_core_web_sm")

def main():
    speak("Hello, how can I help you?")

    while True:
        command = listen()
        if command:
            process_command(command)
        time.sleep(0.1)
        log_memory(command)


def process_command(command):
    if not command:
        return
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}.")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}.")
    elif "hello" in command or "hi" in command:
        speak("Hello. How can I assist you?")
    elif "your name" in command or "who are you" in command:
        speak("I am Gideon")
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            speak(wikipedia.summary({search_term}))
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("Please specify what to search for.")
    elif "calculate" in command:
        expression = command.replace("calculate", "").strip()
        try:
            result = eval(expression)
            speak(f"The result is {result}")
        except:
            speak("Unable to calculate.")
    elif "turn off" in command:
        speak("Shutting down.")
        exit(0)
    else:
        speak("Command not recognized.")

if __name__ == "__main__":
    main()