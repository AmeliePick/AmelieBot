# -*- coding: utf-8 -*-


from tools.system     import FileManager
from Singleton        import Singleton

import simpleaudio as sa
from ibm_watson  import TextToSpeechV1
from googletrans import Translator as gTranslator



def playAudio(soundFile: str) -> None:
    wave_obj = sa.WaveObject.from_wave_file(soundFile)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    return



class TextToSpeech(metaclass = Singleton):
    _translator: gTranslator



    def __init__(self):
        self._translator = gTranslator()

        return



    def __call__(self, textSource: str, srcLang: str) -> Exception:
        textSource = self._translator.translate(text = textSource, dest = "en", src = srcLang).text

        text_to_speech = TextToSpeechV1(iam_apikey="D6i3r45_nB2pNi_ewnSuZpu4ze_KexO9fBHtL1vs5E56",
                                            url="https://stream.watsonplatform.net/text-to-speech/api")

        #TODO: make convertation to wave format from ogg;opus
        audio = text_to_speech.synthesize(textSource, voice="en-US_AllisonV3Voice", accept="audio/wav")
        FileManager.writeToFile(audio.get_result().content, "TEMP/sound.wav", "wb")

        return
