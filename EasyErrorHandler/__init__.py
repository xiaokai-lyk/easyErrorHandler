#encoding=utf-8

import traceback
import platform


if platform.system() != "Windows":
    print("Warning:Easy Error Code has only been tested on Windows.")


class EasyErrHandler:
    """
    A class that can help you to handle errors easily
    Example:

    eeh=EasyErrHandler()

    @eeh.errCatch()
    def a(x):
        return 3/x

    print(a(1))
    print(a(0))
    """
    def __init__(self,show_detail:str="all",initCodes:list=[],autoUpdate=True):
        self.code2msg={}
        self.show_detail=show_detail
        self.autoUpdate=autoUpdate
        for i in initCodes:
            self.code2msg[i['code']]=i['msg']

    def  __str__(self) -> str:
        return str({"type":type(self),"data":self.code2msg})

    def add(self,code,msg:str,replace=False):
        if replace:
            self.code2msg[code]=msg
            return {"success":True,"res":self}
        elif code not in dict.keys():
            self.code2msg[code]=msg
            return {"success":True,"res":self}
        else:
            return {"success":False,"res":self}

    def get(self,code):
        if code in self.code2msg.keys():    
            return {"success":True,"res":self.code2msg[code]}
        else:
            return {"success":False,"res":""}

    def errCatch(self,show_detail:str=None,errCodeObj:object=None,changeErrObj=None):
        if show_detail == None:
            show_detail=self.show_detail
        if changeErrObj==None:
            changeErrObj=self.autoUpdate
        if errCodeObj==None:
            errCodeObj=self
        if type(errCodeObj) != type(self):
            raise TypeError("type of parameter errCodeObj should be None or errCode")
        if show_detail not in ["all","simple","none"]:
            raise ValueError("parameter show_detail should be in ['all','simple','none']")
        def decorator(func):
            funcName=func.__name__
            def warp(*args, **kwargs):
                try:
                    res = func(*args, **kwargs)
                except BaseException as e:
                    if show_detail=="all":
                        return errCodeObj.add(code=e,msg="Error:{} in function \"{}\"  ,\r\n{}".format(str(e),funcName,traceback.format_exc()),replace=changeErrObj)['res'].get(e)['res']
                    elif show_detail=="simple":
                        return errCodeObj.add(code=e,msg="Error:{} in function \"{}\" ".format(str(e),funcName),replace=changeErrObj)['res'].get(e)['res']
                    elif show_detail=="none":
                        return errCodeObj.add(code=e,msg="An error happened in the function!",replace=changeErrObj)['res'].get(e)['res']
                else:
                    return res
            return warp
        return decorator
    def getall(self)->dict:
        return self.code2msg
