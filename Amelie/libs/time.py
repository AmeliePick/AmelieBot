# -*- coding: utf-8 -*-

''' The module for work with time

'''

import time

class Stopwatch:
    sec = 0

    def start(self):
        self.sec = 0
        self.sec = time.time()


    def stop(self):
        self.sec = time.time() - self.sec 
        return int(self.sec)


stopWatch = Stopwatch()