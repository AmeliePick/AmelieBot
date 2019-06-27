# -*- coding: utf-8 -*-

'''
Log file maintenance
'''
from traceback      import format_exc
from sys            import exit as sys_exit

import configparser



class SessionLog:
    ''' The class is a singleton


    '''

    path = ''
    config = configparser.ConfigParser()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def __init__():
        path = "session_journal.log"
        if not sys_exit(path):
            log =  configParser.settings()

            log.createSetting(path)
            log.createConfig(path)


    def setConfig(self, option: str):

        self.config.read(path)

        if not self.config.has_section(option):
            self.config.set(option, value)

            


    def SessionCollector(option: str, value):
        pass









def LogWrite():
    with open("Amelie_log.log", 'a') as log:
        log.write(10*'-'+'\n'+ str(format_exc()+'\n'))

    return
