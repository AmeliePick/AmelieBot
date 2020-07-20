# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2020   #
#  github.com/AmeliePick  #
# ======================= #



from os                 import path as os_path
from threading          import Thread
from memory_profiler    import memory_usage


from Amelie    import Amelie
from cli       import Console



def main() -> int:
    AmelieInstance = Amelie()
    console = Console()


    username = str(AmelieInstance.getUsername())


    console.printLogo()

    console.writeLine(AmelieInstance.getMessageFor("Voice_control"))
    turnOnTheVoice = console.readLine("--> ")
    while (True):
        try:
            if turnOnTheVoice == "Y" or turnOnTheVoice ==  "y":
                while(True):
                    try:
                        AmelieInstance.recorderCalibration()
                    except OSError:
                        from os import system
                        console.writeLine(AmelieInstance.getMessageFor("microAccesDenied"))
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
                console.writeLine(AmelieInstance.getMessageFor("WrongInput"))
                turnOnTheVoice = console.readLine("--> ")
                continue


            



        except MemoryError:
            AmelieInstance.writeLog()
            console.writeLine(AmelieInstance.getMessageFor("error"))
            continue

        except SystemExit:
            

            break

        except ConnectionError:
            AmelieInstance.writeLog()
            console.writeLine(AmelieInstance.getMessageFor("service_error"))
      
        except OSError:
            AmelieInstance.writeLog()
            console.writeLine(AmelieInstance.getMessageFor("error"))

        except Exception:
            AmelieInstance.writeLog()
            console.writeLine(AmelieInstance.getMessageFor("crash"))

            AmelieInstance.restart()


    AmelieInstance.__del__()
    return 0



if __name__ == '__main__':
    main()
