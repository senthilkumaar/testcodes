from abc import ABC, abstractmethod
class Area(ABC):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    @abstractmethod
    def calculate(self):
        pass

class squre(Area):
    def __init__(self, length, breath):
        super().__init__(length,breath)

    def calculate(self):
        self.area = self.length*self.length
        print("the squre area is :",self.area)


class rectangle(Area):
    def __init__(self, length, breath):
        super().__init__(length,breath)

    def calculate(self):

        area = self.length * self.breath
        print("the rectangle area is :", area)


squrearea=squre(10,20)
squrearea.calculate()
rectanglearea=rectangle(10,20)
rectanglearea.calculate()
