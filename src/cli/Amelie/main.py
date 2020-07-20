# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2020   #
#  github.com/AmeliePick  #
# ======================= #



from os                 import path as os_path
from threading          import Thread
from memory_profiler    import memory_usage

from lib.chat.dialog import Dialog  
from Settings  import Settings
from Amelie    import Amelie
from cli       import Console



def main() -> int:
    console = Console()
    console.printLogo()



    settingsFile = Settings()
    dialog = Dialog('en') if settingsFile.getLanguage() == '-' else Dialog(settingsFile.getLanguage())
        
    #---------------------------------------------------------------------------------------------------------------#
    #                                   FILLING THE SETTINGS FILE WITH USER INPUT                                   #

    settingsMethods = settingsFile.getMethodsToResolveErrors()
    for methodname, method in settingsMethods.items():
        if methodname == "lang":
            console.write(dialog.getMessageFor("Choose_lang"))

            langs = settingsFile.getSupportingLangs()
            for key, value in langs.items():
                console.write('[' + str(key) + ']')
                console.write(value.upper() + ' ')
            console.write('\n')

            while(True):
                langInput = int(console.readLine("\n--> "))

                if langInput in langs.keys():
                    method(langs[langInput])
                    break

                else:
                    console.writeLine(dialog.getMessageFor("WrongInput"))


            dialog.changeLanguage(settingsFile.getLanguage())

        elif methodname == "username":
            while(True):
                console.writeLine(dialog.getMessageFor("getName"))
                usernameInput = (console.readLine("\n--> "))

                from re import sub
                if len(sub('[\t, \n, \r \s]', '', usernameInput)) >= 2:
                    method(usernameInput)
                    break

    #---------------------------------------------------------------------------------------------------------------#


    AmelieInstance = Amelie()
    
    username = str(settingsFile.getUsername())

    
    console.writeLine('\n' + dialog.getMessageFor("Voice_control"))
    turnOnTheVoice = console.readLine("--> ")
    while (True):
        try:
            if turnOnTheVoice == "Y" or turnOnTheVoice ==  "y":
                while(True):
                    try:
                        AmelieInstance.recorderCalibration()
                    except OSError:
                        from os import system
                        console.writeLine(dialog.getMessageFor("microAccesDenied"))
                        system("pause")
                        continue


                    console.write('\n' + username + ": ")
                    chatAnswer = AmelieInstance.voiceChat()

                    console.writeLine(AmelieInstance.getUserInput())
                    console.writeLine("\n\t\tAmelie: " + chatAnswer)

                    AmelieInstance.update()


            elif turnOnTheVoice == "N" or turnOnTheVoice ==  "n":
                while(True):
                    userInput = console.readLine('\n' + username + ": ")
                    chatAnswer = AmelieInstance.chat(userInput)

                    console.writeLine("\n\t\t\tAmelie: " + chatAnswer)

                    AmelieInstance.update()
                     

            else:
                console.writeLine(dialog.getMessageFor("WrongInput"))
                turnOnTheVoice = console.readLine("--> ")
                continue


            



        except MemoryError:
            AmelieInstance.writeLog()
            console.writeLine(dialog.getMessageFor("error"))
            continue

        except SystemExit:
            

            break

        except ConnectionError:
            AmelieInstance.writeLog()
            console.writeLine(dialog.getMessageFor("service_error"))
      
        except OSError:
            AmelieInstance.writeLog()
            console.writeLine(dialog.getMessageFor("error"))

        except Exception:
            AmelieInstance.writeLog()
            console.writeLine(dialog.getMessageFor("crash"))

            AmelieInstance.restart()


    AmelieInstance.__del__()
    return 0



if __name__ == '__main__':
    main()
