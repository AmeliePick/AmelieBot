# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2019   #
#  github.com/AmeliePick  #
# ======================= #


''' The main file of the bot. 
The functions of entering the program and choosing the bot mode are called.
'''

from time   import sleep
from sys    import stdin, exit as sys_exit
from sys    import argv
from sys    import exc_info 
from sys    import executable
from os     import path as os_path
from os     import execl
from os     import _exit
from os     import remove

from memory_profiler import memory_usage


from modules.AIProcessing       import LangChoice

from libs.configParser          import SettingsControl, DisplayText
from libs.logger                import sessionLogger
from libs.update                import checkUpdate, download
from libs.logger                import LogWrite
from libs.time                  import stopWatch



def restart() -> None:
    #restart of the bot
    exe = executable
    execl(exe, exe, *argv)


def getUpdate() -> None:
    # --- Check updates ---
    isupdate  = checkUpdate()
    if isupdate:
        print(DisplayText.print("isUpdate"))
        sleep(1.5)

        download(isupdate)
        restart()

    else:
        print(DisplayText.print("istUpdate"), '\n')

    #TODO: remove here
    

    print("AmelieBot " + SettingsControl.getConfig("Settings", "ver"), '\n')


def set_username() -> None:
    if os_path.exists("../DataBase/username.json"):
        username = ''
        with open("../DataBase/username.json", 'r') as file_user:
            username = file_user.read()

        if (username == ""):
            print(DisplayText.print("getName"))
            username = input("> ")

        if (username != ""):
            with open("../DataBase/username.json", "w") as writeUsername:
                writeUsername.write(username)
            print ("\n Welcome, "+ username + "!")

        else:
            print (DisplayText.print("emptyName"))
            set_username()

    else:
        with open("../DataBase/username.json", 'w') as file_user:
            file_user.close()
        set_username()

maxRAMUsage = memory_usage()
def RAMCheck() -> None:
    global maxRAMUsage
    if(memory_usage() > maxRAMUsage):
        maxRAMUsage = memory_usage()
    return


def main() -> int:
     # ----- Start the bot -----
    global stopWatch
    global sessionLogger

    print ( 70 * "_")
    print ("\t\t                         _ _       \n" +
           "\t\t    /\                  | (_)      \n" +
           "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
           "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
           "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
           "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
    print ( 70 * "_")

    getUpdate()
    set_username()
    
    
    

   

    print(DisplayText.print("Learning"))
    stopWatch.start()
    from modules.AIProcessing       import getAnswer, Answer
    from modules.AICore             import Chat
    sessionLogger.sessionCollector( "Chat loading(sec)", str(stopWatch.stop()) )
    stopWatch = None


    LangChoice()
    chatOBJ = Chat()

    # inline function
    def launchChat(voice: str = "") -> Answer:
        chatOBJ.Enter(voice)
        chatOBJ.open_AI()

        return getAnswer(chatOBJ.getInput(), chatOBJ.getInputType(), chatOBJ.getSessionInput())
    

    # --- Chat ---
    print(DisplayText.print("Voice_control"))
    On = input ("--> ")
    while (True):
        try:
            if On == "Y" or On ==  "y":
                from libs.Recognition   import speechRecognition

                if SettingsControl.getConfig("Settings", "lang") == "RU":
                    from libs.RuSpeak import speak

                    speechRecognition.calibration()
                    while (True):
                        speak(launchChat(speechRecognition.recognize()))
                        RAMCheck()
                        continue
                else:
                    from libs.Speak import speak

                    speechRecognition.calibration()
                    while (True):
                        speak(launchChat(speechRecognition.recognize()))
                        RAMCheck()
                        continue

            elif On == "N" or On ==  "n":
                while(True):
                    сhat = launchChat()
                    if сhat.getCode() == 0:
                        sleep(1)
                        _exit(0)          
            else:
                print(DisplayText.print("WrongInput"))
                On = input("--> ")
                continue


        except MemoryError:
            print(DisplayText.print("error"))
            continue

        except SystemExit:
            sessionLogger.sessionCollector( "max RAM usage", str(maxRAMUsage) )
            _exit(0)

        except ConnectionError:
            print(DisplayText.print("service_error"))
      
        except OSError:
            LogWrite()
            print(DisplayText.print("error"))

        except Exception:
            LogWrite()
            print(DisplayText.print("crash"))

            restart()


        print(DisplayText.print("Voice_control"))
        On = input ("--> ")

    return 0


if __name__ == '__main__':
    main()
