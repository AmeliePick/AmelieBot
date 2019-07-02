# -*- coding: utf-8 -*-
from os import path as os_path
import configparser

'''
Module for creating and parsing the settings file
Using the module "configparser" creates a file with specific fields and their properties.

The second function reads the value of the required parameter and returns its value for further verification in the chat file(Chat_AI.py).

'''

class Config:
    config = ''
    path = ''

    def getConfig(self, path: str, option: str):
        ''' Getting values from settings

        '''

        self.config.read(path)

        return self.config.get("Settings", option)


    def setConfig(self, path: str, option: str, value, section: str) -> None:
        ''' Sets the values of settings in the configuration file

        '''

        self.config.read(path)


        if not self.config.has_section(option):
            self.config.set(section, option, value)

            with open(path, "w") as config_file:
                self.config.write(config_file)
        
        return


    def createSetting(self, path: str, section: str) -> None:
        self.path = path

        createSettings = open(path, 'a')
        createSettings.close()

        self.config.add_section(section)
        with open(path, "w") as config_file:
            self.config.write(config_file)

        return


    def __init__(self):
        self.config = configparser.ConfigParser()


class settings(Config):
    ''' The class is a singleton

    ReadFile --- Stores data from a file considering language settings

    lang     --- Stores the current language setting

    '''

    ReadFile = ''
    lang = ''


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def Print(self, value: str) -> str:
        '''
        The function for service expressions, 
        so that when changing the language, 
        the text in the whole program changes

        value - name of expression

        '''
        
        text = []
        for line in self.ReadFile:
            row = line.split(' # ')

            if row[0] == value:
                text.append(row[1])
                return ''.join(text)


        '''If the error in the name of the expression
           By recursion it finds the value of the expression by tag "error"

        '''
        return self.Print("error")


    def setLang(self, path: str) -> None:
        '''
        path -- The path where the configuration file is located

        '''

        # Default settings
        self.setConfig(path, "lang", "-")

        choose_lang = input("Choose language [RU] of [EN]: ") #delete this

        while(True):

            if choose_lang == "RU":
                value = "RU"
                self.setConfig(path, "lang", value)
                break

            elif choose_lang == "EN":
                value = "EN"
                self.setConfig(path, "lang", value)
                break

            else:
                choose_lang = input("Choose language [RU] of [EN]: ") #delete this
                continue


    def checkSettings(self) -> None:
        ''' language selection
        A configuration file is created. Further from it all information is read. 
        If the file is empty, which means this is the first launch of the application, the user 
        is prompted to select the bot language.

        '''
        path = "settings.ini"

        if not os_path.exists(path):

            self.createSetting(path)


            self.setConfig(path, "ver", "2.5.2")
            self.setLang(path)

        elif os_path.exists(path):
            ReadHandle = ''

            # Check for empty settings
            with open(path, 'r') as handle:
                ReadHandle = handle.read()

            if ReadHandle == '':
                # set the default settings
                self.createConfig("settings.ini")
                self.setConfig(path, "ver", "2.5.2")
                self.setLang(path)

            if self.getConfig(path, "lang") == '-':
                self.setLang(path)


    def __init__(self):
        super().__init__()
        self.checkSettings()
        self.lang = self.getConfig("settings.ini", "lang")
        if self.lang == "RU":
            with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
                self.ReadFile = file.readlines()

        elif self.lang == "EN":
            with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
                self.ReadFile = file.readlines()
        

SettingsControl = settings()
