# -*- coding: utf-8 -*-



from .tools.system          import FileManager
from .tools.iniParser       import IniParser



class Settings(object):
    """Control the config file"""


    _fileManager: FileManager
    _iniParser: IniParser
    _methods: dict

    _supportingLangs: dict


    def __init__(self):
        super().__init__()
        self._iniParser = IniParser("settings.ini")

        self._methods = dict()
        self._supportingLangs = dict()

        langs = (self._iniParser.getValue("AppData", "langs", "../../Version/AppSetup.ini")).split(", ")
        for index in range(0, len(langs)):
            self._supportingLangs[index + 1] = langs[index]



        if len(FileManager.readFile("settings.ini")) == 0:
            self._iniParser.setSection("Settings")
            self._iniParser.setSection("User")

            self._iniParser.setValue("Settings", 
                                     "ver", 
                                     self._iniParser.getValue("Setup", "Version", "../../Version/AppSetup.ini")
                                    )


            


        if len(self.getLanguage()) != 2:
            self._iniParser.setValue("Settings", "lang", "-")
            self._methods["lang"] = self.setLanguage


        from re import sub
        if len(sub('[\t, \n, \r \s]', '', self.getUsername())) < 2:
            self._iniParser.setValue("User", "name", '')
            self._methods["username"] = self.setUsername


        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance




    def setLanguage(self, langValue: str) -> None:
        self._iniParser.setValue("Settings", "lang", langValue)

        return



    def setUsername(self, nameValue: str) -> None:
        self._iniParser.setValue("User", "name", nameValue)

        return



    def getLanguage(self) -> str:
        return self._iniParser.getValue("Settings", "lang")



    def getSupportingLangs(self) -> dict:
        return self._supportingLangs



    def getUsername(self) -> str:
        return self._iniParser.getValue("User", "name")



    def getMethodsToResolveErrors(self) -> dict:
        return self._methods
