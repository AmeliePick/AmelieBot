# -*- coding: utf-8 -*-

from Singleton             import Singleton

from Settings              import Settings

from chat.dialog           import Dialog
from chat.AICore           import Chat

from httpcore._exceptions import ConnectError

from tools.system          import FileManager
from tools.system          import Network
from tools.logger          import Logger
from tools.input           import voiceInput


from audio.processing      import playAudio, TextToSpeech
from audio.recognition     import SpeechRecognition

from webbrowser            import open as webbrowser_open
from subprocess            import Popen


from re import sub



class Amelie(metaclass = Singleton):
    ''' Bot's logic to get conversation with the user.

    This class is literally bot itself.

    The class is a Singleton.

    '''

    _logger: Logger



    _chat: Chat
    _dialog: Dialog
    _voiceRecorder: SpeechRecognition
    _textToSpeech: TextToSpeech
    _voice: bool

    _exceptionStack: list
    _exceptionStep: int
    _programsList:  list



    def __init__(self, applanguage: str):
        super().__init__()
        self._logger = Logger()

        self._voiceRecorder = None
        self._textToSpeech = None
        self.voice = False

        self._chat = Chat(applanguage)
        self._dialog = Dialog(applanguage)
        self._voice = False

        self._updateProgramList()

        self._exceptionStack = list()
        self._exceptionStep = 1

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



    def conversation(self, userInput = "") -> str:
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


        chatAnswer = str()



        try:
            self.update();

            if userInput == "":
                self._setVoice(True)
                try:
                    userInput = voiceInput();
                except ValueError:
                    userInput = ""

            chatAnswer = _startChat(userInput)



        except FileNotFoundError:
            if self._exceptionStep == 1 and userInput == 'Y' or userInput == 'y':
                self._exceptionStep = 2
                chatAnswer = self._dialog.getMessageFor("addProgName") + " " + self._dialog.getMessageFor("addProgPath")
                
            elif self._exceptionStep == 2:
                parsedInput = userInput.split(" = ")

                if self.getPathToProgram(sub('[\t, \n, \r, \s]', '', parsedInput[0])):
                    chatAnswer = self._dialog.getMessageFor("progNameExist")
                else:
                    self.addProgram(sub('[\t, \n, \r, \s]', '', parsedInput[0]), sub('[\t]', '', parsedInput[1]))
                    chatAnswer = self._dialog.getMessageFor("done")
                    self._exceptionStep = 1
                    self._exceptionStack.pop(0)

        except (ConnectionError, ConnectError):
            self._logger.writeLog()
            self._exceptionStack.pop(0)
            return self._dialog.getMessageFor("serviceError")

        except OSError as e:
            self._logger.writeLog()
            if e.errno == 6:
                return self._dialog.getMessageFor("errMicroDefine")
            elif e.errno == -9999:
                chatAnswer = self._dialog.getMessageFor("microAccesDenied").replace('\n', " or ") + self._dialog.getMessageFor("errMicroDefine")
            else:
                chatAnswer = self._dialog.getMessageFor("error")
            self._exceptionStack.pop(0)

        except Exception:
            self._logger.logWrite()
            self._exceptionStack.pop(0)
            return self._dialog.getMessageFor("error")

       

        if self._voice:
            try:
                self.tts(chatAnswer)
            except:
                self._logger.logWrite()
                self._voice = False
                return str(self._dialog.getMessageFor("serviceError") + ". " + chatAnswer)

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
            excpetion = self._exceptionStack[0]
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



    def getVoice(self) -> bool:
        return self._voice



    def _setVoice(self, value: bool) -> None:
        if(self._voice == value): return

        if value == True and Network.checkNetworkConnection():
            try:
                self._voiceRecorder = SpeechRecognition(self._chat.getLanguage())
                self._textToSpeech = TextToSpeech()
            except OSError as e:
                self._voiceRecorder = None
                e.errno = 6
                raise e

        elif value == True and not Network.checkNetworkConnection():
            raise ConnectionError()

        self._voice = value
        return



    def getUserInput(self) -> str:
        return self._chat.getInput()



    def __del__(self):
        pass
