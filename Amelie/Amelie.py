# -*- coding: utf-8 -*

from sys import stdin, exit as sys_exit
import os
import webbrowser
import subprocess
import random

print ( 100 * "_")
print ("                                                  _ _       ")
print ("                             /\                  | (_)      ")
print ("                            /  \   _ __ ___   ___| |_  ___  ")
print ("                           / /\ \ | '_ ` _ \ / _ \ | |/ _ \ ")
print ("                          / ____ \| | | | | |  __/ | |  __/ ")
print ("                         /_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 100 * "_")

#--- Бот ---

#--- Логин профиля ---
username = os.getlogin()


#--- Запись/Изменение имени юзера ---

def Rename():
    userRname = input("What your name? ")
    with open("DataBase/username.txt", "wt") as Userwrite:
        loginOfUs = Userwrite.write(userRname)
    with open("DataBase/username.txt", "r") as login:
        Login = login.read()
        print ("Welcome, "+ userRname)

#--- Вход ---


start = input("\n Hi, I'm Amelie. Start me? Press Y of N: ")

if start == "Y" or start == "y":
    print ("\n Salute! What I'm capable of, you can find out right now =D")
elif start == "N" or start == "n":
    print (" Think... Now you working BB =D")
    sys_exit()
elif start != "Y" or start != "N":
    while start != "Y" or start != "N":
        startFalse = input("Invalid syntax, enter Y or N pls: ")
        if startFalse == "Y" or startFalse == "y":
            print ("\n Salute! What I'm capable of, you can find out right now =D")
            break
        elif startFalse == "N" or startFalse == "n":
            print ("Think... Now you working BB =D")
            sys_exit()
            break
        elif startFalse != "Y" or startFalse != "y" or startFalse != "N" or startFalse != "n":
            print ("\n Try again =D")
            continue
else:
    while start == "":
        start_sec = input("Write Y or N pls: ")
        if start_sec == "Y" or start_sec == "y":
            print ("\n Salute! What I'm capable of, you can find out right now =D")
            break
        elif start_sec == "N" or start_sec == "n":
            print (" Think... Now you working BB =D")
            sys_exit()
            break
        elif not "Y" or "y" or "N" or "n" in start:
            print ("\n Try again!")
            continue

#--- Конец входа


userlogin = open("DataBase/username.txt", "r")
source = userlogin.read()
userlogin.close()

if source == "":
    Rename()

#--- Функция листа возможностей

def menu():
    while menu:
        print ( 100 * "_", "*")
        print ("\n Пока что я могу выполнять 4 функции ^-^ \n 1- I can try to guess your name. \n 2- If you wanted to go Enternet, I can help you. \n 3- Strong 18+ \n 4- Open Explorer")
        print (40 * "_")
        print ("\n 5- About Amelie ^-^ \n 6- Website of my creator")
        print ("\n ПСССС, если хочешь закрыть список, команда Stop вся твоя ^-^")
        canDoit = input ("\n Write number of string: ")

        canDo = canDoit.lower()
        if canDo == "1":
            print ("\n You're probably calling yourself: "+ username)
            
        elif canDo == "2":
            En = webbrowser.open('http://google.com', new=2)
            print ("I'm opened your browser ^-^")
            
        elif canDo == "3":
            En18 = webbrowser.open('https://rt.pornhub.com/', new=3)
            print ("I'm opened your browser, honey ^-^")
            
        elif canDo == "4":
            Ex = subprocess.Popen('explorer "C:\path\of\folder"')
            print ("\n--- Expolere was opened ---")
            invalid_input = False
        elif canDo == "5":
            with open("DataBase/about.txt", 'r') as file:
                print (" Reading...")
                print ("\n", file.readline())
            
        elif canDo == "6":
            Site = webbrowser.open('http://clear-sky.zz.vc', new=2)
            print ("\n Browser was opened =D")
        elif canDo == "stop":
            break
        elif canDo == "R":
            Rename()
        else:
            print ("I don't know, what are you doing =( ")


#--- Чат
while True:

    #--- Считывание данных из Базы ---
    with open("DataBase/hi_s.txt", "r") as fileHI:
        data = fileHI.read()
        massData = data.replace('\n', '')
        
        

    with open("DataBase/Synonym.txt", "r") as Sin:
        dataSin = Sin.read()
        massDataSin = dataSin.replace('\n', '')
        
    #--- Конец считывания ---


    quest = input("\n---> ")
    Input = quest.lower()
    # --- Input он же Quest на mobile Ver ---

    if Input in massData:
        fileHI = open("DataBase/hi_s.txt", "r")
        linelist = []
        for line in fileHI:
            linelist.append(line)
        choice = random.choice(linelist)
        fileHI.close()
        with open ("DataBase/username.txt", "r") as LoginTXT:
            userName = LoginTXT.read()
        print ("\n<--- "+ userName+ ", "+ choice)

    elif Input in massDataSin:
        QAN = open("DataBase/Expression.txt", "r")
        linelist =[]
        for line in QAN:
            linelist.append(line)
        choice = random.choice(linelist)
        print ("\n<--- "+ choice)

    elif Input == "list":
        menu()
