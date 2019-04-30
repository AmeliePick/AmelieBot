# -*- coding: utf-8 -*-

'''
Log file maintenance
'''

from traceback import format_exc


def LogWrite():
    with open("Amelie_log.txt", 'a') as log:
        log.write(10*'-'+'\n'+ str(format_exc()+'\n'))