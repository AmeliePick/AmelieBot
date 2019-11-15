# -*- coding: utf-8 -*

''' Recognizer module
Listens to speech, converts to text and sends it to the chat module for processing.

'''


import pyaudio, wave
import speech_recognition as sr

from os                     import system
from .configParser          import SettingsControl, DisplayText
from libs.AudioManagement   import *



class SpeechRecognition():
    ''' Recognize the speech and convert it in the text.
    '''

    def __init__(self):
        # Microphone and Recognition
        self.r = sr.Recognizer()
        self.micro = sr.Microphone()


    def calibration(self) -> None:
         ''' Noise calibration.

         '''

         print(DisplayText.print("Silence"))

         try:
             with self.micro as source:
                self.r.adjust_for_ambient_noise(source)
         except OSError:
            print(DisplayText.print("microAccesDenied"))
            system("pause")
            calibration()
         return
    

    def recognize(self) -> None:
        while(True):
            # Listening to the microphone
            playAudio('../Res/Sounds/readytohear.wav')
            print(DisplayText.print("SaySTH"))

            with self.micro as source:
                audio = self.r.listen(source)

            # Speech to text recording
            try:
                input_ = self.r.recognize_google(audio, language=SettingsControl.getConfig("settings.ini", "lang"))
                print("---> ", input_)
        
                return input_

            except sr.UnknownValueError:
                print(DisplayText.print("errSay"))
                system("pause")
                continue

            except sr.RequestError:
                raise ConnectionError 

            return



speechRecognition = SpeechRecognition()
