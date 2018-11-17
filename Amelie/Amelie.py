# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2018   #
#  github.com/AmeliePick  #
# ======================= #

from sys import stdin, exit as sys_exit
import os, webbrowser, subprocess ,random, re, pyttsx3
import set_username, entry_input

from libs.Speak import speak

#------

print ( 70 * "_")
print ("\t\t                         _ _       \n" +
       "\t\t    /\                  | (_)      \n" +
       "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
       "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
       "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
       "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 70 * "_")

# ----- Bot -----
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
On = input ("\nEnable voice? [Y] or [N]: ")
while (True):
    if On == "Y" or On ==  "y":
        print("Идёт обучение бота...")

        from Chat_AI_with_syn import speech
        while (True):
            speech()
            
    elif On == "N" or On ==  "n":
        print("Идёт обучение бота...")

        from Chat_AI import open_AI
        while (True):
            open_AI()
       
    else:
        On = input("Enter [Y] or [N] please ^-^ : ")