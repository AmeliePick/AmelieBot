# -*- coding: utf-8 -*

from libs.configParser import Parser

# === Username installation module ===

def set_username():
    print(Parser("getName"))
    username = input("> ")

    if (username != ""):
        with open("../DataBase/username.txt", "w") as writeUsername:
            writeUsername.write(username)
        print ("\n Welcome, "+ username + "!")
    else:
        print (Parser("emptyName"))
        set_username();
