# -*- coding: utf-8 -*-

from Singleton            import Singleton

from Settings              import Settings

from chat.dialog           import Dialog
from chat.AICore           import Chat

from tools.system          import FileManager
from tools.system          import Network


from audio.processing      import playAudio, TextToSpeech
from audio.recognition     import SpeechRecognition

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
    _voice: bool

    _exceptionStack: list
    _programsList:  list



    def __init__(self, applanguage: str):
        super().__init__()
        self._exceptionStack = list()

        self._voiceRecorder = None
        self._textToSpeech = None
        self.voice = False

        self._chat = Chat(applanguage)
        self._dialog = Dialog(applanguage)
        self._voice = False

        self._updateProgramList()

        return



    def _doAction(self, inputType: str) -> None:
        ''' Do action based on user's request.

        This method must calling in a try block, because the bot can generate exceptions.

        '''

        if self._chat.getInputType() == "Exit":
            self._exceptionStack.append(SystemExit(0))

        elif self._chat.getInputType() == "Search":
            url = "https://www.google.ru/search?q="
            webbrowser_open( url + str(self._chat.stemming(self._chat.editInput())), new = 1)

        elif self._chat.getInputType() == "Youtube":
            url = "http://www.youtube.com/results?search_query="
            webbrowser_open( url + str(self._chat.stemming(self._chat.editInput())), new = 1)

        # In this block can be an exception
        elif self._chat.getInputType() == "Open":
                Popen( self.getPathToProgram(self._chat.editInput()) )

        return



    def changeLanguage(self, language: str) -> None:
        self._voiceRecorder = SpeechRecognition(language)
        self._chat.changeLanguage(language)
        self._dialog.changeLanguage(language)

        return



    def conversation(self, userInput) -> str:
        ''' Start the conversation with the bot by current input mode.
        '''

        def _startChat(userInput: str) -> str:
            chatAnswer = self._chat.launch(userInput)

            try:
                self._doAction(self._chat.getInputType())
            except (FileNotFoundError, OSError):
                self._exceptionStack.append(FileNotFoundError())
                return str(self._dialog.getMessageFor("progNotFound") +
                       " " +
                       self._dialog.getMessageFor("addProg")).replace('\n', '')

            return chatAnswer


        chatAnswer = _startChat(userInput)

        if self._voice:
            try:
                self.tts(chatAnswer)
            except:
                self._exceptionStack.append(ConnectionError())
                self._voice = False

        return chatAnswer



    def tts(self, pharse: str) -> Exception:
        ''' Convert Text To Speech and play it.
        '''

        self._textToSpeech(pharse, self._chat.getLanguage())
        playAudio("TEMP/sound.wav")

        return



    def update(self) -> Exception:
        ''' Update the bot's logic.
        '''

        if len(self._exceptionStack) > 0:
            excpetion = self._exceptionStack.pop(0)
            raise excpetion

        return



    def _updateProgramList(self) -> None:
        programsFile = FileManager.readFile("../DataBase/addedProgramms.db")
        self._programsList = { row.split(" = ")[0].lower(): row.split(" = ")[1].replace('\n', '') for row in programsFile }

        return



    def getPathToProgram(self, programName: str) -> str:
        path = self._programsList.get(programName.lower())
        if path == None:
            return ''
        else:
            return path



    def addProgram(self, program: str, path: str) -> None:
        FileManager.writeToFile(program + " = " + path + '\n', "../DataBase/addedProgramms.db")
        self._updateProgramList()

        return



    @property
    def voice(self) -> bool:
        return self._voice



    @voice.setter
    def voice(self, value: bool) -> None:
        if value == True and Network.checkNetworkConnection():
            try:
                self._voiceRecorder = SpeechRecognition(self._chat.getLanguage())
                self._textToSpeech = TextToSpeech()
            except OSError as e:
                self._voiceRecorder = None
                e.errno = 6
                self._exceptionStack.append(e)

                return


        elif value == True and not Network.checkNetworkConnection():
            self._exceptionStack.append(ConnectionError())
            return

        self._voice = value
        return



    def getUserInput(self) -> str:
        return self._chat.getInput()



    def __del__(self):
        pass
