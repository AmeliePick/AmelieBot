# -*- coding: utf-8 -*-

import sys, os, random, pickle, re, playsound
import numpy as np
import nltk.stem as stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from gtts import gTTS
#from Speak import speak

def speak():
    

    Old_name_mp3 = "old"

    #Sound device initialization
    #mixer.init()
    
    Send_in_Google = gTTS(text = str(Answer), lang = "ru")

        #take name of file
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    file = str(r2)+"sound"+str(r1) +".mp3"

        #get result from Google 
    Send_in_Google.save(file)
    
        
    #try:
        #play sound
    playsound.playsound(file)
        #mixer.music.play()
        #delete file from drive
    os.remove(file)

#open file
f = open ("../DataBase/social.txt", "r")
ReadFile = f.read()
ff = open ("../DataBase/answers.txt", "r")
ReadFFile = ff.read()

def EditTXT(TXT):
    TXT = TXT.lower()
    
    stemmer = Stemmer('russian')
    TXT = ' '.join(Stemmer.stemWords(TXT.split()))
    

    TXT = re.sub('\?', "", ReadFile )
    return TXT

def AI():
    data = {'text': [], 'tag':[]}
    for line in open("../DataBase/social.txt"):
        row = line.split('@')
        data['text'] += [row[0]]
        data['tag'] += [row[1]]
    return data

def training(data, Val_split = 0.1):
    lenght = len(data['text'])
    
    indexes = np.arange(lenght)

    np.random.shuffle(indexes)

    X = [data['text'][i]
    for i in indexes ]
    Y = [data['tag'][i]
    for i in indexes]

    nb_valid_samples = int(Val_split * lenght)

    return { 
        'train': { 'x': X[:-nb_valid_samples], 'y': Y[:-nb_valid_samples]  },
        'test': { 'x': X[-nb_valid_samples:], 'y': Y[-nb_valid_samples:]  }
    }

def open_AI():
    data = AI()
    D = training(data)
    text_clf = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                    ('clf', SGDClassifier(loss='hinge')),
                    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict( D['train']['x'] )


    Chat_Input = input("---> ")

    mass = []
    mass.append(Chat_Input)
    pred = text_clf.predict(mass)
    ToAnswser = ''.join(pred).replace(' ', '')

    return ToAnswser

AA = open_AI

#--- Revers AI ---
def inv_EditTXT(TXT):
    TXT = TXT.lower()
    
    stemmer = Stemmer('russian')
    TXT = ' '.join(Stemmer.stemWords(TXT.split()))
    

    TXT = re.sub('\?', "", ReadFFile )
    return TXT

def inv_AI():
    data = {'text': [], 'tag':[]}
    for line in open("../DataBase/answers.txt"):
        row = line.split('@')
        data['tag'] += [row[0]]
        data['text'] += [row[1]]
    return data

#Training Ai
def inv_training(data, Val_split = 0.1):
    lenght = len(data['tag'])
    
    indexes = np.arange(lenght)

    np.random.shuffle(indexes)

    X = [data['tag'][i]
    for i in indexes ]
    Y = [data['text'][i]
    for i in indexes]

    nb_valid_samples = int(Val_split * lenght)

    return { 
        'train': { 'x': X[:-nb_valid_samples], 'y': Y[:-nb_valid_samples]  },
        'test': { 'x': X[-nb_valid_samples:], 'y': Y[-nb_valid_samples:]  }
    }

def inv_open_AI():
    global Answer

    data = inv_AI()
    D = inv_training(data)
    text_clf = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                    ('clf', SGDClassifier(loss='hinge')),
                    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict( D['train']['x'] )


    Output = str(AA)
    
    mass = []
    mass.append(Output)
    EditAnswer = text_clf.predict(mass)
    Answer  = ''.join(EditAnswer)
    speak()
    print ('<---',Answer + '\n')

    return str(Answer)


    