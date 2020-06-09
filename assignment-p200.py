from abc import ABC, abstractmethod

class Thing(ABC):
    def __init__(self,name):
        self.name = name
    def getName(self):
        print(self.name)
    @abstractmethod
    def getSides(self,sides):
        pass

class Shape(Thing):
    def getSides(self,sides):
        print(f"I have {sides} sides!")

if __name__ == "__main__":
    altj = Shape("Triangle")
    altj.getName()
    altj.getSides(3)