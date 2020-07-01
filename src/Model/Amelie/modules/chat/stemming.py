# -*- coding: utf-8 -*-

''' Stemming module
From different words converts one thing. For example: mats - will mat.

Works only on russian language.

'''

from Stemmer import Stemmer


def stemming(EditSearch: str) -> str:

    stemmer = Stemmer('russian')

    return stemmer.stemWord(EditSearch)
