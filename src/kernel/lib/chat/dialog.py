# -*- coding: utf-8 -*-



from ..tools.system     import FileManager
from ..Singleton        import Singleton



class Dialog(metaclass = Singleton):
    ''' Printing messages in current language

    The class is a singleton.

    serviceExpressions: the data from the data base file.

    '''



    serviceExpressions: str



    def __init__(self, appLanguage: str):
        super().__init__()

        self.changeLanguage(appLanguage)

        return



    def getMessageFor(self, expression: str) -> str:
        ''' Getting the text of expression by given expression
        '''

        text = list()
        for line in self.serviceExpressions:
            row = line.split(' # ')

            if row[0] == expression:
                text.append(row[1])
                return ''.join(text)

        return self.getMessageFor("error")



    def changeLanguage(self, lang: str) -> None:
        self.serviceExpressions = FileManager.readFile("../DataBase/ServiceExpressions" + lang.upper() + ".db")

        return