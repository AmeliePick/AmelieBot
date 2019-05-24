# -*- coding: utf-8 -*

# === The synthesis module ====

'''
The synthesis is based on gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, and writes it to a file .mp3 for work synthesis need the Internet. 
Due to the algorithm of the library, there is a delay of a few seconds before playback
'''

import os
from random     import randint
from libs.tts   import gTTS
from sys        import exit
from pyglet     import media
from os         import path as os_path
from os         import remove
from time       import sleep



def speak(speech):
    # TODO: fix the deletion of file
    answer = gTTS(text = speech.getOut(), lang = "ru")
    
    

    #take name of file
    r1 = randint(1,10000000)

    file = "sound"+".mp3"

    answer.save(file)

    #play sound
    song = media.load(file)
    song.play()
    sleep(2)
    
    

    if(speech.getNum() == 0):
        #TODO: fix the deletion of sound file
        if os_path.exists(file):
            remove(file)

        exit(0)