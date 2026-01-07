import pygame
import tempfile
from gtts import gTTS
import time
import os
import speech_recognition as sr
from datetime import datetime

def speak(text):
    tts = gTTS(text=text, lang='en')
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmpfile.close()
    tts.save(tmpfile.name)
    
    pygame.mixer.init()
    pygame.mixer.music.load(tmpfile.name)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(tmpfile.name)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source)
            command = r.recognize_google(audio, language="en-US")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
        return ""

def log_memory(command):
    dt=datetime.now()
    ts=dt.timestamp()
    with open("memory.txt","a") as f:
        f.write(f"{ts}: {command}\n")