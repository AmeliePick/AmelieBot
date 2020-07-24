# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2020   #
#  github.com/AmeliePick  #
# ======================= #



from os                 import path as os_path
from os                 import system
from threading          import Thread
from memory_profiler    import memory_usage

from httpcore._exceptions import ConnectError

from lib.tools.runtime         import restart
from lib.tools.logger          import Logger
from lib.chat.dialog           import Dialog  
from lib.tools.system          import FileManager
from lib.Settings              import Settings
from lib.Amelie                import Amelie
from cli                       import Console



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
                self._console.write(dialog.getMessageFor("Choose_lang"))

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
                        self._console.writeLine(self._dialog.getMessageFor("WrongInput"))


                self._dialog.changeLanguage(self._settingsFile.getLanguage())

            elif methodname == "username":
                while(True):
                    self._console.writeLine(self._dialog.getMessageFor("getName"))
                    usernameInput = (console.readLine("\n--> "))

                    # checking the spelling of the username
                    from re import sub
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

        self._amelie.update()

        return



    def writeToJournal(self, recordTitle: str, value: str) -> None:
        ''' Write an info-record to the journal of the program.
        '''

        self._logger.addRecord(recordTitle, value)

        return



    def main(self):
        username = str(self._settingsFile.getUsername())

        self._console.writeLine('\n' + self._dialog.getMessageFor("Voice_control"))
        turnOnTheVoice = self._console.readLine("--> ")
        while (True):
            try:
                if turnOnTheVoice == "Y" or turnOnTheVoice ==  "y":
                    self._console.write('\n' + username + ": ")
                    self._chatAnswer = self._amelie.voiceChat()

                    self._console.writeLine(self._amelie.getUserInput())
                    self._console.writeLine("\n\t\tAmelie: " + chatAnswer)

                    system("pause")


                elif turnOnTheVoice == "N" or turnOnTheVoice ==  "n":
                    userInput = self._console.readLine('\n' + username + ": ")
                    chatAnswer = self._amelie.chat(userInput)

                    self._console.writeLine("\n\t\t\tAmelie: " + chatAnswer)

                     

                else:
                    self._console.writeLine(dialog.getMessageFor("WrongInput"))
                    turnOnTheVoice = self._console.readLine("--> ")
                    continue


                self.update()



            except MemoryError:
                self._logger.logWrite()
                self._console.writeLine(dialog.getMessageFor("error"))

            except SystemExit:
                break

            except (ConnectionError, ConnectError):
                self._logger.logWrite()
                self._console.writeLine('\n' + self._dialog.getMessageFor("service_error"))
                self._console.writeLine('\n' + self._dialog.getMessageFor("Voice_control"))
                turnOnTheVoice = self._console.readLine("--> ")
      
            except OSError:
                self._logger.logWrite()
                self._console.writeLine(dialog.getMessageFor("error"))

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
