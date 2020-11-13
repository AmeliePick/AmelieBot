# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2020   #
#  github.com/AmeliePick  #
# ======================= #


import msvcrt
from os                 import path as os_path
from threading          import Thread
from memory_profiler    import memory_usage

from httpcore._exceptions import ConnectError

#from lib.tools.runtime         import restart
from lib.tools.logger          import Logger
from lib.chat.dialog           import Dialog
from lib.tools.system          import FileManager
from lib.tools.system          import Network
from lib.Settings              import Settings
from lib.Amelie                import Amelie
from cli                       import Console

from re import sub


class AmelieProgramm:
    ''' CLI version of AmelieBot.

    This class is the programm itself.

    '''



    _amelie: Amelie
    _dialog: Dialog
    _logger: Logger
    _console: Console
    _settingsFile: Settings
    _fileManager: FileManager

    _inputMode: object
    _exceptionStack: list



    def __init__(self):
        self._console = Console()
        self._console.printLogo()
        self._exceptionStack = list()

        self._fileManager = FileManager()
        self._logger = Logger()
        self._settingsFile = Settings()

        self._dialog = Dialog('en') if self._settingsFile.getLanguage() == '-' else Dialog(self._settingsFile.getLanguage())

        #---------------------------------------------------------------------------------------------------------------#
        #                                   FILLING THE SETTINGS FILE WITH USER INPUT                                   #

        settingsMethods = self._settingsFile.getMethodsToResolveErrors()
        for methodname, method in settingsMethods.items():
            if methodname == "lang": # print a list of supporting languages and get user input for language setting
                self._console.write(self._dialog.getMessageFor("chooseLang"))

                langs = self._settingsFile.getSupportingLangs()
                for key, value in langs.items():
                    self._console.write('[' + str(key) + ']')
                    self._console.write(value.upper() + ' ')
                self._console.write('\n')

                while(True):
                    langInput = int(self._console.readLine("\n--> "))

                    if langInput in langs.keys():
                        method(langs[langInput])
                        break

                    else:
                        self._console.writeLine(self._dialog.getMessageFor("wrongInput"))

                self._dialog.changeLanguage(self._settingsFile.getLanguage())

            elif methodname == "username": # just get username fron input
                while(True):
                    self._console.writeLine(self._dialog.getMessageFor("getName"))
                    usernameInput = (self._console.readLine("\n--> "))

                    # checking the spelling of the username
                    if len(sub('[\t, \n, \r \s]', '', usernameInput)) >= 2:
                        method(usernameInput)
                        break

            else:
                continue

        #---------------------------------------------------------------------------------------------------------------#


        self._amelie = Amelie(self._settingsFile.getLanguage())

        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AmelieProgramm, cls).__new__(cls)
            return cls.instance

        return cls.instance



    def restart(self) -> None:
        restart()

        return



    def update(self):
        ''' Update all programm logic.

        '''

        if len(self._exceptionStack) > 0:
            excpetion = self._exceptionStack.pop(0)
            raise excpetion

        self._amelie.update()

        return



    def writeToJournal(self, recordTitle: str, value: str) -> None:
        ''' Write an info-record to the journal of the program.
        '''

        self._logger.addRecord(recordTitle, value)

        return



    def changeInputMode(self, enableVoice: bool):
        self._amelie.voice = enableVoice

        if self._amelie.voice: self._inputMode = voiceInput
        else: self._inputMode = self._console.readLine

        return



    def main(self):
        self._console.writeLine('\n' + self._dialog.getMessageFor("enableVoice"))
        enableVoice = self._console.readLine("--> ")
        while (True):
            if enableVoice == "Y" or enableVoice ==  "y":
                enableVoice = True


            elif enableVoice == "N" or enableVoice ==  "n":
                enableVoice = False

            else:
                self._console.writeLine(self._dialog.getMessageFor("wrongInput"))
                enableVoice = self._console.readLine("--> ")
                continue
            break


        username = str(self._settingsFile.getUsername())
        userInput = ""
        if enableVoice == False:
            while(True):
                self._console.write('\n' + username + ": ")
                userInput = self._console.readLine()
                self._console.writeLine("\t\t\tAmelie: " + self._amelie.conversation(enableVoice, userInput))
                
        else:
            while(True):
                self._console.write('\n' + username + ": ")
                chatAnswer = self._amelie.conversation(enableVoice, userInput)
                self._console.write(self._amelie.getUserInput() + '\n')
                self._console.writeLine("\t\t\tAmelie: " + chatAnswer + '\n')

                self._console.write(self._dialog.getMessageFor("wait"))
                msvcrt.getch()
            
        return



    def __del__(self):
        self._amelie.__del__()
        self._fileManager.__del__()






def main() -> int:
    app = AmelieProgramm()
    app.main()

    app.__del__()
    return 0



if __name__ == '__main__':
    main()
