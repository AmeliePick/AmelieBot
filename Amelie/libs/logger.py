# -*- coding: utf-8 -*-

'''
Log file maintenance
'''
from traceback      import format_exc
from datetime       import datetime
from os             import path as os_path

from libs.configParser      import Config




class SessionLog(Config):
    ''' The class is a singleton


    '''
    section = "Records"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SessionLog, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def SessionCollector(self, option: str, value: str) -> None:
        self.setConfig(self.path, option, value, self.section)


    def __init__(self):
        super().__init__()

        path = "session_journal.log"
        section = "Records"

        if not os_path.exists(path):
            self.createSetting(path, self.section)

        else:
            # clearing the session log file from old records
            with open(path, 'w') as log_file:
                log_file.close()
            self.config.add_section(self.section)
            self.path = path


        # Set the date of the bot's latest start
        date = datetime.now()
        self.setConfig(path, "Latest start", str(date), section)


    def __del__(self):
        with open(path, "w") as log_file:
            self.config.write(log_file)


sessionLogger = SessionLog()


def LogWrite():
    with open("Amelie_log.log", 'a') as log:
        log.write(10*'-'+'\n'+ str(format_exc()+'\n'))

    return
