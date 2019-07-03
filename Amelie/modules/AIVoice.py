# -*- coding: utf-8 -*-

'''
Chat module for synthesis

The function returns the value from REG in the open_AI (for typing a question) in Ansever (for generating an answer) in SPEC (for articulating an answer)
'''


from modules.chatMain       import openChat
from libs.Recognition       import REG, calibration
from libs.Speak             import speak
from libs.GoogleSpeak       import speak as RUSpeak

def speech():

    return speak( openChat(REG()) )

def speechRU():
    
    return RUSpeak( openChat(REG()) )

