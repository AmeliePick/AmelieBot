# -*- coding: utf-8 -*

# === Program start module ===

from libs.configParser import Parser

'''
Enter the program where the program expects an exact response from the user
'''

from sys import exit as sys_exit
from time import sleep
from os import _exit

def start():
    print(Parser("start"))
    start = input("--> ")

    while (True):
        if (start == "Y" or start == "y"):
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

