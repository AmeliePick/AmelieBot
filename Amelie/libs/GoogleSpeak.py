# -*- coding: utf-8 -*

# === The synthesis module ====

'''
The synthesis is based on gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, and writes it to a file .mp3 for work synthesis need the Internet. 
Due to the algorithm of the library, there is a delay of a few seconds before playback
'''

from random     import randint
from libs.tts   import gTTS
from sys        import exit
from os         import path as os_path
from os         import remove
from time       import sleep

from libs.AudioManagement import playAudio



def _exit(file):
    if os_path.exists(file):
        remove(file)

    exit(0)


def speak(speech):
    answer = gTTS(text = speech.getOut(), lang = "ru")
    
    #take name of file
    file = "sound"+".mp3"

    #save to .mp3 file
    answer.save(file)

    #play sound
    playAudio(file)

    if speech.getNum() == 0:
        _exit(file)
