# -*- coding: utf-8 -*-

'''
Request module for adding a program to the database

'''


def except_for_add():
    print("<--- I have not found such a program")
    AddProgramm = input("=D can you add it to my database and I'll open it next time\n Add a program? [Y] or [N]: ")

    if AddProgramm == "Y" or  AddProgramm == "y":
        from AddPr import AddProgramm
        AddProgramm()
    else:
        return 0