# -*- coding: utf-8 -*

# === The synthesis module ====

'''
The synthesis is based on gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, and writes it to a file .mp3 for work synthesis need the Internet. 
Due to the algorithm of the library, there is a delay of a few seconds before playback
'''

from random     import randint
from gtts       import gTTS
from sys        import exit
from os         import path as os_path
from os         import remove
from time       import sleep

from libs.AudioManagement import playAudio



def _exit(file, player):
    if os_path.exists(file):
        ''' We can use song.__del__()
        # Delete the source of AVbin, close the file and stop the thread.
        # Anyway it will works, because its in a source file:
        # pyglet.media.sources.avbin.py -> line 327 -> __del__(self)
        ================================================================
            Or we can use player.delete() - due to the pyglet.player uses
        # Includes a call of __del__() from pyglet.media.sources.avbin.py
        # Deleting of all child objects of player
        # I added a few changes due to WinError 32. Didn't remove the mp3 file, because other process used it.
        # A new file was saved in Amelie\libs\pyglet\player.py -> Changes: line 171, line 172.

        '''

        player.delete()
        remove(file)

    exit(0)


def speak(speech):

    answer = gTTS(text = speech.getOut(), lang = "ru")
    
    #take name of file
    file = "sound"+".mp3"

    #save to .mp3 file
    answer.save(file)

    #play sound
    player = playAudio(file)

    if speech.getNum() == 0:
        _exit(file, player)
