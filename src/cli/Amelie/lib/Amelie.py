# -*- coding: utf-8 -*-


from .Settings              import Settings

from .chat.dialog           import Dialog
from .chat.AICore           import Chat

from .tools.system          import FileManager

from .audio.processing      import playAudio, TextToSpeech
from .audio.recognition     import SpeechRecognition

from webbrowser         import open as webbrowser_open
from subprocess         import Popen



class Amelie():
    ''' Bot's logic to get conversation with the user.

    This class is literally bot itself.
    
    '''



    _chat: Chat
    _dialog: Dialog
    _voiceRecorder: SpeechRecognition
    _textToSpeech: TextToSpeech
    


    def __init__(self, applanguage: str):
        super().__init__()

        self._voiceRecorder = SpeechRecognition(applanguage)
        self._textToSpeech = TextToSpeech()
        self._chat = Chat(applanguage)
        self._dialog = Dialog(applanguage)

        return



    def __new__(cls, applanguage: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Amelie, cls).__new__(cls)
            return cls.instance
            
        return cls.instance



    def changeLanguage(self, language: str) -> None:
        self._voiceRecorder = SpeechRecognition(language)
        self._chat.changeLanguage(language)
        self._dialog.changeLanguage(language)

        return



    def doAction(self, inputType: str) -> None:
        ''' Do action based on user's request.

        This method must calling in a try block, because the bot can generate exceptions.
        '''

        def getProgrammPath(name: str) -> str:
                ''' Get the path to the executable file

                '''
                
                file = FileManager.readFile("../../DataBase/added_programms.json")             
                for line in file:
                    row = line.split(" = ")
                    
                    if row[0].lower() in name.lower():
                        return row[1].replace('\n', '')
    
                return ''



        if self._chat.getInputType() == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(self._chat.EditInput()), new = 1)
    
        elif self._chat.getInputType() == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(self._chat.stemming(self._chat.EditInput())), new = 1)
        
        # In this block can be an exception
        elif self._chat.getInputType() == "Open":
                Popen( getProgrammPath( self._chat.EditInput() ) )

        return



    def chat(self, userInput: str) -> str:
        ''' The usual chat To get bot's answer user must type a request in a keyborad.
        '''

        chatAnswer = self._chat.launch(userInput)

        try:
            self.doAction(self._chat.getInputType())
        except (FileNotFoundError, OSError):
            return self._dialog.getMessageFor("Prog_not_found")
 
        return chatAnswer



    def voiceChat(self) -> str:
        ''' The voice chat. To get bot's answer user must use a microphone. 
        '''

        playAudio("../../Res/Sounds/readytohear.wav")

        userInput = str()

        try:
            self.recorderCalibration()
            userInput = self._voiceRecorder.recognize()

            chatAnswer = self.chat(userInput)

            self._textToSpeech(chatAnswer, self._chat.getLanguage())
            playAudio("TEMP/sound.wav")

            return chatAnswer

        except OSError:
            self._logger.logWrite()
            return self_dialog.getMessageBy("microAccesDenied")
                
        return
    


    def update(self):
        ''' Update the bot's logic.
        '''

        if self._chat.getInputType() == "Exit":
            raise SystemExit(0)



        return



    def getUserInput(self) -> str:
        return self._chat.getInput()



    def __del__(self):
        pass
