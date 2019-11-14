# -*- coding: utf-8 -*-

from random             import choice
from webbrowser         import open as webbrowser_open
from subprocess         import Popen

from libs.Stemming      import Stemm
from .AIFiles           import dataSet, clearSearch, ANfile, checkLang

class Answer:
    ''' The class is a singleton

    code --- for request processing logic
    if code == 0 > This means exit from the application.

    self --- text for answer to user

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
        answerType = []
        answerText = []
        url = ""
        output = Answer()

  
        if inputType == "Exit":
            output.setCode(0)

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
            answerType.append(row[0])

            if inputType in line:
                answerText.append(row[1])

        try:
            output.setText(choice(answerText))
            print ("\n<---", output.getOutput())

            # add phrases in DB
            if output.getCode() == 0 :
                selfLearning(sessionInput)
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
    Fill in the fields with the necessary data based on the choice of language.
    '''
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


def getProgrammPath(search) -> str:
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


def EditSearch(Input, ToAnswer = '') -> str:
    '''Input editing
    Removes from the user input the stop words.
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
     
    modified = False
    for item in deleteTextFromInput:
        if item in Input:
            Editedtext = Input.replace(item, '')
        elif item.capitalize() in Input.capitalize(): 
            Editedtext = Input.capitalize().replace(item.capitalize(), '')
            modified = True

        else:
            continue

        Editedtext = Editedtext.lstrip()

        break
        
    clearText = [] # Original words
    wordLen = 0
    text = []
    if modified:
        # word breakdown
        word = []
        for char in Input:
            if char == ' ':
                clearText.append(''.join(word))
                word.clear()
            else:
                word.append(char)
        clearText.append(''.join(word))

        # Search for original spelling
        # word --- is an original word
        for word in clearText:
            if word.lower() in Editedtext.lower():
                text.append(word)
                
        Editedtext = ' '.join(text)


    try:
        Editedtext = sub('[?!]', '', Editedtext)

    except:
        Editedtext = Input


    return Editedtext.lstrip()


def selfLearning(text: dict) -> None:
    ''' Word processing and write down to DB's file

    '''

    global checkLang
    getInput = []

    # Fill the array all inputs phrases
    for txt, tag in text.items():
        statement = '\n' + txt + ' @ ' + tag
        getInput.append(statement)


    if checkLang == "RU":
        with open("../DataBase/DataSet_RU.json", "a", encoding="utf8") as train:
            train.writelines(getInput)

    elif checkLang == "EN":
        with open("../DataBase/DataSet_EN.json", "a") as train:
            train.writelines(getInput)

    return





