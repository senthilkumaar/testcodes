from abc import ABC, abstractmethod


class vehicle(ABC):

    def __init__(self, color, engine, tankcapacity):
        self.color = color
        self.engine = engine
        self.tankcapacity = tankcapacity

    @abstractmethod
    def startengine(self):
        pass


class twoWheeler(vehicle):
    def __init__(self, color, engine, tankcapacity, types, number, milage):
        self.types = types
        self.number = number
        self.milage = milage
        vehicle.__init__(self, color, engine, tankcapacity)

    def startengine(self):
        print("two wheel riding")

    def displaySeat(self):
        print("two Seater")


class fourWheeler(vehicle):
    def __init__(self, color, engine, tankcapacity, fueltype, number, milage):
        self.__childlock = "Yes"# private variable
        self.fueltype = fueltype
        self.number = number
        self.milage = milage
        vehicle.__init__(self, color, engine, tankcapacity)

    def startengine(self):
        print("four wheel riding")

    def displaySeat(self):
        print("four Seater")


class batMobile(fourWheeler, twoWheeler):
    noofvehicle = 0

    def __init__(self, color, engine, tankcapacity, types, fueltype, number, milage):
        twoWheeler.__init__(self, color, engine, tankcapacity, types, number, milage)
        fourWheeler.__init__(self, color, engine, tankcapacity, fueltype, number, milage)
        batMobile.noofvehicle += 1

    @classmethod
    def specialbatmobile(cls, color, engine, tankcapacity, types, fueltype, number, milage, weapons):
        cls.weapons = weapons
        return cls(color, engine, tankcapacity, types, fueltype, number, milage)

    def startengine(self):
        print("BAT wheel riding")

    def displaySeat(self):
        print("two BAT Seater")

    def __add__(self, other):
        return "" + self.color + "riding with" + other.color

    @staticmethod
    def vehiclesOwned(a, b):
        print("no of owned:", batMobile.noofvehicle)
        return a + b


G1 = twoWheeler("red", 350, 14, "Super", 1993, 25)
G2 = fourWheeler("Red", 1130, 30, "petrol", 1234, 24)
G3 = batMobile("black", 3000, 50, "Super", "Disel", 0000, 13)
G4 = batMobile("cameflogue", 3000, 50, "Super", "Disel", 0000, 13)
G5 = batMobile("radiantblue", 3000, 50, "Super", "Disel", 0000, 13)
G6 = batMobile.specialbatmobile("radiantblue", 3000, 50, "Super", "Disel", 0000, 13, "Rocket Launcher")
print(G1.color)
print(G2.tankcapacity)
print(G3.fueltype)
G3.startengine()
G1.displaySeat()
G2.displaySeat()
G3.displaySeat()
# print(batMobile.vehiclesOwned())
print(G3 + G2)
print(G6.weapons)
print(G2._fourWheeler__childlock)
print(batMobile.vehiclesOwned(2, 3))

