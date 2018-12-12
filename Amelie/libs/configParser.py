# -*- coding: utf-8 -*-
import configparser, os

'''
Module for creating and parsing the settings file
Using the module "configparser" creates a file with specific fields and their properties.

The second function reads the value of the required parameter and returns its value for further verification in the chat file(Chat_AI.py).

'''

def createConfig(path, value):
    """
    Create a config file
    """

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "Language", value)

    with open(path, "w") as config_file:
        config.write(config_file)



def Config(path):

    config = configparser.ConfigParser()
    config.read(path)
    
    lang = config.get("Settings", "Language")

    return lang



def Parser(value):
    lang = Config("./settings.ini")
    if lang == "RU":
        with open("../DataBase/Service_expressionsRU.json", encoding='utf-8') as file:
            ReadFile = file.readlines()

    elif Config("./settings.ini") == "EN":
        with open("../DataBase/Service_expressionsEN.json", encoding='utf-8') as file:
            ReadFile = file.readlines()
        
    text = []
    for line in ReadFile:
        row = line.split(' # ')

        if row[0] == value:
            text.append(row[1])
            return ''.join(text)
