'''class Celsius:
    def __init__(self, temp = 0):
        self._temper = temp

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temper

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temper = value

    @temperature.deleter
    def temperature(self):
        print ("deleting the instance variable temperature")
        del self._temper

c1=Celsius(20)
print(c1.temperature)
c1.temperature=-274
print(c1.temperature)
del c1.temperature
print(c1.temperature)

'''

class Celsius:
    def __init__(self, temp=0):
        self._temper = temp

    def to_fahrenheit(self):
        return (self._temper * 1.8) + 32

    def get_temperature(self):   ####accesser
        print("Getting value")
        return self._temper

    def set_temperature(self, value):  ####mutator
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temper = value


C1=Celsius(100)
print(C1.to_fahrenheit())
print(C1.get_temperature())
print(C1.set_temperature(-700))