# -*- coding: utf-8 -*-



import time


from lib.chat.dialog           import Dialog
from lib.chat.AICore           import Chat

from lib.tools.system          import FileManager
from lib.tools.logger          import Logger
from lib.tools.runtime         import restart

from lib.audio.processing      import playAudio, TextToSpeech
from lib.audio.recognition     import SpeechRecognition

from lib.Settings import Settings

from webbrowser         import open as webbrowser_open
from subprocess         import Popen



class Amelie():
    """CLI version of AmelieBot"""

    _chat: Chat
    _dialog: Dialog
    _settings: Settings
    _fileManager: FileManager
    _logger: Logger
    _voiceRecorder: SpeechRecognition
    _textToSpeech: TextToSpeech

    _stateCode: int
    


    def __init__(self):
        super().__init__()

        self._fileManager = FileManager()
        self._logger = Logger()

        self._settings = Settings()
        
       
        


        language = self._settings.getLanguage()

        self._voiceRecorder = SpeechRecognition(language)
        self._textToSpeech = TextToSpeech()
        self._chat = Chat(language)
        self._dialog = Dialog(language)

        self._stateCode = 1

        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Amelie, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def changeLanguage(self, language: str) -> None:
        self._voiceRecorder = SpeechRecognition(language)
        self._chat = Chat(language)
        self._dialog.changeLanguage(language)

        return



    def doAction(self, inputType: str) -> None:
        def getProgrammPath(name: str) -> str:
                ''' Get the path to the executable file

                '''

                
                file = self._fileManager.readFile("../../DataBase/added_programms.json")             
                for line in file:
                    row = line.split(" = ")
                    
                    if row[0].lower() in name.lower():
                        return row[1].replace('\n', '')
    
                return ''



        if self._chat.getInputType() == "Exit":
            self._stateCode = 0

        elif self._chat.getInputType() == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(self._chat.EditInput()), new = 1)
    
        elif self._chat.getInputType() == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(self._chat.stemming(self._chat.EditInput())), new = 1)
        
        # here we can get an empty answer, when the user says a phrase like "open" and nothing more
        elif self._chat.getInputType() == "Open":
                Popen( getProgrammPath( self._chat.EditInput() ) )

        return



    def chat(self, userInput: str) -> str:
        chatAnswer = self._chat.launch(userInput)

        try:
            self.doAction(self._chat.getInputType())
        except (FileNotFoundError, OSError):
            return self._dialog.getMessageFor("Prog_not_found")
 
        return chatAnswer



    def voiceChat(self) -> str:
        playAudio("../../Res/Sounds/readytohear.wav")

        userInput = str()

        try:
            userInput = self._voiceRecorder.recognize()
        except ValueError:
            userInput = ''

        except ConnectionError:
            self._logger.logWrite()
            return self._dialog.getMessageBy("service_error ")
            

        chatAnswer = self.chat(userInput)

        self._textToSpeech(chatAnswer, self._chat.getLanguage())
        playAudio("TEMP/sound.wav")

        return chatAnswer
    
    
    
    def recorderCalibration(self) -> None:
        self._voiceRecorder.calibration()

        return



    def playSound(self, soundPath: str) -> None:
        playAudio(soundPath)

        return



    def writeToJournal(self, recordTitle: str, value: str) -> None:
        self._logger.addRecord(recordTitle, value)

        return



    def writeLog(self) -> None:
        self._logger.logWrite()

        return



    def update(self) -> Exception:
        if self._stateCode == 0:
            raise SystemExit(0)


        return



    def restart(self) -> None:
        restart()

        return



    def getUserInput(self) -> str:
        return self._chat.getInput()



    def getAppLanguage(self) -> str:
        return self._chat.getLanguage()



    def __del__(self):
        self._fileManager.__del__()
