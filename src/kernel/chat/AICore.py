# -*- coding: utf-8 -*-



from re             import sub

from numpy          import random, arange

from sklearn.externals                  import joblib
from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.linear_model               import SGDClassifier
from sklearn.pipeline                   import Pipeline

from random             import choice
from Stemmer            import Stemmer
from tools.system       import FileManager
from Singleton          import Singleton



class Chat(metaclass = Singleton):
    ''' The class is a Singleton.

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
    _text_clf: Pipeline

    _lang: str



    def __init__(self, appLanguage: str):
        def training(dataSet: dict, Val_split = 0.1) -> None:
            if not FileManager.fileExist("../DataBase/models/model.pkl"):
                FileManager.createFile("../DataBase/models/model.pkl")
            else:
                self._text_clf = joblib.load("../DataBase/models/model.pkl")


            # fit and train the model
            lenght = len(dataSet['text'])
            if lenght > 10:
                indexes = arange(lenght)
                random.shuffle(indexes)

                X = [dataSet['text'][i] for i in indexes]
                Y = [dataSet['tag'][i]  for i in indexes]

                nb_valid_samples = int(Val_split * lenght)


                trained = { 'train': { 'x': X[:-nb_valid_samples], 'y': Y[:-nb_valid_samples]  },
                            'test':  { 'x': X[-nb_valid_samples:], 'y': Y[-nb_valid_samples:]  }
                          }

                self._text_clf.fit(trained['train']['x'], trained['train']['y'])
                self._text_clf.predict(trained['test']['x'])

                # save the model to disk
                joblib.dump(self._text_clf, "../DataBase/models/model.pkl", compress = 3, protocol = 4)


            return



        def parseDataSet() -> dict:
            dataSet = {'text': [], 'tag':[]}
            for line in self._dataSet:
                if(line == '' or line == '\n' or line == ' '):
                    continue

                row = line.split(' @ ')


                dataSet['text'] += [row[0]]
                dataSet['tag'] += [row[1]]


            return dataSet



        super().__init__()

        self._lang = appLanguage

        self._dataSet = list()
        self._stopWords = list()
        self._answerText = list()
        self._getDataFromDB()
        self._text_clf = joblib.load("../DataBase/models/model.pkl")

        self._input = str()
        self._sessionInput = dict()


        #self._text_clf = Pipeline([ ('tfidf', TfidfVectorizer()), ('clf', SGDClassifier(loss='hinge')),])
        #training(parseDataSet())

        return



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

        return



    def stemming(self, expression: str) -> str:
        if self._lang == "ru":
            return Stemmer(self._lang.lower()).stemWord(expression)
        else:
            return expression



    def _getDataFromDB(self) -> None:
        ''' Check language choice and parse needed files.
        '''

        def readFileToList(listOBJ: list, file: str) -> None:
            file = FileManager.readFile(file)
            listOBJ.clear()
            for line in file:
                listOBJ.append(line.replace('\n', ''))
            return


        # Parse data set only once.
        if len(self._dataSet) == 0 and FileManager.fileExist("../DataBase/DataSet.db") == True:
            readFileToList(self._dataSet, "../DataBase/DataSet.db")

        readFileToList(self._stopWords, "../DataBase/stopWords" + self._lang.upper() + ".db")
        readFileToList(self._answerText, "../DataBase/answers" + self._lang.upper() + ".db")

        return



    def _inputAnalysis(self, input_: str) -> None:
        # if the input is garbage
        input_ = sub('[^\w, \s]', '', input_)
        if len(sub('[\t, \n, \r, \s]', '', input_)) <= 1 or sub('[\t, \n, \r, \s]', '', input_).isdigit() or len(input_) <= 1:
            self._input = ""
            self._inputType = "Unknown"
            return

        self._input = input_

        # predict the input type
        input = []
        input.append(self._input.capitalize())
        self._inputType = ''.join(self._text_clf.predict(input)).replace('\n', '')

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

        return ''.join(result).lstrip().rstrip()



    def _getAnswer(self) -> str:
        # add to the list all phrases with current input type
        answerPharse = []
        for line in self._answerText:
            row = line.split(" @ ")
            if row[0] == self._inputType:
                answerPharse.append(row[1])


        self.output = choice(answerPharse)

        # add phrases in data set
        #if self._inputType != "Unknown":
        #    FileManager.writeToFile(self._input + " @ " + self._inputType + '\n', "../DataBase/DataSet.db")

        return self.output
