# -*- coding: utf-8 -*

import os, random, playsound
from pygame import mixer
from gtts import gTTS
from Imports import Chat_w_synthesis

#FF = Chat_w_synthesis


def speak():
    

    Old_name_mp3 = "old"

    #Sound device initialization
    #mixer.init()
    
    Send_in_Google = gTTS(text = str(Chat_w_synthesis), lang = "ru")

        #take name of file
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    file = str(r2)+"sound"+str(r1) +".mp3"

        #get result from Google 
    Send_in_Google.save(file)
    
        
    #try:
        #play sound
    playsound.playsound(file)
        #mixer.music.play()
        #delete file from drive
    os.remove(file)
    #except:
        #print(" Check you Internet connetion")

print ()