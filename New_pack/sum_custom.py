def sum_c(a,b):
    """sum to variables"""
    return a+b

class herbivor():
    def __init__(self, legs,type):
        self.type = type

    def printall(self):
        print("success")

    @classmethod
    def diff_way(cls,legs,type):
        return cls(legs,type)