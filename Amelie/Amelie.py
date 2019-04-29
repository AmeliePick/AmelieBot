# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2018   #
#  github.com/AmeliePick  #
# ======================= #


'''
The main file of the bot. 
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




from modules                    import entry_input
from modules.set_username       import set_username
from libs.configParser          import *
from libs.update                import checkUpdate, download
from libs.logger                import LogWrite



def restart():
    #restart of the bot
    exe = executable
    execl(exe, exe, *argv)


def createSetting():
    createSettings = open("settings.ini", 'a')
    createSettings.close()

    createConfig("settings.ini")


def setLang(path):
    '''
    path -- The path where the configuration file is located
    '''

    # Default settings
    setConfig(path, "lang", "-")

    choose_lang = input("Choose language [RU] of [EN]: ") #delete this

    while(True):

        if choose_lang == "RU":
            value = "RU"
            setConfig(path, "lang", value)
            break

        elif choose_lang == "EN":
            value = "EN"
            setConfig(path, "lang", value)
            break

        else:
            choose_lang = input("Choose language [RU] of [EN]: ") #delete this
            continue



# ----- Bot -----


print ( 70 * "_")
print ("\t\t                         _ _       \n" +
       "\t\t    /\                  | (_)      \n" +
       "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
       "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
       "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
       "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 70 * "_")





#--- language selection ---
'''
A configuration file is created.
Further from it all information is read. 
If the file is empty, which means this is the first launch of the application, the user is prompted to select the bot language.
'''



if os_path.exists("settings.ini") == False:

    createSetting()

    path = "settings.ini"
    

    setConfig(path, "ver", "2.5.2")
    setLang(path)

elif os_path.exists("settings.ini") == True:
    path = "settings.ini"
    handle = open(path, 'r')
    ReadHandle = handle.read()
    handle.close() # Check for empty settings

    if ReadHandle == '':
        createConfig("settings.ini")
        setConfig(path, "ver", "2.5.2")
        setLang(path)

    if Config(path, "lang") == '-':
        setLang(path)

# --- Check updates ---
isupdate  = checkUpdate()
if isupdate:
    print(Parser("isUpdate"))
    sleep(2)
    download(isupdate)
    remove("tmp_file.py")

    restart()

else:
    print(Parser("istUpdate"), '\n')

if os_path.exists("t.ini"):
    remove("t.ini")

print("AmelieBot " + Config("settings.ini", "ver"), '\n')


# --- Set username ---
if os_path.exists("../DataBase/username.txt"):
    with open("../DataBase/username.txt", 'r') as file_user:
        username = file_user.read()
        if (username == ""):
            set_username()

if not os_path.exists("../DataBase/username.txt"):
    set_username()




# ----- entry -----
entry_input.start()
# ----- end of the entry -----
# ===== i will not go deeper, cmon. (c) Matt Fawkes =====  UPD: changed by AmeliePick === #


#--- Chat
print(Parser("Voice_control"))
On = input ("--> ")
while (True):
    try:
        if On == "Y" or On ==  "y":
            print(Parser("Learning"))

        
            if Config("settings.ini", "lang") == "RU":
                from modules.Chat_AI_with_syn import speechRU, calibration
                calibration()

                while (True):
                    speechRU()
                    continue

            else:
                from modules.Chat_AI_with_syn import speech, calibration
                calibration()

                while (True):
                    speech()
                    continue



    
        elif On == "N" or On ==  "n":
            print(str(Parser("Learning")))

            from modules.Chat_AI import Enter, open_AI, Answer

            while(True):
                Chat = Answer(open_AI(Enter()))

                if Chat.getNum() == 0:
                    sleep(1)
                    _exit(0)
                    

        else:
            print(Parser("WrongInput"))
            On = input("--> ")
            continue


    except SystemExit:
        _exit(0)

    except Exception:
        LogWrite()
        print(Parser("crash"))
        restart()

    except ConnectionError:
        print(Parser("service_error"))
                
    except OSError:
        print(Parser("errMicro"))


    print(Parser("Voice_control"))
    On = input ("--> ")