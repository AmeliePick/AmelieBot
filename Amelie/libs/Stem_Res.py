# -*- coding: utf-8 -*-

'''

Stemming module. From different words converts one thing. For example: mats - will Mat

Gets the final response from the query processing function and converts it

'''

import Stemmer


def Stemm(EditSearch):

    stemmer = Stemmer.Stemmer('russian')
    Getting = stemmer.stemWord(EditSearch)


    return Getting



