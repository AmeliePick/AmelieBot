# -*- coding: utf-8 -*



import speech_recognition as sr
from Singleton import Singleton





class SpeechRecognition(metaclass = Singleton):
    ''' Recognize the speech and convert it in the text.

    The class is a Singleton.

    '''



    _lang: str
    _recognizer: sr.Recognizer
    _micro: sr.Microphone



    def __init__(self, appLanguage: str):
        self._lang = appLanguage
        self._recognizer = sr.Recognizer()
        self._micro = sr.Microphone()

        return



    def changeLanguage(self, appLanguage: str) -> None:
        self._lang = appLanguage
        return



    def calibration(self) -> Exception:
         ''' Noise calibration.
         '''

         with self._micro as source:
            self._recognizer.adjust_for_ambient_noise(source)

         return
    


    def recognize(self) -> str:
        try:
            # Listening to the microphone
            with self._micro as _source:
                audio = self._recognizer.listen(source = _source, timeout = 3, phrase_time_limit = 5)
                return self._recognizer.recognize_google(audio, language = self._lang)

        except (sr.WaitTimeoutError, sr.UnknownValueError):
            raise ValueError()

        except sr.RequestError:
            exception = ConnectionError()
            exception.errno = 13
            raise exception

        return
