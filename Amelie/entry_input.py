# -*- coding: utf-8 -*

# === Program start module ===

'''
Enter the program where the program expects an exact response from the user
'''

from sys import exit as sys_exit
from time import sleep

def start():
    start = input("\n Hi, I'm Amelie. Start me? Press [Y] of [N]: ")

    while (True):
        if (start == "Y" or start == "y"):
            print ("\n Salute! What I'm capable of, you can find out right now =D")
            break
        elif (start == "N" or start == "n"):
            print ("\n Thinking... Now you are working, bye =D")
            sleep(1.5)
            sys_exit()
        else:
            start = input("\n (!) Try again - [Y] or [N]: ")
            continue

