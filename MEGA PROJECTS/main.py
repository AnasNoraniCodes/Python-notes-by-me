# Jarvis

import speech_recognition as s_r
import webbrowser
import pyttsx3

# Initilization
recognizer = s_r.Recognizer()
engine = pyttsx3.init()

# Speak Function

def speak(text):
    # pyttsx3 module statements
    engine.say(text)
    engine.runAndWait()

# If statement with this to do thing well...
if __name__ == '__main__':
    
    # Speak() called
    speak('Hello , I am Muhammad Anas.')

    