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

from modules.entry_input        import start
from modules.set_username       import set_username
from libs.configParser          import SettingsControl
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
        remove("tmp_file.py")

        restart()

    else:
        print(SettingsControl.Print("istUpdate"), '\n')

    if os_path.exists("t.ini"):
        remove("t.ini")

    print("AmelieBot " + SettingsControl.getConfig("settings.ini", "ver"), '\n')


def main():


    # ----- Bot -----

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
    while (True):
        try:
            if On == "Y" or On ==  "y":
                print(SettingsControl.Print("Learning"))

                if SettingsControl.getConfig("settings.ini", "lang") == "RU":
                    stopWatch.start()
                    from modules.AIVoice import speechRU, calibration
                    calibration()

                    while (True):
                        speechRU()
                        continue

                else:
                    stopWatch.start()
                    from modules.AIVoice import speech, calibration
                    calibration()

                    while (True):
                        speech()
                        continue

            elif On == "N" or On ==  "n":
                print(str(SettingsControl.Print("Learning")))

                stopWatch.start()
                from modules.chatMain import openChat

                while(True):
                    Chat = openChat()

                    if Chat.getNum() == 0:
                        sleep(1)
                        _exit(0)
                    
            else:
                print(SettingsControl.Print("WrongInput"))
                On = input("--> ")
                continue


        except SystemExit:
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
