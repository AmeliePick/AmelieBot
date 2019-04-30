# -*- coding: utf-8 -*

# === The synthesis module ====

'''
The synthesis is based on gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, and writes it to a file .mp3 for work synthesis need the Internet. 
Due to the algorithm of the library, there is a delay of a few seconds before playback
'''

from os         import remove
from random     import randint
from gtts       import gTTS
from playsound  import playsound



def speak(speech):
    # TODO: fix the deletion of file
    Send_in_Google = gTTS(text = speech.getOut(), lang = "ru")
    
    

    #take name of file
    r1 = randint(1,10000000)

    file = "sound"+str(r1) +".mp3"

    #get result from Google 
    Send_in_Google.save(file)
    
        
    #play sound
    playsound(file)

    #delete file from drive
    remove(file)

    if(speech.getNum() == 0):
        exit(0)