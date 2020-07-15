# -*- coding: utf-8 -*-



from lib.chat.dialog           import Dialog
from lib.chat.AICore           import Chat
from lib.tools.system          import FileManager
from lib.tools.logger          import Logger
from lib.tools.runtime         import restart
from lib.tools.iniParser       import IniParser



from lib.audio.processing      import playAudio, textToSpeech



class Amelie():
    """CLI version of AmelieBot"""

    chat: Chat
    dialog: Dialog
    iniParser: IniParser
    fileManager: FileManager
    logger: Logger
    


    def __init__(self):
        super().__init__()

        self.fileManager = FileManager()
        self.iniParser = IniParser("settings.ini")
        self.logger = Logger()


        language = self.iniParser.getValue("Settings", "lang")

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



    def speechChat(self, userInput: str) -> str:
        chatAnswer = self.chat.launch(userInput)
        textToSpeech(chatAnswer, self.chat.lang)

        return chatAnswer



    def getMessageFor(self, expression: str) -> str:
        return self.dialog.getMessageBy(expression)



    def getUsername(self) -> str:
        return ''.join(self.fileManager.readFile("../DataBase/username.json"))



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


    def restart() -> None:
        restart()
