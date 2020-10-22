# -*- coding: utf-8 -*-


from Singleton              import Singleton
from tools.system           import FileManager
from tools.iniParser        import IniParser

from re import sub


class Settings(metaclass = Singleton):
    ''' Control the config file

    The class is a Singleton.
    '''


    _fileManager: FileManager
    _iniParser: IniParser
    _methods: dict

    _supportingLangs: list


    def __init__(self):
        super().__init__()
        self._iniParser = IniParser("settings.ini")

        self._methods = dict()
        self._supportingLangs = dict()

        langs = (self._iniParser.getValue("AppData", "langs", "../setup/AppSetup.ini")).split(", ")
        for index in range(0, len(langs)):
            self._supportingLangs[index + 1] = langs[index]



        if len(FileManager.readFile("settings.ini")) == 0:
            self._iniParser.setSection("Settings")
            self._iniParser.setSection("User")

            self._iniParser.setValue("Settings",
                                     "ver",
                                     self._iniParser.getValue("Setup", "Version", "../setup/AppSetup.ini")
                                    )

            self._iniParser.setValue("Settings", "lang", "-")
            self._iniParser.setValue("User", "name", '')



        if len(self.getLanguage()) != 2:
            self._methods["lang"] = self.setLanguage


        from re import sub
        if len(sub('[\t, \n, \r \s]', '', self.getUsername())) < 2:
            self._methods["username"] = self.setUsername


        return



    def setLanguage(self, langValue: str) -> None:
        self._iniParser.setValue("Settings", "lang", langValue)

        return



    def setUsername(self, nameValue: str) -> bool:
        if len(sub('[\t, \n, \r \s]', '', nameValue)) >= 2:
            self._iniParser.setValue("User", "name", nameValue)
            return True

        return False



    def getLanguage(self) -> str:
        return self._iniParser.getValue("Settings", "lang")



    def getSupportingLangs(self) -> list:
        self._supportingLangs = self._iniParser.getValue("AppData", "langs", "../setup/AppSetup.ini").split(',')
        return self._supportingLangs



    def getUsername(self) -> str:
        return self._iniParser.getValue("User", "name")



    def getMethodsToResolveErrors(self) -> dict:
        return self._methods
