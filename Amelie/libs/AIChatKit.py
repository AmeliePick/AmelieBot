# -*- coding: utf-8 -*

from libs.configParser import SettingsControl

'''
For request editing
'''
def LangChoice():
    #--- Language check --- 
    global dataSet, clearSearch, ANfile
    global checkLang

    checkLang = SettingsControl.getConfig("settings.ini", "lang")

    postfix = "EN.json"
    if checkLang == "RU":
        postfix = "RU.json"

    with open("../DataBase/DataSet_"+postfix, "r", encoding="utf8") as train:
        dataSet = train.readlines()
    
    with open ("../DataBase/ClearSearch"+postfix, "r") as file:
        clearSearch = file.readlines()

    with open ("../DataBase/answers"+postfix, "r") as Afile:
        ANfile = Afile.readlines()

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
            An = Input.replace(item, '')

            
    try:
        An = sub('[?!]', '', An)

        return An.lstrip().capitalize()

    except:
        return Input