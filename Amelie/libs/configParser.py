# -*- coding: utf-8 -*-
from configparser import ConfigParser

'''
Module for creating and parsing the settings file
Using the module "configparser" creates a file with specific fields and their properties.

The second function reads the value of the required parameter and returns its value for further verification in the chat file(Chat_AI.py).

'''

def createConfig(path, value):
    '''
    Create a config file
    '''

    config = ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "Language", value)





def Config(path, option = "NONE"):
    '''
    Getting values from settings
    '''

    config = ConfigParser()
    config.read(path)

    if(option == "lang"):
        lang = config.get("Settings", "language")

        return lang

    if(option == "ver"):
        newVer = config.get("Settings", "ver")

        return newVer

    if(option == "modules"):
        modules = config.get("Settings", "modules")

        return modules


def setConfig(path, option, value):
    '''
    Sets the values of settings in the configuration file
    '''

    config = ConfigParser()
    config.read(path)
    if(option == "lang"):
        config.set("Settings", "language", value)

    if(option == "ver"):
        config.set("Settings", "ver", value)

    if(option == "modules"):
        config.set("Settings", "modules", value)

    with open(path, "w") as config_file:
        config.write(config_file)


def Parser(value):
    '''
    The function for service expressions, 
    so that when changing the language, 
    the text in the whole program changes

    value - Value of expression
    '''
    lang = Config("settings.ini", "lang")
    if lang == "RU":
        with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
            ReadFile = file.readlines()

    elif lang == "EN":
        with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
            ReadFile = file.readlines()
        
    text = []
    for line in ReadFile:
        row = line.split(' # ')

        if row[0] == value:
            text.append(row[1])
            return ''.join(text)


