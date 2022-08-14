#import Libaries
from cgi import test
import speech_recognition as sr
import pyaudio

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hydra waiting for you...")
    while True:
        audio = r.listen(source)

        text = r.recognize_google_cloud(audio)

        print(text)
