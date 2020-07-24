# -*- coding: utf-8 -*-



from numpy          import random, arange
from pickle         import dump, load
from re             import sub
from re             import findall as re_findall

from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.linear_model               import SGDClassifier
from sklearn.pipeline                   import Pipeline

from random             import choice
from Stemmer            import Stemmer
from ..tools.system     import FileManager



class Chat(object):
    '''
    Chat is a neural network that classifies requests from the user. 
    Then, after processing the type of the question, it passes it to the answer function, 
    where the answer is processed by searhing of phrases like the input type.

    User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

    '''



    # DataBase info
    _dataSet:    list
    _stopWords:  list
    _answerText: list

    # Chat
    _input: str
    _output: str
    _inputType: str
    _sessionInput: dict
    
    _lang: str
    _text_clf: Pipeline



    def __init__(self, appLanguage: str):
        super().__init__()


        
        def parseDataSet() -> dict:
            Edit = {'text': [], 'tag':[]}
            for line in self._dataSet:
                if(line == '' or line == '\n' or line == ' '):
                    continue

                row = line.split(' @ ')
            
            
                Edit['text'] += [row[0]]
                Edit['tag'] += [row[1]]
    
        
            return Edit



        def training(Edit, Val_split = 0.1) -> dict:
            lenght = len(Edit['text'])
            indexes = arange(lenght)
            random.shuffle(indexes)

            X = [Edit['text'][i] for i in indexes]
            Y = [Edit['tag'][i]  for i in indexes]

            nb_valid_samples = int(Val_split * lenght)


            #save the model to disk
            dump(nb_valid_samples, open("../../models/model.sav", 'wb'))
    
            #load the model from disk
            loaded_model = load(open("../../models/model.sav", 'rb'))
  

            return { 
                'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
                'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
            }



        self._lang = appLanguage

        self._dataSet = list()
        self._stopWords = list()
        self._answerText = list()
        self._getDataFromDB()


        self._input = str()
        self._sessionInput = dict()

        # Do train n-network
        data = parseDataSet()
        trained = training(data)
        self._text_clf = Pipeline([
                        ('tfidf', TfidfVectorizer()),
                        ('clf', SGDClassifier(loss='hinge')),
                        ])
        self._text_clf.fit(trained['train']['x'], trained['train']['y'])
        self._text_clf.predict( trained['test']['x'] )



    def __new__(cls, appLanguage: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Chat, cls).__new__(Chat)
            return cls.instance
            
        return cls.instance



    def getInput(self) -> str:
        return self._input



    def getInputType(self) -> str:
        return self._inputType



    def getSessionInput(self) -> dict:
        return self.sessionInput_
    


    def getLanguage(self) -> str:
        return self._lang



    def launch(self, input_ = "") -> str:
        ''' Start the chat and get the answer based on user's input.
        '''

        self._inputAnalysis(input_)
        return self._getAnswer()



    def changeLanguage(self, language: str) -> None:
        self._lang = language
        self._getDataFromDB()



    def _stemming(self, expression: str) -> str:
        if self._lang == "ru":
            return Stemmer(self._lang.lower()).stemWord(expression)
        else:
            return expression



    def _getDataFromDB(self) -> None:
        ''' Check language choice and parse needed files.

        '''


        def readFileToList(listOBJ: list, file: str) -> None:
            file = FileManager.readFile(file)
            for line in file:
                listOBJ.append(line.replace('\n', ''))


        if len(self._dataSet) == 0:
            readFileToList(self._dataSet, "../../DataBase/DataSet.db")

        readFileToList(self._stopWords, "../../DataBase/stopWords" + self._lang.upper() + ".json")
        readFileToList(self._answerText, "../../DataBase/answers" + self._lang.upper() + ".json")


        return



    def _inputAnalysis(self, input_: str) -> None:
        # if the input is garbage
        input_ = sub('[^\w, \s]', '', input_)
        if len(sub('[\t, \n, \r, \s]', '', input_)) <= 1 or sub('[\t, \n, \r, \s]', '', input_).isdigit() or len(input_) <= 1:
            self._inputType = "Unknown"
            return
        
        self._input = input_
        input = []
        input.append(self._input.capitalize())


        predicted = self._text_clf.predict(input)
        
        self._inputType = ''.join(predicted).replace('\n', '')
        self._sessionInput[self._input] = self._inputType


        return



    def editInput(self, meaningLength = 2) -> str:
        ''' Removes from the user input the stop words.

        Example:
                Input: open Google, find summer wallpapers
                Result: Google, summer wallpapers
        '''



        ''' 
        This method can incorrectly edit the input, because the meaning of the sentcene doesn't detecting.
        The lenght of meaning worlds detecting only manualy by meaningLength value.

        Incorrectly behaivour:
        meaningLength: 2
        input: find youtube website.
        output: website
        '''



        result = list(self._input)
  
        for stopWord in self._stopWords:
            occurrence = (''.join(result).lower()).find(stopWord.lower())
            if occurrence != -1 and len(''.join(result).split()) >= meaningLength:

                # remove stop words from the input
                for index in range(occurrence, occurrence + len(stopWord)):
                    result[index] = ''

                result = list(''.join(result))

                

        return sub('[?, !]', '', ''.join(result)).lstrip().rstrip()



    def _getAnswer(self) -> str:
        url = str()

        # get answer

        answerPharse = []
        for line in self._answerText:
            row = line.split(" @ ")
            if row[0] == self._inputType:
                answerPharse.append(row[1])



        # TODO: This case would be, because the data set has wrong records. Remove this code atfer the fix of data set.
        try:
            self.output = choice(answerPharse)
        except IndexError:
            Unknown = []
            self._inputTyoe = "Unknown"

            for i in self._answerText:
                row = i.split(" @ ")

                if row[0] == "Unknown":
                    Unknown.append(row[1])

            self.output = choice(Unknown)



        # add phrases in DB
        if self._inputType != "Unknown":
            FileManager.writeToFile(self._input + " @ " + self._inputType + '\n', "../../DataBase/DataSet" + self._lang.upper() + ".json")
                
        

        return self.output
