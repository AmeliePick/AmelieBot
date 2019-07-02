# -*- coding: utf-8 -*-

'''
Chat is a neural network that classifies requests from the user. 
Then, after processing the type of the question, it passes it to the answer function, 
where the answer is processed and the operations are performed according to the input.

User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

'''

from webbrowser     import open as webbrowser_open
from os             import _exit
from subprocess     import Popen
from time           import sleep

from random         import choice
from numpy          import random, arange
from pickle         import dump, load

from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.linear_model               import SGDClassifier
from sklearn.pipeline                   import Pipeline
from sklearn                            import model_selection

from libs.AIChatKit     import dataSet, ANfile, checkLang
from libs.AIChatKit     import getProgrammPath, EditSearch, selfLearning
from libs.configParser  import SettingsControl
from libs.Stem_Res      import Stemm
from .request_obj       import Output
from libs.time          import stopWatch
from libs.logger        import sessionLogger



'''

Functions for creating and training the neural network to recognize the type of input. 
For example: What is the weather today? - Weather. Where is Paris? - Location

'''
def AI():
    global dataSet

    Edit = {'text': [], 'tag':[]}
    for line in dataSet:
        row = line.split(' @ ')
        
        Edit['text'] += [row[0]]
        Edit['tag'] += [row[1]]
    
        
    return Edit


def training(Edit, Val_split = 0.1):
    global checkLang

    lenght = len(Edit['text'])
    
    indexes = arange(lenght)

    random.shuffle(indexes)

    X = [Edit['text'][i]
    for i in indexes ]
    Y = [Edit['tag'][i]
    for i in indexes]

    nb_valid_samples = int(Val_split * lenght)


    #save the model to disk
    filename = 'modelEN.sav'
    if checkLang == "RU":
        filename = 'model.sav'


    dump(nb_valid_samples, open("models/"+filename, 'wb'))
    
    #load the model from disk
    loaded_model = load(open("models/"+filename, 'rb'))
  

    return { 
        'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
        'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
    }


def Enter():
    global stopWatch
    global sessionLogger

    while(True):
        try:
            if(stopWatch):
                sessionLogger.SessionCollector( "Chat Duration(sec)", str(stopWatch.stop()) )
                del(sessionLogger)
                stopWatch = None

            Input = str(input('\n---> ').capitalize())
            
            if Input == '' or Input == '\n':
                raise KeyboardInterrupt

        except KeyboardInterrupt:
            print("\n\n<--- " + SettingsControl.Print("WrongInput"))
            continue
            

        global Chat_Input
        Chat_Input = Input

        return Input


dataSet_tmp = {}
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
        
    ToAnswer = ''.join(pred).replace('\n', '')

    global dataSet_tmp
    dataSet_tmp[Chat_Input] = ToAnswer

    return ToAnswer


'''
Functions for processing user input based on request type, self-learning
For example: Hi Amelie - Hello. How are you? - I'm fine, and you?
'''



def Answer(ToAnswer):
    global Chat_Input
    global dataSet_tmp
    
    tag = []
    text = []
    url = ""

  
    if ToAnswer == "Exit":
        Output.setNum(0)

    elif ToAnswer == "Search":
        url = "https://www.google.ru/search?q="
        webbrowser_open( url + str(EditSearch(Chat_Input, ToAnswer)), new=1)
    
    elif ToAnswer == "Youtube":
        url = "http://www.youtube.com/results?search_query="
        webbrowser_open( url + str(Stemm(EditSearch(Chat_Input, ToAnswer))), new=1)
        
    # here we can get an empty answer, when the user says a phrase like "open" and nothing more
    elif ToAnswer == "Open" and EditSearch(Chat_Input,  ToAnswer) != '':
        try:
            Popen( getProgrammPath( EditSearch(Chat_Input, ToAnswer ) ) )
            
        except FileNotFoundError:
            if EditedOpen(EditSearch(Chat_Input)) == 1:
                from modules.exceptions_chat import programmNotFound

                programmNotFound()
                getProgrammPath(EditSearch(Chat_Input, ToAnswer))

        except OSError as os:
            if(os.winerror == 87):
                ToAnswer = "Unknown"


    # --- Get answer ---
    for line in ANfile:
        row = line.split(' @ ')
        tag.append(row[0])

        if ToAnswer in line:
            text.append(row[1])

    try:
        Output.setText(choice(text))
        print ("\n<---", Output.getOut())

        # add phrases in DB
        if Output.getNum() == 0 :
            selfLearning(dataSet_tmp)
            dataSet_tmp.clear()

    except IndexError:
            Unknown = []

            for i in ANfile:
                row = i.split(' @ ')

                if "Unknown" in i:
                    Unknown.append(row[1])

            Output.setText(choice(Unknown))
            print ("\n<---", Output.getOut())
        

    return Output


