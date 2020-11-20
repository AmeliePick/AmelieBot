# -*- coding: utf-8 -*-



from tools.system     import FileManager
from Singleton        import Singleton



class Dialog(metaclass = Singleton):
    ''' Printing messages in current language

    The class is a singleton.

    serviceExpressions: the data from the data base file.

    '''



    serviceExpressions: list



    def __init__(self, appLanguage: str):
        super().__init__()

        self.serviceExpressions = list()
        self.changeLanguage(appLanguage)

        return



    def getMessageFor(self, expression: str) -> str:
        ''' Getting the text of expression by given expression
        '''

        for line in self.serviceExpressions:
            row = line.split(' # ')

            if row[0] == expression:
                return row[1]

        return self.getMessageFor("error")



    def changeLanguage(self, lang: str) -> None:
        self.serviceExpressions = FileManager.readFile("../DataBase/ServiceExpressions" + lang.upper() + ".db")

        return
