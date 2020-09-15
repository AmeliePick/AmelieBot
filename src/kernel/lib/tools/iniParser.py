# -*- coding: utf-8 -*-

import configparser
from os      import path as os_path

from Singleton        import Singleton
from .system           import FileManager



class IniParser(object):
    ''' Parse the .ini file.
    '''



    config: configparser.ConfigParser()
    path: str



    def __init__(self, fileToParsePath: str):
        self.config = configparser.ConfigParser()


        if not os_path.exists(fileToParsePath):
            FileManager.createFile(fileToParsePath)

        self.path = fileToParsePath
        self.config.read(self.path)

        return



    def setSection(self, section: str) -> None:
        ''' Set the new section in the file.
        '''

        if not self.config.has_section(section):
            self.config.add_section(section)

            with open(self.path, "w") as config_file:
                self.config.write(config_file)

        return



    def getValue(self, section: str, option: str, path = "") -> str:
        ''' Getting values from settings.
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
        ''' Sets the value of settings in the configuration file.
        '''

        if self.config.has_section(section):
            self.config.set(section, option, value)

        with open(self.path, "w") as config_file:
            self.config.write(config_file)

        return



    def swapFile(self, file_path: str) -> None:
        ''' Change the file path.
        '''

        self.path = file_path

        return



    def clearConfig(self) -> None:
        ''' Remove all items from the config.
        '''

        for section in self.config.sections():
            self.config.remove_section(section)

        return



    def update(self) -> None:
        ''' Update parser's variables.
        '''

        self.clearConfig()
        self.config.read(self.path)

        return
