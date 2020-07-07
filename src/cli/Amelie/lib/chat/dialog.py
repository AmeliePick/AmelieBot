from ..tools.oc     import fileManager



class Dialog():
    """ Printing messages in current language

    The class is a singleton.

    serviceExpressions: the data from the data base file.

    """



    serviceExpressions: str



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Dialog, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def __init__(self, languageValue: str):
        super().__init__()

        initDataBase(languageValue)

        return
    


    def getMessageBy(self, value: str) -> str:
        ''' Getting the text of expression by given value

        value: name of the expression.

        '''

        text = []
        for line in self.serviceExpressions:
            row = line.split(' # ')

            if row[0] == value:
                text.append(row[1])
                return ''.join(text)


        '''
        If the error exist in the name of the expression
        By recursion it finds the value of the expression by "error" tag
        '''
        return self.Print("error")



    def initByDataBase(self, appLanguage: str):
        self.serviceExpressions = fileManager.readFile("../DataBase/Service_expressions"+appLanguage+".json")


        return