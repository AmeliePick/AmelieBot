# -*- coding: utf-8 -*-
from urllib.request import urlopen
from .configParser import SettingsControl
from re import sub
from time import sleep


def checkUpdate():
    '''
    Getting config file and check versions
    '''
    try:
        # get config file
        response = urlopen('http://ameliepick.ml/AmelieBot/update.ini')
        with open ("TEMP/t.ini", 'wb') as tmp:
            tmp.write(response.read())

        # if a new version is it, change version in this config file
        if(SettingsControl.getConfig('TEMP/t.ini', "ver") != SettingsControl.getConfig("settings.ini", "ver")):
            SettingsControl.setConfig("settings.ini", "ver", SettingsControl.getConfig('TEMP/t.ini', "ver"))
            return True

    except:
        print(DisplayText.print("service_error"))
        return False
     

def download(response):
    '''
    response --- new version flag
    '''
    if response == True:
        # getting list of new files
        R = SettingsControl.getConfig('TEMP/t.ini', "modules").split();
        getModules = []
        for i in R:
            getModules.append(i)
            
        # download new files
        for file in getModules:
            try:
                getFile = urlopen('http://ameliepick.ml/AmelieBot/'+file)
            except:
                print(DisplayText.print("WrongPath"))
                return 1

            # paste from new file to temp file
            with open('TEMP/tmp_file.py', 'wb') as tmp:
                tmp.write(getFile.read())

            # rewrite local file
            with open(file, 'w') as mergeFile:
                with open('TEMP/tmp_file.py', 'r') as tmp2:
                    mergeFile.write(tmp2.read())

        
        print(DisplayText.print("Yupdate"))
        sleep(1.5)
        return 0


    else:
        print(Parser("Nupdate"))
        return 1