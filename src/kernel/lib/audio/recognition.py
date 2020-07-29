# -*- coding: utf-8 -*



import speech_recognition as sr
from ..Singleton import Singleton





class SpeechRecognition(metaclass = Singleton):
    ''' Recognize the speech and convert it in the text.

    The class is a Singleton.

    '''



    lang: str
    recognizer: sr.Recognizer
    micro: sr.Microphone



    def __init__(self, appLanguage: str):
        self.lang = appLanguage
        self.recognizer = sr.Recognizer()
        self.micro = sr.Microphone()

        return



    def calibration(self) -> None:
         ''' Noise calibration.
         '''

         with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)

         return
    


    def recognize(self) -> str:
        try:
            # Listening to the microphone
            with self.micro as _source:
                audio = self.recognizer.listen(source = _source, timeout = 3, phrase_time_limit = 5)

                # Speech to text
                return self.recognizer.recognize_google(audio, language = self.lang)

        except (sr.WaitTimeoutError, sr.UnknownValueError):
            raise ValueError()

        except sr.RequestError:
            exception = ConnectionError()
            exception.errno = 13
            raise exception

        return
