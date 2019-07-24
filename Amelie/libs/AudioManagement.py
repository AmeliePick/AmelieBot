# -*- coding: utf-8 -*-

import pyglet
from time               import sleep
from sys                import exit
from os                 import getenv
from os                 import path as os_path
from os                 import remove
from .pyglet.player     import Player
from .pyglet.app        import _run




def initAudio():

    dir = "libs\\"
    dll_name = ""
    
    if ("64" in getenv('PROCESSOR_ARCHITECTURE')) or ("64" in getenv('PROCESSOR_ARCHITEW6432')): 
        dll_name = "avbin64.dll"
    else:
        dll_name = "avbin.dll"

    pyglet.lib.load_library(dir + dll_name)


def playAudio(sound, reps=1):
    player = Player()
    _song = pyglet.media.load(sound)
    player.queue(_song)
  
    player.play()
    
    def callback(dt):
        pyglet.app.exit()

    pyglet.clock.schedule_once(callback, _song.duration*reps)
    pyglet.app._run()
    
    #TODO: delay while music is playing

    return player


def _exit(file: str, player: Player) -> None:
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
        
        remove(file)

    exit(0)
