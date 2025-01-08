#encoding=utf-8
from . import Constants

class EasyErrCode(Constants):
    def __init__(self,initCodes:dict=[],**kwargs):
        """
        MISSING!
        Args:
        - initCodes : Some preloaded codes. eg:{500,"internal error!","unknown":"unknown error!"}
        - kwargs : Other unimportant arguments.
            - default_msg : Return this message cannot match any saved code.
        """
        self.code2msg={}
        for i in initCodes:
            self.code2msg[i['code']]=i['msg']
        self.settings = kwargs

    def  __str__(self) -> str:
        return str({"type":type(self),"data":self.code2msg})

    def add(self,code,msg:str,replace=False):
        if replace:
            if self.exist(code):
                old_msg=self.code2msg[code]
                self.code2msg[code]=msg
                return {"success":True,"res":self
                        ,"msg":f"Code {code} already exists, it was{old_msg}, and it is replaces."}
            else:
                self.code2msg[code]=msg
                return {"success":True,"res":self,"msg":f"{code} is successfully added!"}
        else:
            return {"success":False,"res":self
                    ,"msg":f"Code {code} already exists, use `replace=True` to update it."}

    def exist(self,code):
        if code in self.code2msg.keys():   
            return True
        else:
            return False

    def get(self,code,default_msg:str=None):
        """
        * If argument 'default_msg' is given and is not None, the default massage 
        * that was set when initialize won't work!
        """
        if default_msg==None:
            default_msg = self.settings.get("default_msg",None)

        if self.exist(code):    
            return {"success":True,"res":self.code2msg[code]}
        elif default_msg!=None:
            return {"success":False,"res":default_msg}
        else:
            return {"success":False,"res":""}
