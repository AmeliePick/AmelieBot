# -*- coding: utf-8 -*-

from os import path as os_path
import configparser



''' Module for creating and parsing the settings file
Settings class - for work with the settings file.
'''


class IniParser(object):
    ''' Parser to read another config files
    '''

    #TODO: fix the not safety ctor.


    config: configparser.ConfigParser()
    path: str


    # NOT SAFETY CONSTRUCTOR #
    def __init__(self, fileToParsePath: str):
        self.config = configparser.ConfigParser()

        self.path = fileToParsePath
        
        # if the file is empty, here it will be an exception 
        self.config.read(self.path)

        return



    def setSection(self, section: str) -> None:
        ''' Set the new section in file
        '''


        if not self.config.has_section(section):
            self.config.add_section(section)

            with open(self.path, "w") as config_file:
                self.config.write(config_file)

        return



    def getValue(self, section: str, option: str, path = "") -> str:
        ''' Getting values from settings
        '''

        if path != "":
            self.config.read(path)

            value = self.config.get(section, option)
        
            # When we reads any file, the config's variables keep storage the data from the config file.
            # And it leads to incorrect reading parameters in the next time. So we must to clear the data after each reading.
            self.update()

            return value

        return self.config.get(section, option)



    def setValue(self, section: str, option: str, value: str, ) -> None:
        ''' Sets the values of settings in the configuration file
        '''

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


        for section in self.config.sections():
            self.config.remove_section(section)

        return



    def update(self) -> None:
        '''
        Update parser's variables
        '''


        self.cleanConfig()
        self.config.read(self.path)

        return




class Settings(IniParser):
    ''' Parser for settings file.
    The class is a singleton.
    
    lang: Current language setting.
    '''

    lang: str



    def __init__(self):
        #TODO: fix the not safety ctor.
        if not os_path.exists(self.path):
            self.createSettings(self.path, "Settings")

        try:
            super().__init__("settings.ini")
        except ConfigParser.NoSectionError:
            self.checkSettingsInfo()


        self.lang = self.getValue("Settings", "lang")
        
        with open("../DataBase/Service_expressions"+ self.lang + ".json", encoding='utf-8') as file:
                self.serviceExpressions = file.readlines()

            
        return



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
            return cls.instance

        return cls.instance



    def createSettings(self, path: str, section: str) -> None:
        ''' Create the settings file and add first section to that
        '''


        handleSettings = open(path, 'w')
        handleSettings.close()

        self.config.add_section(section)
        with open(self.path, "w") as config_file:
            self.config.write(config_file)

        return



    def setLanguage(self, lang: str) -> None:
        '''
        lang: Current language choice. Using the ISO 639-3 standard
        '''

        if len(lang) < 3:
            raise AttributeError

        self.lang = lang.lower()
        self.setValue("Settings", "lang",  self.lang)

        return



    def checkSettingsInfo(self) -> None:
        ''' Checking the validity of the settings file.
        '''

        AppVersion = self.getValue("Setup", "Version", "../../Version/AppSetup.ini")

        # Check for empty settings
        with open(self.path, 'r') as handle:
            ReadHandle = handle.read()

            if ReadHandle == '' or ReadHandle == '\n':
                # set the default settings
                self.setSection("Settings")
                self.setConfig("Settings", "ver", AppVersion)
                ###self.setLanguage()

            ###if self.getConfig("Settings", "lang") == '-':
                ###self.setLanguage()
       

            

        return



iniParser = IniParser()

SettingsControl = Settings()
