# -*- coding: utf-8 -*-

'''
Chat is a neural network that classifies requests from the user. 
Then, after processing the type of the question, it passes it to the answer function, 
where the answer is processed and the operations are performed according to the input.

User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

'''

from numpy          import random, arange #slow loading
from pickle         import dump, load

from sklearn.feature_extraction.text    import TfidfVectorizer #slow loading
from sklearn.linear_model               import SGDClassifier
from sklearn.pipeline                   import Pipeline

from libs.time          import stopWatch
from libs.logger        import sessionLogger
from .AIFiles           import dataSet, checkLang


class Chat:
    input:          str
    inputType:      str
    dataSet_new:    dict

    input = ""
    inputType = ""
    dataSet_new = {}

    def getInput(self) -> str:
        return self.input


    def getInputType(self) -> str:
        return self.inputType

    def getDataSet_new(self) -> dict:
        return self.dataSet_new


    '''
    Functions for creating and training the neural network to recognize the type of input. 
    For example: What is the weather today? - Weather. Where is Paris? - Location

    '''
    def AI(self):
        global dataSet

        Edit = {'text': [], 'tag':[]}
        for line in dataSet:
            row = line.split(' @ ')
        
            Edit['text'] += [row[0]]
            Edit['tag'] += [row[1]]
    
        
        return Edit


    def training(self, Edit, Val_split = 0.1):
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


    def Enter(self, voice: str = "") -> None:
        global stopWatch
        global sessionLogger

        while(True):
            if(stopWatch):
                sessionLogger.SessionCollector( "Chat Duration(sec)", str(stopWatch.stop()) )

                del(sessionLogger)
                stopWatch = None
            
            if(voice == ""):
                self.input = str(input('\n---> ').capitalize())
                if self.input == '' or self.input == '\n' or self.input == ' ':
                    continue
                else:
                    break
            else:
                self.input = voice
                break


    def open_AI(self) -> None:
        data = self.AI()
        D = self.training(data)
        text_clf = Pipeline([
                        ('tfidf', TfidfVectorizer()),
                        ('clf', SGDClassifier(loss='hinge')),
                        ])
        text_clf.fit(D['train']['x'], D['train']['y'])
        predicted = text_clf.predict( D['test']['x'] )

        #give a type of input
        mass = []
        mass.append(self.input)


        try:
            pred = text_clf.predict(mass)
        except:
            return "Pause"
        
        self.inputType = ''.join(pred).replace('\n', '')

        self.dataSet_new[self.input] = self.inputType

chatOBJ = Chat()
