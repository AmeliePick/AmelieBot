# -*- coding: utf-8 -*-


from shutil import rmtree as shutil_rmtree
from os     import path as os_path
from os     import remove
from os     import makedirs as os_makedirs



class FileManager:
    ''' Providing the interface to work with file system
    '''



    def __init__(self):
        super().__init__()

        if not os_path.isdir("TEMP"):
            os_makedirs("TEMP")


        return
        


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    @staticmethod
    def fileExist(file: str) -> bool:
        return os_path.exists(file)


    @staticmethod
    def writeToFile(value: str, file: str, mode = 'a', _encoding="utf-8") -> None:
        if 'b' in mode:
            with open (file, mode) as file:
                file.write(value)
        else:
            with open (file, mode, encoding = _encoding) as file:
                file.write(value)

        return



    @staticmethod
    def readFile(file: str, _encoding="utf-8") -> str:
        with open (file, encoding = _encoding) as file:
            return file.readlines()

        return



    @staticmethod
    def createFile(file: str) -> None:
        if not os_path.exists(file):
            with open(file, 'w'): pass

        return



    @staticmethod
    def deleteFile(file: str) -> None:
        if os_path.exist(file):
            os.remove(file)

        return



    @staticmethod
    def clearFile(file: str) -> None:
        if os_path.exists(file):
            with open(file, 'w') as _file:
                _file.close()

        return



    def __del__(self):
        if os_path.isdir("TEMP"):
            shutil_rmtree("TEMP", ignore_errors = True)

        return
