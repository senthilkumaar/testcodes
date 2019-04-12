class Car:
    def __init__(self,name,milage):
        self.name=name
        self.milage=milage

class Audi(Car):
    features = []

    def __init__(self, name, milage, feature):
        super().__init__(name,milage)
        self.features.append(feature)

    def addfeature(self, feature):
        self.features.append(feature)
        print (self.features)

    def removefeature(self, feature):
        try:
            self.features.remove(feature)
            print (self.features)
        except Exception as e:
            print(e)


audidetails=Audi("A8",24,'Airbag')
audidetails.addfeature("HDR")
audidetails.removefeature("HDR")
audidetails.removefeature("Push Back")

# setattr(Car,'color',"color")
# setattr(Audi,'color','yellow')
#
# print(audidetails.color)
#
# audidetail=Audi("A6",20,'tublesstire')
# print(audidetail.color)
