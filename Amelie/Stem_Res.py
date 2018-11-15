# -*- coding: utf-8 -*-

from EditSearch import EditSearch

import Stemmer


def Stemm(EditSearch):

    stemmer = Stemmer.Stemmer('russian')
    Getting = stemmer.stemWord(EditSearch)


    return Getting



