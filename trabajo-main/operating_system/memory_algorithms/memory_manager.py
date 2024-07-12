from utilities.queue import Queue
from hardware.hardware import HARDWARE

class MemoryManager:

    def __init__(self, kernel):
        self.__kernel = kernel
        self.__hueco_list = Queue()


   
    @property
    def kernel(self):
        return self.__kernel 


    @property
    def allHueco(self):
        return self.__hueco_list
    
    @property
    def hardware(self):
        return HARDWARE
    
    