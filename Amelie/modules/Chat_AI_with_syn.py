# -*- coding: utf-8 -*-

'''
Chat module for synthesis

The function returns the value from REG in the open_AI (for typing a question) in Ansever (for generating an answer) in SPEC (for articulating an answer)
'''

import sys, os, random, pickle, re, playsound

from modules.Chat_AI import Answer, open_AI
from libs.Recognition import REG
from libs.Speak import speak
from libs.GoogleSpeak import speak as Speak

def speech():

    return speak(Answer(open_AI(REG())))

def speechRU():
    
    return Speak(Answer(open_AI(REG())))

