# -*- coding: utf-8 -*-

import sys, os, random, pickle, re, playsound

from Chat_AI import open_AI
from libs.Speak import speak

def speech():

    return speak(open_AI())
