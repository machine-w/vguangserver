from abc import ABCMeta, abstractmethod

class Verify(metaclass=ABCMeta):
    def __init__(self,url):
        self.url = url
    @abstractmethod
    def checkQR(self,qrCode):
        return 0