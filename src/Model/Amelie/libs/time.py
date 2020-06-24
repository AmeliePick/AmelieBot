# -*- coding: utf-8 -*-

''' Module for work with time
'''


import time

class Stopwatch:
    sec: int

    def start(self) -> None:
        self.sec = 0
        self.sec = time.time()


    def stop(self) -> int: 
        return int(time.time() - self.sec)



stopWatch = Stopwatch()