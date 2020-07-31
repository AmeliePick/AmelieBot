# -*- coding: utf-8 -*-



from lib.audio.recognition     import SpeechRecognition
from lib.audio.processing      import playAudio
from lib.tools.system          import Network



def voiceInput() -> str:
    if not Network.checkNetworkConnection(): raise ConnectionError()

    voice = SpeechRecognition()
    voice.calibration()

    playAudio("../resources/Sounds/readytohear.wav")
    return voice.recognize()
