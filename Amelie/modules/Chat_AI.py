# -*- coding: utf-8 -*-

'''
Chat is a neural network that classifies requests from the user. 
Then, after processing the type of the question, it passes it to the answer function, 
where the answer is processed and the operations are performed according to the input.

User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

'''
import random
import numpy as np

from webbrowser import open as webbrowser_open
from os import _exit
from pickle import dump
from pickle import load
from subprocess import Popen
from re import sub
from time import sleep

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import model_selection

from libs.Stem_Res import Stemm
from libs.configParser import Config, Parser


class answer:
    num = 0
    output = ''

    def __init__(self, num, output):
        self.num = num
        self.output = output

    def getNum(self):
        return self.num

    def getOut(self):
        return self.output





#--- Language check --- 
check = Config("settings.ini", "lang")

postfix = "EN.json"
if check == "RU":
     postfix = "RU.json"

with open("../DataBase/DataSet_"+postfix, "r", encoding="utf8") as train:
    Ftrain = train.readlines()
    
with open ("../DataBase/ClearSearch"+postfix, "r") as file:
    f = file.readlines()

with open ("../DataBase/answers"+postfix, "r") as Afile:
    ANfile = Afile.readlines()
        

Chat_Input = ""

# Variables for EditSearch()
text = []


'''

Functions for creating and training the neural network to recognize the type of input. 
For example: What is the weather today? - Weather. Where is Paris? - Location

'''

def AI():
    Edit = {'text': [], 'tag':[]}
    for line in Ftrain:
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
    filename = 'modelEN.sav'
    if check == "RU":
        filename = 'model.sav'



    dump(nb_valid_samples, open("models/"+filename, 'wb'))
    
    #load the model from disk
    loaded_model = load(open("models/"+filename, 'rb'))
  

    return { 
        'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
        'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
    }


def Enter():
    while(True):
        try:
            Input = str(input('\n---> ').capitalize())
            
            if Input == '' or Input == '\n':
                raise KeyboardInterrupt

        except KeyboardInterrupt:
            print("\n\n<--- " + Parser("WrongInput"))
            continue
            

        global Chat_Input
        Chat_Input = Input

        return Input


def open_AI(Something):
    data = AI()
    D = training(data)
    text_clf = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                    ('clf', SGDClassifier(loss='hinge')),
                    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict( D['test']['x'] )

    #give a type of input
    mass = []
    
    
    mass.append(Something)

    global Chat_Input
    Chat_Input = Something

    try:
        pred = text_clf.predict(mass)
    except:
        return "Pause"
        
    ToAnswser = ''.join(pred).replace('\n', '')
    
    global To
    To = ToAnswser

    

    return ToAnswser


def selfLearning(InputType):
    global Chat_Input
    getInput = str(Chat_Input) + ' @ ' + InputType + "\n"

    if check == "RU":
        with open("../DataBase/DataSet_RU.json", "a", encoding="utf8") as train:
            train.write(getInput)
    if check == "EN":

        with open("../DataBase/DataSet_EN.json", "a") as train:
            train.write(getInput)


def Answer(ToAnswser):

    selfLearning(ToAnswser)

    if ToAnswser == "Search":
        
        search = webbrowser_open('https://www.google.ru/search?q=' + str(EditSearch(Chat_Input)), new=1)
    
    elif ToAnswser == "Youtube":

        EditS = EditSearch(Chat_Input)
        GetAns = Stemm(EditS)
        
        search = webbrowser_open('http://www.youtube.com/results?search_query=' + str(GetAns), new=1)
        
    elif ToAnswser == "Open":

        try:
            search = Popen(EditSearch(Chat_Input))
            
        except FileNotFoundError:
        
            Ed = EditedOpen(EditSearch(Chat_Input))
            if Ed == 1:
                from modules.exceptions_chat import except_for_add
                Add_prog = except_for_add()

                search = EditedOpen(EditSearch(str(Chat_Input)))

        except OSError as e:
            if(e.winerror == 87):
                ToAnswser = "Unknown"
        
        
    # --- Get answer ---
    tag = []
    text = []
    
    for line in ANfile:
        
        row = line.split(' @ ')
        tag.append(row[0])
        

        if ToAnswser in line:
            text.append(row[1])



    try:
        Output = random.choice(text)
        print ("\n<---", Output)

    except IndexError:
            Unknown = []
            for i in ANfile:
                row = i.split(' @ ')

                if "Unknown" in i:
                    Unknown.append(row[1])


            Output = random.choice(Unknown)
            print ("\n<---", Output)
        

    if ToAnswser == "Exit":
        out = answer(0, Output)

        return out


    return Output


'''
Net search functions

The processing function of the search query in the search engines.

User input is supplied to the function input and unnecessary search words are removed from it. 
For example: Find music on YouTube - it will be just music


'''

def EditSearch(Input):


    global An
    
    for i in f:
        
        row = i.split(' @ ')
       
        

        if To == "Youtube" and "Youtube" in i:
            text.append(row[0])
            
            
        elif To == "Search" and "Search" in i:
            text.append(row[0])


        elif To == "Open" and "Open" in i:
            text.append(row[0])
           

    for item in text:
        if item in text and item in Input:              
            An = Input.replace(item, '')

            
    try:

        An = sub('[?!]', '', An)

        return An.lstrip().capitalize()

    except:

        return Input

        

        

    
def EditedOpen(search):
    with open('../DataBase/added_programms.json', 'r') as File:
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
            return Popen(Links[0])
        except FileNotFoundError:
            print(Parser("Wrong path"))
            return 1
    else:
        return 1