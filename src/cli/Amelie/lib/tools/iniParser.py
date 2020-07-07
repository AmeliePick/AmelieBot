# -*- coding: utf-8 -*-

from os import path as os_path
from os import SEEK_END
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

        
        
        # if the file is empty, here it will be an exception 
        if not os_path.exists(fileToParsePath):
            handleSettings = open(fileToParsePath, 'w')
            handleSettings.close()

        self.path = fileToParsePath     
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



    def setValue(self, section: str, option: str, value: str) -> None:
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
