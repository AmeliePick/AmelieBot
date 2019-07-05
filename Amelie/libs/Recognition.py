# -*- coding: utf-8 -*
from os import system
import speech_recognition as sr
from .configParser import SettingsControl
from libs.AudioManagement import *

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''

# check lang
if SettingsControl.getConfig("settings.ini", "lang") == "RU":
    valuelang = "RU"
else:
    valuelang = "en_US"

initAudio() #TODO: to rebuild 

# Microphone and Recognition
r = sr.Recognizer()
micro = sr.Microphone()


def calibration():
     #Noise calibration
     print(SettingsControl.Print("Silence"))

     with micro as source:
        r.adjust_for_ambient_noise(source)


def REG():
    #Listening to the microphone
    with micro as source:
        playAudio('../Res/Sounds/readytohear.mp3')
        print(SettingsControl.Print("SaySTH"))
        audio = r.listen(source)

    #Speech to text recording
    while(True):
        try:
            Chat_Input = r.recognize_google(audio, language=valuelang)
            print("---> ", Chat_Input)
        
            return Chat_Input.capitalize()

        except sr.UnknownValueError:
            print(SettingsControl.Print("errSay"))
            system("pause")
            continue

        except sr.RequestError:
            raise ConnectionError 
        
