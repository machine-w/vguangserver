import sys 
sys.path.append("..") 
from .resultinterface import OperResult

class ToList(OperResult):
    def __init__(self,SimpleRate,**extendInfor):
        super().__init__(SimpleRate,**extendInfor)
        self.dataList =[]
    def read(self):
        print(self.dataList)
    def write(self,step,stepTime,curTime,dataType,data):
        self.dataList.append(data.numpy())
    def clear(self):
        pass

if __name__ == "__main__":
    r = ToList(100)
    print(isinstance(r, OperResult))