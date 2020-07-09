# -*- coding: utf-8 -*-



from os     import path as os_path
from os     import remove
from os     import makedirs as os_makedirs



class FileManager:
    ''' Providing the interface to work with file system
    '''



    def __init__(self):
        super().__init__()

        os_makedirs("TEMP")


        return
        


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    @staticmethod
    def writeToFile(value: str, file: str, mode = 'a') -> None:
        with open (file, mode) as file:
            file.write(value)

        return



    @staticmethod
    def readFile(file: str, encoding="utf8") -> str:
        with open (file, mode, encoding) as file:
            return file.readlines()

        return



    @staticmethod
    def createFile(file: str) -> None:
        if not os.path.exists(file):
            with open(file, 'w'): pass

        return



    @staticmethod
    def deleteFile(file: str) -> None:
        if os_path.exist(file):
            os.remove(file)

        return



    @staticmethod
    def clearFile(file: str) -> None:
        if os_path.exist(file):
            with open(path, 'w') as file:
                file.close()



    def __del__(self):
        if os_path.isdir("TEMP"):
            os.rmdir("TEMP")

        return
