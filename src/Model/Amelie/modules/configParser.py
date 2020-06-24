# -*- coding: utf-8 -*-

from os import path as os_path
import configparser



''' Module for creating and parsing the settings file
Settings class - for work with settings file.
MessagePrinter class - for work with service expressions

'''

class Config:
    config: configparser.ConfigParser()
    path: str


    def __init__(self):
        self.config = configparser.ConfigParser()
        return


    def setSection(self, section: str) -> None:
        ''' Set the new section in file

        '''

        self.config.read(self.path);

        if not self.config.has_section(section):
            self.config.add_section(section)
        
            with open(self.path, "w") as config_file:
                self.config.write(config_file)
        return


    def getConfig(self, section: str, option: str, path = "") -> str:
        ''' Getting values from settings

        '''

        if path == "":
            self.config.read(self.path)
        else:
            self.config.read(path)

        return self.config.get(section, option)


    def setConfig(self, section: str, option: str, value: str, ) -> None:
        ''' Sets the values of settings in the configuration file

        '''

        self.config.read(self.path)


        if self.config.has_section(section):
            self.config.set(section, option, value)

        with open(self.path, "w") as config_file:
            self.config.write(config_file)
        
        return


    def swapFile(self, file_path: str) -> None:
        ''' Change the file path

        '''

        self.path = file_path
        
        return


    def cleanConfig(self) -> None:
        ''' Remove all items from config

        '''

        sectionsList: list

        sectionsList = self.config.sections()

        for section in sectionsList:
            self.config.remove_section(section)

        return



class IniParser(Config):
    ''' The class is a singleton.
    Parser for reading another config files.

    '''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(IniParser, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def _getConfig(self, section, option, path = "") -> str:

        if path == "": raise Exception("He needs some path") 


        value = self.getConfig(section, option, path)

        '''
        When we reads any file, the config's variables keep storage the data from the config file.
        And it leads to incorrect reading parameters in the next time. So we must to clear the data after each reading.

        '''
        self.cleanConfig()

        return value



class Settings(Config):
    ''' The class is a singleton
    Parser for settings file.

    lang - Stores the current language setting.

    '''
    lang: str



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def createSettings(self, path: str, section: str) -> None:
        ''' Create the settings file and add first section to that
        '''
        self.path = path

        handleSettings = open(path, 'w')
        handleSettings.close()

        self.config.add_section(section)
        with open(self.path, "w") as config_file:
            self.config.write(config_file)

        return

    
    def setLanguage(self) -> None:
        '''
        path -- The path where the configuration file is located

        '''

        self.lang = input("Choose language [RU] of [EN]: ")
        while(True):

            if self.lang == "RU":                
                break

            elif self.lang == "EN":
                break

            else:
                self.lang = input("Choose language [RU] of [EN]: ")
                continue


        self.setConfig("Settings", "lang",  self.lang)

        
    def checkSettingsInfo(self) -> None:
        ''' Checking the validity of the settings file
        A configuration file is created. Further from it all information is read. 
        If the file is empty, which means this is the first launch of the application, the user 
        is prompted to select the bot language.

        '''
        
        AppVersion = iniParser._getConfig("Setup", "Version", "Version/AppSetup.ini")

        
        self.path = "settings.ini"

        if not os_path.exists(self.path):

            self.createSettings(self.path, "Settings")

            # set the default settings
            self.setConfig("Settings", "ver", AppVersion)
            self.setConfig("Settings", "lang", '-')
            self.setLanguage()

        elif os_path.exists(self.path):
            ReadHandle = ''

            # Check for empty settings
            with open(self.path, 'r') as handle:
                ReadHandle = handle.read()

            if ReadHandle == '' or ReadHandle == '\n':
                # set the default settings
                self.setSection("Settings")
                self.setConfig("Settings", "ver", AppVersion)
                self.setLanguage()

            if self.getConfig("Settings", "lang") == '-':
                self.setLanguage()

        return


    def __init__(self):
        super().__init__()
        
        self.checkSettingsInfo()

        self.lang = self.getConfig("Settings", "lang")
        if self.lang == "RU":
            with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
                self.serviceExpressions = file.readlines()

        elif self.lang == "EN":
            with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
                self.serviceExpressions = file.readlines()

        return

      

class MessagePrinter:
    ''' The class is a singleton
    Printing messages in current language
    
    serviceExpressions - the DB file

    '''
    serviceExpressions: str



    def __new__(cls, settings: Settings):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessagePrinter, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def __init__(self, settings: Settings):
        super().__init__()

        if settings.getConfig("Settings", "lang") == "RU":
            with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
                self.serviceExpressions = file.readlines()

        elif settings.getConfig("Settings", "lang") == "EN":
            with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
                self.serviceExpressions = file.readlines()
        return
    

    def print(self, value: str) -> str:
        '''
        The function for service expressions, 
        so that when changing the language, 
        the text in the whole program changes

        value - name of expression

        '''

        text = []
        for line in self.serviceExpressions:
            row = line.split(' # ')

            if row[0] == value:
                text.append(row[1])
                return ''.join(text)


        '''If the error in the name of the expression
           By recursion it finds the value of the expression by tag "error"

        '''
        return self.Print("error")



iniParser = IniParser()

SettingsControl = Settings()

DisplayText = MessagePrinter(SettingsControl)