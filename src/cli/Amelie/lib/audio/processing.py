# -*- coding: utf-8 -*-

import simpleaudio      as sa
from ..tools.system     import FileManager


from requests   import get
from ibm_watson import TextToSpeechV1
from ..tools.system import FileManager



def playAudio(soundFile: str, reps=1) -> None:
    wave_obj = sa.WaveObject.from_wave_file(soundFile)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    return



def textToSpeech(textToVoice: str, lang: str):
    text_to_speech = TextToSpeechV1(iam_apikey="D6i3r45_nB2pNi_ewnSuZpu4ze_KexO9fBHtL1vs5E56",
                                        url="https://stream.watsonplatform.net/text-to-speech/api")

    audio = text_to_speech.synthesize(textToVoice, voice="en-US_AllisonVoice", accept="audio/wav")
    FileManager.writeToFile(audio.get_result().content, "TEMP/sound.wav", "wb")
        


    return
