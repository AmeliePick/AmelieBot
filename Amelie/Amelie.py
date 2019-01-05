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
import os, webbrowser, subprocess ,random, re, pyttsx3

from modules import set_username, entry_input
from libs.configParser import *

print ( 70 * "_")
print ("\t\t                         _ _       \n" +
       "\t\t    /\                  | (_)      \n" +
       "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
       "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
       "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
       "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 70 * "_")

# ----- Bot -----

#--- language selection ---
'''
A configuration file is created.
A configuration file is created. 
Further from it all information is read. 
If the file is empty, which means this is the first launch of the application, the user is prompted to select the bot language.
'''

if os.path.exists("settings.ini") == False:
    
    
    createSettings = open("settings.ini", 'a')
    createSettings.close()

    settings = open("settings.ini", 'r')
    Rsettings = settings.read()

    path = "settings.ini"

    if Rsettings == "":

        
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

    settings.close()

# read username from file in DB
usernameInFile = open("../DataBase/username.txt", "r")
username = usernameInFile.read()
usernameInFile.close()

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

        
        from Chat_AI_with_syn import speechRU
        if Config("settings.ini") == "RU":
            
                if speechRU() == 1:
                    print(Parser("Voice_control"))
                    On = input ("--> ")
                    continue

        else:
            from Chat_AI_with_syn import speech
            
            if speech() == 1:
                print(Parser("Voice_control"))
                On = input ("--> ")
                continue
        # ↑ Microphone check

        #If there is no microphone
        
            
    elif On == "N" or On ==  "n":
        print(str(Parser("Learning")))

        from modules.Chat_AI import Enter, open_AI, Answer

        while(True):
            
            Answer(open_AI(Enter()))

    else:
        print(Parser("WrongInput"))
        On = input("--> ")