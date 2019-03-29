# -*- coding: utf-8 -*
from os import system
import speech_recognition as sr
from .configParser import Parser, Config

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''

# check lang

valuelang = ""

if Config("settings.ini", "lang") == "RU":
    valuelang = "RU"

else:
    valuelang = "en_US"


def REG():

    # Microphone and Recognition
    r = sr.Recognizer()

    #Microphone check
    micro = sr.Microphone()


    #Noise calibration

    print(Parser("Silence"))
    with micro as source:
        r.adjust_for_ambient_noise(source)

    #Listening to the microphone

    with micro as source:
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
        
