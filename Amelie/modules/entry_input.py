# -*- coding: utf-8 -*

# === Program start module ===

from libs.configParser import Parser
from .Chat_AI import LangChoice


'''
Enter the program where the program expects an exact response from the user
'''

from os import _exit
from time import sleep

def start():
    print(Parser("start"))
    start = input("--> ")

    while (True):
        if (start == "Y" or start == "y"):
            LangChoice()
            print(Parser("sayHello"))
            print ("--> ")
            break
        elif (start == "N" or start == "n"):
            print (Parser("bye"))
            sleep(1.5)
            _exit(0)
        else:
            print(Parser("tryAgain"))
            start = input("--> ")
            continue
