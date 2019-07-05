# -*- coding: utf-8 -*-

from random             import choice
from webbrowser         import open as webbrowser_open
from subprocess         import Popen

from libs.Stem_Res      import Stemm
from .AIFiles           import dataSet, clearSearch, ANfile, checkLang

class Answer:
    ''' The class is a singleton

    num --- for request processing logic
    if num == 0 > This means exit from the application.

    output --- text for answer to user

    '''
    num = 1
    output = ''
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Answer, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def setNum(self, num):
        self.num = num


    def setText(self, txt):
        self.output = txt


    def getNum(self):
        return self.num


    def getOut(self):
        return self.output


'''
For request editing
'''
def LangChoice():
    #--- Language check --- 
    from libs.configParser import SettingsControl

    global dataSet, clearSearch, ANfile
    global checkLang

    checkLang = SettingsControl.getConfig("settings.ini", "lang")

    postfix = "EN.json"
    if checkLang == "RU":
        postfix = "RU.json"

    with open("../DataBase/DataSet_"+postfix, "r", encoding="utf8") as train:
        for line in train:
            dataSet.append(line)

    
    with open ("../DataBase/ClearSearch"+postfix, "r") as file:
        for line in file:
            clearSearch.append(line)
        

    with open ("../DataBase/answers"+postfix, "r") as Afile:
        for line in Afile:
            ANfile.append(line)


    return


def getProgrammPath(search):
    ''' Get the programm's path
    The function parse the file from the database
    with the names of programs and paths to .exe file
    If the file contains the specified program, 
    the function returns the path to the exe program.
    '''
    Name = ''
    Link = ''

    with open('../DataBase/added_programms.json', 'r') as File:
        for line in File:
            
            row = line.split(' = ')

            if search in line:
                Link = str(row[1])
                Name = str(row[0])
               
    if search in Name:
        return Link
    
    else:
        return


def EditSearch(Input, ToAnswer = ''):
    '''Input editing
    Removes from the user input phrases that are in the database.
    This results in a clean query for a program search operation or a web query.

    Example:
            Input: open Google, find summer wallpaper
            Result: Google, summer wallpaper
    '''
    from re import sub

    global clearSearch
    deleteTextFromInput = []

    for i in clearSearch:
        
        row = i.split(' @ ')
       
        if ToAnswer == "Youtube" and "Youtube" in i:
            deleteTextFromInput.append(row[0])     
            
        elif ToAnswer == "Search" and "Search" in i:
            deleteTextFromInput.append(row[0])

        elif ToAnswer == "Open" and "Open" in i:
            deleteTextFromInput.append(row[0])
           

    for item in deleteTextFromInput:
        if item in deleteTextFromInput and item in Input:              
            Editedtext = Input.replace(item, '')

            
    try:
        Editedtext = sub('[?!]', '', Editedtext)

    except:
        Editedtext = Input


    return Editedtext.lstrip().capitalize()


def selfLearning(text: dict) -> None:
    ''' Word processing and write down to DB's file

    '''

    global checkLang
    getInput = []

    
    for txt, tag in text.items():
        mask = '\n' + txt + ' @ ' + tag
        getInput.append(mask)


    if checkLang == "RU":
        with open("../DataBase/DataSet_RU.json", "a", encoding="utf8") as train:
            train.writelines(getInput)

    elif checkLang == "EN":
        with open("../DataBase/DataSet_EN.json", "a") as train:
            train.writelines(getInput)

    return



'''
Functions for processing user input based on request type, self-learning
For example: Hi Amelie - Hello. How are you? - I'm fine, and you?
'''
Output = Answer()

def answer(input: str, inputType: str, dataSet_new: dict) -> Answer:
    tag = []
    text = []
    url = ""

  
    if inputType == "Exit":
        Output.setNum(0)

    elif inputType == "Search":
        url = "https://www.google.ru/search?q="
        webbrowser_open( url + str(EditSearch(input, inputType)), new=1)
    
    elif inputType == "Youtube":
        url = "http://www.youtube.com/results?search_query="
        webbrowser_open( url + str(Stemm(EditSearch(input, inputType))), new=1)
        
    # here we can get an empty answer, when the user says a phrase like "open" and nothing more
    elif inputType == "Open" and EditSearch(input,  inputType) != '':
        try:
            Popen( getProgrammPath( EditSearch(input, inputType ) ) )
            
        except FileNotFoundError:
            if EditedOpen(EditSearch(input)) == 1:
                from modules.exceptions_chat import programmNotFound

                programmNotFound()
                getProgrammPath(EditSearch(input, inputType))

        except OSError as os:
            if(os.winerror == 87):
                inputType = "Unknown"


    # --- Get answer ---
    for line in ANfile:
        row = line.split(' @ ')
        tag.append(row[0])

        if inputType in line:
            text.append(row[1])

    try:
        Output.setText(choice(text))
        print ("\n<---", Output.getOut())

        # add phrases in DB
        if Output.getNum() == 0 :
            selfLearning(dataSet_new)
            dataSet_new.clear()

    except IndexError:
            Unknown = []

            for i in ANfile:
                row = i.split(' @ ')

                if "Unknown" in i:
                    Unknown.append(row[1])

            Output.setText(choice(Unknown))
            print ("\n<---", Output.getOut())
        

    return Output