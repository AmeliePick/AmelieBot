# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2018   #
#  github.com/AmeliePick  #
# ======================= #


'''
The main file of the bot. 
The functions of entering the program and choosing the bot mode are called.
'''


from sys import stdin, exit as sys_exit
from sys import argv
from sys import executable
from os import path as os_path
from os import execl
from time import sleep

from modules import set_username, entry_input
from libs.configParser import *
from libs.update import checkUpdate, download

print ( 70 * "_")
print ("\t\t                         _ _       \n" +
       "\t\t    /\                  | (_)      \n" +
       "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
       "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
       "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
       "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 70 * "_")

print("AmelieBot " + Config("settings.ini", "ver"), '\n')
# ----- Bot -----

# Errors dictionary:
    # if return 1 - error with Internet connetcion
    # if return 2 - error with input(user didnt enter somethings)
    # if return 3 - error with micro(micro is not defined)


#--- language selection ---
'''
A configuration file is created.
A configuration file is created. 
Further from it all information is read. 
If the file is empty, which means this is the first launch of the application, the user is prompted to select the bot language.
'''


def createSetting():
    createSettings = open("settings.ini", 'a')
    createSettings.close()


def pullSettings(path):
    '''
    path -- The path where the configuration file is located
    '''
    choose_lang = input("Choose language [RU] of [EN]: ") #delete this

    while(True):

        if choose_lang == "RU":
            value = "RU"
            createConfig(path, value)
            break

        elif choose_lang == "EN":
            value = "EN"
            createConfig(path, value)
            break

        else:
            choose_lang = input("Choose language [RU] of [EN]: ") #delete this
            continue


if os_path.exists("settings.ini") == False:

    createSetting()

    path = "settings.ini"

    settings = open("settings.ini", 'r')
    Rsettings = settings.read()
    
    pullSettings(path)


    settings.close()
elif os_path.exists("settings.ini") == True:
    handle = open("settings.ini", 'r')
    ReadHandle = handle.read()

    if ReadHandle == '':
        pullSettings("settings.ini")
        handle.close() # Check for empty settings


# read username from file in DB
usernameInFile = open("../DataBase/username.txt", "r")
username = usernameInFile.read()
usernameInFile.close()


#check updates
isupdate  = checkUpdate()
if isupdate:
    print(Parser("isUpdate"))
    sleep(2)
    download(isupdate)

    #restart of bot
    exe = executable
    execl(exe, exe, *argv)

else:
    print(Parser("istUpdate"), '\n')


# call function to set it if it's empty, set username
if (username == ""):
    set_username.set_username()


# ----- entry -----
entry_input.start()
# ----- end of the entry -----
# ===== i will not go deeper, cmon. (c) Matt Fawkes =====  UPD: changed by AmeliePick === #


#--- Chat
print(Parser("Voice_control"))
On = input ("--> ")
while (True):
    if On == "Y" or On ==  "y":
        print(Parser("Learning"))
        if Config("settings.ini", "lang") == "RU":
            from modules.Chat_AI_with_syn import speechRU

            Chat = speechRU()
            #Microphone check
            if Chat == 1 or Chat == 3:
                print(Parser("Voice_control"))
                On = input ("--> ")
                continue

        else:
            from modules.Chat_AI_with_syn import speech
            Chat = speech()

            #Microphone check
            if Chat == 1 or Chat == 3:
                print(Parser("Voice_control"))
                On = input ("--> ")
                continue
      
      
    elif On == "N" or On ==  "n":
        print(str(Parser("Learning")))

        from modules.Chat_AI import Enter, open_AI, Answer

        while(True):
            Chat = Answer(open_AI(Enter()))

    else:
        print(Parser("WrongInput"))
        On = input("--> ")