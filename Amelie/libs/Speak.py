# -*- coding: utf-8 -*

# === The synthesis module ====

from pyaudio import PyAudio
from requests import get
from ibm_watson import TextToSpeechV1

from libs.AudioManagement import playAudio, _exit



''' Synthesis is carried out with the help of IBM Watson. 
'''

text_to_speech = TextToSpeechV1(
    iam_apikey='D6i3r45_nB2pNi_ewnSuZpu4ze_KexO9fBHtL1vs5E56',
    url='https://stream.watsonplatform.net/text-to-speech/api')



def speak(Answer):

    with open('sound.mp3', 'wb') as audio_file:
        audio = text_to_speech.synthesize(text=Answer.getOut(), voice='en-US_AllisonVoice', accept='audio/mp3')
        audio_file.write(audio.get_result().content)


    player = playAudio('sound.mp3')

        
    
    if Answer.getNum() == 0:
        _exit('sound.mp3', player)
