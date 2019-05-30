# -*- coding: utf-8 -*-
from configparser import ConfigParser

'''
Module for creating and parsing the settings file
Using the module "configparser" creates a file with specific fields and their properties.

The second function reads the value of the required parameter and returns its value for further verification in the chat file(Chat_AI.py).

'''

class settings:
    ''' The class is a singleton

    ReadFile --- Stores data from 
    a file considering language settings

    lang --- Stores the current language setting

    '''

    ReadFile = ''
    lang = ''
    config = ConfigParser()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def createConfig(self, path):
        '''
        Create a config file
        '''

        self.config.add_section("Settings")

        with open(path, "w") as config_file:
            config.write(config_file)


    def getConfig(self, path, option = "NONE"):
        '''
        Getting values from settings
        '''

        self.config.read(path)

        if(option == "lang"):
            lang = self.config.get("Settings", "language")

            return lang

        if(option == "ver"):
            newVer = self.config.get("Settings", "ver")

            return newVer

        if(option == "modules"):
            modules = self.config.get("Settings", "modules")

            return modules


    def setConfig(self, path, option, value):
        '''
        Sets the values of settings in the configuration file
        '''

        self.config.read(path)

        if(option == "lang"):
            self.config.set("Settings", "language", value)

        elif(option == "ver"):
            self.config.set("Settings", "ver", value)

        elif(option == "modules"):
            self.config.set("Settings", "modules", value)

        with open(path, "w") as config_file:
            self.config.write(config_file)


    def Print(self, value):
        '''
        The function for service expressions, 
        so that when changing the language, 
        the text in the whole program changes

        value - Value of expression
        '''
        
        text = []
        for line in self.ReadFile:
            row = line.split(' # ')

            if row[0] == value:
                text.append(row[1])
                return ''.join(text)

    def __init__(self):
        self.lang = self.getConfig("settings.ini", "lang")
        if self.lang == "RU":
            with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
                self.ReadFile = file.readlines()

        elif self.lang == "EN":
            with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
                self.ReadFile = file.readlines()


SettingsControl = settings()
