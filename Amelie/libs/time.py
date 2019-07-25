# -*- coding: utf-8 -*-

import time

class Stopwatch:
    sec = 0

    def start(self):
        self.sec = 0
        self.sec = time.time()


    def stop(self): 
        return int(time.time() - self.sec)


stopWatch = Stopwatch()