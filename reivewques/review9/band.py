class Band(object):

    bandlist=[]
    def __init__(self,band):
        self.bandlist.append(band)
    @classmethod
    def Assignband(cls,band):
        cls.bandlist.extend(band)

    def setPrice(self,band):
        self.band = band
        if self.band in self.bandlist:
            for i in range(0,len(self.bandlist)):
                if band == self.bandlist[i]:
                    self.price= (1200 * i/2)+1200
                else:
                    continue
        else:
            print("enter the right Band value the available band are:" ,self.bandlist)
            del self.band



# bandvalue=Band('E00')
# bandvalue.Assignband(['E01','E02','E030','E04'])
# print(bandvalue.bandlist)
# bandvalue.setPrice("E02")
# print(bandvalue.getPrice())


