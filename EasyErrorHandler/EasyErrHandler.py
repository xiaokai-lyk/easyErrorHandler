#encoding=utf-8
import traceback
from typing import Any
import colorama
colorama.init(autoreset=True)

from .EasyErrCode import EasyErrCode

class EasyErrHandler:
    """
    A class that can help you to handle errors easily
    """
    def __init__(self,show_detail:str="all",autoUpdate=True):
        self.show_detail=show_detail
        self.autoUpdate=autoUpdate
        self.errColor=colorama.Fore.RED

    def output(self,content:str)->Any:
        return print(content)

    def errCatchDecorator(self,show_detail:str=None,errCodeObj:object=None,changeErrObj=None,errReturn=None):
        """
        A decorator to catch errors and show traceback without interrupt whole program.
        Example:
            import EasyErrorHandler as eeh
            myErrorCodes=eeh.EasyErrCode()
            myErrorHandler=eeh.EasyErrHandler()

            @myErrorHandler.errCatchDecorator()
            def a(x):
                return 3/x

            print(a(1))
            print(a(0))
            print("Program can still run.")
        """
        if show_detail == None:
            show_detail=self.show_detail
        if changeErrObj==None:
            changeErrObj=self.autoUpdate
        if errCodeObj==None:
            errCodeObj=EasyErrCode()
        if type(errCodeObj) != EasyErrCode:
            raise TypeError("type of parameter errCodeObj should be None or EasyErrCode, if you want to use wustom error code management class, please override EasyErrCode")
        if show_detail not in ["all","simple","none"]:
            raise ValueError("parameter show_detail should be in ['all','simple','none']")
        def decorator(func):
            funcName=func.__name__
            def warp(*args, **kwargs):
                try:
                    res = func(*args, **kwargs)
                except BaseException as e:
                    if show_detail=="all":
                        self.output(errCodeObj.add(
                            code=e,
                            msg="{}Error:{} in function \"{}\"  ,\r\n{}".format(self.errColor,str(e),funcName,traceback.format_exc()),
                            replace=changeErrObj)['res'].get(e)['res'])
                    elif show_detail=="simple":
                        self.output(errCodeObj.add(
                            code=e,
                            msg="{}Error:{} in function \"{}\" ".format(self.errColor,str(e),funcName),
                            replace=changeErrObj)['res'].get(e)['res'])
                    elif show_detail=="none":
                        self.output(errCodeObj.add(
                            code=e,
                            msg="{}An error happened in the function!".format(self.errColor),
                            replace=changeErrObj)['res'].get(e)['res'])
                    return errReturn

                else:
                    return res
            return warp
        return decorator

    def showErr():
        pass