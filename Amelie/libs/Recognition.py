# -*- coding: utf-8 -*
import time, os
import speech_recognition as sr
from .configParser import Parser, Config

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''

# check lang

valuelang = ""

if Config("settings.ini") == "RU":
    valuelang = "RU"

else:
    valuelang = "en_US"


def REG():

    # Microphone and Recognition
    r = sr.Recognizer()

    #Microphone check
    try:
        micro = sr.Microphone()

    except OSError:
        print(Parser("errMicro"))
        return 1


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
        os.system("pause")

    except sr.RequestError as e:
        print(Parser("service_error") +"{0}".format(e))
        return 1
