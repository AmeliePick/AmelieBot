# -*- coding: utf-8 -*-

'''
Request module for adding a program to the database

'''


from os     import path as os_path
from os     import makedirs as os_makedirs



class FileManager:


    def __init__(self):
        super().__init__()

        os_makedirs("TEMP")
        



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def writeToFile(self, value: str, file: str, mode = 'a') -> None:
        with open (file, mode) as file:
            file.write(value)
        return



    def readFile(self, file: str, encoding="utf8") -> str:
        with open (file, mode, encoding) as file:
            return file.readlines()



    def __del__(self):
        if os_path.isdir("TEMP"):
            os.rmdir("TEMP")



