# -*- coding: utf-8 -*-

'''
Chat module for synthesis

The function gets the result of the chat feature of Chat_AI and passes them to the function synthesis of speak() of Speak of the module

'''

import sys, os, random, pickle, re, playsound

from Chat_AI import open_AI
from libs.Speak import speak

def speech():

    return speak(open_AI())
