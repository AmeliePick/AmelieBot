# -*- coding: utf-8 -*

''' The english voice playing module
Synthesis based on TTS service of IBM Watson. 

'''


from pyaudio import PyAudio
from requests import get
from ibm_watson import TextToSpeechV1

from libs.AudioManagement import playAudio, _exit



text_to_speech = TextToSpeechV1(
    iam_apikey='D6i3r45_nB2pNi_ewnSuZpu4ze_KexO9fBHtL1vs5E56',
    url='https://stream.watsonplatform.net/text-to-speech/api')


def speak(answer) -> None:
    ''' Convert text to speech, save it in .wav file and play it.
    answer: Answer - The object of bot answer
    '''

    with open('TEMP/sound.wav', 'wb') as audio_file:
        audio = text_to_speech.synthesize(text=answer.getOutput(), voice='en-US_AllisonVoice', accept='audio/wav')
        audio_file.write(audio.get_result().content)

    playAudio('TEMP/sound.wav')
    
    if answer.getCode() == 0:
        _exit('TEMP/sound.wav')
    return
