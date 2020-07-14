# -*- coding: utf-8 -*-



from .lib.chat.dialog           import Dialog
from .lib.chat.AICore           import Chat
from .lib.tools.system          import FileManager
from .lib.tools.iniParser       import IniParser

from .lib.audio.processing      import playAudio, textToSpeech
from .lib.tools.system          import readFile



class Amelie():
    """CLI version of AmelieBot"""

    chat: Chat
    dialog: Message
    iniParser: IniParser
    fileManager: FileManager
    


    def __init__(self):
        super().__init__()

        self.fileManager = FileManager()
        self.iniParser = IniParser("settings.ini")


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
        return dialog.getMessageBy(expression)



    def getUsername(self) -> str:
        return readFile("../DataBase/username.json")



    def playSound(self, soundPath: str) -> None:
        playAudio(soundName)

        return



    def isExit(self) -> Exception:
        if self.chat.getStateCode():
            raise SystemExit(0)\

        return
