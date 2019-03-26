# -*- coding: utf-8 -*-
from urllib.request import urlopen
from .configParser import Config, Parser
from re import sub


def checkUpdate():
    try:
        response = urlopen('http://ameliepick.ml/update.ini')
        with open ("t.ini", 'wb') as tmp:
            tmp.write(response.read())
    except:
        return Parser("service_error")
     

def download(response):
        if(Config('t.ini', "update") == Config("update.ini", "update")):
            R = Config('t.ini', "modules").split();
            getModules = []
            for i in R:
                getModules.append(i)
            

            prefix = "modules/"
            for i in getModules:
                getFile = urlopen('http://ameliepick.ml/modules/'+i)

                with open('tmp_file.py', 'wb') as tmp:
                    tmp.write(getFile.read())

                with open(prefix+i, 'w') as mergeFile:
                    with open('tmp_file.py', 'r') as tmp2:
                        mergeFile.write(tmp2.read())

            return Parser("Yupdate")

        else:
            return Parser("Nupdate")