# -*- coding: utf-8 -*-

'''
Request module for adding a program to the database

'''


class FileManager:


    def __init__(self):
        super().__init__()



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def AddProgramm(self, name: str, path: str) -> None:
        with open ("../DataBase/added_programms.json", 'a') as file:
            file.write(name + " = " + path)

        return



    def getProgrammPath(self, name: str) -> str:
                ''' Get the path to the executable file

                '''


                with open('../DataBase/added_programms.json', 'r') as File:
                    for line in File:
                        row = line.split(" = ")
                    
                        if row[0].lower() in name.lower():
                            return row[1].replace('\n', '')
    
                return ''



    def programmNotFound(self):
        print("<--- "+ DisplayText.print("n_found"))
        print(DisplayText.print("addPr"))
        input_ = input("--> ")

        if input_ == "Y" or  input_ == "y":
            AddProgramm()
        else:
            return 0



fileManager = FileManager()