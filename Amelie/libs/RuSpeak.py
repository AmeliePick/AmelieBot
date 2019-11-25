# -*- coding: utf-8 -*

''' The russian voice playing module
Based on the gTTS (Google Text-to-Speech). Gets data from a chat file, processes it, 
and writes it to a file .mp3. For module's work needs the Internet connection.

'''


from random     import randint
from gtts       import gTTS
from time       import sleep
from pydub      import AudioSegment

from libs.AudioManagement import playAudio, _exit



def speak(speech) -> None:
    ''' Create .mp3 file with user input and play it.

    '''

    answer = gTTS(text = speech.getOutput(), lang = "ru")
    
    file = "TEMP/sound.mp3"
    answer.save(file)

    # Convert mp3 to wav
    sound = AudioSegment.from_mp3(file)
    sound.export("TEMP/sound.wav", format="wav")

    #play sound
    playAudio("TEMP/sound.wav")


    if speech.getCode() == 0:
        _exit("TEMP/sound.wav", file)
    return
