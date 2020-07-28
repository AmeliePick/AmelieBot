# -*- coding: utf-8 -*-



from lib.audio.recognition     import SpeechRecognition
from lib.audio.processing      import playAudio



def voiceInput() -> str:
    voice = SpeechRecognition()
    voice.calibration()

    playAudio("../resources/Sounds/readytohear.wav")
    return voice.recognize()
