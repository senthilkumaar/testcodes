print("this is the first line")
class animals:
    def __init__(self,legs):
        self.legs = legs

    @property
    def test(self):
        return self.legs

class herbivor(animals):
    def __init__(self, legs,type):
        self.type = type
        animals.__init__(self, legs)

class carnivorus(herbivor):      #
    def __init__(self,legs,type):
        herbivor.__init__(self,legs,type)

class scavengers(carnivorus):
    def __init__(self,legs,type):
        carnivorus.__init__(self, legs, type)

class omnivorus(herbivor,carnivorus): # multiple inheritance
    def __init__(self,legs,type):
        herbivor.__init__(self,legs,type)
        carnivorus.__init__(self,legs,type)


if __name__=='__main__':
    omni = omnivorus(4, "fly")
    print(omni.type, omni.legs)
    carni = carnivorus(4, "walk")
    print(carni.legs, carni.type)
    scav=scavengers(4,'walk and fly')
    print(scav.type,scav.legs)

    animalslegs=animals(4)
    print(animalslegs.test)
