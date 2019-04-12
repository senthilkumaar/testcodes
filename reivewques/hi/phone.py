# class nokia:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
#     def getprice(self):
#         return self.price
#
#
# class iphone(nokia):
#     def __init__(self, name,price):
#         self.name = name
#         self.price = price
#
#
#     def getprice(self):
#         price = self.price*2
#         return price
#
#
# nokiaprice = nokia("nokia3", 10000)
# print(nokiaprice.name)
# print(nokiaprice.price)
# print(nokiaprice.getprice())
#
# # iphoneprice = iphone("i7",)
# # print(iphoneprice.name)
# # #print(iphoneprice.price)
# # print(iphoneprice.getprice())
#
#
# #method 2
# iphoneprice = iphone("i7",nokiaprice.price)
# print(iphoneprice.name)
# print(iphoneprice.price)
# print(iphoneprice.getprice())



# class nokia:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def getprice(self):
#         return self.price*2
#
# class iphone(nokia):
#     def __init__(self, name):
#         nokia().__init__(name,price)
#
#     def getprice(self):
#         price = self.price
#         return price
#
# nokiaprice = nokia("nokia3", 10000)
# print(nokiaprice.name)
# print(nokiaprice.price)
# #print(nokiaprice.getprice())
# #method 2
# iphoneprice = iphone("i7")
# print(iphoneprice.name)
# # print(iphoneprice.price)
# print(nokiaprice.getprice())
#
# nokiaprice = nokia("nokia 6", 24000)
# print(nokiaprice.name)
# print(nokiaprice.price)
#
# iphoneprice = iphone("i8")
# print(iphoneprice.name)
# # print(iphoneprice.price)
# print(nokiaprice.getprice())
#
# nokiaprice.price=18000
# print(nokiaprice.getprice())

'''

# class nokia:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
#     def getprice(self):
#         return self.price
#
#
# class iphone(nokia):
#     def __init__(self, name):
#         self.name = name
#
#     def getprice(self):
#         price = nokiaprice.price*2
#         return price
#
# nokiaprice = nokia("nokia3", 10000)
# print(nokiaprice.name)
# print(nokiaprice.price)
# iphoneprice = iphone("i8")
# print(iphoneprice.name)
# # print(iphoneprice.price)
# print(iphoneprice.getprice())
'''


'''
class nokia:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def getprice(self):
        return self.price

class iphone(nokia):
    def __init__(self, name):
        self.name = name

    def getprice(self):
        return nokiaprice.price*2


nokiaprice = nokia("nokia3", 10000)
print(nokiaprice.name)
print(nokiaprice.price)
iphoneprice = iphone("i8")
print(iphoneprice.name)
print(iphoneprice.getprice())

'''


class nokia:
    def __init__(self, name, price):
        self._name=name
        self.nokiaprice = price/2

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def setprice(self,price):
        self.price=price

    def getprice(self):
        return self.price*2

class iphone(nokia):
    def __init__(self, name, price):
        super().__init__(name,price)

    def getprice(self):
        return self.price*2

    def setprice(self,price):
        self.price=price

    def getname(self):
        return self.name

    def setname(self, value):
        self.name = value

iphoneprice=iphone("i8",3600)
iphoneprice.name="nokia 6"
iphoneprice.setprice(20035)
# iphoneprice.setname("iphonex")
print("nokia phone name:",iphoneprice.name)
print("nokia phone price:", iphoneprice.price)
iphoneprice.setname("iphonex")
print("iphone phone name:",iphoneprice.getname())
print("iphone phone price:",iphoneprice.getprice())
