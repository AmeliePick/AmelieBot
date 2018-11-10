# -*- coding: utf-8 -*

# === The synthesis module ====


import os, random, playsound
from pygame import mixer
from gtts import gTTS


def speak(speech):

    Old_name_mp3 = "old"
    
    Send_in_Google = gTTS(text = speech, lang = "ru")

        #take name of file
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    file = str(r2)+"sound"+str(r1) +".mp3"

        #get result from Google 
    Send_in_Google.save(file)
    
        
        #play sound
    playsound.playsound(file)
        #delete file from drive
    os.remove(file)
