# -*- coding: utf-8 -*-

'''
Chat is a neural network that classifies requests from the user. 
Then, after processing the type of the question, it passes it to the answer function, 
where the answer is processed and the operations are performed according to the input.

User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

'''

import sys, random, pickle, re, webbrowser, subprocess, os
from time import sleep
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import model_selection

from libs.Stem_Res import Stemm
from libs.configParser import Config, Parser

#--- Language check --- 
check = Config("settings.ini")

if check == "RU":

    with open ("../DataBase/social.json", "r") as file:
        f = file.readlines()

    with open ("../DataBase/answers.json", "r") as Afile:
        ANfile = Afile.readlines()

if check == "EN":

    with open ("../DataBase/socialEN.json", "r") as file:
        f = file.readlines()

    with open ("../DataBase/answersEN.json", "r") as Afile:
        ANfile = Afile.readlines()


# Variables for EditSearch()
text = []
An = ""

# get ToAnswser from open_AI() in EditSearch()
To = ''

# get global value from input for functions
Chat_Input = ''



'''

Functions for creating and training the neural network to recognize the type of input. 
For example: What is the weather today? - Weather. Where is Paris? - Location

'''

def AI():
    Edit = {'text': [], 'tag':[]}
    for line in f:
        row = line.split(' @ ')
        

        Edit['text'] += [row[0]]
        Edit['tag'] += [row[1]]
    
        
    return Edit

def training(Edit, Val_split = 0.1):
    lenght = len(Edit['text'])
    
    indexes = np.arange(lenght)

    np.random.shuffle(indexes)

    X = [Edit['text'][i]
    for i in indexes ]
    Y = [Edit['tag'][i]
    for i in indexes]

    

    nb_valid_samples = int(Val_split * lenght)



    #save the model to disk
    if check == "RU":
        filename = 'model.sav'

    elif check == "EN":
        filename = 'modelEN.sav'


    pickle.dump(nb_valid_samples, open("models/"+filename, 'wb'))
    
    #load the model from disk
    loaded_model = pickle.load(open("models/"+filename, 'rb'))
  

    return { 
        'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
        'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
    }



def Enter():
    Input = str(input('\n---> ').capitalize())

    global Chat_Input
    Chat_Input = Input

    return Input

def open_AI(Something):
    if Something == 1:
        return 1
    data = AI()
    D = training(data)
    text_clf = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                    ('clf', SGDClassifier(loss='hinge')),
                    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict( D['test']['x'] )

    
    
    
    #Input
    
    

    #give a type of input
    mass = []
    
    
    mass.append(Something)
    try:
        pred = text_clf.predict(mass)
    except:
        return "Pause"
        
    ToAnswser = ''.join(pred).replace('\n', '')
    
    
    To = ToAnswser
    
    global Chat_Input
    Chat_Input = Something

    

    return ToAnswser

def Answer(ToAnswser):
    if ToAnswser == 1:
        return 1

    tag = []
    text = []
    
    for line in ANfile:
        
        row = line.split(' @ ')
        tag.append(row[0])
        
        

        if ToAnswser in line:

            text.append(row[1])

    

    if ToAnswser == "Pause":
        return ''

    if ToAnswser == "Search":
        
        search = webbrowser.open('https://www.google.ru/search?q=' + str(EditSearch(Chat_Input)), new=1)
    
    elif ToAnswser == "Youtube":

        EditS = EditSearch(Chat_Input)
        GetAns = Stemm(EditS)
        
            
        search = webbrowser.open('http://www.youtube.com/results?search_query=' + str(GetAns), new=1)
        
    elif ToAnswser == "Open":

        try:
            search = subprocess.Popen(EditSearch(Chat_Input))
            
        except FileNotFoundError:
            

            Ed = EditedOpen(EditSearch(Chat_Input))

            if Ed == 1:
                from exceptions_chat import except_for_add
                Add_prog = except_for_add()

                if Add_prog == 0:
                    pass


    #Exit from app
    elif ToAnswser == "Exit":
        Output = random.choice(text)
        print ("\n<---", Output)
        sleep(1)
        sys.exit()


    try:

        Output = random.choice(text)
        print ("\n<---", Output)


    except:
        Output = Parser("Unknown")
        print ("\n<---", Output)


    return Output


'''
Net search functions

The processing function of the search query in the search engines.

User input is supplied to the function input and unnecessary search words are removed from it. 
For example: Find music on YouTube - it will be just music


'''

def EditSearch(Input):

    for i in f:
        
        row = i.split(' @ ')
        
        text.append(row[0])
        

        if To == "Youtube" and "Youtube" in i:
            text.append(row[0])
            
        
        elif To == "Search" and "Search" in i:
            text.append(row[0])


        elif To == "Open" and "Open" in i:
            text.append(row[0])
        
        
            
        

    for item in text:
        if item in text and item in Input:

            global An
            An = Input.replace(item, '')

            



    An = re.sub('[?!]', '', An)

    try:
        
        return An.lstrip().capitalize()

    except:
        An = ''

        return An

def EditedOpen(search):
    with open('../DataBase/added_programms.json', 'r') as File:
    #AP = File.readlines()
        Names = []
        Links = []
    

        for line in File:
        
            row = line.split(' = ')
            if search in line:
                if Names != []:
                    Names.clear()
                if Links != []:
                    Links.clear()
            
                Links.append(row[1])
                Names.append(row[0])
            
            



    if search in Names:
        try:
            search = subprocess.Popen(Links[0])
            return 0
        except FileNotFoundError:
            print(Parser("Wrong path"))
            return 1
    else:
        return 1