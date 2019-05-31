# -*- coding: utf-8 -*-

import pyglet
from pyglet.media import Player
import pyglet


def playAudio(sound, reps=1):
    dll_name ='libs/avbin64.dll'
    pyglet.lib.load_library(dll_name)

    player = Player()
    song = pyglet.media.load(sound,streaming=False)
    for i in range(reps):
        player.queue(song)
  
    player.play()
    def callback(dt):
        pyglet.app.exit()
  
    pyglet.clock.schedule_once(callback,song.duration*reps)
    pyglet.app.run()
