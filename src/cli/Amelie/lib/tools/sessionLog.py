# -*- coding: utf-8 -*-

''' Log file maintenance module
'''


from traceback      import format_exc
from datetime       import datetime
from os             import path as os_path

from .configParser      import Config




class SessionLog(Config):
    ''' Collects data from the current session and generates a session log file
    The class is a singleton
    section - the default section in log file

    '''
    section: str



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SessionLog, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def sessionCollector(self, option: str, value: str) -> None:
        ''' Write in a config a parameter from the current session.
        option - title of recording.
        value - the value of recording/parameter.

        '''

        self.setConfig(self.section, option, value)


    def __init__(self):
        super().__init__()

        path = "session_journal.log"
        self.section = "Records"

        if not os_path.exists(path):
            self.createSettings(path, self.section)

        else:
            # Clearing the session log file from old records
            with open(path, 'w') as log_file:
                log_file.close()
            self.config.add_section(self.section)
            self.path = path


        # Set the date of the bot's latest start
        date = datetime.now()
        self.setConfig(self.section, "Latest start", str(date), )


    def __del__(self):
        with open(path, "w") as log_file:
            self.config.write(log_file)
        return



def LogWrite() -> None:
    ''' Collects data from traceback when error is happen and writes to log file

    '''

    with open("Amelie_log.log", 'a') as log:
        log.write(10*'-'+'\n'+ str(format_exc()+'\n'))

    return



sessionLogger = SessionLog()
