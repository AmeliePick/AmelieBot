# -*- coding: utf-8 -*


# === Username installation module ===

def set_username():
    username = input("\n What is your name? > ")

    if (username != ""):
        with open("../DataBase/username.txt", "w") as writeUsername:
            writeUsername.write(username)
        print ("\n Welcome, "+ username + "!")
    else:
        print ("\n (!) Name can't be empty :D")
        set_username();
