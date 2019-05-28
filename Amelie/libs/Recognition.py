# -*- coding: utf-8 -*
from os import system
import speech_recognition as sr
from .configParser import Parser, Config
from libs.AudioManagement import playAudio

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''

# check lang
if Config("settings.ini", "lang") == "RU":
    valuelang = "RU"

else:
    valuelang = "en_US"


# Microphone and Recognition
r = sr.Recognizer()
micro = sr.Microphone()


def calibration():
     #Noise calibration
     print(Parser("Silence"))

     with micro as source:
        r.adjust_for_ambient_noise(source)


def REG():
    global Chat_Input


    #Listening to the microphone
    with micro as source:
        playAudio('../Res/Sounds/readytohear.mp3')
        print(Parser("SaySTH"))
        audio = r.listen(source)

        #Speech to text recording
    try:
        
        Chat_Input = r.recognize_google(audio, language=valuelang)
        print("---> ", Chat_Input)
        
        return Chat_Input.capitalize()

    except sr.UnknownValueError:
        print(Parser("errSay"))
        system("pause")

    except sr.RequestError:
        raise ConnectionError 
        
