# -*- coding: utf-8 -*-

'''
Chat is a neural network that classifies requests from the user. 
Then, after processing the type of the question, it passes it to the answer function, 
where the answer is processed and the operations are performed according to the input.

User input is also processed for search engines. Unnecessary part of the phrase is cut off and search is performed only within the meaning of the sentence.

'''

from numpy          import random, arange
from pickle         import dump, load

from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.linear_model               import SGDClassifier
from sklearn.pipeline                   import Pipeline


from random         import choice
from webbrowser     import open as webbrowser_open
from subprocess     import Popen

from .stemming          import stemming



class Chat:
    # Storage for DB lines of stop words 
    clearSearch = list()

    # Storage for DB lines
    dataSet = list()

    # Storage for DB answer lines
    answerText = list()

    # Storages current language choice
    checkLang = ""


    input_ = str()
    output = str()
    inputType_ = str()
    sessionInput_ = dict()
    

    text_clf = None

    StateCode = 1   # 0 means to exit from app.
                    # 1 means to continue work.



    def __init__(self):
        super().__init__()


        
        def parseDataSet() -> dict:

            Edit = {'text': [], 'tag':[]}
            for line in self.dataSet:
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
            filename = 'modelEN.sav'
            if self.checkLang == "RU":
                filename = 'model.sav'
            dump(nb_valid_samples, open("models/"+filename, 'wb'))
    
            #load the model from disk
            loaded_model = load(open("models/"+filename, 'rb'))
  

            return { 
                'train': { 'x': X[:-loaded_model], 'y': Y[:-loaded_model]  },
                'test': { 'x': X[-loaded_model:], 'y': Y[-loaded_model:]  }
            }



        self.LangChoice()


        # Do train n-network
        data = parseDataSet()
        trained = training(data)
        self.text_clf = Pipeline([
                        ('tfidf', TfidfVectorizer()),
                        ('clf', SGDClassifier(loss='hinge')),
                        ])
        self.text_clf.fit(trained['train']['x'], trained['train']['y'])
        self.text_clf.predict( trained['test']['x'] )



        



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Chat, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def Enter(self, input_: str = "") -> None:
        ''' Get the user input(text/voice)

        '''


        while(True):
            if(input_ == ""):
                self.input_ = str(input('\n---> '))
                if self.input_ == '' or self.input_ == '\n' or self.input_ == ' ':
                    continue
                else:
                    break
            else:
                self.input_ = input_
                break



    def getAnswer(self) -> str:
        #TODO: refactor this

        def getProgrammPath(search: str) -> str:
            ''' Get the path to the executable file

            '''


            Name: str
            Link: str

            with open('../DataBase/added_programms.json', 'r') as File:
                for line in File:
            
                    row = line.split(' = ')

                    if search in line:
                        Link = str(row[1])
                        Name = str(row[0])
               
                        if search == Name:
                            return Link.replace('\n', '')
    
            raise FileNotFoundError



        def EditInput(input: str) -> str:
            ''' Removes from the user input the stop words.

            Example:
                    Input: open Google, find summer wallpapers
                    Result: Google, summer wallpapers
            '''


            from re import sub

            global clearSearch

            stopPhrase = ''
            for row in clearSearch:
                if ((input.capitalize()).find(row.capitalize()) != -1):
                    stopPhrase = row.replace('\n', '')
                    break


            if stopPhrase == '':
                return input
            else:
                result = list(input)
                for i in range(input.capitalize().find(row.capitalize()), len(stopPhrase)):
                               result[i] = ''

        
        
                return sub('[?!]', '', ''.join(result))
        


        url = ""

  
        if self.inputType_ == "Exit":
            self.StateCode = 0

        elif self.inputType_ == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(EditInput(self.input_)), new=1)
    
        elif self.inputType_ == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(stemming(EditInput(self.input_))), new=1)
        
        # here we can get an empty answer, when the user says a phrase like "open" and nothing more
        elif self.inputType_ == "Open" and EditInput(self.input_) != '':
                try:
                    Popen( getProgrammPath( EditInput(self.input_) ) )
            
                except FileNotFoundError:
                        from .exceptions_chat import programmNotFound
                    
                        while(True):
                            try:
                                if programmNotFound() != 0:
                                    Popen( getProgrammPath( EditInput(self.input_) ) )
                                    break

                                else:
                                    #change input type
                                    break

                            except FileNotFoundError:
                                continue


                except OSError as os:
                    if(os.winerror == 87):
                        self.inputType_ = "Unknown"


        # get answer
        try:
                answerPharse = []
                for line in self.answerText:
                    row = line.split(" @ ")

                    if row[0] == self.inputType_:
                        answerPharse.append(row[1])

                self.output = choice(answerPharse)
                print ("\n<---", self.output)

                # add phrases in DB
                self.selfLearning(self.input_ + " @ " + self.inputType_)
                

        except IndexError:
                    Unknown = []

                    for i in self.answerText:
                        row = i.split(" @ ")

                        if row[0] == "Unknown":
                            Unknown.append(row[1])

                    self.output = choice(Unknown)
        

        return self.output



    def selfLearning(self, text: str) -> None:
        ''' Word processing and write down to DB's file

        '''

        global checkLang


        if self.checkLang == "RU":
            with open("../DataBase/DataSet_RU.json", "a", encoding="utf8") as train:
                train.write(text)

        elif self.checkLang == "EN":
            with open("../DataBase/DataSet_EN.json", "a") as train:
                train.write(text)

        return



    def LangChoice(self) -> None:
        ''' Check language choice and parse needed files.

        '''


        from modules.configParser import SettingsControl

        self.checkLang = SettingsControl.getConfig("Settings", "lang")

        postfix = "EN.json"
        if self.checkLang == "RU":
            postfix = "RU.json"


        with open("../DataBase/DataSet_"+postfix, "r", encoding="utf8") as file:
            for line in file:
                self.dataSet.append(line.replace('\n', ''))

    
        with open ("../DataBase/ClearSearch"+postfix, "r") as file:
            for line in file:
                self.clearSearch.append(line.replace('\n', ''))
        

        with open ("../DataBase/answers"+postfix, "r") as file:
            for line in file:
                self.answerText.append(line.replace('\n', ''))


        return



    def inputAnalysis(self) -> None:
        # give a type of input
        input = []
        input.append(self.input_.capitalize())


        try:
            pred = self.text_clf.predict(input)
        except:
            return "Pause"
        
        self.inputType_ = ''.join(pred).replace('\n', '')

        self.sessionInput_[self.input_] = self.inputType_

    

    def launch(self, input_ = "") -> str:
        self.Enter(input_)
        self.inputAnalysis()
        return self.getAnswer()






    def getInput(self) -> str:
        return self.input_



    def getInputType(self) -> str:
        return self.inputType_



    def getSessionInput(self) -> dict:
        return self.sessionInput_


    def getCode(self) -> int:
        return self.StateCode
