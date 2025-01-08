#encoding=utf-8
from dataclasses import dataclass



@dataclass
class DataStorer:
    pass
class EasyAnalyser():
    """
    Record errors and shortcomings and help developers to analyse them.
    Functions:
    Generate better trace back using a tree structure
    Collect data from EasyErrHandler
    """
    def __init__(self,data:dict={},settings:dict={}) -> None:
        self.data = data
        self.settings = settings
        
    def __str__(self) -> str:
        pass
    
    def __hash__(self) -> int:
        return hash([self.data,self.settings])
    def __call__(self) -> str:...
        #显示错误统计信息

    def load(self,source:dict,replace:bool=False) -> bool:
        if replace and self.locked==False :
            pass
        else:
            pass
    def __eq__(self, value: object) -> bool:
        if type(self)==type(value):
            return hash(self)==hash(value)
        elif type(value)==dict:
            return hash(self)==hash(EasyAnalyser(value))
        else:
            return False