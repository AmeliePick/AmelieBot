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

from modules.entry_input        import start
from modules.set_username       import set_username

from libs.configParser          import SettingsControl
from libs.logger                import sessionLogger
from libs.update                import checkUpdate, download
from libs.logger                import LogWrite
from libs.time                  import stopWatch



def restart():
    #restart of the bot
    exe = executable
    execl(exe, exe, *argv)


def getUpdate():
    # --- Check updates ---
    isupdate  = checkUpdate()
    if isupdate:
        print(SettingsControl.Print("isUpdate"))
        sleep(2)
        download(isupdate)
        remove("TEMP/tmp_file.py")

        restart()

    else:
        print(SettingsControl.Print("istUpdate"), '\n')

    if os_path.exists("TEMP/t.ini"):
        remove("TEMP/t.ini")

    print("AmelieBot " + SettingsControl.getConfig("settings.ini", "ver"), '\n')


maxRAMUsage = memory_usage()
def RAMCheck():
    global maxRAMUsage
    if(memory_usage() > maxRAMUsage):
        maxRAMUsage = memory_usage()


def main():
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

    # ----- Start the bot -----
    start()


    #--- Chat
    print(SettingsControl.Print("Voice_control"))
    On = input ("--> ")

    print(SettingsControl.Print("Learning"))
    stopWatch.start()
    from modules.AIProcessing       import answer
    from modules.AICore             import Chat

    chatOBJ = Chat()


    def launchChat(voice: str = ""):
        global stopWatch
        global sessionLogger

        if(stopWatch):
            sessionLogger.SessionCollector( "Chat Duration(sec)", str(stopWatch.stop()) )

            #del(sessionLogger)
            stopWatch = None
        chatOBJ.Enter(voice)
        chatOBJ.open_AI()

        return answer(chatOBJ.getInput(), chatOBJ.getInputType(), chatOBJ.getDataSet_new())
    

    while (True):
        try:
            if On == "Y" or On ==  "y":
                from libs.Recognition   import REG, calibration
                from libs.AudioManagement import initAudio

                initAudio()

                if SettingsControl.getConfig("settings.ini", "lang") == "RU":
                    from libs.RuSpeak import speak

                    calibration()
                    while (True):
                        speak(launchChat(REG()))
                        RAMCheck()
                        continue
                else:
                    from libs.Speak import speak

                    calibration()
                    while (True):
                        speak(launchChat(REG()))
                        RAMCheck()
                        continue

            elif On == "N" or On ==  "n":
                while(True):
                    сhat = launchChat()
                    if сhat.getNum() == 0:
                        sleep(1)
                        _exit(0)          
            else:
                print(SettingsControl.Print("WrongInput"))
                On = input("--> ")
                continue


        except SystemExit:
            sessionLogger.SessionCollector( "max RAM usage", str(maxRAMUsage) )
            _exit(0)


        except Exception:
            LogWrite()
            print(SettingsControl.Print("crash"))

            restart()


        except ConnectionError:
            print(SettingsControl.Print("service_error"))

                
        except OSError:
            print(SettingsControl.Print("errMicro"))


        print(SettingsControl.Print("Voice_control"))
        On = input ("--> ")


if __name__ == '__main__':
    main()
