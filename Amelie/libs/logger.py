# -*- coding: utf-8 -*-

'''
Log file maintenance
'''
from traceback      import format_exc
from datetime       import datetime
from sys            import exit as sys_exit

from libs.configParser      import Config




class SessionLog(Config):
    ''' The class is a singleton


    '''


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def SessionCollector(option: str, value) -> None:
        pass

    def __init__(self):
        path = "session_journal.log"

        if not sys_exit(path):
            log =  configParser.settings()
            log.createSetting(path)


        # clearing the session log file from old records
        with open(self.path, 'w') as log_file:
            log.file.close()

        # Set the date of the bot's latest start
        date = datetime.now()
        self.setConfig("Latest Start", date)




def LogWrite():
    with open("Amelie_log.log", 'a') as log:
        log.write(10*'-'+'\n'+ str(format_exc()+'\n'))

    return
