#encoding=utf-8
class EasyErrCode:
    def __init__(self,initCodes:list=[]):
        self.code2msg={}

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
