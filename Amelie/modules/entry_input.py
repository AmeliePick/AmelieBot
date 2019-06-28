# -*- coding: utf-8 -*

# === Program start module ===

from libs.configParser import SettingsControl
from libs.AIChatKit import LangChoice


'''
Enter the program where the program expects an exact response from the user
'''

from os import _exit
from time import sleep

def start():
    print(SettingsControl.Print("start"))
    start = input("--> ")

    while (True):
        if (start == "Y" or start == "y"):
            LangChoice()
            print(SettingsControl.Print("sayHello"))
            print ("--> ")
            break
        elif (start == "N" or start == "n"):
            print (SettingsControl.Print("bye"))
            sleep(1.5)
            _exit(0)
        else:
            print(SettingsControl.Print("tryAgain"))
            start = input("--> ")
            continue
