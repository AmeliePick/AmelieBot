# -*- coding: utf-8 -*-

import simpleaudio      as sa
from playsound          import _playsoundWin

from time               import sleep
from sys                import exit as sys_exit
from os                 import getenv
from os                 import path as os_path
from os                 import remove

from .time              import Stopwatch

timer = Stopwatch()

def initAudio():

    dir = "libs\\"
    dll_name = ""
    
    if ("64" in getenv('PROCESSOR_ARCHITECTURE')) or ("64" in getenv('PROCESSOR_ARCHITEW6432')): 
        dll_name = "avbin64.dll"
    else:
        dll_name = "avbin.dll"


def playAudio(sound: str, reps=1) -> None:

  
    timer.start()

    wave_obj = sa.WaveObject.from_wave_file(sound)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    #while timer.stop() < _song.duration:
        #continue
    


def _exit(file: str, second_file = "") -> None:
    if os_path.exists(file):
        remove(file)

    if os_path.exists(second_file):
        remove(second_file)

    return sys_exit(0)
