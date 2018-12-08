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
