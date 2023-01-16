"""
Abstraction : which is represent only few infomation

            not allocated background inforamation

if we want to be 


"""

from abc import ABC, abstractmethod

class RBI(ABC):
    @abstractmethod
    def display(self):
        pass

class SBI(RBI):
    def display(self):
        print("SBI class")
        return