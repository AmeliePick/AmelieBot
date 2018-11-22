# -*- coding: utf-8 -*-

'''
Chat module for synthesis

The function returns the value from REG in the open_AI (for typing a question) in Ansever (for generating an answer) in SPEC (for articulating an answer)
'''

import sys, os, random, pickle, re, playsound

from Chat_AI import Answer, open_AI
from libs.Recognition import REG
from libs.Speak import speak

def speech():

    return speak(Answer(open_AI(REG())))


while(True):
    speech()

    if speech == 1:
        os.system("pause")