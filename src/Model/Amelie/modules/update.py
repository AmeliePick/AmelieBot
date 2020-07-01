# -*- coding: utf-8 -*-

''' Update module
Check the list of updated files on the server and download new files and replace it in the local directories.

'''

from re                 import sub
from os                 import remove
from os                 import path as os_path
from time               import sleep
from urllib.request     import urlopen

from .tools.sessionLog  import LogWrite
from .tools.configParser      import iniParser, SettingsControl, DisplayText



def checkUpdate() -> bool:
    '''
    Getting config file and check versions
    '''
    try:
        # get config file
        response = urlopen('http://ameliepick.ml/AmelieBot/update.ini')

        FileContent = response.read()

        if FileContent == "": return False
        else:
            with open ("TEMP/UpdateConfig.ini", 'wb') as file:
                file.write(FileContent)


        # Modify current settings file according to the update file
        NewVersion = iniParser.getConfig_(  "Settings", "ver", "TEMP/UpdateConfig.ini")
        if SettingsControl.getConfig("Settings", "ver") != NewVersion:
            SettingsControl.setConfig("Settings", "ver", NewVersion)
            return True

    except:
        LogWrite()
        print(DisplayText.print("service_error"))
        return False
    return


def download(response: bool) -> int:
    '''
    response - new version flag

    '''

    if response == True:
        # getting list of new files
        filesList = iniParser.getConfig_("Settings", "modules", "TEMP/UpdateConfig.ini").split();
        modules = []
        for line in filesList:
            modules.append(line)
            
        # download new files
        for module in modules:
            try:
                getFile = urlopen('http://ameliepick.ml/AmelieBot/'+module)
            except:
                LogWrite()
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

        if os_path.exists("TEMP/UpdateConfig.ini"):
            remove("TEMP/UpdateConfig.ini")

        if os_path.exists("TEMP/tmp_file.py"):
            remove("TEMP/tmp_file.py")
        sleep(1.5)
        return 0


    else:
        print(Parser("Nupdate"))
        return 1