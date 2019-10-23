# -*- coding: utf-8 -*
import pyaudio
import wave
import speech_recognition as sr
from os                     import system
from .time                  import Stopwatch
from .configParser          import SettingsControl
from libs.AudioManagement   import *

timer = Stopwatch()

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''

# check lang
if SettingsControl.getConfig("settings.ini", "lang") == "RU":
    valuelang = "RU"
else:
    valuelang = "en_US"




class SpeechRecognition():

    def __init__(self):
        # Microphone and Recognition
        self.r = sr.Recognizer()
        self.micro = sr.Microphone()


    def calibration(self):
         #Noise calibration
         print(SettingsControl.Print("Silence"))

         try:
             with self.micro as source:
                self.r.adjust_for_ambient_noise(source)
         except OSError:
            print(SettingsControl.Print("microAccesDenied"))
            system("pause")
            calibration()


    def REG(self):
        while(True):
            #Listening to the microphone
            with self.micro as source:
                playAudio('../Res/Sounds/readytohear.wav')
                print(SettingsControl.Print("SaySTH"))
                audio = self.r.listen(source)

            #Speech to text recording
            try:
                Chat_Input = self.r.recognize_google(audio, language=valuelang)
                print("---> ", Chat_Input)
        
                return Chat_Input

            except sr.UnknownValueError:
                print(SettingsControl.Print("errSay"))
                system("pause")
                continue

            except sr.RequestError:
                raise ConnectionError 



speechRecognition = SpeechRecognition()