# -*- coding: utf-8 -*-
from libs.configParser import Print

'''
Request module for adding a program to the database

'''


def programmNotFound():
    print("<--- "+ Print("n_found"))
    print(Print("addPr"))
    AddProgramm = input("--> ")

    if AddProgramm == "Y" or  AddProgramm == "y":
        from .AddPr import AddProgramm

        AddProgramm()
    else:
        return 0