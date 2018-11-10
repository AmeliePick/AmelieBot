# -*- coding: utf-8 -*-
import sys, random, pickle, re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import model_selection



def AI():
    Edit = {'text': [], 'tag':[]}
    for line in open ("../DataBase/social.txt", "r"):
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
    filename = 'model.sav'
    pickle.dump(nb_valid_samples, open("models/model.sav", 'wb'))
    
    #load the model from disk
    loaded_model = pickle.load(open("models/model.sav", 'rb'))
  

    return { 
        'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
        'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
    }

def open_AI():
    data = AI()
    D = training(data)
    text_clf = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                    ('clf', SGDClassifier(loss='hinge')),
                    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict( D['test']['x'] )

    
    
    
    #Input
    Chat_Input = input('---> ').capitalize()

    #give a type of input
    mass = []
    mass.append(Chat_Input)
    pred = text_clf.predict(mass)
    ToAnswser = ''.join(pred).replace('\n', '')
    


        #--- Answer ---

    tag = []
    text = []
    
    for line in open ("../DataBase/answers.txt", "r"):
        row = line.split(' @ ')
        tag.append(row[0])
        #text.append(row[1])

        if ToAnswser in line:
            text.append(row[1])
            Output = random.choice(text)
    
    print("\n<--- ", Output)

    return Output