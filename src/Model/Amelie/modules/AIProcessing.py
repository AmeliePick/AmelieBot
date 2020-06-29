# -*- coding: utf-8 -*-

from random             import choice
from webbrowser         import open as webbrowser_open
from subprocess         import Popen

from .stemming          import stemming
from .AIFiles           import dataSet, clearSearch, ANfile, checkLang




class Answer:
    ''' The chat's answer formation

    The class is a singleton.

    code: State value.
          0 means to exit from app.
          1 means to continue work.


    '''



    code_ = 1
    output_ = ''
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Answer, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def setCode(self, code) -> None:
        self.code_ = code



    def setText(self, txt) -> None:
        self.output_ = txt



    def getCode(self) -> int:
        return self.code_



    def getOutput(self) -> str:
        return self.output_



def getAnswer(input: str, inputType: str, sessionInput: dict) -> Answer:
    #TODO: refactor this

        answerText = []
        url = ""
        output = Answer()

  
        if inputType == "Exit":
            output.setCode(0)

        elif inputType == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(EditInput(input)), new=1)
    
        elif inputType == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(stemming(EditInput(input))), new=1)
        
        # here we can get an empty answer, when the user says a phrase like "open" and nothing more
        elif inputType == "Open" and EditInput(input) != '':
            try:
                Popen( getProgrammPath( EditInput(input) ) )
            
            except FileNotFoundError:
                    from modules.exceptions_chat import programmNotFound
                    
                    while(True):
                        try:
                            if programmNotFound() != 0:
                                Popen( getProgrammPath( EditInput(input) ) )
                                break

                            else:
                                #change input type
                                break

                        except FileNotFoundError:
                            continue


            except OSError as os:
                if(os.winerror == 87):
                    inputType = "Unknown"


        # get answer
        for line in ANfile:
            row = line.split(' @ ')

            if inputType in line:
                answerText.append(row[1])

        try:
            output.setText(choice(answerText))
            print ("\n<---", output.getOutput())

            # add phrases in DB
            selfLearning(input + " @ " + inputType)
            sessionInput.clear()
                

        except IndexError:
                Unknown = []

                for i in ANfile:
                    row = i.split(' @ ')

                    if "Unknown" in i:
                        Unknown.append(row[1])

                output.setText(choice(Unknown))
                print ("\n<---", output.getOutput())
        

        return output




def LangChoice() -> None:
    ''' Check language choice.

    '''


    from modules.configParser import SettingsControl

    global dataSet, clearSearch, ANfile
    global checkLang

    checkLang = SettingsControl.getConfig("Settings", "lang")

    postfix = "EN.json"
    if checkLang == "RU":
        postfix = "RU.json"


    with open("../DataBase/DataSet_"+postfix, "r", encoding="utf8") as train:
        for line in train:
            dataSet.append(line)

    
    with open ("../DataBase/ClearSearch"+postfix, "r") as file:
        for line in file:
            clearSearch.append(line.replace('\n', ''))
        

    with open ("../DataBase/answers"+postfix, "r") as Afile:
        for line in Afile:
            ANfile.append(line)


    return



def getProgrammPath(search: str) -> str:
    ''' Get the path to the executable file

    '''


    Name: str
    Link: str

    with open('../DataBase/added_programms.json', 'r') as File:
        for line in File:
            
            row = line.split(' = ')

            if search in line:
                Link = str(row[1])
                Name = str(row[0])
               
                if search == Name:
                    return Link.replace('\n', '')
    
    raise FileNotFoundError



def EditInput(input: str) -> str:
    ''' Removes from the user input the stop words.

    Example:
            Input: open Google, find summer wallpapers
            Result: Google, summer wallpapers
    '''


    from re import sub

    global clearSearch

    stopPhrase = ''
    for row in clearSearch:
        if ((input.capitalize()).find(row.capitalize()) != -1):
            stopPhrase = row.replace('\n', '')
            break


    if stopPhrase == '':
        return input
    else:
        result = list(input)
        for i in range(input.capitalize().find(row.capitalize()), len(stopPhrase)):
                       result[i] = ''

        
        
        return sub('[?!]', '', ''.join(result))



def selfLearning(text: str) -> None:
    ''' Word processing and write down to DB's file

    '''

    global checkLang


    if checkLang == "RU":
        with open("../DataBase/DataSet_RU.json", "a", encoding="utf8") as train:
            train.writeline(text)

    elif checkLang == "EN":
        with open("../DataBase/DataSet_EN.json", "a") as train:
            train.writeline(text)

    return





