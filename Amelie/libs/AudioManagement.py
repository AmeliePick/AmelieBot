# -*- coding: utf-8 -*-

import simpleaudio      as sa
from playsound          import _playsoundWin

from sys                import exit as sys_exit
from os                 import path as os_path
from os                 import remove


def playAudio(sound: str, reps=1) -> None:
    wave_obj = sa.WaveObject.from_wave_file(sound)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def _exit(file: str, second_file = "") -> None:
    if os_path.exists(file):
        remove(file)

    if os_path.exists(second_file):
        remove(second_file)

    return sys_exit(0)
