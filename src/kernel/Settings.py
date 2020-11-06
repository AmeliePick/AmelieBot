# -*- coding: utf-8 -*-


from Singleton              import Singleton
from tools.system           import FileManager
from tools.iniParser        import IniParser

from re import sub


class Settings(metaclass = Singleton):
    ''' Control the config file, database files and other file of the app.

    The class is a Singleton.
    '''


    _fileManager: FileManager
    _iniParser: IniParser
    _methods: dict



    def __init__(self):
        super().__init__()

        self._fileManager = FileManager()
        if not FileManager.dirExist("TEMP"):
            FileManager.createDir("TEMP")
        if not FileManager.fileExist("../DataBase/addedProgramms.db"):
            FileManager.clearFile("../DataBase/addedProgramms.db")


        self._iniParser = IniParser("settings.ini")
        self._methods = dict()
        self._supportingLangs = dict()

        langs = (self._iniParser.getValue("AppData", "langs", "../setup/AppSetup.ini")).split(", ")
        for index in range(0, len(langs)):
            self._supportingLangs[index + 1] = langs[index]



        if len(FileManager.readFile("settings.ini")) == 0:
            self._iniParser.setSection("Settings")
            self._iniParser.setSection("Bot")
            self._iniParser.setSection("User")

            self._iniParser.setValue("Settings",
                                     "ver",
                                     self._iniParser.getValue("Setup", "Version", "../setup/AppSetup.ini")
                                    )

            self._iniParser.setValue("Settings", "lang", "-")
            self._iniParser.setValue("Bot", "botAvatar", "-")
            self._iniParser.setValue("User", "userAvatar", "-")
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



    def setBotAvatar(self, avatarName: str) -> None:
        self._iniParser.setValue("Bot", "botAvatar", avatarName)



    def setUserAvatar(self, avatarName: str) -> None:
        self._iniParser.setValue("User", "userAvatar", avatarName)



    def getLanguage(self) -> str:
        return self._iniParser.getValue("Settings", "lang")



    def getSupportingLangs(self) -> list:
        return self._iniParser.getValue("AppData", "langs", "../setup/AppSetup.ini").split(',')



    def getBotAvatars(self) -> list:
        return self._iniParser.getValue("AppData", "botAvatars", "../setup/AppSetup.ini").split(',')



    def getUserAvatars(self) -> list:
        return self._iniParser.getValue("AppData", "userAvatars", "../setup/AppSetup.ini").split(',')


    def getBotAvatar(self) -> str:
        return self._iniParser.getValue("Bot", "botAvatar")



    def getUserAvatar(self) -> str:
        return self._iniParser.getValue("User", "userAvatar")



    def getUsername(self) -> str:
        return self._iniParser.getValue("User", "name")



    def getMethodsToResolveErrors(self) -> dict:
        return self._methods



    def __del__(self):
        FileManager.deleteDir("TEMP")
