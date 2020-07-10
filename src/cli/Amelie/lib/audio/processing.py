# -*- coding: utf-8 -*-

import simpleaudio      as sa
from playsound          import _playsoundWin



def playAudio(soundFile: str, reps=1) -> None:
    wave_obj = sa.WaveObject.from_wave_file(soundFile)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    return



def textToSpeech(self, text: str, lang: str):
    if lang == "ru":
        from gtts       import gTTS
        from pydub      import AudioSegment

        answer = gTTS(text = textToVoice, lang = "ru")
    
        # gTTS converting files only in .mp3 format.
        file = "TEMP/sound.mp3"
        answer.save(file)

        # Convert mp3 to wav
        sound = AudioSegment.from_mp3(file)
        sound.export("TEMP/sound.wav", format="wav")

    else:
        from requests   import get
        from ibm_watson import TextToSpeechV1
        from ..tools.system import FileManager


        text_to_speech = TextToSpeechV1(iam_apikey="H7shGfh_spPgJD837_XmVLgdfsHA8874",
                                        url="https://stream.watsonplatform.net/text-to-speech/api")

        audio = text_to_speech.synthesize(text, voice="en-US_AllisonVoice", accept="audio/wav")
        FileManager.writeToFile(audio.get_result().content, "TEMP/sound.wav", "wb")


    return
