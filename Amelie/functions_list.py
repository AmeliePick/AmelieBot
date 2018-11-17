# -*- coding: utf-8 -*


#UPD 17.11.2018/19:00 
#It doesn't work at the time of publication, I'll see what I can do about it

import os, webbrowser, subprocess ,random, re
# get current login username
g_username = os.getlogin()

def menu():
    while menu:
        print ( 100 * "_", "*")
        print ("\n So far I can perform 4 functions ^-^ \n 1- I can try to guess your name. \n 2- If you wanted to go Enternet, I can help you. \n 3- Strong 18+ \n 4- Open Explorer \n 5- Play in games")
        print (40 * "_")
        print ("\n A- About Amelie ^-^ \n W- Website of my creator")
        print ("\n PSST, if you want to close the list, the \"Stop\" command is all yours.  ^-^")
        canDoit = input ("\n Write number of string: ")

        canDo = canDoit.lower()
        if canDo == "1":
            print ("\n You're probably calling yourself: "+ g_username)

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
            plays = input ("\n What are we playing? \n Cities[1] or ...[2]: ")
            if plays == "1":
                import Games
                Games.main()
            elif plays == "2":
                print ("\nI'm working on it")
            
        elif canDo == "A":
            with open("DataBase/about.txt", 'r') as file:
                print (" Reading...")
                print ("\n", file.readline())

        elif canDo == "W":
            Site = webbrowser.open('http://clear-sky.zz.vc', new=2)
            print ("\n Browser was opened =D")
        elif canDo == "stop":
            break
        elif canDo == "R":
            set_username()
        else:
            print ("I don't know, what are you doing =( ")
