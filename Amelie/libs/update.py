# -*- coding: utf-8 -*-

''' Update module
Check the list of updated files on the server and download new files and replace it in the local directories.

'''


from urllib.request import urlopen
from .configParser import SettingsControl
from re import sub
from time import sleep


def checkUpdate() -> bool:
    '''
    Getting config file and check versions
    '''
    try:
        # get config file
        response = urlopen('http://ameliepick.ml/AmelieBot/update.ini')
        with open ("TEMP/UpdateConfig.ini", 'wb') as tmp:
            tmp.write(response.read())

        # if a new version is it, change version in this config file
        if(SettingsControl.getConfig('TEMP/UpdateConfig.ini', "ver") != SettingsControl.getConfig("settings.ini", "ver")):
            SettingsControl.setConfig("settings.ini", "ver", SettingsControl.getConfig('TEMP/UpdateConfig.ini', "ver"))
            return True

    except:
        print(DisplayText.print("service_error"))
        return False
    return


def download(response: bool) -> int:
    '''
    response - new version flag
    '''
    if response == True:
        # getting list of new files
        filesList = SettingsControl.getConfig('TEMP/UpdateConfig.ini', "modules").split();
        modules = []
        for i in filesList:
            modules.append(i)
            
        # download new files
        for module in modules:
            try:
                getFile = urlopen('http://ameliepick.ml/AmelieBot/'+module)
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
        remove("TEMP/tmp_file.py")
        sleep(1.5)
        return 0


    else:
        print(Parser("Nupdate"))
        return 1