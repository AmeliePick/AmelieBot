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

from lib.tools.input           import voiceInput
from lib.tools.runtime         import restart
from lib.tools.logger          import Logger
from lib.chat.dialog           import Dialog  
from lib.tools.system          import FileManager
from lib.Settings              import Settings
from lib.Amelie                import Amelie
from cli                       import Console

from re import sub


class AmelieProgramm:
    ''' CLI version of AmelieBot

    This class is the programm itself.
    
    '''



    _amelie: Amelie
    _dialog: Dialog
    _logger: Logger
    _console: Console
    _settingsFile: Settings
    _fileManager: FileManager

    _inputMode: object



    def __init__(self):
        self._console = Console()
        self._console.printLogo()

        self._fileManager = FileManager()
        self._logger = Logger()
        self._settingsFile = Settings()

        self._dialog = Dialog('en') if self._settingsFile.getLanguage() == '-' else Dialog(self._settingsFile.getLanguage())

        #---------------------------------------------------------------------------------------------------------------#
        #                                   FILLING THE SETTINGS FILE WITH USER INPUT                                   #

        settingsMethods = self._settingsFile.getMethodsToResolveErrors()
        for methodname, method in settingsMethods.items():
            if methodname == "lang":

                # print a list of supporting languages
                self._console.write(dialog.getMessageFor("chooseLang"))

                langs = self._settingsFile.getSupportingLangs()
                for key, value in langs.items():
                    self._console.write('[' + str(key) + ']')
                    self._console.write(value.upper() + ' ')
                self._console.write('\n')

                # get user's input
                while(True):
                    langInput = int(self._console.readLine("\n--> "))

                    if langInput in langs.keys():
                        method(langs[langInput])
                        break

                    else:
                        self._console.writeLine(self._dialog.getMessageFor("wrongInput"))


                self._dialog.changeLanguage(self._settingsFile.getLanguage())

            elif methodname == "username":
                while(True):
                    self._console.writeLine(self._dialog.getMessageFor("getName"))
                    usernameInput = (console.readLine("\n--> "))

                    # checking the spelling of the username      
                    if len(sub('[\t, \n, \r \s]', '', usernameInput)) >= 2:
                        method(usernameInput)
                        break

            else:
                continue

        #---------------------------------------------------------------------------------------------------------------#


        self._amelie = Amelie(self._settingsFile.getLanguage())

        self._console.writeLine('\n' + self._dialog.getMessageFor("enableVoice"))
        enableVoice = self._console.readLine("--> ")
        while (True):
            if enableVoice == "Y" or enableVoice ==  "y":
                self.changeInputMode(True)
                    
            elif enableVoice == "N" or enableVoice ==  "n":
                self.changeInputMode(False)
                     
            else:
                self._console.writeLine(self._dialog.getMessageFor("wrongInput"))
                enableVoice = self._console.readLine("--> ")
                continue

            break


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

        self._amelie.update()

        return



    def writeToJournal(self, recordTitle: str, value: str) -> None:
        ''' Write an info-record to the journal of the program.
        '''

        self._logger.addRecord(recordTitle, value)

        return



    def changeInputMode(self, enableVoice: bool):
        if enableVoice: self._inputMode = voiceInput
        else: self._inputMode = self._console.readLine

        self._amelie.voice = enableVoice

        return



    def main(self):
        username = str(self._settingsFile.getUsername())
        addedProgramsFile = self._fileManager.readFile("../DataBase/added_programms.db")
        existingProgramNames = [row.split()[0].lower() for row in addedProgramsFile]
        

        while(True):
            try:
                self._console.write('\n' + username + ": ")

                try:
                    userInput = self._inputMode()
                    

                    chatAnswer = self._amelie.conversation(userInput)

                    if self._amelie.voice: self._console.write(userInput + '\n')

                    self._console.writeLine("\n\t\t\tAmelie: " + chatAnswer)
                    self.update()

                except ValueError:
                    self._console.writeLine("\n\t\t\tAmelie: " + self._dialog.getMessageFor("waitVoice"))
                    msvcrt.getch()
                    continue
 
                except FileNotFoundError:
                    def messageFor(phrase: str) -> None:
                        if self._amelie.voice:
                            self._amelie.tts(phrase)


                        self._console.write("\n\t\t\tAmelie: " + self._dialog.getMessageFor(phrase))

                        return


                    userInput = self._console.readLine('\n' + username + ": ")
                    if userInput == 'Y' or userInput == 'y':
                        result = list()

                        messageFor("addProgName")
                        while(True):
                            userInput = sub('[\t, \n, \r, \s]', '', self._console.readLine('\n' + username + ": "))

                            if userInput.lower() in existingProgramNames:
                                messageFor("progNameExist")
                            else:
                                result.append(userInput)
                                break                

                        result.append(" = ")
                    
                        messageFor("addProgPath")
                        result.append(sub('[\t, \n, \r]', '', self._console.readLine('\n' + username + ": ")))

                        self._fileManager.writeToFile(''.join(result) + '\n', "../DataBase/added_programms.db")
                        messageFor("done")

                except OSError as e:
                    if e.errno == -9999:
                        self._logger.logWrite()
                        self._console.writeLine("\n\t\t\tAmelie: " + self._dialog.getMessageFor("microAccesDenied").replace('\n', ". ") + self._dialog.getMessageFor("wait"))
                        msvcrt.getch()
                    else: raise e


            except MemoryError:
                self._logger.logWrite()
                self._console.writeLine(dialog.getMessageFor("error"))

            except SystemExit:
                break

            except (ConnectionError, ConnectError):
                self._logger.logWrite()
                self._console.writeLine('\n' + self._dialog.getMessageFor("serviceError"))
                self._console.writeLine('\n' + self._dialog.getMessageFor("enableVoice"))
                self.changeInputMode(False)
      
            except OSError:
                self._logger.logWrite()
                self._console.writeLine(self._dialog.getMessageFor("error"))

            except Exception:
                self._logger.logWrite()
                self._console.writeLine(self._dialog.getMessageFor("crash"))
                self.restart()

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
