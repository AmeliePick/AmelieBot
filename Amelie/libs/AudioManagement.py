# -*- coding: utf-8 -*-

from pyglet.lib         import load_library
from pyglet.app         import exit, _run
from pyglet.media       import load
from pyglet.clock       import schedule_once

from .pyglet.player     import Player

from time               import sleep
from sys                import exit as sys_exit
from os                 import getenv
from os                 import path as os_path
from os                 import remove

from .time              import Stopwatch

timer = Stopwatch()
player = Player()

def initAudio():

    dir = "libs\\"
    dll_name = ""
    
    if ("64" in getenv('PROCESSOR_ARCHITECTURE')) or ("64" in getenv('PROCESSOR_ARCHITEW6432')): 
        dll_name = "avbin64.dll"
    else:
        dll_name = "avbin.dll"

    load_library(dir + dll_name)


def playAudio(sound, reps=1):
    global player
    _song = load(sound)
    player.queue(_song)
  
    
    player.play()
    timer.start()
    
    def callback(dt):
        exit()

    schedule_once(callback, _song.duration*reps)
    _run()

    while timer.stop() < _song.duration:
        continue
    player.stop() # deleting the player here!
    player.clear_queue()


def _exit(file: str) -> None:
    global player
    if os_path.exists(file):
        ''' We can use song.__del__()
        # Delete the source of AVbin, close the file and stop the thread.
        # Anyway it will works, because its in a source file:
        # pyglet.media.sources.avbin.py -> line 327 -> __del__(self)
        ================================================================
            Or we can use player.delete() - due to the pyglet.player uses
        # Includes a call of __del__() from pyglet.media.sources.avbin.py
        # Deleting of all child objects of player
        # I added a few changes due to WinError 32. Didn't remove the mp3 file, because other process used it.
        # A new file was saved in Amelie\libs\pyglet\player.py -> Changes: line 171, line 172.

        '''

        player.delete()
        player = None
        
        remove(file)

    return sys_exit(0)
