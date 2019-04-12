class Nokia:
    def __init__(self, name, price):
        self._name = name
        self.price = price/2

    def setprice(self,price):
        self.price=price

    def getprice(self):
        return self.price*2

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name