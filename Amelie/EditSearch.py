# -*- coding: utf-8 -*-

import Stemmer, re

f = open ("../DataBase/social.txt", "r")

text = []

An = ""

def EditSearch(Input):


    

    for i in f:
        row = i.split(' @ ')

        if "Youtube" in i and ToAnswser == "Youtube":
                text.append(row[0])

        if "Search" in i:
                text.append(row[0])

    for item in text:
        if item in text and item in Input:

            An = Input.replace(item, '')

    #An = re.sub('[?!]', '', An)

    return An.lstrip()







    
