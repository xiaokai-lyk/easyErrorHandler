#encoding=utf-8
class EasyErrAnalyser:
    """
    Record errors and help developers to analyse them.
    Functions:
    Generate better trace back using a tree structure
    Collect data from EasyErrHandler
    """
    def __init__(self,source:dict={},locked:bool=False) -> None:
        self.locked=locked

    def __str__(self) -> str:
        pass
    
    def __hash__(self) -> int:...
        #未完成！
    def __call__(self) -> str:...
        #显示错误追踪信息

    def load(self,source:dict,replace:bool=False) -> bool:
        if replace and self.locked==False :
            pass
        else:
            pass
    def __eq__(self, value: object) -> bool:
        if type(self)==type(value):
            return hash(self)==hash(value)
        elif type(value)==dict:
            return hash(self)==hash(EasyErrAnalyser(value))
        else:
            return False