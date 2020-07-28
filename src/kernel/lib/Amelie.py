# -*- coding: utf-8 -*-

from .Singleton            import Singleton

from .Settings              import Settings

from .chat.dialog           import Dialog
from .chat.AICore           import Chat

from .tools.system          import FileManager

from .audio.processing      import playAudio, TextToSpeech
from .audio.recognition     import SpeechRecognition

from webbrowser         import open as webbrowser_open
from subprocess         import Popen



class Amelie(metaclass = Singleton):
    ''' Bot's logic to get conversation with the user.

    This class is literally bot itself.

    The class is a Singleton.
    
    '''



    _chat: Chat
    _dialog: Dialog
    _voiceRecorder: SpeechRecognition
    _textToSpeech: TextToSpeech

    _exceptionList: list
    _voice: bool
    


    def __init__(self, applanguage: str, enableVoice = False):
        super().__init__()

        self._voiceRecorder = SpeechRecognition(applanguage)
        self._textToSpeech = TextToSpeech()
        self._chat = Chat(applanguage)
        self._dialog = Dialog(applanguage)

        self._exceptionList = list()
        self._voice = enableVoice

        return



    def _doAction(self, inputType: str) -> None:
        ''' Do action based on user's request.

        This method must calling in a try block, because the bot can generate exceptions.
        '''

        def getProgrammPath(name: str) -> str:
                ''' Get the path to the executable file

                '''
                
                file = FileManager.readFile("../DataBase/added_programms.json")             
                for line in file:
                    row = line.split(" = ")
                    
                    if row[0].lower() in name.lower():
                        return row[1].replace('\n', '')
    
                return ''

        if self._chat.getInputType() == "Exit":
            self._exceptionList.append(SystemExit(0))

        elif self._chat.getInputType() == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(self._chat.EditInput()), new = 1)
    
        elif self._chat.getInputType() == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(self._chat.stemming(self._chat.EditInput())), new = 1)
        
        # In this block can be an exception
        elif self._chat.getInputType() == "Open":
                Popen( getProgrammPath( self._chat.editInput() ) )

        return



    def changeLanguage(self, language: str) -> None:
        self._voiceRecorder = SpeechRecognition(language)
        self._chat.changeLanguage(language)
        self._dialog.changeLanguage(language)

        return


    @property
    def voice(self) -> None:
        return self._voice


    @voice.setter
    def voice(self, value: bool) -> bool:    
        self._voice = value
        return



    def conversation(self, userInput) -> str:
        def _silentChat(userInput: str) -> str:
            ''' The usual chat to get bot's answer, user must type a request in a keyborad.
            '''

            chatAnswer = self._chat.launch(userInput)

            try:
                self._doAction(self._chat.getInputType())
            except (FileNotFoundError, OSError):
                self._exceptionList.append(FileNotFoundError())
                return str(self._dialog.getMessageFor("progNotFound") +
                       " " +
                       self._dialog.getMessageFor("addProg")).replace('\n', '')
 
            return chatAnswer


        if self._voice:
            chatAnswer = _silentChat(userInput)
            self.tts(chatAnswer)

            return chatAnswer

        else:
            return _silentChat(userInput)



    def tts(self, pharse: str) -> str:
        self._textToSpeech(pharse, self._chat.getLanguage())
        playAudio("TEMP/sound.wav")

        return



    def update(self):
        ''' Update the bot's logic.
        '''

        if len(self._exceptionList) > 0:
            excpetion = self._exceptionList.pop()
            raise excpetion



        return



    def getUserInput(self) -> str:
        return self._chat.getInput()



    def __del__(self):
        pass
