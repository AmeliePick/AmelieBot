# -*- coding: utf-8 -*-
from urllib.request import urlopen
from configParser import Config
from re import sub


def checkUpdate():

    response = urlopen('http://ameliepick.ml/update.ini')
    with open ("t.ini", 'wb') as tmp:
        tmp.write(response.read())
     

def download(response):

        if(Config('t.ini', "update") == Config("../update.ini", "update")):
            return 0

        else:
            return 1;