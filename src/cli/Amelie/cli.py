# -*- coding: utf-8 -*-



class Console(object):
    """Command Line Interface class"""



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Amelie, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def write(self, text: str) -> None:
        print(text, end = '')

        return



    def writeLine(self, text: str) -> None:
        print(text, end = '\n')

        return



    def readLine(self, subtitle: str) -> str:
        return input(subtitle)



    def printLogo(self) -> None:
        print ( 70 * "_")
        print ("\t\t                         _ _       \n" +
               "\t\t    /\                  | (_)      \n" +
               "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
               "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
               "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
               "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
        print ( 70 * "_")
