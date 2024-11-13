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
        ...#�������û��UI�⣬����֮��Ҫװһ�£�
           #Ŀǰ���뷨��ʹ��gradio��webUI
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