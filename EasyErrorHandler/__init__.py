#encoding=utf-8

import platform
from typing import  overload
from typing import Any
import colorama
colorama.init(autoreset=True)

import importlib

def dynamic_import(module_name):
    return importlib.import_module('.' + module_name, __name__)


def compatibilityCheck():
    if platform.system() != "Windows":
        print(colorama.Fore.RED+"Warning:Easy Error Handler should run well on other OSs, but it has only been tested on Windows.")

def UIavailable()->bool:
    try:
        ...#这个环境没有UI库，有网之后要装一下！
           #目前的想法是使用gradio做webUI
    except:
        ...
    else:
        ...
__version__:str="0.0.1"
__withUI__=UIavailable()

from .EasyErrHandler import *
from .EasyErrCode import *





def __init__():
    compatibilityCheck()