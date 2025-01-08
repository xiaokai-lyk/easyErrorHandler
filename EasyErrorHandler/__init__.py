#encoding=utf-8

"""
Created on 2025-01-07 14:51:40

@author: xk
@func: Initialize the module and help with auto-completion
"""

from dataclasses import dataclass
from logging import warning
import platform
import colorama
colorama.init(autoreset=True)


    

def compatibilityCheck():
    if platform.system() != "Windows":
        warning("Easy Error Handler should run well on other OSs, but it has only been tested on Windows")

def UIavailable()->bool:
    try:
        ...#这个环境没有UI库，有网之后要装一下！
           #目前的想法是使用flask做webUI
    except:
        ...
    else:
        ...

@dataclass
class Constants:
    __version__:str="0.0.1"
    __withUI__=UIavailable()


if __name__=="__main__":
    import sys
    warning("__init__ can not be ran directly")
    sys.exit(0)

from .EasyErrHandler import *
from .EasyErrCode import *




def __init__():
    compatibilityCheck()