# -*- coding: utf-8 -*-



from sys    import executable as exe
from sys    import argv
from os     import execl


def restart() -> None:
    ''' Restart the application
    '''
    execl(exe, exe, *argv)

    return
