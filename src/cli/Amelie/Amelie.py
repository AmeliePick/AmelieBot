# -*- coding: utf-8 -*-



import time


from lib.chat.dialog           import Dialog
from lib.chat.AICore           import Chat
from googletrans               import Translator as gTranslator

from lib.tools.system          import FileManager
from lib.tools.logger          import Logger
from lib.tools.runtime         import restart
from lib.tools.iniParser       import IniParser

from lib.audio.processing      import playAudio, textToSpeech
from lib.audio.recognition     import SpeechRecognition



class Amelie():
    """CLI version of AmelieBot"""

    chat: Chat
    dialog: Dialog
    iniParser: IniParser
    fileManager: FileManager
    logger: Logger
    translator: gTranslator
    voiceRecorder: SpeechRecognition
    


    def __init__(self):
        super().__init__()

        self.fileManager = FileManager()
        self.iniParser = IniParser("settings.ini")
        self.logger = Logger()


        language = self.iniParser.getValue("Settings", "lang")

        self.translator = gTranslator()
        self.voiceRecorder = SpeechRecognition(language)
        self.chat = Chat(language)
        self.dialog = Dialog(language)

        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Amelie, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def silentChat(self, userInput: str) -> str:
        return self.chat.launch(userInput)



    def recorderCalibration(self) -> None:
        self.voiceRecorder.calibration()



    def speechChat(self) -> str:
        playAudio("../../Res/Sounds/readytohear.wav")

        userInput = str()

        try:
            userInput = self.voiceRecorder.recognize()
        except ValueError:
            userInput = ''

        except ConnectionError:
            self.logger.logWrite()
            return self.dialog.getMessageBy("service_error ")
            

        chatAnswer = self.chat.launch(userInput)

        lang = self.chat.getLanguage()
        if lang != "en":
            translatedAnswer = self.translator.translate(text = chatAnswer, dest = "en", src = lang).text
            textToSpeech(translatedAnswer, lang)

        else:
            textToSpeech(chatAnswer, lang)

        playAudio("TEMP/sound.wav")

        return chatAnswer



    def playSound(self, soundPath: str) -> None:
        playAudio(soundName)

        return



    def isExit(self) -> Exception:
        if self.chat.getStateCode() == 0:
            raise SystemExit(0)

        return



    def writeToJournal(self, recordTitle: str, value: str) -> None:
        self.logger.addRecord(recordTitle, value)

        return



    def writeLog(self) -> None:
        self.logger.logWrite()

        return



    def restart(self) -> None:
        restart()

        return



    def getMessageFor(self, expression: str) -> str:
        return self.dialog.getMessageBy(expression)



    def getUserInput(self) -> str:
        return self.chat.getInput()



    def getUsername(self) -> str:
        return ''.join(self.fileManager.readFile("../../DataBase/username.json"))



    def getAppLanguage(self) -> str:
        return self.chat.getLanguage()



    def __del__(self):
        self.fileManager.__del__()
