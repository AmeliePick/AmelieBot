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
from webbrowser         import open as webbrowser_open
from subprocess         import Popen
from ..tools.system     import FileManager



class Chat(object):
    '''
    Chat is a neural network that classifies requests from the user. 
    Then, after processing the type of the question, it passes it to the answer function, 
    where the answer is processed and the operations are performed according to the input.

    User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

    '''



    # DataBase info
    _dataSet:    list
    _stopWords:  list
    _answerText: list

    # App setup's info
    

    # Chat
    _input: str
    _output: str
    _inputType: str
    _sessionInput: dict
    
    _lang: str
    _text_clf: Pipeline
    _stateCode: int  # 0 means to exit from app.
                    # 1 means to continue work.



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
            dump(nb_valid_samples, open("../../models/model"+ self._lang + ".sav", 'wb'))
    
            #load the model from disk
            loaded_model = load(open("../../models/model"+ self._lang + ".sav", 'rb'))
  

            return { 
                'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
                'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
            }



        self._lang = appLanguage

        self._dataSet = list()
        self._stopWords = list()
        self._answerText = list()
        self.getDataFromDB()


        self._input = str()
        self._sessionInput = dict()

        self._stateCode = int(1)

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



    def getAnswer(self) -> str:
        def EditInput(input: str) -> str:
            ''' Removes from the user input the stop words.

            Example:
                    Input: open Google, find summer wallpapers
                    Result: Google, summer wallpapers
            '''


            from re import sub

            stopPhrase = ''
            for row in self._stopWords:
                if ((input.capitalize()).find(row.capitalize()) != -1):
                    stopPhrase = row.replace('\n', '')
                    break


            if stopPhrase == '':
                return input
            else:
                result = list(input)
                for i in range(input.capitalize().find(row.capitalize()), len(stopPhrase)):
                               result[i] = ''

        
        
                return sub('[?!]', '', ''.join(result)).lstrip()
        


        def getProgrammPath(self, name: str) -> str:
                ''' Get the path to the executable file

                '''

                
                file = FileManager.readFile("../DataBase/added_programms.json")             
                for line in file:
                    row = line.split(" = ")
                    
                    if row[0].lower() in name.lower():
                        return row[1].replace('\n', '')
    
                return ''



        url = str()

  
        if self._inputType == "Exit":
            self._stateCode = 0

        elif self._inputType == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(EditInput(self._input)), new=1)
    
        elif self._inputType == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(self.stemming(EditInput(self._input))), new=1)
        
        # here we can get an empty answer, when the user says a phrase like "open" and nothing more
        elif self._inputType == "Open" and EditInput(self._input) != '':
                try:
                    Popen( getProgrammPath( EditInput(self._input) ) )
            
                except FileNotFoundError:
                        pass


                except OSError as os:
                    if(os.winerror == 87):
                        self._inputType = "Unknown"


        # get answer
        try:
            answerPharse = []
            for line in self._answerText:
                row = line.split(" @ ")

                if row[0] == self._inputType:
                    answerPharse.append(row[1])

            self.output = choice(answerPharse)

            # add phrases in DB
            FileManager.writeToFile(self._input + " @ " + self._inputType + '\n', "../../DataBase/DataSet" + self._lang + ".json")
                

        except IndexError:
            Unknown = []

            for i in self._answerText:
                row = i.split(" @ ")

                if row[0] == "Unknown":
                    Unknown.append(row[1])

            self.output = choice(Unknown)
        

        return self.output



    def getDataFromDB(self) -> None:
        ''' Check language choice and parse needed files.

        '''


        def readFileToList(listOBJ: list, file: str) -> None:
            file = FileManager.readFile(file)
            for line in file:
                listOBJ.append(line.replace('\n', ''))


        readFileToList(self._dataSet, "../../DataBase/DataSet" + self._lang + ".json")
        readFileToList(self._stopWords, "../../DataBase/stopWords" + self._lang + ".json")
        readFileToList(self._answerText, "../../DataBase/answers" + self._lang + ".json")


        return



    def inputAnalysis(self, input_: str) -> None:
        # if the input is garbage
        if re_findall('\t, \n, \r, \s, w', input_) and len(input_) <= 3:
            self._inputType = "Unknown"
            return
        
        self._input = input_
        input = []
        input.append(self._input.capitalize())


        predicted = self._text_clf.predict(input)
        
        self._inputType = ''.join(predicted).replace('\n', '')
        self._sessionInput[self._input] = self._inputType


        return



    def launch(self, input_ = "") -> str:
        self.inputAnalysis(input_)
        return self.getAnswer()



    def stemming(self, expression: str) -> str:
        return Stemmer(self._lang.lower()).stemWord(expression)



    def getInput(self) -> str:
        return self._input



    def getInputType(self) -> str:
        return self._inputType



    def getSessionInput(self) -> dict:
        return self.sessionInput_


    def getStateCode(self) -> int:
        return self._stateCode


    def getLanguage(self) -> str:
        return self._lang