# -*- coding: utf-8 -*-



from audio.recognition     import SpeechRecognition
from audio.processing      import playAudio
from tools.system          import Network



def voiceInput() -> str:
    if not Network.checkNetworkConnection(): raise ConnectionError()

    voice = SpeechRecognition()
    voice.calibration()

    playAudio("../resources/Sounds/readytohear.wav")
    return voice.recognize()
