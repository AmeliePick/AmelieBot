# -*- coding: utf-8 -*

# === The synthesis module ====

'''

The synthesis is based on gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, and writes it to a file .mp3 for work synthesis need the Internet. 
Due to the algorithm of the library, there is a delay of a few seconds before playback

'''

import os, random, playsound
from pygame import mixer
from gtts import gTTS




def speak(speech):

    Old_name_mp3 = "old"

    try:
    
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

    except AssertionError:
        return 1
