# -*- coding: utf-8 -*-
from libs.configParser import Parser

'''
Request module for adding a program to the database

'''


def except_for_add():
    print("<--- "+ Parser("n_found"))
    print(Parser("addPr"))
    AddProgramm = input("--> ")

    if AddProgramm == "Y" or  AddProgramm == "y":
        from AddPr import AddProgramm
        AddProgramm()
    else:
        return 0