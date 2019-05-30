# -*- coding: utf-8 -*-

'''
Module for request objects, but this is not a pattern command implementation.

'''



class answer:
    ''' The class is a singleton

    num --- for request processing logic
    if num == 0 > This means exit from the application.

    output --- text for answer to user

    '''
    num = 1
    output = ''
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(answer, cls).__new__(cls)
            return cls.instance
            
        return cls.instance


    def setNum(self, num):
        self.num = num


    def setText(self, txt):
        self.output = txt


    def getNum(self):
        return self.num


    def getOut(self):
        return self.output

Output = answer()