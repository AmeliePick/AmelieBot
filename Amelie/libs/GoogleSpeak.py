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
import pyaudio
import wave




def speak(speech):
    # TODO: fix the deletion of file
    answer = gTTS(text = speech.getOut(), lang = "ru")
    
    

    #take name of file
    r1 = randint(1,10000000)

    file = "sound"+".mp3"

    answer.save(file)

    #play sound
    # TODO: Fix decoding
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100

    p = pyaudio.PyAudio()
    output = p.open(format=FORMAT,
                            channels=1,
                            rate=RATE,
                            output=True) # frames_per_buffer=CHUNK_SIZE

    with open(file, 'rb') as fh:
        while fh.tell() != os.stat(file).st_size : # get the file-size from the os module
            AUDIO_FRAME = fh.read(CHUNK_SIZE)
            output.write(AUDIO_FRAME)


    if(speech.getNum() == 0):
        exit(0)