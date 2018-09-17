# -*- coding: utf-8 -*

# ======================= #
#   by AmeliePick. 2018   #
#  github.com/AmeliePick  #
# ======================= #

from sys import stdin, exit as sys_exit
import os, webbrowser, subprocess ,random

print ( 70 * "_")
print ("\t\t                         _ _       \n" +
       "\t\t    /\                  | (_)      \n" +
       "\t\t   /  \   _ __ ___   ___| |_  ___  \n" +
       "\t\t  / /\ \ | '_ ` _ \ / _ \ | |/ _ \ \n" +
       "\t\t / ____ \| | | | | |  __/ | |  __/ \n" +
       "\t\t/_/    \_\_| |_| |_|\___|_|_|\___| ")
print ( 70 * "_")

# ----- bot -----

# get current login username
g_username = os.getlogin()

# set username
def set_username():
    username = input("\n What is your name? > ")

    if (username != ""):
        with open("../DataBase/username.txt", "w") as writeUsername:
            writeUsername.write(username)
        print ("\n Welcome, "+ username + "!")
    else:
        print ("\n (!) Name can't be empty :D")
        set_username();

# ----- entry -----

start = input("\n Hi, I'm Amelie. Start me? Press [Y] of [N]: ")

while (True):
    if (start == "Y" or start == "y"):
        print ("\n Salute! What I'm capable of, you can find out right now =D")
        break
    elif (start == "N" or start == "n"):
        print ("\n Thinking... Now you are working, bye =D")
        sys_exit()
    else:
        start = input("\n (!) Try again - [Y] or [N]: ")
        continue

# ----- end of the entry -----

# read username from file in DB
usernameInFile = open("../DataBase/username.txt", "r")
username = usernameInFile.read()
usernameInFile.close()

# call function to set it if it's empty
if (username == ""):
    set_username()
else:
    print("\n Welcome, " + username + "!")

# ===== i will not go deeper, cmon. (c) Matt Fawkes ===== #

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
    with open("../DataBase/hi_s.txt", "r") as fileHI:
        data = fileHI.read()
        massData = data.replace('\n', '')



    with open("../DataBase/Synonym.txt", "r") as Sin:
        dataSin = Sin.read()
        massDataSin = dataSin.replace('\n', '')

    #--- Конец считывания ---


    quest = input("\n---> ")
    Input = quest.lower()
    # --- Input он же Quest на mobile Ver ---

    if Input in massData:
        fileHI = open("../DataBase/hi_s.txt", "r")
        linelist = []
        for line in fileHI:
            linelist.append(line)
        choice = random.choice(linelist)
        fileHI.close()
        with open ("../DataBase/username.txt", "r") as LoginTXT:
            userName = LoginTXT.read()
        print ("\n<--- "+ userName+ ", "+ choice)

    elif Input in massDataSin:
        QAN = open("../DataBase/Expression.txt", "r")
        linelist =[]
        for line in QAN:
            linelist.append(line)
        choice = random.choice(linelist)
        print ("\n<--- "+ choice)

    elif Input == "list":
        menu()
