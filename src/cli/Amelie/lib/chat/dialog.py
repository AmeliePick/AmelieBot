# -*- coding: utf-8 -*-



from ..tools.system     import FileManager



class Dialog():
    ''' Printing messages in current language

    The class is a singleton.

    serviceExpressions: the data from the data base file.

    '''



    serviceExpressions: str



    def __init__(self, appLanguage: str):
        super().__init__()

        self.serviceExpressions = FileManager.readFile("../../DataBase/Service_expressions" + appLanguage + ".json")

        return
    


    def __new__(cls, appLanguage: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Dialog, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def getMessageBy(self, expression: str) -> str:
        ''' Getting the text of expression by given expression
        '''

        text = list()
        for line in self.serviceExpressions:
            row = line.split(' # ')

            if row[0] == expression:
                text.append(row[1])
                return ''.join(text)


        '''
        If the error exist in the name of the expression
        By recursion it finds the value of the expression by "error" tag.
        '''
        return self.getMessageBy("error")