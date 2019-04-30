# -*- coding: utf-8 -*

# === The synthesis module ====

from pyaudio import PyAudio
from requests import get
from sys import exit



'''
Synthesis is carried out with the help of IBM Watson. 
In the code, I left my API Kay. If you want a friend to use your Cloud Foundry Services, then simply replace line 65 and enter your data into it.


I  made minor changes to the work of the Watson module
'''


class TtsWatson:

    RATE = 22050
    SAMPWIDTH = 2
    NCHANNELS = 1
    ACCEPT = 'audio/wav'

    def __init__(self, user, password, voice = 'en-US_AllisonVoice',
                 url = 'https://stream.watsonplatform.net/text-to-speech/api',
                 chunk = 2048):
        self.user = user
        self.password = password
        self.voice = voice
        self.url = url
        self.chunk = int(chunk)

    def play(self, text):
        
        req = get(self.url + "/v1/synthesize",
                           auth=(self.user, self.password),
                           params={'text': text, 'voice': self.voice, 'accept': self.ACCEPT},
                           stream=False, verify=True) #changed by AmeliePick

        
        '''

        When playing the voice, there were small suspensions.

        '''
                          

        p = PyAudio()

        stream = p.open(format=p.get_format_from_width(self.SAMPWIDTH),
                        channels=self.NCHANNELS,
                        rate=self.RATE,
                        output=True)
        bytesRead = 0
        dataToRead = b''
        for data in req.iter_content(1):
            dataToRead += data
            bytesRead += 1
            if bytesRead % self.chunk == 0:
                stream.write(dataToRead)
                dataToRead = b''
        stream.stop_stream()
        stream.close()
        p.terminate()


Speak = TtsWatson('a1e788b1-51d6-44b6-afde-4e5e29539c2a', '7mPsS2pAxngj')

def speak(Answer):
    Speak.play(Answer.getOut())
    if Answer.getNum() == 0:
        exit(0)
