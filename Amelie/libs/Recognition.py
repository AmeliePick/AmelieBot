import time, os
import speech_recognition as sr

'''
Regonizer module

Listens to speech, converts to text and sends it to the chat module for processing.

'''


def REG():

    # Microphone and Recognition
    r = sr.Recognizer()
    micro = sr.Microphone()


    #Noise calibration

    print("Пару секунд тишины...")
    with micro as source:
        r.adjust_for_ambient_noise(source)

    #Listening to the microphone

    with micro as source:
        print("Скажите что-нибудь\n")
        audio = r.listen(source)

        #Speech to text recording
    try:
        
        Chat_Input = r.recognize_google(audio, language="ru_RU")
        print("---> ", Chat_Input)
        
        return Chat_Input

    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
        os.system("pause")

    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
