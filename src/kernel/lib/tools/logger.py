# -*- coding: utf-8 -*-



from traceback      import format_exc
from datetime       import datetime
from os             import path as os_path

from .system        import FileManager
from .iniParser     import IniParser



class Logger(IniParser):
    ''' Collects data from the current session and generates a session log file

    The class is a singleton.
    '''



    def __init__(self):
        super().__init__("session_journal.log")

        # Clearing the session log file from old records
        FileManager.clearFile(self.path)

        # Set the date of the bot's latest start
        self.setValue("Records", "Latest start", str(datetime.now()))


        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def addRecord(self, recordTitle: str, value: str) -> None:
        ''' Add the record to the log file.
        '''

        self.setValue("Records", recordTitle, value)

        return



    def logWrite(self) -> None:
            ''' Collect data from traceback when error is happen and writes to log file.
            '''

            with open("Amelie_log.log", 'a') as log:
                log.write(100*'='+'\n'+ str(format_exc()+'\n'))

            return
