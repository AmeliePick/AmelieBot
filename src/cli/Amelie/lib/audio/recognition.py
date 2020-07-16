# -*- coding: utf-8 -*



import speech_recognition as sr



class SpeechRecognition():
    ''' Recognize the speech and convert it in the text.
    '''


    lang: str
    recognizer: sr.Recognizer
    micro: sr.Microphone



    def __init__(self, appLanguage: str):
        self.lang = appLanguage
        self.recognizer = sr.Recognizer()
        self.micro = sr.Microphone()



    def calibration(self) -> None:
         ''' Noise calibration.
         '''

         with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)
         return
    


    def recognize(self) -> str:
        # Listening to the microphone
        with self.micro as _source:
            audio = self.recognizer.listen(source = _source, timeout = 3, phrase_time_limit = 5)

            # Speech to text
            return self.recognizer.recognize_google(audio, language = self.lang.lower())

        return
