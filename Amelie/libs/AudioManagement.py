# -*- coding: utf-8 -*-

import pyglet

from os             import getenv
from .pyglet.player  import Player



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
    pyglet.app.run()

    return player

    
    
