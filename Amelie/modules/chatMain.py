# -*- coding: utf-8 -*-

from .AICore        import chatOBJ
from .AIProcessing  import answer


def openChat(voice:str = "") -> str:
    # launch the chat
    chatOBJ.Enter(voice)
    chatOBJ.open_AI()

    # get answer
    result = answer(chatOBJ.getInput(), chatOBJ.getInputType(), chatOBJ.getDataSet_new())

    return result