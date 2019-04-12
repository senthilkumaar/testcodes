from nokiaphone import Nokia
class iphone(Nokia):
    def __init__(self, name, price):
        super().__init__(name, price)

    def setprice(self,price):
        self.price=price

    def getprice(self):
        return self.price*2

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name


iphoneprice=iphone("i8",3600)
nokiaprice=Nokia('Nokiac6',1200)
print("Phone name:",nokiaprice.name)
print("Phone price:",nokiaprice.getprice())
print("***********************************************")
print("iphone name:",iphoneprice.getname())
print("iphone price:",iphoneprice.getprice())
iphoneprice.name="nokiac3010"
print("updated nokia name :",iphoneprice.name)
print("updated nokia price :",iphoneprice.price)
iphoneprice.setprice(6000)
print("updated iphone price :",iphoneprice.getprice())
print("nokiaphone price after setting price:",iphoneprice.price)
print("***********************************************")
iphoneupdated=iphone("i10",100000)
print("iphone name:",iphoneupdated.getname())
print("iphone price:",iphoneupdated.getprice())
print("nokia phone price:",iphoneupdated.price )
print(iphoneprice.getname())
iphoneprice.name="nokiac3000"
print(iphoneprice.name)
print(iphoneprice.price)
iphoneprice.setname("iphonex")
print(iphoneprice.getname())
print(iphoneprice.getprice())

