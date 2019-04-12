class nokia:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class iphone(nokia):
    def __init__(self, name,price,model):
        super().__init__(name,price)
        self.model=model

    def addiphonevalue(self):
        self.price= self.price*2

class Micromax(nokia):
    def __init__(self, name,price,model):
        super().__init__(name,price)
        self.model=model

    def addiphonevalue(self):
        self.price= self.price*4


iphoneprice=iphone("Nokia 6", 2400, "I8")
iphoneprice.addiphonevalue()
print(iphoneprice.price)





